---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_TemplateVersionSourceInput.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# TemplateVersionSourceInput
<a name="API_TemplateVersionSourceInput"></a>

Template version source data.

## Contents
<a name="API_TemplateVersionSourceInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="proton-Type-TemplateVersionSourceInput-s3"></a>
An S3 source object that includes the template bundle S3 path and name for a template minor version.
Type: [S3ObjectSource](API_S3ObjectSource.md) object
Required: No

## See Also
<a name="API_TemplateVersionSourceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/TemplateVersionSourceInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/TemplateVersionSourceInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/TemplateVersionSourceInput)
