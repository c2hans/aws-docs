---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DependentEntity.html
---

# DependentEntity
<a name="API_SSMContacts_DependentEntity"></a>

Information about a resource that another resource is related to or depends on.

For example, if a contact is a member of a rotation, the rotation is a dependent entity of the contact.

## Contents
<a name="API_SSMContacts_DependentEntity_Contents"></a>

 ** DependentResourceIds **   <a name="IncidentManager-Type-SSMContacts_DependentEntity-DependentResourceIds"></a>
The Amazon Resource Names (ARNs) of the dependent resources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** RelationType **   <a name="IncidentManager-Type-SSMContacts_DependentEntity-RelationType"></a>
The type of relationship between one resource and the other resource that it is related to or depends on.
Type: String
Required: Yes

## See Also
<a name="API_SSMContacts_DependentEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/DependentEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/DependentEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/DependentEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
