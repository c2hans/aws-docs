---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_EyeDirection.html
---

# EyeDirection
<a name="API_EyeDirection"></a>

Indicates the direction the eyes are gazing in (independent of the head pose) as determined by its pitch and yaw.

## Contents
<a name="API_EyeDirection_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-EyeDirection-Confidence"></a>
The confidence that the service has in its predicted eye direction.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Pitch **   <a name="rekognition-Type-EyeDirection-Pitch"></a>
Value representing eye direction on the pitch axis.
Type: Float
Valid Range: Minimum value of -180. Maximum value of 180.
Required: No

 ** Yaw **   <a name="rekognition-Type-EyeDirection-Yaw"></a>
Value representing eye direction on the yaw axis.
Type: Float
Valid Range: Minimum value of -180. Maximum value of 180.
Required: No

## See Also
<a name="API_EyeDirection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/EyeDirection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/EyeDirection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/EyeDirection)
