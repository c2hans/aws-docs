---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PerformanceFactorReference.html
---

# PerformanceFactorReference
<a name="API_PerformanceFactorReference"></a>

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

**Note**
Currently, only one instance family can be specified in the list.

## Contents
<a name="API_PerformanceFactorReference_Contents"></a>

 ** InstanceFamily ** (request), ** instanceFamily ** (response)
The instance family to use as a baseline reference.
Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.`) in the instance type name. For example, in the instance type `c6i.large`, the instance family is `c6i`, not `c6`. For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types*.
The following instance families are *not supported* for performance protection:
+  `c1`
+  `g3` \| `g3s`
+  `hpc7g`
+  `m1` \| `m2`
+  `mac1` \| `mac2` \| `mac2-m1ultra` \| `mac2-m2` \| `mac2-m2pro`
+  `p3dn` \| `p4d` \| `p5`
+  `t1`
+  `u-12tb1` \| `u-18tb1` \| `u-24tb1` \| `u-3tb1` \| `u-6tb1` \| `u-9tb1` \| `u7i-12tb` \| `u7in-16tb` \| `u7in-24tb` \| `u7in-32tb`
If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.
If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet), [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet), [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet), and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest).
Type: String
Required: No

## See Also
<a name="API_PerformanceFactorReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PerformanceFactorReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PerformanceFactorReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PerformanceFactorReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
