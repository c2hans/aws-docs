---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionProxyConfigurationDetails.html
---

# AwsEcsTaskDefinitionProxyConfigurationDetails
<a name="API_AwsEcsTaskDefinitionProxyConfigurationDetails"></a>

The configuration details for the App Mesh proxy.

## Contents
<a name="API_AwsEcsTaskDefinitionProxyConfigurationDetails_Contents"></a>

 ** ContainerName **   <a name="securityhub-Type-AwsEcsTaskDefinitionProxyConfigurationDetails-ContainerName"></a>
The name of the container that will serve as the App Mesh proxy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProxyConfigurationProperties **   <a name="securityhub-Type-AwsEcsTaskDefinitionProxyConfigurationDetails-ProxyConfigurationProperties"></a>
The set of network configuration parameters to provide to the Container Network Interface (CNI) plugin, specified as key-value pairs.
Type: Array of [AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails](API_AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails.md) objects
Required: No

 ** Type **   <a name="securityhub-Type-AwsEcsTaskDefinitionProxyConfigurationDetails-Type"></a>
The proxy type.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionProxyConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionProxyConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionProxyConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionProxyConfigurationDetails)
