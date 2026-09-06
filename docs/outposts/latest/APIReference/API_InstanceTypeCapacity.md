---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_InstanceTypeCapacity.html
---

# InstanceTypeCapacity
<a name="API_InstanceTypeCapacity"></a>

The instance type that you specify determines the combination of CPU, memory, storage, and networking capacity.

## Contents
<a name="API_InstanceTypeCapacity_Contents"></a>

 ** Count **   <a name="outposts-Type-InstanceTypeCapacity-Count"></a>
The number of instances for the specified instance type.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: Yes

 ** InstanceType **   <a name="outposts-Type-InstanceTypeCapacity-InstanceType"></a>
The instance type of the hosts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9\-]+\.[a-z0-9\-]+$`
Required: Yes

## See Also
<a name="API_InstanceTypeCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/InstanceTypeCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/InstanceTypeCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/InstanceTypeCapacity)
