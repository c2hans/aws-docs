---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationAnalysisTemplate.html
---

# GetCollaborationAnalysisTemplate
<a name="API_GetCollaborationAnalysisTemplate"></a>

Retrieves an analysis template within a collaboration.

## Request Syntax
<a name="API_GetCollaborationAnalysisTemplate_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/analysistemplates/{{analysisTemplateArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollaborationAnalysisTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analysisTemplateArn](#API_GetCollaborationAnalysisTemplate_RequestSyntax) **   <a name="API-GetCollaborationAnalysisTemplate-request-uri-analysisTemplateArn"></a>
The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** [collaborationIdentifier](#API_GetCollaborationAnalysisTemplate_RequestSyntax) **   <a name="API-GetCollaborationAnalysisTemplate-request-uri-collaborationIdentifier"></a>
A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetCollaborationAnalysisTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollaborationAnalysisTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationAnalysisTemplate": {
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
      "creatorAccountId": "string",
      "description": "string",
      "errorMessageConfiguration": {
         "type": "string"
      },
      "format": "string",
      "id": "string",
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
<a name="API_GetCollaborationAnalysisTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationAnalysisTemplate](#API_GetCollaborationAnalysisTemplate_ResponseSyntax) **   <a name="API-GetCollaborationAnalysisTemplate-response-collaborationAnalysisTemplate"></a>
The analysis template within a collaboration.
Type: [CollaborationAnalysisTemplate](API_CollaborationAnalysisTemplate.md) object

## Errors
<a name="API_GetCollaborationAnalysisTemplate_Errors"></a>

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
<a name="API_GetCollaborationAnalysisTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GetCollaborationAnalysisTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
