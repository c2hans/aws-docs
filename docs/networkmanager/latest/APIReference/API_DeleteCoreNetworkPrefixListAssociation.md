---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteCoreNetworkPrefixListAssociation.html
---

# DeleteCoreNetworkPrefixListAssociation
<a name="API_DeleteCoreNetworkPrefixListAssociation"></a>

Deletes an association between a core network and a prefix list.

## Request Syntax
<a name="API_DeleteCoreNetworkPrefixListAssociation_RequestSyntax"></a>

```
DELETE /prefix-list/{{prefixListArn}}/core-network/{{coreNetworkId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCoreNetworkPrefixListAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreNetworkId](#API_DeleteCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-DeleteCoreNetworkPrefixListAssociation-request-uri-CoreNetworkId"></a>
The ID of the core network from which to delete the prefix list association.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [prefixListArn](#API_DeleteCoreNetworkPrefixListAssociation_RequestSyntax) **   <a name="networkmanager-DeleteCoreNetworkPrefixListAssociation-request-uri-PrefixListArn"></a>
The ARN of the prefix list to disassociate from the core network.
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_DeleteCoreNetworkPrefixListAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCoreNetworkPrefixListAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkId": "string",
   "PrefixListArn": "string"
}
```

## Response Elements
<a name="API_DeleteCoreNetworkPrefixListAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkId](#API_DeleteCoreNetworkPrefixListAssociation_ResponseSyntax) **   <a name="networkmanager-DeleteCoreNetworkPrefixListAssociation-response-CoreNetworkId"></a>
The ID of the core network from which the prefix list association was deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [PrefixListArn](#API_DeleteCoreNetworkPrefixListAssociation_ResponseSyntax) **   <a name="networkmanager-DeleteCoreNetworkPrefixListAssociation-response-PrefixListArn"></a>
The ARN of the prefix list that was disassociated from the core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`

## Errors
<a name="API_DeleteCoreNetworkPrefixListAssociation_Errors"></a>

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
<a name="API_DeleteCoreNetworkPrefixListAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/DeleteCoreNetworkPrefixListAssociation)
