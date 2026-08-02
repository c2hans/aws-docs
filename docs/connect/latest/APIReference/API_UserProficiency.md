---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserProficiency.html
---

# UserProficiency
<a name="API_UserProficiency"></a>

Information about proficiency of a user.

## Contents
<a name="API_UserProficiency_Contents"></a>

 ** AttributeName **   <a name="connect-Type-UserProficiency-AttributeName"></a>
The name of user's proficiency. You must use name of predefined attribute present in the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** AttributeValue **   <a name="connect-Type-UserProficiency-AttributeValue"></a>
The value of user's proficiency. You must use value of predefined attribute present in the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Level **   <a name="connect-Type-UserProficiency-Level"></a>
The level of the proficiency. The valid values are 1, 2, 3, 4 and 5.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 5.0.
Required: Yes

## See Also
<a name="API_UserProficiency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserProficiency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserProficiency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserProficiency)
