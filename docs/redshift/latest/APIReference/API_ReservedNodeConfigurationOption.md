---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ReservedNodeConfigurationOption.html
---

# ReservedNodeConfigurationOption
<a name="API_ReservedNodeConfigurationOption"></a>

Details for a reserved-node exchange. Examples include the node type for a reserved node, the price for a node, the node's state, and other details.

## Contents
<a name="API_ReservedNodeConfigurationOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SourceReservedNode **
Describes a reserved node. You can call the [DescribeReservedNodeOfferings](API_DescribeReservedNodeOfferings.md) API to obtain the available reserved node offerings.
Type: [ReservedNode](API_ReservedNode.md) object
Required: No

 ** TargetReservedNodeCount **
The target reserved-node count.
Type: Integer
Required: No

 ** TargetReservedNodeOffering **
Describes a reserved node offering.
Type: [ReservedNodeOffering](API_ReservedNodeOffering.md) object
Required: No

## See Also
<a name="API_ReservedNodeConfigurationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ReservedNodeConfigurationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ReservedNodeConfigurationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ReservedNodeConfigurationOption)
