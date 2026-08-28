---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkEndpoint.html
---

# NetworkEndpoint
<a name="API_NetworkEndpoint"></a>

 Contains information about network endpoints involved in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

This field can provide information about the network endpoints associated with the resource in the attack sequence finding, or about a specific network endpoint used for the attack.

## Contents
<a name="API_NetworkEndpoint_Contents"></a>

 ** AutonomousSystem **   <a name="securityhub-Type-NetworkEndpoint-AutonomousSystem"></a>
 The Autonomous System Number (ASN) of the network endpoint.
Type: [NetworkAutonomousSystem](API_NetworkAutonomousSystem.md) object
Required: No

 ** Connection **   <a name="securityhub-Type-NetworkEndpoint-Connection"></a>
 Information about the network connection.
Type: [NetworkConnection](API_NetworkConnection.md) object
Required: No

 ** Domain **   <a name="securityhub-Type-NetworkEndpoint-Domain"></a>
 The domain information for the network endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-NetworkEndpoint-Id"></a>
 The identifier of the network endpoint involved in the attack sequence.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ip **   <a name="securityhub-Type-NetworkEndpoint-Ip"></a>
 The IP address used in the network endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Location **   <a name="securityhub-Type-NetworkEndpoint-Location"></a>
 Information about the location of the network endpoint.
Type: [NetworkGeoLocation](API_NetworkGeoLocation.md) object
Required: No

 ** Port **   <a name="securityhub-Type-NetworkEndpoint-Port"></a>
 The port number associated with the network endpoint.
Type: Integer
Required: No

## See Also
<a name="API_NetworkEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
