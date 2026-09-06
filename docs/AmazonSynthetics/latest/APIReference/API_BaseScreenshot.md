---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_BaseScreenshot.html
---

# BaseScreenshot
<a name="API_BaseScreenshot"></a>

A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

## Contents
<a name="API_BaseScreenshot_Contents"></a>

 ** ScreenshotName **   <a name="synthetics-Type-BaseScreenshot-ScreenshotName"></a>
The name of the screenshot. This is generated the first time the canary is run after the `UpdateCanary` operation that specified for this canary to perform visual monitoring.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** IgnoreCoordinates **   <a name="synthetics-Type-BaseScreenshot-IgnoreCoordinates"></a>
Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see [ Editing or deleting a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html)
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `^(-?\d{1,5}\.?\d{0,2},){3}(-?\d{1,5}\.?\d{0,2}){1}$`
Required: No

## See Also
<a name="API_BaseScreenshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/BaseScreenshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/BaseScreenshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/BaseScreenshot)
