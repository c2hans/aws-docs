---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Flow.html
---

# Flow

One flow on a link: a set of modules that runs on the link's bid requests.

## Contents
<a name="API_Flow_Contents"></a>

 ** name **   <a name="rtbfabric-Type-Flow-name"></a>
The flow's name, unique within the link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]*`
Required: Yes

 ** pipeline **   <a name="rtbfabric-Type-Flow-pipeline"></a>
The pipeline that the flow's modules run in. In a sequential pipeline, each module sees the previous module's output. In a phased pipeline, a phase's modules see the prior phase's output, not each other's.
Type: [FlowPipeline](API_FlowPipeline.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_Flow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/Flow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/Flow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/Flow)
