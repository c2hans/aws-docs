---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NetworkResourceSummary.html
---

# NetworkResourceSummary
<a name="API_NetworkResourceSummary"></a>

Describes a network resource.

## Contents
<a name="API_NetworkResourceSummary_Contents"></a>

 ** Definition **   <a name="networkmanager-Type-NetworkResourceSummary-Definition"></a>
Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** IsMiddlebox **   <a name="networkmanager-Type-NetworkResourceSummary-IsMiddlebox"></a>
Indicates whether this is a middlebox appliance.
Type: Boolean
Required: No

 ** NameTag **   <a name="networkmanager-Type-NetworkResourceSummary-NameTag"></a>
The value for the Name tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** RegisteredGatewayArn **   <a name="networkmanager-Type-NetworkResourceSummary-RegisteredGatewayArn"></a>
The ARN of the gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-NetworkResourceSummary-ResourceArn"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="networkmanager-Type-NetworkResourceSummary-ResourceType"></a>
The resource type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_NetworkResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
