---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html
---

# CreateTrialComponent
<a name="API_CreateTrialComponent"></a>

Creates a *trial component*, which is a stage of a machine learning *trial*. A trial is composed of one or more trial components. A trial component can be used in multiple trials.

Trial components include pre-processing jobs, training jobs, and batch transform jobs.

When you use SageMaker Studio or the SageMaker Python SDK, all experiments, trials, and trial components are automatically tracked, logged, and indexed. When you use the AWS SDK for Python (Boto), you must use the logging APIs provided by the SDK.

You can add tags to a trial component and then use the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search for the tags.

## Request Syntax
<a name="API_CreateTrialComponent_RequestSyntax"></a>

```
{
   "DisplayName": "{{string}}",
   "EndTime": {{number}},
   "InputArtifacts": {
      "{{string}}" : {
         "MediaType": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "MetadataProperties": {
      "CommitId": "{{string}}",
      "GeneratedBy": "{{string}}",
      "ProjectId": "{{string}}",
      "Repository": "{{string}}"
   },
   "OutputArtifacts": {
      "{{string}}" : {
         "MediaType": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "Parameters": {
      "{{string}}" : {
         "NumberValue": {{number}},
         "StringValue": "{{string}}"
      }
   },
   "StartTime": {{number}},
   "Status": {
      "Message": "{{string}}",
      "PrimaryStatus": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrialComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrialComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DisplayName](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-DisplayName"></a>
The name of the component as displayed. The name doesn't need to be unique. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [EndTime](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-EndTime"></a>
When the component ended.
Type: Timestamp
Required: No

 ** [InputArtifacts](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-InputArtifacts"></a>
The input artifacts for the component. Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** [MetadataProperties](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** [OutputArtifacts](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-OutputArtifacts"></a>
The output artifacts for the component. Examples of output artifacts are metrics, snapshots, logs, and images.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** [Parameters](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-Parameters"></a>
The hyperparameters for the component.
Type: String to [TrialComponentParameterValue](API_TrialComponentParameterValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 300 items.
Key Length Constraints: Minimum length of 0. Maximum length of 320.
Key Pattern: `.*`
Required: No

 ** [StartTime](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-StartTime"></a>
When the component started.
Type: Timestamp
Required: No

 ** [Status](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-Status"></a>
The status of the component. States include:
+ InProgress
+ Completed
+ Failed
Type: [TrialComponentStatus](API_TrialComponentStatus.md) object
Required: No

 ** [Tags](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-Tags"></a>
A list of tags to associate with the component. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrialComponentName](#API_CreateTrialComponent_RequestSyntax) **   <a name="sagemaker-CreateTrialComponent-request-TrialComponentName"></a>
The name of the component. The name must be unique in your AWS account and is not case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_CreateTrialComponent_ResponseSyntax"></a>

```
{
   "TrialComponentArn": "string"
}
```

## Response Elements
<a name="API_CreateTrialComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialComponentArn](#API_CreateTrialComponent_ResponseSyntax) **   <a name="sagemaker-CreateTrialComponent-response-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`

## Errors
<a name="API_CreateTrialComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTrialComponent)
