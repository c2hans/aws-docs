---
source_url: https://docs.aws.amazon.com/polly/latest/dg/encryption-at-rest.html
---

# Encryption at Rest
<a name="encryption-at-rest"></a>

Output of your Amazon Polly voice synthesis can be saved on your own system. You can also call Amazon Polly, and then encrypt the file with any encryption key of your choice and store it in Amazon Simple Storage Service (Amazon S3) or another secure storage. The Amazon Polly [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/APIReference/API_SynthesizeSpeech.html) operation is stateless and is not associated with a customer identity. You can't retrieve it from Amazon Polly later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
