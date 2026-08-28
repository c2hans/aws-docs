---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_OrganizationalUnitScope.html
---

# OrganizationalUnitScope
<a name="API_OrganizationalUnitScope"></a>

Defines the Organizations organizational units (OUs) that the specified Firewall Manager administrator can apply policies to. For more information about OUs in Organizations, see [Managing organizational units (OUs) ](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *Organizations User Guide*.

## Contents
<a name="API_OrganizationalUnitScope_Contents"></a>

 ** AllOrganizationalUnitsEnabled **   <a name="fms-Type-OrganizationalUnitScope-AllOrganizationalUnitsEnabled"></a>
A boolean value that indicates if the administrator can apply policies to all OUs within an organization. If true, the administrator can manage all OUs within the organization. You can either enable management of all OUs through this operation, or you can specify OUs to manage in `OrganizationalUnitScope$OrganizationalUnits`. You cannot specify both.
Type: Boolean
Required: No

 ** ExcludeSpecifiedOrganizationalUnits **   <a name="fms-Type-OrganizationalUnitScope-ExcludeSpecifiedOrganizationalUnits"></a>
A boolean value that excludes the OUs in `OrganizationalUnitScope$OrganizationalUnits` from the administrator's scope. If true, the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs listed in `OrganizationalUnitScope$OrganizationalUnits`. You can either specify a list of OUs to exclude by `OrganizationalUnitScope$OrganizationalUnits`, or you can enable management of all OUs by `OrganizationalUnitScope$AllOrganizationalUnitsEnabled`. You cannot specify both.
Type: Boolean
Required: No

 ** OrganizationalUnits **   <a name="fms-Type-OrganizationalUnitScope-OrganizationalUnits"></a>
The list of OUs within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits`. If `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits` is set to `true`, then the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs in this list. If `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits` is set to `false`, then the Firewall Manager administrator can only apply policies to the OUs in this list.
Type: Array of strings
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

## See Also
<a name="API_OrganizationalUnitScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/OrganizationalUnitScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/OrganizationalUnitScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/OrganizationalUnitScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
