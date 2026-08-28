---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/transfer-gdsii-file-to-foundry.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Transfer GDSII file to foundry
<a name="transfer-gdsii-file-to-foundry"></a>

 With your workflow built on AWS, you can now do final sign-off and tape-out. You can transfer the GDSII file to the foundry in multiple ways, including legacy methods such as SFTP. Work with your foundry to enable secure and reliable methods of transferring the GDSII file over to the fab.

 The following figure shows transferring the GDSII file over to the foundry using [AWS Transfer for SFTP](https://aws.amazon.com/aws-transfer-family/). The [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family) provides fully managed support for file transfers directly into and out of Amazon S3 or Amazon EFS.

![This image shows the components involved with transferring the GDSII file to the foundry.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-transfer-gdsii.png)

**Transfer GDSII file to foundry**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
