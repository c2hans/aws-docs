---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_VpcConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

Configuration details about the network where the Privatelink endpoint of the cluster resides.

## Contents
<a name="API_VpcConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ipAddressType **   <a name="finspace-Type-VpcConfiguration-ipAddressType"></a>
The IP address type for cluster network configuration parameters. The following type is available:
+ IP\_V4 – IP address version 4
Type: String
Valid Values: `IP_V4`
Required: No

 ** securityGroupIds **   <a name="finspace-Type-VpcConfiguration-securityGroupIds"></a>
The unique identifier of the VPC security group applied to the VPC endpoint ENI for the cluster.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^sg-([a-z0-9]{8}$|[a-z0-9]{17}$)`
Required: No

 ** subnetIds **   <a name="finspace-Type-VpcConfiguration-subnetIds"></a>
The identifier of the subnet that the Privatelink VPC endpoint uses to connect to the cluster.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^subnet-([a-z0-9]{8}$|[a-z0-9]{17}$)`
Required: No

 ** vpcId **   <a name="finspace-Type-VpcConfiguration-vpcId"></a>
The identifier of the VPC endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^vpc-([a-z0-9]{8}$|[a-z0-9]{17}$)`
Required: No

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/VpcConfiguration)
