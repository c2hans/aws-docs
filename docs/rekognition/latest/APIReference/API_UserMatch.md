---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UserMatch.html
---

# UserMatch
<a name="API_UserMatch"></a>

Provides UserID metadata along with the confidence in the match of this UserID with the input face.

## Contents
<a name="API_UserMatch_Contents"></a>

 ** Similarity **   <a name="rekognition-Type-UserMatch-Similarity"></a>
 Describes the UserID metadata.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** User **   <a name="rekognition-Type-UserMatch-User"></a>
 Confidence in the match of this UserID with the input face.
Type: [MatchedUser](API_MatchedUser.md) object
Required: No

## See Also
<a name="API_UserMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UserMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UserMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UserMatch)
