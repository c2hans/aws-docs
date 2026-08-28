---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_ColorDisplayed.html
---

# ColorDisplayed
<a name="API_rekognitionstreaming_ColorDisplayed"></a>

Contains information regarding `SequenceNumber`, `CurrentColor`, `PreviousColor`, and `CurrentColorStartTimestamp`.

## Contents
<a name="API_rekognitionstreaming_ColorDisplayed_Contents"></a>

 ** CurrentColor **   <a name="rekognition-Type-rekognitionstreaming_ColorDisplayed-CurrentColor"></a>
 The current color being displayed on the screen (flat or downscrolled). It will contain a separate RGB list having 3 elements (each element can have values between 0 to 255).
Type: [FreshnessColor](API_rekognitionstreaming_FreshnessColor.md) object
Required: Yes

 ** CurrentColorStartTimestamp **   <a name="rekognition-Type-rekognitionstreaming_ColorDisplayed-CurrentColorStartTimestamp"></a>
Epoch timestamp of when the current color was displayed on the user screen.
Type: Long
Valid Range: Minimum value of 1640995200000. Maximum value of 2272147200000.
Required: Yes

 ** SequenceNumber **   <a name="rekognition-Type-rekognitionstreaming_ColorDisplayed-SequenceNumber"></a>
The order in which the current color was displayed on the screen.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 50.
Required: Yes

 ** PreviousColor **   <a name="rekognition-Type-rekognitionstreaming_ColorDisplayed-PreviousColor"></a>
The previous color displayed on screen (flat or downscrolled). It will contain a separate RGB list having 3 elements (each element can have values between 0 to 255).
Type: [FreshnessColor](API_rekognitionstreaming_FreshnessColor.md) object
Required: No

## See Also
<a name="API_rekognitionstreaming_ColorDisplayed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/ColorDisplayed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/ColorDisplayed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/ColorDisplayed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
