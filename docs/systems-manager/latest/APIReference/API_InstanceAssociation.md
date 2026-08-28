---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceAssociation.html
---

# InstanceAssociation
<a name="API_InstanceAssociation"></a>

One or more association documents on the managed node.

## Contents
<a name="API_InstanceAssociation_Contents"></a>

 ** AssociationId **   <a name="systemsmanager-Type-InstanceAssociation-AssociationId"></a>
The association ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-InstanceAssociation-AssociationVersion"></a>
Version information for the association on the managed node.
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** Content **   <a name="systemsmanager-Type-InstanceAssociation-Content"></a>
The content of the association document for the managed nodes.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-InstanceAssociation-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

## See Also
<a name="API_InstanceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
