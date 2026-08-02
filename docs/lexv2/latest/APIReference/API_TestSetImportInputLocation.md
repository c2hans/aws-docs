---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetImportInputLocation.html
---

# TestSetImportInputLocation
<a name="API_TestSetImportInputLocation"></a>

Contains information about the Amazon S3 location from which the test set is imported.

## Contents
<a name="API_TestSetImportInputLocation_Contents"></a>

 ** s3BucketName **   <a name="lexv2-Type-TestSetImportInputLocation-s3BucketName"></a>
The name of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
Required: Yes

 ** s3Path **   <a name="lexv2-Type-TestSetImportInputLocation-s3Path"></a>
The path inside the Amazon S3 bucket pointing to the test-set CSV file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*$`
Required: Yes

## See Also
<a name="API_TestSetImportInputLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetImportInputLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetImportInputLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetImportInputLocation)
