---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ApplicationResourceAssociation.html
---

# ApplicationResourceAssociation
<a name="API_ApplicationResourceAssociation"></a>

Describes the association between an application and an application resource.

## Contents
<a name="API_ApplicationResourceAssociation_Contents"></a>

 ** ApplicationId **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-ApplicationId"></a>
The identifier of the application.
Type: String
Pattern: `^wsa-[0-9a-z]{8,63}$`
Required: No

 ** AssociatedResourceId **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-AssociatedResourceId"></a>
The identifier of the associated resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** AssociatedResourceType **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-AssociatedResourceType"></a>
The resource type of the associated resource.
Type: String
Valid Values: `WORKSPACE | BUNDLE | IMAGE`
Required: No

 ** Created **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-Created"></a>
The time the association was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-LastUpdatedTime"></a>
The time the association status was last updated.
Type: Timestamp
Required: No

 ** State **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-State"></a>
The status of the application resource association.
Type: String
Valid Values: `PENDING_INSTALL | PENDING_INSTALL_DEPLOYMENT | PENDING_UNINSTALL | PENDING_UNINSTALL_DEPLOYMENT | INSTALLING | UNINSTALLING | ERROR | COMPLETED | REMOVED`
Required: No

 ** StateReason **   <a name="WorkSpaces-Type-ApplicationResourceAssociation-StateReason"></a>
The reason the association deployment failed.
Type: [AssociationStateReason](API_AssociationStateReason.md) object
Required: No

## See Also
<a name="API_ApplicationResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ApplicationResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ApplicationResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ApplicationResourceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
