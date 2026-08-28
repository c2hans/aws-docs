---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-tagging.html
---

# Tagging Inferences and Resources in Bedrock Data Automation
<a name="bda-tagging"></a>

To help you manage your BDA resources and inferences, you can assign metadata to either as tags. A tag is a label that you assign to an AWS resource, such as a project, or blueprint. Each tag consists of a key and a value.

Tagging resources enables you to catagorize your AWS resources in different ways, for example, by purpose, owner, or application. Tagging inferences works slightly differently. This kind of tagging allows you to catagorize not just projects or blueprints, but specific calls of the BDA API. For more information, see Tagging your AWS resources.

On top of catagorization you can use inference tags to see costs allocations each month. For more information, see Use cost allocation tags in the AWS Billing and Cost Management User Guide.

Tags help you do the following:
+ Identify and organize your AWS resources. Many AWS resources support tagging, so you can assign the same tag to resources in different services to indicate that the resources are the same.
+ Control access to your resources. You can use tags with Amazon Bedrock to create policies to control access to Amazon Bedrock resources. These policies can be attached to an IAM role or user to enable tag-based access control.
+ Allocate costs. You activate tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. Usable with inference tagging only.

For more information on tagging resoruces and inferences, such as how to use API tagging operations, see [Tagging Amazon Bedrock resources](tagging.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
