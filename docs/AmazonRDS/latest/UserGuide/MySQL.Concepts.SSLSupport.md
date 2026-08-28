---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.SSLSupport.html
---

# SSL/TLS support for MySQL DB instances on Amazon RDS
<a name="MySQL.Concepts.SSLSupport"></a>

Amazon RDS creates an SSL/TLS certificate and installs the certificate on the DB instance when Amazon RDS provisions the instance. These certificates are signed by a certificate authority. The SSL/TLS certificate includes the DB instance endpoint as the Common Name (CN) for the SSL/TLS certificate to guard against spoofing attacks.

An SSL/TLS certificate created by Amazon RDS is the trusted root entity and should work in most cases, but might fail if your application doesn't accept certificate chains. If your application doesn't accept certificate chains, try using an intermediate certificate to connect to your AWS Region. For example, you must use an intermediate certificate to connect to the AWS GovCloud (US) Regions with SSL/TLS.

For information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster ](UsingWithRDS.SSL.md). For more information about using SSL/TLS with MySQL, see [Updating applications to connect to MySQL DB instances using new SSL/TLS certificates](ssl-certificate-rotation-mysql.md).

For MySQL version 8.0 and lower, Amazon RDS for MySQL uses OpenSSL for secure connections. For MySQL version 8.4 and higher, Amazon RDS for MySQL uses AWS-LC. TLS support depends on the MySQL version. The following table shows the TLS support for MySQL versions.

| MySQL version | TLS 1.0 | TLS 1.1 | TLS 1.2 | TLS 1.3 |
| --- | --- | --- | --- | --- |
| MySQL 8.4 | Not supported | Not supported | Supported | Supported |
| MySQL 8.0 | Not supported | Not supported | Supported | Supported |
| MySQL 5.7 | Supported | Supported | Supported | Not supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
