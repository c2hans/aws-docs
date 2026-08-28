---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_cloud9_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# AWS Cloud9 examples using Tools for PowerShell V5
<a name="powershell_cloud9_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS Cloud9.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-C9EnvironmentData`
<a name="cloud9_DescribeEnvironments_powershell_topic"></a>

The following code example shows how to use `Get-C9EnvironmentData`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified AWS Cloud9 development environments.**

```
Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX,1980b80e5f584920801c09086667f0EX
```
**Output:**

```
Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX
Description : Created from CodeStar.
Id          : 685f892f431b45c2b28cb69eadcdb0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ec2-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ec2

Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:1980b80e5f584920801c09086667f0EX
Description :
Id          : 1980b80e5f584920801c09086667f0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ssh-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ssh
```
**Example 2: This example gets information about the lifecycle status of the specified AWS Cloud9 development environment.**

```
(Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX).Lifecycle
```
**Output:**

```
FailureResource Reason Status
--------------- ------ ------
                       CREATED
```
+  For API details, see [DescribeEnvironments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-C9EnvironmentList`
<a name="cloud9_ListEnvironments_powershell_topic"></a>

The following code example shows how to use `Get-C9EnvironmentList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available AWS Cloud9 development environment identifiers.**

```
Get-C9EnvironmentList
```
**Output:**

```
685f892f431b45c2b28cb69eadcdb0EX
1980b80e5f584920801c09086667f0EX
```
+  For API details, see [ListEnvironments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-C9EnvironmentMembershipList`
<a name="cloud9_DescribeEnvironmentMemberships_powershell_topic"></a>

The following code example shows how to use `Get-C9EnvironmentMembershipList`.

**Tools for PowerShell V5**
**Example 1: This example gets information about environment members for the specified AWS Cloud9 development environment.**

```
Get-C9EnvironmentMembershipList -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-write
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX

EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : owner
UserArn       : arn:aws:iam::123456789012:user/MyDemoUser
UserId        : AIDAJ3LOROMOUXTBSU6EX
```
**Example 2: This example gets information about the owner of the specified AWS Cloud9 development environment.**

```
Get-C9EnvironmentMembershipList -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission owner
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : owner
UserArn       : arn:aws:iam::123456789012:user/MyDemoUser
UserId        : AIDAJ3LOROMOUXTBSU6EX
```
**Example 3: This example gets information about the specified environment member for multiple AWS Cloud9 development environments.**

```
Get-C9EnvironmentMembershipList -UserArn arn:aws:iam::123456789012:user/MyDemoUser
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/17/2018 7:48:14 PM
Permissions   : owner
UserArn       : arn:aws:iam::123456789012:user/MyDemoUser
UserId        : AIDAJ3LOROMOUXTBSU6EX

EnvironmentId : 1980b80e5f584920801c09086667f0EX
LastAccess    : 1/16/2018 11:21:24 PM
Permissions   : owner
UserArn       : arn:aws:iam::123456789012:user/MyDemoUser
UserId        : AIDAJ3LOROMOUXTBSU6EX
```
+  For API details, see [DescribeEnvironmentMemberships](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-C9EnvironmentStatus`
<a name="cloud9_DescribeEnvironmentStatus_powershell_topic"></a>

The following code example shows how to use `Get-C9EnvironmentStatus`.

**Tools for PowerShell V5**
**Example 1: This example gets status information for the specified AWS Cloud9 development environment.**

```
Get-C9EnvironmentStatus -EnvironmentId 349c86d4579e4e7298d500ff57a6b2EX
```
**Output:**

```
Message                     Status
-------                     ------
Environment is ready to use ready
```
+  For API details, see [DescribeEnvironmentStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-C9EnvironmentEC2`
<a name="cloud9_CreateEnvironmentEc2_powershell_topic"></a>

The following code example shows how to use `New-C9EnvironmentEC2`.

**Tools for PowerShell V5**
**Example 1: This example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.**

```
New-C9EnvironmentEC2 -Name my-demo-env -AutomaticStopTimeMinutes 60 -Description "My demonstration development environment." -InstanceType t2.micro -OwnerArn arn:aws:iam::123456789012:user/MyDemoUser -SubnetId subnet-d43a46EX
```
**Output:**

```
ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [CreateEnvironmentEc2](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-C9EnvironmentMembership`
<a name="cloud9_CreateEnvironmentMembership_powershell_topic"></a>

The following code example shows how to use `New-C9EnvironmentMembership`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified environment member to the specified AWS Cloud9 development environment.**

```
New-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-write
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-write
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [CreateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-C9Environment`
<a name="cloud9_DeleteEnvironment_powershell_topic"></a>

The following code example shows how to use `Remove-C9Environment`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.**

```
Remove-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-C9EnvironmentMembership`
<a name="cloud9_DeleteEnvironmentMembership_powershell_topic"></a>

The following code example shows how to use `Remove-C9EnvironmentMembership`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified environment member from the specified AWS Cloud9 development environment.**

```
Remove-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-C9Environment`
<a name="cloud9_UpdateEnvironment_powershell_topic"></a>

The following code example shows how to use `Update-C9Environment`.

**Tools for PowerShell V5**
**Example 1: This example changes the specified settings of the specified existing AWS Cloud9 development environment.**

```
Update-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Description "My changed demonstration development environment." -Name my-changed-demo-env
```
+  For API details, see [UpdateEnvironment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-C9EnvironmentMembership`
<a name="cloud9_UpdateEnvironmentMembership_powershell_topic"></a>

The following code example shows how to use `Update-C9EnvironmentMembership`.

**Tools for PowerShell V5**
**Example 1: This example changes the settings of the specified existing environment member for the specified AWS Cloud9 development environment.**

```
Update-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-only
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-only
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [UpdateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
