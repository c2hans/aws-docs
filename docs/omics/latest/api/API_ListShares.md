---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListShares.html
---

# ListShares
<a name="API_ListShares"></a>

Retrieves the resource shares associated with an account. Use the filter parameter to retrieve a specific subset of the shares.

## Request Syntax
<a name="API_ListShares_RequestSyntax"></a>

```
POST /shares?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "resourceArns": [ "{{string}}" ],
      "status": [ "{{string}}" ],
      "type": [ "{{string}}" ]
   },
   "resourceOwner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListShares_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListShares_RequestSyntax) **   <a name="omics-ListShares-request-uri-maxResults"></a>
The maximum number of shares to return in one page of results.

 ** [nextToken](#API_ListShares_RequestSyntax) **   <a name="omics-ListShares-request-uri-nextToken"></a>
Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.

## Request Body
<a name="API_ListShares_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListShares_RequestSyntax) **   <a name="omics-ListShares-request-filter"></a>
Attributes that you use to filter for a specific subset of resource shares.
Type: [Filter](API_Filter.md) object
Required: No

 ** [resourceOwner](#API_ListShares_RequestSyntax) **   <a name="omics-ListShares-request-resourceOwner"></a>
The account that owns the resource shares.
Type: String
Valid Values: `SELF | OTHER`
Required: Yes

## Response Syntax
<a name="API_ListShares_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "shares": [
      {
         "creationTime": "string",
         "ownerId": "string",
         "principalSubscriber": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "shareId": "string",
         "shareName": "string",
         "status": "string",
         "statusMessage": "string",
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListShares_ResponseSyntax) **   <a name="omics-ListShares-response-nextToken"></a>
 Next token returned in the response of a previous ListSharesResponse call. Used to get the next page of results.
Type: String

 ** [shares](#API_ListShares_ResponseSyntax) **   <a name="omics-ListShares-response-shares"></a>
The shares available and their metadata details.
Type: Array of [ShareDetails](API_ShareDetails.md) objects

## Errors
<a name="API_ListShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListShares)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListShares)
