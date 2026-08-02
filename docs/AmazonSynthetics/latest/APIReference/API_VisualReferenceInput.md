---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VisualReferenceInput.html
---

# VisualReferenceInput
<a name="API_VisualReferenceInput"></a>

An object that specifies what screenshots to use as a baseline for visual monitoring by this canary. It can optionally also specify parts of the screenshots to ignore during the visual monitoring comparison.

Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later. For more information, see [ Visual monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html) and [ Visual monitoring blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html)

## Contents
<a name="API_VisualReferenceInput_Contents"></a>

 ** BaseCanaryRunId **   <a name="synthetics-Type-VisualReferenceInput-BaseCanaryRunId"></a>
Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are `nextrun` to use the screenshots from the next run after this update is made, `lastrun` to use the screenshots from the most recent run before this update was made, or the value of `Id` in the [ CanaryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html) from a run of this a canary in the past 31 days. If you specify the `Id` of a canary run older than 31 days, the operation returns a 400 validation exception error..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** BaseScreenshots **   <a name="synthetics-Type-VisualReferenceInput-BaseScreenshots"></a>
An array of screenshots that will be used as the baseline for visual monitoring in future runs of this canary. If there is a screenshot that you don't want to be used for visual monitoring, remove it from this array.
Type: Array of [BaseScreenshot](API_BaseScreenshot.md) objects
Required: No

 ** BrowserType **   <a name="synthetics-Type-VisualReferenceInput-BrowserType"></a>
The browser type associated with this visual reference.
Type: String
Valid Values: `CHROME | FIREFOX`
Required: No

## See Also
<a name="API_VisualReferenceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/VisualReferenceInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/VisualReferenceInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/VisualReferenceInput)
