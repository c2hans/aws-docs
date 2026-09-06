---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrialComponent.html
---

# UpdateTrialComponent
<a name="API_UpdateTrialComponent"></a>

Updates one or more properties of a trial component.

## Request Syntax
<a name="API_UpdateTrialComponent_RequestSyntax"></a>

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
   "InputArtifactsToRemove": [ "{{string}}" ],
   "OutputArtifacts": {
      "{{string}}" : {
         "MediaType": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "OutputArtifactsToRemove": [ "{{string}}" ],
   "Parameters": {
      "{{string}}" : {
         "NumberValue": {{number}},
         "StringValue": "{{string}}"
      }
   },
   "ParametersToRemove": [ "{{string}}" ],
   "StartTime": {{number}},
   "Status": {
      "Message": "{{string}}",
      "PrimaryStatus": "{{string}}"
   },
   "TrialComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTrialComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DisplayName](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-DisplayName"></a>
The name of the component as displayed. The name doesn't need to be unique. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [EndTime](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-EndTime"></a>
When the component ended.
Type: Timestamp
Required: No

 ** [InputArtifacts](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-InputArtifacts"></a>
Replaces all of the component's input artifacts with the specified artifacts or adds new input artifacts. Existing input artifacts are replaced if the trial component is updated with an identical input artifact key.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** [InputArtifactsToRemove](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-InputArtifactsToRemove"></a>
The input artifacts to remove from the component.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [OutputArtifacts](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-OutputArtifacts"></a>
Replaces all of the component's output artifacts with the specified artifacts or adds new output artifacts. Existing output artifacts are replaced if the trial component is updated with an identical output artifact key.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** [OutputArtifactsToRemove](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-OutputArtifactsToRemove"></a>
The output artifacts to remove from the component.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [Parameters](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-Parameters"></a>
Replaces all of the component's hyperparameters with the specified hyperparameters or add new hyperparameters. Existing hyperparameters are replaced if the trial component is updated with an identical hyperparameter key.
Type: String to [TrialComponentParameterValue](API_TrialComponentParameterValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 300 items.
Key Length Constraints: Minimum length of 0. Maximum length of 320.
Key Pattern: `.*`
Required: No

 ** [ParametersToRemove](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-ParametersToRemove"></a>
The hyperparameters to remove from the component.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [StartTime](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-StartTime"></a>
When the component started.
Type: Timestamp
Required: No

 ** [Status](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-Status"></a>
The new status of the component.
Type: [TrialComponentStatus](API_TrialComponentStatus.md) object
Required: No

 ** [TrialComponentName](#API_UpdateTrialComponent_RequestSyntax) **   <a name="sagemaker-UpdateTrialComponent-request-TrialComponentName"></a>
The name of the component to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_UpdateTrialComponent_ResponseSyntax"></a>

```
{
   "TrialComponentArn": "string"
}
```

## Response Elements
<a name="API_UpdateTrialComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialComponentArn](#API_UpdateTrialComponent_ResponseSyntax) **   <a name="sagemaker-UpdateTrialComponent-response-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`

## Errors
<a name="API_UpdateTrialComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateTrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateTrialComponent)
