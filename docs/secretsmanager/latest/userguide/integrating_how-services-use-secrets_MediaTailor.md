---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_MediaTailor.html
---

# How AWS Elemental MediaTailor uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_MediaTailor"></a>

AWS Elemental MediaTailor is a scalable ad insertion and channel assembly service that runs in the AWS Cloud.

MediaTailor supports Secrets Manager access token authentication to your source locations. With Secrets Manager access token authentication, MediaTailor uses a Secrets Manager secret to authenticate requests to your origin. For more information, see [Configuring AWS Secrets Manager access token authentication](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-configuring.html) in the *AWS Elemental MediaTailor User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
