---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html
---

# Best Practices for Tagging AWS Resources
<a name="tagging-best-practices"></a>

Publication date: **March 30, 2023** ([Document revisions](document-revisions.md))

 Amazon Web Services (AWS) allows you to assign metadata to many of your AWS resources in the form of tags. Each tag is a simple label consisting of a key and an optional value to store information about the resource or data retained on that resource. This whitepaper focuses on tagging use cases, strategies, techniques, and tools that can help you to categorize resources by purpose, team, environment, or other criteria relevant to your business. Implementing a consistent tagging strategy can make it easier to filter and search for resources, monitor cost and usage, and manage your AWS environment.

 This paper builds on the practices and guidance provided in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper. It is recommended that you read that whitepaper before this one. AWS recommends that you establish your cloud foundation in a holistic way. For additional information, refer to [Establishing your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html).

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 AWS makes it easy to deploy your workloads in AWS by creating resources, such as [Amazon EC2 instances](https://aws.amazon.com/ec2), [Amazon EBS volumes](https://aws.amazon.com/ebs/), [security groups](https://docs.aws.amazon.com/AWSEC2/latest/DeveloperGuide/using-network-security.html), and [AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). You can also scale and grow the ﬂeet of AWS resources that hosts your applications, stores your data, and expands your AWS infrastructure over time. As your AWS usage grows to many resource types spanning multiple applications, you will need a mechanism to track which resources are assigned to which application. Use this mechanism to support your operational activities, such as cost monitoring, incident management, patching, backup, and access control.

 In on-premises environments, this knowledge is often captured in knowledge management systems, document management systems, and on internal wiki pages. With a configuration management database (CMDB), you can store and manage the relevant detailed metadata using standard change control processes. This approach provides governance, but requires additional effort to develop and maintain. You can take a structured approach to the naming of resources, but a resource name can only hold a limited amount of information.

![Picture showing the decomposition of the name of a resource into its parts.](http://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/images/structured-approach-to-resource-naming.png)

 For example, EC2 instances have a predefined tag called Name that provides similar functionality and allows you to name workloads as they are moved to AWS.

 In 2010, AWS launched [*resource tags*](https://aws.amazon.com/blogs/aws/new-amazon-ec2-feature-resource-tagging/) to provide a ﬂexible and scalable mechanism for attaching metadata to your resources. This whitepaper guides you through the process of developing and implementing a robust tagging strategy across your AWS environment. This guidance will help you ensure tagging consistency and coverage that supports your decision-making and operational activities

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
