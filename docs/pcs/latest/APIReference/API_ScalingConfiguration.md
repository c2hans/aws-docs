---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ScalingConfiguration.html
---

# ScalingConfiguration
<a name="API_ScalingConfiguration"></a>

Specifies the boundaries of the compute node group auto scaling.

## Contents
<a name="API_ScalingConfiguration_Contents"></a>

 ** maxInstanceCount **   <a name="PCS-Type-ScalingConfiguration-maxInstanceCount"></a>
The upper bound of the number of instances allowed in the compute fleet.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** minInstanceCount **   <a name="PCS-Type-ScalingConfiguration-minInstanceCount"></a>
The lower bound of the number of instances allowed in the compute fleet.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_ScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
