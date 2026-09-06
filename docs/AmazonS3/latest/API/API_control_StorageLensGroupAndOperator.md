---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupAndOperator.html
---

# StorageLensGroupAndOperator
<a name="API_control_StorageLensGroupAndOperator"></a>

 A logical operator that allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data.

## Contents
<a name="API_control_StorageLensGroupAndOperator_Contents"></a>

 ** MatchAnyPrefix **   <a name="AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix"></a>
 Contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.
Type: Array of strings
Required: No

 ** MatchAnySuffix **   <a name="AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix"></a>
 Contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.
Type: Array of strings
Required: No

 ** MatchAnyTag **   <a name="AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag"></a>
 Contains the list of object tags. At least one object tag must be specified. Up to 10 object tags are allowed.
Type: Array of [S3Tag](API_control_S3Tag.md) data types
Required: No

 ** MatchObjectAge **   <a name="AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge"></a>
 Contains `DaysGreaterThan` and `DaysLessThan` to define the object age range (minimum and maximum number of days).
Type: [MatchObjectAge](API_control_MatchObjectAge.md) data type
Required: No

 ** MatchObjectSize **   <a name="AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize"></a>
 Contains `BytesGreaterThan` and `BytesLessThan` to define the object size range (minimum and maximum number of Bytes).
Type: [MatchObjectSize](API_control_MatchObjectSize.md) data type
Required: No

## See Also
<a name="API_control_StorageLensGroupAndOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensGroupAndOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensGroupAndOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensGroupAndOperator)
