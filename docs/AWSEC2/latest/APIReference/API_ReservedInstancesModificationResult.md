---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedInstancesModificationResult.html
---

# ReservedInstancesModificationResult
<a name="API_ReservedInstancesModificationResult"></a>

Describes the modification request/s.

## Contents
<a name="API_ReservedInstancesModificationResult_Contents"></a>

 ** reservedInstancesId **
The ID for the Reserved Instances that were created as part of the modification request. This field is only available when the modification is fulfilled.
Type: String
Required: No

 ** targetConfiguration **
The target Reserved Instances configurations supplied as part of the modification request.
Type: [ReservedInstancesConfiguration](API_ReservedInstancesConfiguration.md) object
Required: No

## See Also
<a name="API_ReservedInstancesModificationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedInstancesModificationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedInstancesModificationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedInstancesModificationResult)
