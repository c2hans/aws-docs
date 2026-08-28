---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_TransitGatewayRegistrationStateReason.html
---

# TransitGatewayRegistrationStateReason
<a name="API_TransitGatewayRegistrationStateReason"></a>

Describes the status of a transit gateway registration.

## Contents
<a name="API_TransitGatewayRegistrationStateReason_Contents"></a>

 ** Code **   <a name="networkmanager-Type-TransitGatewayRegistrationStateReason-Code"></a>
The code for the state reason.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | DELETED | FAILED`
Required: No

 ** Message **   <a name="networkmanager-Type-TransitGatewayRegistrationStateReason-Message"></a>
The message for the state reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_TransitGatewayRegistrationStateReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayRegistrationStateReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayRegistrationStateReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayRegistrationStateReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
