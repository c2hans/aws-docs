---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspacesIpGroup.html
---

# WorkspacesIpGroup
<a name="API_WorkspacesIpGroup"></a>

Describes an IP access control group.

## Contents
<a name="API_WorkspacesIpGroup_Contents"></a>

 ** groupDesc **   <a name="WorkSpaces-Type-WorkspacesIpGroup-groupDesc"></a>
The description of the group.
Type: String
Required: No

 ** groupId **   <a name="WorkSpaces-Type-WorkspacesIpGroup-groupId"></a>
The identifier of the group.
Type: String
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: No

 ** groupName **   <a name="WorkSpaces-Type-WorkspacesIpGroup-groupName"></a>
The name of the group.
Type: String
Required: No

 ** userRules **   <a name="WorkSpaces-Type-WorkspacesIpGroup-userRules"></a>
The rules.
Type: Array of [IpRuleItem](API_IpRuleItem.md) objects
Required: No

## See Also
<a name="API_WorkspacesIpGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspacesIpGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspacesIpGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspacesIpGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
