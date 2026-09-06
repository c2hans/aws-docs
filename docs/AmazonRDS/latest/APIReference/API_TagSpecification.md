---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_TagSpecification.html
---

# TagSpecification
<a name="API_TagSpecification"></a>

The tags to apply to resources when creating or modifying a DB instance or DB cluster. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

## Contents
<a name="API_TagSpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceType **
The type of resource to tag on creation.
Valid Values:
+  `auto-backup` - The DB instance's automated backup.
+  `cluster-auto-backup` - The DB cluster's automated backup.
Type: String
Required: No

 ** Tags.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_TagSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/TagSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/TagSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/TagSpecification)
