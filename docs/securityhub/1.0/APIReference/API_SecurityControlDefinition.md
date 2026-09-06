---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SecurityControlDefinition.html
---

# SecurityControlDefinition
<a name="API_SecurityControlDefinition"></a>

 Provides metadata for a security control, including its unique standard-agnostic identifier, title, description, severity, availability in AWS Regions, and a link to remediation steps.

## Contents
<a name="API_SecurityControlDefinition_Contents"></a>

 ** CurrentRegionAvailability **   <a name="securityhub-Type-SecurityControlDefinition-CurrentRegionAvailability"></a>
 Specifies whether a security control is available in the current AWS Region.
Type: String
Valid Values: `AVAILABLE | UNAVAILABLE`
Required: Yes

 ** Description **   <a name="securityhub-Type-SecurityControlDefinition-Description"></a>
 The description of a security control across standards. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter doesn't reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** RemediationUrl **   <a name="securityhub-Type-SecurityControlDefinition-RemediationUrl"></a>
 A link to Security Hub CSPM documentation that explains how to remediate a failed finding for a security control.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-SecurityControlDefinition-SecurityControlId"></a>
 The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number (for example, APIGateway.3). This parameter differs from `SecurityControlArn`, which is a unique Amazon Resource Name (ARN) assigned to a control. The ARN references the security control ID (for example, arn:aws:securityhub:eu-central-1:123456789012:security-control/APIGateway.3).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SeverityRating **   <a name="securityhub-Type-SecurityControlDefinition-SeverityRating"></a>
 The severity of a security control. For more information about how Security Hub CSPM determines control severity, see [Assigning severity to control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity) in the *Security Hub CSPM User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`
Required: Yes

 ** Title **   <a name="securityhub-Type-SecurityControlDefinition-Title"></a>
 The title of a security control.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** CustomizableProperties **   <a name="securityhub-Type-SecurityControlDefinition-CustomizableProperties"></a>
 Security control properties that you can customize. Currently, only parameter customization is supported for select controls. An empty array is returned for controls that don’t support custom properties.
Type: Array of strings
Valid Values: `Parameters`
Required: No

 ** ParameterDefinitions **   <a name="securityhub-Type-SecurityControlDefinition-ParameterDefinitions"></a>
 An object that provides a security control parameter name, description, and the options for customizing it. This object is excluded for a control that doesn't support custom parameters.
Type: String to [ParameterDefinition](API_ParameterDefinition.md) object map
Key Pattern: `.*\S.*`
Required: No

 ** Provider **   <a name="securityhub-Type-SecurityControlDefinition-Provider"></a>
The cloud provider whose resources the security control evaluates. For example, `AWS` or `Azure`.
Type: String
Valid Values: `AWS | Azure`
Required: No

## See Also
<a name="API_SecurityControlDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SecurityControlDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SecurityControlDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SecurityControlDefinition)
