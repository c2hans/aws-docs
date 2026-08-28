---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_PortProbeAction.html
---

# PortProbeAction
<a name="API_PortProbeAction"></a>

Contains information about the PORT\_PROBE action described in the finding.

## Contents
<a name="API_PortProbeAction_Contents"></a>

 ** blocked **   <a name="guardduty-Type-PortProbeAction-blocked"></a>
Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.
Type: Boolean
Required: No

 ** portProbeDetails **   <a name="guardduty-Type-PortProbeAction-portProbeDetails"></a>
A list of objects related to port probe details.
Type: Array of [PortProbeDetail](API_PortProbeDetail.md) objects
Required: No

## See Also
<a name="API_PortProbeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/PortProbeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/PortProbeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/PortProbeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
