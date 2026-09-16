---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunDependencySummary.html
---

# TestRunDependencySummary
<a name="API_TestRunDependencySummary"></a>

Contains summary information about a dependency that a test run blocked, as captured when the run started.

## Contents
<a name="API_TestRunDependencySummary_Contents"></a>

 ** criticality **   <a name="ngresiliencehub-Type-TestRunDependencySummary-criticality"></a>
The criticality classification of the dependency when the run started. A dependency that was not discovered has the UNKNOWN criticality.
Type: String
Valid Values: `HARD | SOFT | UNKNOWN`
Required: Yes

 ** dependencyName **   <a name="ngresiliencehub-Type-TestRunDependencySummary-dependencyName"></a>
The name of the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** dnsName **   <a name="ngresiliencehub-Type-TestRunDependencySummary-dnsName"></a>
The DNS name of the dependency that the test run blocked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Required: Yes

 ** source **   <a name="ngresiliencehub-Type-TestRunDependencySummary-source"></a>
The origin of the dependency. A discovered dependency was found by dependency discovery; a manual dependency was entered when the run started.
Type: String
Valid Values: `DISCOVERED | MANUAL`
Required: Yes

 ** dependencyId **   <a name="ngresiliencehub-Type-TestRunDependencySummary-dependencyId"></a>
The unique identifier of the dependency. Absent when the dependency was entered manually and was not part of dependency discovery.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** location **   <a name="ngresiliencehub-Type-TestRunDependencySummary-location"></a>
The location of the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** provider **   <a name="ngresiliencehub-Type-TestRunDependencySummary-provider"></a>
The provider of the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** sourceRegions **   <a name="ngresiliencehub-Type-TestRunDependencySummary-sourceRegions"></a>
The source Regions from which the dependency was detected.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

## See Also
<a name="API_TestRunDependencySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunDependencySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunDependencySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunDependencySummary)
