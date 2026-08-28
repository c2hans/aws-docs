---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsControl.html
---

# StandardsControl
<a name="API_StandardsControl"></a>

Details for an individual security standard control.

## Contents
<a name="API_StandardsControl_Contents"></a>

 ** ControlId **   <a name="securityhub-Type-StandardsControl-ControlId"></a>
The identifier of the security standard control.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ControlStatus **   <a name="securityhub-Type-StandardsControl-ControlStatus"></a>
The current status of the security standard control. Indicates whether the control is enabled or disabled. Security Hub CSPM does not check against disabled controls.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ControlStatusUpdatedAt **   <a name="securityhub-Type-StandardsControl-ControlStatusUpdatedAt"></a>
The date and time that the status of the security standard control was most recently updated.
Type: Timestamp
Required: No

 ** Description **   <a name="securityhub-Type-StandardsControl-Description"></a>
The longer description of the security standard control. Provides information about what the control is checking for.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DisabledReason **   <a name="securityhub-Type-StandardsControl-DisabledReason"></a>
The reason provided for the most recent change in status for the control.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RelatedRequirements **   <a name="securityhub-Type-StandardsControl-RelatedRequirements"></a>
The list of requirements that are related to this control.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** RemediationUrl **   <a name="securityhub-Type-StandardsControl-RemediationUrl"></a>
A link to remediation information for the control in the Security Hub CSPM user documentation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SeverityRating **   <a name="securityhub-Type-StandardsControl-SeverityRating"></a>
The severity of findings generated from this security standard control.
The finding severity is based on an assessment of how easy it would be to compromise AWS resources if the issue is detected.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** StandardsControlArn **   <a name="securityhub-Type-StandardsControl-StandardsControlArn"></a>
The ARN of the security standard control.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Title **   <a name="securityhub-Type-StandardsControl-Title"></a>
The title of the security standard control.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
