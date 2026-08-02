---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapshotFilter.html
---

# SnapshotFilter
<a name="API_SnapshotFilter"></a>

A filter used to restrict the results of `DescribeSnapshots` calls. You can use multiple filters to return results that meet all applied filter requirements.

## Contents
<a name="API_SnapshotFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-SnapshotFilter-Name"></a>
The name of the filter to use. You can filter by the `file-system-id` or by `volume-id`.
Type: String
Valid Values: `file-system-id | volume-id`
Required: No

 ** Values **   <a name="FSx-Type-SnapshotFilter-Values"></a>
The `file-system-id` or `volume-id` that you are filtering for.
Type: Array of strings
Array Members: Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
Required: No

## See Also
<a name="API_SnapshotFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapshotFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapshotFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapshotFilter)
