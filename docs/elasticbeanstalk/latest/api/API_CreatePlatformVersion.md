---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreatePlatformVersion.html
---

# CreatePlatformVersion
<a name="API_CreatePlatformVersion"></a>

Create a new version of your custom platform.

## Request Parameters
<a name="API_CreatePlatformVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentName **
The name of the builder environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 **OptionSettings.member.N**
The configuration option settings to apply to the builder environment.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 ** PlatformDefinitionBundle **
The location of the platform definition archive in Amazon S3.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** PlatformName **
The name of your custom platform.
Type: String
Required: Yes

 ** PlatformVersion **
The number, such as 1.0.2, for the new platform version.
Type: String
Required: Yes

 **Tags.member.N**
Specifies the tags applied to the new platform version.
Elastic Beanstalk applies these tags only to the platform version. Environments that you create using the platform version don't inherit the tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreatePlatformVersion_ResponseElements"></a>

The following elements are returned by the service.

 ** Builder **
The builder used to create the custom platform.
Type: [Builder](API_Builder.md) object

 ** PlatformSummary **
Detailed information about the new version of the custom platform.
Type: [PlatformSummary](API_PlatformSummary.md) object

## Errors
<a name="API_CreatePlatformVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyPlatforms **
You have exceeded the maximum number of allowed platforms associated with the account.
HTTP Status Code: 400

## See Also
<a name="API_CreatePlatformVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreatePlatformVersion)
