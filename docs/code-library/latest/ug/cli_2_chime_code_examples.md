---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_chime_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Chime examples using AWS CLI
<a name="cli_2_chime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Chime.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `associate-phone-number-with-user`
<a name="chime_AssociatePhoneNumberWithUser_cli_2_topic"></a>

The following code example shows how to use `associate-phone-number-with-user`.

**AWS CLI**
**To associate a phone number with a user**
The following `associate-phone-number-with-user` example associates the specified phone number with a user.

```
aws chime associate-phone-number-with-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --e164-phone-number {{"+12065550100"}}
```
This command produces no output.
For more information, see [Assigning Amazon Chime Business Calling phone numbers](https://docs.aws.amazon.com/chime/latest/ag/assign-cbc-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [AssociatePhoneNumberWithUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-phone-number-with-user.html) in *AWS CLI Command Reference*.

### `associate-signin-delegate-groups-with-account`
<a name="chime_AssociateSigninDelegateGroupsWithAccount_cli_2_topic"></a>

The following code example shows how to use `associate-signin-delegate-groups-with-account`.

**AWS CLI**
**To associate sign-in delegate groups**
The following `associate-signin-delegate-groups-with-account` example associates the specified sign-in delegate group with the specified Amazon Chime account.

```
aws chime associate-signin-delegate-groups-with-account \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --signin-delegate-groups {{GroupName=my_users}}
```
This command produces no output.
For more information, see [Managing User Access and Permissions](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [AssociateSigninDelegateGroupsWithAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-signin-delegate-groups-with-account.html) in *AWS CLI Command Reference*.

### `batch-create-room-membership`
<a name="chime_BatchCreateRoomMembership_cli_2_topic"></a>

The following code example shows how to use `batch-create-room-membership`.

**AWS CLI**
**To create multiple room memberships**
The following `batch-create-room-membership` example adds multiple users to a chat room as chat room members. It also assigns administrator and member roles to the users.

```
aws chime batch-create-room-membership \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --membership-item-list {{"MemberId=a1b2c3d4-5678-90ab-cdef-EXAMPLE33333,Role=Administrator"}} {{"MemberId=a1b2c3d4-5678-90ab-cdef-EXAMPLE44444,Role=Member"}}
```
Output:

```
{
    "Errors": []
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [BatchCreateRoomMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-create-room-membership.html) in *AWS CLI Command Reference*.

### `batch-delete-phone-number`
<a name="chime_BatchDeletePhoneNumber_cli_2_topic"></a>

The following code example shows how to use `batch-delete-phone-number`.

**AWS CLI**
**To delete multiple phone numbers**
The following `batch-delete-phone-number` example deletes all of the specified phone numbers.

```
aws chime batch-delete-phone-number \
    --phone-number-ids {{"%2B12065550100"}} {{"%2B12065550101"}}
```
This command produces no output. Output:

```
{
    "PhoneNumberErrors": []
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [BatchDeletePhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-delete-phone-number.html) in *AWS CLI Command Reference*.

### `batch-suspend-user`
<a name="chime_BatchSuspendUser_cli_2_topic"></a>

The following code example shows how to use `batch-suspend-user`.

**AWS CLI**
**To suspend multiple users**
The following `batch-suspend-user` example suspends the listed users from the specified Amazon Chime account.

```
aws chime batch-suspend-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id-list {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}} {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"}} {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"}}
```
Output:

```
{
    "UserErrors": []
}
```
For more information, see [Managing user permissions and access](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [BatchSuspendUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-suspend-user.html) in *AWS CLI Command Reference*.

### `batch-unsuspend-user`
<a name="chime_BatchUnsuspendUser_cli_2_topic"></a>

The following code example shows how to use `batch-unsuspend-user`.

**AWS CLI**
**To unsuspend multiple users**
The following `batch-unsuspend-user` example removes any previous suspension for the listed users on the specified Amazon Chime account.

```
aws chime batch-unsuspend-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id-list {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}} {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"}} {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"}}
```
Output:

```
{
    "UserErrors": []
}
```
For more information, see [Managing user permissions and access](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [BatchUnsuspendUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-unsuspend-user.html) in *AWS CLI Command Reference*.

### `batch-update-phone-number`
<a name="chime_BatchUpdatePhoneNumber_cli_2_topic"></a>

The following code example shows how to use `batch-update-phone-number`.

**AWS CLI**
**Example 1: To update several phone number product types at the same time**
The following `batch-update-phone-number` example updates the product types for all of the specified phone numbers.

```
aws chime batch-update-phone-number \
    --update-phone-number-request-items {{PhoneNumberId=%2B12065550100,ProductType=BusinessCalling}} {{PhoneNumberId=%2B12065550101,ProductType=BusinessCalling}}
```
Output:

```
{
    "PhoneNumberErrors": []
}
```
**Example 2: To update several phone number calling names at the same time**
The following `batch-update-phone-number` example updates the calling names for all of the specified phone numbers.

```
aws chime batch-update-phone-number \
    --update-phone-number-request-items {{PhoneNumberId=%2B14013143874,CallingName=phonenumber1}} {{PhoneNumberId=%2B14013144061,CallingName=phonenumber2}}
```
Output:

```
{
    "PhoneNumberErrors": []
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [BatchUpdatePhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-phone-number.html) in *AWS CLI Command Reference*.

### `batch-update-user`
<a name="chime_BatchUpdateUser_cli_2_topic"></a>

The following code example shows how to use `batch-update-user`.

**AWS CLI**
**To update multiple users in a single command**
The following `batch-update-user` example updates the `LicenseType` for each of the listed users in the specified Amazon Chime account.

```
aws chime batch-update-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --update-user-request-items {{"UserId=a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,LicenseType=Basic"}} {{"UserId=a1b2c3d4-5678-90ab-cdef-EXAMPLE33333,LicenseType=Basic"}}
```
Output:

```
{
    "UserErrors": []
}
```
For more information, see [Managing user permissions and access](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [BatchUpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-user.html) in *AWS CLI Command Reference*.

### `create-account`
<a name="chime_CreateAccount_cli_2_topic"></a>

The following code example shows how to use `create-account`.

**AWS CLI**
**To create an account**
The following `create-account` example creates an Amazon Chime account under the administrator's AWS account.

```
aws chime create-account \
    --name {{MyChimeAccount}}
```
Output:

```
{
    "Account": {
        "AwsAccountId": "123456789012",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Name": "MyChimeAccount",
        "AccountType": "Team",
        "CreatedTimestamp": "2019-01-04T17:11:22.003Z",
        "DefaultLicense": "Pro",
        "SupportedLicenses": [
            "Basic",
            "Pro"
        ],
        "SigninDelegateGroups": [
            {
                "GroupName": "myGroup"
            }
        ]
    }
}
```
For more information, see [Getting started](https://docs.aws.amazon.com/chime/latest/ag/getting-started.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [CreateAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-account.html) in *AWS CLI Command Reference*.

### `create-bot`
<a name="chime_CreateBot_cli_2_topic"></a>

The following code example shows how to use `create-bot`.

**AWS CLI**
**To create an Amazon Chime bot**
The following `create-bot` example creates a bot for the specified Amazon Chime Enterprise account.

```
aws chime create-bot \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --display-name {{"myBot"}} \
    --domain {{"example.com"}}
```
Output:

```
{
    "Bot": {
        "BotId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "DisplayName": "myBot (Bot)",
        "BotType": "ChatBot",
        "Disabled": false,
        "CreatedTimestamp": "2019-09-09T18:05:56.749Z",
        "UpdatedTimestamp": "2019-09-09T18:05:56.749Z",
        "BotEmail": "myBot-chimebot@example.com",
        "SecurityToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    }
}
```
For more information, see [Step 1: Integrate a chatbot with Amazon Chime](https://docs.aws.amazon.com/chime/latest/ag/integrate-bots.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [CreateBot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-bot.html) in *AWS CLI Command Reference*.

### `create-phone-number-order`
<a name="chime_CreatePhoneNumberOrder_cli_2_topic"></a>

The following code example shows how to use `create-phone-number-order`.

**AWS CLI**
**To create a phone number order**
The following `create-phone-number-order` example creates a phone number order for the specified phone numbers.

```
aws chime create-phone-number-order \
    --product-type {{VoiceConnector}} \
    --e164-phone-numbers {{"+12065550100"}} {{"+12065550101"}} {{"+12065550102"}}
```
Output:

```
{
    "PhoneNumberOrder": {
        "PhoneNumberOrderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "ProductType": "VoiceConnector",
        "Status": "Processing",
        "OrderedPhoneNumbers": [
            {
                "E164PhoneNumber": "+12065550100",
                "Status": "Processing"
            },
            {
                "E164PhoneNumber": "+12065550101",
                "Status": "Processing"
            },
            {
                "E164PhoneNumber": "+12065550102",
                "Status": "Processing"
            }
        ],
        "CreatedTimestamp": "2019-08-09T21:35:21.427Z",
        "UpdatedTimestamp": "2019-08-09T21:35:22.408Z"
    }
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [CreatePhoneNumberOrder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-phone-number-order.html) in *AWS CLI Command Reference*.

### `create-room-membership`
<a name="chime_CreateRoomMembership_cli_2_topic"></a>

The following code example shows how to use `create-room-membership`.

**AWS CLI**
**To create a room membership**
The following `create-room-membership` example adds the specified user to the chat room as a chat room member.

```
aws chime create-room-membership \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --member-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "RoomMembership": {
        "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Member": {
            "MemberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MemberType": "User",
            "Email": "janed@example.com",
            "FullName": "Jane Doe",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        "Role": "Member",
        "InvitedBy": "arn:aws:iam::123456789012:user/alejandro",
        "UpdatedTimestamp": "2019-12-02T22:36:41.969Z"
    }
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [CreateRoomMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room-membership.html) in *AWS CLI Command Reference*.

### `create-room`
<a name="chime_CreateRoom_cli_2_topic"></a>

The following code example shows how to use `create-room`.

**AWS CLI**
**To create a chat room**
The following `create-room` example creates a chat room for the specified Amazon Chime account.

```
aws chime create-room \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --name {{chatRoom}}
```
Output:

```
{
    "Room": {
        "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Name": "chatRoom",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreatedBy": "arn:aws:iam::123456789012:user/alejandro",
        "CreatedTimestamp": "2019-12-02T22:29:31.549Z",
        "UpdatedTimestamp": "2019-12-02T22:29:31.549Z"
    }
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [CreateRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room.html) in *AWS CLI Command Reference*.

### `create-user`
<a name="chime_CreateUser_cli_2_topic"></a>

The following code example shows how to use `create-user`.

**AWS CLI**
**To create a user profile for a shared device**
The following `create-user` example creates a shared device profile for the specified email address.

```
aws chime create-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --email {{roomdevice@example.com}} \
    --user-type {{SharedDevice}}
```
Output:

```
{
    "User": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PrimaryEmail": "roomdevice@example.com",
        "DisplayName": "Room Device",
        "LicenseType": "Pro",
        "UserType": "SharedDevice",
        "UserRegistrationStatus": "Registered",
        "RegisteredOn": "2020-01-15T22:38:09.806Z",
        "AlexaForBusinessMetadata": {
            "IsAlexaForBusinessEnabled": false
        }
    }
}
```
For more information, see [Adding users](https://docs.aws.amazon.com/chime/latest/ag/adding-users.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html) in *AWS CLI Command Reference*.

### `delete-account`
<a name="chime_DeleteAccount_cli_2_topic"></a>

The following code example shows how to use `delete-account`.

**AWS CLI**
**To delete an account**
The following `delete-account` example deletes the specified account.

```
aws chime delete-account \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
This command produces no output.
For more information, see [Deleting your account](https://docs.aws.amazon.com/chime/latest/ag/enterprise-account.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [DeleteAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-account.html) in *AWS CLI Command Reference*.

### `delete-phone-number`
<a name="chime_DeletePhoneNumber_cli_2_topic"></a>

The following code example shows how to use `delete-phone-number`.

**AWS CLI**
**To delete a phone number**
The following `delete-phone-number` example moves the specified phone number into the deletion queue.

```
aws chime delete-phone-number \
    --phone-number-id {{"+12065550100"}}
```
This command produces no output.
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [DeletePhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-phone-number.html) in *AWS CLI Command Reference*.

### `delete-room-membership`
<a name="chime_DeleteRoomMembership_cli_2_topic"></a>

The following code example shows how to use `delete-room-membership`.

**AWS CLI**
**To remove a user as a member of a chat room**
The following `delete-room-membership` example removes the specified member from the specified chat room.

```
aws chime delete-room-membership \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --member-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
This command produces no output.
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [DeleteRoomMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room-membership.html) in *AWS CLI Command Reference*.

### `delete-room`
<a name="chime_DeleteRoom_cli_2_topic"></a>

The following code example shows how to use `delete-room`.

**AWS CLI**
**To delete a chat room**
The following `delete-room` example deletes the specified chat room and removes the chat room memberships.

```
aws chime delete-room \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
This command produces no output.
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [DeleteRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room.html) in *AWS CLI Command Reference*.

### `disassociate-phone-number-from-user`
<a name="chime_DisassociatePhoneNumberFromUser_cli_2_topic"></a>

The following code example shows how to use `disassociate-phone-number-from-user`.

**AWS CLI**
**To disassociate a phone number from a user**
The following `disassociate-phone-number-from-user` example disassociates a phone number from the specified user.

```
aws chime disassociate-phone-number-from-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
This command produces no output.
For more information, see [Unassigning Amazon Chime Business Calling phone numbers](https://docs.aws.amazon.com/chime/latest/ag/unassign-cbc-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [DisassociatePhoneNumberFromUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/disassociate-phone-number-from-user.html) in *AWS CLI Command Reference*.

### `disassociate-signin-delegate-groups-from-account`
<a name="chime_DisassociateSigninDelegateGroupsFromAccount_cli_2_topic"></a>

The following code example shows how to use `disassociate-signin-delegate-groups-from-account`.

**AWS CLI**
**To disassociate sign-in delegate groups**
The following `disassociate-signin-delegate-groups-from-account` example disassociates the specified sign-in delegate group from the specified Amazon Chime account.

```
aws chime disassociate-signin-delegate-groups-from-account \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --group-names {{"my_users"}}
```
This command produces no output.
For more information, see [Managing User Access and Permissions](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [DisassociateSigninDelegateGroupsFromAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/disassociate-signin-delegate-groups-from-account.html) in *AWS CLI Command Reference*.

### `get-account-settings`
<a name="chime_GetAccountSettings_cli_2_topic"></a>

The following code example shows how to use `get-account-settings`.

**AWS CLI**
**To retrieve settings for an account**
The following `get-account-settings` example retrieves the account settings for the specified account.

```
aws chime get-account-settings \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "AccountSettings": {
        "DisableRemoteControl": false,
        "EnableDialOut": false
    }
}
```
For more information, see [Managing your Amazon Chime accounts](https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetAccountSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account-settings.html) in *AWS CLI Command Reference*.

### `get-account`
<a name="chime_GetAccount_cli_2_topic"></a>

The following code example shows how to use `get-account`.

**AWS CLI**
**To retrieve the details for an account**
The following `get-account` example retrieves the details for the specified Amazon Chime account.

```
aws chime get-account \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "Account": {
        "AwsAccountId": "123456789012",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Name": "EnterpriseDirectory",
        "AccountType": "EnterpriseDirectory",
        "CreatedTimestamp": "2018-12-20T18:38:02.181Z",
        "DefaultLicense": "Pro",
        "SupportedLicenses": [
            "Basic",
            "Pro"
        ],
        "SigninDelegateGroups": [
            {
                "GroupName": "myGroup"
            }
        ]
    }
}
```
For more information, see [Managing your Amazon Chime accounts](https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account.html) in *AWS CLI Command Reference*.

### `get-bot`
<a name="chime_GetBot_cli_2_topic"></a>

The following code example shows how to use `get-bot`.

**AWS CLI**
**To retrieve details about a bot**
The following `get-bot` example displays the details for the specified bot.

```
aws chime get-bot \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --bot-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "Bot": {
        "BotId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "DisplayName": "myBot (Bot)",
        "BotType": "ChatBot",
        "Disabled": false,
        "CreatedTimestamp": "2019-09-09T18:05:56.749Z",
        "UpdatedTimestamp": "2019-09-09T18:05:56.749Z",
        "BotEmail": "myBot-chimebot@example.com",
        "SecurityToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    }
}
```
For more information, see [Update chatbots](https://docs.aws.amazon.com/chime/latest/ag/update-bots.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetBot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-bot.html) in *AWS CLI Command Reference*.

### `get-global-settings`
<a name="chime_GetGlobalSettings_cli_2_topic"></a>

The following code example shows how to use `get-global-settings`.

**AWS CLI**
**To get global settings**
The following `get-global-settings` example retrieves the S3 bucket names used to store call detail records for Amazon Chime Business Calling and Amazon Chime Voice Connectors associated with the administrator's AWS account.

```
aws chime get-global-settings
```
Output:

```
{
    "BusinessCalling": {
        "CdrBucket": "s3bucket"
    },
    "VoiceConnector": {
        "CdrBucket": "s3bucket"
    }
}
```
For more information, see [Managing Global Settings](https://docs.aws.amazon.com/chime/latest/ag/manage-global.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetGlobalSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-global-settings.html) in *AWS CLI Command Reference*.

### `get-phone-number-order`
<a name="chime_GetPhoneNumberOrder_cli_2_topic"></a>

The following code example shows how to use `get-phone-number-order`.

**AWS CLI**
**To get details for a phone number order**
The following `get-phone-number-order` example displays the details of the specified phone number order.

```
aws chime get-phone-number-order \
    --phone-number-order-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "PhoneNumberOrder": {
        "PhoneNumberOrderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "ProductType": "VoiceConnector",
        "Status": "Partial",
        "OrderedPhoneNumbers": [
            {
                "E164PhoneNumber": "+12065550100",
                "Status": "Acquired"
            },
            {
                "E164PhoneNumber": "+12065550101",
                "Status": "Acquired"
            },
            {
                "E164PhoneNumber": "+12065550102",
                "Status": "Failed"
            }
        ],
        "CreatedTimestamp": "2019-08-09T21:35:21.427Z",
        "UpdatedTimestamp": "2019-08-09T21:35:31.926Z"
    }
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetPhoneNumberOrder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number-order.html) in *AWS CLI Command Reference*.

### `get-phone-number-settings`
<a name="chime_GetPhoneNumberSettings_cli_2_topic"></a>

The following code example shows how to use `get-phone-number-settings`.

**AWS CLI**
**To retrieve an outbound calling name**
The following `get-phone-number-settings` example retrieves the default outbound calling name for the calling user's AWS account.

```
aws chime get-phone-number-settings
```
This command produces no output. Output:

```
{
    "CallingName": "myName",
    "CallingNameUpdatedTimestamp": "2019-10-28T18:56:42.911Z"
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetPhoneNumberSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number-settings.html) in *AWS CLI Command Reference*.

### `get-phone-number`
<a name="chime_GetPhoneNumber_cli_2_topic"></a>

The following code example shows how to use `get-phone-number`.

**AWS CLI**
**To get phone number details**
The following `get-phone-number` example displays the details of the specified phone number.

```
aws chime get-phone-number \
    --phone-number-id {{+12065550100}}
```
Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "VoiceConnector",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [
            {
                "Value": "abcdef1ghij2klmno3pqr4",
                "Name": "VoiceConnectorId",
                "AssociatedTimestamp": "2019-10-28T18:40:37.453Z"
            }
        ],
        "CallingNameStatus": "UpdateInProgress",
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-09T21:35:31.745Z"
    }
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetPhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number.html) in *AWS CLI Command Reference*.

### `get-room`
<a name="chime_GetRoom_cli_2_topic"></a>

The following code example shows how to use `get-room`.

**AWS CLI**
**To get the details about a chat room**
The following `get-room` example displays details about the specified chat room.

```
aws chime get-room \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "Room": {
        "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Name": "chatRoom",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreatedBy": "arn:aws:iam::123456789012:user/alejandro",
        "CreatedTimestamp": "2019-12-02T22:29:31.549Z",
        "UpdatedTimestamp": "2019-12-02T22:29:31.549Z"
    }
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [GetRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-room.html) in *AWS CLI Command Reference*.

### `get-user-settings`
<a name="chime_GetUserSettings_cli_2_topic"></a>

The following code example shows how to use `get-user-settings`.

**AWS CLI**
**To retrieve user settings**
The following `get-user-settings` example displays the specified user settings.

```
aws chime get-user-settings \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "UserSettings": {
        "Telephony": {
            "InboundCalling": true,
            "OutboundCalling": true,
            "SMS": true
        }
    }
}
```
For more information, see [Managing phone numbers in Amazon Chime](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetUserSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user-settings.html) in *AWS CLI Command Reference*.

### `get-user`
<a name="chime_GetUser_cli_2_topic"></a>

The following code example shows how to use `get-user`.

**AWS CLI**
**To get details about a user**
The following `get-user` example retrieves the details for the specified user.

```
aws chime get-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "User": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PrimaryEmail": "marthar@example.com",
        "DisplayName": "Martha Rivera",
        "LicenseType": "Pro",
        "UserRegistrationStatus": "Registered",
        "RegisteredOn": "2018-12-20T18:45:25.231Z",
        "InvitedOn": "2018-12-20T18:45:25.231Z",
        "AlexaForBusinessMetadata": {
            "IsAlexaForBusinessEnabled": false,
            "AlexaForBusinessRoomArn": "null"
        },
        "PersonalPIN": "XXXXXXXXXX"
    }
}
```
For more information, see [Managing users](https://docs.aws.amazon.com/chime/latest/ag/manage-users.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [GetUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html) in *AWS CLI Command Reference*.

### `invite-users`
<a name="chime_InviteUsers_cli_2_topic"></a>

The following code example shows how to use `invite-users`.

**AWS CLI**
**To invite users to join Amazon Chime**
The following `invite-users` example sends an email to invite a user to the specified Amazon Chime account.

```
aws chime invite-users \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-email-list {{"alejandror@example.com"}} {{"janed@example.com"}}
```
Output:

```
{
    "Invites": [
        {
            "InviteId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Status": "Pending",
            "EmailAddress": "alejandror@example.com",
            "EmailStatus": "Sent"
        },
        {
            "InviteId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "Status": "Pending",
            "EmailAddress": "janed@example.com",
            "EmailStatus": "Sent"
        }
    ]
}
```
For more information, see [Managing user permissions and access](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [InviteUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html) in *AWS CLI Command Reference*.

### `list-accounts`
<a name="chime_ListAccounts_cli_2_topic"></a>

The following code example shows how to use `list-accounts`.

**AWS CLI**
**To get a list of accounts**
The following `list-accounts` example retrieves a list of the Amazon Chime accounts in the administrator's AWS account.

```
aws chime list-accounts
```
Output:

```
{
    "Accounts": [
        {
            "AwsAccountId": "123456789012",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Name": "First Chime Account",
            "AccountType": "EnterpriseDirectory",
            "CreatedTimestamp": "2018-12-20T18:38:02.181Z",
            "DefaultLicense": "Pro",
            "SupportedLicenses": [
                "Basic",
                "Pro"
            ],
            "SigninDelegateGroups": [
                {
                    "GroupName": "myGroup"
                }
            ]
        },
        {
            "AwsAccountId": "123456789012",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Name": "Second Chime Account",
            "AccountType": "Team",
            "CreatedTimestamp": "2018-09-04T21:44:22.292Z",
            "DefaultLicense": "Pro",
            "SupportedLicenses": [
                "Basic",
                "Pro"
            ],
            "SigninDelegateGroups": [
                {
                    "GroupName": "myGroup"
                }
            ]
        }
    ]
}
```
For more information, see [Managing your Amazon Chime accounts](https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [ListAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-accounts.html) in *AWS CLI Command Reference*.

### `list-bots`
<a name="chime_ListBots_cli_2_topic"></a>

The following code example shows how to use `list-bots`.

**AWS CLI**
**To retrieve a list of bots**
The following `list-bots` example lists the bots associated with the specified Amazon Chime Enterprise account.

```
aws chime list-bots \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "Bots": [
        {
            "BotId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "DisplayName": "myBot (Bot)",
            "BotType": "ChatBot",
            "Disabled": false,
            "CreatedTimestamp": "2019-09-09T18:05:56.749Z",
            "UpdatedTimestamp": "2019-09-09T18:05:56.749Z",
            "BotEmail": "myBot-chimebot@example.com",
            "SecurityToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        }
    ]
}
```
For more information, see [Use Chat Bots with Amazon Chime](https://docs.aws.amazon.com/chime/latest/dg/use-bots.html) in the *Amazon Chime Developer Guide*.
+  For API details, see [ListBots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-bots.html) in *AWS CLI Command Reference*.

### `list-phone-number-orders`
<a name="chime_ListPhoneNumberOrders_cli_2_topic"></a>

The following code example shows how to use `list-phone-number-orders`.

**AWS CLI**
**To list phone number orders**
The following `list-phone-number-orders` example lists the phone number orders associated with the Amazon Chime administrator's account.

```
aws chime list-phone-number-orders
```
Output:

```
{
    "PhoneNumberOrders": [
        {
            "PhoneNumberOrderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "ProductType": "VoiceConnector",
            "Status": "Partial",
            "OrderedPhoneNumbers": [
                {
                    "E164PhoneNumber": "+12065550100",
                    "Status": "Acquired"
                },
                {
                    "E164PhoneNumber": "+12065550101",
                    "Status": "Acquired"
                },
                {
                    "E164PhoneNumber": "+12065550102",
                    "Status": "Failed"
                }
            ],
            "CreatedTimestamp": "2019-08-09T21:35:21.427Z",
            "UpdatedTimestamp": "2019-08-09T21:35:31.926Z"
        },
        {
            "PhoneNumberOrderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "ProductType": "BusinessCalling",
            "Status": "Partial",
            "OrderedPhoneNumbers": [
                {
                    "E164PhoneNumber": "+12065550103",
                    "Status": "Acquired"
                },
                {
                    "E164PhoneNumber": "+12065550104",
                    "Status": "Acquired"
                },
                {
                    "E164PhoneNumber": "+12065550105",
                    "Status": "Failed"
                }
            ],
            "CreatedTimestamp": "2019-08-09T21:35:21.427Z",
            "UpdatedTimestamp": "2019-08-09T21:35:31.926Z"
        }
    ]
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [ListPhoneNumberOrders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-number-orders.html) in *AWS CLI Command Reference*.

### `list-phone-numbers`
<a name="chime_ListPhoneNumbers_cli_2_topic"></a>

The following code example shows how to use `list-phone-numbers`.

**AWS CLI**
**To list phone numbers for an Amazon Chime account**
The following `list-phone-numbers` example lists the phone numbers associated with the administrator's Amazon Chime account.

```
aws chime list-phone-numbers
```
This command produces no output. Output:

```
{
    "PhoneNumbers": [
        {
            "PhoneNumberId": "%2B12065550100",
            "E164PhoneNumber": "+12065550100",
            "Type": "Local",
            "ProductType": "VoiceConnector",
            "Status": "Assigned",
            "Capabilities": {
                "InboundCall": true,
                "OutboundCall": true,
                "InboundSMS": true,
                "OutboundSMS": true,
                "InboundMMS": true,
                "OutboundMMS": true
            },
            "Associations": [
                {
                    "Value": "abcdef1ghij2klmno3pqr4",
                    "Name": "VoiceConnectorId",
                    "AssociatedTimestamp": "2019-10-28T18:40:37.453Z"
                }
            ],
            "CallingNameStatus": "UpdateInProgress",
            "CreatedTimestamp": "2019-08-12T22:10:20.521Z",
            "UpdatedTimestamp": "2019-10-28T18:42:07.964Z"
        },
        {
            "PhoneNumberId": "%2B12065550101",
            "E164PhoneNumber": "+12065550101",
            "Type": "Local",
            "ProductType": "VoiceConnector",
            "Status": "Assigned",
            "Capabilities": {
                "InboundCall": true,
                "OutboundCall": true,
                "InboundSMS": true,
                "OutboundSMS": true,
                "InboundMMS": true,
                "OutboundMMS": true
            },
            "Associations": [
                {
                    "Value": "abcdef1ghij2klmno3pqr4",
                    "Name": "VoiceConnectorId",
                    "AssociatedTimestamp": "2019-10-28T18:40:37.511Z"
                }
            ],
            "CallingNameStatus": "UpdateInProgress",
            "CreatedTimestamp": "2019-08-12T22:10:20.521Z",
            "UpdatedTimestamp": "2019-10-28T18:42:07.960Z"
        }
    ]
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [ListPhoneNumbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-numbers.html) in *AWS CLI Command Reference*.

### `list-room-memberships`
<a name="chime_ListRoomMemberships_cli_2_topic"></a>

The following code example shows how to use `list-room-memberships`.

**AWS CLI**
**To list room memberships**
The following `list-room-memberships` example displays a list of the membership details for the specified chat room.

```
aws chime list-room-memberships \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "RoomMemberships": [
        {
            "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Member": {
                "MemberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
                "MemberType": "User",
                "Email": "zhangw@example.com",
                "FullName": "Zhang Wei",
                "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            },
            "Role": "Member",
            "InvitedBy": "arn:aws:iam::123456789012:user/alejandro",
            "UpdatedTimestamp": "2019-12-02T22:46:58.532Z"
        },
        {
            "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Member": {
                "MemberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
                "MemberType": "User",
                "Email": "janed@example.com",
                "FullName": "Jane Doe",
                "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            },
            "Role": "Administrator",
            "InvitedBy": "arn:aws:iam::123456789012:user/alejandro",
            "UpdatedTimestamp": "2019-12-02T22:46:58.532Z"
        }
    ]
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [ListRoomMemberships](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-room-memberships.html) in *AWS CLI Command Reference*.

### `list-rooms`
<a name="chime_ListRooms_cli_2_topic"></a>

The following code example shows how to use `list-rooms`.

**AWS CLI**
**To list chat rooms**
The following `list-rooms` example displays a list of chat rooms in the specified account. The list is filtered to only those chat rooms that the specified member belongs to.

```
aws chime list-rooms \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --member-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "Rooms": [
        {
            "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "Name": "teamRoom",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "CreatedBy": "arn:aws:iam::123456789012:user/alejandro",
            "CreatedTimestamp": "2019-12-02T22:29:31.549Z",
            "UpdatedTimestamp": "2019-12-02T22:33:19.310Z"
        }
    ]
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [ListRooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-rooms.html) in *AWS CLI Command Reference*.

### `list-users`
<a name="chime_ListUsers_cli_2_topic"></a>

The following code example shows how to use `list-users`.

**AWS CLI**
**To list the users in an account**
The following `list-users` example lists the users for the specified Amazon Chime account.

```
aws chime list-users \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "Users": [
        {
            "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "PrimaryEmail": "mariag@example.com",
            "DisplayName": "Maria Garcia",
            "LicenseType": "Pro",
            "UserType": "PrivateUser",
            "UserRegistrationStatus": "Registered",
            "RegisteredOn": "2018-12-20T18:45:25.231Z",
            "AlexaForBusinessMetadata": {
                "IsAlexaForBusinessEnabled": false
            }
        },
        {
            "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "PrimaryEmail": "richardr@example.com",
            "DisplayName": "Richard Roe",
            "LicenseType": "Pro",
            "UserType": "PrivateUser",
            "UserRegistrationStatus": "Registered",
            "RegisteredOn": "2018-12-20T18:45:45.415Z",
            "AlexaForBusinessMetadata": {
                "IsAlexaForBusinessEnabled": false
            }
        },
        {
            "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "PrimaryEmail": "saanvis@example.com",
            "DisplayName": "Saanvi Sarkar",
            "LicenseType": "Basic",
            "UserType": "PrivateUser",
            "UserRegistrationStatus": "Registered",
            "RegisteredOn": "2018-12-20T18:46:57.747Z",
            "AlexaForBusinessMetadata": {
                "IsAlexaForBusinessEnabled": false
            }
        },
        {
            "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "PrimaryEmail": "wxiulan@example.com",
            "DisplayName": "Wang Xiulan",
            "LicenseType": "Basic",
            "UserType": "PrivateUser",
            "UserRegistrationStatus": "Registered",
            "RegisteredOn": "2018-12-20T18:47:15.390Z",
            "AlexaForBusinessMetadata": {
                "IsAlexaForBusinessEnabled": false
            }
        }
    ]
}
```
For more information, see [Managing users](https://docs.aws.amazon.com/chime/latest/ag/manage-users.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html) in *AWS CLI Command Reference*.

### `logout-user`
<a name="chime_LogoutUser_cli_2_topic"></a>

The following code example shows how to use `logout-user`.

**AWS CLI**
**To log out a user**
The following `logout-user` example logs out the specified user.

```
aws chime logout-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
This command produces no output.
For more information, see [Managing users](https://docs.aws.amazon.com/chime/latest/ag/manage-users.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [LogoutUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html) in *AWS CLI Command Reference*.

### `regenerate-security-token`
<a name="chime_RegenerateSecurityToken_cli_2_topic"></a>

The following code example shows how to use `regenerate-security-token`.

**AWS CLI**
**To regenerate a security token**
The following `regenerate-security-token` example regenerates the security token for the specified bot.

```
aws chime regenerate-security-token \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --bot-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "Bot": {
        "BotId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "DisplayName": "myBot (Bot)",
        "BotType": "ChatBot",
        "Disabled": false,
        "CreatedTimestamp": "2019-09-09T18:05:56.749Z",
        "UpdatedTimestamp": "2019-09-09T18:05:56.749Z",
        "BotEmail": "myBot-chimebot@example.com",
        "SecurityToken": "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"
    }
}
```
For more information, see [Authenticate chatbot requests](https://docs.aws.amazon.com/chime/latest/ag/auth-bots.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [RegenerateSecurityToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/regenerate-security-token.html) in *AWS CLI Command Reference*.

### `reset-personal-pin`
<a name="chime_ResetPersonalPin_cli_2_topic"></a>

The following code example shows how to use `reset-personal-pin`.

**AWS CLI**
**To reset a user's personal meeting PIN**
The following `reset-personal-pin` example resets the specified user's personal meeting PIN.

```
aws chime reset-personal-pin \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "User": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PrimaryEmail": "mateo@example.com",
        "DisplayName": "Mateo Jackson",
        "LicenseType": "Pro",
        "UserType": "PrivateUser",
        "UserRegistrationStatus": "Registered",
        "RegisteredOn": "2018-12-20T18:45:25.231Z",
        "AlexaForBusinessMetadata": {
            "IsAlexaForBusinessEnabled": false,
            "AlexaForBusinessRoomArn": "null"
        },
        "PersonalPIN": "XXXXXXXXXX"
    }
}
```
For more information, see [Changing personal meeting PINs](https://docs.aws.amazon.com/chime/latest/ag/change-PINs.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [ResetPersonalPin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/reset-personal-pin.html) in *AWS CLI Command Reference*.

### `restore-phone-number`
<a name="chime_RestorePhoneNumber_cli_2_topic"></a>

The following code example shows how to use `restore-phone-number`.

**AWS CLI**
**To restore a phone number**
The following `restore-phone-number` example restores the specified phone number from the deletion queue.

```
aws chime restore-phone-number \
    --phone-number-id {{"+12065550100"}}
```
Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "BusinessCalling",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [],
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-12T22:06:36.355Z"
    }
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [RestorePhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/restore-phone-number.html) in *AWS CLI Command Reference*.

### `search-available-phone-numbers`
<a name="chime_SearchAvailablePhoneNumbers_cli_2_topic"></a>

The following code example shows how to use `search-available-phone-numbers`.

**AWS CLI**
**To search available phone numbers**
The following `search-available-phone-numbers` example searches available phone numbers by area code.

```
aws chime search-available-phone-numbers \
    --area-code {{"206"}}
```
Output:

```
{
    "E164PhoneNumbers": [
        "+12065550100",
        "+12065550101",
        "+12065550102",
        "+12065550103",
        "+12065550104",
        "+12065550105",
        "+12065550106",
        "+12065550107",
        "+12065550108",
        "+12065550109"
    ]
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [SearchAvailablePhoneNumbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/search-available-phone-numbers.html) in *AWS CLI Command Reference*.

### `update-account-settings`
<a name="chime_UpdateAccountSettings_cli_2_topic"></a>

The following code example shows how to use `update-account-settings`.

**AWS CLI**
**To update the settings for your account**
The following `update-account-settings` example disables the remote control of shared screens for the specified Amazon Chime account.

```
aws chime update-account-settings \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --account-settings {{DisableRemoteControl=true}}
```
This command produces no output.
For more information, see [Managing meeting settings](https://docs.aws.amazon.com/chime/latest/ag/mtg-settings.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateAccountSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account-settings.html) in *AWS CLI Command Reference*.

### `update-account`
<a name="chime_UpdateAccount_cli_2_topic"></a>

The following code example shows how to use `update-account`.

**AWS CLI**
**To update an account**
The following `update-account` example updates the specified account name.

```
aws chime update-account \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --name {{MyAccountName}}
```
Output:

```
{
    "Account": {
        "AwsAccountId": "123456789012",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Name": "MyAccountName",
        "AccountType": "Team",
        "CreatedTimestamp": "2018-09-04T21:44:22.292Z",
        "DefaultLicense": "Pro",
        "SupportedLicenses": [
            "Basic",
            "Pro"
        ],
        "SigninDelegateGroups": [
            {
                "GroupName": "myGroup"
            }
        ]
    }
}
```
For more information, see [Renaming Your Account](https://docs.aws.amazon.com/chime/latest/ag/rename-account.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account.html) in *AWS CLI Command Reference*.

### `update-bot`
<a name="chime_UpdateBot_cli_2_topic"></a>

The following code example shows how to use `update-bot`.

**AWS CLI**
**To update a bot**
The following `update-bot` example updates the status of the specified bot to stop it from running.

```
aws chime update-bot \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --bot-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --disabled
```
Output:

```
{
    "Bot": {
        "BotId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "DisplayName": "myBot (Bot)",
        "BotType": "ChatBot",
        "Disabled": true,
        "CreatedTimestamp": "2019-09-09T18:05:56.749Z",
        "UpdatedTimestamp": "2019-09-09T18:05:56.749Z",
        "BotEmail": "myBot-chimebot@example.com",
        "SecurityToken": "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"
    }
}
```
For more information, see [Update chatbots](https://docs.aws.amazon.com/chime/latest/ag/update-bots.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateBot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-bot.html) in *AWS CLI Command Reference*.

### `update-global-settings`
<a name="chime_UpdateGlobalSettings_cli_2_topic"></a>

The following code example shows how to use `update-global-settings`.

**AWS CLI**
**To update global settings**
The following `update-global-settings` example updates the S3 bucket used to store call detail records for Amazon Chime Business Calling and Amazon Chime Voice Connectors associated with the administrator's AWS account.

```
aws chime update-global-settings \
    --business-calling CdrBucket="s3bucket" \
    --voice-connector CdrBucket="s3bucket"
```
This command produces no output.
For more information, see [Managing Global Settings](https://docs.aws.amazon.com/chime/latest/ag/manage-global.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateGlobalSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-global-settings.html) in *AWS CLI Command Reference*.

### `update-phone-number-settings`
<a name="chime_UpdatePhoneNumberSettings_cli_2_topic"></a>

The following code example shows how to use `update-phone-number-settings`.

**AWS CLI**
**To update an outbound calling name**
The following `update-phone-number-settings` example updates the default outbound calling name for the administrator's AWS account.

```
aws chime update-phone-number-settings \
    --calling-name {{"myName"}}
```
This command produces no output.
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdatePhoneNumberSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number-settings.html) in *AWS CLI Command Reference*.

### `update-phone-number`
<a name="chime_UpdatePhoneNumber_cli_2_topic"></a>

The following code example shows how to use `update-phone-number`.

**AWS CLI**
**Example 1: To update the product type for a phone number**
The following `update-phone-number` example updates the specified phone number's product type.

```
aws chime update-phone-number \
    --phone-number-id {{"+12065550100"}} \
    --product-type {{"BusinessCalling"}}
```
Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "BusinessCalling",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [],
        "CallingName": "phonenumber1",
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-12T21:44:07.591Z"
    }
}
```
**Example 2: To update the outbound calling name for a phone number**
The following `update-phone-number` example updates the outbound calling name for the specified phone number.
aws chime update-phone-number --phone-number-id "\+12065550100" --calling-name "phonenumber2"
Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "BusinessCalling",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [],
        "CallingName": "phonenumber2",
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-12T21:44:07.591Z"
    }
}
```
For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdatePhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html) in *AWS CLI Command Reference*.

### `update-room-membership`
<a name="chime_UpdateRoomMembership_cli_2_topic"></a>

The following code example shows how to use `update-room-membership`.

**AWS CLI**
**To update a room membership**
The following `update-room-membership` example modifies the role of the specified chat room member to `Administrator`.

```
aws chime update-room-membership \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --member-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}} \
    --role {{Administrator}}
```
Output:

```
{
    "RoomMembership": {
        "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Member": {
            "MemberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MemberType": "User",
            "Email": "sofiamartinez@example.com",
            "FullName": "Sofia Martinez",
            "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        "Role": "Administrator",
        "InvitedBy": "arn:aws:iam::123456789012:user/admin",
        "UpdatedTimestamp": "2019-12-02T22:40:22.931Z"
    }
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [UpdateRoomMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room-membership.html) in *AWS CLI Command Reference*.

### `update-room`
<a name="chime_UpdateRoom_cli_2_topic"></a>

The following code example shows how to use `update-room`.

**AWS CLI**
**To update a chat room**
The following `update-room` example modifies the name of the specified chat room.

```
aws chime update-room \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --room-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --name {{teamRoom}}
```
Output:

```
{
    "Room": {
        "RoomId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "Name": "teamRoom",
        "AccountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreatedBy": "arn:aws:iam::123456789012:user/alejandro",
        "CreatedTimestamp": "2019-12-02T22:29:31.549Z",
        "UpdatedTimestamp": "2019-12-02T22:33:19.310Z"
    }
}
```
For more information, see [Creating a Chat Room](https://docs.aws.amazon.com/chime/latest/ug/chime-chat-room.html) in the *Amazon Chime User Guide*.
+  For API details, see [UpdateRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room.html) in *AWS CLI Command Reference*.

### `update-user-settings`
<a name="chime_UpdateUserSettings_cli_2_topic"></a>

The following code example shows how to use `update-user-settings`.

**AWS CLI**
**To update user settings**
The following `update-user-settings` example enables the specified user to make inbound and outbound calls and send and receive SMS messages.

```
aws chime update-user-settings \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --user-settings {{"Telephony={InboundCalling=true,OutboundCalling=true,SMS=true}"}}
```
This command produces no output.
For more information, see [Managing phone numbers in Amazon Chime](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateUserSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user-settings.html) in *AWS CLI Command Reference*.

### `update-user`
<a name="chime_UpdateUser_cli_2_topic"></a>

The following code example shows how to use `update-user`.

**AWS CLI**
**To update user details**
The following `update-user` example updates the specified details for the specified user.

```
aws chime update-user \
    --account-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --user-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --license-type {{"Basic"}}
```
Output:

```
{
    "User": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
}
```
For more information, see [Managing user permissions and access](https://docs.aws.amazon.com/chime/latest/ag/manage-access.html) in the *Amazon Chime Administration Guide*.
+  For API details, see [UpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html) in *AWS CLI Command Reference*.
