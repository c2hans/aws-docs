---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateContextStore.html
---

# AssociateContextStore

Associates a transit gateway with a context store. The transit gateway must be registered with the global network of the context store, and can't be associated with more than one context store. The context store must be in the `AVAILABLE` state.

The association is in the `ASSOCIATING` state when it's created, and changes to `ASSOCIATED` when it's complete.

## Request Syntax
<a name="API_AssociateContextStore_RequestSyntax"></a>

```
POST /context-stores/{{contextStoreId}}/associations HTTP/1.1
Content-type: application/json

{
   "TransitGatewayArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateContextStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contextStoreId](#API_AssociateContextStore_RequestSyntax) **   <a name="networkmanager-AssociateContextStore-request-uri-ContextStoreId"></a>
The ID of the context store.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^context-store-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_AssociateContextStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TransitGatewayArn](#API_AssociateContextStore_RequestSyntax) **   <a name="networkmanager-AssociateContextStore-request-TransitGatewayArn"></a>
The Amazon Resource Name (ARN) of the transit gateway to associate with the context store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_AssociateContextStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContextStoreAssociation": {
      "ContextStoreId": "string",
      "CreatedAt": number,
      "State": "string",
      "TransitGatewayArn": "string"
   }
}
```

## Response Elements
<a name="API_AssociateContextStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextStoreAssociation](#API_AssociateContextStore_ResponseSyntax) **   <a name="networkmanager-AssociateContextStore-response-ContextStoreAssociation"></a>
Information about the context store association.
Type: [ContextStoreAssociation](API_ContextStoreAssociation.md) object

## Errors
<a name="API_AssociateContextStore_Errors"></a>

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
<a name="API_AssociateContextStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/AssociateContextStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AssociateContextStore)
