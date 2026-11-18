---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_TextSearchConfiguration.html
---

# TextSearchConfiguration
<a name="API_S3VectorBuckets_TextSearchConfiguration"></a>

A full-text search configuration for a single metadata key.

## Contents
<a name="API_S3VectorBuckets_TextSearchConfiguration_Contents"></a>

 ** metadataKey **   <a name="AmazonS3-Type-S3VectorBuckets_TextSearchConfiguration-metadataKey"></a>
The metadata key to make full-text searchable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: Yes

 ** language **   <a name="AmazonS3-Type-S3VectorBuckets_TextSearchConfiguration-language"></a>
The language that the text search analyzer uses. Valid values are `en` (English), `fr` (French), `es` (Spanish), `pt` (Portuguese), `it` (Italian), `de` (German), `nl` (Dutch), `zh` (Chinese), `ja` (Japanese), and `ko` (Korean). If you don't specify a language, Amazon S3 Vectors uses the default standard analyzer.
Type: String
Valid Values: `en | fr | es | pt | it | de | nl | zh | ja | ko`
Required: No

 ** status **   <a name="AmazonS3-Type-S3VectorBuckets_TextSearchConfiguration-status"></a>
The backfill status of the text search configuration. Valid values are `ACTIVE`, which indicates that the analyzer is built and serving queries, and `BUILDING`, which indicates that the analyzer is being backfilled and isn't yet serving queries. This field is returned by `GetIndex`.
Type: String
Valid Values: `ACTIVE | BUILDING`
Required: No

## See Also
<a name="API_S3VectorBuckets_TextSearchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/TextSearchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/TextSearchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/TextSearchConfiguration)
