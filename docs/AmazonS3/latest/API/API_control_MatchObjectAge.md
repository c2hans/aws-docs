---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MatchObjectAge.html
---

# MatchObjectAge
<a name="API_control_MatchObjectAge"></a>

 A filter condition that specifies the object age range of included objects in days. Only integers are supported.

## Contents
<a name="API_control_MatchObjectAge_Contents"></a>

 ** DaysGreaterThan **   <a name="AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan"></a>
 Specifies the maximum object age in days. Must be a positive whole number, greater than the minimum object age and less than or equal to 2,147,483,647.
Type: Integer
Required: No

 ** DaysLessThan **   <a name="AmazonS3-Type-control_MatchObjectAge-DaysLessThan"></a>
 Specifies the minimum object age in days. The value must be a positive whole number, greater than 0 and less than or equal to 2,147,483,647.
Type: Integer
Required: No

## See Also
<a name="API_control_MatchObjectAge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/MatchObjectAge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/MatchObjectAge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/MatchObjectAge)
