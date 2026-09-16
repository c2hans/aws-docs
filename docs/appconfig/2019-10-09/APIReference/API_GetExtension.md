---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExtension.html
---

# GetExtension
<a name="API_GetExtension"></a>

Returns information about an AWS AppConfig extension.

## Request Syntax
<a name="API_GetExtension_RequestSyntax"></a>

```
GET /extensions/{{ExtensionIdentifier}}?version_number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetExtension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtensionIdentifier](#API_GetExtension_RequestSyntax) **   <a name="appconfig-GetExtension-request-uri-ExtensionIdentifier"></a>
The name, the ID, or the Amazon Resource Name (ARN) of the extension.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [VersionNumber](#API_GetExtension_RequestSyntax) **   <a name="appconfig-GetExtension-request-uri-VersionNumber"></a>
The extension version number. If no version number was defined, AWS AppConfig uses the highest version.

## Request Body
<a name="API_GetExtension_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExtension_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Actions": {
      "string" : [
         {
            "Description": "string",
            "Name": "string",
            "RoleArn": "string",
            "Uri": "string"
         }
      ]
   },
   "Arn": "string",
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "Parameters": {
      "string" : {
         "Description": "string",
         "Dynamic": boolean,
         "Required": boolean
      }
   },
   "VersionNumber": number
}
```

## Response Elements
<a name="API_GetExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Actions](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Actions"></a>
The actions defined in the extension.
Type: String to array of [Action](API_Action.md) objects map
Map Entries: Maximum number of 5 items.
Valid Keys: `PRE_CREATE_HOSTED_CONFIGURATION_VERSION | PRE_START_DEPLOYMENT | AT_DEPLOYMENT_TICK | ON_DEPLOYMENT_START | ON_DEPLOYMENT_STEP | ON_DEPLOYMENT_BAKING | ON_DEPLOYMENT_COMPLETE | ON_DEPLOYMENT_ROLLED_BACK`
Array Members: Fixed number of 1 item.

 ** [Arn](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Arn"></a>
The system-generated Amazon Resource Name (ARN) for the extension.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [Description](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Description"></a>
Information about the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Id"></a>
The system-generated ID of the extension.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Name](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Name"></a>
The extension name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Parameters](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-Parameters"></a>
The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the `CreateExtensionAssociation` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
Type: String to [Parameter](API_Parameter.md) object map
Map Entries: Maximum number of 10 items.
Key Pattern: `^[^\/#:\n]{1,64}$`

 ** [VersionNumber](#API_GetExtension_ResponseSyntax) **   <a name="appconfig-GetExtension-response-VersionNumber"></a>
The extension version number.
Type: Integer

## Errors
<a name="API_GetExtension_Errors"></a>

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
<a name="API_GetExtension_Examples"></a>

### Example
<a name="API_GetExtension_Example_1"></a>

This example illustrates one usage of GetExtension.

#### Sample Request
<a name="API_GetExtension_Example_1_Request"></a>

```
GET /extensions/my-test-extension HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.get-extension
X-Amz-Date: 20220803T220925Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetExtension_Example_1_Response"></a>

```
{
	"Actions": {
		"PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [{
			"Description": null,
			"Name": "S3backup",
			"RoleArn": "arn:aws:iam::111122223333:role/mytestextensionrole",
			"Uri": "arn:aws:lambda:us-west-2:111122223333:function:mytestfunction"
		}]
	}
```

## See Also
<a name="API_GetExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetExtension)
