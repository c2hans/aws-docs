---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/cloudformation.html
---

# Deploy Environments with CloudFormation
<a name="cloudformation"></a>

CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack). For more information, see *[AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)*.

AWS Control Tower uses CloudFormation StackSets to deploy and manage baseline resources, such as IAM roles and AWS Config recorders, in your accounts. For more information about how CloudFormation and AWS Control Tower work together, see [Create AWS Control Tower resources with AWS CloudFormation](creating-resources-with-cloudformation.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
