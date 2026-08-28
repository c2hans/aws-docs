---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html
---

# ResourceSharePermissionDetail
<a name="API_ResourceSharePermissionDetail"></a>

Information about a AWS RAM managed permission.

## Contents
<a name="API_ResourceSharePermissionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="ram-Type-ResourceSharePermissionDetail-arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of this AWS RAM managed permission.
Type: String
Required: No

 ** creationTime **   <a name="ram-Type-ResourceSharePermissionDetail-creationTime"></a>
The date and time when the permission was created.
Type: Timestamp
Required: No

 ** defaultVersion **   <a name="ram-Type-ResourceSharePermissionDetail-defaultVersion"></a>
Specifies whether the version of the permission represented in this response is the default version for this permission.
Type: Boolean
Required: No

 ** featureSet **   <a name="ram-Type-ResourceSharePermissionDetail-featureSet"></a>
Indicates what features are available for this resource share. This parameter can have one of the following values:
+  **STANDARD** – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in AWS RAM using the console or APIs. This resource share might have been created by AWS RAM, or it might have been **CREATED\_FROM\_POLICY** and then promoted.
+  **CREATED\_FROM\_POLICY** – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so AWS RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the AWS account that created it. You can't modify it in AWS RAM unless you promote it. For more information, see [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md).
+  **PROMOTING\_TO\_STANDARD** – This resource share was originally `CREATED_FROM_POLICY`, but the customer ran the [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md) and that operation is still in progress. This value changes to `STANDARD` when complete.
Type: String
Valid Values: `CREATED_FROM_POLICY | PROMOTING_TO_STANDARD | STANDARD`
Required: No

 ** isResourceTypeDefault **   <a name="ram-Type-ResourceSharePermissionDetail-isResourceTypeDefault"></a>
Specifies whether the version of the permission represented in this response is the default version for all resources of this resource type.
Type: Boolean
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-ResourceSharePermissionDetail-lastUpdatedTime"></a>
The date and time when the permission was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="ram-Type-ResourceSharePermissionDetail-name"></a>
The name of this permission.
Type: String
Required: No

 ** permission **   <a name="ram-Type-ResourceSharePermissionDetail-permission"></a>
The permission's effect and actions in JSON format. The `effect` indicates whether the specified actions are allowed or denied. The `actions` list the operations to which the principal is granted or denied access.
Type: String
Required: No

 ** permissionType **   <a name="ram-Type-ResourceSharePermissionDetail-permissionType"></a>
The type of managed permission. This can be one of the following values:
+  `AWS_MANAGED` – AWS created and manages this managed permission. You can associate it with your resource shares, but you can't modify it.
+  `CUSTOMER_MANAGED` – You, or another principal in your account created this managed permission. You can associate it with your resource shares and create new versions that have different permissions.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** resourceType **   <a name="ram-Type-ResourceSharePermissionDetail-resourceType"></a>
The resource type to which this permission applies.
Type: String
Required: No

 ** status **   <a name="ram-Type-ResourceSharePermissionDetail-status"></a>
The current status of the association between the permission and the resource share. The following are the possible values:
+  `ATTACHABLE` – This permission or version can be associated with resource shares.
+  `UNATTACHABLE` – This permission or version can't currently be associated with resource shares.
+  `DELETING` – This permission or version is in the process of being deleted.
+  `DELETED` – This permission or version is deleted.
Type: String
Valid Values: `ATTACHABLE | UNATTACHABLE | DELETING | DELETED`
Required: No

 ** tags **   <a name="ram-Type-ResourceSharePermissionDetail-tags"></a>
The tag key and value pairs attached to the resource share.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** version **   <a name="ram-Type-ResourceSharePermissionDetail-version"></a>
The version of the permission described in this response.
Type: String
Required: No

## See Also
<a name="API_ResourceSharePermissionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ResourceSharePermissionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ResourceSharePermissionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ResourceSharePermissionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
