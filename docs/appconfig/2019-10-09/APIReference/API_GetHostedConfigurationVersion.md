---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetHostedConfigurationVersion.html
---

# GetHostedConfigurationVersion
<a name="API_GetHostedConfigurationVersion"></a>

Retrieves information about a specific configuration version.

## Request Syntax
<a name="API_GetHostedConfigurationVersion_RequestSyntax"></a>

```
GET /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}}/hostedconfigurationversions/{{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHostedConfigurationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_GetHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_GetHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [VersionNumber](#API_GetHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-request-uri-VersionNumber"></a>
The version.
Required: Yes

## Request Body
<a name="API_GetHostedConfigurationVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHostedConfigurationVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Application-Id: {{ApplicationId}}
Configuration-Profile-Id: {{ConfigurationProfileId}}
Version-Number: {{VersionNumber}}
Description: {{Description}}
Content-Type: {{ContentType}}
VersionLabel: {{VersionLabel}}
KmsKeyArn: {{KmsKeyArn}}

{{Content}}
```

## Response Elements
<a name="API_GetHostedConfigurationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ApplicationId](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-ApplicationId"></a>
The application ID.
Pattern: `[a-z0-9]{4,7}`

 ** [ConfigurationProfileId](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-ConfigurationProfileId"></a>
The configuration profile ID.
Pattern: `[a-z0-9]{4,7}`

 ** [ContentType](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-ContentType"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Description](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-Description"></a>
A description of the configuration.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [KmsKeyArn](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key that was used to encrypt this specific version of the configuration data in the AWS AppConfig hosted configuration store.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [VersionLabel](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-VersionLabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`

 ** [VersionNumber](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-VersionNumber"></a>
The configuration version.

The response returns the following as the HTTP body.

 ** [Content](#API_GetHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-GetHostedConfigurationVersion-response-Content"></a>
The content of the configuration or the configuration data.

## Errors
<a name="API_GetHostedConfigurationVersion_Errors"></a>

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
<a name="API_GetHostedConfigurationVersion_Examples"></a>

### Example
<a name="API_GetHostedConfigurationVersion_Example_1"></a>

This example illustrates one usage of GetHostedConfigurationVersion.

#### Sample Request
<a name="API_GetHostedConfigurationVersion_Example_1_Request"></a>

```
GET /applications/abc1234/configurationprofiles/ur8hx2f/hostedconfigurationversions/1 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.get-hosted-configuration-version
X-Amz-Date: 20210917T224843Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210917/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetHostedConfigurationVersion_Example_1_Response"></a>

```
{
    "ApplicationId": "abc1234",
    "ConfigurationProfileId": "ur8hx2f",
    "VersionNumber": "1",
    "ContentType": "application/json"
}
```

## See Also
<a name="API_GetHostedConfigurationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetHostedConfigurationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetHostedConfigurationVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
