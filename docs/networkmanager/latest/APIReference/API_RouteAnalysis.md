---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RouteAnalysis.html
---

# RouteAnalysis
<a name="API_RouteAnalysis"></a>

Describes a route analysis.

## Contents
<a name="API_RouteAnalysis_Contents"></a>

 ** Destination **   <a name="networkmanager-Type-RouteAnalysis-Destination"></a>
The destination.
Type: [RouteAnalysisEndpointOptions](API_RouteAnalysisEndpointOptions.md) object
Required: No

 ** ForwardPath **   <a name="networkmanager-Type-RouteAnalysis-ForwardPath"></a>
The forward path.
Type: [RouteAnalysisPath](API_RouteAnalysisPath.md) object
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-RouteAnalysis-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** IncludeReturnPath **   <a name="networkmanager-Type-RouteAnalysis-IncludeReturnPath"></a>
Indicates whether to analyze the return path. The return path is not analyzed if the forward path analysis does not succeed.
Type: Boolean
Required: No

 ** OwnerAccountId **   <a name="networkmanager-Type-RouteAnalysis-OwnerAccountId"></a>
The ID of the AWS account that created the route analysis.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** ReturnPath **   <a name="networkmanager-Type-RouteAnalysis-ReturnPath"></a>
The return path.
Type: [RouteAnalysisPath](API_RouteAnalysisPath.md) object
Required: No

 ** RouteAnalysisId **   <a name="networkmanager-Type-RouteAnalysis-RouteAnalysisId"></a>
The ID of the route analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Source **   <a name="networkmanager-Type-RouteAnalysis-Source"></a>
The source.
Type: [RouteAnalysisEndpointOptions](API_RouteAnalysisEndpointOptions.md) object
Required: No

 ** StartTimestamp **   <a name="networkmanager-Type-RouteAnalysis-StartTimestamp"></a>
The time that the analysis started.
Type: Timestamp
Required: No

 ** Status **   <a name="networkmanager-Type-RouteAnalysis-Status"></a>
The status of the route analysis.
Type: String
Valid Values: `RUNNING | COMPLETED | FAILED`
Required: No

 ** UseMiddleboxes **   <a name="networkmanager-Type-RouteAnalysis-UseMiddleboxes"></a>
Indicates whether to include the location of middlebox appliances in the route analysis.
Type: Boolean
Required: No

## See Also
<a name="API_RouteAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
