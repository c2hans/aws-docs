---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchCreateUserRequestItem.html
---

# BatchCreateUserRequestItem
<a name="API_BatchCreateUserRequestItem"></a>

Contains the details for a single user to be created in a batch user creation request.

**Note**
A user can only be assigned to a single security group. Attempting to add a user to multiple security groups is not supported and will result in an error.

**Note**
 `codeValidation`, `inviteCode`, and `inviteCodeTtl` are restricted to networks under preview only.

## Contents
<a name="API_BatchCreateUserRequestItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** securityGroupIds **   <a name="wickr-Type-BatchCreateUserRequestItem-securityGroupIds"></a>
A list of security group IDs to which the user should be assigned.
Type: Array of strings
Pattern: `[\S]+`
Required: Yes

 ** username **   <a name="wickr-Type-BatchCreateUserRequestItem-username"></a>
The email address or username for the user. Must be unique within the network.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** codeValidation **   <a name="wickr-Type-BatchCreateUserRequestItem-codeValidation"></a>
Indicates whether the user can be verified through a custom invite code.
Type: Boolean
Required: No

 ** firstName **   <a name="wickr-Type-BatchCreateUserRequestItem-firstName"></a>
The first name of the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** inviteCode **   <a name="wickr-Type-BatchCreateUserRequestItem-inviteCode"></a>
A custom invite code for the user. If not provided, one will be generated automatically.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** inviteCodeTtl **   <a name="wickr-Type-BatchCreateUserRequestItem-inviteCodeTtl"></a>
The time-to-live for the invite code in days. After this period, the invite code will expire.
Type: Integer
Required: No

 ** lastName **   <a name="wickr-Type-BatchCreateUserRequestItem-lastName"></a>
The last name of the user.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_BatchCreateUserRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchCreateUserRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchCreateUserRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchCreateUserRequestItem)
