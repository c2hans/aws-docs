---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzerConfiguration.html
---

# AnalyzerConfiguration
<a name="API_AnalyzerConfiguration"></a>

Contains information about the configuration of an analyzer for an AWS organization or account.

## Contents
<a name="API_AnalyzerConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** internalAccess **   <a name="accessanalyzer-Type-AnalyzerConfiguration-internalAccess"></a>
Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates access within your AWS environment.
Type: [InternalAccessConfiguration](API_InternalAccessConfiguration.md) object
Required: No

 ** unusedAccess **   <a name="accessanalyzer-Type-AnalyzerConfiguration-unusedAccess"></a>
Specifies the configuration of an unused access analyzer for an AWS organization or account.
Type: [UnusedAccessConfiguration](API_UnusedAccessConfiguration.md) object
Required: No

## See Also
<a name="API_AnalyzerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzerConfiguration)
