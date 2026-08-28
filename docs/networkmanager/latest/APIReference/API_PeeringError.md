---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PeeringError.html
---

# PeeringError
<a name="API_PeeringError"></a>

Describes an error associated with a peering request.

## Contents
<a name="API_PeeringError_Contents"></a>

 ** Code **   <a name="networkmanager-Type-PeeringError-Code"></a>
The error code for the peering request.
Type: String
Valid Values: `TRANSIT_GATEWAY_NOT_FOUND | TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED | MISSING_PERMISSIONS | INTERNAL_ERROR | EDGE_LOCATION_PEER_DUPLICATE | INVALID_TRANSIT_GATEWAY_STATE`
Required: No

 ** Message **   <a name="networkmanager-Type-PeeringError-Message"></a>
The message associated with the error `code`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

 ** MissingPermissionsContext **   <a name="networkmanager-Type-PeeringError-MissingPermissionsContext"></a>
Provides additional information about missing permissions for the peering error.
Type: [PermissionsErrorContext](API_PermissionsErrorContext.md) object
Required: No

 ** RequestId **   <a name="networkmanager-Type-PeeringError-RequestId"></a>
The ID of the Peering request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-PeeringError-ResourceArn"></a>
The ARN of the requested peering resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_PeeringError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PeeringError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PeeringError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PeeringError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
