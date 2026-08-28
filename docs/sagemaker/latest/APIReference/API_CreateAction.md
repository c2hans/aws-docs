---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAction.html
---

# CreateAction
<a name="API_CreateAction"></a>

Creates an *action*. An action is a lineage tracking entity that represents an action or activity. For example, a model deployment or an HPO job. Generally, an action involves at least one input or output artifact. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Request Syntax
<a name="API_CreateAction_RequestSyntax"></a>

```
{
   "ActionName": "{{string}}",
   "ActionType": "{{string}}",
   "Description": "{{string}}",
   "MetadataProperties": {
      "CommitId": "{{string}}",
      "GeneratedBy": "{{string}}",
      "ProjectId": "{{string}}",
      "Repository": "{{string}}"
   },
   "Properties": {
      "{{string}}" : "{{string}}"
   },
   "Source": {
      "SourceId": "{{string}}",
      "SourceType": "{{string}}",
      "SourceUri": "{{string}}"
   },
   "Status": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActionName](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-ActionName"></a>
The name of the action. Must be unique to your account in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [ActionType](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-ActionType"></a>
The action type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [Description](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-Description"></a>
The description of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [MetadataProperties](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** [Properties](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-Properties"></a>
A list of properties to add to the action.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** [Source](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-Source"></a>
The source type, ID, and URI.
Type: [ActionSource](API_ActionSource.md) object
Required: Yes

 ** [Status](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-Status"></a>
The status of the action.
Type: String
Valid Values: `Unknown | InProgress | Completed | Failed | Stopping | Stopped`
Required: No

 ** [Tags](#API_CreateAction_RequestSyntax) **   <a name="sagemaker-CreateAction-request-Tags"></a>
A list of tags to apply to the action.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAction_ResponseSyntax"></a>

```
{
   "ActionArn": "string"
}
```

## Response Elements
<a name="API_CreateAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionArn](#API_CreateAction_ResponseSyntax) **   <a name="sagemaker-CreateAction-response-ActionArn"></a>
The Amazon Resource Name (ARN) of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:action/.*`

## Errors
<a name="API_CreateAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
