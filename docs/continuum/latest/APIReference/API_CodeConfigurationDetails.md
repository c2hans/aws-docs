---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CodeConfigurationDetails.html
---

# CodeConfigurationDetails
<a name="API_CodeConfigurationDetails"></a>

The code Configuration Details.

## Contents
<a name="API_CodeConfigurationDetails_Contents"></a>

 ** collectorDetails **   <a name="continuum-Type-CodeConfigurationDetails-collectorDetails"></a>
Collector data access configuration returned for an environment.
Type: [CollectorDetails](API_CollectorDetails.md) object
Required: No

 ** environmentConfiguration **   <a name="continuum-Type-CodeConfigurationDetails-environmentConfiguration"></a>
Environment-level operating policy.
Type: [EnvironmentConfiguration](API_EnvironmentConfiguration.md) object
Required: No

 ** latestScan **   <a name="continuum-Type-CodeConfigurationDetails-latestScan"></a>
The latest Scan.
Type: [CodeScanSummary](API_CodeScanSummary.md) object
Required: No

 ** sourceConfiguration **   <a name="continuum-Type-CodeConfigurationDetails-sourceConfiguration"></a>
GA source configuration for code and customer-authored context.
Type: [EnvironmentSourceConfiguration](API_EnvironmentSourceConfiguration.md) object
Required: No

## See Also
<a name="API_CodeConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CodeConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CodeConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CodeConfigurationDetails)
