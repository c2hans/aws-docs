---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_BaselineEbsBandwidthMbpsRequest.html
---

# BaselineEbsBandwidthMbpsRequest
<a name="API_BaselineEbsBandwidthMbpsRequest"></a>

The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps) for instance type selection. This is important for workloads with high storage I/O requirements.

## Contents
<a name="API_BaselineEbsBandwidthMbpsRequest_Contents"></a>

 ** max **   <a name="ECS-Type-BaselineEbsBandwidthMbpsRequest-max"></a>
The maximum baseline Amazon EBS bandwidth in Mbps. Instance types with higher Amazon EBS bandwidth are excluded from selection.
Type: Integer
Required: No

 ** min **   <a name="ECS-Type-BaselineEbsBandwidthMbpsRequest-min"></a>
The minimum baseline Amazon EBS bandwidth in Mbps. Instance types with lower Amazon EBS bandwidth are excluded from selection.
Type: Integer
Required: No

## See Also
<a name="API_BaselineEbsBandwidthMbpsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/BaselineEbsBandwidthMbpsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/BaselineEbsBandwidthMbpsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/BaselineEbsBandwidthMbpsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
