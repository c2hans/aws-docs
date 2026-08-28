---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_FailedCreateAssociation.html
---

# FailedCreateAssociation
<a name="API_FailedCreateAssociation"></a>

Describes a failed association.

## Contents
<a name="API_FailedCreateAssociation_Contents"></a>

 ** Entry **   <a name="systemsmanager-Type-FailedCreateAssociation-Entry"></a>
The association.
Type: [CreateAssociationBatchRequestEntry](API_CreateAssociationBatchRequestEntry.md) object
Required: No

 ** Fault **   <a name="systemsmanager-Type-FailedCreateAssociation-Fault"></a>
The source of the failure.
Type: String
Valid Values: `Client | Server | Unknown`
Required: No

 ** Message **   <a name="systemsmanager-Type-FailedCreateAssociation-Message"></a>
A description of the failure.
Type: String
Required: No

## See Also
<a name="API_FailedCreateAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/FailedCreateAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/FailedCreateAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/FailedCreateAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
