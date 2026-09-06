---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateAnalysisTemplate.html
---

# CreateAnalysisTemplate
<a name="API_CreateAnalysisTemplate"></a>

Creates a new analysis template.

## Request Syntax
<a name="API_CreateAnalysisTemplate_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/analysistemplates HTTP/1.1
Content-type: application/json

{
   "analysisParameters": [
      {
         "defaultValue": "{{string}}",
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "errorMessageConfiguration": {
      "type": "{{string}}"
   },
   "format": "{{string}}",
   "name": "{{string}}",
   "schema": {
      "referencedTables": [ "{{string}}" ]
   },
   "source": { ... },
   "syntheticDataParameters": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAnalysisTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-uri-membershipIdentifier"></a>
The identifier for a membership resource.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateAnalysisTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisParameters](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-analysisParameters"></a>
The parameters of the analysis template.
Type: Array of [AnalysisParameter](API_AnalysisParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [description](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-description"></a>
The description of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [errorMessageConfiguration](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-errorMessageConfiguration"></a>
The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to `DETAILED`, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.
Type: [ErrorMessageConfiguration](API_ErrorMessageConfiguration.md) object
Required: No

 ** [format](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-format"></a>
The format of the analysis template.
Type: String
Valid Values: `SQL | PYSPARK_1_0`
Required: Yes

 ** [name](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-name"></a>
The name of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** [schema](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-schema"></a>
A relation within an analysis.
Type: [AnalysisSchema](API_AnalysisSchema.md) object
Required: No

 ** [source](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-source"></a>
The information in the analysis template.
Type: [AnalysisSource](API_AnalysisSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [syntheticDataParameters](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-syntheticDataParameters"></a>
The parameters for generating synthetic data when running the analysis template.
Type: [SyntheticDataParameters](API_SyntheticDataParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_CreateAnalysisTemplate_RequestSyntax) **   <a name="API-CreateAnalysisTemplate-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAnalysisTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisTemplate": {
      "analysisParameters": [
         {
            "defaultValue": "string",
            "name": "string",
            "type": "string"
         }
      ],
      "arn": "string",
      "collaborationArn": "string",
      "collaborationId": "string",
      "createTime": number,
      "description": "string",
      "errorMessageConfiguration": {
         "type": "string"
      },
      "format": "string",
      "id": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "schema": {
         "referencedTables": [ "string" ]
      },
      "source": { ... },
      "sourceMetadata": { ... },
      "syntheticDataParameters": { ... },
      "updateTime": number,
      "validations": [
         {
            "reasons": [
               {
                  "message": "string"
               }
            ],
            "status": "string",
            "type": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateAnalysisTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisTemplate](#API_CreateAnalysisTemplate_ResponseSyntax) **   <a name="API-CreateAnalysisTemplate-response-analysisTemplate"></a>
The analysis template.
Type: [AnalysisTemplate](API_AnalysisTemplate.md) object

## Errors
<a name="API_CreateAnalysisTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateAnalysisTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateAnalysisTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateAnalysisTemplate)
