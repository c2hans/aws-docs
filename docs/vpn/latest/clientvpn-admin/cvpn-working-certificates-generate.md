---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-generate.html
---

# Generate an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-generate"></a>

You can generate a Client VPN certificate revocation list on either a Linux/macOS or Windows operating system. The revocation list is used to revoke access to a Client VPN endpoint for specific certificates. For more information about client certificate revocation lists, see [Client certificate revocation lists](cvpn-working-certificates.md).

------
#### [ Linux/macOS ]

In the following procedure, you generate a client certificate revocation list using the OpenVPN easy-rsa command line utility.

**To generate a client certificate revocation list using OpenVPN easy-rsa**

1. Log on to the server hosting the easyrsa installation used to generate the certificate.

1. Navigate into the `easy-rsa/easyrsa3` folder in your local repo.

   ```
   $ cd easy-rsa/easyrsa3
   ```

1. Revoke the client certificate and generate the client revocation list.

   ```
   $ ./easyrsa revoke {{client1.domain.tld}}
   $ ./easyrsa gen-crl
   ```

   Enter `yes` when prompted.

------
#### [ Windows ]

The following procedure uses the OpenVPN software to generate a client revocation list. It assumes that you followed the [steps for using the OpenVPN software](mutual.md) to generate the client and server certificates and keys.

**To generate a client certificate revocation list using EasyRSA version 3.x.x**

1. Open a command prompt and navigate to the EasyRSA-3.x.x directory, which will depend on where it is installed on your system.

   ```
   C:\> cd c:\{{Users}}\{{windows}}\EasyRSA-3.{{x.x}}
   ```

1. Run the `EasyRSA-Start.bat` file to start the EasyRSA shell.

   ```
   C:\> .\EasyRSA-Start.bat
   ```

1. In the EasyRSA shell, revoke the client certificate.

   ```
   # ./easyrsa revoke {{client_certificate_name}}
   ```

1. Enter `yes` when prompted.

1. Generate the client revocation list.

   ```
   # ./easyrsa gen-crl
   ```

1. The client revocation list will be created in the following location:

   ```
   c:\{{Users}}\{{windows}}\EasyRSA-3.{{x.x}}\pki\crl.pem
   ```

**To generate a client certificate revocation list using previous EasyRSA versions**

1. Open a command prompt and navigate to the OpenVPN directory.

   ```
   C:\> cd \Program Files\OpenVPN\easy-rsa
   ```

1. Run the `vars.bat` file.

   ```
   C:\> vars
   ```

1. Revoke the client certificate and generate the client revocation list.

   ```
   C:\> revoke-full {{client_certificate_name}}
   C:\> more crl.pem
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
