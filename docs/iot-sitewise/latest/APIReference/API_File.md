---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_File.html
---

# File
<a name="API_File"></a>

The file in Amazon S3 where your data is saved.

## Contents
<a name="API_File_Contents"></a>

 ** bucket **   <a name="iotsitewise-Type-File-bucket"></a>
The name of the Amazon S3 bucket from which data is imported.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** key **   <a name="iotsitewise-Type-File-key"></a>
The key of the Amazon S3 object that contains your data. Each object has a key that is a unique identifier. Each object has exactly one key.
Type: String
Required: Yes

 ** alias **   <a name="iotsitewise-Type-File-alias"></a>
The alias associated with the file's time series.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** fileFormat **   <a name="iotsitewise-Type-File-fileFormat"></a>
The file format of the data in S3.
Type: [FileFormat](API_FileFormat.md) object
Required: No

 ** startTime **   <a name="iotsitewise-Type-File-startTime"></a>
The nanosecond-precision start time for the file data.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: No

 ** versionId **   <a name="iotsitewise-Type-File-versionId"></a>
The version ID to identify a specific version of the Amazon S3 object that contains your data.
Type: String
Required: No

## See Also
<a name="API_File_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/File)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/File)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/File)
