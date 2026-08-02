---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ActionSummary.html
---

# ActionSummary
<a name="API_ActionSummary"></a>

Provides a summary of an action.

## Contents
<a name="API_ActionSummary_Contents"></a>

 ** arn **   <a name="fis-Type-ActionSummary-arn"></a>
The Amazon Resource Name (ARN) of the action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** description **   <a name="fis-Type-ActionSummary-description"></a>
The description for the action.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** id **   <a name="fis-Type-ActionSummary-id"></a>
The ID of the action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** tags **   <a name="fis-Type-ActionSummary-tags"></a>
The tags for the action.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** targets **   <a name="fis-Type-ActionSummary-targets"></a>
The targets for the action.
Type: String to [ActionTarget](API_ActionTarget.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ActionSummary)
