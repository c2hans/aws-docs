---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_MatchedUser.html
---

# MatchedUser
<a name="API_MatchedUser"></a>

Contains metadata for a UserID matched with a given face.

## Contents
<a name="API_MatchedUser_Contents"></a>

 ** UserId **   <a name="rekognition-Type-MatchedUser-UserId"></a>
A provided ID for the UserID. Unique within the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

 ** UserStatus **   <a name="rekognition-Type-MatchedUser-UserStatus"></a>
The status of the user matched to a provided FaceID.
Type: String
Valid Values: `ACTIVE | UPDATING | CREATING | CREATED`
Required: No

## See Also
<a name="API_MatchedUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/MatchedUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/MatchedUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/MatchedUser)
