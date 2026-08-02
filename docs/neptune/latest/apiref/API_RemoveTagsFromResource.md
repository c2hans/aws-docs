---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_RemoveTagsFromResource.html
---

# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes metadata tags from an Amazon Neptune resource.

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **
The Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see [ Constructing an Amazon Resource Name (ARN)](https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
Type: String
Required: Yes

 **TagKeys.member.N**
The tag key (name) of the tag to be removed.
Type: Array of strings
Required: Yes

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** DBSnapshotNotFound **
 *DBSnapshotIdentifier* does not refer to an existing DB snapshot.
HTTP Status Code: 404

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/RemoveTagsFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/RemoveTagsFromResource)
