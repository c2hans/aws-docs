---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/quotas.html
---

# Quotas for AWS End User Messaging Social
<a name="quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

Your AWS account has the following quotas related to AWS End User Messaging Social.

| Resource | Default |
| --- | --- |
| WhatsApp Business Account (WABA) | 25 per Region |

AWS End User Messaging Social implements quotas that restrict the number of requests that you can make to the AWS End User Messaging Social API from your AWS account.

|  Operation  | Default quota rate (requests per second) |
| --- | --- |
| SendWhatsAppMessage  | 1,000 |
| PostWhatsAppMessageMedia  | 100 |
| GetWhatsAppMessageMedia  | 100 |
| DeleteWhatsAppMessageMedia  | 100 |
| DisassociateWhatsAppBusinessAccount  | 10 |
| ListWhatsAppBusinessAccount  | 10 |
| TagResource  | 10 |
| UntagResourceRate  | 10 |
| ListTagsForResourceRate  | 10 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
