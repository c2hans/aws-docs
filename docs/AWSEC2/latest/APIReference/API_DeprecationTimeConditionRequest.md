---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprecationTimeConditionRequest.html
---

# DeprecationTimeConditionRequest
<a name="API_DeprecationTimeConditionRequest"></a>

The maximum period since deprecation for allowed images.

## Contents
<a name="API_DeprecationTimeConditionRequest_Contents"></a>

 ** MaximumDaysSinceDeprecated **
The maximum number of days that have elapsed since the image was deprecated. Set to `0` to exclude all deprecated images.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_DeprecationTimeConditionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeprecationTimeConditionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeprecationTimeConditionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeprecationTimeConditionRequest)
