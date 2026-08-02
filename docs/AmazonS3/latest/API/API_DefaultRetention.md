---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DefaultRetention.html
---

# DefaultRetention
<a name="API_DefaultRetention"></a>

The container element for optionally specifying the default Object Lock retention settings for new objects placed in the specified bucket.

**Note**
The `DefaultRetention` settings require both a mode and a period.
The `DefaultRetention` period can be either `Days` or `Years` but you must select one. You cannot specify `Days` and `Years` at the same time.

## Contents
<a name="API_DefaultRetention_Contents"></a>

 ** Days **   <a name="AmazonS3-Type-DefaultRetention-Days"></a>
The number of days that you want to specify for the default retention period. Must be used with `Mode`.
Type: Integer
Required: No

 ** Mode **   <a name="AmazonS3-Type-DefaultRetention-Mode"></a>
The default Object Lock retention mode you want to apply to new objects placed in the specified bucket. Must be used with either `Days` or `Years`.
Type: String
Valid Values: `GOVERNANCE | COMPLIANCE`
Required: No

 ** Years **   <a name="AmazonS3-Type-DefaultRetention-Years"></a>
The number of years that you want to specify for the default retention period. Must be used with `Mode`.
Type: Integer
Required: No

## See Also
<a name="API_DefaultRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DefaultRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DefaultRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DefaultRetention)
