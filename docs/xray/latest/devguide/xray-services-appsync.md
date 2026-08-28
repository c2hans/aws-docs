---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-services-appsync.html
---

# AWS AppSync and AWS X-Ray
<a name="xray-services-appsync"></a>

You can enable and trace requests for AWS AppSync. For more information, see [Tracing with AWS X-Ray](https://docs.aws.amazon.com/appsync/latest/devguide/x-ray-tracing.html) for instructions.

When X-Ray tracing is enabled for an AWS AppSync API, an AWS Identity and Access Management [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your account with the appropriate permissions. This allows AWS AppSync to send traces to X-Ray in a secure way.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
