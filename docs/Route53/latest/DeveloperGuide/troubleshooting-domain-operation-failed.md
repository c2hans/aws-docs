---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-domain-operation-failed.html
---

# My domain operation failed
<a name="troubleshooting-domain-operation-failed"></a>

Here are some troubleshooting tips if your domain operation fails. Operations can be registration, transfer, renewal, or contact update.

## Domain operation failed due to invalid contact information
<a name="troubleshooting-domain-operation-failed-contact-validation"></a>

If a domain operation fails with an error about invalid contact information, the contact details that you provided don't meet the registry's validation requirements.

To resolve this issue, verify that all contact details are correctly formatted:
+ **Name** – Make sure the name contains only valid characters and is properly formatted.
+ **Address** – Confirm that the address format matches the postal standards for the country.
+ **Phone number** – Use the correct international format for the country.
+ **Identification fields** – For domains that require identification numbers, make sure the format is correct for the specified country.

After you correct the contact information, try the domain operation again. For specific requirements for different top-level domains, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
