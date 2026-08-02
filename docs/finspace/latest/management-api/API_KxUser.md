---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxUser.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxUser
<a name="API_KxUser"></a>

A structure that stores metadata for a kdb user.

## Contents
<a name="API_KxUser_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createTimestamp **   <a name="finspace-Type-KxUser-createTimestamp"></a>
The timestamp at which the kdb user was created.
Type: Timestamp
Required: No

 ** iamRole **   <a name="finspace-Type-KxUser-iamRole"></a>
The IAM role ARN that is associated with the user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** updateTimestamp **   <a name="finspace-Type-KxUser-updateTimestamp"></a>
The timestamp at which the kdb user was updated.
Type: Timestamp
Required: No

 ** userArn **   <a name="finspace-Type-KxUser-userArn"></a>
 The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}/kxUser/[0-9A-Za-z_-]{1,128}$`
Required: No

 ** userName **   <a name="finspace-Type-KxUser-userName"></a>
A unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[0-9A-Za-z_-]{1,50}$`
Required: No

## See Also
<a name="API_KxUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxUser)
