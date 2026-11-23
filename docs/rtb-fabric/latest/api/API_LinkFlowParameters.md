---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkFlowParameters.html
---

# LinkFlowParameters

A requested link flow.

## Contents
<a name="API_LinkFlowParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** flows **   <a name="rtbfabric-Type-LinkFlowParameters-flows"></a>
A link's flows: at most one.
Type: Array of [Flow](API_Flow.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** modules **   <a name="rtbfabric-Type-LinkFlowParameters-modules"></a>
The requested modules.
Type: Array of [ModuleConfiguration](API_ModuleConfiguration.md) objects
Required: No

## See Also
<a name="API_LinkFlowParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/LinkFlowParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/LinkFlowParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/LinkFlowParameters)
