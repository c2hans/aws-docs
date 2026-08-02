---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/upgrade-the-centralized-logging-with-opensearch.html
---

# Upgrade the solution
<a name="upgrade-the-centralized-logging-with-opensearch"></a>

 **Time to upgrade**: Approximately 20 minutes

**Important**
Important The following upgrade documentation only supports Centralized Logging with OpenSearch version 2.x and later. If you are using older versions, such as v1.x or any version of Log Hub, refer to the [Discussions on GitHub](https://github.com/aws-solutions/centralized-logging-with-opensearch/discussions).

 **Step 1. Update the CloudFormation stack**

1. Go to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the Centralized Logging with OpenSearch main stack, and click the **Update** button.

1. Choose **Replace current template**, and enter the specific **Amazon S3 URL** according to your initial deployment type. Refer to [Deployment Overview](http://127.0.0.1:8000/centralized-logging-with-opensearch/implementation-guide/deployment/) for more details.

 **Launch with Amazon Cognito User Pool**

| Type | Link |
| --- | --- |
| Launch with a new VPC | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLogging.template |
| Launch with an existing VPC | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLoggingFromExistingVPC.template |

 **Launch with OpenID Connect (OIDC)**

| Type | Link |
| --- | --- |
| Launch with a new VPC in AWS Regions | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLoggingWithOIDC.template |
| Launch with an existing VPC in AWS Regions | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLoggingFromExistingVPCWithOIDC.template |
| Launch with a new VPC in AWS China Regions | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLoggingWithOIDC.template |
| Launch with an existing VPC in AWS China Regions | link:https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/CentralizedLoggingFromExistingVPCWithOIDC.template |

1. Under **Parameters**, review the parameters for the template and modify them as necessary.

1. Choose **Next**.

1. On Configure stack options page, choose Next.

1. On Review page, review and confirm the settings. Check the box: I acknowledge that AWS CloudFormation might create IAM resources.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **UPDATE\_COMPLETE** status in approximately 15 minutes.

 **Step 2. Refresh the web console**

Now you have completed all the upgrade steps. Choose the refresh button in your browser.
