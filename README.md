## 🎰 sorteio-para-instagram

Realizando sorteio para Instagram com Python e Selenium através do terminal. 

#

### 📑 Versões das tecnologias usadas:

<table>
  <tr>
    <td>Python</td>
    <td>Selenium</td>    
  </tr>
  <tr>
    <td>3.*</td>
    <td>4.3</td>
  </tr>
</table>

#

### 🔨 Instalando o projeto:

- Clone o repositório:
```
git clone https://github.com/RakelMacedo/sorteio-para-instagram.git
```

- Crie seu ambiente virtual:
```
python3 -m venv venv
```

- E ative seu ambiente virtual:
```
source venv/bin/activate
```

#

### 🛠️ Abrir e rodar o projeto:

- Instale as depencências:
```
pip install -r requirements.txt
``` 

- O Selenium requer um driver para fazer interface com o navegador. Seguem links para alguns dos drivers de navegador mais populares:

<table border="1" class="docutils">
<colgroup>
<col width="16%" />
<col width="84%" />
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Chrome</strong>:</td>
<td><a class="reference external" href="https://sites.google.com/chromium.org/driver/">https://sites.google.com/chromium.org/driver/</a></td>
</tr>
<tr class="row-even"><td><strong>Edge</strong>:</td>
<td><a class="reference external" href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/</a></td>
</tr>
<tr class="row-odd"><td><strong>Firefox</strong>:</td>
<td><a class="reference external" href="https://github.com/mozilla/geckodriver/releases">https://github.com/mozilla/geckodriver/releases</a></td>
</tr>
<tr class="row-even"><td><strong>Safari</strong>:</td>
<td><a class="reference external" href="https://webkit.org/blog/6900/webdriver-support-in-safari-10/">https://webkit.org/blog/6900/webdriver-support-in-safari-10/</a></td>
</tr>
</tbody>
</table>

Depois de baixar o driver de acordo com seu sistema operacional, faça o uplode do mesmo na raiz do projeto. 
No meu caso, esse arquivo em questão é o 'chromedriver' referente a versão mais recente do Driver do Chrome no momento. 

Sinta-se a vontade para exclui-lo quando der o Fork no código, pois provavelmente esta versão já terá sido ultrapassada e baixando o seu próprio driver ele será desnecessário. Priorize sempre a versão mais recente ;)

#

### ✅ Pronto! Você esta pronto para rodar o código! =)

#

### Exemplo de uso: 

- Execute o código:
```
python3 code.py
```
<br>

```
| Sorteio do Instagram! ><

Carregando Instagram
Por favor aguarde...

Informe seu usúario: me.user
```

```
(Por segurança, não conseguimos ver a sua senha)
Informe sua senha: 
```

```
Logando, aguarde... \ / \ / \ / \ /
```

```
Login realizado com sucesso!

Informe a url da publicação do sorteio:
>>> https://www.instagram.com/p/url_da_pub_que_deseja_sortear_o_user/
```

```
Estamos carregando o post, por favor aguarde.

Terminamos de carregar todos os comentários!
Agora vamos pegar todos os usuários e apagar os duplicados para o sorteio,
Por favor, aguarde mais um pouco...
```

```
Carregamos todos os comentários, tiramos os duplicados e sorteamos o vencedor.

O vencedor do sorteio é -user_tal- !!!

Obrigado por utilizar nosso programa, volte sempre! ;)
```
