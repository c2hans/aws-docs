---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UnfilteredPartition.html
---

# UnfilteredPartition
<a name="API_UnfilteredPartition"></a>

A partition that contains unfiltered metadata.

## Contents
<a name="API_UnfilteredPartition_Contents"></a>

 ** AuthorizedColumns **   <a name="Glue-Type-UnfilteredPartition-AuthorizedColumns"></a>
The list of columns the user has permissions to access.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** IsRegisteredWithLakeFormation **   <a name="Glue-Type-UnfilteredPartition-IsRegisteredWithLakeFormation"></a>
A Boolean value indicating that the partition location is registered with Lake Formation.
Type: Boolean
Required: No

 ** Partition **   <a name="Glue-Type-UnfilteredPartition-Partition"></a>
The partition object.
Type: [Partition](API_Partition.md) object
Required: No

## See Also
<a name="API_UnfilteredPartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UnfilteredPartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UnfilteredPartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UnfilteredPartition)
