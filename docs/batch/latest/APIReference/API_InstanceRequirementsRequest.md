---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_InstanceRequirementsRequest.html
---

# InstanceRequirementsRequest
<a name="API_InstanceRequirementsRequest"></a>

The instance type requirements for the Amazon ECS Managed Instances capacity provider. Use this to specify which Amazon EC2 instance types or instance families Amazon ECS can launch.

## Contents
<a name="API_InstanceRequirementsRequest_Contents"></a>

 ** allowedInstanceTypes **   <a name="Batch-Type-InstanceRequirementsRequest-allowedInstanceTypes"></a>
A list of specific instance types or instance families that Amazon ECS can launch (for example, `m5.large` or `g5`). When specified, only these instance types are used.
Type: Array of strings
Required: No

## See Also
<a name="API_InstanceRequirementsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/InstanceRequirementsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/InstanceRequirementsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/InstanceRequirementsRequest)
