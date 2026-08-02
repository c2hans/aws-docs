---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupOrOperator.html
---

# StorageLensGroupOrOperator
<a name="API_control_StorageLensGroupOrOperator"></a>

A container element for specifying `Or` rule conditions. The rule conditions determine the subset of objects to which the `Or` rule applies. Objects can match any of the listed filter conditions, which are joined by the `Or` logical operator. Only one of each filter condition is allowed.

## Contents
<a name="API_control_StorageLensGroupOrOperator_Contents"></a>

 ** MatchAnyPrefix **   <a name="AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix"></a>
 Filters objects that match any of the specified prefixes.
Type: Array of strings
Required: No

 ** MatchAnySuffix **   <a name="AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix"></a>
 Filters objects that match any of the specified suffixes.
Type: Array of strings
Required: No

 ** MatchAnyTag **   <a name="AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag"></a>
 Filters objects that match any of the specified S3 object tags.
Type: Array of [S3Tag](API_control_S3Tag.md) data types
Required: No

 ** MatchObjectAge **   <a name="AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge"></a>
 Filters objects that match the specified object age range.
Type: [MatchObjectAge](API_control_MatchObjectAge.md) data type
Required: No

 ** MatchObjectSize **   <a name="AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize"></a>
 Filters objects that match the specified object size range.
Type: [MatchObjectSize](API_control_MatchObjectSize.md) data type
Required: No

## See Also
<a name="API_control_StorageLensGroupOrOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensGroupOrOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensGroupOrOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensGroupOrOperator)
