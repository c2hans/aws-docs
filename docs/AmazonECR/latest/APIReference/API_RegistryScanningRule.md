---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegistryScanningRule.html
---

# RegistryScanningRule
<a name="API_RegistryScanningRule"></a>

The details of a scanning rule for a private registry.

## Contents
<a name="API_RegistryScanningRule_Contents"></a>

 ** repositoryFilters **   <a name="ECR-Type-RegistryScanningRule-repositoryFilters"></a>
The repository filters associated with the scanning configuration for a private registry.
Type: Array of [ScanningRepositoryFilter](API_ScanningRepositoryFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** scanFrequency **   <a name="ECR-Type-RegistryScanningRule-scanFrequency"></a>
The frequency that scans are performed at for a private registry. When the `ENHANCED` scan type is specified, the supported scan frequencies are `CONTINUOUS_SCAN` and `SCAN_ON_PUSH`. When the `BASIC` scan type is specified, the `SCAN_ON_PUSH` scan frequency is supported. If scan on push is not specified, then the `MANUAL` scan frequency is set by default.
Type: String
Valid Values: `SCAN_ON_PUSH | CONTINUOUS_SCAN | MANUAL`
Required: Yes

## See Also
<a name="API_RegistryScanningRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RegistryScanningRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RegistryScanningRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RegistryScanningRule)
