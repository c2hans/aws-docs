---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareAssociation.html
---

# ResourceShareAssociation
<a name="API_ResourceShareAssociation"></a>

Describes an association between a resource share and either a principal or a resource.

## Contents
<a name="API_ResourceShareAssociation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** associatedEntity **   <a name="ram-Type-ResourceShareAssociation-associatedEntity"></a>
The associated entity. This can be either of the following:
+ For a resource association, this is the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource.
+ For principal associations, this is one of the following:
  + The ID of an AWS account
  + The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in AWS Organizations
  + The ARN of an organizational unit (OU) in AWS Organizations
  + The ARN of an IAM role
  + The ARN of an IAM user
Type: String
Required: No

 ** associationType **   <a name="ram-Type-ResourceShareAssociation-associationType"></a>
The type of entity included in this association.
Type: String
Valid Values: `PRINCIPAL | RESOURCE | SOURCE`
Required: No

 ** creationTime **   <a name="ram-Type-ResourceShareAssociation-creationTime"></a>
The date and time when the association was created.
Type: Timestamp
Required: No

 ** external **   <a name="ram-Type-ResourceShareAssociation-external"></a>
Indicates whether the principal belongs to the same organization in AWS Organizations as the AWS account that owns the resource share.
Type: Boolean
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-ResourceShareAssociation-lastUpdatedTime"></a>
The date and time when the association was last updated.
Type: Timestamp
Required: No

 ** resourceShareArn **   <a name="ram-Type-ResourceShareAssociation-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share.
Type: String
Required: No

 ** resourceShareName **   <a name="ram-Type-ResourceShareAssociation-resourceShareName"></a>
The name of the resource share.
Type: String
Required: No

 ** status **   <a name="ram-Type-ResourceShareAssociation-status"></a>
The current status of the association.
Type: String
Valid Values: `ASSOCIATING | ASSOCIATED | FAILED | DISASSOCIATING | DISASSOCIATED | SUSPENDED | SUSPENDING | RESTORING`
Required: No

 ** statusMessage **   <a name="ram-Type-ResourceShareAssociation-statusMessage"></a>
A message about the status of the association.
Type: String
Required: No

## See Also
<a name="API_ResourceShareAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ResourceShareAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ResourceShareAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ResourceShareAssociation)
