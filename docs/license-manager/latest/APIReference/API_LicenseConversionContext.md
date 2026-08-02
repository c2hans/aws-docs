---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConversionContext.html
---

# LicenseConversionContext
<a name="API_LicenseConversionContext"></a>

Information about a license type conversion task.

## Contents
<a name="API_LicenseConversionContext_Contents"></a>

 ** ProductCodes **   <a name="licensemanager-Type-LicenseConversionContext-ProductCodes"></a>
Product codes referred to in the license conversion process.
Type: Array of [ProductCodeListItem](API_ProductCodeListItem.md) objects
Required: No

 ** UsageOperation **   <a name="licensemanager-Type-LicenseConversionContext-UsageOperation"></a>
The Usage operation value that corresponds to the license type you are converting your resource from. For more information about which platforms correspond to which usage operation values see [Sample data: usage operation by platform ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html#billing-info)
Type: String
Length Constraints: Maximum length of 50.
Required: No

## See Also
<a name="API_LicenseConversionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseConversionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseConversionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseConversionContext)
