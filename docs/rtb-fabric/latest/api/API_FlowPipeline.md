---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_FlowPipeline.html
---

# FlowPipeline

How a flow's modules run. In `sequential`, each module sees the previous module's output. In `phased`, phases run in order, and the modules in a phase run at the same time on the same request, so a module can see a change that another module in its phase already made. Put a module that depends on another module in a later phase. Set exactly one. New members can be added, so handle an unknown one.

## Contents
<a name="API_FlowPipeline_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** phased **   <a name="rtbfabric-Type-FlowPipeline-phased"></a>
Phases run in order, and a phase's modules run at the same time on the same request. Use it when a phase's modules don't depend on each other.
Type: [PhasedPipeline](API_PhasedPipeline.md) object
Required: No

 ** sequential **   <a name="rtbfabric-Type-FlowPipeline-sequential"></a>
Modules run in list order. Use it when each module needs the previous module's output.
Type: [SequentialPipeline](API_SequentialPipeline.md) object
Required: No

## See Also
<a name="API_FlowPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/FlowPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/FlowPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/FlowPipeline)
