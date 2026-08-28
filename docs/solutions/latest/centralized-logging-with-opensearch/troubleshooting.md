---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the solution.

If these instructions don’t address your issue, see the [Contact AWS Support](contact-aws-support.md) section for instructions on opening an AWS Support case for this solution.

## Error: Failed to assume service-linked role arn:x:x:x:/AWSServiceRoleForAppSync
<a name="error-service-linked-role"></a>

The reason for this error is that the account has never used the [AWS AppSync](https://aws.amazon.com/appsync/) service. You can deploy the solution’s CloudFormation template again. AWS has already created the role automatically when you encountered the error.

You can also go to [AWS CloudShell](https://aws.amazon.com/cloudshell/) or the local terminal and run the following AWS CLI command to Link AWS AppSync Role

```
aws iam create-service-linked-role --aws-service-name appsync.amazonaws.com
```

## Error: Unable to add backend
<a name="error-backend"></a>

Centralized Logging with OpenSearch only supports Amazon OpenSearch Service domain with [fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) enabled. You must go to the Amazon OpenSearch Service console, and edit the **Access policy** for the Amazon OpenSearch Service domain.

## Error: User xxx is not authorized to perform sts:AssumeRole on resource
<a name="error-user-not-authorized"></a>

 **Message labeled Oops, user is not authorized to perform sts:AssumeRole on resource.**

![image47](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image47.png)

If you see this error, make sure you have entered the correct information during [cross account setup](cross-account-ingestion.md), and then wait for several minutes.

Centralized Logging with OpenSearch uses [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) for cross-account access. This is the best practice to temporarily access the AWS resources in your member account. However, these roles created during [cross account setup](cross-account-ingestion.md) take seconds or minutes to be affective.

## Error: PutRecords API responded with error='InvalidSignatureException'
<a name="error-invalidsignatureexception"></a>

Fluent-bit agent reports PutRecords API responded with error='InvalidSignatureException', message='The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.'

Restart the fluent-bit agent. For example, on EC2 with Amazon Linux2, run the following command:

```
sudo service fluent-bit restart
```

## Error: PutRecords API responded with error='AccessDeniedException'
<a name="error-accessdeniedexception"></a>

Fluent-bit agent deployed on EKS Cluster reports "AccessDeniedException" when sending records to Kinesis. Verify that the IAM role trust relations are correctly set. With the Centralized Logging with OpenSearch console:

1. Open the Centralized Logging with OpenSearch console.

1. In the left sidebar, under **Log Source**, choose **EKS Clusters**.

1. Choose the **EKS Cluster** that you want to check.

1. Choose the **IAM Role ARN**, which will open the IAM Role in the AWS Management Console.

1. Choose the **Trust relationships** to verify that the OIDC Provider, the service account namespace, and conditions are correctly set.

You can get more information from Amazon EKS [IAM role configuration](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts-technical-overview.html#iam-role-configuration).

## CloudFormation stack is stuck on deleting an AWS::Lambda::Function resource when I update the stack
<a name="error-cloudformation-delete"></a>

 **Event with status of DELETE\_IN\_PROGRESS.**

![image48](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image48.png)

The Lambda function resides in a VPC, and you must wait for the associated elastic network interface resource to be deleted.

## The agent status is offline after I restart the EC2 instance
<a name="agent-offline"></a>

This usually happens if you have installed the log agent, but restart the instance before you create any Log Ingestion. The log agent will auto restart if there is at least one Log Ingestion. If you have a log ingestion, but the problem still exists, you can use systemctl status fluent-bit to check its status inside the instance.

## Switched to Global tenant and can’t find the dashboard in OpenSearch
<a name="error-global-tenant"></a>

This is usually because Centralized Logging with OpenSearch received a 403 error from OpenSearch when creating the index template and dashboard. This can be fixed by re-running the Lambda function manually by following the following steps:

With the Centralized Logging with OpenSearch console:

1. Open the Centralized Logging with OpenSearch console, and find the AWS Service Log pipeline that has this issue.

1. Copy the first 5 characters from the ID section. For example, you should copy c169c from ID c169cb23-88f3-4a7e-90d7-4ab4bc18982c

1. Go to AWS Management Console > Lambda. Paste in the function filters. This will filter in all the Lambda functions created for this AWS Service Log ingestion.

1. Click the Lambda function whose name contains "OpenSearchHelperFn".

1. In the **Test** tab, create a new event with any Event name.

1. Click the **Test** button to trigger the Lambda, and wait for the Lambda function to complete.

1. The dashboard should be available in OpenSearch.

## Error from Fluent-bit agent: version `GLIBC\_2.25' not found
<a name="error-fluent-bit"></a>

Refer to [Fix version GLIBC\_2.25 not found issue](additional-resources.md#fix-version-glibc-2.25-not-found-issue).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
