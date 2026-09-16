---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetContactAttributes.html
---

# GetContactAttributes
<a name="API_GetContactAttributes"></a>

Retrieves the contact attributes for the specified contact.

## Request Syntax
<a name="API_GetContactAttributes_RequestSyntax"></a>

```
GET /contact/attributes/{{InstanceId}}/{{InitialContactId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetContactAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InitialContactId](#API_GetContactAttributes_RequestSyntax) **   <a name="connect-GetContactAttributes-request-uri-InitialContactId"></a>
The identifier of the initial contact.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_GetContactAttributes_RequestSyntax) **   <a name="connect-GetContactAttributes-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetContactAttributes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetContactAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetContactAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_GetContactAttributes_ResponseSyntax) **   <a name="connect-GetContactAttributes-response-Attributes"></a>
Information about the attributes.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.

## Errors
<a name="API_GetContactAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_GetContactAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetContactAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetContactAttributes)
