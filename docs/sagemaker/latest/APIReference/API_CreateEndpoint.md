---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html
---

# CreateEndpoint
<a name="API_CreateEndpoint"></a>

Creates an endpoint using the endpoint configuration specified in the request. SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API.

 Use this API to deploy models using SageMaker hosting services.

**Note**
 You must not delete an `EndpointConfig` that is in use by an endpoint that is live or while the `UpdateEndpoint` or `CreateEndpoint` operations are being performed on the endpoint. To update an endpoint, you must create a new `EndpointConfig`.

The endpoint name must be unique within an AWS Region in your AWS account.

When it receives the request, SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them.

**Note**
When you call [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html), a load call is made to DynamoDB to verify that your endpoint configuration exists. When you read data from a DynamoDB table supporting [`Eventually Consistent Reads`](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), the response might not reflect the results of a recently completed write operation. The response might include some stale data. If the dependent entities are not yet in DynamoDB, this causes a validation error. If you repeat your read request after a short time, the response should return the latest data. So retry logic is recommended to handle these possible issues. We also recommend that customers call [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html) before calling [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) to minimize the potential impact of a DynamoDB eventually consistent read.

When SageMaker receives the request, it sets the endpoint status to `Creating`. After it creates the endpoint, it sets the status to `InService`. SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API.

If any of the models hosted at this endpoint get model data from an Amazon S3 location, SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provided. AWS STS is activated in your AWS account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see [Activating and Deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the * AWS Identity and Access Management User Guide*.

**Note**
 To add the IAM role policies for using this API operation, go to the [IAM console](https://console.aws.amazon.com/iam/), and choose Roles in the left navigation pane. Search the IAM role that you want to grant access to use the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) and [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API operations, add the following policies to the role.
Option 1: For a full SageMaker access, search and attach the `AmazonSageMakerFullAccess` policy.
Option 2: For granting a limited access to an IAM role, paste the following Action elements manually into the JSON file of the IAM role:
 `"Action": ["sagemaker:CreateEndpoint", "sagemaker:CreateEndpointConfig"]`
 `"Resource": [`
 `"arn:aws:sagemaker:region:account-id:endpoint/endpointName"`
 `"arn:aws:sagemaker:region:account-id:endpoint-config/endpointConfigName"`
 `]`
For more information, see [SageMaker API Permissions: Actions, Permissions, and Resources Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html).

## Request Syntax
<a name="API_CreateEndpoint_RequestSyntax"></a>

```
{
   "DeploymentConfig": {
      "AutoRollbackConfiguration": {
         "Alarms": [
            {
               "AlarmName": "{{string}}"
            }
         ]
      },
      "BlueGreenUpdatePolicy": {
         "MaximumExecutionTimeoutInSeconds": {{number}},
         "TerminationWaitInSeconds": {{number}},
         "TrafficRoutingConfiguration": {
            "CanarySize": {
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "LinearStepSize": {
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "Type": "{{string}}",
            "WaitIntervalInSeconds": {{number}}
         }
      },
      "RollingUpdatePolicy": {
         "MaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "MaximumExecutionTimeoutInSeconds": {{number}},
         "RollbackMaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "WaitIntervalInSeconds": {{number}}
      }
   },
   "EndpointConfigName": "{{string}}",
   "EndpointName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeploymentConfig](#API_CreateEndpoint_RequestSyntax) **   <a name="sagemaker-CreateEndpoint-request-DeploymentConfig"></a>
The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.
Type: [DeploymentConfig](API_DeploymentConfig.md) object
Required: No

 ** [EndpointConfigName](#API_CreateEndpoint_RequestSyntax) **   <a name="sagemaker-CreateEndpoint-request-EndpointConfigName"></a>
The name of an endpoint configuration. For more information, see [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EndpointName](#API_CreateEndpoint_RequestSyntax) **   <a name="sagemaker-CreateEndpoint-request-EndpointName"></a>
The name of the endpoint.The name must be unique within an AWS Region in your AWS account. The name is case-insensitive in `CreateEndpoint`, but the case is preserved and must be matched in [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Tags](#API_CreateEndpoint_RequestSyntax) **   <a name="sagemaker-CreateEndpoint-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateEndpoint_ResponseSyntax"></a>

```
{
   "EndpointArn": "string"
}
```

## Response Elements
<a name="API_CreateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointArn](#API_CreateEndpoint_ResponseSyntax) **   <a name="sagemaker-CreateEndpoint-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

## Errors
<a name="API_CreateEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateEndpoint)
