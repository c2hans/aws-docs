---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RouteAnalysisEndpointOptions.html
---

# RouteAnalysisEndpointOptions
<a name="API_RouteAnalysisEndpointOptions"></a>

Describes a source or a destination.

## Contents
<a name="API_RouteAnalysisEndpointOptions_Contents"></a>

 ** IpAddress **   <a name="networkmanager-Type-RouteAnalysisEndpointOptions-IpAddress"></a>
The IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** TransitGatewayArn **   <a name="networkmanager-Type-RouteAnalysisEndpointOptions-TransitGatewayArn"></a>
The ARN of the transit gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** TransitGatewayAttachmentArn **   <a name="networkmanager-Type-RouteAnalysisEndpointOptions-TransitGatewayAttachmentArn"></a>
The ARN of the transit gateway attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_RouteAnalysisEndpointOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteAnalysisEndpointOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteAnalysisEndpointOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteAnalysisEndpointOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
