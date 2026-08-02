---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_SafetyLever.html
---

# SafetyLever
<a name="API_SafetyLever"></a>

 Describes a safety lever.

## Contents
<a name="API_SafetyLever_Contents"></a>

 ** arn **   <a name="fis-Type-SafetyLever-arn"></a>
 The Amazon Resource Name (ARN) of the safety lever.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** id **   <a name="fis-Type-SafetyLever-id"></a>
 The ID of the safety lever.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** state **   <a name="fis-Type-SafetyLever-state"></a>
 The state of the safety lever.
Type: [SafetyLeverState](API_SafetyLeverState.md) object
Required: No

## See Also
<a name="API_SafetyLever_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/SafetyLever)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/SafetyLever)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/SafetyLever)
