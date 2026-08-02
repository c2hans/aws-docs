---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateUserDetails.html
---

# UpdateUserDetails
<a name="API_UpdateUserDetails"></a>

Contains the modifiable details for updating an existing user, including name, password, security group membership, and invitation settings.

**Note**
A user can only be assigned to a single security group. Attempting to add a user to multiple security groups is not supported and will result in an error.

## Contents
<a name="API_UpdateUserDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** codeValidation **   <a name="wickr-Type-UpdateUserDetails-codeValidation"></a>
Indicates whether the user can be verified through a custom invite code.
Type: Boolean
Required: No

 ** firstName **   <a name="wickr-Type-UpdateUserDetails-firstName"></a>
The new first name for the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** inviteCode **   <a name="wickr-Type-UpdateUserDetails-inviteCode"></a>
A new custom invite code for the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** inviteCodeTtl **   <a name="wickr-Type-UpdateUserDetails-inviteCodeTtl"></a>
The new time-to-live for the invite code in days.
Type: Integer
Required: No

 ** lastName **   <a name="wickr-Type-UpdateUserDetails-lastName"></a>
The new last name for the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** securityGroupIds **   <a name="wickr-Type-UpdateUserDetails-securityGroupIds"></a>
The updated list of security group IDs to which the user should belong.
Type: Array of strings
Pattern: `[\S]+`
Required: No

 ** username **   <a name="wickr-Type-UpdateUserDetails-username"></a>
The new username or email address for the user.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_UpdateUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/UpdateUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/UpdateUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/UpdateUserDetails)
