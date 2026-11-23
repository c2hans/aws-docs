---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_PutLinkFlows.html
---

# PutLinkFlows

Replaces a link's flow configuration. For this release, use PutLinkFlows on the links of a responder gateway. The change applies asynchronously. The call returns once the change is accepted, and the link serves its prior flows until the update is applied. While the update rolls out, some requests can still run the prior flows. RTB Fabric validates the request before accepting it, and a request that fails validation changes nothing. After the call, use GetUpdate with the returned `updateId` to see whether the change succeeded. The link's status is ACTIVE again either way.

The call fails with AccessDeniedException when you don't have an active subscription for a module in the request. It fails with ServiceQuotaExceededException when the flow has more modules than your Modules per flow quota allows, or when a Rate Limiter Module sets `tps` above the link's TPS quota.

## Request Syntax
<a name="API_PutLinkFlows_RequestSyntax"></a>

```
PUT /gateway/{{gatewayId}}/link/{{linkId}}/flows HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "flows": [
      {
         "name": "{{string}}",
         "pipeline": { ... }
      }
   ],
   "lockToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutLinkFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_PutLinkFlows_RequestSyntax) **   <a name="rtbfabric-PutLinkFlows-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_PutLinkFlows_RequestSyntax) **   <a name="rtbfabric-PutLinkFlows-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_PutLinkFlows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutLinkFlows_RequestSyntax) **   <a name="rtbfabric-PutLinkFlows-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry with the same token and parameters, you get the original response without an error. If you retry with the same token but different parameters, the call fails with ValidationException. If you don't provide a token, the SDK generates one, and RTB Fabric remembers each clientToken for 8 hours. A retry returns the original `updateId` before `lockToken` is checked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [flows](#API_PutLinkFlows_RequestSyntax) **   <a name="rtbfabric-PutLinkFlows-request-flows"></a>
The link's flows, replacing the current ones. An empty list removes every flow.
Type: Array of [Flow](API_Flow.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** [lockToken](#API_PutLinkFlows_RequestSyntax) **   <a name="rtbfabric-PutLinkFlows-request-lockToken"></a>
The concurrency token that you read from GetLink. If the link changed since that read, by any operation, the call fails with ConflictException. The link must also be ACTIVE or ACCEPTED with no other change in progress. After a conflict, wait for that change to finish, read the link again, and retry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_PutLinkFlows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayId": "string",
   "linkId": "string",
   "status": "string",
   "updateId": "string"
}
```

## Response Elements
<a name="API_PutLinkFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayId](#API_PutLinkFlows_ResponseSyntax) **   <a name="rtbfabric-PutLinkFlows-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [linkId](#API_PutLinkFlows_ResponseSyntax) **   <a name="rtbfabric-PutLinkFlows-response-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [status](#API_PutLinkFlows_ResponseSyntax) **   <a name="rtbfabric-PutLinkFlows-response-status"></a>
The link's status. A successful call returns PENDING\_UPDATE, and the link serves its prior flows until the change completes.
Type: String
Valid Values: `PENDING_CREATION | PENDING_REQUEST | REQUESTED | ACCEPTED | ACTIVE | REJECTED | FAILED | PENDING_DELETION | DELETED | PENDING_UPDATE | PENDING_ISOLATION | ISOLATED | PENDING_RESTORATION | CREATE_FAILED | DELETE_FAILED`

 ** [updateId](#API_PutLinkFlows_ResponseSyntax) **   <a name="rtbfabric-PutLinkFlows-response-updateId"></a>
The ID of the update this call started.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `update-[a-z0-9]{1,57}`

## Errors
<a name="API_PutLinkFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because you exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_PutLinkFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/PutLinkFlows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/PutLinkFlows)
