---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/include-exclude-limit-permissions.html
---

# Limiting permissions to include or exclude AWS Resilience Hub recommendations
<a name="include-exclude-limit-permissions"></a>

AWS Resilience Hub enables you to restrict permissions to include or exclude recommendations per application. You can restrict permissions to include or exclude recommendations per application using the following IAM trust policy. In this IAM trust policy, `caller_IAM_role` (associated with your AWS user account) is used in the current account to call the APIs for AWS Resilience Hub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
