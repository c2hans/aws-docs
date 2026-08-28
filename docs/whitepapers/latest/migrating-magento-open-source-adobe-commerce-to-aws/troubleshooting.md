---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/troubleshooting.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Troubleshooting
<a name="troubleshooting"></a>

 Terraform can sometimes timeout when interacting with the AWS API. It is usually best to do a terraform destroy and then do terraform apply when encountering these errors.

 For troubleshooting common Quick Start issues visit the [AWS Quick Start General Content Guide](http://general-content-file) or the [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) page in the AWS documentation.

 After you successfully deploy a Quick Start, confirm that your resources and services are updated and configured — including any required patches — to meet your security and other needs. For more information, see the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
