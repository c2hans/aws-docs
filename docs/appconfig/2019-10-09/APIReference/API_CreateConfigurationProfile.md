---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateConfigurationProfile.html
---

# CreateConfigurationProfile
<a name="API_CreateConfigurationProfile"></a>

Creates a configuration profile, which is information that enables AWS AppConfig to access the configuration source. Valid configuration sources include the following:
+ Configuration data in YAML, JSON, and other formats stored in the AWS AppConfig hosted configuration store
+ Configuration data stored as objects in an Amazon Simple Storage Service (Amazon S3) bucket
+ Pipelines stored in AWS CodePipeline
+ Secrets stored in AWS Secrets Manager
+ Standard and secure string parameters stored in AWS Systems Manager Parameter Store
+ Configuration data in SSM documents stored in the Systems Manager document store

A configuration profile includes the following information:
+ The URI location of the configuration data.
+ The AWS Identity and Access Management (IAM) role that provides access to the configuration data.
+ A validator for the configuration data. Available validators include either a JSON Schema or an AWS Lambda function.

For more information, see [Create a Configuration and a Configuration Profile](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_CreateConfigurationProfile_RequestSyntax"></a>

```
POST /applications/{{ApplicationId}}/configurationprofiles HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "KmsKeyIdentifier": "{{string}}",
   "LocationUri": "{{string}}",
   "Name": "{{string}}",
   "RetrievalRoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Type": "{{string}}",
   "Validators": [
      {
         "Content": "{{string}}",
         "Type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateConfigurationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_CreateConfigurationProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-Description"></a>
A description of the configuration profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [KmsKeyIdentifier](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-KmsKeyIdentifier"></a>
The identifier for an AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for `hosted` configuration types. The identifier can be an AWS KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [LocationUri](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-LocationUri"></a>
A URI to locate the configuration. You can specify the following:
+ For the AWS AppConfig hosted configuration store and for feature flags, specify `hosted`.
+ For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format `ssm-parameter://<parameter name>` or the ARN.
+ For an AWS CodePipeline pipeline, specify the URI in the following format: `codepipeline`://<pipeline name>.
+ For an AWS Secrets Manager secret, specify the URI in the following format: `secretsmanager`://<secret name>.
+ For an Amazon S3 object, specify the URI in the following format: `s3://<bucket>/<objectKey> `. Here is an example: `s3://amzn-s3-demo-bucket/my-app/us-east-1/my-config.json`
+ For an SSM document, specify either the document name in the format `ssm-document://<document name>` or the Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Name](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-Name"></a>
A name for the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [RetrievalRoleArn](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-RetrievalRoleArn"></a>
The ARN of an IAM role with permission to access the configuration at the specified `LocationUri`.
A retrieval role ARN is not required for configurations stored in AWS CodePipeline or the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`
Required: No

 ** [Tags](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-Tags"></a>
Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Type](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-Type"></a>
The type of configurations contained in the profile. AWS AppConfig supports `feature flags` and `freeform` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for `Type`:
 `AWS.AppConfig.FeatureFlags`
 `AWS.Freeform`
Type: String
Pattern: `^[a-zA-Z0-9\.\-]+`
Required: No

 ** [Validators](#API_CreateConfigurationProfile_RequestSyntax) **   <a name="appconfig-CreateConfigurationProfile-request-Validators"></a>
A list of methods for validating the configuration.
Type: Array of [Validator](API_Validator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## Response Syntax
<a name="API_CreateConfigurationProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateConfigurationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-Description"></a>
The configuration profile description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-Id"></a>
The configuration profile ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [KmsKeyArn](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for `hosted` configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [KmsKeyIdentifier](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-KmsKeyIdentifier"></a>
The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LocationUri](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-LocationUri"></a>
The URI location of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Name](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-Name"></a>
The name of the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [RetrievalRoleArn](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-RetrievalRoleArn"></a>
The ARN of an IAM role with permission to access the configuration at the specified `LocationUri`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`

 ** [Type](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-Type"></a>
The type of configurations contained in the profile. AWS AppConfig supports `feature flags` and `freeform` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for `Type`:
 `AWS.AppConfig.FeatureFlags`
 `AWS.Freeform`
Type: String
Pattern: `^[a-zA-Z0-9\.\-]+`

 ** [Validators](#API_CreateConfigurationProfile_ResponseSyntax) **   <a name="appconfig-CreateConfigurationProfile-response-Validators"></a>
A list of methods for validating the configuration.
Type: Array of [Validator](API_Validator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.

## Errors
<a name="API_CreateConfigurationProfile_Errors"></a>

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

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateConfigurationProfile_Examples"></a>

### Example
<a name="API_CreateConfigurationProfile_Example_1"></a>

This example illustrates one usage of CreateConfigurationProfile.

#### Sample Request
<a name="API_CreateConfigurationProfile_Example_1_Request"></a>

```
POST /applications/abc1234/configurationprofiles HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.create-configuration-profile
X-Amz-Date: 20210916T190059Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 171

{
	"Name": "Example-Configuration-Profile",
	"LocationUri": "ssm-parameter://Example-Parameter",
	"RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role"
}
```

#### Sample Response
<a name="API_CreateConfigurationProfile_Example_1_Response"></a>

```
{
	"ApplicationId": "abc1234",
	"Description": null,
	"Id": "ur8hx2f",
	"LocationUri": "ssm-parameter://Example-Parameter",
	"Name": "Example-Configuration-Profile",
	"RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role",
	"Type": null,
	"Validators": null
}
```

## See Also
<a name="API_CreateConfigurationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateConfigurationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateConfigurationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
