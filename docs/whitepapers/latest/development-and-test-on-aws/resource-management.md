---
source_url: https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/resource-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Resource management
<a name="resource-management"></a>

 With AWS, your development and test teams can have their own resources, scaled according to their own needs. Provisioning complex environments or platforms composed of multiple resources can be done using AWS CloudFormation stacks, or some of the other automation techniques described in this whitepaper. In large organizations comprising multiple teams, it is a good practice to create an internal role or service responsible for centralizing and managing IT resources running on AWS. This role typically consists of:
+  Promoting the internal development and test practices described here
+  Developing and maintaining template AMIs and template AWS CloudFormation stacks with the different tools and platforms used in your organization
+  Collecting resource requests from project teams, and provisioning resources on AWS according to your organization’s policies, including network configuration (such as Amazon VPC) and security configurations (such as Security Groups and IAM credentials)
+  Monitoring resource usage and charges using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), and allocating these to team budgets

 You can use the [Service Catalog](https://aws.amazon.com/servicecatalog/) to achieve the tasks above or you might want to develop your own internal provisioning and management portal for a tighter integration with internal processes. You can do this by using one of the AWS SDKs, which allow programmatic access to resources running on AWS.

## Cost allocation and multiple AWS accounts
<a name="cost-allocation-and-multiple-aws-accounts"></a>

 Some customers have found it helpful to create specific accounts for development and test activities. This can be important when your production environment also runs on AWS and you need to separate teams and responsibilities. Separate accounts are isolated from each other by default, so that, for example, development and test users do not interfere with production resources. To enable collaboration, AWS offers a number of features that enable sharing of resources across accounts, such as [Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html), AMIs, and [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html).

 To separate out and allocate the cost for the various activities and phases of the development and test cycle, AWS offers various options. One option is to use separate accounts (for example, for development, testing, staging, and production), and each account will have its own bill. You can also consolidate multiple accounts using consolidated billing for [AWS Organizations](https://aws.amazon.com/organizations/) to simplify costs and take advantage of quantity discounts with a single bill.

 Another option is to make use of the [monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html), which enables you to organize and track your AWS costs by using resource tagging. In the context of development and test, tags can represent the various stages or teams of the development cycle, though you are free to choose the dimensions you find most helpful.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
