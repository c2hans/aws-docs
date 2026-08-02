---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_InputSessionStateSpecification.html
---

# InputSessionStateSpecification
<a name="API_InputSessionStateSpecification"></a>

Specifications for the current state of the dialog between the user and the bot in the test set.

## Contents
<a name="API_InputSessionStateSpecification_Contents"></a>

 ** activeContexts **   <a name="lexv2-Type-InputSessionStateSpecification-activeContexts"></a>
Active contexts for the session state.
Type: Array of [ActiveContext](API_ActiveContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** runtimeHints **   <a name="lexv2-Type-InputSessionStateSpecification-runtimeHints"></a>
Runtime hints for the session state.
Type: [RuntimeHints](API_RuntimeHints.md) object
Required: No

 ** sessionAttributes **   <a name="lexv2-Type-InputSessionStateSpecification-sessionAttributes"></a>
Session attributes for the session state.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_InputSessionStateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/InputSessionStateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/InputSessionStateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/InputSessionStateSpecification)
