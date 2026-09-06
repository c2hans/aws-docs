---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TrustStoreSummary.html
---

# TrustStoreSummary
<a name="API_TrustStoreSummary"></a>

A trust store summary.

## Contents
<a name="API_TrustStoreSummary_Contents"></a>

 ** Arn **   <a name="cloudfront-Type-TrustStoreSummary-Arn"></a>
The trust store's Amazon Resource Name (ARN).
Type: String
Required: Yes

 ** ETag **   <a name="cloudfront-Type-TrustStoreSummary-ETag"></a>
The version identifier for the current version of the trust store.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-TrustStoreSummary-Id"></a>
The trust store's ID.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-TrustStoreSummary-LastModifiedTime"></a>
The trust store's last modified time.
Type: Timestamp
Required: Yes

 ** Name **   <a name="cloudfront-Type-TrustStoreSummary-Name"></a>
The trust store's name.
Type: String
Required: Yes

 ** NumberOfCaCertificates **   <a name="cloudfront-Type-TrustStoreSummary-NumberOfCaCertificates"></a>
The trust store's number of CA certificates.
Type: Integer
Required: Yes

 ** Status **   <a name="cloudfront-Type-TrustStoreSummary-Status"></a>
The trust store's status.
Type: String
Valid Values: `pending | active | failed`
Required: Yes

 ** Reason **   <a name="cloudfront-Type-TrustStoreSummary-Reason"></a>
The trust store's reason.
Type: String
Required: No

## See Also
<a name="API_TrustStoreSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrustStoreSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrustStoreSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrustStoreSummary)
