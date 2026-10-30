---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_MatchModels.html
---

# MatchModels
<a name="API_MatchModels"></a>

A condition that matches inference requests based on the requested model.

## Contents
<a name="API_MatchModels_Contents"></a>

 ** anyOf **   <a name="bedrockagentcorecontrol-Type-MatchModels-anyOf"></a>
A list of model entries. The condition is met if the requested model matches any of the entries.
Type: Array of [MatchModelEntry](API_MatchModelEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_MatchModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MatchModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MatchModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MatchModels)
