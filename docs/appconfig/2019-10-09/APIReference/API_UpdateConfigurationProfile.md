---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateConfigurationProfile.html
---

# UpdateConfigurationProfile
<a name="API_UpdateConfigurationProfile"></a>

Updates a configuration profile.

## Request Syntax
<a name="API_UpdateConfigurationProfile_RequestSyntax"></a>

```
PATCH /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "KmsKeyIdentifier": "{{string}}",
   "Name": "{{string}}",
   "RetrievalRoleArn": "{{string}}",
   "Validators": [
      {
         "Content": "{{string}}",
         "Type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_UpdateConfigurationProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-Description"></a>
A description of the configuration profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [KmsKeyIdentifier](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-KmsKeyIdentifier"></a>
The identifier for a AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for `hosted` configuration types. The identifier can be an AWS KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [Name](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-Name"></a>
The name of the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [RetrievalRoleArn](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-RetrievalRoleArn"></a>
The ARN of an IAM role with permission to access the configuration at the specified `LocationUri`.
A retrieval role ARN is not required for configurations stored in AWS CodePipeline or the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`
Required: No

 ** [Validators](#API_UpdateConfigurationProfile_RequestSyntax) **   <a name="appconfig-UpdateConfigurationProfile-request-Validators"></a>
A list of methods for validating the configuration.
Type: Array of [Validator](API_Validator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## Response Syntax
<a name="API_UpdateConfigurationProfile_ResponseSyntax"></a>

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
<a name="API_UpdateConfigurationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-Description"></a>
The configuration profile description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-Id"></a>
The configuration profile ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [KmsKeyArn](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for `hosted` configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [KmsKeyIdentifier](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-KmsKeyIdentifier"></a>
The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LocationUri](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-LocationUri"></a>
The URI location of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Name](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-Name"></a>
The name of the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [RetrievalRoleArn](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-RetrievalRoleArn"></a>
The ARN of an IAM role with permission to access the configuration at the specified `LocationUri`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`

 ** [Type](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-Type"></a>
The type of configurations contained in the profile. AWS AppConfig supports `feature flags` and `freeform` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for `Type`:
 `AWS.AppConfig.FeatureFlags`
 `AWS.Freeform`
Type: String
Pattern: `^[a-zA-Z0-9\.\-]+`

 ** [Validators](#API_UpdateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-UpdateConfigurationProfile-response-Validators"></a>
A list of methods for validating the configuration.
Type: Array of [Validator](API_Validator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.

## Errors
<a name="API_UpdateConfigurationProfile_Errors"></a>

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
<a name="API_UpdateConfigurationProfile_Examples"></a>

### Example
<a name="API_UpdateConfigurationProfile_Example_1"></a>

This example illustrates one usage of UpdateConfigurationProfile.

#### Sample Request
<a name="API_UpdateConfigurationProfile_Example_1_Request"></a>

```
PATCH /applications/abc1234/configurationprofiles/ur8hx2f HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.update-configuration-profile
X-Amz-Date: 20210920T213335Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 59

{
    "Description": "Configuration profile used for examples."
}
```

#### Sample Response
<a name="API_UpdateConfigurationProfile_Example_1_Response"></a>

```
{
    "ApplicationId": "abc1234",
    "Id": "ur8hx2f",
    "Name": "Example-Configuration-Profile",
    "Description": "Configuration profile used for examples.",
    "LocationUri": "ssm-parameter://Example-Parameter",
    "RetrievalRoleArn": "arn:aws:iam::682428703967:role/Example-App-Config-Role"
}
```

## See Also
<a name="API_UpdateConfigurationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateConfigurationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateConfigurationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
