---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentActionState.html
---

# ExperimentActionState
<a name="API_ExperimentActionState"></a>

Describes the state of an action.

## Contents
<a name="API_ExperimentActionState_Contents"></a>

 ** reason **   <a name="fis-Type-ExperimentActionState-reason"></a>
The reason for the state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** status **   <a name="fis-Type-ExperimentActionState-status"></a>
The state of the action.
Type: String
Valid Values: `pending | initiating | running | completed | cancelled | stopping | stopped | failed | skipped`
Required: No

## See Also
<a name="API_ExperimentActionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentActionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentActionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentActionState)
