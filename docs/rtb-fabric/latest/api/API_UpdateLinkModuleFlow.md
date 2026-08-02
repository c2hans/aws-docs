---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkModuleFlow.html
---

# UpdateLinkModuleFlow
<a name="API_UpdateLinkModuleFlow"></a>

Updates a link module flow.

## Request Syntax
<a name="API_UpdateLinkModuleFlow_RequestSyntax"></a>

```
POST /gateway/{{gatewayId}}/link/{{linkId}}/module-flow HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "modules": [
      {
         "dependsOn": [ "{{string}}" ],
         "moduleParameters": { ... },
         "name": "{{string}}",
         "version": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateLinkModuleFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_UpdateLinkModuleFlow_RequestSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_UpdateLinkModuleFlow_RequestSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_UpdateLinkModuleFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateLinkModuleFlow_RequestSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `clientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: Yes

 ** [modules](#API_UpdateLinkModuleFlow_RequestSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-request-modules"></a>
The configuration of a module.
Type: Array of [ModuleConfiguration](API_ModuleConfiguration.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateLinkModuleFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayId": "string",
   "linkId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateLinkModuleFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayId](#API_UpdateLinkModuleFlow_ResponseSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [linkId](#API_UpdateLinkModuleFlow_ResponseSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-response-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [status](#API_UpdateLinkModuleFlow_ResponseSyntax) **   <a name="rtbfabric-UpdateLinkModuleFlow-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | PENDING_REQUEST | REQUESTED | ACCEPTED | ACTIVE | REJECTED | FAILED | PENDING_DELETION | DELETED | PENDING_UPDATE | PENDING_ISOLATION | ISOLATED | PENDING_RESTORATION`

## Errors
<a name="API_UpdateLinkModuleFlow_Errors"></a>

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
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLinkModuleFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateLinkModuleFlow)
