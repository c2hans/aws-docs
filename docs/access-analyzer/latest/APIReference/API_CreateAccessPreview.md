---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAccessPreview.html
---

# CreateAccessPreview
<a name="API_CreateAccessPreview"></a>

Creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions.

## Request Syntax
<a name="API_CreateAccessPreview_RequestSyntax"></a>

```
PUT /access-preview HTTP/1.1
Content-type: application/json

{
   "analyzerArn": "{{string}}",
   "clientToken": "{{string}}",
   "configurations": {
      "{{string}}" : { ... }
   }
}
```

## URI Request Parameters
<a name="API_CreateAccessPreview_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessPreview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analyzerArn](#API_CreateAccessPreview_RequestSyntax) **   <a name="accessanalyzer-CreateAccessPreview-request-analyzerArn"></a>
The [ARN of the account analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview. You can only create an access preview for analyzers with an `Account` type and `Active` status.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [clientToken](#API_CreateAccessPreview_RequestSyntax) **   <a name="accessanalyzer-CreateAccessPreview-request-clientToken"></a>
A client token.
Type: String
Required: No

 ** [configurations](#API_CreateAccessPreview_RequestSyntax) **   <a name="accessanalyzer-CreateAccessPreview-request-configurations"></a>
Access control configuration for your resource that is used to generate the access preview. The access preview includes findings for external access allowed to the resource with the proposed access control configuration. The configuration must contain exactly one element.
Type: String to [Configuration](API_Configuration.md) object map
Required: Yes

## Response Syntax
<a name="API_CreateAccessPreview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string"
}
```

## Response Elements
<a name="API_CreateAccessPreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_CreateAccessPreview_ResponseSyntax) **   <a name="accessanalyzer-CreateAccessPreview-response-id"></a>
The unique ID for the access preview.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateAccessPreview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A conflict exception error.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Service quote met error.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 402

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateAccessPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CreateAccessPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CreateAccessPreview)
