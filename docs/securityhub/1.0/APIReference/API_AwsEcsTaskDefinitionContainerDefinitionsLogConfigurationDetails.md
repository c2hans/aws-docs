---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails"></a>

The log configuration specification for the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails_Contents"></a>

 ** LogDriver **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails-LogDriver"></a>
The log driver to use for the container.
Valid values on AWS Fargate are as follows:
+  `awsfirelens`
+  `awslogs`
+  `splunk`
Valid values on Amazon EC2 are as follows:
+  `awsfirelens`
+  `awslogs`
+  `fluentd`
+  `gelf`
+  `journald`
+  `json-file`
+  `logentries`
+  `splunk`
+  `syslog`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Options **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails-Options"></a>
The configuration options to send to the log driver. Requires version 1.19 of the Docker Remote API or greater on your container instance.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** SecretOptions **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails-SecretOptions"></a>
The secrets to pass to the log configuration.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails.md) objects
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails)
