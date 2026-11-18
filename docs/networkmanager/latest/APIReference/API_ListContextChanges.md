---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListContextChanges.html
---

# ListContextChanges
<a name="API_ListContextChanges"></a>

Returns the context entries that were added to or removed from a context store after the specified version. The context store must be in the `AVAILABLE` state.

## Request Syntax
<a name="API_ListContextChanges_RequestSyntax"></a>

```
GET /context-stores/{{contextStoreId}}/context-changes?fromVersionId={{FromVersionId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContextChanges_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contextStoreId](#API_ListContextChanges_RequestSyntax) **   <a name="networkmanager-ListContextChanges-request-uri-ContextStoreId"></a>
The ID of the context store.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^context-store-([0-9a-f]{8,17})$`
Required: Yes

 ** [FromVersionId](#API_ListContextChanges_RequestSyntax) **   <a name="networkmanager-ListContextChanges-request-uri-FromVersionId"></a>
The version to return changes from. Specify a version returned by `ListContexts`, `GetContextVersion`, or the `ToVersionId` of a previous `ListContextChanges` request. If the version is no longer available, the request fails, and you must call `ListContexts` to get the current context entries.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: Yes

 ** [MaxResults](#API_ListContextChanges_RequestSyntax) **   <a name="networkmanager-ListContextChanges-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListContextChanges_RequestSyntax) **   <a name="networkmanager-ListContextChanges-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListContextChanges_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContextChanges_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContextChanges": [
      {
         "ChangeType": "string",
         "Context": {
            "AttachmentType": "string",
            "AvailabilityZone": "string",
            "ContextId": "string",
            "ContextType": "string",
            "PublicId": "string",
            "Region": "string",
            "SegmentType": "string"
         }
      }
   ],
   "FromVersionId": "string",
   "NextToken": "string",
   "ToVersionId": "string"
}
```

## Response Elements
<a name="API_ListContextChanges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextChanges](#API_ListContextChanges_ResponseSyntax) **   <a name="networkmanager-ListContextChanges-response-ContextChanges"></a>
The context entries that were added or removed.
Type: Array of [ContextChange](API_ContextChange.md) objects

 ** [FromVersionId](#API_ListContextChanges_ResponseSyntax) **   <a name="networkmanager-ListContextChanges-response-FromVersionId"></a>
The version that the changes start from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

 ** [NextToken](#API_ListContextChanges_ResponseSyntax) **   <a name="networkmanager-ListContextChanges-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [ToVersionId](#API_ListContextChanges_ResponseSyntax) **   <a name="networkmanager-ListContextChanges-response-ToVersionId"></a>
The version that the changes bring the context entries up to. To get later changes, specify this value as `FromVersionId` in your next request. All pages of the same request return the same version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListContextChanges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_ListContextChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListContextChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListContextChanges)
