---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_NodeOwnerInfo.html
---

# NodeOwnerInfo
<a name="API_NodeOwnerInfo"></a>

Information about ownership of a managed node.

## Contents
<a name="API_NodeOwnerInfo_Contents"></a>

 ** AccountId **   <a name="systemsmanager-Type-NodeOwnerInfo-AccountId"></a>
The ID of the AWS account that owns the managed node.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** OrganizationalUnitId **   <a name="systemsmanager-Type-NodeOwnerInfo-OrganizationalUnitId"></a>
The ID of the organization unit (OU) that the account is part of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** OrganizationalUnitPath **   <a name="systemsmanager-Type-NodeOwnerInfo-OrganizationalUnitPath"></a>
The path for the organizational unit (OU) that owns the managed node. The path for the OU is built using the IDs of the organization, root, and all OUs in the path down to and including the OU. For example:
 `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_NodeOwnerInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/NodeOwnerInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/NodeOwnerInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/NodeOwnerInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
