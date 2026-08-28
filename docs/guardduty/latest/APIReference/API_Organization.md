---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Organization.html
---

# Organization
<a name="API_Organization"></a>

Contains information about the ISP organization of the remote IP address.

## Contents
<a name="API_Organization_Contents"></a>

 ** asn **   <a name="guardduty-Type-Organization-asn"></a>
The Autonomous System Number (ASN) of the internet provider of the remote IP address.
Type: String
Required: No

 ** asnOrg **   <a name="guardduty-Type-Organization-asnOrg"></a>
The organization that registered this ASN.
Type: String
Required: No

 ** isp **   <a name="guardduty-Type-Organization-isp"></a>
The ISP information for the internet provider.
Type: String
Required: No

 ** org **   <a name="guardduty-Type-Organization-org"></a>
The name of the internet provider.
Type: String
Required: No

## See Also
<a name="API_Organization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Organization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Organization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Organization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
