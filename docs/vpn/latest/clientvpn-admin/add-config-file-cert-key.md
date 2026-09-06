---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/add-config-file-cert-key.html
---

# Add the AWS Client VPN client certificate and key information for mutual authentication
<a name="add-config-file-cert-key"></a>

If your Client VPN endpoint uses mutual authentication, you must add the client certificate and the client private key to the .ovpn configuration file that you download.

You cannot modify the client certificate when you use mutual authentication.

**To add the client certificate and key information (mutual authentication)**
You can use one of the following options.

(Option 1) Distribute the client certificate and key to clients along with the Client VPN endpoint configuration file. In this case, specify the path to the certificate and key in the configuration file. Open the configuration file using your preferred text editor, and add the following to the end of the file. Replace {{/path/}} with the location of the client certificate and key (the location is relative to the client that's connecting to the endpoint).

```
cert /{{path}}/client1.domain.tld.crt
key /{{path}}/client1.domain.tld.key
```

(Option 2) Add the contents of the client certificate between `<cert>``</cert>` tags and the contents of the private key between `<key>``</key>` tags to the configuration file. If you choose this option, you distribute only the configuration file to your clients.

If you generated separate client certificates and keys for each user that will connect to the Client VPN endpoint, repeat this step for each user.

The following is an example of the format of a Client VPN configuration file that includes the client certificate and key.

```
client
dev tun
proto udp
remote cvpn-endpoint-0011abcabcabcabc1.prod.clientvpn.eu-west-2.amazonaws.com 443
remote-random-hostname
resolv-retry infinite
nobind
remote-cert-tls server
cipher AES-256-GCM
verb 3

<ca>
{{Contents of CA}}
</ca>

<cert>
{{Contents of client certificate (.crt) file}}
</cert>

<key>
{{Contents of private key (.key) file}}
</key>

reneg-sec 0
```
