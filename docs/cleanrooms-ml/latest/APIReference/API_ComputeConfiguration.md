---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ComputeConfiguration.html
---

# ComputeConfiguration
<a name="API_ComputeConfiguration"></a>

Provides configuration information for the instances that will perform the compute work.

## Contents
<a name="API_ComputeConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** worker **   <a name="API-Type-ComputeConfiguration-worker"></a>
The worker instances that will perform the compute work.
Type: [WorkerComputeConfiguration](API_WorkerComputeConfiguration.md) object
Required: No

## See Also
<a name="API_ComputeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ComputeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ComputeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ComputeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
