---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html
---

# CreateHostedConfigurationVersion
<a name="API_CreateHostedConfigurationVersion"></a>

Creates a new configuration in the AWS AppConfig hosted configuration store. If you're creating a feature flag, we recommend you familiarize yourself with the JSON schema for feature flag data. For more information, see [Type reference for AWS.AppConfig.FeatureFlags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_CreateHostedConfigurationVersion_RequestSyntax"></a>

```
POST /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}}/hostedconfigurationversions HTTP/1.1
Description: {{Description}}
Content-Type: {{ContentType}}
Latest-Version-Number: {{LatestVersionNumber}}
VersionLabel: {{VersionLabel}}

{{Content}}
```

## URI Request Parameters
<a name="API_CreateHostedConfigurationVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [ContentType](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-ContentType"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Description](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-Description"></a>
A description of the configuration.
Due to HTTP limitations, this field only supports ASCII characters.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LatestVersionNumber](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-LatestVersionNumber"></a>
An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.

 ** [VersionLabel](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-VersionLabel"></a>
An optional, user-defined label for the AWS AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, "v2.2.0".
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`

## Request Body
<a name="API_CreateHostedConfigurationVersion_RequestBody"></a>

The request accepts the following binary data.

 ** [Content](#API_CreateHostedConfigurationVersion_RequestSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-request-Content"></a>
The configuration data, as bytes.
 AWS AppConfig accepts any type of data, including text formats like JSON or TOML, or binary formats like protocol buffers or compressed data.
Required: Yes

## Response Syntax
<a name="API_CreateHostedConfigurationVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateHostedConfigurationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [ApplicationId](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-ApplicationId"></a>
The application ID.
Pattern: `[a-z0-9]{4,7}`

 ** [ConfigurationProfileId](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-ConfigurationProfileId"></a>
The configuration profile ID.
Pattern: `[a-z0-9]{4,7}`

 ** [ContentType](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-ContentType"></a>
A standard MIME type describing the format of the configuration content. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17).
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Description](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-Description"></a>
A description of the configuration.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [KmsKeyArn](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key that was used to encrypt this specific version of the configuration data in the AWS AppConfig hosted configuration store.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [VersionLabel](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-VersionLabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`

 ** [VersionNumber](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-VersionNumber"></a>
The configuration version.

The response returns the following as the HTTP body.

 ** [Content](#API_CreateHostedConfigurationVersion_ResponseSyntax) **   <a name="appconfig-CreateHostedConfigurationVersion-response-Content"></a>
The content of the configuration or the configuration data.

## Errors
<a name="API_CreateHostedConfigurationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** PayloadTooLargeException **
The configuration size is too large.
HTTP Status Code: 413

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateHostedConfigurationVersion_Examples"></a>

### Example
<a name="API_CreateHostedConfigurationVersion_Example_1"></a>

This example illustrates one usage of CreateHostedConfigurationVersion.

#### Sample Request
<a name="API_CreateHostedConfigurationVersion_Example_1_Request"></a>

```
POST /applications/abc1234/configurationprofiles/ur8hx2f/hostedconfigurationversions HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.create-hosted-configuration-version
X-Amz-Date: 20210917T184857Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210917/us-east-1/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 27

{ "Name": "ExampleApplication", "Id": ExampleID, "Rank": 7 }
```

#### Sample Response
<a name="API_CreateHostedConfigurationVersion_Example_1_Response"></a>

```
{
    "ApplicationId": "abc1234",
    "ConfigurationProfileId": "ur8hx2f",
    "VersionNumber": "1",
    "ContentType": "application/json"
}
```

## See Also
<a name="API_CreateHostedConfigurationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateHostedConfigurationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateHostedConfigurationVersion)
