---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseColumnList.html
---

# DatabaseColumnList
<a name="API_DatabaseColumnList"></a>

The structure used to configure the list of column patterns in source database endpoint for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

## Contents
<a name="API_DatabaseColumnList_Contents"></a>

 ** Exclude **   <a name="Firehose-Type-DatabaseColumnList-Exclude"></a>
 The list of column patterns in source database to be excluded for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 194.
Pattern: `[\u0001-\uFFFF]*`
Required: No

 ** Include **   <a name="Firehose-Type-DatabaseColumnList-Include"></a>
 The list of column patterns in source database to be included for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 194.
Pattern: `[\u0001-\uFFFF]*`
Required: No

## See Also
<a name="API_DatabaseColumnList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DatabaseColumnList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DatabaseColumnList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DatabaseColumnList)
