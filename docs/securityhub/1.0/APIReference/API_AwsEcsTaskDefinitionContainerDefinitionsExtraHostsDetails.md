---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails"></a>

A hostname and IP address mapping to append to the **/etc/hosts** file on the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails_Contents"></a>

 ** Hostname **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails-Hostname"></a>
The hostname to use in the **/etc/hosts** entry.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IpAddress **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails-IpAddress"></a>
The IP address to use in the **/etc/hosts** entry.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails)
