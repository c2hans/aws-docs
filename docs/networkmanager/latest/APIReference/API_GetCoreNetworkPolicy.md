---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCoreNetworkPolicy.html
---

# GetCoreNetworkPolicy
<a name="API_GetCoreNetworkPolicy"></a>

Returns details about a core network policy. You can get details about your current live policy or any previous policy version.

## Request Syntax
<a name="API_GetCoreNetworkPolicy_RequestSyntax"></a>

```
GET /core-networks/{{coreNetworkId}}/core-network-policy?alias={{Alias}}&policyVersionId={{PolicyVersionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCoreNetworkPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Alias](#API_GetCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-GetCoreNetworkPolicy-request-uri-Alias"></a>
The alias of a core network policy
Valid Values: `LIVE | LATEST`

 ** [coreNetworkId](#API_GetCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-GetCoreNetworkPolicy-request-uri-CoreNetworkId"></a>
The ID of a core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [PolicyVersionId](#API_GetCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-GetCoreNetworkPolicy-request-uri-PolicyVersionId"></a>
The ID of a core network policy version.

## Request Body
<a name="API_GetCoreNetworkPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCoreNetworkPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkPolicy": {
      "Alias": "string",
      "ChangeSetState": "string",
      "CoreNetworkId": "string",
      "CreatedAt": number,
      "Description": "string",
      "PolicyDocument": "string",
      "PolicyErrors": [
         {
            "ErrorCode": "string",
            "Message": "string",
            "Path": "string"
         }
      ],
      "PolicyVersionId": number
   }
}
```

## Response Elements
<a name="API_GetCoreNetworkPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkPolicy](#API_GetCoreNetworkPolicy_ResponseSyntax) **   <a name="networkmanager-GetCoreNetworkPolicy-response-CoreNetworkPolicy"></a>
The details about a core network policy.
Type: [CoreNetworkPolicy](API_CoreNetworkPolicy.md) object

## Errors
<a name="API_GetCoreNetworkPolicy_Errors"></a>

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
<a name="API_GetCoreNetworkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetCoreNetworkPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetCoreNetworkPolicy)
