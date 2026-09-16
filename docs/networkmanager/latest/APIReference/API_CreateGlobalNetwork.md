---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateGlobalNetwork.html
---

# CreateGlobalNetwork
<a name="API_CreateGlobalNetwork"></a>

Creates a new, empty global network.

## Request Syntax
<a name="API_CreateGlobalNetwork_RequestSyntax"></a>

```
POST /global-networks HTTP/1.1
Content-type: application/json

{
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
<a name="API_CreateGlobalNetwork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGlobalNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateGlobalNetwork_RequestSyntax) **   <a name="networkmanager-CreateGlobalNetwork-request-Description"></a>
A description of the global network.
Constraints: Maximum length of 256 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Tags](#API_CreateGlobalNetwork_RequestSyntax) **   <a name="networkmanager-CreateGlobalNetwork-request-Tags"></a>
The tags to apply to the resource during creation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateGlobalNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GlobalNetwork": {
      "CreatedAt": number,
      "Description": "string",
      "GlobalNetworkArn": "string",
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
<a name="API_CreateGlobalNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlobalNetwork](#API_CreateGlobalNetwork_ResponseSyntax) **   <a name="networkmanager-CreateGlobalNetwork-response-GlobalNetwork"></a>
Information about the global network object.
Type: [GlobalNetwork](API_GlobalNetwork.md) object

## Errors
<a name="API_CreateGlobalNetwork_Errors"></a>

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
<a name="API_CreateGlobalNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateGlobalNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateGlobalNetwork)
