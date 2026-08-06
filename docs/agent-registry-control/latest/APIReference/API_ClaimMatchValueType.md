---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ClaimMatchValueType.html
---

# ClaimMatchValueType
<a name="API_ClaimMatchValueType"></a>

The expected value used to match a claim. Exactly one member is set.

## Contents
<a name="API_ClaimMatchValueType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** matchValueString **   <a name="agentregistrycontrol-Type-ClaimMatchValueType-matchValueString"></a>
A single string value to match the claim against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_.:/-]+`
Required: No

 ** matchValueStringList **   <a name="agentregistrycontrol-Type-ClaimMatchValueType-matchValueStringList"></a>
A list of string values to match the claim against.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_.:/-]+`
Required: No

## See Also
<a name="API_ClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vestry-control-plane-2025-12-01/ClaimMatchValueType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vestry-control-plane-2025-12-01/ClaimMatchValueType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vestry-control-plane-2025-12-01/ClaimMatchValueType)
