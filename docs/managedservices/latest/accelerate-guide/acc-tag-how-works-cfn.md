---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-how-works-cfn.html
---

# Using CloudFormation to create tags for AMS Accelerate
<a name="acc-tag-how-works-cfn"></a>

You can use CloudFormation to apply tags at the stack level (see CloudFormation documentation, [ Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)) or at the individual resource level (for example, see [ Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)).

**Important**
Some AMS Accelerate service components require tags with the **ams:rt:** prefix. Resource Tagger believes that it owns these tags, and will delete them if no Resource Tagger configuration rules permit them. You always need to deploy a Resource Tagger configuration profile for these tags, even if you are using CloudFormation or Terraform.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
