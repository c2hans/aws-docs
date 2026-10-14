---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DependencyInsight.html
---

# DependencyInsight
<a name="API_DependencyInsight"></a>

Contains a single insight about a service's dependencies.

## Contents
<a name="API_DependencyInsight_Contents"></a>

 ** category **   <a name="ngresiliencehub-Type-DependencyInsight-category"></a>
The category of the insight. Valid values:
+ CROSS\_REGION - The insight relates to dependencies used across multiple Regions.
+ NEW\_DEPENDENCY - The insight relates to a recently detected dependency.
+ THIRD\_PARTY - The insight relates to a third-party dependency.
+ UNEVEN\_USAGE - The insight relates to a dependency with uneven usage across the service.
+ AWS\_SERVICE - The insight relates to a dependency on an Amazon Web Services service.
Type: String
Valid Values: `CROSS_REGION | NEW_DEPENDENCY | THIRD_PARTY | UNEVEN_USAGE | AWS_SERVICE`
Required: Yes

 ** description **   <a name="ngresiliencehub-Type-DependencyInsight-description"></a>
A human-readable explanation of the insight, describing the dependency behavior or condition that was detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_DependencyInsight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DependencyInsight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DependencyInsight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DependencyInsight)
