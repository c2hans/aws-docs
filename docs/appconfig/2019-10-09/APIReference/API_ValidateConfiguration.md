---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ValidateConfiguration.html
---

# ValidateConfiguration
<a name="API_ValidateConfiguration"></a>

Uses the validators in a configuration profile to validate a configuration.

## Request Syntax
<a name="API_ValidateConfiguration_RequestSyntax"></a>

```
POST /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}}/validators?configuration_version={{ConfigurationVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ValidateConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_ValidateConfiguration_RequestSyntax) **   <a name="appconfig-ValidateConfiguration-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_ValidateConfiguration_RequestSyntax) **   <a name="appconfig-ValidateConfiguration-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [ConfigurationVersion](#API_ValidateConfiguration_RequestSyntax) **   <a name="appconfig-ValidateConfiguration-request-uri-ConfigurationVersion"></a>
The version of the configuration to validate.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Request Body
<a name="API_ValidateConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ValidateConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_ValidateConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_ValidateConfiguration_Errors"></a>

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
<a name="API_ValidateConfiguration_Examples"></a>

### Example
<a name="API_ValidateConfiguration_Example_1"></a>

This example illustrates one usage of ValidateConfiguration.

#### Sample Request
<a name="API_ValidateConfiguration_Example_1_Request"></a>

```
POST /applications/abc1234/configurationprofiles/ur8hx2f/validators?configuration_version=1 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.validate-configuration
X-Amz-Date: 20210920T214947Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_ValidateConfiguration_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_ValidateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ValidateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ValidateConfiguration)
