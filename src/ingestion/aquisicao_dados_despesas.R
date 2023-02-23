library(dplyr)
library(readxl)

###############  Aquisicao de dados ###############################################################
municipios <- read_excel("Municipios_DivisaoRegional.xlsx")
municipios <-as.data.frame(municipios)

n.muni <- nrow(municipios)
  
inicio = 1
for (i in inicio:n.muni ){
  
cidade <- municipios[i,2]

# Baixar o arquivo
url <- paste("https://transparencia.tce.sp.gov.br/sites/default/files/csv/despesas-",cidade,"-2020.zip", sep = "") 

# Nome do arquivo zip
arquivo <- paste("despesas-",cidade,"-2020.zip", sep = "")

# Nome do arquivo csv
arquivo.csv <- paste("despesas-",cidade,"-2020.csv", sep = "")

# Download para a pasta zip.files
arquivo.zip <- paste0(getwd(),"/zip.files/",arquivo)
download.file(url, arquivo.zip)

# Extrai arquivo csv na subpasta "csv"
dirextr <- paste0(getwd(),"/csv.files")
unzip(zipfile = arquivo.zip, exdir = dirextr)

}

##### Leitura dos dados dos arquivos csv, obtencao de ids de fornecedores ###################

dirextr <- paste0(getwd(),"/csv.files")

n.muni <- nrow(municipios)

inicio = 1

for (i in inicio:n.muni ){
  cidade <- municipios[i,2]
  arquivo.csv <- paste("despesas-",cidade,"-2020.csv", sep = "")
  
  file.dados <- paste0(dirextr,"/",arquivo.csv)
  dados <- read.csv2(file.dados)
  
  empresas.alim <- dados %>%
           filter (ds_subfuncao_governo %in% c("ALIMENTAÇÃO E NUTRIÇÃO")) %>%
           filter (ds_despesa != "FOLHA DE PAGAMENTO")
  
  empresas <- empresas.alim %>% select(identificador_despesa,ds_despesa)
  empresas <- unique(empresas)
  if (i == 1) {
    lista <- empresas
  } else {
    lista <- rbind(lista,empresas)
  } 
}

lista <- unique(lista)
lista.id <- lista$identificador_despesa
lista.id <- unique(lista.id)

##### Obtendo todos os fornecimentos dos ids na lista #####

dirextr <- paste0(getwd(),"/csv.files")

n.muni <- nrow(municipios)

inicio = 1

for (i in inicio:n.muni ){
  cidade <- municipios[i,2]
  regiao <- municipios[i,1]
  
  arquivo.csv <- paste("despesas-",cidade,"-2020.csv", sep = "")
  
  file.dados <- paste0(dirextr,"/",arquivo.csv)
  dados <- read.csv2(file.dados)
  dados$regiao <- regiao
  
  dados.muni <- dados[dados$identificador_despesa %in% lista.id,]
 
  if (i == 1) {
    df.regiao <- dados.muni
  } else {
    df.regiao <- rbind(df.regiao,dados.muni)
  } 
}
 
write.csv2(df.regiao,file = "regiao_campinas_2020.csv",row.names = FALSE)
#################################################################

table(df.regiao$ds_subfuncao_governo)
