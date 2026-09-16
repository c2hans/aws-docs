---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateCoreNetworkPrefixListAssociation.html
---

# CreateCoreNetworkPrefixListAssociation
<a name="API_CreateCoreNetworkPrefixListAssociation"></a>

Creates an association between a core network and a prefix list for routing control.

## Request Syntax
<a name="API_CreateCoreNetworkPrefixListAssociation_RequestSyntax"></a>

```
POST /prefix-list HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CoreNetworkId": "{{string}}",
   "PrefixListAlias": "{{string}}",
   "PrefixListArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCoreNetworkPrefixListAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCoreNetworkPrefixListAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [CoreNetworkId](#API_CreateCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-request-CoreNetworkId"></a>
The ID of the core network to associate with the prefix list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [PrefixListAlias](#API_CreateCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-request-PrefixListAlias"></a>
An optional alias for the prefix list association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: Yes

 ** [PrefixListArn](#API_CreateCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-request-PrefixListArn"></a>
The ARN of the prefix list to associate with the core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_CreateCoreNetworkPrefixListAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkId": "string",
   "PrefixListAlias": "string",
   "PrefixListArn": "string"
}
```

## Response Elements
<a name="API_CreateCoreNetworkPrefixListAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkId](#API_CreateCoreNetworkPrefixListAssociation_ResponseSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-response-CoreNetworkId"></a>
The ID of the core network associated with the prefix list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [PrefixListAlias](#API_CreateCoreNetworkPrefixListAssociation_ResponseSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-response-PrefixListAlias"></a>
The alias of the prefix list association, if provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

 ** [PrefixListArn](#API_CreateCoreNetworkPrefixListAssociation_ResponseSyntax) **   <a name="networkmanager-CreateCoreNetworkPrefixListAssociation-response-PrefixListArn"></a>
The ARN of the prefix list that was associated with the core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`

## Errors
<a name="API_CreateCoreNetworkPrefixListAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
A service limit was exceeded.
 ** LimitCode **
The limit code.
 ** Message **
The error message.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
 ** ServiceCode **
The service code.
HTTP Status Code: 402

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
<a name="API_CreateCoreNetworkPrefixListAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateCoreNetworkPrefixListAssociation)
