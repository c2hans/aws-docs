---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionFailureContext.html
---

# DistributionFailureContext
<a name="API_DistributionFailureContext"></a>

Contains details about a failure that occurred while Image Builder distributed the image or applied configuration to the distributed image.

## Contents
<a name="API_DistributionFailureContext_Contents"></a>

 ** errorMessage **   <a name="imagebuilder-Type-DistributionFailureContext-errorMessage"></a>
The error message for the distribution failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 384000.
Required: No

 ** regionFailures **   <a name="imagebuilder-Type-DistributionFailureContext-regionFailures"></a>
The details about the failure for each Region where the image didn't finish distribution or configuration.
Type: Array of [RegionFailure](API_RegionFailure.md) objects
Array Members: Minimum number of 1 item. Maximum number of 256 items.
Required: No

## See Also
<a name="API_DistributionFailureContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DistributionFailureContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DistributionFailureContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DistributionFailureContext)
