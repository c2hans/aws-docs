---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomContentConfiguration.html
---

# CustomContentConfiguration
<a name="API_CustomContentConfiguration"></a>

The configuration of a `CustomContentVisual`.

## Contents
<a name="API_CustomContentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContentType **   <a name="QS-Type-CustomContentConfiguration-ContentType"></a>
The content type of the custom content visual. You can use this to have the visual render as an image.
Type: String
Valid Values: `IMAGE | OTHER_EMBEDDED_CONTENT`
Required: No

 ** ContentUrl **   <a name="QS-Type-CustomContentConfiguration-ContentUrl"></a>
The input URL that links to the custom content that you want in the custom visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ImageScaling **   <a name="QS-Type-CustomContentConfiguration-ImageScaling"></a>
The sizing options for the size of the custom content visual. This structure is required when the `ContentType` of the visual is `'IMAGE'`.
Type: String
Valid Values: `FIT_TO_HEIGHT | FIT_TO_WIDTH | DO_NOT_SCALE | SCALE_TO_VISUAL`
Required: No

 ** Interactions **   <a name="QS-Type-CustomContentConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

## See Also
<a name="API_CustomContentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomContentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomContentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomContentConfiguration)
