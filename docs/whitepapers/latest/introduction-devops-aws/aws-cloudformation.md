---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cloudformation.html
---

# CloudFormation
<a name="aws-cloudformation"></a>

AWS CloudFormation is a service that enables developers to create AWS resources in an orderly and predictable fashion. Resources are written in text files using JSON or YAML format. The templates require a specific syntax and structure that depends on the types of resources being created and managed. You author your resources in JSON or YAML with any code editor such as [AWS Cloud9](https://aws.amazon.com/cloud9/), check it into a version control system, and then CloudFormation builds the specified services in safe, repeatable manner.

A CloudFormation template is deployed into the AWS environment as a stack. You can manage stacks through the AWS Management Console, AWS Command Line Interface, or CloudFormation APIs. If you need to make changes to the running resources in a stack you update the stack. Before making changes to your resources, you can generate a change set, which is a summary of your proposed changes. Change sets enable you to see how your changes might impact your running resources, especially for critical resources, before implementing them.

![A diagram depicting AWS CloudFormation creating an entire environment (stack) from one template](http://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/images/figure-1.png)

You can use a single template to create and update an entire environment, or separate templates to manage multiple layers within an environment. This enables templates to be modularized, and also provides a layer of governance that is important to many organizations.

When you create or update a stack in the CloudFormation console, events are displayed, showing the status of the configuration. If an error occurs, by default the stack is rolled back to its previous state. Amazon SNS provides notifications on events. For example, you can use Amazon SNS to track stack creation and deletion progress using email and integrate with other processes programmatically.

AWS CloudFormation makes it easy to organize and deploy a collection of AWS resources, and lets you describe any dependencies or pass in special parameters when the stack is configured.

With CloudFormation templates, you can work with a broad set of AWS services, such as Amazon S3, Auto Scaling, Amazon CloudFront, Amazon DynamoDB, Amazon EC2, Amazon ElastiCache, AWS Elastic Beanstalk, Elastic Load Balancing, IAM, AWS OpsWorks, and Amazon VPC. For the most recent list of supported resources, refer to [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).
