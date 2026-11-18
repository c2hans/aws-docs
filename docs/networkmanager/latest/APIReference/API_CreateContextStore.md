---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateContextStore.html
---

# CreateContextStore
<a name="API_CreateContextStore"></a>

Creates a context store in a global network. A context store maintains context entries, such as security groups, subnets, and attachments, for the resources connected to the transit gateways that you associate with it.

The context store is in the `PENDING` state when it's created, and changes to `AVAILABLE` when it's ready to use.

## Request Syntax
<a name="API_CreateContextStore_RequestSyntax"></a>

```
POST /global-networks/{{globalNetworkId}}/context-stores HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateContextStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalNetworkId](#API_CreateContextStore_RequestSyntax) **   <a name="networkmanager-CreateContextStore-request-uri-GlobalNetworkId"></a>
The ID of the global network to create the context store in.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_CreateContextStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateContextStore_RequestSyntax) **   <a name="networkmanager-CreateContextStore-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Description](#API_CreateContextStore_RequestSyntax) **   <a name="networkmanager-CreateContextStore-request-Description"></a>
A description of the context store.
Constraints: Maximum length of 256 characters. Only printable ASCII characters are allowed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Tags](#API_CreateContextStore_RequestSyntax) **   <a name="networkmanager-CreateContextStore-request-Tags"></a>
The tags to apply to the context store during creation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateContextStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContextStore": {
      "ContextStoreArn": "string",
      "ContextStoreId": "string",
      "CreatedAt": number,
      "Description": "string",
      "GlobalNetworkId": "string",
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateContextStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextStore](#API_CreateContextStore_ResponseSyntax) **   <a name="networkmanager-CreateContextStore-response-ContextStore"></a>
Information about the context store.
Type: [ContextStore](API_ContextStore.md) object

## Errors
<a name="API_CreateContextStore_Errors"></a>

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
<a name="API_CreateContextStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateContextStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateContextStore)
