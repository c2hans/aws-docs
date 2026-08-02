---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceTopologyEdgeSummary.html
---

# ServiceTopologyEdgeSummary
<a name="API_ServiceTopologyEdgeSummary"></a>

Contains summary information about a service topology edge.

## Contents
<a name="API_ServiceTopologyEdgeSummary_Contents"></a>

 ** destinationResourceIdentifier **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-destinationResourceIdentifier"></a>
The identifier of the destination resource.
Type: String
Required: Yes

 ** sourceResourceIdentifier **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-sourceResourceIdentifier"></a>
The identifier of the source resource.
Type: String
Required: Yes

 ** destinationAccount **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-destinationAccount"></a>
The AWS account ID of the destination resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** destinationRegion **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-destinationRegion"></a>
The AWS Region of the destination resource.
Type: String
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** properties **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-properties"></a>
The properties of the topology edge.
Type: Array of [EdgePropertySummary](API_EdgePropertySummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** sourceAccount **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-sourceAccount"></a>
The AWS account ID of the source resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** sourceRegion **   <a name="ngresiliencehub-Type-ServiceTopologyEdgeSummary-sourceRegion"></a>
The AWS Region of the source resource.
Type: String
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

## See Also
<a name="API_ServiceTopologyEdgeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceTopologyEdgeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceTopologyEdgeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceTopologyEdgeSummary)
