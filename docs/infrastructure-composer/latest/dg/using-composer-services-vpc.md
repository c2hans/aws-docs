---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-services-vpc.html
---

# Integrate Infrastructure Composer with Amazon Virtual Private Cloud (Amazon VPC)
<a name="using-composer-services-vpc"></a>

AWS Infrastructure Composer features an integration with the Amazon Virtual Private Cloud (Amazon VPC) service. Using Infrastructure Composer, you can do the following:
+ Identify the resources on your canvas that are in a VPC through a visual **VPC** tag.
+ Configure AWS Lambda functions with VPCs from an external template.

The following image shows is an example of an application with a Lambda function configured with a VPC.

![An application with the VPC tag visualizing a Lambda function in Infrastructure Composer that is configured with a VPC.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_use_vpc_06.png)

To learn more about Amazon VPC, see [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide*.

**Topics**
+ [Identify Infrastructure Composer resources and related information in a VPC](using-composer-services-vpc-tag.md)
+ [Configure Lambda functions with external VPCs in Infrastructure Composer](using-composer-services-vpc-configure.md)
+ [Parameters in imported templates for an external VPC with Infrastructure Composer](using-composer-services-vpc-import.md)
+ [Adding new parameters to imported templates with Infrastructure Composer](using-composer-services-vpc-import-add.md)
+ [Configure a Lambda function and a VPC defined in another template with Infrastructure Composer](using-composer-services-vpc-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
