---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_iam_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# IAM examples using Tools for PowerShell V4
<a name="powershell_4_iam_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with IAM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-IAMClientIDToOpenIDConnectProvider`
<a name="iam_AddClientIdToOpenIdConnectProvider_powershell_4_topic"></a>

The following code example shows how to use `Add-IAMClientIDToOpenIDConnectProvider`.

**Tools for PowerShell V4**
**Example 1: This command adds the client ID (or audience) `my-application-ID` to the existing OIDC provider named `server.example.com`.**

```
Add-IAMClientIDToOpenIDConnectProvider -ClientID "my-application-ID" -OpenIDConnectProviderARN "arn:aws:iam::123456789012:oidc-provider/server.example.com"
```
+  For API details, see [AddClientIdToOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-IAMRoleTag`
<a name="iam_TagRole_powershell_4_topic"></a>

The following code example shows how to use `Add-IAMRoleTag`.

**Tools for PowerShell V4**
**Example 1: This example adds tag to Role in Identity Management Service**

```
Add-IAMRoleTag -RoleName AdminRoleacess -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-IAMRoleToInstanceProfile`
<a name="iam_AddRoleToInstanceProfile_powershell_4_topic"></a>

The following code example shows how to use `Add-IAMRoleToInstanceProfile`.

**Tools for PowerShell V4**
**Example 1: This command adds the role named `S3Access` to an existing instance profile named `webserver`. To create the instance profile, use the `New-IAMInstanceProfile` command. After you create the instance profile and associate it with a role using this command, you can attach it to an EC2 instance. To do that, use the `New-EC2Instance` cmdlet with either the `InstanceProfile_Arn` or the `InstanceProfile-Name` parameter to launch the new instance.**

```
Add-IAMRoleToInstanceProfile -RoleName "S3Access" -InstanceProfileName "webserver"
```
+  For API details, see [AddRoleToInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-IAMUserTag`
<a name="iam_TagUser_powershell_4_topic"></a>

The following code example shows how to use `Add-IAMUserTag`.

**Tools for PowerShell V4**
**Example 1: This example adds tag to User in Identity Management Service**

```
Add-IAMUserTag -UserName joe -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-IAMUserToGroup`
<a name="iam_AddUserToGroup_powershell_4_topic"></a>

The following code example shows how to use `Add-IAMUserToGroup`.

**Tools for PowerShell V4**
**Example 1: This command adds the user named `Bob` to the group named `Admins`.**

```
Add-IAMUserToGroup -UserName "Bob" -GroupName "Admins"
```
+  For API details, see [AddUserToGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Disable-IAMMFADevice`
<a name="iam_DeactivateMfaDevice_powershell_4_topic"></a>

The following code example shows how to use `Disable-IAMMFADevice`.

**Tools for PowerShell V4**
**Example 1: This command disables the hardware MFA device associated with the user `Bob` that has the serial number `123456789012`.**

```
Disable-IAMMFADevice -UserName "Bob" -SerialNumber "123456789012"
```
**Example 2: This command disables the virtual MFA device associated with the user `David` that has the ARN `arn:aws:iam::210987654321:mfa/David`. Note that virtual MFA device is not deleted from the account. The virtual device is still present and appears in the output of the `Get-IAMVirtualMFADevice` command. Before you can create a new virtual MFA device for the same user, you must delete the old one by using the `Remove-IAMVirtualMFADevice` command.**

```
Disable-IAMMFADevice -UserName "David" -SerialNumber "arn:aws:iam::210987654321:mfa/David"
```
+  For API details, see [DeactivateMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-IAMPassword`
<a name="iam_ChangePassword_powershell_4_topic"></a>

The following code example shows how to use `Edit-IAMPassword`.

**Tools for PowerShell V4**
**Example 1: This command changes the password for the user that is running the command. This command can be called by IAM users only. If this command is called when you are signed-in with AWS account (root) credentials, the command returns an `InvalidUserType` error.**

```
Edit-IAMPassword -OldPassword "MyOldP@ssw0rd" -NewPassword "MyNewP@ssw0rd"
```
+  For API details, see [ChangePassword](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Enable-IAMMFADevice`
<a name="iam_EnableMfaDevice_powershell_4_topic"></a>

The following code example shows how to use `Enable-IAMMFADevice`.

**Tools for PowerShell V4**
**Example 1: This command enables the hardware MFA device with the serial number `987654321098` and associates the device with the user `Bob`. It includes the first two codes in sequence from the device.**

```
Enable-IAMMFADevice -UserName "Bob" -SerialNumber "987654321098" -AuthenticationCode1 "12345678" -AuthenticationCode2 "87654321"
```
**Example 2: This example creates and enables a virtual MFA device. The first command creates the virtual device and returns the device's object representation in the variable `$MFADevice`. You can use the `.Base32StringSeed` or `QRCodePng` properties to configure the user's software application. The final command assigns the device to the user `David`, identifying the device by its serial number. The command also synchronizes the device with AWS by including the first two codes in sequence from the virtual MFA device.**

```
$MFADevice = New-IAMVirtualMFADevice -VirtualMFADeviceName "MyMFADevice"
# see example for New-IAMVirtualMFADevice to see how to configure the software program with PNG or base32 seed code
Enable-IAMMFADevice -UserName "David" -SerialNumber -SerialNumber $MFADevice.SerialNumber -AuthenticationCode1 "24681357" -AuthenticationCode2 "13572468"
```
+  For API details, see [EnableMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccessKey`
<a name="iam_ListAccessKeys_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccessKey`.

**Tools for PowerShell V4**
**Example 1: This command lists the access keys for the IAM user named `Bob`. Note that you cannot list the secret access keys for IAM users. If the secret access keys are lost, you must create new access keys with the `New-IAMAccessKey` cmdlet.**

```
Get-IAMAccessKey -UserName "Bob"
```
**Output:**

```
AccessKeyId                CreateDate                   Status              UserName
-----------                ----------                   ------              --------
AKIAIOSFODNN7EXAMPLE       12/3/2014 10:53:41 AM        Active              Bob
AKIAI44QH8DHBEXAMPLE       6/6/2013 8:42:26 PM          Inactive            Bob
```
+  For API details, see [ListAccessKeys](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccessKeyLastUsed`
<a name="iam_GetAccessKeyLastUsed_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccessKeyLastUsed`.

**Tools for PowerShell V4**
**Example 1: Returns the owning user name and last-usage information for the supplied access key.**

```
Get-IAMAccessKeyLastUsed -AccessKeyId ABCDEXAMPLE
```
+  For API details, see [GetAccessKeyLastUsed](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccountAlias`
<a name="iam_ListAccountAliases_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccountAlias`.

**Tools for PowerShell V4**
**Example 1: This command returns the account alias for the AWS account.**

```
Get-IAMAccountAlias
```
**Output:**

```
ExampleCo
```
+  For API details, see [ListAccountAliases](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccountAuthorizationDetail`
<a name="iam_GetAccountAuthorizationDetails_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccountAuthorizationDetail`.

**Tools for PowerShell V4**
**Example 1: This example gets authorization details about the identities in the AWS account, and displays the element list of the returned object, including users, groups, and roles. For example, the `UserDetailList` property displays details about the users. Similar information is available in the `RoleDetailList` and `GroupDetailList` properties.**

```
$Details=Get-IAMAccountAuthorizationDetail
$Details
```
**Output:**

```
GroupDetailList : {Administrators, Developers, Testers, Backup}
IsTruncated     : False
Marker          :
RoleDetailList  : {TestRole1, AdminRole, TesterRole, clirole...}
UserDetailList  : {Administrator, Bob, BackupToS3, }
```

```
$Details.UserDetailList
```
**Output:**

```
Arn            : arn:aws:iam::123456789012:user/Administrator
CreateDate     : 10/16/2014 9:03:09 AM
GroupList      : {Administrators}
Path           : /
UserId         : AIDACKCEVSQ6CEXAMPLE1
UserName       : Administrator
UserPolicyList : {}

Arn            : arn:aws:iam::123456789012:user/Bob
CreateDate     : 4/6/2015 12:54:42 PM
GroupList      : {Developers}
Path           : /
UserId         : AIDACKCEVSQ6CEXAMPLE2
UserName       : bab
UserPolicyList : {}

Arn            : arn:aws:iam::123456789012:user/BackupToS3
CreateDate     : 1/27/2015 10:15:08 AM
GroupList      : {Backup}
Path           : /
UserId         : AIDACKCEVSQ6CEXAMPLE3
UserName       : BackupToS3
UserPolicyList : {BackupServicePermissionsToS3Buckets}
```
+  For API details, see [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccountPasswordPolicy`
<a name="iam_GetAccountPasswordPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccountPasswordPolicy`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the password policy for the current account. If no password policy is defined for the account, the command returns a `NoSuchEntity` error.**

```
Get-IAMAccountPasswordPolicy
```
**Output:**

```
AllowUsersToChangePassword : True
ExpirePasswords            : True
HardExpiry                 : False
MaxPasswordAge             : 90
MinimumPasswordLength      : 8
PasswordReusePrevention    : 20
RequireLowercaseCharacters : True
RequireNumbers             : True
RequireSymbols             : False
RequireUppercaseCharacters : True
```
+  For API details, see [GetAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAccountSummary`
<a name="iam_GetAccountSummary_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAccountSummary`.

**Tools for PowerShell V4**
**Example 1: This example returns information about the current IAM entity usage and current IAM entity quotas in the AWS account.**

```
Get-IAMAccountSummary
```
**Output:**

```
Key                                        Value
Users                                      7
GroupPolicySizeQuota                       5120
PolicyVersionsInUseQuota                   10000
ServerCertificatesQuota                    20
AccountSigningCertificatesPresent          0
AccountAccessKeysPresent                   0
Groups                                     3
UsersQuota                                 5000
RolePolicySizeQuota                        10240
UserPolicySizeQuota                        2048
GroupsPerUserQuota                         10
AssumeRolePolicySizeQuota                  2048
AttachedPoliciesPerGroupQuota              2
Roles                                      9
VersionsPerPolicyQuota                     5
GroupsQuota                                100
PolicySizeQuota                            5120
Policies                                   5
RolesQuota                                 250
ServerCertificates                         0
AttachedPoliciesPerRoleQuota               2
MFADevicesInUse                            2
PoliciesQuota                              1000
AccountMFAEnabled                          1
Providers                                  2
InstanceProfilesQuota                      100
MFADevices                                 4
AccessKeysPerUserQuota                     2
AttachedPoliciesPerUserQuota               2
SigningCertificatesPerUserQuota            2
PolicyVersionsInUse                        4
InstanceProfiles                           1
...
```
+  For API details, see [GetAccountSummary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAttachedGroupPolicyList`
<a name="iam_ListAttachedGroupPolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAttachedGroupPolicyList`.

**Tools for PowerShell V4**
**Example 1: This command returns the names and ARNs of the managed policies that are attached to the IAM group named `Admins` in the AWS account. To see the list of inline policies embedded in the group, use the `Get-IAMGroupPolicyList` command.**

```
Get-IAMAttachedGroupPolicyList -GroupName "Admins"
```
**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/SecurityAudit                     SecurityAudit
arn:aws:iam::aws:policy/AdministratorAccess               AdministratorAccess
```
+  For API details, see [ListAttachedGroupPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAttachedRolePolicyList`
<a name="iam_ListAttachedRolePolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAttachedRolePolicyList`.

**Tools for PowerShell V4**
**Example 1: This command returns the names and ARNs of the managed policies attached to the IAM role named `SecurityAuditRole` in the AWS account. To see the list of inline policies that are embedded in the role, use the `Get-IAMRolePolicyList` command.**

```
Get-IAMAttachedRolePolicyList -RoleName "SecurityAuditRole"
```
**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/SecurityAudit                     SecurityAudit
```
+  For API details, see [ListAttachedRolePolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMAttachedUserPolicyList`
<a name="iam_ListAttachedUserPolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMAttachedUserPolicyList`.

**Tools for PowerShell V4**
**Example 1: This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account. To see the list of inline policies that are embedded in the IAM user, use the `Get-IAMUserPolicyList` command.**

```
Get-IAMAttachedUserPolicyList -UserName "Bob"
```
**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/TesterPolicy                      TesterPolicy
```
+  For API details, see [ListAttachedUserPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMContextKeysForCustomPolicy`
<a name="iam_GetContextKeysForCustomPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMContextKeysForCustomPolicy`.

**Tools for PowerShell V4**
**Example 1: This example fetches all the context keys present in the provided policy json.In order to provide multiple policies you can provide as comma separated list of values.**

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForCustomPolicy -PolicyInputList $policy1,$policy2
```
+  For API details, see [GetContextKeysForCustomPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMContextKeysForPrincipalPolicy`
<a name="iam_GetContextKeysForPrincipalPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMContextKeysForPrincipalPolicy`.

**Tools for PowerShell V4**
**Example 1: This example fetches all the context keys present in the provided policy json and the policies attached to IAM entity(user/role etc.). For -PolicyInputList you can provide multiple values list as comma separated values. **

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForPrincipalPolicy -PolicyInputList $policy1,$policy2 -PolicySourceArn arn:aws:iam::852640994763:user/TestUser
```
+  For API details, see [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMCredentialReport`
<a name="iam_GetCredentialReport_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMCredentialReport`.

**Tools for PowerShell V4**
**Example 1: This example opens the returned report and outputs it to the pipeline as an array of text lines. The first line is the header with comma-separated column names. Each successive row is the detail row for one user, with each field separated by commas. Before you can view the report, you must generate it with the `Request-IAMCredentialReport` cmdlet. To retrieve the report as a single string, use `-Raw` instead of `-AsTextArray`. The alias `-SplitLines` is also accepted for the `-AsTextArray` switch. For the full list of columns in the output consult the service API reference. Note that if you do not use `-AsTextArray` or `-SplitLines`, then you must extract the text from the `.Content` property using the .NET `StreamReader` class.**

```
Request-IAMCredentialReport
```
**Output:**

```
Description                                                         State
-----------                                                         -----
No report exists. Starting a new report generation task             STARTED
```

```
Get-IAMCredentialReport -AsTextArray
```
**Output:**

```
      user,arn,user_creation_time,password_enabled,password_last_used,password_last_changed,password_next_rotation,mfa_active,access_key_1_active,access_key_1_last_rotated,access_key_2_active,access_key_2_last_rotated,cert_1_active,cert_1_last_rotated,cert_2_active,cert_2_last_rotated root_account,arn:aws:iam::123456789012:root,2014-10-15T16:31:25+00:00,not_supported,2015-04-20T17:41:10+00:00,not_supported,not_supported,true,false,N/A,false,N/A,false,N/A,false,N/A
Administrator,arn:aws:iam::123456789012:user/Administrator,2014-10-16T16:03:09+00:00,true,2015-04-20T15:18:32+00:00,2014-10-16T16:06:00+00:00,N/A,false,true,2014-12-03T18:53:41+00:00,true,2015-03-25T20:38:14+00:00,false,N/A,false,N/A
Bill,arn:aws:iam::123456789012:user/Bill,2015-04-15T18:27:44+00:00,false,N/A,N/A,N/A,false,false,N/A,false,N/A,false,2015-04-20T20:00:12+00:00,false,N/A
```
+  For API details, see [GetCredentialReport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMEntitiesForPolicy`
<a name="iam_ListEntitiesForPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMEntitiesForPolicy`.

**Tools for PowerShell V4**
**Example 1: This example returns a list of IAM groups, roles, and users who have the policy `arn:aws:iam::123456789012:policy/TestPolicy` attached.**

```
Get-IAMEntitiesForPolicy -PolicyArn "arn:aws:iam::123456789012:policy/TestPolicy"
```
**Output:**

```
IsTruncated  : False
Marker       :
PolicyGroups : {}
PolicyRoles  : {testRole}
PolicyUsers  : {Bob, Theresa}
```
+  For API details, see [ListEntitiesForPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMGroup`
<a name="iam_GetGroup_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMGroup`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the IAM group `Testers`, including a collection of all the IAM users that belong to the group. **

```
$results = Get-IAMGroup -GroupName "Testers"
$results
```
**Output:**

```
Group                                     IsTruncated           Marker                Users
-----                                     -----------           ------                -----
Amazon.IdentityManagement.Model.Group     False                                       {Theresa, David}
```

```
$results.Group
```
**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : 3RHNZZGQJ7QHMAEXAMPLE1
GroupName  : Testers
Path       : /
```

```
$results.Users
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:user/Theresa
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 1/1/0001 12:00:00 AM
Path             : /
UserId           : 4OSVDDJJTF4XEEXAMPLE2
UserName         : Theresa

Arn              : arn:aws:iam::123456789012:user/David
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 3/19/2015 8:44:04 AM
Path             : /
UserId           : Y4FKWQCXTA52QEXAMPLE3
UserName         : David
```
+  For API details, see [GetGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMGroupForUser`
<a name="iam_ListGroupsForUser_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMGroupForUser`.

**Tools for PowerShell V4**
**Example 1: This example returns the list of IAM groups that the IAM user `David` belongs to.**

```
Get-IAMGroupForUser -UserName David
```
**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Administrators
CreateDate : 10/20/2014 10:06:24 AM
GroupId    : 6WCH4TRY3KIHIEXAMPLE1
GroupName  : Administrators
Path       : /

Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : RHNZZGQJ7QHMAEXAMPLE2
GroupName  : Testers
Path       : /

Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 12/10/2014 3:38:55 PM
GroupId    : ZU2EOWMK6WBZOEXAMPLE3
GroupName  : Developers
Path       : /
```
+  For API details, see [ListGroupsForUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMGroupList`
<a name="iam_ListGroups_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMGroupList`.

**Tools for PowerShell V4**
**Example 1: This example returns a collection of all the IAM groups defined in the current AWS account.**

```
Get-IAMGroupList
```
**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Administrators
CreateDate : 10/20/2014 10:06:24 AM
GroupId    : 6WCH4TRY3KIHIEXAMPLE1
GroupName  : Administrators
Path       : /

Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 12/10/2014 3:38:55 PM
GroupId    : ZU2EOWMK6WBZOEXAMPLE2
GroupName  : Developers
Path       : /

Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : RHNZZGQJ7QHMAEXAMPLE3
GroupName  : Testers
Path       : /
```
+  For API details, see [ListGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMGroupPolicy`
<a name="iam_GetGroupPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMGroupPolicy`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the embedded inline policy named `PowerUserAccess-Testers` for the group `Testers`. The `PolicyDocument` property is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = Get-IAMGroupPolicy -GroupName Testers -PolicyName PowerUserAccess-Testers
$results
```
**Output:**

```
GroupName     PolicyDocument                                              PolicyName
---------     --------------                                              ----------
Testers       %7B%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%0A%20... PowerUserAccess-Testers

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.PolicyDocument)
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:555555555555:instance/i-b188560f"
      ]
    }
  ]
}
```
+  For API details, see [GetGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMGroupPolicyList`
<a name="iam_ListGroupPolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMGroupPolicyList`.

**Tools for PowerShell V4**
**Example 1: This example returns a list of the inline policies that are embedded in the group `Testers`. To get the managed policies that are attached to the group, use the command `Get-IAMAttachedGroupPolicyList`.**

```
Get-IAMGroupPolicyList -GroupName Testers
```
**Output:**

```
Deny-Assume-S3-Role-In-Production
PowerUserAccess-Testers
```
+  For API details, see [ListGroupPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMInstanceProfile`
<a name="iam_GetInstanceProfile_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMInstanceProfile`.

**Tools for PowerShell V4**
**Example 1: This example returns details of the instance profile named `ec2instancerole` that is defined in the current AWS account.**

```
Get-IAMInstanceProfile -InstanceProfileName ec2instancerole
```
**Output:**

```
Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
CreateDate          : 2/17/2015 2:49:04 PM
InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
InstanceProfileName : ec2instancerole
Path                : /
Roles               : {ec2instancerole}
```
+  For API details, see [GetInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMInstanceProfileForRole`
<a name="iam_ListInstanceProfilesForRole_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMInstanceProfileForRole`.

**Tools for PowerShell V4**
**Example 1: This example returns details of the instance profile associated with the role `ec2instancerole`.**

```
Get-IAMInstanceProfileForRole -RoleName ec2instancerole
```
**Output:**

```
      Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
      CreateDate          : 2/17/2015 2:49:04 PM
      InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
      InstanceProfileName : ec2instancerole
      Path                : /
      Roles               : {ec2instancerole}
```
+  For API details, see [ListInstanceProfilesForRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMInstanceProfileList`
<a name="iam_ListInstanceProfiles_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMInstanceProfileList`.

**Tools for PowerShell V4**
**Example 1: This example returns a collection of the instance profiles defined in the current AWS account.**

```
Get-IAMInstanceProfileList
```
**Output:**

```
Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
CreateDate          : 2/17/2015 2:49:04 PM
InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
InstanceProfileName : ec2instancerole
Path                : /
Roles               : {ec2instancerole}
```
+  For API details, see [ListInstanceProfiles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMLoginProfile`
<a name="iam_GetLoginProfile_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMLoginProfile`.

**Tools for PowerShell V4**
**Example 1: This example returns the password creation date and whether a password reset is required for the IAM user `David`.**

```
Get-IAMLoginProfile -UserName David
```
**Output:**

```
CreateDate                   PasswordResetRequired                 UserName
----------                   ---------------------                 --------
12/10/2014 3:39:44 PM        False                                 David
```
+  For API details, see [GetLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMMFADevice`
<a name="iam_ListMfaDevices_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMMFADevice`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the MFA device assigned to the IAM user `David`. In this example you can tell that it is a virtual device because the `SerialNumber` is an ARN instead of a physical device's actual serial number.**

```
Get-IAMMFADevice -UserName David
```
**Output:**

```
EnableDate                  SerialNumber                           UserName
----------                  ------------                           --------
4/8/2015 9:41:10 AM         arn:aws:iam::123456789012:mfa/David    David
```
+  For API details, see [ListMfaDevices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMOpenIDConnectProvider`
<a name="iam_GetOpenIdConnectProvider_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMOpenIDConnectProvider`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/accounts.google.com`. The `ClientIDList` property is a collection that contains all the Client IDs defined for this provider.**

```
Get-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/oidc.example.com
```
**Output:**

```
ClientIDList         CreateDate                ThumbprintList                               Url
------------         ----------                --------------                               ---
{MyOIDCApp}          2/3/2015 3:00:30 PM       {12345abcdefghijk67890lmnopqrst98765uvwxy}   oidc.example.com
```
+  For API details, see [GetOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMOpenIDConnectProviderList`
<a name="iam_ListOpenIdConnectProviders_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMOpenIDConnectProviderList`.

**Tools for PowerShell V4**
**Example 1: This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.**

```
Get-IAMOpenIDConnectProviderList
```
**Output:**

```
Arn
---
arn:aws:iam::123456789012:oidc-provider/server.example.com
arn:aws:iam::123456789012:oidc-provider/another.provider.com
```
+  For API details, see [ListOpenIdConnectProviders](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMPolicy`
<a name="iam_GetPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMPolicy`.

**Tools for PowerShell V4**
**Example 1: This example returns details about the managed policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.**

```
Get-IAMPolicy -PolicyArn arn:aws:iam::123456789012:policy/MySamplePolicy
```
**Output:**

```
Arn              : arn:aws:iam::aws:policy/MySamplePolicy
AttachmentCount  : 0
CreateDate       : 2/6/2015 10:40:08 AM
DefaultVersionId : v1
Description      :
IsAttachable     : True
Path             : /
PolicyId         : Z27SI6FQMGNQ2EXAMPLE1
PolicyName       : MySamplePolicy
UpdateDate       : 2/6/2015 10:40:08 AM
```
+  For API details, see [GetPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMPolicyList`
<a name="iam_ListPolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMPolicyList`.

**Tools for PowerShell V4**
**Example 1: This example returns a collection of the first three managed policies available in the current AWS account. Because `-scope` is not specified, it defaults to `all` and includes both AWS managed and customer managed policies.**

```
Get-IAMPolicyList -MaxItem 3
```
**Output:**

```
Arn              : arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess
AttachmentCount  : 0
CreateDate       : 2/6/2015 10:40:08 AM
DefaultVersionId : v1
Description      :
IsAttachable     : True
Path             : /
PolicyId         : Z27SI6FQMGNQ2EXAMPLE1
PolicyName       : AWSDirectConnectReadOnlyAccess
UpdateDate       : 2/6/2015 10:40:08 AM

Arn              : arn:aws:iam::aws:policy/AmazonGlacierReadOnlyAccess
AttachmentCount  : 0
CreateDate       : 2/6/2015 10:40:27 AM
DefaultVersionId : v1
Description      :
IsAttachable     : True
Path             : /
PolicyId         : NJKMU274MET4EEXAMPLE2
PolicyName       : AmazonGlacierReadOnlyAccess
UpdateDate       : 2/6/2015 10:40:27 AM

Arn              : arn:aws:iam::aws:policy/AWSMarketplaceFullAccess
AttachmentCount  : 0
CreateDate       : 2/11/2015 9:21:45 AM
DefaultVersionId : v1
Description      :
IsAttachable     : True
Path             : /
PolicyId         : 5ULJSO2FYVPYGEXAMPLE3
PolicyName       : AWSMarketplaceFullAccess
UpdateDate       : 2/11/2015 9:21:45 AM
```
**Example 2: This example returns a collection of the first two customer managed policies available in current AWS account. It uses `-Scope local` to limit the output to only customer managed policies. **

```
Get-IAMPolicyList -Scope local -MaxItem 2
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:policy/MyLocalPolicy
AttachmentCount  : 0
CreateDate       : 2/12/2015 9:39:09 AM
DefaultVersionId : v2
Description      :
IsAttachable     : True
Path             : /
PolicyId         : SQVCBLC4VAOUCEXAMPLE4
PolicyName       : MyLocalPolicy
UpdateDate       : 2/12/2015 9:39:53 AM

Arn              : arn:aws:iam::123456789012:policy/policyforec2instancerole
AttachmentCount  : 1
CreateDate       : 2/17/2015 2:51:38 PM
DefaultVersionId : v11
Description      :
IsAttachable     : True
Path             : /
PolicyId         : X5JPBLJH2Z2SOEXAMPLE5
PolicyName       : policyforec2instancerole
UpdateDate       : 2/18/2015 8:52:31 AM
```
+  For API details, see [ListPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMPolicyVersion`
<a name="iam_GetPolicyVersion_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMPolicyVersion`.

**Tools for PowerShell V4**
**Example 1: This example returns the policy document for the `v2` version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyManagedPolicy`. The policy document in the `Document` property is URL encoded and is decoded in this example with the `UrlDecode` .NET method.**

```
$results = Get-IAMPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MyManagedPolicy -VersionId v2
$results
```
**Output:**

```
CreateDate             Document                                        IsDefaultVersion     VersionId
----------             --------                                        ----------------     ---------
2/12/2015 9:39:53 AM   %7B%0A%20%20%22Version%22%3A%20%222012-10...    True                 v2

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
$policy = [System.Web.HttpUtility]::UrlDecode($results.Document)
$policy
{
  "Version":"2012-10-17",
  "Statement":
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:555555555555:instance/i-b188560f"
      ]
    }
}
```
+  For API details, see [GetPolicyVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMPolicyVersionList`
<a name="iam_ListPolicyVersions_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMPolicyVersionList`.

**Tools for PowerShell V4**
**Example 1: This example returns the list of available versions of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyManagedPolicy`. To get the policy document for a specific version, use the `Get-IAMPolicyVersion` command and specify the `VersionId` of the one you want.**

```
Get-IAMPolicyVersionList -PolicyArn arn:aws:iam::123456789012:policy/MyManagedPolicy
```
**Output:**

```
CreateDate                   Document                 IsDefaultVersion                  VersionId
----------                   --------                 ----------------                  ---------
2/12/2015 9:39:53 AM                                  True                              v2
2/12/2015 9:39:09 AM                                  False                             v1
```
+  For API details, see [ListPolicyVersions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMRole`
<a name="iam_GetRole_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMRole`.

**Tools for PowerShell V4**
**Example 1: This example returns the details of the `lamda_exec_role`. It includes the trust policy document that specifies who can assume this role. The policy document is URL encoded and can be decoded using the .NET `UrlDecode` method. In this example, the original policy had all white space removed before it was uploaded to the policy. To see the permissions policy documents that determine what someone who assumes the role can do, use the `Get-IAMRolePolicy` for inline policies, and `Get-IAMPolicyVersion` for attached managed policies.**

```
$results = Get-IamRole -RoleName lambda_exec_role
$results | Format-List
```
**Output:**

```
Arn                      : arn:aws:iam::123456789012:role/lambda_exec_role
AssumeRolePolicyDocument : %7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Sid%22
                           %3A%22%22%2C%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22Service
                           %22%3A%22lambda.amazonaws.com%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole
                           %22%7D%5D%7D
CreateDate               : 4/2/2015 9:16:11 AM
Path                     : /
RoleId                   : 2YBIKAIBHNKB4EXAMPLE1
RoleName                 : lambda_exec_role
```

```
$policy = [System.Web.HttpUtility]::UrlDecode($results.AssumeRolePolicyDocument)
$policy
```
**Output:**

```
{"Version":"2012-10-17",		 	 	 "Statement":[{"Sid":"","Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}
```
+  For API details, see [GetRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMRoleList`
<a name="iam_ListRoles_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMRoleList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves a list of all of the IAM roles in the AWS account.**

```
Get-IAMRoleList
```
+  For API details, see [ListRoles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMRolePolicy`
<a name="iam_GetRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example returns the permissions policy document for the policy named `oneClick_lambda_exec_role_policy` that is embedded in the IAM role `lamda_exec_role`. The resulting policy document is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = Get-IAMRolePolicy -RoleName lambda_exec_role -PolicyName oneClick_lambda_exec_role_policy
$results
```
**Output:**

```
PolicyDocument                                            PolicyName                           UserName
--------------                                            ----------                           --------
%7B%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%...    oneClick_lambda_exec_role_policy     lambda_exec_role
```

```
[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.PolicyDocument)
```
**Output:**

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:*"
      ],
      "Resource": "arn:aws:logs:us-east-1:555555555555:log-group:/aws/lambda/aws-example-function:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ]
    }
  ]
}
```
+  For API details, see [GetRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMRolePolicyList`
<a name="iam_ListRolePolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMRolePolicyList`.

**Tools for PowerShell V4**
**Example 1: This example returns the list of names of inline policies that are embedded in the IAM role `lamda_exec_role`. To see the details of an inline policy, use the command `Get-IAMRolePolicy`.**

```
Get-IAMRolePolicyList -RoleName lambda_exec_role
```
**Output:**

```
oneClick_lambda_exec_role_policy
```
+  For API details, see [ListRolePolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMRoleTagList`
<a name="iam_ListRoleTags_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMRoleTagList`.

**Tools for PowerShell V4**
**Example 1: This example fetches the tag associated with the role..**

```
Get-IAMRoleTagList -RoleName MyRoleName
```
+  For API details, see [ListRoleTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMSAMLProvider`
<a name="iam_GetSamlProvider_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMSAMLProvider`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the details about the SAML 2.0 provider whose ARM is arn:aws:iam::123456789012:saml-provider/SAMLADFS. The response includes the metadata document that you got from the identity provider to create the AWS SAML provider entity as well as the creation and expiration dates.**

```
Get-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFS
```
**Output:**

```
CreateDate                 SAMLMetadataDocument                                          ValidUntil
----------                 --------------------                                          ----------
12/23/2014 12:16:55 PM    <EntityDescriptor ID="_12345678-1234-5678-9012-example1...    12/23/2114 12:16:54 PM
```
+  For API details, see [GetSamlProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMSAMLProviderList`
<a name="iam_ListSAMLProviders_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMSAMLProviderList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the list of SAML 2.0 providers created in the current AWS account. It returns the ARN, creation date, and expiration date for each SAML provider.**

```
Get-IAMSAMLProviderList
```
**Output:**

```
Arn                                                 CreateDate                      ValidUntil
---                                                 ----------                      ----------
arn:aws:iam::123456789012:saml-provider/SAMLADFS    12/23/2014 12:16:55 PM          12/23/2114 12:16:54 PM
```
+  For API details, see [ListSAMLProviders](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMServerCertificate`
<a name="iam_GetServerCertificate_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMServerCertificate`.

**Tools for PowerShell V4**
**Example 1: This example retrieves details about the server certificate named `MyServerCertificate`. You can find the certificate details in the `CertificateBody` and `ServerCertificateMetadata` properties.**

```
$result = Get-IAMServerCertificate -ServerCertificateName MyServerCertificate
$result | format-list
```
**Output:**

```
CertificateBody           : -----BEGIN CERTIFICATE-----
                            MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
                            VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
                            b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
                            BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
                            MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
                            VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
                            b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
                            YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
                            21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
                            rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
                            Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
                            nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
                            FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
                            NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=
                            -----END CERTIFICATE-----
CertificateChain          :
ServerCertificateMetadata : Amazon.IdentityManagement.Model.ServerCertificateMetadata
```

```
$result.ServerCertificateMetadata
```
**Output:**

```
Arn                   : arn:aws:iam::123456789012:server-certificate/Org1/Org2/MyServerCertificate
Expiration            : 1/14/2018 9:52:36 AM
Path                  : /Org1/Org2/
ServerCertificateId   : ASCAJIFEXAMPLE17HQZYW
ServerCertificateName : MyServerCertificate
UploadDate            : 4/21/2015 11:14:16 AM
```
+  For API details, see [GetServerCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMServerCertificateList`
<a name="iam_ListServerCertificates_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMServerCertificateList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the list of server certificates that have been uploaded to the current AWS account.**

```
Get-IAMServerCertificateList
```
**Output:**

```
Arn                   : arn:aws:iam::123456789012:server-certificate/Org1/Org2/MyServerCertificate
Expiration            : 1/14/2018 9:52:36 AM
Path                  : /Org1/Org2/
ServerCertificateId   : ASCAJIFEXAMPLE17HQZYW
ServerCertificateName : MyServerCertificate
UploadDate            : 4/21/2015 11:14:16 AM
```
+  For API details, see [ListServerCertificates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMServiceLastAccessedDetail`
<a name="iam_GetServiceLastAccessedDetails_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMServiceLastAccessedDetail`.

**Tools for PowerShell V4**
**Example 1: This example provides details of the service last accessed by the IAM entity(user, group, role or policy) associated in Request call. **

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser
```
**Output:**

```
f0b7a819-eab0-929b-dc26-ca598911cb9f
```

```
Get-IAMServiceLastAccessedDetail -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f
```
+  For API details, see [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMServiceLastAccessedDetailWithEntity`
<a name="iam_GetServiceLastAccessedDetailsWithEntities_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMServiceLastAccessedDetailWithEntity`.

**Tools for PowerShell V4**
**Example 1: This example provides the last accessed timestamp for the service in the request by that respective IAM entity.**

```
$results = Get-IAMServiceLastAccessedDetailWithEntity -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f -ServiceNamespace ec2
$results
```
**Output:**

```
EntityDetailsList : {Amazon.IdentityManagement.Model.EntityDetails}
Error             :
IsTruncated       : False
JobCompletionDate : 12/29/19 11:19:31 AM
JobCreationDate   : 12/29/19 11:19:31 AM
JobStatus         : COMPLETED
Marker            :
```

```
$results.EntityDetailsList
```
**Output:**

```
EntityInfo                                 LastAuthenticated
----------                                 -----------------
Amazon.IdentityManagement.Model.EntityInfo 11/16/19 3:47:00 PM
```

```
$results.EntityInfo
```
**Output:**

```
Arn  : arn:aws:iam::123456789012:user/TestUser
Id   : AIDA4NBK5CXF5TZHU1234
Name : TestUser
Path : /
Type : USER
```
+  For API details, see [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMSigningCertificate`
<a name="iam_ListSigningCertificates_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMSigningCertificate`.

**Tools for PowerShell V4**
**Example 1: This example retrieves details about the signing certificate that is associated with the user named `Bob`.**

```
Get-IAMSigningCertificate -UserName Bob
```
**Output:**

```
CertificateBody : -----BEGIN CERTIFICATE-----
                  MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
                  VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
                  b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
                  BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
                  MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
                  VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
                  b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
                  YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
                  21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
                  rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
                  Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
                  nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
                  FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
                  NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=
                  -----END CERTIFICATE-----
CertificateId   : Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
Status          : Active
UploadDate      : 4/20/2015 1:26:01 PM
UserName        : Bob
```
+  For API details, see [ListSigningCertificates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMUser`
<a name="iam_GetUser_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMUser`.

**Tools for PowerShell V4**
**Example 1: This example retrieves details about the user named `David`.**

```
Get-IAMUser -UserName David
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:user/David
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 3/19/2015 8:44:04 AM
Path             : /
UserId           : Y4FKWQCXTA52QEXAMPLE1
UserName         : David
```
**Example 2: This example retrieves details about the currently signed-in IAM user.**

```
Get-IAMUser
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:user/Bob
CreateDate       : 10/16/2014 9:03:09 AM
PasswordLastUsed : 3/4/2015 12:12:33 PM
Path             : /
UserId           : 7K3GJEANSKZF2EXAMPLE2
UserName         : Bob
```
+  For API details, see [GetUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMUserList`
<a name="iam_ListUsers_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMUserList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves a collection of users in the current AWS account.**

```
Get-IAMUserList
```
**Output:**

```
      Arn              : arn:aws:iam::123456789012:user/Administrator
      CreateDate       : 10/16/2014 9:03:09 AM
      PasswordLastUsed : 3/4/2015 12:12:33 PM
      Path             : /
      UserId           : 7K3GJEANSKZF2EXAMPLE1
      UserName         : Administrator

      Arn              : arn:aws:iam::123456789012:user/Bob
      CreateDate       : 4/6/2015 12:54:42 PM
      PasswordLastUsed : 1/1/0001 12:00:00 AM
      Path             : /
      UserId           : L3EWNONDOM3YUEXAMPLE2
      UserName         : bab

      Arn              : arn:aws:iam::123456789012:user/David
      CreateDate       : 12/10/2014 3:39:27 PM
      PasswordLastUsed : 3/19/2015 8:44:04 AM
      Path             : /
      UserId           : Y4FKWQCXTA52QEXAMPLE3
      UserName         : David
```
+  For API details, see [ListUsers](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMUserPolicy`
<a name="iam_GetUserPolicy_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMUserPolicy`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the details of the inline policy named `Davids_IAM_Admin_Policy` that is embedded in the IAM user named `David`. The policy document is URL encoded.**

```
$results = Get-IAMUserPolicy -PolicyName Davids_IAM_Admin_Policy -UserName David
$results
```
**Output:**

```
PolicyDocument                                            PolicyName                    UserName
--------------                                            ----------                    --------
%7B%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%...    Davids_IAM_Admin_Policy       David

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.PolicyDocument)
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:GetUser",
        "iam:ListUsers"
      ],
      "Resource": [
        "arn:aws:iam::111122223333:user/*"
      ]
    }
  ]
}
```
+  For API details, see [GetUserPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMUserPolicyList`
<a name="iam_ListUserPolicies_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMUserPolicyList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the list of names of the inline policies that are embedded in the IAM user named `David`.**

```
Get-IAMUserPolicyList -UserName David
```
**Output:**

```
Davids_IAM_Admin_Policy
```
+  For API details, see [ListUserPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMUserTagList`
<a name="iam_ListUserTags_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMUserTagList`.

**Tools for PowerShell V4**
**Example 1: This example fetches the tag associated with the user.**

```
Get-IAMUserTagList -UserName joe
```
+  For API details, see [ListUserTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-IAMVirtualMFADevice`
<a name="iam_ListVirtualMfaDevices_powershell_4_topic"></a>

The following code example shows how to use `Get-IAMVirtualMFADevice`.

**Tools for PowerShell V4**
**Example 1: This example retrieves a collection of the virtual MFA devices that are assigned to users in the AWS account. The `User` property of each is an object with details of the IAM user to which the device is assigned.**

```
Get-IAMVirtualMFADevice -AssignmentStatus Assigned
```
**Output:**

```
Base32StringSeed :
EnableDate       : 4/13/2015 12:03:42 PM
QRCodePNG        :
SerialNumber     : arn:aws:iam::123456789012:mfa/David
User             : Amazon.IdentityManagement.Model.User

Base32StringSeed :
EnableDate       : 4/13/2015 12:06:41 PM
QRCodePNG        :
SerialNumber     : arn:aws:iam::123456789012:mfa/root-account-mfa-device
User             : Amazon.IdentityManagement.Model.User
```
+  For API details, see [ListVirtualMfaDevices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMAccessKey`
<a name="iam_CreateAccessKey_powershell_4_topic"></a>

The following code example shows how to use `New-IAMAccessKey`.

**Tools for PowerShell V4**
**Example 1: This example creates a new access key and secret access key pair and assigns it to the user `David`. Ensure that you save the `AccessKeyId` and `SecretAccessKey` values to a file because this is the only time you can obtain the `SecretAccessKey`. You cannot retrieve it later. If you lose the secret key, you must create a new access key pair.**

```
New-IAMAccessKey -UserName David
```
**Output:**

```
AccessKeyId     : AKIAIOSFODNN7EXAMPLE
CreateDate      : 4/13/2015 1:00:42 PM
SecretAccessKey : wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Status          : Active
UserName        : David
```
+  For API details, see [CreateAccessKey](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMAccountAlias`
<a name="iam_CreateAccountAlias_powershell_4_topic"></a>

The following code example shows how to use `New-IAMAccountAlias`.

**Tools for PowerShell V4**
**Example 1: This example changes the account alias for your AWS account to `mycompanyaws`. The address of the user logon page chages to https://mycompanyaws.signin.aws.amazon.com/console. The original URL using your account ID number instead of the alias (https://<accountidnumber>.signin.aws.amazon.com/console) continues to work. However, any previously defined alias-based URLs stop working.**

```
New-IAMAccountAlias -AccountAlias mycompanyaws
```
+  For API details, see [CreateAccountAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMGroup`
<a name="iam_CreateGroup_powershell_4_topic"></a>

The following code example shows how to use `New-IAMGroup`.

**Tools for PowerShell V4**
**Example 1: This example creates a new IAM group named `Developers`.**

```
New-IAMGroup -GroupName Developers
```
**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 4/14/2015 11:21:31 AM
GroupId    : QNEJ5PM4NFSQCEXAMPLE1
GroupName  : Developers
Path       : /
```
+  For API details, see [CreateGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMInstanceProfile`
<a name="iam_CreateInstanceProfile_powershell_4_topic"></a>

The following code example shows how to use `New-IAMInstanceProfile`.

**Tools for PowerShell V4**
**Example 1: This example creates a new IAM instance profile named `ProfileForDevEC2Instance`. You must separately run the `Add-IAMRoleToInstanceProfile` command to associate the instance profile with an existing IAM role that provides permissions to the instance. Finally, attach the instance profile to an EC2 instance when you launch it. To do that, use the `New-EC2Instance` cmdlet with either the `InstanceProfile_Arn` or `InstanceProfile_Name` parameter.**

```
New-IAMInstanceProfile -InstanceProfileName ProfileForDevEC2Instance
```
**Output:**

```
Arn                 : arn:aws:iam::123456789012:instance-profile/ProfileForDevEC2Instance
CreateDate          : 4/14/2015 11:31:39 AM
InstanceProfileId   : DYMFXL556EY46EXAMPLE1
InstanceProfileName : ProfileForDevEC2Instance
Path                : /
Roles               : {}
```
+  For API details, see [CreateInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMLoginProfile`
<a name="iam_CreateLoginProfile_powershell_4_topic"></a>

The following code example shows how to use `New-IAMLoginProfile`.

**Tools for PowerShell V4**
**Example 1: This example creates a (temporary) password for the IAM user named Bob, and sets the flag that requires the user to change the password the next time `Bob` signs in.**

```
New-IAMLoginProfile -UserName Bob -Password P@ssw0rd -PasswordResetRequired $true
```
**Output:**

```
CreateDate                    PasswordResetRequired                UserName
----------                    ---------------------                --------
4/14/2015 12:26:30 PM         True                                 Bob
```
+  For API details, see [CreateLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMOpenIDConnectProvider`
<a name="iam_CreateOpenIdConnectProvider_powershell_4_topic"></a>

The following code example shows how to use `New-IAMOpenIDConnectProvider`.

**Tools for PowerShell V4**
**Example 1: This example creates an IAM OIDC provider associated with the OIDC compatible provider service found at the URL `https://example.oidcprovider.com` and the client ID `my-testapp-1`. The OIDC provider supplies the thumbprint. To authenticate the thumbprint, follow the steps at http://docs.aws.amazon.com/IAM/latest/UserGuide/identity-providers-oidc-obtain-thumbprint.html.**

```
New-IAMOpenIDConnectProvider -Url https://example.oidcprovider.com -ClientIDList my-testapp-1 -ThumbprintList 990F419EXAMPLEECF12DDEDA5EXAMPLE52F20D9E
```
**Output:**

```
arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com
```
+  For API details, see [CreateOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMPolicy`
<a name="iam_CreatePolicy_powershell_4_topic"></a>

The following code example shows how to use `New-IAMPolicy`.

**Tools for PowerShell V4**
**Example 1: This example creates a new IAM policy in the current AWS account named `MySamplePolicy` The file `MySamplePolicy.json` provides the policy content. Note that you must use the `-Raw` switch parameter to successfully process the JSON policy file.**

```
New-IAMPolicy -PolicyName MySamplePolicy -PolicyDocument (Get-Content -Raw MySamplePolicy.json)
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:policy/MySamplePolicy
AttachmentCount  : 0
CreateDate       : 4/14/2015 2:45:59 PM
DefaultVersionId : v1
Description      :
IsAttachable     : True
Path             : /
PolicyId         : LD4KP6HVFE7WGEXAMPLE1
PolicyName       : MySamplePolicy
UpdateDate       : 4/14/2015 2:45:59 PM
```
+  For API details, see [CreatePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMPolicyVersion`
<a name="iam_CreatePolicyVersion_powershell_4_topic"></a>

The following code example shows how to use `New-IAMPolicyVersion`.

**Tools for PowerShell V4**
**Example 1: This example creates a new "v2" version of the IAM policy whose ARN is `arn:aws:iam::123456789012:policy/MyPolicy` and makes it the default version. The `NewPolicyVersion.json` file provides the policy content. Note that you must use the `-Raw` switch parameter to successfully process the JSON policy file.**

```
New-IAMPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MyPolicy -PolicyDocument (Get-content -Raw NewPolicyVersion.json) -SetAsDefault $true
```
**Output:**

```
CreateDate                           Document                  IsDefaultVersion             VersionId
----------                           --------                  ----------------             ---------
4/15/2015 10:54:54 AM                                          True                         v2
```
+  For API details, see [CreatePolicyVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMRole`
<a name="iam_CreateRole_powershell_4_topic"></a>

The following code example shows how to use `New-IAMRole`.

**Tools for PowerShell V4**
**Example 1: This example creates a new role named `MyNewRole` and attaches to it the policy found in the file `NewRoleTrustPolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the JSON policy file. The policy document displayed in the output is URL encoded. It is decoded in this example with the `UrlDecode` .NET method. **

```
$results = New-IAMRole -AssumeRolePolicyDocument (Get-Content -raw NewRoleTrustPolicy.json) -RoleName MyNewRole
$results
```
**Output:**

```
Arn                      : arn:aws:iam::123456789012:role/MyNewRole
AssumeRolePolicyDocument : %7B%0D%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%0D%0A%20%20%22Statement%22
                           %3A%20%5B%0D%0A%20%20%20%20%7B%0D%0A%20%20%20%20%20%20%22Sid%22%3A%20%22%22%2C
                           %0D%0A%20%20%20%20%20%20%22Effect%22%3A%20%22Allow%22%2C%0D%0A%20%20%20%20%20%20
                           %22Principal%22%3A%20%7B%0D%0A%20%20%20%20%20%20%20%20%22AWS%22%3A%20%22arn%3Aaws
                           %3Aiam%3A%3A123456789012%3ADavid%22%0D%0A%20%20%20%20%20%20%7D%2C%0D%0A%20%20%20
                           %20%20%20%22Action%22%3A%20%22sts%3AAssumeRole%22%0D%0A%20%20%20%20%7D%0D%0A%20
                           %20%5D%0D%0A%7D
CreateDate               : 4/15/2015 11:04:23 AM
Path                     : /
RoleId                   : V5PAJI2KPN4EAEXAMPLE1
RoleName                 : MyNewRole

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.AssumeRolePolicyDocument)
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:David"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
+  For API details, see [CreateRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMSAMLProvider`
<a name="iam_CreateSAMLProvider_powershell_4_topic"></a>

The following code example shows how to use `New-IAMSAMLProvider`.

**Tools for PowerShell V4**
**Example 1: This example creates a new SAML provider entity in IAM. It is named `MySAMLProvider` and is described by the SAML metadata document found in the file `SAMLMetaData.xml`, which was separately downloaded from the SAML service provider's web site.**

```
New-IAMSAMLProvider -Name MySAMLProvider -SAMLMetadataDocument (Get-Content -Raw SAMLMetaData.xml)
```
**Output:**

```
arn:aws:iam::123456789012:saml-provider/MySAMLProvider
```
+  For API details, see [CreateSAMLProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMServiceLinkedRole`
<a name="iam_CreateServiceLinkedRole_powershell_4_topic"></a>

The following code example shows how to use `New-IAMServiceLinkedRole`.

**Tools for PowerShell V4**
**Example 1: This example creates a servicelinked role for autoscaling service.**

```
New-IAMServiceLinkedRole -AWSServiceName autoscaling.amazonaws.com -CustomSuffix RoleNameEndsWithThis -Description "My service-linked role to support autoscaling"
```
+  For API details, see [CreateServiceLinkedRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMUser`
<a name="iam_CreateUser_powershell_4_topic"></a>

The following code example shows how to use `New-IAMUser`.

**Tools for PowerShell V4**
**Example 1: This example creates an IAM user named `Bob`. If Bob needs to sign in to the AWS console, then you must separately run the command `New-IAMLoginProfile` to create a sign-in profile with a password. If Bob needs to run AWS PowerShell or cross-platform CLI commands or make AWS API calls, then you must separately run the `New-IAMAccessKey` command to create access keys.**

```
New-IAMUser -UserName Bob
```
**Output:**

```
Arn              : arn:aws:iam::123456789012:user/Bob
CreateDate       : 4/22/2015 12:02:11 PM
PasswordLastUsed : 1/1/0001 12:00:00 AM
Path             : /
UserId           : AIDAJWGEFDMEMEXAMPLE1
UserName         : Bob
```
+  For API details, see [CreateUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-IAMVirtualMFADevice`
<a name="iam_CreateVirtualMfaDevice_powershell_4_topic"></a>

The following code example shows how to use `New-IAMVirtualMFADevice`.

**Tools for PowerShell V4**
**Example 1: This example creates a new virtual MFA device. Lines 2 and 3 extract the `Base32StringSeed` value that the virtual MFA software program needs to create an account (as an alternative to the QR code). After you configure the program with the value, get two sequential authentication codes from the program. Finally, use the last command to link the virtual MFA device to the IAM user `Bob` and synchronize the account with the two authentication codes.**

```
$Device = New-IAMVirtualMFADevice -VirtualMFADeviceName BobsMFADevice
$SR = New-Object System.IO.StreamReader($Device.Base32StringSeed)
$base32stringseed = $SR.ReadToEnd()
$base32stringseed
CZWZMCQNW4DEXAMPLE3VOUGXJFZYSUW7EXAMPLECR4NJFD65GX2SLUDW2EXAMPLE
```
**Output:**

```
-- Pause here to enter base-32 string seed code into virtual MFA program to register account. --

Enable-IAMMFADevice -SerialNumber $Device.SerialNumber -UserName Bob -AuthenticationCode1 123456 -AuthenticationCode2 789012
```
**Example 2: This example creates a new virtual MFA device. Lines 2 and 3 extract the `QRCodePNG` value and write it to a file. This image can be scanned by the virtual MFA software program to create an account (as an alternative to manually entering the Base32StringSeed value). After you create the account in your virtual MFA program, get two sequential authentication codes and enter them in the last commands to link the virtual MFA device to the IAM user `Bob` and synchronize the account.**

```
$Device = New-IAMVirtualMFADevice -VirtualMFADeviceName BobsMFADevice
$BR = New-Object System.IO.BinaryReader($Device.QRCodePNG)
$BR.ReadBytes($BR.BaseStream.Length) | Set-Content -Encoding Byte -Path QRCode.png
```
**Output:**

```
 -- Pause here to scan PNG with virtual MFA program to register account. --

Enable-IAMMFADevice -SerialNumber $Device.SerialNumber -UserName Bob -AuthenticationCode1 123456 -AuthenticationCode2 789012
```
+  For API details, see [CreateVirtualMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Publish-IAMServerCertificate`
<a name="iam_UploadServerCertificate_powershell_4_topic"></a>

The following code example shows how to use `Publish-IAMServerCertificate`.

**Tools for PowerShell V4**
**Example 1: This example uploads a new server certificate to the IAM account. The files containing the certificate body, the private key, and (optionally) the certificate chain must all be PEM encoded. Note that the parameters require the actual content of the files rather than the file names. You must use the `-Raw` switch parameter to successfully process the file contents. **

```
Publish-IAMServerCertificate -ServerCertificateName MyTestCert -CertificateBody (Get-Content -Raw server.crt) -PrivateKey (Get-Content -Raw server.key)
```
**Output:**

```
Arn                   : arn:aws:iam::123456789012:server-certificate/MyTestCert
Expiration            : 1/14/2018 9:52:36 AM
Path                  : /
ServerCertificateId   : ASCAJIEXAMPLE7J7HQZYW
ServerCertificateName : MyTestCert
UploadDate            : 4/21/2015 11:14:16 AM
```
+  For API details, see [UploadServerCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Publish-IAMSigningCertificate`
<a name="iam_UploadSigningCertificate_powershell_4_topic"></a>

The following code example shows how to use `Publish-IAMSigningCertificate`.

**Tools for PowerShell V4**
**Example 1: This example uploads a new X.509 signing certificate and associates it with the IAM user named `Bob`. The file containing the certificate body is PEM encoded. The `CertificateBody` parameter requires the actual contents of the certificate file rather than the file name. You must use the `-Raw` switch parameter to successfully process the file.**

```
Publish-IAMSigningCertificate -UserName Bob -CertificateBody (Get-Content -Raw SampleSigningCert.pem)
```
**Output:**

```
CertificateBody : -----BEGIN CERTIFICATE-----
                  MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
                  VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
                  b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
                  BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
                  MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
                  VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
                  b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
                  YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
                  21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
                  rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
                  Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
                  nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
                  FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
                  NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=
                  -----END CERTIFICATE-----
CertificateId   : Y3EK7RMEXAMPLESV33FCEXAMPLEHMJLU
Status          : Active
UploadDate      : 4/20/2015 1:26:01 PM
UserName        : Bob
```
+  For API details, see [UploadSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-IAMGroupPolicy`
<a name="iam_AttachGroupPolicy_powershell_4_topic"></a>

The following code example shows how to use `Register-IAMGroupPolicy`.

**Tools for PowerShell V4**
**Example 1: This example attaches the customer managed policy named `TesterPolicy` to the IAM group `Testers`. The users in that group are immediately affected by the permissions defined in the default version of that policy.**

```
Register-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterPolicy
```
**Example 2: This example attaches the AWS managed policy named `AdministratorAccess` to the IAM group `Admins`. The users in that group are immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMGroupPolicy -GroupName Admins -PolicyArn arn:aws:iam::aws:policy/AdministratorAccess
```
+  For API details, see [AttachGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-IAMRolePolicy`
<a name="iam_AttachRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Register-IAMRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example attaches the AWS managed policy named `SecurityAudit` to the IAM role `CoSecurityAuditors`. The users who assume that role are immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMRolePolicy -RoleName CoSecurityAuditors -PolicyArn arn:aws:iam::aws:policy/SecurityAudit
```
+  For API details, see [AttachRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-IAMUserPolicy`
<a name="iam_AttachUserPolicy_powershell_4_topic"></a>

The following code example shows how to use `Register-IAMUserPolicy`.

**Tools for PowerShell V4**
**Example 1: This example attaches the AWS managed policy named `AmazonCognitoPowerUser` to the IAM user `Bob`. The user is immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMUserPolicy -UserName Bob -PolicyArn arn:aws:iam::aws:policy/AmazonCognitoPowerUser
```
+  For API details, see [AttachUserPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMAccessKey`
<a name="iam_DeleteAccessKey_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMAccessKey`.

**Tools for PowerShell V4**
**Example 1: This example deletes the AWS access key pair with the key ID `AKIAIOSFODNN7EXAMPLE` from the user named `Bob`.**

```
Remove-IAMAccessKey -AccessKeyId AKIAIOSFODNN7EXAMPLE -UserName Bob -Force
```
+  For API details, see [DeleteAccessKey](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMAccountAlias`
<a name="iam_DeleteAccountAlias_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMAccountAlias`.

**Tools for PowerShell V4**
**Example 1: This example removes the account alias from your AWS account. The user sign in page with the alias at https://mycompanyaws.signin.aws.amazon.com/console no longer works. You must instead use the original URL with your AWS account ID number at https://<accountidnumber>.signin.aws.amazon.com/console.**

```
Remove-IAMAccountAlias -AccountAlias mycompanyaws
```
+  For API details, see [DeleteAccountAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMAccountPasswordPolicy`
<a name="iam_DeleteAccountPasswordPolicy_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMAccountPasswordPolicy`.

**Tools for PowerShell V4**
**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**

```
Remove-IAMAccountPasswordPolicy
```
+  For API details, see [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMClientIDFromOpenIDConnectProvider`
<a name="iam_RemoveClientIdFromOpenIdConnectProvider_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMClientIDFromOpenIDConnectProvider`.

**Tools for PowerShell V4**
**Example 1: This example removes the client ID `My-TestApp-3` from the list of client IDs associated with the IAM OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`.**

```
Remove-IAMClientIDFromOpenIDConnectProvider -ClientID My-TestApp-3 -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com
```
+  For API details, see [RemoveClientIdFromOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMGroup`
<a name="iam_DeleteGroup_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMGroup`.

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM group named `MyTestGroup`. The first command removes any IAM users that are members of the group, and the second command deletes the IAM group. Both commands work without any prompts for confirmation.**

```
(Get-IAMGroup -GroupName MyTestGroup).Users | Remove-IAMUserFromGroup -GroupName MyTestGroup -Force
Remove-IAMGroup -GroupName MyTestGroup -Force
```
+  For API details, see [DeleteGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMGroupPolicy`
<a name="iam_DeleteGroupPolicy_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMGroupPolicy`.

**Tools for PowerShell V4**
**Example 1: This example removes the inline policy named `TesterPolicy` from the IAM group `Testers`. The users in that group immediately lose the permissions defined in that policy.**

```
Remove-IAMGroupPolicy -GroupName Testers -PolicyName TestPolicy
```
+  For API details, see [DeleteGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMInstanceProfile`
<a name="iam_DeleteInstanceProfile_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMInstanceProfile`.

**Tools for PowerShell V4**
**Example 1: This example deletes the EC2 instance profile named `MyAppInstanceProfile`. The first command detaches any roles from the instance profile, and then the second command deletes the instance profile.**

```
(Get-IAMInstanceProfile -InstanceProfileName MyAppInstanceProfile).Roles | Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyAppInstanceProfile
Remove-IAMInstanceProfile -InstanceProfileName MyAppInstanceProfile
```
+  For API details, see [DeleteInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMLoginProfile`
<a name="iam_DeleteLoginProfile_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMLoginProfile`.

**Tools for PowerShell V4**
**Example 1: This example deletes the login profile from the IAM user named `Bob`. This prevents the user from signing-in to the AWS console. It does not prevent the user from running any AWS CLI, PowerShell, or API calls using AWS access keys that might still be attached to the user account.**

```
Remove-IAMLoginProfile -UserName Bob
```
+  For API details, see [DeleteLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMOpenIDConnectProvider`
<a name="iam_DeleteOpenIdConnectProvider_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMOpenIDConnectProvider`.

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM OIDC provider that connects to the provider `example.oidcprovider.com`. Ensure that you update or delete any roles that reference this provider in the `Principal` element of the role's trust policy.**

```
Remove-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com
```
+  For API details, see [DeleteOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMPolicy`
<a name="iam_DeletePolicy_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMPolicy`.

**Tools for PowerShell V4**
**Example 1: This example deletes the policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`. Before you can delete the policy, you must first delete all versions except the default by running `Remove-IAMPolicyVersion`. You must also detach the policy from any IAM users, groups, or roles.**

```
Remove-IAMPolicy -PolicyArn arn:aws:iam::123456789012:policy/MySamplePolicy
```
**Example 2: This example deletes a policy by first deleting all the non-default policy versions, detaching it from all attached IAM entities, and finally deleting the policy itself. The first line retrieves the policy object. The second line retrieves all the policy versions that are not flagged as the default version into a collection and then deletes each policy in the collection. The third line retrieves all of the IAM users, groups, and roles to which the policy is attached. Lines four through six detach the policy from each attached entity. The last line uses this command to remove the managed policy as well as the remaining default version. The example includes the `-Force` switch parameter on any line that needs it to suppress prompts for confirmation.**

```
$pol = Get-IAMPolicy -PolicyArn arn:aws:iam::123456789012:policy/MySamplePolicy
Get-IAMPolicyVersions -PolicyArn $pol.Arn | where {-not $_.IsDefaultVersion} | Remove-IAMPolicyVersion -PolicyArn $pol.Arn -force
$attached = Get-IAMEntitiesForPolicy -PolicyArn $pol.Arn
$attached.PolicyGroups | Unregister-IAMGroupPolicy -PolicyArn $pol.arn
$attached.PolicyRoles | Unregister-IAMRolePolicy -PolicyArn $pol.arn
$attached.PolicyUsers | Unregister-IAMUserPolicy -PolicyArn $pol.arn
Remove-IAMPolicy $pol.Arn -Force
```
+  For API details, see [DeletePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMPolicyVersion`
<a name="iam_DeletePolicyVersion_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMPolicyVersion`.

**Tools for PowerShell V4**
**Example 1: This example deletes the version identified as `v2` from the policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.**

```
Remove-IAMPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MySamplePolicy -VersionID v2
```
**Example 2: This example deletes a policy by first deleting all non-default policy versions and then deleting the policy itself. The first line retrieves the policy object. The second line retrieves all of the policy versions that are not flagged as the default into a collection and then uses this command to delete each policy in the collection. The last line removes the policy itself as well as the remaining default version. Note that to successfully delete a managed policy, you must also detach the policy from any users, groups, or roles by using the `Unregister-IAMUserPolicy`, `Unregister-IAMGroupPolicy`, and `Unregister-IAMRolePolicy` commands. See the example for the `Remove-IAMPolicy` cmdlet. **

```
$pol = Get-IAMPolicy -PolicyArn arn:aws:iam::123456789012:policy/MySamplePolicy
Get-IAMPolicyVersions -PolicyArn $pol.Arn | where {-not $_.IsDefaultVersion} | Remove-IAMPolicyVersion -PolicyArn $pol.Arn -force
Remove-IAMPolicy -PolicyArn $pol.Arn -force
```
+  For API details, see [DeletePolicyVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMRole`
<a name="iam_DeleteRole_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMRole`.

**Tools for PowerShell V4**
**Example 1: This example deletes the role named `MyNewRole` from the current IAM account. Before you can delete the role you must first use the `Unregister-IAMRolePolicy` command to detach any managed policies. Inline policies are deleted with the role.**

```
Remove-IAMRole -RoleName MyNewRole
```
**Example 2: This example detaches any managed policies from the role named `MyNewRole` and then deletes the role. The first line retrieves any managed policies attached to the role as a collection and then detaches each policy in the collection from the role. The second line deletes the role itself. Inline policies are deleted along with the role.**

```
Get-IAMAttachedRolePolicyList -RoleName MyNewRole | Unregister-IAMRolePolicy -RoleName MyNewRole
Remove-IAMRole -RoleName MyNewRole
```
+  For API details, see [DeleteRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMRoleFromInstanceProfile`
<a name="iam_RemoveRoleFromInstanceProfile_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMRoleFromInstanceProfile`.

**Tools for PowerShell V4**
**Example 1: This example deletes the role named `MyNewRole` from the EC2 instance profile named `MyNewRole`. An instance profile that is created in the IAM console always has the same name as the role, as in this example. If you create them in the API or CLI, then they can have different names.**

```
Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyNewRole -RoleName MyNewRole -Force
```
+  For API details, see [RemoveRoleFromInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMRolePermissionsBoundary`
<a name="iam_DeleteRolePermissionsBoundary_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMRolePermissionsBoundary`.

**Tools for PowerShell V4**
**Example 1: This example shows how to remove the permission boundary attached to an IAM role.**

```
Remove-IAMRolePermissionsBoundary -RoleName MyRoleName
```
+  For API details, see [DeleteRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMRolePolicy`
<a name="iam_DeleteRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example deletes the inline policy `S3AccessPolicy` that is embedded in the IAM role `S3BackupRole`.**

```
Remove-IAMRolePolicy -PolicyName S3AccessPolicy -RoleName S3BackupRole
```
+  For API details, see [DeleteRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMRoleTag`
<a name="iam_UntagRole_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMRoleTag`.

**Tools for PowerShell V4**
**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"
```
+  For API details, see [UntagRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMSAMLProvider`
<a name="iam_DeleteSAMLProvider_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMSAMLProvider`.

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM SAML 2.0 provider whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`.**

```
Remove-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider
```
+  For API details, see [DeleteSAMLProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMServerCertificate`
<a name="iam_DeleteServerCertificate_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMServerCertificate`.

**Tools for PowerShell V4**
**Example 1: This example deletes the server certificate named `MyServerCert`.**

```
Remove-IAMServerCertificate -ServerCertificateName MyServerCert
```
+  For API details, see [DeleteServerCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMServiceLinkedRole`
<a name="iam_DeleteServiceLinkedRole_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMServiceLinkedRole`.

**Tools for PowerShell V4**
**Example 1: This example deleted the service linked role. Please note that if the service is still using this role, then this command results in a failure.**

```
Remove-IAMServiceLinkedRole -RoleName AWSServiceRoleForAutoScaling_RoleNameEndsWithThis
```
+  For API details, see [DeleteServiceLinkedRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMSigningCertificate`
<a name="iam_DeleteSigningCertificate_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMSigningCertificate`.

**Tools for PowerShell V4**
**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
```
+  For API details, see [DeleteSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMUser`
<a name="iam_DeleteUser_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMUser`.

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM user named `Bob`.**

```
Remove-IAMUser -UserName Bob
```
**Example 2: This example deletes the IAM user named `Theresa` along with any elements that must be deleted first.**

```
$name = "Theresa"

# find any groups and remove user from them
$groups = Get-IAMGroupForUser -UserName $name
foreach ($group in $groups) { Remove-IAMUserFromGroup -GroupName $group.GroupName -UserName $name -Force }

# find any inline policies and delete them
$inlinepols = Get-IAMUserPolicies -UserName $name
foreach ($pol in $inlinepols) { Remove-IAMUserPolicy -PolicyName $pol -UserName $name -Force}

# find any managed polices and detach them
$managedpols = Get-IAMAttachedUserPolicies -UserName $name
foreach ($pol in $managedpols) { Unregister-IAMUserPolicy -PolicyArn $pol.PolicyArn -UserName $name }

# find any signing certificates and delete them
$certs = Get-IAMSigningCertificate -UserName $name
foreach ($cert in $certs) { Remove-IAMSigningCertificate -CertificateId $cert.CertificateId -UserName $name -Force }

# find any access keys and delete them
$keys = Get-IAMAccessKey -UserName $name
foreach ($key in $keys) { Remove-IAMAccessKey -AccessKeyId $key.AccessKeyId -UserName $name -Force }

# delete the user's login profile, if one exists - note: need to use try/catch to suppress not found error
try { $prof = Get-IAMLoginProfile -UserName $name -ea 0 } catch { out-null }
if ($prof) { Remove-IAMLoginProfile -UserName $name -Force }

# find any MFA device, detach it, and if virtual, delete it.
$mfa = Get-IAMMFADevice -UserName $name
if ($mfa) {
    Disable-IAMMFADevice -SerialNumber $mfa.SerialNumber -UserName $name
    if ($mfa.SerialNumber -like "arn:*") { Remove-IAMVirtualMFADevice -SerialNumber $mfa.SerialNumber }
}

# finally, remove the user
Remove-IAMUser -UserName $name -Force
```
+  For API details, see [DeleteUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMUserFromGroup`
<a name="iam_RemoveUserFromGroup_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMUserFromGroup`.

**Tools for PowerShell V4**
**Example 1: This example removes the IAM user `Bob` from the group `Testers`. **

```
Remove-IAMUserFromGroup -GroupName Testers -UserName Bob
```
**Example 2: This example finds any groups of which IAM user `Theresa` is a member, and then removes `Theresa` from those groups.**

```
$groups = Get-IAMGroupForUser -UserName Theresa
foreach ($group in $groups) { Remove-IAMUserFromGroup -GroupName $group.GroupName -UserName Theresa -Force }
```
**Example 3: This example shows an alternate way of removing the IAM user `Bob` from the `Testers` group.**

```
Get-IAMGroupForUser -UserName Bob | Remove-IAMUserFromGroup -UserName Bob -GroupName Testers -Force
```
+  For API details, see [RemoveUserFromGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMUserPermissionsBoundary`
<a name="iam_DeleteUserPermissionsBoundary_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMUserPermissionsBoundary`.

**Tools for PowerShell V4**
**Example 1: This example shows how to remove the permission boundary attached to an IAM user.**

```
Remove-IAMUserPermissionsBoundary -UserName joe
```
+  For API details, see [DeleteUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMUserPolicy`
<a name="iam_DeleteUserPolicy_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMUserPolicy`.

**Tools for PowerShell V4**
**Example 1: This example deletes the inline policy named `AccessToEC2Policy` that is embedded in the IAM user named `Bob`.**

```
Remove-IAMUserPolicy -PolicyName AccessToEC2Policy -UserName Bob
```
**Example 2: This example finds all of the inline polices that are embedded in the IAM user named `Theresa` and then deletes them.**

```
$inlinepols = Get-IAMUserPolicies -UserName Theresa
foreach ($pol in $inlinepols) { Remove-IAMUserPolicy -PolicyName $pol -UserName Theresa -Force}
```
+  For API details, see [DeleteUserPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMUserTag`
<a name="iam_UntagUser_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMUserTag`.

**Tools for PowerShell V4**
**Example 1: This example removes the tag from the user named "joe" with tag key as "abac" and "xyzw". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMUserTag -UserName joe -TagKey "abac","xyzw"
```
+  For API details, see [UntagUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-IAMVirtualMFADevice`
<a name="iam_DeleteVirtualMfaDevice_powershell_4_topic"></a>

The following code example shows how to use `Remove-IAMVirtualMFADevice`.

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM virtual MFA device whose ARN is `arn:aws:iam::123456789012:mfa/bob`.**

```
Remove-IAMVirtualMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/bob
```
**Example 2: This example checks to see whether the IAM user Theresa has an MFA device assigned. If one is found, the device is disabled for the IAM user. If the device is virtual, then it is also deleted.**

```
$mfa = Get-IAMMFADevice -UserName Theresa
if ($mfa) {
    Disable-IAMMFADevice -SerialNumber $mfa.SerialNumber -UserName $name
    if ($mfa.SerialNumber -like "arn:*") { Remove-IAMVirtualMFADevice -SerialNumber $mfa.SerialNumber }
}
```
+  For API details, see [DeleteVirtualMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Request-IAMCredentialReport`
<a name="iam_GenerateCredentialReport_powershell_4_topic"></a>

The following code example shows how to use `Request-IAMCredentialReport`.

**Tools for PowerShell V4**
**Example 1: This example requests generation of a new report, which can be done every four hours. If the last report is still recent the State field reads `COMPLETE`. Use `Get-IAMCredentialReport` to view the completed report.**

```
Request-IAMCredentialReport
```
**Output:**

```
Description                                                    State
-----------                                                    -----
No report exists. Starting a new report generation task        STARTED
```
+  For API details, see [GenerateCredentialReport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Request-IAMServiceLastAccessedDetail`
<a name="iam_GenerateServiceLastAccessedDetails_powershell_4_topic"></a>

The following code example shows how to use `Request-IAMServiceLastAccessedDetail`.

**Tools for PowerShell V4**
**Example 1: This example is equivalent cmdlet of GenerateServiceLastAccessedDetails API. This provides with a job id which can be used in Get-IAMServiceLastAccessedDetail and Get-IAMServiceLastAccessedDetailWithEntity**

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser
```
+  For API details, see [GenerateServiceLastAccessedDetails](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-IAMDefaultPolicyVersion`
<a name="iam_SetDefaultPolicyVersion_powershell_4_topic"></a>

The following code example shows how to use `Set-IAMDefaultPolicyVersion`.

**Tools for PowerShell V4**
**Example 1: This example sets the `v2` version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyPolicy` as the default active version.**

```
Set-IAMDefaultPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MyPolicy -VersionId v2
```
+  For API details, see [SetDefaultPolicyVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-IAMRolePermissionsBoundary`
<a name="iam_PutRolePermissionsBoundary_powershell_4_topic"></a>

The following code example shows how to use `Set-IAMRolePermissionsBoundary`.

**Tools for PowerShell V4**
**Example 1: This example shows how to set the Permission boundary for a IAM Role. You can set AWS Managed policies or Custom policies as permission boundary.**

```
Set-IAMRolePermissionsBoundary -RoleName MyRoleName -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-IAMUserPermissionsBoundary`
<a name="iam_PutUserPermissionsBoundary_powershell_4_topic"></a>

The following code example shows how to use `Set-IAMUserPermissionsBoundary`.

**Tools for PowerShell V4**
**Example 1: This example shows how to set the Permission boundary for the user. You can set AWS Managed policies or Custom policies as permission boundary. **

```
Set-IAMUserPermissionsBoundary -UserName joe -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Sync-IAMMFADevice`
<a name="iam_ResyncMfaDevice_powershell_4_topic"></a>

The following code example shows how to use `Sync-IAMMFADevice`.

**Tools for PowerShell V4**
**Example 1: This example synchronizes the MFA device that is associated with the IAM user `Bob` and whose ARN is `arn:aws:iam::123456789012:mfa/bob` with an authenticator program that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/theresa -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Bob
```
**Example 2: This example synchronizes the IAM MFA device that is associated with the IAM user `Theresa` with a physical device that has the serial number `ABCD12345678` and that provided the two authentication codes.**

```
Sync-IAMMFADevice -SerialNumber ABCD12345678 -AuthenticationCode1 123456 -AuthenticationCode2 987654 -UserName Theresa
```
+  For API details, see [ResyncMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-IAMGroupPolicy`
<a name="iam_DetachGroupPolicy_powershell_4_topic"></a>

The following code example shows how to use `Unregister-IAMGroupPolicy`.

**Tools for PowerShell V4**
**Example 1: This example detaches the managed group policy whose ARN is `arn:aws:iam::123456789012:policy/TesterAccessPolicy` from the group named `Testers`.**

```
Unregister-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterAccessPolicy
```
**Example 2: This example finds all the managed policies that are attached to the group named `Testers` and detaches them from the group.**

```
Get-IAMAttachedGroupPolicies -GroupName Testers | Unregister-IAMGroupPolicy -Groupname Testers
```
+  For API details, see [DetachGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-IAMRolePolicy`
<a name="iam_DetachRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Unregister-IAMRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example detaches the managed group policy whose ARN is `arn:aws:iam::123456789012:policy/FederatedTesterAccessPolicy` from the role named `FedTesterRole`.**

```
Unregister-IAMRolePolicy -RoleName FedTesterRole -PolicyArn arn:aws:iam::123456789012:policy/FederatedTesterAccessPolicy
```
**Example 2: This example finds all of the managed policies that are attached to the role named `FedTesterRole` and detaches them from the role.**

```
Get-IAMAttachedRolePolicyList -RoleName FedTesterRole | Unregister-IAMRolePolicy -Rolename FedTesterRole
```
+  For API details, see [DetachRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-IAMUserPolicy`
<a name="iam_DetachUserPolicy_powershell_4_topic"></a>

The following code example shows how to use `Unregister-IAMUserPolicy`.

**Tools for PowerShell V4**
**Example 1: This example detaches the managed policy whose ARN is `arn:aws:iam::123456789012:policy/TesterPolicy` from the IAM user named `Bob`.**

```
Unregister-IAMUserPolicy -UserName Bob -PolicyArn arn:aws:iam::123456789012:policy/TesterPolicy
```
**Example 2: This example finds all the managed policies that are attached to the IAM user named `Theresa` and detaches those policies from the user.**

```
Get-IAMAttachedUserPolicyList -UserName Theresa | Unregister-IAMUserPolicy -Username Theresa
```
+  For API details, see [DetachUserPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMAccessKey`
<a name="iam_UpdateAccessKey_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMAccessKey`.

**Tools for PowerShell V4**
**Example 1: This example changes the status of the access key `AKIAIOSFODNN7EXAMPLE` for the IAM user named `Bob` to `Inactive`.**

```
Update-IAMAccessKey -UserName Bob -AccessKeyId AKIAIOSFODNN7EXAMPLE -Status Inactive
```
+  For API details, see [UpdateAccessKey](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMAccountPasswordPolicy`
<a name="iam_UpdateAccountPasswordPolicy_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMAccountPasswordPolicy`.

**Tools for PowerShell V4**
**Example 1: This example updates the password policy for the account with the specified settings. Note that any parameters that are not included in the command are not left unmodified. Instead, they are reset to default values.**

```
Update-IAMAccountPasswordPolicy -AllowUsersToChangePasswords $true -HardExpiry $false -MaxPasswordAge 90 -MinimumPasswordLength 8 -PasswordReusePrevention 20 -RequireLowercaseCharacters $true -RequireNumbers $true -RequireSymbols $true -RequireUppercaseCharacters $true
```
+  For API details, see [UpdateAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMAssumeRolePolicy`
<a name="iam_UpdateAssumeRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMAssumeRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example updates the IAM role named `ClientRole` with a new trust policy, the contents of which come from the file `ClientRolePolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the contents of the JSON file.**

```
Update-IAMAssumeRolePolicy -RoleName ClientRole -PolicyDocument (Get-Content -raw ClientRolePolicy.json)
```
+  For API details, see [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMGroup`
<a name="iam_UpdateGroup_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMGroup`.

**Tools for PowerShell V4**
**Example 1: This example renames the IAM group `Testers` to `AppTesters`.**

```
Update-IAMGroup -GroupName Testers -NewGroupName AppTesters
```
**Example 2: This example changes the path of the IAM group `AppTesters` to `/Org1/Org2/`. This changes the ARN for the group to `arn:aws:iam::123456789012:group/Org1/Org2/AppTesters`.**

```
Update-IAMGroup -GroupName AppTesters -NewPath /Org1/Org2/
```
+  For API details, see [UpdateGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMLoginProfile`
<a name="iam_UpdateLoginProfile_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMLoginProfile`.

**Tools for PowerShell V4**
**Example 1: This example sets a new temporary password for the IAM user `Bob`, and requires the user to change the password the next time the user signs in.**

```
Update-IAMLoginProfile -UserName Bob -Password "P@ssw0rd1234" -PasswordResetRequired $true
```
+  For API details, see [UpdateLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMOpenIDConnectProviderThumbprint`
<a name="iam_UpdateOpenIdConnectProviderThumbprint_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMOpenIDConnectProviderThumbprint`.

**Tools for PowerShell V4**
**Example 1: This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint. The OIDC provider shares the new value when the certificate that is associated with the provider changes.**

```
Update-IAMOpenIDConnectProviderThumbprint -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com -ThumbprintList 7359755EXAMPLEabc3060bce3EXAMPLEec4542a3
```
+  For API details, see [UpdateOpenIdConnectProviderThumbprint](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMRole`
<a name="iam_UpdateRole_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMRole`.

**Tools for PowerShell V4**
**Example 1: This example updates the role description and the maximum session duration value(in seconds) for which a role's session can be requested.**

```
Update-IAMRole -RoleName MyRoleName -Description "My testing role" -MaxSessionDuration 43200
```
+  For API details, see [UpdateRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMRoleDescription`
<a name="iam_UpdateRoleDescription_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMRoleDescription`.

**Tools for PowerShell V4**
**Example 1: This example updates the description of an IAM role in your account.**

```
Update-IAMRoleDescription -RoleName MyRoleName -Description "My testing role"
```
+  For API details, see [UpdateRoleDescription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMSAMLProvider`
<a name="iam_UpdateSamlProvider_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMSAMLProvider`.

**Tools for PowerShell V4**
**Example 1: This example updates the SAML provider in IAM whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFS` with a new SAML metadata document from the file `SAMLMetaData.xml`. Note that you must use the `-Raw` switch parameter to successfully process the contents of the JSON file.**

```
Update-IAMSAMLProvider -SAMLProviderArn arn:aws:iam::123456789012:saml-provider/SAMLADFS -SAMLMetadataDocument (Get-Content -Raw SAMLMetaData.xml)
```
+  For API details, see [UpdateSamlProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMServerCertificate`
<a name="iam_UpdateServerCertificate_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMServerCertificate`.

**Tools for PowerShell V4**
**Example 1: This example renames the certificate named `MyServerCertificate` to `MyRenamedServerCertificate`.**

```
Update-IAMServerCertificate -ServerCertificateName MyServerCertificate -NewServerCertificateName MyRenamedServerCertificate
```
**Example 2: This example moves the certificate named `MyServerCertificate` to the path /Org1/Org2/. This changes the ARN for the resource to `arn:aws:iam::123456789012:server-certificate/Org1/Org2/MyServerCertificate`.**

```
Update-IAMServerCertificate -ServerCertificateName MyServerCertificate -NewPath /Org1/Org2/
```
+  For API details, see [UpdateServerCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMSigningCertificate`
<a name="iam_UpdateSigningCertificate_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMSigningCertificate`.

**Tools for PowerShell V4**
**Example 1: This example updates the certificate that is associated with the IAM user named `Bob` and whose certificate ID si `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` to mark it as inactive.**

```
Update-IAMSigningCertificate -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU -UserName Bob -Status Inactive
```
+  For API details, see [UpdateSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-IAMUser`
<a name="iam_UpdateUser_powershell_4_topic"></a>

The following code example shows how to use `Update-IAMUser`.

**Tools for PowerShell V4**
**Example 1: This example renames the IAM user `Bob` to `Robert`.**

```
Update-IAMUser -UserName Bob -NewUserName Robert
```
**Example 2: This example changes the path of the IAM User `Bob` to `/Org1/Org2/`, which effectively changes the ARN for the user to `arn:aws:iam::123456789012:user/Org1/Org2/bob`.**

```
Update-IAMUser -UserName Bob -NewPath /Org1/Org2/
```
+  For API details, see [UpdateUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-IAMGroupPolicy`
<a name="iam_PutGroupPolicy_powershell_4_topic"></a>

The following code example shows how to use `Write-IAMGroupPolicy`.

**Tools for PowerShell V4**
**Example 1: This example creates an inline policy named `AppTesterPolicy` and embeds it in the IAM group `AppTesters`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes the file `apptesterpolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMGroupPolicy -GroupName AppTesters -PolicyName AppTesterPolicy -PolicyDocument (Get-Content -Raw apptesterpolicy.json)
```
+  For API details, see [PutGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-IAMRolePolicy`
<a name="iam_PutRolePolicy_powershell_4_topic"></a>

The following code example shows how to use `Write-IAMRolePolicy`.

**Tools for PowerShell V4**
**Example 1: This example creates an inline policy named `FedTesterRolePolicy` and embeds it in the IAM role `FedTesterRole`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes from the file `FedTesterPolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMRolePolicy -RoleName FedTesterRole -PolicyName FedTesterRolePolicy -PolicyDocument (Get-Content -Raw FedTesterPolicy.json)
```
+  For API details, see [PutRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-IAMUserPolicy`
<a name="iam_PutUserPolicy_powershell_4_topic"></a>

The following code example shows how to use `Write-IAMUserPolicy`.

**Tools for PowerShell V4**
**Example 1: This example creates an inline policy named `EC2AccessPolicy` and embeds it in the IAM user `Bob`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes from the file `EC2AccessPolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMUserPolicy -UserName Bob -PolicyName EC2AccessPolicy -PolicyDocument (Get-Content -Raw EC2AccessPolicy.json)
```
+  For API details, see [PutUserPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
