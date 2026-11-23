---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_SequentialPipeline.html
---

# SequentialPipeline

Modules that run one after another, each on the previous module's output.

## Contents
<a name="API_SequentialPipeline_Contents"></a>

 ** modules **   <a name="rtbfabric-Type-SequentialPipeline-modules"></a>
In execution order. The modules count against your Modules per flow quota. A request over the quota fails with ServiceQuotaExceededException.
Type: Array of [FlowModule](API_FlowModule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: Yes

## See Also
<a name="API_SequentialPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/SequentialPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/SequentialPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/SequentialPipeline)
