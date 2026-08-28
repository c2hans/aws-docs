---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetFlowLogsIntegrationTemplate.html
---

# GetFlowLogsIntegrationTemplate
<a name="API_GetFlowLogsIntegrationTemplate"></a>

Generates a CloudFormation template that streamlines and automates the integration of VPC flow logs with Amazon Athena. This make it easier for you to query and gain insights from VPC flow logs data. Based on the information that you provide, we configure resources in the template to do the following:
+ Create a table in Athena that maps fields to a custom log format
+ Create a Lambda function that updates the table with new partitions on a daily, weekly, or monthly basis
+ Create a table partitioned between two timestamps in the past
+ Create a set of named queries in Athena that you can use to get started quickly

**Note**
 `GetFlowLogsIntegrationTemplate` does not support integration between AWS Transit Gateway Flow Logs and Amazon Athena.

## Request Parameters
<a name="API_GetFlowLogsIntegrationTemplate_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ConfigDeliveryS3DestinationArn**
To store the CloudFormation template in Amazon S3, specify the location in Amazon S3.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FlowLogId**
The ID of the flow log.
Type: String
Required: Yes

 **IntegrateService**
Information about the service integration.
Type: [IntegrateServices](API_IntegrateServices.md) object
Required: Yes

## Response Elements
<a name="API_GetFlowLogsIntegrationTemplate_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **result**
The generated CloudFormation template.
Type: String

## Errors
<a name="API_GetFlowLogsIntegrationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetFlowLogsIntegrationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
