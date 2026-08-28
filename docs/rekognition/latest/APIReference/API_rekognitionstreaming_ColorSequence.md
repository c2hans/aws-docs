---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_ColorSequence.html
---

# ColorSequence
<a name="API_rekognitionstreaming_ColorSequence"></a>

A color sequence to be displayed on the user’s screen.

## Contents
<a name="API_rekognitionstreaming_ColorSequence_Contents"></a>

 ** DownscrollDuration **   <a name="rekognition-Type-rekognitionstreaming_ColorSequence-DownscrollDuration"></a>
Duration in milliseconds for which a given color in the color sequence will down-scroll before taking over full screen.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: Yes

 ** FlatDisplayDuration **   <a name="rekognition-Type-rekognitionstreaming_ColorSequence-FlatDisplayDuration"></a>
Duration in milliseconds for which a given flat color in the color sequence will be displayed on the full screen.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: Yes

 ** FreshnessColor **   <a name="rekognition-Type-rekognitionstreaming_ColorSequence-FreshnessColor"></a>
Represents the colors in a given ColorSequence to be flashed to the end user, with each color represented in RGB values.
Type: [FreshnessColor](API_rekognitionstreaming_FreshnessColor.md) object
Required: Yes

## See Also
<a name="API_rekognitionstreaming_ColorSequence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/ColorSequence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/ColorSequence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/ColorSequence)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
