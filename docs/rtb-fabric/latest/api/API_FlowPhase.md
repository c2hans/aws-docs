---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_FlowPhase.html
---

# FlowPhase

One phase of a phased pipeline. Its modules run at the same time on the same request. A response from any module, such as a no-bid, ends the flow, and modules that are still running are canceled.

## Contents
<a name="API_FlowPhase_Contents"></a>

 ** modules **   <a name="rtbfabric-Type-FlowPhase-modules"></a>
The modules to run at the same time in this phase.
Type: Array of [FlowModule](API_FlowModule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: Yes

## See Also
<a name="API_FlowPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/FlowPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/FlowPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/FlowPhase)
