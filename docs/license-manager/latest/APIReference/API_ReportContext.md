---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ReportContext.html
---

# ReportContext
<a name="API_ReportContext"></a>

Details of the license configuration that this generator reports on.

## Contents
<a name="API_ReportContext_Contents"></a>

 ** licenseAssetGroupArns **   <a name="licensemanager-Type-ReportContext-licenseAssetGroupArns"></a>
Amazon Resource Names (ARNs) of the license asset groups to include in the report.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** licenseConfigurationArns **   <a name="licensemanager-Type-ReportContext-licenseConfigurationArns"></a>
Amazon Resource Name (ARN) of the license configuration that this generator reports on.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** reportEndDate **   <a name="licensemanager-Type-ReportContext-reportEndDate"></a>
End date for the report data collection period.
Type: Timestamp
Required: No

 ** reportStartDate **   <a name="licensemanager-Type-ReportContext-reportStartDate"></a>
Start date for the report data collection period.
Type: Timestamp
Required: No

## See Also
<a name="API_ReportContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ReportContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ReportContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ReportContext)
