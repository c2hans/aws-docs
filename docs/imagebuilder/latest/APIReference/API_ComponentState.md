---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentState.html
---

# ComponentState
<a name="API_ComponentState"></a>

A group of fields that describe the current status of components.

## Contents
<a name="API_ComponentState_Contents"></a>

 ** reason **   <a name="imagebuilder-Type-ComponentState-reason"></a>
Describes how or why the component changed state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-ComponentState-status"></a>
The current state of the component. Components with a status of `DEPRECATED` or `DISABLED` can't be added to new recipes.
Type: String
Valid Values: `DEPRECATED | DISABLED | ACTIVE`
Required: No

## See Also
<a name="API_ComponentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentState)
