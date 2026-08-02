---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Action.html
---

# Action
<a name="API_Action"></a>

Describes a bid action.

## Contents
<a name="API_Action_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** headerTag **   <a name="rtbfabric-Type-Action-headerTag"></a>
Describes the header tag for a bid action.
Type: [HeaderTagAction](API_HeaderTagAction.md) object
Required: No

 ** noBid **   <a name="rtbfabric-Type-Action-noBid"></a>
Describes a no bid action.
Type: [NoBidAction](API_NoBidAction.md) object
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/Action)
