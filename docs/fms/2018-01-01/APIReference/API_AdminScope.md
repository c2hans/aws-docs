---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AdminScope.html
---

# AdminScope
<a name="API_AdminScope"></a>

Defines the resources that the Firewall Manager administrator can manage. For more information about administrative scope, see [Managing Firewall Manager administrators](https://docs.aws.amazon.com/waf/latest/developerguide/fms-administrators.html) in the *Firewall Manager Developer Guide*.

## Contents
<a name="API_AdminScope_Contents"></a>

 ** AccountScope **   <a name="fms-Type-AdminScope-AccountScope"></a>
Defines the accounts that the specified Firewall Manager administrator can apply policies to.
Type: [AccountScope](API_AccountScope.md) object
Required: No

 ** OrganizationalUnitScope **   <a name="fms-Type-AdminScope-OrganizationalUnitScope"></a>
Defines the AWS Organizations organizational units that the specified Firewall Manager administrator can apply policies to. For more information about OUs in Organizations, see [Managing organizational units (OUs) ](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *Organizations User Guide*.
Type: [OrganizationalUnitScope](API_OrganizationalUnitScope.md) object
Required: No

 ** PolicyTypeScope **   <a name="fms-Type-AdminScope-PolicyTypeScope"></a>
Defines the Firewall Manager policy types that the specified Firewall Manager administrator can create and manage.
Type: [PolicyTypeScope](API_PolicyTypeScope.md) object
Required: No

 ** RegionScope **   <a name="fms-Type-AdminScope-RegionScope"></a>
Defines the AWS Regions that the specified Firewall Manager administrator can perform actions in.
Type: [RegionScope](API_RegionScope.md) object
Required: No

## See Also
<a name="API_AdminScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AdminScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AdminScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AdminScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
