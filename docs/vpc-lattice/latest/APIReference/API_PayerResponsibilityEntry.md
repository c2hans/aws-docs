---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_PayerResponsibilityEntry.html
---

# PayerResponsibilityEntry
<a name="API_PayerResponsibilityEntry"></a>

Specifies which account pays for a category of charges on a VPC endpoint association.

## Contents
<a name="API_PayerResponsibilityEntry_Contents"></a>

 ** payerResponsibilityType **   <a name="vpclattice-Type-PayerResponsibilityEntry-payerResponsibilityType"></a>
The account that pays this category of charges. `VpcEndpointAccount` owns the VPC endpoint. `ResourceGatewayAccount` owns the resource gateway.
Type: String
Valid Values: `VpcEndpointAccount | ResourceGatewayAccount`
Required: No

 ** scope **   <a name="vpclattice-Type-PayerResponsibilityEntry-scope"></a>
The category of charges that this entry applies to. `ResourceGatewayCharges` covers the resource gateway's data processing charge.
Type: String
Valid Values: `ResourceGatewayCharges`
Required: No

## See Also
<a name="API_PayerResponsibilityEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/PayerResponsibilityEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/PayerResponsibilityEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/PayerResponsibilityEntry)
