---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_NamespaceSummary.html
---

# NamespaceSummary
<a name="API_s3Buckets_NamespaceSummary"></a>

Contains details about a namespace.

## Contents
<a name="API_s3Buckets_NamespaceSummary_Contents"></a>

 ** createdAt **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-createdAt"></a>
The date and time the namespace was created at.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-createdBy"></a>
The ID of the account that created the namespace.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9].*`
Required: Yes

 ** namespace **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-namespace"></a>
The name of the namespace.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** ownerAccountId **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-ownerAccountId"></a>
The ID of the account that owns the namespace.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9].*`
Required: Yes

 ** namespaceId **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-namespaceId"></a>
The system-assigned unique identifier for the namespace.
Type: String
Required: No

 ** tableBucketId **   <a name="AmazonS3-Type-s3Buckets_NamespaceSummary-tableBucketId"></a>
The system-assigned unique identifier for the table bucket that contains this namespace.
Type: String
Required: No

## See Also
<a name="API_s3Buckets_NamespaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/NamespaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/NamespaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/NamespaceSummary)
