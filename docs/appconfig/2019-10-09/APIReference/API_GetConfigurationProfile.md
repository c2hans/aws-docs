---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfigurationProfile.html
---

# GetConfigurationProfile
<a name="API_GetConfigurationProfile"></a>

Retrieves information about a configuration profile.

## Request Syntax
<a name="API_GetConfigurationProfile_RequestSyntax"></a>

```
GET /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfigurationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_GetConfigurationProfile_RequestSyntax) **   <a name="appconfig-GetConfigurationProfile-request-uri-ApplicationId"></a>
The ID or name of the application that includes the configuration profile you want to get.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_GetConfigurationProfile_RequestSyntax) **   <a name="appconfig-GetConfigurationProfile-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile that you want to get.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_GetConfigurationProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfigurationProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Description": "string",
   "Id": "string",
   "KmsKeyArn": "string",
   "KmsKeyIdentifier": "string",
   "LocationUri": "string",
   "Name": "string",
   "RetrievalRoleArn": "string",
   "Type": "string",
   "Validators": [
      {
         "Content": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetConfigurationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-Description"></a>
The configuration profile description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-Id"></a>
The configuration profile ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [KmsKeyArn](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for `hosted` configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [KmsKeyIdentifier](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-KmsKeyIdentifier"></a>
The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LocationUri](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-LocationUri"></a>
The URI location of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Name](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-Name"></a>
The name of the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [RetrievalRoleArn](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-RetrievalRoleArn"></a>
The ARN of an IAM role with permission to access the configuration at the specified `LocationUri`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`

 ** [Type](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-Type"></a>
The type of configurations contained in the profile. AWS AppConfig supports `feature flags` and `freeform` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for `Type`:
 `AWS.AppConfig.FeatureFlags`
 `AWS.Freeform`
Type: String
Pattern: `^[a-zA-Z0-9\.\-]+`

 ** [Validators](#API_GetConfigurationProfile_ResponseSyntax) **   <a name="appconfig-GetConfigurationProfile-response-Validators"></a>
A list of methods for validating the configuration.
Type: Array of [Validator](API_Validator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.

## Errors
<a name="API_GetConfigurationProfile_Errors"></a>

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
<a name="API_GetConfigurationProfile_Examples"></a>

### Example
<a name="API_GetConfigurationProfile_Example_1"></a>

This example illustrates one usage of GetConfigurationProfile.

#### Sample Request
<a name="API_GetConfigurationProfile_Example_1_Request"></a>

```
GET /applications/abc1234/configurationprofiles/ur8hx2f HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.get-configuration-profile
X-Amz-Date: 20210917T221417Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210917/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetConfigurationProfile_Example_1_Response"></a>

```
{
    "ApplicationId": "abc1234",
    "Id": "ur8hx2f",
    "Name": "Example-Configuration-Profile",
    "LocationUri": "ssm-parameter://Example-Parameter",
    "RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role"
}
```

## See Also
<a name="API_GetConfigurationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetConfigurationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetConfigurationProfile)
