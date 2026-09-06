---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-cannot-connect.html
---

# Troubleshooting AWS Client VPN: Client software returns a TLS error when trying to connect to Client VPN
<a name="client-cannot-connect"></a>

**Problem**
I used to be able to connect my clients to the Client VPN successfully, but now the OpenVPN-based client returns one of the following errors when it tries to connect:

```
TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
TLS Error: TLS handshake failed
```

```
Connection failed because of a TLS handshake error. Contact your IT administrator.
```

**Possible cause \#1**
If you use mutual authentication and you imported a client certificate revocation list, the client certificate revocation list might have expired. During the authentication phase, the Client VPN endpoint checks the client certificate against the client certificate revocation list that you imported. If the client certificate revocation list has expired, you cannot connect to the Client VPN endpoint.

**Solution \#1**
Check the expiry date of your client certificate revocation list by using the OpenSSL tool.

```
$ openssl crl -in {{path_to_crl_pem_file}} -noout -nextupdate
```

The output displays the expiry date and time. If the client certificate revocation list has expired, you must create a new one and import it to the Client VPN endpoint. For more information, see [AWS Client VPN client certificate revocation lists](cvpn-working-certificates.md).

**Possible cause \#2**
The server certificate being used for the Client VPN endpoint has expired.

**Solution \#2**
Check the status of your server certificate in the AWS Certificate Manager console or by using the AWS CLI. If the server certificate is expired, create a new certificate and upload to ACM. For detailed steps to generate the server and client certificates and keys using the [OpenVPN easy-rsa utility](https://github.com/OpenVPN/easy-rsa), and import them into ACM see [Mutual authentication in AWS Client VPN](mutual.md).

Alternatively, there might be an issue with the OpenVPN-based software that the client is using to connect to the Client VPN. For more information about troubleshooting OpenVPN-based software, see [Troubleshooting Your Client VPN Connection](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/troubleshooting.html) in the *AWS Client VPN User Guide*.
