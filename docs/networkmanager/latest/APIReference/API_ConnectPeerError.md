---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ConnectPeerError.html
---

# ConnectPeerError
<a name="API_ConnectPeerError"></a>

Describes an error associated with a Connect peer request

## Contents
<a name="API_ConnectPeerError_Contents"></a>

 ** Code **   <a name="networkmanager-Type-ConnectPeerError-Code"></a>
The error code for the Connect peer request.
Type: String
Valid Values: `EDGE_LOCATION_NO_FREE_IPS | EDGE_LOCATION_PEER_DUPLICATE | SUBNET_NOT_FOUND | IP_OUTSIDE_SUBNET_CIDR_RANGE | INVALID_INSIDE_CIDR_BLOCK | NO_ASSOCIATED_CIDR_BLOCK`
Required: No

 ** Message **   <a name="networkmanager-Type-ConnectPeerError-Message"></a>
The message associated with the error `code`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

 ** RequestId **   <a name="networkmanager-Type-ConnectPeerError-RequestId"></a>
The ID of the Connect peer request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-ConnectPeerError-ResourceArn"></a>
The ARN of the requested Connect peer resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ConnectPeerError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
