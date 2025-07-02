#clonar o repositorio r.
git clone https://github.com/CienciaDeDadosUFF/python.github.io.git

#verificar status dos arquivos
git status
#versao resumida:??=nao rastr,A=Stagged,M=Modificado
git status -s

#rastrear novos arquivos
git add <nome do arquivo>

#adicionar todos arq. mod. para staged
git add .

#Realizar o commit comentado
git commit -m "Comentários aqui"

#Para atualizar seu branch teste local:
git pull origin teste

#Para enviar suas alterações para o teste:
git push origin teste

#atualizar arquivos locais
git pull 

#enviar commit para github
git push

#Para mudar para o branch teste (nosso branch de trabalho):
git checkout teste
