---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails"></a>

The FireLens configuration for the container. The configuration specifies and configures a log router for container logs.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails_Contents"></a>

 ** Options **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails-Options"></a>
The options to use to configure the log router.
The valid option keys are as follows:
+  `enable-ecs-log-metadata`. The value can be `true` or `false`.
+  `config-file-type`. The value can be `s3` or `file`.
+  `config-file-value`. The value is either an S3 ARN or a file path.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails-Type"></a>
The log router to use. Valid values are `fluentbit` or `fluentd`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails)
