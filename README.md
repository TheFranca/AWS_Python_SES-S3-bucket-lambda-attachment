Para esse script rodar é necessário que você tenha instalado o AWS SDK em sua máquina e que suas credenticiais estejam no arquivo 'credential', o qual fica dentro do diretório: seu_diretório/.aws/credentials (no windows).

Por exemplo, o diretório do meu 'credentials' fica em C:\Users\T.I\.aws\credentials seu diretório vai variar de acordo de onde você instalar o SDK e do seu sistema operacional.

Também será necessário fazer a configuração do SES dentro da plataforma da Amazon: https://sa-east-1.console.aws.amazon.com/ses/home?region=sa-east-1
A configuração do SES é bem simples, basta verificar o endereço de email para receber/enviar emails