---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html
---

# ValidateConfigurationSettings
<a name="API_ValidateConfigurationSettings"></a>

Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.

This action returns a list of messages indicating any errors or warnings associated with the selection of option values.

## Request Parameters
<a name="API_ValidateConfigurationSettings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application that the configuration template or environment belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** EnvironmentName **
The name of the environment to validate the settings against.
Condition: You cannot specify both this and a configuration template name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 **OptionSettings.member.N**
A list of the options and desired values to evaluate.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: Yes

 ** TemplateName **
The name of the configuration template to validate the settings against.
Condition: You cannot specify both this and an environment name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_ValidateConfigurationSettings_ResponseElements"></a>

The following element is returned by the service.

 **Messages.member.N**
 A list of [ValidationMessage](API_ValidationMessage.md).
Type: Array of [ValidationMessage](API_ValidationMessage.md) objects

## Errors
<a name="API_ValidateConfigurationSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_ValidateConfigurationSettings_Examples"></a>

### Example
<a name="API_ValidateConfigurationSettings_Example_1"></a>

This example illustrates one usage of ValidateConfigurationSettings.

#### Sample Request
<a name="API_ValidateConfigurationSettings_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&EnvironmentName=SampleAppVersion
&OptionSettings.member.1.Namespace=aws%3Aautoscaling%3Atrigger
&OptionSettings.member.1.OptionName=LowerThreshold
&OptionSettings.member.1.Value=1000000
&Operation=ValidateConfigurationSettings
&AuthParams
```

#### Sample Response
<a name="API_ValidateConfigurationSettings_Example_1_Response"></a>

```
<ValidateConfigurationSettingsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ValidateConfigurationSettingsResult>
    <Messages/>
  </ValidateConfigurationSettingsResult>
  <ResponseMetadata>
    <RequestId>06f1cfff-f28f-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</ValidateConfigurationSettingsResponse>
```

## See Also
<a name="API_ValidateConfigurationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings)
