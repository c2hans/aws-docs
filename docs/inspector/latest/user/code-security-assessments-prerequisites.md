---
source_url: https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-prerequisites.html
---

# Prerequisites for Code Security
<a name="code-security-assessments-prerequisites"></a>

 Before you can begin using Code Security, you must activate Code Security and decide how to encrypt your data. This can be information like integration credentials, code, or any other information related to your integrations, code repositories, and projects. By default, your data is encrypted with an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). This means the key is created, owned, and managed by the service. If you want to own and manage the key used to encrypt your data, you can create a [customer managed KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
