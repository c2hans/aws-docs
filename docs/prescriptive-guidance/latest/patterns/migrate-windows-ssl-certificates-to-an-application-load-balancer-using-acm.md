---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm.html
---

# Migrate Windows SSL certificates to an Application Load Balancer using ACM
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm"></a>

*Chandra Sekhar Yaratha and Igor Kovalchuk, Amazon Web Services*

## Summary
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-summary"></a>

The pattern provides guidance for using AWS Certificate Manager (ACM) to migrate existing Secure Sockets Layer (SSL) certificates from websites that are hosted on on-premises servers or Amazon Elastic Compute Cloud (Amazon EC2) instances on Microsoft Internet Information Services (IIS). The SSL certificates can then be used with Elastic Load Balancing on AWS.

SSL protects your data, affirms your identity, provides better search engine rankings, helps meet Payment Card Industry Data Security Standard (PCI DSS) requirements, and improves customer trust. Developers and IT teams that manage these workloads want their web applications and infrastructure, including the IIS server and Windows Server, to remain compliant with their baseline policies.

This pattern covers manually exporting existing SSL certificates from Microsoft IIS, converting them from Personal Information Exchange (PFX) format to the Private Enhanced Mail (PEM) format that ACM supports, and then importing them into ACM in your AWS account. It also describes how to create an Application Load Balancer for your application and configure the Application Load Balancer to use your imported certificates. HTTPS connections are then terminated on the Application Load Balancer, and you don’t need further configuration overhead on the web server. For more information, see [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html).

Windows servers use .pfx or .p12 files to contain the public key file (SSL certificate) and its unique private key file. The Certificate Authority (CA) provides you with your public key file. You use your server to generate the associated private key file where the certificate signing request (CSR) was created.

## Prerequisites and limitations
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC) on AWS with at least one private and one public subnet in each Availability Zone used by your targets
+ IIS version 8.0 or later running on Windows Server 2012 or later
+ A web application running on IIS
+ Administrator access to the IIS server

## Architecture
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-architecture"></a>

**Source technology stack**
+ IIS web server implementation with SSL to ensure that data is transmitted securely in an encrypted connection (HTTPS)

**Source architecture**

![Source architecture for migrating Windows SSL certificates to Application Load Balancer using ACM](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cad6e465-da39-4819-970e-10e1c30e0a1f/images/e63efb6f-205b-4e20-a043-6bc954470191.png)

**Target technology stack**
+ ACM certificates in your AWS account
+ An Application Load Balancer configured to use imported certificates
+ Windows Server instances in the private subnets

**Target architecture**

![Target architecture for migrating Windows SSL certificates to Application Load Balancer using ACM](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cad6e465-da39-4819-970e-10e1c30e0a1f/images/45ac7fba-fbad-4c74-9b1f-80ca212dae08.png)

## Tools
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-tools"></a>
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across EC2 instances, containers, and IP addresses in one or more Availability Zones.

## Best practices
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-best-practices"></a>
+ Enforce traffic redirects from HTTP to HTTPS.
+ Configure security groups for your Application Load Balancer properly to allow inbound traffic only to specific ports.
+ Launch your EC2 instances in different Availability Zones to ensure high availability.
+ Configure your application’s domain to point to the Application Load Balancer’s DNS name instead of its IP address.
+ Make sure that the Application Load Balancer has application-layer [health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) configured.
+ Configure the threshold for health checks.
+ Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor the Application Load Balancer.

## Epics
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-epics"></a>

### Export a .pfx file
<a name="export-a-pfx-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export the .pfx file from Windows Server. | To export the SSL certificate as a .pfx file from the on-premises IIS manager in Windows Server:1. Choose **Start**, **Administrative**, **Internet Information Services (IIS) Manager**.<br />2. Select the server name, and under **Security**, double-click **Server Certificates**.<br />3. Choose the certificate that you want to export, and then choose **Export**.<br />4. In the **Export Certificate** box, choose a location, path, and name for your .pfx file.<br />5. Specify and confirm a password for your .pfx file.You need this password when you install the .pfx file.<br />6. Choose OK.<br />Your .pfx file should now be saved to the location and path you specified. | Systems administrator |

