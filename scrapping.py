from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://engeplusinfo.com/SAC/')
sleep(1)

#acessando a página do SAC
navegador.find_element_by_xpath('//*[@id="txtEmpresa"]').send_keys('065') 

navegador.find_element_by_xpath('//*[@id="txtUsuario"]').send_keys('getulio') 

navegador.find_element_by_xpath('//*[@id="txtSenha"]').send_keys('Suporteweb#1')

navegador.find_element_by_xpath('//*[@id="btEntrar"]').click() 
sleep(0.5)

#acessando o menu de OSs
navegador.find_element_by_xpath('//*[@id="menuitem_Solicitacões"]/p').click()

navegador.find_element_by_xpath('//*[@id="menuitemexpand_Solicitacões"]/a[1]').click()

navegador.find_element_by_xpath('//*[@id="btFiltro"]').click()

navegador.find_element_by_xpath('//*[@id="dropTipoBusca"]').click()

navegador.find_element_by_xpath('//*[@id="dropStatus"]').click()

navegador.find_element_by_xpath('/html/body/form/div[6]/div/div/div/div/div[2]/div[1]/div[1]/div/select/option[3]').click()
                                
navegador.find_element_by_xpath('//*[@id="dropModulo"]').click()

navegador.find_element_by_xpath('/html/body/form/div[6]/div/div/div/div/div[2]/div[1]/div[2]/div/select/option[14]').click()

navegador.find_element_by_xpath('//*[@id="btBuscar"]').click()

#finalizado
