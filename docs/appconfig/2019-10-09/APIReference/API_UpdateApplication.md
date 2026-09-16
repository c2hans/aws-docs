---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates an application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{ApplicationId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_UpdateApplication_RequestSyntax) **   <a name="appconfig-UpdateApplication-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateApplication_RequestSyntax) **   <a name="appconfig-UpdateApplication-request-Description"></a>
A description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_UpdateApplication_RequestSyntax) **   <a name="appconfig-UpdateApplication-request-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Description": "string",
   "Id": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateApplication_ResponseSyntax) **   <a name="appconfig-UpdateApplication-response-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_UpdateApplication_ResponseSyntax) **   <a name="appconfig-UpdateApplication-response-Id"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Name](#API_UpdateApplication_ResponseSyntax) **   <a name="appconfig-UpdateApplication-response-Name"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_UpdateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_UpdateApplication_Examples"></a>

### Example
<a name="API_UpdateApplication_Example_1"></a>

This example illustrates one usage of UpdateApplication.

#### Sample Request
<a name="API_UpdateApplication_Example_1_Request"></a>

```
PATCH /applications/abc1234 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.update-application
X-Amz-Date: 20210920T212018Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 31

{
	"Name": "Example-Application"
}
```

#### Sample Response
<a name="API_UpdateApplication_Example_1_Response"></a>

```
{
    "Id": "abc1234",
    "Name": "Example-Application",
    "Description": "An application used for creating an example."
}
```

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateApplication)
