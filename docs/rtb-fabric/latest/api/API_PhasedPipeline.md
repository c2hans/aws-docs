---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_PhasedPipeline.html
---

# PhasedPipeline

Phases that run in order; each starts after the previous one completes.

## Contents
<a name="API_PhasedPipeline_Contents"></a>

 ** phases **   <a name="rtbfabric-Type-PhasedPipeline-phases"></a>
The modules across the phases count against your Modules per flow quota. A request over the quota fails with ServiceQuotaExceededException.
Type: Array of [FlowPhase](API_FlowPhase.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: Yes

## See Also
<a name="API_PhasedPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/PhasedPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/PhasedPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/PhasedPipeline)
