---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_BundleResourceAssociation.html
---

# BundleResourceAssociation
<a name="API_BundleResourceAssociation"></a>

Describes the association between an application and a bundle resource.

## Contents
<a name="API_BundleResourceAssociation_Contents"></a>

 ** AssociatedResourceId **   <a name="WorkSpaces-Type-BundleResourceAssociation-AssociatedResourceId"></a>
The identifier of the associated resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** AssociatedResourceType **   <a name="WorkSpaces-Type-BundleResourceAssociation-AssociatedResourceType"></a>
The resource type of the associated resources.
Type: String
Valid Values: `APPLICATION`
Required: No

 ** BundleId **   <a name="WorkSpaces-Type-BundleResourceAssociation-BundleId"></a>
The identifier of the bundle.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** Created **   <a name="WorkSpaces-Type-BundleResourceAssociation-Created"></a>
The time the association is created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="WorkSpaces-Type-BundleResourceAssociation-LastUpdatedTime"></a>
The time the association status was last updated.
Type: Timestamp
Required: No

 ** State **   <a name="WorkSpaces-Type-BundleResourceAssociation-State"></a>
The status of the bundle resource association.
Type: String
Valid Values: `PENDING_INSTALL | PENDING_INSTALL_DEPLOYMENT | PENDING_UNINSTALL | PENDING_UNINSTALL_DEPLOYMENT | INSTALLING | UNINSTALLING | ERROR | COMPLETED | REMOVED`
Required: No

 ** StateReason **   <a name="WorkSpaces-Type-BundleResourceAssociation-StateReason"></a>
The reason the association deployment failed.
Type: [AssociationStateReason](API_AssociationStateReason.md) object
Required: No

## See Also
<a name="API_BundleResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/BundleResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/BundleResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/BundleResourceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
