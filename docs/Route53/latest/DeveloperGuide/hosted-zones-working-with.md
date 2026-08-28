---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html
---

# Working with hosted zones
<a name="hosted-zones-working-with"></a>

A hosted zone is a container for records. Records hold information about how to route traffic for a domain, such as example.com, and its subdomains (acme.example.com, zenith.example.com). A hosted zone has the same name as its domain. There are two types:
+ *Public hosted zones* contain records that specify how you want to route traffic on the internet. For more information, see [Working with public hosted zones](AboutHZWorkingWith.md).
+ *Private hosted zones* contain records that specify how you want to route traffic in an Amazon VPC. For more information, see [Working with private hosted zones](hosted-zones-private.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
