---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrial.html
---

# CreateTrial
<a name="API_CreateTrial"></a>

Creates an SageMaker *trial*. A trial is a set of steps called *trial components* that produce a machine learning model. A trial is part of a single SageMaker *experiment*.

When you use SageMaker Studio or the SageMaker Python SDK, all experiments, trials, and trial components are automatically tracked, logged, and indexed. When you use the AWS SDK for Python (Boto), you must use the logging APIs provided by the SDK.

You can add tags to a trial and then use the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search for the tags.

To get a list of all your trials, call the [ListTrials](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html) API. To view a trial's properties, call the [DescribeTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html) API. To create a trial component, call the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) API.

## Request Syntax
<a name="API_CreateTrial_RequestSyntax"></a>

```
{
   "DisplayName": "{{string}}",
   "ExperimentName": "{{string}}",
   "MetadataProperties": {
      "CommitId": "{{string}}",
      "GeneratedBy": "{{string}}",
      "ProjectId": "{{string}}",
      "Repository": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrialName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrial_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DisplayName](#API_CreateTrial_RequestSyntax) **   <a name="sagemaker-CreateTrial-request-DisplayName"></a>
The name of the trial as displayed. The name doesn't need to be unique. If `DisplayName` isn't specified, `TrialName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [ExperimentName](#API_CreateTrial_RequestSyntax) **   <a name="sagemaker-CreateTrial-request-ExperimentName"></a>
The name of the experiment to associate the trial with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [MetadataProperties](#API_CreateTrial_RequestSyntax) **   <a name="sagemaker-CreateTrial-request-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** [Tags](#API_CreateTrial_RequestSyntax) **   <a name="sagemaker-CreateTrial-request-Tags"></a>
A list of tags to associate with the trial. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrialName](#API_CreateTrial_RequestSyntax) **   <a name="sagemaker-CreateTrial-request-TrialName"></a>
The name of the trial. The name must be unique in your AWS account and is not case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_CreateTrial_ResponseSyntax"></a>

```
{
   "TrialArn": "string"
}
```

## Response Elements
<a name="API_CreateTrial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialArn](#API_CreateTrial_ResponseSyntax) **   <a name="sagemaker-CreateTrial-response-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`

## Errors
<a name="API_CreateTrial_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTrial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTrial)
