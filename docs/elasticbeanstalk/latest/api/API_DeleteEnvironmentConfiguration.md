---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteEnvironmentConfiguration.html
---

# DeleteEnvironmentConfiguration
<a name="API_DeleteEnvironmentConfiguration"></a>

Deletes the draft configuration associated with the running environment.

Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using [DescribeConfigurationSettings](API_DescribeConfigurationSettings.md) while the update is in progress or if the update fails. The `DeploymentStatus` for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.

## Request Parameters
<a name="API_DeleteEnvironmentConfiguration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application the environment is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** EnvironmentName **
The name of the environment to delete the draft configuration from.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: Yes

## Errors
<a name="API_DeleteEnvironmentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteEnvironmentConfiguration_Examples"></a>

### Example
<a name="API_DeleteEnvironmentConfiguration_Example_1"></a>

This example illustrates one usage of DeleteEnvironmentConfiguration.

#### Sample Request
<a name="API_DeleteEnvironmentConfiguration_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&EnvironmentName=SampleApp
&Operation=DeleteEnvironmentConfiguration
&AuthParams
```

#### Sample Response
<a name="API_DeleteEnvironmentConfiguration_Example_1_Response"></a>

```
<DeleteEnvironmentConfigurationResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>fdf76507-f26d-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DeleteEnvironmentConfigurationResponse>
```

## See Also
<a name="API_DeleteEnvironmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration)
