---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SecurityControl.html
---

# SecurityControl
<a name="API_SecurityControl"></a>

 A security control in Security Hub CSPM describes a security best practice related to a specific resource.

## Contents
<a name="API_SecurityControl_Contents"></a>

 ** Description **   <a name="securityhub-Type-SecurityControl-Description"></a>
 The description of a security control across standards. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter doesn't reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** RemediationUrl **   <a name="securityhub-Type-SecurityControl-RemediationUrl"></a>
 A link to Security Hub CSPM documentation that explains how to remediate a failed finding for a security control.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlArn **   <a name="securityhub-Type-SecurityControl-SecurityControlArn"></a>
 The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-SecurityControl-SecurityControlId"></a>
 The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlStatus **   <a name="securityhub-Type-SecurityControl-SecurityControlStatus"></a>
 The enablement status of a security control in a specific standard.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** SeverityRating **   <a name="securityhub-Type-SecurityControl-SeverityRating"></a>
 The severity of a security control. For more information about how Security Hub CSPM determines control severity, see [Assigning severity to control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity) in the *Security Hub CSPM User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`
Required: Yes

 ** Title **   <a name="securityhub-Type-SecurityControl-Title"></a>
The title of a security control.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** LastUpdateReason **   <a name="securityhub-Type-SecurityControl-LastUpdateReason"></a>
 The most recent reason for updating the customizable properties of a security control. This differs from the `UpdateReason` field of the [`BatchUpdateStandardsControlAssociations`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.
Type: String
Pattern: `^([^\u0000-\u007F]|[-_ a-zA-Z0-9])+$`
Required: No

 ** Parameters **   <a name="securityhub-Type-SecurityControl-Parameters"></a>
 An object that identifies the name of a control parameter, its current value, and whether it has been customized.
Type: String to [ParameterConfiguration](API_ParameterConfiguration.md) object map
Key Pattern: `.*\S.*`
Required: No

 ** Provider **   <a name="securityhub-Type-SecurityControl-Provider"></a>
The cloud provider whose resources the security control evaluates. For example, `AWS` or `Azure`.
Type: String
Valid Values: `AWS | Azure`
Required: No

 ** UpdateStatus **   <a name="securityhub-Type-SecurityControl-UpdateStatus"></a>
 Identifies whether customizable properties of a security control are reflected in Security Hub CSPM findings. A status of `READY` indicates that Security Hub CSPM uses the current control parameter values when running security checks of the control. A status of `UPDATING` indicates that all security checks might not use the current parameter values.
Type: String
Valid Values: `READY | UPDATING`
Required: No

## See Also
<a name="API_SecurityControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SecurityControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SecurityControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SecurityControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
