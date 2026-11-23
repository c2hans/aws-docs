---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListUpdates.html
---

# ListUpdates

Lists the updates on a gateway, link, or routing rule, newest first. To see flow updates, specify `linkId`. Results are paginated. Use `nextToken` to get the next page.

## Request Syntax
<a name="API_ListUpdates_RequestSyntax"></a>

```
GET /gateway/{{gatewayId}}/updates?linkId={{linkId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&ruleId={{ruleId}}&status={{status}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListUpdates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-linkId"></a>
The ID of a link on this gateway, to list only that link's updates. Omit both `linkId` and `ruleId` to list the gateway's own updates.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [maxResults](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-maxResults"></a>
The maximum number of results to return for each call. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-nextToken"></a>
If nextToken is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. A nextToken expires after 24 hours.
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [ruleId](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-ruleId"></a>
The ID of a routing rule, to list only that rule's updates. Requires `linkId`, because you address a rule through its link. A `ruleId` without `linkId` fails with ValidationException.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`

 ** [status](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-status"></a>
Lists only updates in this status.
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED`

 ** [type](#API_ListUpdates_RequestSyntax) **   <a name="rtbfabric-ListUpdates-request-uri-type"></a>
Lists only updates of this type.
Valid Values: `GATEWAY_CONFIG_UPDATE | LINK_CONFIG_UPDATE | LINK_FLOW_UPDATE | ROUTING_RULE_UPDATE`

## Request Body
<a name="API_ListUpdates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListUpdates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "updates": [
      {
         "createdAt": number,
         "status": "string",
         "type": "string",
         "updateId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUpdates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUpdates_ResponseSyntax) **   <a name="rtbfabric-ListUpdates-response-nextToken"></a>
If nextToken is returned, there are more results available. Keep calling while it's present, even when `updates` is empty.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [updates](#API_ListUpdates_ResponseSyntax) **   <a name="rtbfabric-ListUpdates-response-updates"></a>
The updates on this page.
Type: Array of [UpdateSummary](API_UpdateSummary.md) objects

## Errors
<a name="API_ListUpdates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/ListUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ListUpdates)
