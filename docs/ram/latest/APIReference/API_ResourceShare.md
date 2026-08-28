---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShare.html
---

# ResourceShare
<a name="API_ResourceShare"></a>

Describes a resource share in AWS RAM.

## Contents
<a name="API_ResourceShare_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** allowExternalPrincipals **   <a name="ram-Type-ResourceShare-allowExternalPrincipals"></a>
Indicates whether principals outside your organization in AWS Organizations can be associated with a resource share.
+  `True` – the resource share can be shared with any AWS account.
+  `False` – the resource share can be shared with only accounts in the same organization as the account that owns the resource share.
Type: Boolean
Required: No

 ** creationTime **   <a name="ram-Type-ResourceShare-creationTime"></a>
The date and time when the resource share was created.
Type: Timestamp
Required: No

 ** featureSet **   <a name="ram-Type-ResourceShare-featureSet"></a>
Indicates what features are available for this resource share. This parameter can have one of the following values:
+  **STANDARD** – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in AWS RAM using the console or APIs. This resource share might have been created by AWS RAM, or it might have been **CREATED\_FROM\_POLICY** and then promoted.
+  **CREATED\_FROM\_POLICY** – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so AWS RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the AWS account that created it. You can't modify it in AWS RAM unless you promote it. For more information, see [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md).
+  **PROMOTING\_TO\_STANDARD** – This resource share was originally `CREATED_FROM_POLICY`, but the customer ran the [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md) and that operation is still in progress. This value changes to `STANDARD` when complete.
Type: String
Valid Values: `CREATED_FROM_POLICY | PROMOTING_TO_STANDARD | STANDARD`
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-ResourceShare-lastUpdatedTime"></a>
The date and time when the resource share was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="ram-Type-ResourceShare-name"></a>
The name of the resource share.
Type: String
Required: No

 ** owningAccountId **   <a name="ram-Type-ResourceShare-owningAccountId"></a>
The ID of the AWS account that owns the resource share.
Type: String
Required: No

 ** resourceShareArn **   <a name="ram-Type-ResourceShare-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share
Type: String
Required: No

 ** resourceShareConfiguration **   <a name="ram-Type-ResourceShare-resourceShareConfiguration"></a>
The configuration of the resource share
Type: [ResourceShareConfiguration](API_ResourceShareConfiguration.md) object
Required: No

 ** status **   <a name="ram-Type-ResourceShare-status"></a>
The current status of the resource share.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING | DELETED`
Required: No

 ** statusMessage **   <a name="ram-Type-ResourceShare-statusMessage"></a>
A message about the status of the resource share.
Type: String
Required: No

 ** tags **   <a name="ram-Type-ResourceShare-tags"></a>
The tag key and value pairs attached to the resource share.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ResourceShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ResourceShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ResourceShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ResourceShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
