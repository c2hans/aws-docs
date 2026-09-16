---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html
---

# GetConfiguration
<a name="API_GetConfiguration"></a>

(Deprecated) Retrieves the latest deployed configuration.

**Important**
Note the following important information.
This API action is deprecated. Calls to receive configuration data should use the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html) and [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) APIs instead.
 [GetConfiguration](#API_GetConfiguration) is a priced call. For more information, see [Pricing](https://aws.amazon.com/systems-manager/pricing/).

## Request Syntax
<a name="API_GetConfiguration_RequestSyntax"></a>

```
GET /applications/{{Application}}/environments/{{Environment}}/configurations/{{Configuration}}?client_configuration_version={{ClientConfigurationVersion}}&client_id={{ClientId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Application](#API_GetConfiguration_RequestSyntax) **   <a name="appconfig-GetConfiguration-request-uri-Application"></a>
The application to get. Specify either the application name or the application ID.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ClientConfigurationVersion](#API_GetConfiguration_RequestSyntax) **   <a name="appconfig-GetConfiguration-request-uri-ClientConfigurationVersion"></a>
The configuration version returned in the most recent [GetConfiguration](#API_GetConfiguration) response.
 AWS AppConfig uses the value of the `ClientConfigurationVersion` parameter to identify the configuration version on your clients. If you don’t send `ClientConfigurationVersion` with each call to [GetConfiguration](#API_GetConfiguration), your clients receive the current configuration. You are charged each time your clients receive a configuration.
To avoid excess charges, we recommend you use the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html) and [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html) APIs, which track the client configuration version on your behalf. If you choose to continue using [GetConfiguration](#API_GetConfiguration), we recommend that you include the `ClientConfigurationVersion` value with every call to [GetConfiguration](#API_GetConfiguration). The value to use for `ClientConfigurationVersion` comes from the `ConfigurationVersion` attribute returned by [GetConfiguration](#API_GetConfiguration) when there is new or updated data, and should be saved for subsequent calls to [GetConfiguration](#API_GetConfiguration).
For more information about working with configurations, see [Retrieving feature flags and configuration data in AWS AppConfig](http://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html) in the * AWS AppConfig User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ClientId](#API_GetConfiguration_RequestSyntax) **   <a name="appconfig-GetConfiguration-request-uri-ClientId"></a>
The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AWS AppConfig to deploy the configuration in intervals, as defined in the deployment strategy.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Configuration](#API_GetConfiguration_RequestSyntax) **   <a name="appconfig-GetConfiguration-request-uri-Configuration"></a>
The configuration to get. Specify either the configuration name or the configuration ID.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Environment](#API_GetConfiguration_RequestSyntax) **   <a name="appconfig-GetConfiguration-request-uri-Environment"></a>
The environment to get. Specify either the environment name or the environment ID.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_GetConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Configuration-Version: {{ConfigurationVersion}}
Content-Type: {{ContentType}}

{{Content}}
```

## Response Elements
<a name="API_GetConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ConfigurationVersion](#API_GetConfiguration_ResponseSyntax) **   <a name="appconfig-GetConfiguration-response-ConfigurationVersion"></a>
The configuration version.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ContentType](#API_GetConfiguration_ResponseSyntax) **   <a name="appconfig-GetConfiguration-response-ContentType"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).

The response returns the following as the HTTP body.

 ** [Content](#API_GetConfiguration_ResponseSyntax) **   <a name="appconfig-GetConfiguration-response-Content"></a>
The content of the configuration or the configuration data.
The `Content` attribute only contains data if the system finds new or updated configuration data. If there is no new or updated data and `ClientConfigurationVersion` matches the version of the current configuration, AWS AppConfig returns a `204 No Content` HTTP response code and the `Content` value will be empty.

## Errors
<a name="API_GetConfiguration_Errors"></a>

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
<a name="API_GetConfiguration_Examples"></a>

### Example
<a name="API_GetConfiguration_Example_1"></a>

This example illustrates one usage of GetConfiguration.

#### Sample Request
<a name="API_GetConfiguration_Example_1_Request"></a>

```
GET /applications/test-application/environments/Example-Environment/configurations/Example-Configuration-Profile?client_id=test-id HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.get-configuration
X-Amz-Date: 20210917T215745Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210917/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetConfiguration_Example_1_Response"></a>

```
{
    "ConfigurationVersion": "1",
    "ContentType": "application/octet-stream"
}
```

## See Also
<a name="API_GetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetConfiguration)
