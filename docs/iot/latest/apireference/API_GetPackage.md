---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackage.html
---

# GetPackage
<a name="API_GetPackage"></a>

Gets information about the specified software package.

Requires permission to access the [GetPackage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetPackage_RequestSyntax"></a>

```
GET /packages/{{packageName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [packageName](#API_GetPackage_RequestSyntax) **   <a name="iot-GetPackage-request-uri-packageName"></a>
The name of the target software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_GetPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "defaultVersionName": "string",
   "description": "string",
   "lastModifiedDate": number,
   "packageArn": "string",
   "packageName": "string"
}
```

## Response Elements
<a name="API_GetPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-creationDate"></a>
The date the package was created.
Type: Timestamp

 ** [defaultVersionName](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-defaultVersionName"></a>
The name of the default package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`

 ** [description](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-description"></a>
The package description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\p{C}]+`

 ** [lastModifiedDate](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-lastModifiedDate"></a>
The date when the package was last updated.
Type: Timestamp

 ** [packageArn](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-packageArn"></a>
The ARN for the package.
Type: String

 ** [packageName](#API_GetPackage_ResponseSyntax) **   <a name="iot-GetPackage-response-packageName"></a>
The name of the software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`

## Errors
<a name="API_GetPackage_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetPackage)
