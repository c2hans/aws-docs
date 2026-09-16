---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplate.html
---

# UpdateTemplate
<a name="API_UpdateTemplate"></a>

Updates a template from an existing Amazon Quick Sight analysis or another template.

## Request Syntax
<a name="API_UpdateTemplate_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/templates/{{TemplateId}} HTTP/1.1
Content-type: application/json

{
   "Definition": {
      "AnalysisDefaults": {
         "DefaultNewSheetConfiguration": { ... }
      },
      "CalculatedFields": [
         { ... }
      ],
      "ColumnConfigurations": [
         { ... }
      ],
      "DataSetConfigurations": [
         { ... }
      ],
      "FilterGroups": [
         { ... }
      ],
      "Options": {
         "CustomActionDefaults": { ... },
         "ExcludedDataSetArns": [ "{{string}}" ],
         "QBusinessInsightsStatus": "{{string}}",
         "Timezone": "{{string}}",
         "VisualMessages": { ... },
         "WeekStart": "{{string}}"
      },
      "ParameterDeclarations": [
         { ... }
      ],
      "QueryExecutionOptions": {
         "QueryExecutionMode": "{{string}}"
      },
      "Sheets": [
         { ... }
      ],
      "StaticFiles": [
         { ... }
      ],
      "TooltipSheets": [
         { ... }
      ],
      "TopicConfigurations": [
         { ... }
      ]
   },
   "Name": "{{string}}",
   "SourceEntity": {
      "SourceAnalysis": {
         "Arn": "{{string}}",
         "DataSetReferences": [
            {
               "DataSetArn": "{{string}}",
               "DataSetPlaceholder": "{{string}}"
            }
         ],
         "TopicReferences": [
            {
               "TopicArn": "{{string}}",
               "TopicPlaceholder": "{{string}}"
            }
         ]
      },
      "SourceTemplate": {
         "Arn": "{{string}}"
      }
   },
   "ValidationStrategy": {
      "Mode": "{{string}}"
   },
   "VersionDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [TemplateId](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-uri-TemplateId"></a>
The ID for the template.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Definition](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-Definition"></a>
The definition of a template.
A definition is the data model of all features in a Dashboard, Template, or Analysis.
Type: [TemplateVersionDefinition](API_TemplateVersionDefinition.md) object
Required: No

 ** [Name](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-Name"></a>
The name for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [SourceEntity](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-SourceEntity"></a>
The entity that you are using as a source when you update the template. In `SourceEntity`, you specify the type of object you're using as source: `SourceTemplate` for a template or `SourceAnalysis` for an analysis. Both of these require an Amazon Resource Name (ARN). For `SourceTemplate`, specify the ARN of the source template. For `SourceAnalysis`, specify the ARN of the source analysis. The `SourceTemplate` ARN can contain any AWS account and any Quick Sight-supported AWS Region;.
Use the `DataSetReferences` entity within `SourceTemplate` or `SourceAnalysis` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. Use the `TopicReferences` entity to list the replacement topics for the topic placeholders listed in the original. The schema in each topic must match its placeholder.
Type: [TemplateSourceEntity](API_TemplateSourceEntity.md) object
Required: No

 ** [ValidationStrategy](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-ValidationStrategy"></a>
The option to relax the validation needed to update a template with definition objects. This skips the validation step for specific errors.
Type: [ValidationStrategy](API_ValidationStrategy.md) object
Required: No

 ** [VersionDescription](#API_UpdateTemplate_RequestSyntax) **   <a name="QS-UpdateTemplate-request-VersionDescription"></a>
A description of the current template version that is being updated. Every time you call `UpdateTemplate`, you create a new version of the template. Each version of the template maintains a description of the version in the `VersionDescription` field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_UpdateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "RequestId": "string",
   "TemplateId": "string",
   "VersionArn": "string"
}
```

## Response Elements
<a name="API_UpdateTemplate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-Arn"></a>
The Amazon Resource Name (ARN) for the template.
Type: String

 ** [CreationStatus](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-CreationStatus"></a>
The creation status of the template.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

 ** [RequestId](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TemplateId](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-TemplateId"></a>
The ID for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [VersionArn](#API_UpdateTemplate_ResponseSyntax) **   <a name="QS-UpdateTemplate-response-VersionArn"></a>
The ARN for the template, including the version information of the first version.
Type: String

## Errors
<a name="API_UpdateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateTemplate)
