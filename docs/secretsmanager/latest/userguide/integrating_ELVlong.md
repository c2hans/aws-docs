---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ELVlong.html
---

# How AWS Elemental Live uses AWS Secrets Manager
<a name="integrating_ELVlong"></a>

AWS Elemental Live is a real-time video service that lets you create live outputs for broadcast and streaming delivery.

AWS Elemental Live uses a secret ARN to get a secret that contains an encryption key from Secrets Manager. Elemental Live uses the encryption key to encrypt/decrypt the video. For more information, see [How delivery from AWS Elemental Live to MediaConnect works at runtime](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect-how-it-works-at-runtime.html) in the *Elemental Live User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
