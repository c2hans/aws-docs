---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateAnalysisTemplate.html
---

# UpdateAnalysisTemplate
<a name="API_UpdateAnalysisTemplate"></a>

Updates the analysis template metadata.

## Request Syntax
<a name="API_UpdateAnalysisTemplate_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/analysistemplates/{{analysisTemplateIdentifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAnalysisTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analysisTemplateIdentifier](#API_UpdateAnalysisTemplate_RequestSyntax) **   <a name="API-UpdateAnalysisTemplate-request-uri-analysisTemplateIdentifier"></a>
The identifier for the analysis template resource.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateAnalysisTemplate_RequestSyntax) **   <a name="API-UpdateAnalysisTemplate-request-uri-membershipIdentifier"></a>
The identifier for a membership resource.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateAnalysisTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateAnalysisTemplate_RequestSyntax) **   <a name="API-UpdateAnalysisTemplate-request-description"></a>
A new description for the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## Response Syntax
<a name="API_UpdateAnalysisTemplate_ResponseSyntax"></a>

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
<a name="API_UpdateAnalysisTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisTemplate](#API_UpdateAnalysisTemplate_ResponseSyntax) **   <a name="API-UpdateAnalysisTemplate-response-analysisTemplate"></a>
The analysis template.
Type: [AnalysisTemplate](API_AnalysisTemplate.md) object

## Errors
<a name="API_UpdateAnalysisTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

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
<a name="API_UpdateAnalysisTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateAnalysisTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateAnalysisTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
