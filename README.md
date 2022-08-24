# ssti_payload_generator
Basic SSTI java based payload generator

Please note that the server didn't ban some characters, this payload may not work based on the characters baned.

![image](https://user-images.githubusercontent.com/15212130/186422425-fda6d84e-f56b-437f-89ef-4f4351d77716.png)


#### The payload generator is inside the ssti_payload(command) function

#### Parse web/path to inject the payload and the command you want to convert to java payload (ints that will be interpreted as ASCII and therefore executed).

#### Based in Spring, basic java SSTI templates

## Cases of use I.E:

#### You can grab SSH Keys with 'cat ~/.ssh/id_rsa' and achieve SSH Sessions

#### You can upload a nc and achieve bind/reverse shell
