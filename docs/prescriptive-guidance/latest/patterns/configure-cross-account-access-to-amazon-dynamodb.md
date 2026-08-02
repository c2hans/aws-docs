---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html
---

# Configure cross-account access to Amazon DynamoDB
<a name="configure-cross-account-access-to-amazon-dynamodb"></a>

*Shashi Dalmia, Imhoertha Ojior, and Esteban Serna Parra, Amazon Web Services*

## Summary
<a name="configure-cross-account-access-to-amazon-dynamodb-summary"></a>

This pattern explains the steps for configuring cross-account access to Amazon DynamoDB by using resource-based policies. For workloads that use DynamoDB, it's becoming more common to use [workload isolation strategies](https://aws.amazon.com/solutions/guidance/workload-isolation-on-aws/?did=sl_card&trk=sl_card) to minimize security threats and to meet compliance requirements. Implementing workload isolation strategies often requires cross-account and cross-Region access to DynamoDB resources by using AWS Identity and Access Management (IAM) identity-based policies. This involves setting IAM permissions and establishing a trust relationship between the AWS accounts.

[Resource-based policies for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) greatly simplify the security posture for cross-account workloads. This pattern provides steps and sample code to demonstrate how you can configure AWS Lambda functions in one AWS account to write data to a DynamoDB database table in a different account.

## Prerequisites and limitations
<a name="configure-cross-account-access-to-amazon-dynamodb-prereqs"></a>

**Prerequisites**
+ Two active AWS accounts. This pattern refers to these accounts as *Account A* and *Account B*.
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to access Account A, to create the DynamoDB table. The other steps in this pattern provide instructions for using the IAM, DynamoDB, and Lambda consoles. If you’re planning to use AWS CLI instead, configure it to access both accounts.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="configure-cross-account-access-to-amazon-dynamodb-architecture"></a>

The following diagram shows a single-account architecture. AWS Lambda, Amazon Elastic Compute Cloud (Amazon EC2), and DynamoDB are all in the same account. In this scenario, Lambda functions and Amazon EC2 instances can access DynamoDB. To grant access to the DynamoDB table, you can create an identity-based policy in IAM, or you can create a resource-based policy in DynamoDB.

![Using IAM permissions to access a DynamoDB table in the same account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bfc32fe8-5db0-4cac-a30f-b870a1a82875/images/cbb009eb-422d-4833-a1bc-0c571d83c21f.png)

The following diagram shows a multi-account architecture. If resources in one AWS account require access to a DynamoDB table in a different account, you need to set up a resource-based policy in DynamoDB to grant the required access. For example, in the following diagram, access to the DynamoDB table in Account A is granted to a Lambda function in Account B by using a resource-based policy.

![Using a resource-based policy to access a DynamoDB table in a different account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bfc32fe8-5db0-4cac-a30f-b870a1a82875/images/9f9165a8-b767-4427-a2ae-31b5b8c83326.png)

This pattern describes cross-account access between Lambda and DynamoDB. You can use similar steps for other AWS services if the appropriate permissions are configured on both accounts. For example, if you want to provide a Lambda function access to an Amazon Simple Storage Service (Amazon S3) bucket in Account A, you can create a [resource-based policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) in Amazon S3 and add the permissions to the [Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) in Account B.

## Tools
<a name="configure-cross-account-access-to-amazon-dynamodb-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Code**

This pattern includes sample code in the [Additional information](#configure-cross-account-access-to-amazon-dynamodb-additional) section to show how you can configure a Lambda function in Account B to write to the DynamoDB table in Account A. The code is provided only for illustration and testing purposes. If you’re implementing this pattern in a production environment, use the code as a reference, and customize it for your own environment.

## Best practices
<a name="configure-cross-account-access-to-amazon-dynamodb-best-practices"></a>
+ Follow the [best practices for resource-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-best-practices.html) in the DynamoDB documentation.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="configure-cross-account-access-to-amazon-dynamodb-epics"></a>

### Create an IAM policy and role for the Lambda function in Account B
<a name="create-an-iam-policy-and-role-for-the-lam-function-in-account-b"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a policy in Account B. | This IAM policy allows the [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) action for a DynamoDB table in Account A.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html) | General AWS |
| Create a role in Account B. | The Lambda function in Account B uses this IAM role to access the DynamoDB table in Account A.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html)<br />For more information about creating roles, see the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). | General AWS |
| Note the role ARN. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html) | General AWS |

### Create a DynamoDB table in Account A
<a name="create-a-ddb-table-in-account-a"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a DynamoDB table. | Use the following AWS CLI command to create a DynamoDB table.<pre> aws dynamodb create-table \<br />    --table-name Table-Account-A \<br />    --attribute-definitions \<br />      AttributeName=category,AttributeType=S \<br />      AttributeName=item,AttributeType=S \<br />    --key-schema \<br />      AttributeName=category,KeyType=HASH \<br />      AttributeName=item,KeyType=RANGE \<br />    --provisioned-throughput \<br />      ReadCapacityUnits=5,WriteCapacityUnits=5 \<br />    --resource-policy \<br />      '{         <br />          "Version": "2012-10-17",		 	 	 <br />          "Statement": [<br />            {                    <br />               "Sid": "Statement1",<br />               "Effect": "Allow",<br />               "Principal": {<br />                  "AWS": "arn:aws:iam::<Account-B-ID>:role/<Role-Name>"<br />               },<br />               "Action": "dynamodb:PutItem",<br />               "Resource": "arn:aws:dynamodb:<Region>:<Account-A-ID>:table/Table-Account-A"<br />            }            <br />         ]<br />      }'</pre><br />Replace the following in this code sample:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html)You specify the resource-based policy configuration in the `create-table` statement by using the `--resource-policy` flag. This policy refers to the ARN for the DynamoDB table in Account A.<br />For more information about creating tables, see the [DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html). | General AWS |

### Create a Lambda function in Account B
<a name="create-a-lam-function-in-account-b"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Lambda function to write data to DynamoDB. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html)For more information about creating Lambda functions, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html). | General AWS |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete resources. | To avoid incurring costs associated with the resources created in this pattern, do the following to delete these resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html) | General AWS |

## Troubleshooting
<a name="configure-cross-account-access-to-amazon-dynamodb-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| When creating the Lambda function, you receive a `ResourceNotFoundException` error. | Confirm that you have correctly entered the AWS Region and ID of Account A. These are part of the ARN for the DynamoDB table. |

## Related resources
<a name="configure-cross-account-access-to-amazon-dynamodb-resources"></a>
+ [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html) (DynamoDB documentation)
+ [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) (Lambda documentation)
+ [Using resource-based policies for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) (DynamoDB documentation)
+ [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) (IAM documentation)
+ [Cross-account policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html) (IAM documentation)
+ [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) (IAM documentation)

## Additional information
<a name="configure-cross-account-access-to-amazon-dynamodb-additional"></a>

*Sample code*

```
import boto3
from datetime import datetime

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
     now = datetime.now().isoformat()
     data = dynamodb_client.put_item(TableName='arn:aws:dynamodb:<Region>:<Account-A-ID>:table/Table-Account-A', Item={"category": {"S": "Fruit"},"item": {"S": "Apple"},"time": {"S": now}})
     return data
```

**Note**
When the DynamoDB client is instantiated, the ARN of the DynamoDB table is provided instead of the table name. This is required so that the Lambda function connects to the correct DynamoDB table when it runs.
