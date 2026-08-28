---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AcceleratorCountRequest.html
---

# AcceleratorCountRequest
<a name="API_AcceleratorCountRequest"></a>

The minimum and maximum number of accelerators (such as GPUs) for instance type selection. This is used for workloads that require specific numbers of accelerators.

## Contents
<a name="API_AcceleratorCountRequest_Contents"></a>

 ** max **   <a name="ECS-Type-AcceleratorCountRequest-max"></a>
The maximum number of accelerators. Instance types with more accelerators are excluded from selection.
Type: Integer
Required: No

 ** min **   <a name="ECS-Type-AcceleratorCountRequest-min"></a>
The minimum number of accelerators. Instance types with fewer accelerators are excluded from selection.
Type: Integer
Required: No

## See Also
<a name="API_AcceleratorCountRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AcceleratorCountRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AcceleratorCountRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AcceleratorCountRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
