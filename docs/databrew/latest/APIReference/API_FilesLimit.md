---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_FilesLimit.html
---

# FilesLimit
<a name="API_FilesLimit"></a>

Represents a limit imposed on number of Amazon S3 files that should be selected for a dataset from a connected Amazon S3 path.

## Contents
<a name="API_FilesLimit_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaxFiles **   <a name="databrew-Type-FilesLimit-MaxFiles"></a>
The number of Amazon S3 files to select.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Order **   <a name="databrew-Type-FilesLimit-Order"></a>
A criteria to use for Amazon S3 files sorting before their selection. By default uses DESCENDING order, i.e. most recent files are selected first. Another possible value is ASCENDING.
Type: String
Valid Values: `DESCENDING | ASCENDING`
Required: No

 ** OrderedBy **   <a name="databrew-Type-FilesLimit-OrderedBy"></a>
A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST\_MODIFIED\_DATE as a sorting criteria. Currently it's the only allowed value.
Type: String
Valid Values: `LAST_MODIFIED_DATE`
Required: No

## See Also
<a name="API_FilesLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/FilesLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/FilesLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/FilesLimit)
