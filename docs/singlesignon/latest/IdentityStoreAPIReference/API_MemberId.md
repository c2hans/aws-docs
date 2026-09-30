---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_MemberId.html
---

# MemberId
<a name="API_MemberId"></a>

An object containing the identifier of a group member.

## Contents
<a name="API_MemberId_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** UserId **   <a name="singlesignon-Type-MemberId-UserId"></a>
The identifier for a user in the identity store.
You can specify the user by ID or by Amazon Resource Name (ARN). For example, user ID `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` or user ARN `arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

## See Also
<a name="API_MemberId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/MemberId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/MemberId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/MemberId)
