---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_S3FilesLocation.html
---

# S3FilesLocation
<a name="API_S3FilesLocation"></a>

The Amazon Simple Storage Service objects to import as the cells of a notebook, specified as a bucket and an ordered list of object keys.

## Contents
<a name="API_S3FilesLocation_Contents"></a>

 ** bucket **   <a name="datazone-Type-S3FilesLocation-bucket"></a>
The name of the Amazon Simple Storage Service bucket that contains the files to import.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`
Required: Yes

 ** fileList **   <a name="datazone-Type-S3FilesLocation-fileList"></a>
The files to import. Cells are created in the order in which you list the files. You can specify between 1 and 100 files.
Type: Array of [S3File](API_S3File.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_S3FilesLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/S3FilesLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/S3FilesLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/S3FilesLocation)
