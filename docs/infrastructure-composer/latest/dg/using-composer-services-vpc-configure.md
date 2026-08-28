---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc-configure.html
---

# Configure Lambda functions with external VPCs in Infrastructure Composer
<a name="using-composer-services-vpc-configure"></a>

To start configuring a Lambda function with a VPC that is defined on another template, use the **Lambda Function** enhanced component card. This card represents a Lambda function using the AWS Serverless Application Model (AWS SAM) `AWS::Serverless::Function` resource type.

**To configure a Lambda function with a VPC from an external template**

1. From the **Lambda Function** resource properties panel, expand the **VPC settings (advanced)** dropdown section.

1. Select **Assign to external VPC**.

1. Provide values for the security groups and subnets to configure for the Lambda function. See [Security group and subnet identifiers](using-composer-services-vpc-tag.md#using-composer-services-vpc-configure-ids) for details.

1. **Save** your changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
