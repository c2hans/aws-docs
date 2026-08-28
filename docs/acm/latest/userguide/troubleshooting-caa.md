---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-caa.html
---

# Certification Authority Authorization (CAA) problems
<a name="troubleshooting-caa"></a>

You can use CAA DNS records to specify that the Amazon certificate authority (CA) can issue ACM certificates for your domain or subdomain. If you receive an error during certificate issuance that says **One or more domain names have failed validation due to a Certification Authority Authorization (CAA) error**, check your CAA DNS records. If you receive this error after your ACM certificate request has been successfully validated, you must update your CAA records and request a certificate again. The **value** field in your CAA record must contain one of the following domain names:
+ amazon.com
+ amazontrust.com
+ awstrust.com
+ amazonaws.com

For more information about creating a CAA record, see [(Optional) Configure a CAA record](setup.md#setup-caa).

**Note**
You can choose to not configure a CAA record for your domain if you do not want to enable CAA checking.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
