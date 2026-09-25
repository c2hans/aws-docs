---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ListTemplateSnapshots.html
---

# ListTemplateSnapshots
<a name="API_ListTemplateSnapshots"></a>

Lists the snapshots of the specified template.

## Request Syntax
<a name="API_ListTemplateSnapshots_RequestSyntax"></a>

```
GET /templates/{{templateIdentifier}}/snapshots?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTemplateSnapshots_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTemplateSnapshots_RequestSyntax) **   <a name="networksecuritymanager-ListTemplateSnapshots-request-uri-maxResults"></a>
The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned `nextToken` value in a subsequent call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTemplateSnapshots_RequestSyntax) **   <a name="networksecuritymanager-ListTemplateSnapshots-request-uri-nextToken"></a>
The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:/+=_-]+`

 ** [templateIdentifier](#API_ListTemplateSnapshots_RequestSyntax) **   <a name="networksecuritymanager-ListTemplateSnapshots-request-uri-templateIdentifier"></a>
The identifier of the template. This is the template's Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: Yes

## Request Body
<a name="API_ListTemplateSnapshots_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTemplateSnapshots_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "snapshots": [
      {
         "firewallType": "string",
         "hasPublishedVersion": boolean,
         "status": "string",
         "templateArn": "string",
         "templateId": "string",
         "templateName": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTemplateSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTemplateSnapshots_ResponseSyntax) **   <a name="networksecuritymanager-ListTemplateSnapshots-response-nextToken"></a>
The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:/+=_-]+`

 ** [snapshots](#API_ListTemplateSnapshots_ResponseSyntax) **   <a name="networksecuritymanager-ListTemplateSnapshots-response-snapshots"></a>
The snapshots of the template.
Type: Array of [TemplateSummary](API_TemplateSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListTemplateSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing failed because of an internal error in the service. This is a retryable error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Reduce your request rate and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation. For details, see the `reason` and `fieldList` members of the response.
 ** fieldList **
The list of request fields that failed validation, if any.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListTemplateSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/ListTemplateSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ListTemplateSnapshots)
