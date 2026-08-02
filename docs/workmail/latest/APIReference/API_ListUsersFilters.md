---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListUsersFilters.html
---

# ListUsersFilters
<a name="API_ListUsersFilters"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Filtering options for *ListUsers* operation. This is only used as input to Operation.

## Contents
<a name="API_ListUsersFilters_Contents"></a>

 ** DisplayNamePrefix **   <a name="workmail-Type-ListUsersFilters-DisplayNamePrefix"></a>
Filters only users with the provided display name prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** IdentityProviderUserIdPrefix **   <a name="workmail-Type-ListUsersFilters-IdentityProviderUserIdPrefix"></a>
Filters only users with the ID from the IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^[A-Fa-f0-9-]+$`
Required: No

 ** PrimaryEmailPrefix **   <a name="workmail-Type-ListUsersFilters-PrimaryEmailPrefix"></a>
Filters only users with the provided email prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** State **   <a name="workmail-Type-ListUsersFilters-State"></a>
Filters only users with the provided state.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

 ** UsernamePrefix **   <a name="workmail-Type-ListUsersFilters-UsernamePrefix"></a>
Filters only users with the provided username prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ListUsersFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListUsersFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListUsersFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListUsersFilters)
