---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ConsentPopupConfig.html
---

# ConsentPopupConfig
<a name="API_ConsentPopupConfig"></a>

Consent popup configuration displayed to users on login.

## Contents
<a name="API_ConsentPopupConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** enabled **   <a name="wickr-Type-ConsentPopupConfig-enabled"></a>
Whether the consent popup is enabled. When set to true, the popup is displayed to users on login.
Type: Boolean
Required: Yes

 ** closeButtonLabel **   <a name="wickr-Type-ConsentPopupConfig-closeButtonLabel"></a>
Label for the close button on the consent popup. Maximum 20 characters. Defaults to "Acknowledge" if not provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `[\S\s]*`
Required: No

 ** content **   <a name="wickr-Type-ConsentPopupConfig-content"></a>
Body content of the consent popup in Markdown format. Maximum 5000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Pattern: `[\S\s]*`
Required: No

 ** header **   <a name="wickr-Type-ConsentPopupConfig-header"></a>
Header text displayed at the top of the consent popup. Maximum 100 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ConsentPopupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/ConsentPopupConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/ConsentPopupConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ConsentPopupConfig)
