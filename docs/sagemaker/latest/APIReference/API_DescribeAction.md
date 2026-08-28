---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAction.html
---

# DescribeAction
<a name="API_DescribeAction"></a>

Describes an action.

## Request Syntax
<a name="API_DescribeAction_RequestSyntax"></a>

```
{
   "ActionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActionName](#API_DescribeAction_RequestSyntax) **   <a name="sagemaker-DescribeAction-request-ActionName"></a>
The name of the action to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial|experiment-trial-component|artifact|action|context)\/)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,119})`
Required: Yes

## Response Syntax
<a name="API_DescribeAction_ResponseSyntax"></a>

```
{
   "ActionArn": "string",
   "ActionName": "string",
   "ActionType": "string",
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "CreationTime": number,
   "Description": "string",
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedTime": number,
   "LineageGroupArn": "string",
   "MetadataProperties": {
      "CommitId": "string",
      "GeneratedBy": "string",
      "ProjectId": "string",
      "Repository": "string"
   },
   "Properties": {
      "string" : "string"
   },
   "Source": {
      "SourceId": "string",
      "SourceType": "string",
      "SourceUri": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionArn](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-ActionArn"></a>
The Amazon Resource Name (ARN) of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:action/.*`

 ** [ActionName](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-ActionName"></a>
The name of the action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial|experiment-trial-component|artifact|action|context)\/)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,119})`

 ** [ActionType](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-ActionType"></a>
The type of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [CreatedBy](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-CreationTime"></a>
When the action was created.
Type: Timestamp

 ** [Description](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-Description"></a>
The description of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [LastModifiedBy](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-LastModifiedTime"></a>
When the action was last modified.
Type: Timestamp

 ** [LineageGroupArn](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [MetadataProperties](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object

 ** [Properties](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-Properties"></a>
A list of the action's properties.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`

 ** [Source](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-Source"></a>
The source of the action.
Type: [ActionSource](API_ActionSource.md) object

 ** [Status](#API_DescribeAction_ResponseSyntax) **   <a name="sagemaker-DescribeAction-response-Status"></a>
The status of the action.
Type: String
Valid Values: `Unknown | InProgress | Completed | Failed | Stopping | Stopped`

## Errors
<a name="API_DescribeAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
