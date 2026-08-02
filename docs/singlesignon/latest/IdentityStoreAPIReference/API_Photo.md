---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Photo.html
---

# Photo
<a name="API_Photo"></a>

Contains information about a user's photo. Users can have up to 3 photos, with one designated as primary. Supports common image formats, including jpg, jpeg, png, and gif.

## Contents
<a name="API_Photo_Contents"></a>

 ** Value **   <a name="singlesignon-Type-Photo-Value"></a>
The photo data or URL. Supported formats include jpg, jpeg, png, and gif. This field is required for all photo entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: Yes

 ** Display **   <a name="singlesignon-Type-Photo-Display"></a>
A human-readable description of the photo for display purposes. This optional field provides context about the photo.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Primary **   <a name="singlesignon-Type-Photo-Primary"></a>
Specifies whether this is the user's primary photo. Default value is `false`. Only one photo can be designated as primary per user.
Type: Boolean
Required: No

 ** Type **   <a name="singlesignon-Type-Photo-Type"></a>
The type of photo. This field is optional and can be used to categorize different types of photos.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## See Also
<a name="API_Photo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/Photo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/Photo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/Photo)
