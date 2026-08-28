---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-transcribe.html
---

# Configuring your account for Amazon Chime SDK live transcription
<a name="configure-transcribe"></a>

Before you can use Amazon Chime SDK live transcription, you must grant Amazon Chime SDK permission to call Amazon Transcribe and Amazon Transcribe Medical in your AWS account. You do that by adding the Chime Transcription service-linked role to your account. For information about creating the service-linked role for live transcription, refer to [Using roles with live transcription](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-transcription.html) in the *Amazon Chime SDK Administration Guide*. For more information about IAM service-linked roles, refer to [Service Linked Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