### Convert the PFX-encoded certificate to PEM format
<a name="convert-the-pfx-encoded-certificate-to-pem-format"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and install the OpenSSL toolkit. | 1. Download and install [Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) from the Shining Light Productions website.<br />2. Add the location of the OpenSSL binaries to your system `PATH` variable, so the binaries can be available for command-line use. | Systems administrator |
| Convert the PFX-encoded certificate to PEM format. | The following steps convert the PFX-encoded, signed certificate file into three files in PEM format:+ `cert-file.pem` contains the SSL/TLS certificate for the resource.<br />+ `privatekey.pem` contains the private key of the certificate with no password protection.<br />+ `ca-chain.pem` contains the root certificate of the CA.<br />To convert the PFX encoded certificate:1. Run Windows PowerShell.<br />2. Use the following command to extract the private key of the certificate from the PFX file. Enter the certificate password when prompted.<pre>openssl pkcs12 -in <filename>.pfx -nocerts -out withpw-privatekey.pem</pre><br />The command generates a PEM-encoded private key file named `privatekey.pem`. Enter a passphrase to protect the private key file when prompted.<br />3. Run the following command to remove the passphrase. When prompted, provide the passphrase that you created in step 2.<pre>openssl rsa -in withpw-privatekey.pem -out privatekey.pem</pre><br />If the command is successful, it displays the message "writing RSA key."<br />4. Use the following command to transfer the certificate from the PFX file to a PEM file.<pre>openssl pkcs12 -in <file_name>.pfx -clcerts -nokeys -out cert-file.pem</pre><br />This creates a PEM-encoded certificate file named `cert-file.pem`. If the command is successful, it displays the message "MAC verified OK."<br />5. Create a CA chain file from the PFX file. The following command creates a CA chain file named `ca-chain.pem`.<pre>openssl pkcs12 -in <file_name>.pfx -cacerts -nokeys -chain -out ca-chain.pem</pre><br />If the command is successful, it displays the message "MAC verified OK." | Systems administrator |

### Import a certificate into ACM
<a name="import-a-certificate-into-acm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare to import the certificate. | On the [ACM console](https://console.aws.amazon.com/acm/home), choose **Import a certificate**. | Cloud administrator |
| Provide the certificate body. | For **Certificate body**, paste the PEM-encoded certificate that you want to import. <br />For more information about the commands and steps described in this and other tasks in this epic, see [Importing a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the ACM documentation. | Cloud administrator |
| Provide the certificate private key. | For **Certificate private key**, paste the PEM-encoded, unencrypted private key that matches the certificate's public key. | Cloud administrator |
| Provide the certificate chain. | For **Certificate chain**, paste the PEM-encoded certificate chain, which is stored in the `CertificateChain.pem` file. | Cloud administrator |
| Import the certificate. | Choose **Review and import**. Confirm that the information about your certificate is correct, and then choose **Import**. | Cloud administrator |

### Create an Application Load Balancer
<a name="create-an-application-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure the load balancer and listeners. | Follow the instructions in the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) to configure a target group, register targets, and create an Application Load Balancer and listener. Add a second listener (HTTPS) for port 443. | Cloud administrator |

## Troubleshooting
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Windows PowerShell doesn't recognize the OpenSSL command even after you add it to the system path. | Check `$env:path` to make sure that it includes the location of the OpenSSL binaries.<br />If it doesn’t, run the following command in PowerShell:<pre>$env:path = $env:path + ";C:\OpenSSL-Win64\bin"</pre> |

## Related resources
<a name="migrate-windows-ssl-certificates-to-an-application-load-balancer-using-acm-resources"></a>

**Importing a certificate into ACM**
+ [ACM console](https://console.aws.amazon.com/acm/home)
+ [Certificate and key format for importing](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-format.html)
+ [Importing a certificate](https://aws.amazon.com/blogs/security/how-to-import-pfx-formatted-certificates-into-aws-certificate-manager-using-openssl/)
+ [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)

**Creating an Application Load Balancer**
+ [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html)
+ [Application Load Balancer User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
