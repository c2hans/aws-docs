---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceVpcConfiguration.html
---

# DataSourceVpcConfiguration
<a name="API_DataSourceVpcConfiguration"></a>

Provides configuration information needed to connect to an Amazon VPC (Virtual Private Cloud).

## Contents
<a name="API_DataSourceVpcConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="qbusiness-Type-DataSourceVpcConfiguration-securityGroupIds"></a>
A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Q Business to connect to the data source.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

 ** subnetIds **   <a name="qbusiness-Type-DataSourceVpcConfiguration-subnetIds"></a>
A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_DataSourceVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataSourceVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataSourceVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataSourceVpcConfiguration)
