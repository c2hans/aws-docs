---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/security-best-practices.html
---

# Security best practices
<a name="security-best-practices"></a>

AWS End User Messaging SMS provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.
+ Create an individual user for each person who manages AWS End User Messaging SMS resources, including yourself. Don't use AWS root credentials to manage AWS End User Messaging SMS resources.
+ Grant each user the minimum set of permissions required to perform his or her duties.
+ Use IAM groups to effectively manage permissions for multiple users.
+ Rotate your IAM credentials regularly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
