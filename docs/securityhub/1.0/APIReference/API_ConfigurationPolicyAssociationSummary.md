---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ConfigurationPolicyAssociationSummary.html
---

# ConfigurationPolicyAssociationSummary
<a name="API_ConfigurationPolicyAssociationSummary"></a>

 An object that contains the details of a configuration policy association that’s returned in a `ListConfigurationPolicyAssociations` request.

## Contents
<a name="API_ConfigurationPolicyAssociationSummary_Contents"></a>

 ** AssociationStatus **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-AssociationStatus"></a>
 The current status of the association between the specified target and the configuration.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED`
Required: No

 ** AssociationStatusMessage **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-AssociationStatusMessage"></a>
 The explanation for a `FAILED` value for `AssociationStatus`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AssociationType **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-AssociationType"></a>
 Indicates whether the association between the specified target and the configuration was directly applied by the AWS Security Hub CSPM delegated administrator or inherited from a parent.
Type: String
Valid Values: `INHERITED | APPLIED`
Required: No

 ** ConfigurationPolicyId **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-ConfigurationPolicyId"></a>
 The universally unique identifier (UUID) of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TargetId **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-TargetId"></a>
 The identifier of the target account, organizational unit, or the root.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TargetType **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-TargetType"></a>
 Specifies whether the target is an AWS account, organizational unit, or the root.
Type: String
Valid Values: `ACCOUNT | ORGANIZATIONAL_UNIT | ROOT`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-ConfigurationPolicyAssociationSummary-UpdatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigurationPolicyAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ConfigurationPolicyAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ConfigurationPolicyAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ConfigurationPolicyAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
