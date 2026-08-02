---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DependencySummary.html
---

# DependencySummary
<a name="API_DependencySummary"></a>

Contains summary information about a discovered dependency.

## Contents
<a name="API_DependencySummary_Contents"></a>

 ** criticality **   <a name="ngresiliencehub-Type-DependencySummary-criticality"></a>
The criticality level of the dependency.
Type: String
Valid Values: `HARD | SOFT | UNKNOWN`
Required: Yes

 ** dependencyId **   <a name="ngresiliencehub-Type-DependencySummary-dependencyId"></a>
The unique identifier of the dependency.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** dependencyName **   <a name="ngresiliencehub-Type-DependencySummary-dependencyName"></a>
The name of the dependency.
Type: String
Required: Yes

 ** dnsName **   <a name="ngresiliencehub-Type-DependencySummary-dnsName"></a>
The DNS name associated with the dependency.
Type: String
Required: Yes

 ** lastDetectedTime **   <a name="ngresiliencehub-Type-DependencySummary-lastDetectedTime"></a>
The timestamp when the dependency was last detected.
Type: Timestamp
Required: Yes

 ** location **   <a name="ngresiliencehub-Type-DependencySummary-location"></a>
The location of the dependency.
Type: String
Required: Yes

 ** queryRange **   <a name="ngresiliencehub-Type-DependencySummary-queryRange"></a>
The query range data for the dependency.
Type: [QueryRange](API_QueryRange.md) object
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-DependencySummary-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** sourceRegions **   <a name="ngresiliencehub-Type-DependencySummary-sourceRegions"></a>
The source Regions from which the dependency was detected.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: Yes

 ** comment **   <a name="ngresiliencehub-Type-DependencySummary-comment"></a>
A user-provided comment about the dependency.
Type: String
Required: No

 ** provider **   <a name="ngresiliencehub-Type-DependencySummary-provider"></a>
The provider of the dependency.
Type: String
Required: No

## See Also
<a name="API_DependencySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DependencySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DependencySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DependencySummary)
