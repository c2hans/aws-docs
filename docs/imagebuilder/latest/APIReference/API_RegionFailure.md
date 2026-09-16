---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_RegionFailure.html
---

# RegionFailure
<a name="API_RegionFailure"></a>

Contains details about a distribution or image configuration failure for a single Region.

## Contents
<a name="API_RegionFailure_Contents"></a>

 ** errorMessage **   <a name="imagebuilder-Type-RegionFailure-errorMessage"></a>
The error message for the failure in the Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 384000.
Required: No

 ** imageConfigurationStep **   <a name="imagebuilder-Type-RegionFailure-imageConfigurationStep"></a>
The image configuration step where the failure occurred. Image Builder sets this property when the failure happened during post-distribution configuration, such as launch template updates or virtual machine (VM) export. This property doesn't appear for failures that occurred while Image Builder copied the image to the Region.
Type: String
Valid Values: `ASSOCIATE_LICENSES | UPDATE_LAUNCH_TEMPLATES | PUT_SSM_PARAMETERS | UPDATE_FAST_LAUNCH_CONFIGURATIONS | EXPORT_AMI`
Required: No

 ** region **   <a name="imagebuilder-Type-RegionFailure-region"></a>
The Region where the failure occurred.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-RegionFailure-status"></a>
The failure status for the Region. Indicates whether the process failed, was canceled, or timed out.
Type: String
Valid Values: `FAILED | CANCELLED | TIMED_OUT`
Required: No

 ** targetAccountId **   <a name="imagebuilder-Type-RegionFailure-targetAccountId"></a>
The account ID of the account that the image was distributed to in the Region.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_RegionFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/RegionFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/RegionFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/RegionFailure)
