---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociatedPermission.html
---

# AssociatedPermission
<a name="API_AssociatedPermission"></a>

An object that describes a managed permission associated with a resource share.

## Contents
<a name="API_AssociatedPermission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="ram-Type-AssociatedPermission-arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the associated managed permission.
Type: String
Required: No

 ** defaultVersion **   <a name="ram-Type-AssociatedPermission-defaultVersion"></a>
Indicates whether the associated resource share is using the default version of the permission.
Type: Boolean
Required: No

 ** featureSet **   <a name="ram-Type-AssociatedPermission-featureSet"></a>
Indicates what features are available for this resource share. This parameter can have one of the following values:
+  **STANDARD** – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in AWS RAM using the console or APIs. This resource share might have been created by AWS RAM, or it might have been **CREATED\_FROM\_POLICY** and then promoted.
+  **CREATED\_FROM\_POLICY** – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so AWS RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the AWS account that created it. You can't modify it in AWS RAM unless you promote it. For more information, see [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md).
+  **PROMOTING\_TO\_STANDARD** – This resource share was originally `CREATED_FROM_POLICY`, but the customer ran the [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md) and that operation is still in progress. This value changes to `STANDARD` when complete.
Type: String
Valid Values: `CREATED_FROM_POLICY | PROMOTING_TO_STANDARD | STANDARD`
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-AssociatedPermission-lastUpdatedTime"></a>
The date and time when the association between the permission and the resource share was last updated.
Type: Timestamp
Required: No

 ** permissionVersion **   <a name="ram-Type-AssociatedPermission-permissionVersion"></a>
The version of the permission currently associated with the resource share.
Type: String
Required: No

 ** resourceShareArn **   <a name="ram-Type-AssociatedPermission-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a resource share associated with this permission.
Type: String
Required: No

 ** resourceType **   <a name="ram-Type-AssociatedPermission-resourceType"></a>
The resource type to which this permission applies.
Type: String
Required: No

 ** status **   <a name="ram-Type-AssociatedPermission-status"></a>
The current status of the association between the permission and the resource share. The following are the possible values:
+  `ATTACHABLE` – This permission or version can be associated with resource shares.
+  `UNATTACHABLE` – This permission or version can't currently be associated with resource shares.
+  `DELETING` – This permission or version is in the process of being deleted.
+  `DELETED` – This permission or version is deleted.
Type: String
Required: No

## See Also
<a name="API_AssociatedPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/AssociatedPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/AssociatedPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/AssociatedPermission)
