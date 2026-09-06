---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RStudioServerProAppSettings.html
---

# RStudioServerProAppSettings
<a name="API_RStudioServerProAppSettings"></a>

A collection of settings that configure user interaction with the `RStudioServerPro` app.

## Contents
<a name="API_RStudioServerProAppSettings_Contents"></a>

 ** AccessStatus **   <a name="sagemaker-Type-RStudioServerProAppSettings-AccessStatus"></a>
Indicates whether the current user has access to the `RStudioServerPro` app.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UserGroup **   <a name="sagemaker-Type-RStudioServerProAppSettings-UserGroup"></a>
The level of permissions that the user has within the `RStudioServerPro` app. This value defaults to `User`. The `Admin` value allows the user access to the RStudio Administrative Dashboard.
Type: String
Valid Values: `R_STUDIO_ADMIN | R_STUDIO_USER`
Required: No

## See Also
<a name="API_RStudioServerProAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RStudioServerProAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RStudioServerProAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RStudioServerProAppSettings)
