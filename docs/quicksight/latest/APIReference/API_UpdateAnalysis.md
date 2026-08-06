---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAnalysis.html
---

# UpdateAnalysis
<a name="API_UpdateAnalysis"></a>

Updates an analysis in Amazon Quick Sight

## Request Syntax
<a name="API_UpdateAnalysis_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/analyses/{{AnalysisId}} HTTP/1.1
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
      "DataSetIdentifierDeclarations": [
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
      "TopicIdentifierDeclarations": [
         { ... }
      ]
   },
   "Name": "{{string}}",
   "Parameters": {
      "DateTimeParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "DecimalParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "IntegerParameters": [
         {
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "StringParameters": [
         {
            "Name": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "SourceEntity": {
      "SourceTemplate": {
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
      }
   },
   "ThemeArn": "{{string}}",
   "ValidationStrategy": {
      "Mode": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateAnalysis_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-uri-AnalysisId"></a>
The ID for the analysis that you're updating. This ID displays in the URL of the analysis.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analysis that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAnalysis_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-Name"></a>
A descriptive name for the analysis that you're updating. This name displays for the analysis in the Amazon Quick Sight console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Definition](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-Definition"></a>
The definition of an analysis.
A definition is the data model of all features in a Dashboard, Template, or Analysis.
Type: [AnalysisDefinition](API_AnalysisDefinition.md) object
Required: No

 ** [Parameters](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-Parameters"></a>
The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values.
Type: [Parameters](API_Parameters.md) object
Required: No

 ** [SourceEntity](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-SourceEntity"></a>
A source entity to use for the analysis that you're updating. This metadata structure contains details that describe a source template and one or more datasets or topics.
Type: [AnalysisSourceEntity](API_AnalysisSourceEntity.md) object
Required: No

 ** [ThemeArn](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-ThemeArn"></a>
The Amazon Resource Name (ARN) for the theme to apply to the analysis that you're creating. To see the theme in the Amazon Quick Sight console, make sure that you have access to it.
Type: String
Required: No

 ** [ValidationStrategy](#API_UpdateAnalysis_RequestSyntax) **   <a name="QS-UpdateAnalysis-request-ValidationStrategy"></a>
The option to relax the validation needed to update an analysis with definition objects. This skips the validation step for specific errors.
Type: [ValidationStrategy](API_ValidationStrategy.md) object
Required: No

## Response Syntax
<a name="API_UpdateAnalysis_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisId": "string",
   "Arn": "string",
   "RequestId": "string",
   "UpdateStatus": "string"
}
```

## Response Elements
<a name="API_UpdateAnalysis_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAnalysis_ResponseSyntax) **   <a name="QS-UpdateAnalysis-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisId](#API_UpdateAnalysis_ResponseSyntax) **   <a name="QS-UpdateAnalysis-response-AnalysisId"></a>
The ID of the analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [Arn](#API_UpdateAnalysis_ResponseSyntax) **   <a name="QS-UpdateAnalysis-response-Arn"></a>
The ARN of the analysis that you're updating.
Type: String

 ** [RequestId](#API_UpdateAnalysis_ResponseSyntax) **   <a name="QS-UpdateAnalysis-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdateStatus](#API_UpdateAnalysis_ResponseSyntax) **   <a name="QS-UpdateAnalysis-response-UpdateStatus"></a>
The update status of the last update that was made to the analysis.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

## Errors
<a name="API_UpdateAnalysis_Errors"></a>

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
<a name="API_UpdateAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAnalysis)
