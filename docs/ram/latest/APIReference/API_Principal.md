---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_Principal.html
---

# Principal
<a name="API_Principal"></a>

Describes a principal for use with AWS Resource Access Manager.

## Contents
<a name="API_Principal_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** creationTime **   <a name="ram-Type-Principal-creationTime"></a>
The date and time when the principal was associated with the resource share.
Type: Timestamp
Required: No

 ** external **   <a name="ram-Type-Principal-external"></a>
Indicates the relationship between the AWS account the principal belongs to and the account that owns the resource share:
+  `True` – The two accounts belong to same organization.
+  `False` – The two accounts do not belong to the same organization.
Type: Boolean
Required: No

 ** id **   <a name="ram-Type-Principal-id"></a>
The ID of the principal that can be associated with a resource share.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-Principal-lastUpdatedTime"></a>
The date and time when the association between the resource share and the principal was last updated.
Type: Timestamp
Required: No

 ** resourceShareArn **   <a name="ram-Type-Principal-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a resource share the principal is associated with.
Type: String
Required: No

## See Also
<a name="API_Principal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/Principal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/Principal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/Principal)
