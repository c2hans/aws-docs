---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionSummary.html
---

# ResourceSharePermissionSummary
<a name="API_ResourceSharePermissionSummary"></a>

Information about an AWS RAM permission.

## Contents
<a name="API_ResourceSharePermissionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="ram-Type-ResourceSharePermissionSummary-arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the permission you want information about.
Type: String
Required: No

 ** creationTime **   <a name="ram-Type-ResourceSharePermissionSummary-creationTime"></a>
The date and time when the permission was created.
Type: Timestamp
Required: No

 ** defaultVersion **   <a name="ram-Type-ResourceSharePermissionSummary-defaultVersion"></a>
Specifies whether the version of the managed permission used by this resource share is the default version for this managed permission.
Type: Boolean
Required: No

 ** featureSet **   <a name="ram-Type-ResourceSharePermissionSummary-featureSet"></a>
Indicates what features are available for this resource share. This parameter can have one of the following values:
+  **STANDARD** – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in AWS RAM using the console or APIs. This resource share might have been created by AWS RAM, or it might have been **CREATED\_FROM\_POLICY** and then promoted.
+  **CREATED\_FROM\_POLICY** – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so AWS RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the AWS account that created it. You can't modify it in AWS RAM unless you promote it. For more information, see [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md).
+  **PROMOTING\_TO\_STANDARD** – This resource share was originally `CREATED_FROM_POLICY`, but the customer ran the [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md) and that operation is still in progress. This value changes to `STANDARD` when complete.
Type: String
Valid Values: `CREATED_FROM_POLICY | PROMOTING_TO_STANDARD | STANDARD`
Required: No

 ** isResourceTypeDefault **   <a name="ram-Type-ResourceSharePermissionSummary-isResourceTypeDefault"></a>
Specifies whether the managed permission associated with this resource share is the default managed permission for all resources of this resource type.
Type: Boolean
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-ResourceSharePermissionSummary-lastUpdatedTime"></a>
The date and time when the permission was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="ram-Type-ResourceSharePermissionSummary-name"></a>
The name of this managed permission.
Type: String
Required: No

 ** permissionType **   <a name="ram-Type-ResourceSharePermissionSummary-permissionType"></a>
The type of managed permission. This can be one of the following values:
+  `AWS_MANAGED` – AWS created and manages this managed permission. You can associate it with your resource shares, but you can't modify it.
+  `CUSTOMER_MANAGED` – You, or another principal in your account created this managed permission. You can associate it with your resource shares and create new versions that have different permissions.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** resourceType **   <a name="ram-Type-ResourceSharePermissionSummary-resourceType"></a>
The type of resource to which this permission applies. This takes the form of: `service-code`:`resource-code`, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string `ec2:subnet`.
Type: String
Required: No

 ** status **   <a name="ram-Type-ResourceSharePermissionSummary-status"></a>
The current status of the permission.
Type: String
Required: No

 ** tags **   <a name="ram-Type-ResourceSharePermissionSummary-tags"></a>
A list of the tag key value pairs currently attached to the permission.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** version **   <a name="ram-Type-ResourceSharePermissionSummary-version"></a>
The version of the permission associated with this resource share.
Type: String
Required: No

## See Also
<a name="API_ResourceSharePermissionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ResourceSharePermissionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ResourceSharePermissionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ResourceSharePermissionSummary)
