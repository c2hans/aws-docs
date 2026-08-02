---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImageResourceAssociation.html
---

# ImageResourceAssociation
<a name="API_ImageResourceAssociation"></a>

Describes the association between an application and an image resource.

## Contents
<a name="API_ImageResourceAssociation_Contents"></a>

 ** AssociatedResourceId **   <a name="WorkSpaces-Type-ImageResourceAssociation-AssociatedResourceId"></a>
The identifier of the associated resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** AssociatedResourceType **   <a name="WorkSpaces-Type-ImageResourceAssociation-AssociatedResourceType"></a>
The resource type of the associated resources.
Type: String
Valid Values: `APPLICATION`
Required: No

 ** Created **   <a name="WorkSpaces-Type-ImageResourceAssociation-Created"></a>
The time the association is created.
Type: Timestamp
Required: No

 ** ImageId **   <a name="WorkSpaces-Type-ImageResourceAssociation-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: No

 ** LastUpdatedTime **   <a name="WorkSpaces-Type-ImageResourceAssociation-LastUpdatedTime"></a>
The time the association status was last updated.
Type: Timestamp
Required: No

 ** State **   <a name="WorkSpaces-Type-ImageResourceAssociation-State"></a>
The status of the image resource association.
Type: String
Valid Values: `PENDING_INSTALL | PENDING_INSTALL_DEPLOYMENT | PENDING_UNINSTALL | PENDING_UNINSTALL_DEPLOYMENT | INSTALLING | UNINSTALLING | ERROR | COMPLETED | REMOVED`
Required: No

 ** StateReason **   <a name="WorkSpaces-Type-ImageResourceAssociation-StateReason"></a>
The reason the association deployment failed.
Type: [AssociationStateReason](API_AssociationStateReason.md) object
Required: No

## See Also
<a name="API_ImageResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImageResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImageResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImageResourceAssociation)
