---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_DetailedInstanceTypeItem.html
---

# DetailedInstanceTypeItem
<a name="API_DetailedInstanceTypeItem"></a>

Information about an instance type that can be ordered for an Outpost, including hardware specifications and supported form factors.

## Contents
<a name="API_DetailedInstanceTypeItem_Contents"></a>

 ** FormFactorConfigs **   <a name="outposts-Type-DetailedInstanceTypeItem-FormFactorConfigs"></a>
The supported form factor and Outpost generation configurations for the instance type.
Type: Array of [FormFactorConfig](API_FormFactorConfig.md) objects
Required: No

 ** InstanceType **   <a name="outposts-Type-DetailedInstanceTypeItem-InstanceType"></a>
The instance type.
Type: String
Required: No

 ** MemoryInMib **   <a name="outposts-Type-DetailedInstanceTypeItem-MemoryInMib"></a>
The memory size of the instance type, in MiB.
Type: Integer
Required: No

 ** NetworkPerformance **   <a name="outposts-Type-DetailedInstanceTypeItem-NetworkPerformance"></a>
The network performance of the instance type.
Type: String
Required: No

 ** VCPUs **   <a name="outposts-Type-DetailedInstanceTypeItem-VCPUs"></a>
The number of default VCPUs in the instance type.
Type: Integer
Required: No

## See Also
<a name="API_DetailedInstanceTypeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/DetailedInstanceTypeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/DetailedInstanceTypeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/DetailedInstanceTypeItem)
