---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/certexpirationindicators.html
---

# Certificate expiration status indicators
<a name="certexpirationindicators"></a>

In the IAM Identity Center console, the **Applications** page displays status indicator icons in the properties of each application. These icons display in the **Expires on** column next to each certificate in the list. The following describes the criteria that IAM Identity Center uses to determine which icon displays for each certificate.
+ **Red** – Indicates that a certificate is currently expired.
+ **Yellow** – Indicates that a certificate will expire in 90 days or less.
+ **Green** – Indicates that a certificate is currently valid and will remain valid for at least 90 more days.

**To check the status of a certificate**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Applications**.

1. In the list of applications, review the status of the certificates in the list as indicated in the **Expires on** column.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
