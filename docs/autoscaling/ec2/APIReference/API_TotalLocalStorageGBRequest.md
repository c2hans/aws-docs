---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TotalLocalStorageGBRequest.html
---

# TotalLocalStorageGBRequest
<a name="API_TotalLocalStorageGBRequest"></a>

Specifies the minimum and maximum for the `TotalLocalStorageGB` object when you specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) for an Auto Scaling group.

## Contents
<a name="API_TotalLocalStorageGBRequest_Contents"></a>

 ** Max **
The storage maximum in GB.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Min **
The storage minimum in GB.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TotalLocalStorageGBRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TotalLocalStorageGBRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TotalLocalStorageGBRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TotalLocalStorageGBRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
