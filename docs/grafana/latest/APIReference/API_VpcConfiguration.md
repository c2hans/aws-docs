---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.

**Note**
Provided `securityGroupIds` and `subnetIds` must be part of the same VPC.
Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="ManagedGrafana-Type-VpcConfiguration-securityGroupIds"></a>
The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** subnetIds **   <a name="ManagedGrafana-Type-VpcConfiguration-subnetIds"></a>
The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.
Type: Array of strings
Array Members: Minimum number of 2 items. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/VpcConfiguration)
