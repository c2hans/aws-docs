---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_TransitGatewayConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# TransitGatewayConfiguration
<a name="API_TransitGatewayConfiguration"></a>

The structure of the transit gateway and network configuration that is used to connect the kdb environment to an internal network.

## Contents
<a name="API_TransitGatewayConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** routableCIDRSpace **   <a name="finspace-Type-TransitGatewayConfiguration-routableCIDRSpace"></a>
The routing CIDR on behalf of kdb environment. It could be any "/26 range in the 100.64.0.0 CIDR space. After providing, it will be added to the customer's transit gateway routing table so that the traffics could be routed to kdb network.
Type: String
Required: Yes

 ** transitGatewayID **   <a name="finspace-Type-TransitGatewayConfiguration-transitGatewayID"></a>
The identifier of the transit gateway created by the customer to connect outbound traffics from kdb network to your internal network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** attachmentNetworkAclConfiguration **   <a name="finspace-Type-TransitGatewayConfiguration-attachmentNetworkAclConfiguration"></a>
 The rules that define how you manage the outbound traffic from kdb network to your internal network.
Type: Array of [NetworkACLEntry](API_NetworkACLEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_TransitGatewayConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/TransitGatewayConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/TransitGatewayConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/TransitGatewayConfiguration)
