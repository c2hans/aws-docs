---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_TargetNetworkUpdate.html
---

# TargetNetworkUpdate
<a name="API_TargetNetworkUpdate"></a>

Updated configuration for the target network topology and addressing.

## Contents
<a name="API_TargetNetworkUpdate_Contents"></a>

 ** inboundCidr **   <a name="mgn-Type-TargetNetworkUpdate-inboundCidr"></a>
The updated CIDR block for inbound traffic.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

 ** inspectionCidr **   <a name="mgn-Type-TargetNetworkUpdate-inspectionCidr"></a>
The updated CIDR block for inspection traffic.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

 ** outboundCidr **   <a name="mgn-Type-TargetNetworkUpdate-outboundCidr"></a>
The updated CIDR block for outbound traffic.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

 ** topology **   <a name="mgn-Type-TargetNetworkUpdate-topology"></a>
The updated network topology type.
Type: String
Valid Values: `ISOLATED_VPC | HUB_AND_SPOKE`
Required: No

## See Also
<a name="API_TargetNetworkUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/TargetNetworkUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/TargetNetworkUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/TargetNetworkUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
