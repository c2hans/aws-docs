---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ImageConfiguration.html
---

# ImageConfiguration
<a name="API_ImageConfiguration"></a>

Describes the configuration that AWS App Runner uses to run an App Runner service using an image pulled from a source image repository.

## Contents
<a name="API_ImageConfiguration_Contents"></a>

 ** Port **   <a name="apprunner-Type-ImageConfiguration-Port"></a>
The port that your application listens to in the container.
Default: `8080`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** RuntimeEnvironmentSecrets **   <a name="apprunner-Type-ImageConfiguration-RuntimeEnvironmentSecrets"></a>
An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
+  If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
+  Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** RuntimeEnvironmentVariables **   <a name="apprunner-Type-ImageConfiguration-RuntimeEnvironmentVariables"></a>
Environment variables that are available to your running App Runner service. An array of key-value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 51200.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 51200.
Value Pattern: `.*`
Required: No

 ** StartCommand **   <a name="apprunner-Type-ImageConfiguration-StartCommand"></a>
An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command.
Type: String
Pattern: `[^\x0a\x0d]+`
Required: No

## See Also
<a name="API_ImageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ImageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ImageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ImageConfiguration)
