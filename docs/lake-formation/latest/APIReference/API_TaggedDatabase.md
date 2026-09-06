---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TaggedDatabase.html
---

# TaggedDatabase
<a name="API_TaggedDatabase"></a>

A structure describing a database resource with LF-tags.

## Contents
<a name="API_TaggedDatabase_Contents"></a>

 ** Database **   <a name="lakeformation-Type-TaggedDatabase-Database"></a>
A database that has LF-tags attached to it.
Type: [DatabaseResource](API_DatabaseResource.md) object
Required: No

 ** LFTags **   <a name="lakeformation-Type-TaggedDatabase-LFTags"></a>
A list of LF-tags attached to the database.
Type: Array of [LFTagPair](API_LFTagPair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_TaggedDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TaggedDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TaggedDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TaggedDatabase)
