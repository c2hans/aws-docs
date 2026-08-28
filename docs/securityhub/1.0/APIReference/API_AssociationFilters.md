---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AssociationFilters.html
---

# AssociationFilters
<a name="API_AssociationFilters"></a>

 Options for filtering the `ListConfigurationPolicyAssociations` response. You can filter by the Amazon Resource Name (ARN) or universally unique identifier (UUID) of a configuration policy, `AssociationType`, or `AssociationStatus`.

## Contents
<a name="API_AssociationFilters_Contents"></a>

 ** AssociationStatus **   <a name="securityhub-Type-AssociationFilters-AssociationStatus"></a>
 The current status of the association between a target and a configuration policy.
Type: String
Valid Values: `PENDING | SUCCESS | FAILED`
Required: No

 ** AssociationType **   <a name="securityhub-Type-AssociationFilters-AssociationType"></a>
 Indicates whether the association between a target and a configuration was directly applied by the AWS Security Hub CSPM delegated administrator or inherited from a parent.
Type: String
Valid Values: `INHERITED | APPLIED`
Required: No

 ** ConfigurationPolicyId **   <a name="securityhub-Type-AssociationFilters-ConfigurationPolicyId"></a>
 The ARN or UUID of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AssociationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AssociationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AssociationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AssociationFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
