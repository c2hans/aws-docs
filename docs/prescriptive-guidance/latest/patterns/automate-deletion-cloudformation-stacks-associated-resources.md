---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html
---

# Automate deletion of AWS CloudFormation stacks and associated resources
<a name="automate-deletion-cloudformation-stacks-associated-resources"></a>

*SANDEEP SINGH and James Jacob, Amazon Web Services*

## Summary
<a name="automate-deletion-cloudformation-stacks-associated-resources-summary"></a>

[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is a widely-used service for managing cloud infrastructure as code (IaC). When you use CloudFormation, you manage related resources as a single unit called a *stack*. You create, update, and delete a collection of resources by creating, updating, and deleting stacks.

Sometimes, you no longer need the resources in a CloudFormation stack. Depending on the resources and their configurations, it can be complicated to delete a stack and its associated resources. In real-world production systems, deletions sometimes fail or take a long time due to conflicting conditions or restrictions that CloudFormation cannot override. It can require careful planning and execution to make sure that all resources are properly deleted in an efficient and consistent manner. This pattern describes how to set up a framework that helps you manage the deletion of CloudFormation stacks that involve the following complexities:
+ **Resources with delete protection** – Some resources might have delete protection enabled. Common examples are [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) tables and [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) buckets. Delete protection prevents automated deletion, such as deletion through CloudFormation. If you want to delete these resources, you must manually or programmatically override or temporarily disable the delete protection. You should carefully consider the implication of deleting these resources before proceeding.
+ **Resources with retention policies** – Certain resources, such as AWS Key Management Service (AWS KMS) keys and Amazon S3 buckets, might have retention policies that specify how long they should be retained after deletion is requested. You should account for these policies in the cleanup strategy to maintain compliance with organizational policies and regulatory requirements.
+ **Delayed deletion of Lambda functions that are attached to a VPC** – Deleting an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that is attached to a virtual private cloud (VPC) can take 5–40 minutes, depending the multiple interconnected dependencies involved in the process. If you detach the function from the VPC before deleting the stack, you can reduce this delay to under 1 minute.
+ **Resources not directly created by CloudFormation** – In certain application designs, resources might be created outside of the original CloudFormation stack, either by the application itself or by resources provisioned through the stack. The following are two examples:
  + CloudFormation might provision an [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance that runs a user data script. Then, this script might create an [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) parameter to store application-related data. This parameter is not managed through CloudFormation.
  + CloudFormation might provision a Lambda function that automatically generates an [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) group for storing logs. This log group is not managed through CloudFormation.

  Even though these resources aren't directly managed by CloudFormation, they often need to be cleaned up when the stack is deleted. If left unmanaged, they can become orphaned and lead to unnecessary resource consumption.

Although these guardrails can cause complexity, they are intentional and critical. Allowing CloudFormation to override all constraints and indiscriminately delete resources could lead to detrimental and unforeseen consequences in many scenarios. However, as a DevOps or cloud engineer who is responsible for managing the environment, there are times when overriding these constraints might be necessary, particularly in development, testing, or staging environments.

**Targeted business outcomes**

By implementing this framework, you can achieve the following benefits:
+ **Cost management** – Regular and efficient cleanup of temporary environments, such as end-to-end or user-acceptance testing environments, helps prevent resources from running longer than necessary. This can significantly reduce costs.
+ **Security** – Automated cleanup of outdated or unused resources reduces the attack surface and helps maintain a secure AWS environment.
+ **Operational efficiency** – Regular and automated cleanup can provide the following operational benefits:
  + Automated scripts that remove old log groups or empty Amazon S3 buckets can improve operational efficiency by keeping the environment clean and manageable.
  + Quickly deleting and recreating stacks supports rapid iteration for design and implementation, which can lead to a more robust and resilient architecture.
  + Regularly deleting and rebuilding environments can help you identify and fix potential issues. This can help you make sure that the infrastructure can withstand real-world scenarios.

## Prerequisites and limitations
<a name="automate-deletion-cloudformation-stacks-associated-resources-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Python version 3.6 or later, [installed](https://www.python.org/downloads/)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Limitations**
+ A naming convention is used to identify the resources that should be deleted. The sample code in this pattern uses a prefix for the resource name, but you can define your own naming convention. Resources that do not use this naming convention will not be identified or subsequently deleted.

## Architecture
<a name="automate-deletion-cloudformation-stacks-associated-resources-architecture"></a>

The following diagram shows how this framework identifies the target CloudFormation stack and the additional resources associated with it.

![The phases that discover, process, and delete CloudFormation stacks and their associated resources.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ab7c3b56-3476-41a3-8ece-68915605a546/images/a7fceb1c-d624-47b3-957d-f910ef2f44d7.png)

The diagram shows the following workflow:

1. **Gather resources** – The automation framework uses a naming convention to return all relevant CloudFormation stacks, Amazon Elastic Container Registry (Amazon ECR) repositories, DynamoDB tables, and Amazon S3 buckets.
**Note**
The functions for this stage use [paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html), a feature in Boto3 that abstracts the process of iterating over a truncated API result set. This makes sure that all resources are processed. To further optimize performance, consider applying [server-side](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html#filtering-results) filtering or consider using JMESPath to perform [client-side](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html#filtering-results-with-jmespath) filtering.

1. **Pre-processing** – The automation framework identifies and addresses the service constraints that must be overridden in order to allow CloudFormation to delete the resources. For example, it changes the `DeletionProtectionEnabled` setting for DynamoDB tables to `False`. In the command-line interface, for each resource, you receive a prompt asking if you want to override the constraint.

1. **Delete stack** – The automation framework deletes the CloudFormation stack. In the command-line interface, you receive a prompt asking if you want to delete the stack.

1. **Post-processing** – The automation framework deletes any related resources that were not directly provisioned through CloudFormation as part of the stack. Examples of these resource types include Systems Manager parameters and CloudWatch log groups. Separate functions gather these resources, pre-process them, and then delete them. In the command-line interface, for each resource, you receive a prompt asking if you want to delete the resource.
**Note**
The functions for this stage use [paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html), a feature in Boto3 that abstracts the process of iterating over a truncated API result set. This makes sure that all resources are processed. To further optimize performance, consider applying [server-side](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html#filtering-results) filtering or consider using JMESPath to perform [client-side](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html#filtering-results-with-jmespath) filtering.

**Automation and scale**

If your CloudFormation stack includes other resources that are not included in the sample code, or if the stack has a constraint that has not been addressed in this pattern, then you can adapt the automation framework for your use case. Follow the same methodology of gathering resources, pre-processing, deleting the stack, and then post-processing.

## Tools
<a name="automate-deletion-cloudformation-stacks-associated-resources-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [CloudFormation Command Line Interface (CFN-CLI)](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html) is an open source tool that helps you develop and test AWS and third-party extensions and then register them for use in CloudFormation.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

**Other tools**
+ [Click](https://click.palletsprojects.com/en/stable/) is a Python tool that helps you create command line interfaces.
+ [Poetry](https://python-poetry.org/docs/) is a tool for dependency management and packaging in Python.
+ [Pyenv](https://github.com/pyenv/pyenv) is a tool that helps you manage and switch between versions of Python.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [cloudformation-stack-cleanup](https://github.com/aws-samples/cloudformation-stack-cleanup/) repository.

## Best practices
<a name="automate-deletion-cloudformation-stacks-associated-resources-best-practices"></a>
+ **Tag resources for easy identification** – Implement a [tagging strategy](https://aws.amazon.com/solutions/guidance/tagging-on-aws/) to identify resources that are created for different environments and purposes. Tags can simplify the cleanup process by helping you filter resources based on their tags.
+ **Set up resource life cycles** – Define resource life cycles in order to automatically delete resources after a certain period. This practice helps you make sure that temporary environments do not become permanent cost liabilities.

## Epics
<a name="automate-deletion-cloudformation-stacks-associated-resources-epics"></a>

### Install tools
<a name="install-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html) | DevOps engineer |
| Install Poetry. | Follow the [instructions](https://python-poetry.org/docs/) (Poetry documentation) to install Poetry in the target virtual environment. | DevOps engineer |
| Install dependencies. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html) | DevOps engineer |
| (Optional) Install Pyenv. | Follow the [instructions](https://github.com/pyenv/pyenv#installation) (GitHub) to install Pyenv. | DevOps engineer |

### (Optional) Customize the framework
<a name="optional-customize-the-framework"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create functions that gather, pre-process, and delete the target resources. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html) | DevOps engineer, Python |

### Create sample resources
<a name="create-sample-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html) | AWS DevOps |
| Create a Systems Manager parameter. | Enter the following command to create a Systems Manager parameter that isn't provisioned through CloudFormation:<pre>aws ssm put-parameter \<br />  --name "/sampleforcleanup/database/password" \<br />  --value "your_db_password" \<br />  --type "SecureString" \<br />  --description "Database password for my app" \<br />  --tier "Standard" \<br />  --region "us-east-1"</pre> | AWS DevOps |
| Create an Amazon S3 bucket. | Enter the following command to create an Amazon S3 bucket that isn't provisioned through CloudFormation:<pre>aws s3api create-bucket \<br />  --bucket samplesorcleanup-unmanagedbucket-<UniqueIdentifier> \<br />  --region us-east-1 \<br />  --create-bucket-configuration LocationConstraint=us-east-1</pre> | AWS DevOps |

### Delete the sample resources
<a name="delete-the-sample-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deletion-cloudformation-stacks-associated-resources.html) | AWS DevOps |
| Validate resource deletion. | In the output, confirm that all of the sample resources have been deleted. For a sample output, see the [Additional resources](#automate-deletion-cloudformation-stacks-associated-resources-additional) section of this pattern. | AWS DevOps |

## Related resources
<a name="automate-deletion-cloudformation-stacks-associated-resources-resources"></a>
+ [Delete a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) (CloudFormation documentation)
+ [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) (CloudFormation documentation)
+ [Giving Lambda functions access to resources in an Amazon VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) (Lambda documentation)
+ [How do I delete an AWS CloudFormation stack that's stuck in DELETE\_FAILED status?](https://repost.aws/knowledge-center/cloudformation-stack-delete-failed) (AWS Knowledge Center)

## Additional information
<a name="automate-deletion-cloudformation-stacks-associated-resources-additional"></a>

The following is a sample output from the `cfncli` command:

```
cfncli --region aus-east-1  dev cleanup-env --prefix-list sampleforcleanup
https://sts.us-east-1.amazonaws.com
Cleaning up: ['sampleforcleanup'] in xxxxxxxxxx:us-east-1
Do you want to proceed? [Y/n]: Y
No S3 buckets
No ECR repositories
No Lambda functions in VPC
The following DynamoDB tables will have their deletion protection removed:
sampleforcleanup-MyDynamoDBTable
Do you want to proceed with removing deletion protection from these tables? [Y/n]: Y
Deletion protection disabled for DynamoDB table 'sampleforcleanup-MyDynamoDBTable'.
The following CloudFormation stacks will be deleted:
sampleforcleanup-Stack
Do you want to proceed with deleting these CloudFormation stacks? [Y/n]: Y
Initiated deletion of CloudFormation stack: `sampleforcleanup-Stack`
Waiting for stack `sampleforcleanup-Stack` to be deleted...
CloudFormation stack `sampleforcleanup-Stack` deleted successfully.
The following ssm_params will be deleted:
/sampleforcleanup/database/password
Do you want to proceed with deleting these ssm_params? [Y/n]: Y
Deleted SSM Parameter: /sampleforcleanup/database/password
Cleaned up: ['sampleforcleanup']
```
