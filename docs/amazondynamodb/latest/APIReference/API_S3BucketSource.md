---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_S3BucketSource.html
---

# S3BucketSource
<a name="API_S3BucketSource"></a>

 The S3 bucket that is being imported from.

## Contents
<a name="API_S3BucketSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** S3Bucket **   <a name="DDB-Type-S3BucketSource-S3Bucket"></a>
 The S3 bucket that is being imported from.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
Required: Yes

 ** S3BucketOwner **   <a name="DDB-Type-S3BucketSource-S3BucketOwner"></a>
 The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** S3KeyPrefix **   <a name="DDB-Type-S3BucketSource-S3KeyPrefix"></a>
 The key prefix shared by all S3 Objects that are being imported.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_S3BucketSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/S3BucketSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/S3BucketSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/S3BucketSource)
