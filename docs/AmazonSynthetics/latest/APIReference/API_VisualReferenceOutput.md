---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VisualReferenceOutput.html
---

# VisualReferenceOutput
<a name="API_VisualReferenceOutput"></a>

If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run that is used as the baseline for screenshots, and the coordinates of any parts of those screenshots that are ignored during visual monitoring comparison.

Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later.

## Contents
<a name="API_VisualReferenceOutput_Contents"></a>

 ** BaseCanaryRunId **   <a name="synthetics-Type-VisualReferenceOutput-BaseCanaryRunId"></a>
The ID of the canary run that produced the baseline screenshots that are used for visual monitoring comparisons by this canary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** BaseScreenshots **   <a name="synthetics-Type-VisualReferenceOutput-BaseScreenshots"></a>
An array of screenshots that are used as the baseline for comparisons during visual monitoring.
Type: Array of [BaseScreenshot](API_BaseScreenshot.md) objects
Required: No

 ** BrowserType **   <a name="synthetics-Type-VisualReferenceOutput-BrowserType"></a>
The browser type associated with this visual reference.
Type: String
Valid Values: `CHROME | FIREFOX`
Required: No

## See Also
<a name="API_VisualReferenceOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/VisualReferenceOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/VisualReferenceOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/VisualReferenceOutput)
