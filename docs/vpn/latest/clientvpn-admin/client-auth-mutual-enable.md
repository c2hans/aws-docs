---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-auth-mutual-enable.html
---

# Enable mutual authentication for AWS Client VPN
<a name="client-auth-mutual-enable"></a>

You can enable mutual authentication in Client VPN in either Linux/MacOS or Windows.

------
#### [ Linux/macOS ]

The following procedure uses OpenVPN easy-rsa to generate the server and client certificates and keys, and then uploads the server certificate and key to ACM. For more information, see the [Easy-RSA 3 Quickstart README](https://github.com/OpenVPN/easy-rsa/blob/v3.0.6/README.quickstart.md).

**To generate the server and client certificates and keys and upload them to ACM**

1. Clone the OpenVPN easy-rsa repo to your local computer and navigate to the `easy-rsa/easyrsa3` folder.

   ```
   $ git clone https://github.com/OpenVPN/easy-rsa.git
   ```

   ```
   $ cd easy-rsa/easyrsa3
   ```

1. Initialize a new PKI environment.

   ```
   $ ./easyrsa init-pki
   ```

1. To build a new certificate authority (CA), run this command and follow the prompts.

   ```
   $ ./easyrsa build-ca nopass
   ```

1. Generate the server certificate and key.

   ```
   $ ./easyrsa --san=DNS:server build-server-full server nopass
   ```

1. Generate the client certificate and key.

   Make sure to save the client certificate and the client private key because you will need them when you configure the client.

   ```
   $ ./easyrsa build-client-full client1.domain.tld nopass
   ```

   You can optionally repeat this step for each client (end user) that requires a client certificate and key.

1. Copy the server certificate and key and the client certificate and key to a custom folder and then navigate into the custom folder.

   Before you copy the certificates and keys, create the custom folder by using the `mkdir` command. The following example creates a custom folder in your home directory.

   ```
   $ mkdir ~/{{custom_folder}}/
   $ cp pki/ca.crt ~/{{custom_folder}}/
   $ cp pki/issued/server.crt ~/{{custom_folder}}/
   $ cp pki/private/server.key ~/{{custom_folder}}/
   $ cp pki/issued/client1.domain.tld.crt ~/{{custom_folder}}
   $ cp pki/private/client1.domain.tld.key ~/{{custom_folder}}/
   $ cd ~/{{custom_folder}}/
   ```

1. Upload the server certificate and key and the client certificate and key to ACM. Be sure to upload them in the same Region in which you intend to create the Client VPN endpoint. The following commands use the AWS CLI to upload the certificates. To upload the certificates using the ACM console instead, see [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the *AWS Certificate Manager User Guide*.

   ```
   $ aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt
   ```

   ```
   $ aws acm import-certificate --certificate fileb://client1.domain.tld.crt --private-key fileb://client1.domain.tld.key --certificate-chain fileb://ca.crt
   ```

   You do not necessarily need to upload the client certificate to ACM. If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client when you create the Client VPN endpoint. In the steps above, the same CA has been used to create both certificates. However, the steps to upload the client certificate are included for completeness.

------
#### [ Windows ]

The following procedure installs Easy-RSA 3.x software and uses it to generate server and client certificates and keys.

**To generate server and client certificates and keys and upload them to ACM**

1. Open the [EasyRSA releases](https://github.com/OpenVPN/easy-rsa/releases) page and download the ZIP file for your version of Windows and extract it.

1. Open a command prompt and navigate to the location that the `EasyRSA-3.x` folder was extracted to.

1. Run the following command to open the EasyRSA 3 shell.

   ```
   C:\Program Files\EasyRSA-3.x> .\EasyRSA-Start.bat
   ```

1. Initialize a new PKI environment.

   ```
   # ./easyrsa init-pki
   ```

1. To build a new certificate authority (CA), run this command and follow the prompts.

   ```
   # ./easyrsa build-ca nopass
   ```

1. Generate the server certificate and key.

   ```
   # ./easyrsa --san=DNS:server build-server-full server nopass
   ```

1. Generate the client certificate and key.

   ```
   # ./easyrsa build-client-full client1.domain.tld nopass
   ```

   You can optionally repeat this step for each client (end user) that requires a client certificate and key.

1. Exit the EasyRSA 3 shell.

   ```
   # exit
   ```

1. Copy the server certificate and key and the client certificate and key to a custom folder and then navigate into the custom folder.

   Before you copy the certificates and keys, create the custom folder by using the `mkdir` command. The following example creates a custom folder in your C:\\ drive.

   ```
   C:\Program Files\EasyRSA-3.x> mkdir C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\ca.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\issued\server.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\private\server.key C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\issued\client1.domain.tld.crt C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> copy pki\private\client1.domain.tld.key C:\{{custom_folder}}
   C:\Program Files\EasyRSA-3.x> cd C:\{{custom_folder}}
   ```

1. Upload the server certificate and key and the client certificate and key to ACM. Be sure to upload them in the same Region in which you intend to create the Client VPN endpoint. The following commands use the AWS CLI to upload the certificates. To upload the certificates using the ACM console instead, see [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the *AWS Certificate Manager User Guide*.

   ```
   aws acm import-certificate \
       --certificate fileb://server.crt \
       --private-key fileb://server.key \
       --certificate-chain fileb://ca.crt
   ```

   ```
   aws acm import-certificate \
       --certificate fileb://client1.domain.tld.crt \
       --private-key fileb://client1.domain.tld.key \
       --certificate-chain fileb://ca.crt
   ```

   You do not necessarily need to upload the client certificate to ACM. If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client when you create the Client VPN endpoint. In the steps above, the same CA has been used to create both certificates. However, the steps to upload the client certificate are included for completeness.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
