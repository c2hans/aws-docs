---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/mutual-renew.html
---

# Renew your server certificate for AWS Client VPN
<a name="mutual-renew"></a>

You can renew and re-import a Client VPN server certificate that has expired. Depending on the version of OpenVPN easy-rsa that you're using, the procedure will vary. See [Easy-RSA 3 Certificate Renewal and Revocation Documentation](https://github.com/OpenVPN/easy-rsa/blob/master/doc/EasyRSA-Renew-and-Revoke.md) for more details.

**To renew your server certificate**

1. Do **one** of the following:
   + Easy-RSA version 3.1.x

     1. Run the certificate renew command.

       ```
       $ ./easyrsa renew server nopass
       ```
   + Easy-RSA version 3.2.x

     1. Run the expire command.

        ```
        $ ./easyrsa expire server
        ```

     1. Sign a new certificate.

        ```
        $ ./easyrsa --san=DNS:server sign-req server server
        ```

1. Create a custom folder, copy the new files to it, then navigate into the folder.

   ```
   $ mkdir ~/{{custom_folder2}}
   $ cp pki/ca.crt ~/{{custom_folder2}}/
   $ cp pki/issued/server.crt ~/{{custom_folder2}}/
   $ cp pki/private/server.key ~/{{custom_folder2}}/
   $ cd ~/{{custom_folder2}}/
   ```

1. Import the new files to ACM. Be sure to import them in the same Region as the Client VPN endpoint.

   ```
   $ aws acm import-certificate \
       --certificate fileb://server.crt \
       --private-key fileb://server.key \
       --certificate-chain fileb://ca.crt \
       --certificate-arn arn:aws:acm:{{region}}:{{123456789012}}:certificate/{{12345678-1234-1234-1234-12345678901}}
   ```
