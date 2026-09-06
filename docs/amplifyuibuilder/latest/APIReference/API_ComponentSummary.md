---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentSummary.html
---

# ComponentSummary
<a name="API_ComponentSummary"></a>

Contains a summary of a component. This is a read-only data type that is returned by `ListComponents`.

## Contents
<a name="API_ComponentSummary_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-ComponentSummary-appId"></a>
The unique ID of the Amplify app associated with the component.
Type: String
Required: Yes

 ** componentType **   <a name="amplifyuibuilder-Type-ComponentSummary-componentType"></a>
The component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-ComponentSummary-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-ComponentSummary-id"></a>
The unique ID of the component.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-ComponentSummary-name"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentSummary)
