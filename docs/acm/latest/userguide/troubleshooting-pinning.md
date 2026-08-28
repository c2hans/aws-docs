---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-pinning.html
---

# Certificate pinning problems
<a name="troubleshooting-pinning"></a>

To renew a certificate, ACM generates a new public-private key pair. If your application uses [Certificate pinning](acm-bestpractices.md#best-practices-pinning), sometimes known as SSL pinning, to pin an ACM certificate, the application might not be able to connect to your domain after AWS renews the certificate. For this reason, we recommend that you don't pin an ACM certificate. If your application must pin a certificate, you can do the following:
+ [Import your own certificate into ACM](import-certificate.md) and then pin your application to the imported certificate. ACM doesn't provide managed renewal for imported certificates.
+ If you're using a public certificate, pin your application to all available [ Amazon root certificates](https://www.amazontrust.com/repository/). If you're using a private certificate, pin your application to the CA's root certificate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
