---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFlowDefinition.html
---

# CreateFlowDefinition
<a name="API_CreateFlowDefinition"></a>

Creates a flow definition.

## Request Syntax
<a name="API_CreateFlowDefinition_RequestSyntax"></a>

```
{
   "FlowDefinitionName": "{{string}}",
   "HumanLoopActivationConfig": {
      "HumanLoopActivationConditionsConfig": {
         "HumanLoopActivationConditions": "{{string}}"
      }
   },
   "HumanLoopConfig": {
      "HumanTaskUiArn": "{{string}}",
      "PublicWorkforceTaskPrice": {
         "AmountInUsd": {
            "Cents": {{number}},
            "Dollars": {{number}},
            "TenthFractionsOfACent": {{number}}
         }
      },
      "TaskAvailabilityLifetimeInSeconds": {{number}},
      "TaskCount": {{number}},
      "TaskDescription": "{{string}}",
      "TaskKeywords": [ "{{string}}" ],
      "TaskTimeLimitInSeconds": {{number}},
      "TaskTitle": "{{string}}",
      "WorkteamArn": "{{string}}"
   },
   "HumanLoopRequestSource": {
      "AwsManagedHumanLoopRequestSource": "{{string}}"
   },
   "OutputConfig": {
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateFlowDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FlowDefinitionName](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-FlowDefinitionName"></a>
The name of your flow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}`
Required: Yes

 ** [HumanLoopActivationConfig](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-HumanLoopActivationConfig"></a>
An object containing information about the events that trigger a human workflow.
Type: [HumanLoopActivationConfig](API_HumanLoopActivationConfig.md) object
Required: No

 ** [HumanLoopConfig](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-HumanLoopConfig"></a>
An object containing information about the tasks the human reviewers will perform.
Type: [HumanLoopConfig](API_HumanLoopConfig.md) object
Required: No

 ** [HumanLoopRequestSource](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-HumanLoopRequestSource"></a>
Container for configuring the source of human task requests. Use to specify if Amazon Rekognition or Amazon Textract is used as an integration source.
Type: [HumanLoopRequestSource](API_HumanLoopRequestSource.md) object
Required: No

 ** [OutputConfig](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-OutputConfig"></a>
An object containing information about where the human review results will be uploaded.
Type: [FlowDefinitionOutputConfig](API_FlowDefinitionOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the role needed to call other services on your behalf. For example, `arn:aws:iam::1234567890:role/service-role/AmazonSageMaker-ExecutionRole-20180111T151298`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateFlowDefinition_RequestSyntax) **   <a name="sagemaker-CreateFlowDefinition-request-Tags"></a>
An array of key-value pairs that contain metadata to help you categorize and organize a flow definition. Each tag consists of a key and a value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateFlowDefinition_ResponseSyntax"></a>

```
{
   "FlowDefinitionArn": "string"
}
```

## Response Elements
<a name="API_CreateFlowDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlowDefinitionArn](#API_CreateFlowDefinition_ResponseSyntax) **   <a name="sagemaker-CreateFlowDefinition-response-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition you create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:flow-definition/.*`

## Errors
<a name="API_CreateFlowDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateFlowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateFlowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateFlowDefinition)
