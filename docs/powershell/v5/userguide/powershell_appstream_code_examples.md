---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_appstream_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# WorkSpaces Applications examples using Tools for PowerShell V5
<a name="powershell_appstream_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with WorkSpaces Applications.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-APSResourceTag`
<a name="appstream_TagResource_powershell_topic"></a>

The following code example shows how to use `Add-APSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This sample adds a resource Tag to AppStream resource**

```
Add-APSResourceTag -ResourceArn arn:aws:appstream:us-east-1:123456789012:stack/SessionScriptTest -Tag @{StackState='Test'} -Select ^Tag
```
**Output:**

```
Name                           Value
----                           -----
StackState                     Test
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Copy-APSImage`
<a name="appstream_CopyImage_powershell_topic"></a>

The following code example shows how to use `Copy-APSImage`.

**Tools for PowerShell V5**
**Example 1: This sample copies an image to other region**

```
Copy-APSImage -DestinationImageName TestImageCopy -DestinationRegion us-west-2 -SourceImageName Powershell
```
**Output:**

```
TestImageCopy
```
+  For API details, see [CopyImage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-APSUSer`
<a name="appstream_DisableUser_powershell_topic"></a>

The following code example shows how to use `Disable-APSUSer`.

**Tools for PowerShell V5**
**Example 1: This sample disables an user in USERPOOL**

```
Disable-APSUser -AuthenticationType USERPOOL -UserName TestUser@lab.com
```
+  For API details, see [DisableUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-APSUser`
<a name="appstream_EnableUser_powershell_topic"></a>

The following code example shows how to use `Enable-APSUser`.

**Tools for PowerShell V5**
**Example 1: This sample enables a disabled user in USERPOOL**

```
Enable-APSUser -AuthenticationType USERPOOL -UserName TestUser@lab.com
```
+  For API details, see [EnableUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSAssociatedFleetList`
<a name="appstream_ListAssociatedFleets_powershell_topic"></a>

The following code example shows how to use `Get-APSAssociatedFleetList`.

**Tools for PowerShell V5**
**Example 1: This sample displays fleet associated with a stack**

```
Get-APSAssociatedFleetList -StackName PowershellStack
```
**Output:**

```
PowershellFleet
```
+  For API details, see [ListAssociatedFleets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSAssociatedStackList`
<a name="appstream_ListAssociatedStacks_powershell_topic"></a>

The following code example shows how to use `Get-APSAssociatedStackList`.

**Tools for PowerShell V5**
**Example 1: This sample displays stack associated with a fleet**

```
Get-APSAssociatedStackList -FleetName PowershellFleet
```
**Output:**

```
PowershellStack
```
+  For API details, see [ListAssociatedStacks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSDirectoryConfigList`
<a name="appstream_DescribeDirectoryConfigs_powershell_topic"></a>

The following code example shows how to use `Get-APSDirectoryConfigList`.

**Tools for PowerShell V5**
**Example 1: This sample displays Directory Configurations created in AppStream**

```
Get-APSDirectoryConfigList | Select DirectoryName, OrganizationalUnitDistinguishedNames, CreatedTime
```
**Output:**

```
DirectoryName OrganizationalUnitDistinguishedNames CreatedTime
------------- ------------------------------------ -----------
Test.com      {OU=AppStream,DC=Test,DC=com}    9/6/2019 10:56:40 AM
contoso.com   {OU=AppStream,OU=contoso,DC=contoso,DC=com}  8/9/2019 9:08:50 AM
```
+  For API details, see [DescribeDirectoryConfigs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSFleetList`
<a name="appstream_DescribeFleets_powershell_topic"></a>

The following code example shows how to use `Get-APSFleetList`.

**Tools for PowerShell V5**
**Example 1: This Sample displays details of a fleet**

```
Get-APSFleetList -Name Test
```
**Output:**

```
Arn                            : arn:aws:appstream:us-east-1:1234567890:fleet/Test
ComputeCapacityStatus          : Amazon.AppStream.Model.ComputeCapacityStatus
CreatedTime                    : 9/12/2019 5:00:45 PM
Description                    : Test
DisconnectTimeoutInSeconds     : 900
DisplayName                    : Test
DomainJoinInfo                 :
EnableDefaultInternetAccess    : False
FleetErrors                    : {}
FleetType                      : ON_DEMAND
IamRoleArn                     :
IdleDisconnectTimeoutInSeconds : 900
ImageArn                       : arn:aws:appstream:us-east-1:1234567890:image/Test
ImageName                      : Test
InstanceType                   : stream.standard.medium
MaxUserDurationInSeconds       : 57600
Name                           : Test
State                          : STOPPED
VpcConfig                      : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [DescribeFleets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSImageBuilderList`
<a name="appstream_DescribeImageBuilders_powershell_topic"></a>

The following code example shows how to use `Get-APSImageBuilderList`.

**Tools for PowerShell V5**
**Example 1: This Sample displays details of an ImageBuilder**

```
Get-APSImageBuilderList -Name TestImage
```
**Output:**

```
AccessEndpoints             : {}
AppstreamAgentVersion       : 06-19-2019
Arn                         : arn:aws:appstream:us-east-1:1234567890:image-builder/TestImage
CreatedTime                 : 1/14/2019 4:33:05 AM
Description                 :
DisplayName                 : TestImage
DomainJoinInfo              :
EnableDefaultInternetAccess : False
IamRoleArn                  :
ImageArn                    : arn:aws:appstream:us-east-1::image/Base-Image-Builder-05-02-2018
ImageBuilderErrors          : {}
InstanceType                : stream.standard.large
Name                        : TestImage
NetworkAccessConfiguration  : Amazon.AppStream.Model.NetworkAccessConfiguration
Platform                    : WINDOWS
State                       : STOPPED
StateChangeReason           :
VpcConfig                   : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [DescribeImageBuilders](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSImageList`
<a name="appstream_DescribeImages_powershell_topic"></a>

The following code example shows how to use `Get-APSImageList`.

**Tools for PowerShell V5**
**Example 1: This sample displays private AppStream Images**

```
Get-APSImageList -Type PRIVATE | select DisplayName, ImageBuilderName, Visibility, arn
```
**Output:**

```
DisplayName          ImageBuilderName      Visibility Arn
-----------          ----------------      ---------- ---
OfficeApps           OfficeApps            PRIVATE    arn:aws:appstream:us-east-1:123456789012:image/OfficeApps
SessionScriptV2      SessionScriptTest     PRIVATE    arn:aws:appstream:us-east-1:123456789012:image/SessionScriptV2
```
+  For API details, see [DescribeImages](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSImagePermission`
<a name="appstream_DescribeImagePermissions_powershell_topic"></a>

The following code example shows how to use `Get-APSImagePermission`.

**Tools for PowerShell V5**
**Example 1: This sample displays Image permissions on a shared AppStream Image**

```
Get-APSImagePermission -Name Powershell  | select SharedAccountId, @{n="AllowFleet";e={$_.ImagePermissions.AllowFleet}}, @{n="AllowImageBuilder";e={$_.ImagePermissions.AllowImageBuilder}}
```
**Output:**

```
SharedAccountId AllowFleet AllowImageBuilder
--------------- ---------- -----------------
123456789012          True              True
```
+  For API details, see [DescribeImagePermissions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSSessionList`
<a name="appstream_DescribeSessions_powershell_topic"></a>

The following code example shows how to use `Get-APSSessionList`.

**Tools for PowerShell V5**
**Example 1: This sample displays list of sessions to a fleet**

```
Get-APSSessionList -FleetName PowershellFleet -StackName PowershellStack
```
**Output:**

```
AuthenticationType         : API
ConnectionState            : CONNECTED
FleetName                  : PowershellFleet
Id                         : d8987c70-4394-4324-a396-2d485c26f2a2
MaxExpirationTime          : 12/27/2019 4:54:07 AM
NetworkAccessConfiguration : Amazon.AppStream.Model.NetworkAccessConfiguration
StackName                  : PowershellStack
StartTime                  : 12/26/2019 12:54:12 PM
State                      : ACTIVE
UserId                     : Test
```
+  For API details, see [DescribeSessions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSStackList`
<a name="appstream_DescribeStacks_powershell_topic"></a>

The following code example shows how to use `Get-APSStackList`.

**Tools for PowerShell V5**
**Example 1: This sample displays list of AppStream Stack**

```
Get-APSStackList | Select DisplayName, Arn, CreatedTime
```
**Output:**

```
DisplayName                   Arn                                                                          CreatedTime
-----------                   ---                                                                          -----------
PowershellStack               arn:aws:appstream:us-east-1:123456789012:stack/PowershellStack               4/24/2019 8:49:29 AM
SessionScriptTest             arn:aws:appstream:us-east-1:123456789012:stack/SessionScriptTest             9/12/2019 3:23:12 PM
```
+  For API details, see [DescribeStacks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSTagsForResourceList`
<a name="appstream_ListTagsForResource_powershell_topic"></a>

The following code example shows how to use `Get-APSTagsForResourceList`.

**Tools for PowerShell V5**
**Example 1: This sample displays tags on an AppStream resource**

```
Get-APSTagsForResourceList -ResourceArn arn:aws:appstream:us-east-1:123456789012:stack/SessionScriptTest
```
**Output:**

```
Key        Value
---        -----
StackState Test
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSUsageReportSubscription`
<a name="appstream_DescribeUsageReportSubscriptions_powershell_topic"></a>

The following code example shows how to use `Get-APSUsageReportSubscription`.

**Tools for PowerShell V5**
**Example 1: This sample displays AppStreamUsageReport configuration details**

```
Get-APSUsageReportSubscription
```
**Output:**

```
LastGeneratedReportDate S3BucketName                                   Schedule SubscriptionErrors
----------------------- ------------                                   -------- ------------------
1/1/0001 12:00:00 AM    appstream-logs-us-east-1-123456789012-sik1hnxe DAILY    {}
```
+  For API details, see [DescribeUsageReportSubscriptions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSUser`
<a name="appstream_DescribeUsers_powershell_topic"></a>

The following code example shows how to use `Get-APSUser`.

**Tools for PowerShell V5**
**Example 1: This Sample displays list of users with enabled status**

```
Get-APSUser -AuthenticationType USERPOOL | Select-Object UserName, AuthenticationType, Enabled
```
**Output:**

```
UserName                   AuthenticationType Enabled
--------                   ------------------ -------
foo1@contoso.com USERPOOL              True
foo2@contoso.com        USERPOOL              True
foo3@contoso.com    USERPOOL              True
foo4@contoso.com   USERPOOL              True
foo5@contoso.com         USERPOOL              True
```
+  For API details, see [DescribeUsers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-APSUserStackAssociation`
<a name="appstream_DescribeUserStackAssociations_powershell_topic"></a>

The following code example shows how to use `Get-APSUserStackAssociation`.

**Tools for PowerShell V5**
**Example 1: This sample displays list of users assigned to a stack**

```
Get-APSUserStackAssociation -StackName PowershellStack
```
**Output:**

```
AuthenticationType SendEmailNotification StackName       UserName
------------------ --------------------- ---------       --------
USERPOOL           False                 PowershellStack TestUser1@lab.com
USERPOOL           False                 PowershellStack TestUser2@lab.com
```
+  For API details, see [DescribeUserStackAssociations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSDirectoryConfig`
<a name="appstream_CreateDirectoryConfig_powershell_topic"></a>

The following code example shows how to use `New-APSDirectoryConfig`.

**Tools for PowerShell V5**
**Example 1: This sample creates a directory configuration in AppStream**

```
New-APSDirectoryConfig -ServiceAccountCredentials_AccountName contoso\ServiceAccount -ServiceAccountCredentials_AccountPassword MyPass -DirectoryName contoso.com -OrganizationalUnitDistinguishedName "OU=AppStream,OU=Contoso,DC=Contoso,DC=com"
```
**Output:**

```
CreatedTime            DirectoryName OrganizationalUnitDistinguishedNames        ServiceAccountCredentials
-----------            ------------- ------------------------------------        -------------------------
12/27/2019 11:00:30 AM contoso.com   {OU=AppStream,OU=Contoso,DC=Contoso,DC=com} Amazon.AppStream.Model.ServiceAccountCredentials
```
+  For API details, see [CreateDirectoryConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSFleet`
<a name="appstream_CreateFleet_powershell_topic"></a>

The following code example shows how to use `New-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample creates a new AppStream fleet**

```
New-APSFleet -ComputeCapacity_DesiredInstance 1 -InstanceType stream.standard.medium -Name TestFleet -DisplayName TestFleet -FleetType ON_DEMAND -EnableDefaultInternetAccess $True -VpcConfig_SubnetIds "subnet-123ce32","subnet-a1234cfd" -VpcConfig_SecurityGroupIds sg-4d012a34 -ImageName SessionScriptTest -Region us-west-2
```
**Output:**

```
Arn                            : arn:aws:appstream:us-west-2:123456789012:fleet/TestFleet
ComputeCapacityStatus          : Amazon.AppStream.Model.ComputeCapacityStatus
CreatedTime                    : 12/27/2019 11:24:42 AM
Description                    :
DisconnectTimeoutInSeconds     : 900
DisplayName                    : TestFleet
DomainJoinInfo                 :
EnableDefaultInternetAccess    : True
FleetErrors                    : {}
FleetType                      : ON_DEMAND
IamRoleArn                     :
IdleDisconnectTimeoutInSeconds : 0
ImageArn                       : arn:aws:appstream:us-west-2:123456789012:image/SessionScriptTest
ImageName                      : SessionScriptTest
InstanceType                   : stream.standard.medium
MaxUserDurationInSeconds       : 57600
Name                           : TestFleet
State                          : STOPPED
VpcConfig                      : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [CreateFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSImageBuilder`
<a name="appstream_CreateImageBuilder_powershell_topic"></a>

The following code example shows how to use `New-APSImageBuilder`.

**Tools for PowerShell V5**
**Example 1: This sample creates an Image Builder in AppStream**

```
New-APSImageBuilder -InstanceType stream.standard.medium -Name TestIB -DisplayName TestIB -ImageName AppStream-WinServer2012R2-12-12-2019 -EnableDefaultInternetAccess $True -VpcConfig_SubnetId subnet-a1234cfd -VpcConfig_SecurityGroupIds sg-2d012a34 -Region us-west-2
```
**Output:**

```
AccessEndpoints             : {}
AppstreamAgentVersion       : 12-16-2019
Arn                         : arn:aws:appstream:us-west-2:123456789012:image-builder/TestIB
CreatedTime                 : 12/27/2019 11:39:24 AM
Description                 :
DisplayName                 : TestIB
DomainJoinInfo              :
EnableDefaultInternetAccess : True
IamRoleArn                  :
ImageArn                    : arn:aws:appstream:us-west-2::image/AppStream-WinServer2012R2-12-12-2019
ImageBuilderErrors          : {}
InstanceType                : stream.standard.medium
Name                        : TestIB
NetworkAccessConfiguration  :
Platform                    : WINDOWS
State                       : PENDING
StateChangeReason           :
VpcConfig                   : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [CreateImageBuilder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSImageBuilderStreamingURL`
<a name="appstream_CreateImageBuilderStreamingURL_powershell_topic"></a>

The following code example shows how to use `New-APSImageBuilderStreamingURL`.

**Tools for PowerShell V5**
**Example 1: This sample creates an ImageBuilder streaming URL with validity of 2 hours**

```
New-APSImageBuilderStreamingURL -Name TestIB -Validity 7200 -Region us-west-2
```
**Output:**

```
Expires               StreamingURL
-------               ------------
12/27/2019 1:49:13 PM https://appstream2.us-west-2.aws.amazon.com/authenticate?parameters=eyJ0eXBlIjoiQURNSU4iLCJleHBpcmVzIjoiMTU3NzQ1NDU1MyIsImF3c0FjY291bnRJZCI6IjM5MzQwMzgxMTQwNyIsInVzZXJJZCI6ImFkbWluIiwiY2F
```
+  For API details, see [CreateImageBuilderStreamingURL](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSStack`
<a name="appstream_CreateStack_powershell_topic"></a>

The following code example shows how to use `New-APSStack`.

**Tools for PowerShell V5**
**Example 1: This sample creates a new AppStream Stack**

```
New-APSStack -Name TestStack -DisplayName TestStack -ApplicationSettings_Enabled $True -ApplicationSettings_SettingsGroup TestStack -Region us-west-2
```
**Output:**

```
AccessEndpoints     : {}
ApplicationSettings : Amazon.AppStream.Model.ApplicationSettingsResponse
Arn                 : arn:aws:appstream:us-west-2:123456789012:stack/TestStack
CreatedTime         : 12/27/2019 12:34:19 PM
Description         :
DisplayName         : TestStack
EmbedHostDomains    : {}
FeedbackURL         :
Name                : TestStack
RedirectURL         :
StackErrors         : {}
StorageConnectors   : {}
UserSettings        : {Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting}
```
+  For API details, see [CreateStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSStreamingURL`
<a name="appstream_CreateStreamingURL_powershell_topic"></a>

The following code example shows how to use `New-APSStreamingURL`.

**Tools for PowerShell V5**
**Example 1: This sample creates a streaming URL of Stack**

```
New-APSStreamingURL -StackName SessionScriptTest -FleetName SessionScriptNew -UserId TestUser
```
**Output:**

```
Expires                StreamingURL
-------                ------------
12/27/2019 12:43:37 PM https://appstream2.us-east-1.aws.amazon.com/authenticate?parameters=eyJ0eXBlIjoiRU5EX1VTRVIiLCJleHBpcmVzIjoiMTU3NzQ1MDYxNyIsImF3c0FjY291bnRJZCI6IjM5MzQwMzgxMTQwNyIsInVzZXJJZCI6IlRlc3RVc2
```
+  For API details, see [CreateStreamingURL](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSUsageReportSubscription`
<a name="appstream_CreateUsageReportSubscription_powershell_topic"></a>

The following code example shows how to use `New-APSUsageReportSubscription`.

**Tools for PowerShell V5**
**Example 1: This sample enables AppStream Usage Reports**

```
New-APSUsageReportSubscription
```
**Output:**

```
S3BucketName                                   Schedule
------------                                   --------
appstream-logs-us-east-1-123456789012-sik2hnxe DAILY
```
+  For API details, see [CreateUsageReportSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-APSUser`
<a name="appstream_CreateUser_powershell_topic"></a>

The following code example shows how to use `New-APSUser`.

**Tools for PowerShell V5**
**Example 1: This sample creates a user in USERPOOL**

```
New-APSUser -UserName Test@lab.com -AuthenticationType USERPOOL -FirstName 'kt' -LastName 'aws' -Select ^UserName
```
**Output:**

```
Test@lab.com
```
+  For API details, see [CreateUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-APSFleet`
<a name="appstream_AssociateFleet_powershell_topic"></a>

The following code example shows how to use `Register-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample registers fleet with a stack**

```
Register-APSFleet -StackName TestStack -FleetName TestFleet -Region us-west-2
```
+  For API details, see [AssociateFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-APSUserStackBatch`
<a name="appstream_BatchAssociateUserStack_powershell_topic"></a>

The following code example shows how to use `Register-APSUserStackBatch`.

**Tools for PowerShell V5**
**Example 1: This sample assigns stack to a user in USERPOOL**

```
Register-APSUserStackBatch -UserStackAssociation @{AuthenticationType="USERPOOL";SendEmailNotification=$False;StackName="PowershellStack";UserName="TestUser1@lab.com"}
```
+  For API details, see [BatchAssociateUserStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSDirectoryConfig`
<a name="appstream_DeleteDirectoryConfig_powershell_topic"></a>

The following code example shows how to use `Remove-APSDirectoryConfig`.

**Tools for PowerShell V5**
**Example 1: This sample removes AppStream Directory configuration**

```
Remove-APSDirectoryConfig -DirectoryName contoso.com
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSDirectoryConfig (DeleteDirectoryConfig)" on target "contoso.com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteDirectoryConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSFleet`
<a name="appstream_DeleteFleet_powershell_topic"></a>

The following code example shows how to use `Remove-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample removes deletes an AppStream fleet**

```
Remove-APSFleet -Name TestFleet -Region us-west-2
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSFleet (DeleteFleet)" on target "TestFleet".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSImage`
<a name="appstream_DeleteImage_powershell_topic"></a>

The following code example shows how to use `Remove-APSImage`.

**Tools for PowerShell V5**
**Example 1: This sample deletes an Image**

```
Remove-APSImage -Name TestImage -Region us-west-2
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSImage (DeleteImage)" on target "TestImage".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A

Applications                : {}
AppstreamAgentVersion       : LATEST
Arn                         : arn:aws:appstream:us-west-2:123456789012:image/TestImage
BaseImageArn                :
CreatedTime                 : 12/27/2019 1:34:10 PM
Description                 :
DisplayName                 : TestImage
ImageBuilderName            :
ImageBuilderSupported       : True
ImagePermissions            :
Name                        : TestImage
Platform                    : WINDOWS
PublicBaseImageReleasedDate : 6/12/2018 12:00:00 AM
State                       : AVAILABLE
StateChangeReason           :
Visibility                  : PRIVATE
```
+  For API details, see [DeleteImage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSImageBuilder`
<a name="appstream_DeleteImageBuilder_powershell_topic"></a>

The following code example shows how to use `Remove-APSImageBuilder`.

**Tools for PowerShell V5**
**Example 1: This sample deletes an ImageBuilder**

```
Remove-APSImageBuilder -Name TestIB -Region us-west-2
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSImageBuilder (DeleteImageBuilder)" on target "TestIB".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A

AccessEndpoints             : {}
AppstreamAgentVersion       : 12-16-2019
Arn                         : arn:aws:appstream:us-west-2:123456789012:image-builder/TestIB
CreatedTime                 : 12/27/2019 11:39:24 AM
Description                 :
DisplayName                 : TestIB
DomainJoinInfo              :
EnableDefaultInternetAccess : True
IamRoleArn                  :
ImageArn                    : arn:aws:appstream:us-west-2::image/AppStream-WinServer2012R2-12-12-2019
ImageBuilderErrors          : {}
InstanceType                : stream.standard.medium
Name                        : TestIB
NetworkAccessConfiguration  : Amazon.AppStream.Model.NetworkAccessConfiguration
Platform                    : WINDOWS
State                       : DELETING
StateChangeReason           :
VpcConfig                   : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [DeleteImageBuilder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSImagePermission`
<a name="appstream_DeleteImagePermissions_powershell_topic"></a>

The following code example shows how to use `Remove-APSImagePermission`.

**Tools for PowerShell V5**
**Example 1: This sample removes permissions of an Image**

```
Remove-APSImagePermission -Name Powershell -SharedAccountId 123456789012
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSImagePermission (DeleteImagePermissions)" on target "Powershell".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteImagePermissions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSResourceTag`
<a name="appstream_UntagResource_powershell_topic"></a>

The following code example shows how to use `Remove-APSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This sample removes a resource tag from AppStream resource**

```
Remove-APSResourceTag -ResourceArn arn:aws:appstream:us-east-1:123456789012:stack/SessionScriptTest -TagKey StackState
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSResourceTag (UntagResource)" on target "arn:aws:appstream:us-east-1:123456789012:stack/SessionScriptTest".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSStack`
<a name="appstream_DeleteStack_powershell_topic"></a>

The following code example shows how to use `Remove-APSStack`.

**Tools for PowerShell V5**
**Example 1: This sample deletes a Stack**

```
Remove-APSStack -Name TestStack -Region us-west-2
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSStack (DeleteStack)" on target "TestStack".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSUsageReportSubscription`
<a name="appstream_DeleteUsageReportSubscription_powershell_topic"></a>

The following code example shows how to use `Remove-APSUsageReportSubscription`.

**Tools for PowerShell V5**
**Example 1: This sample disables AppStream Usage Report subscription**

```
Remove-APSUsageReportSubscription
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSUsageReportSubscription (DeleteUsageReportSubscription)" on target "".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteUsageReportSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-APSUser`
<a name="appstream_DeleteUser_powershell_topic"></a>

The following code example shows how to use `Remove-APSUser`.

**Tools for PowerShell V5**
**Example 1: This sample deletes a user from USERPOOL**

```
Remove-APSUser -UserName TestUser@lab.com -AuthenticationType USERPOOL
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-APSUser (DeleteUser)" on target "TestUser@lab.com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```
+  For API details, see [DeleteUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Revoke-APSSession`
<a name="appstream_ExpireSession_powershell_topic"></a>

The following code example shows how to use `Revoke-APSSession`.

**Tools for PowerShell V5**
**Example 1: This sample revokes a session to AppStream fleet**

```
Revoke-APSSession -SessionId 6cd2f9a3-f948-4aa1-8014-8a7dcde14877
```
+  For API details, see [ExpireSession](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Start-APSFleet`
<a name="appstream_StartFleet_powershell_topic"></a>

The following code example shows how to use `Start-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample starts a fleet**

```
Start-APSFleet -Name PowershellFleet
```
+  For API details, see [StartFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Start-APSImageBuilder`
<a name="appstream_StartImageBuilder_powershell_topic"></a>

The following code example shows how to use `Start-APSImageBuilder`.

**Tools for PowerShell V5**
**Example 1: This sample starts an ImageBuilder**

```
Start-APSImageBuilder -Name TestImage
```
**Output:**

```
AccessEndpoints             : {}
AppstreamAgentVersion       : 06-19-2019
Arn                         : arn:aws:appstream:us-east-1:123456789012:image-builder/TestImage
CreatedTime                 : 1/14/2019 4:33:05 AM
Description                 :
DisplayName                 : TestImage
DomainJoinInfo              :
EnableDefaultInternetAccess : False
IamRoleArn                  :
ImageArn                    : arn:aws:appstream:us-east-1::image/Base-Image-Builder-05-02-2018
ImageBuilderErrors          : {}
InstanceType                : stream.standard.large
Name                        : TestImage
NetworkAccessConfiguration  : Amazon.AppStream.Model.NetworkAccessConfiguration
Platform                    : WINDOWS
State                       : PENDING
StateChangeReason           :
VpcConfig                   : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [StartImageBuilder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Stop-APSFleet`
<a name="appstream_StopFleet_powershell_topic"></a>

The following code example shows how to use `Stop-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample stops a fleet**

```
Stop-APSFleet -Name PowershellFleet
```
+  For API details, see [StopFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Stop-APSImageBuilder`
<a name="appstream_StopImageBuilder_powershell_topic"></a>

The following code example shows how to use `Stop-APSImageBuilder`.

**Tools for PowerShell V5**
**Example 1: This sample stops an ImageBuilder**

```
Stop-APSImageBuilder -Name TestImage
```
**Output:**

```
AccessEndpoints             : {}
AppstreamAgentVersion       : 06-19-2019
Arn                         : arn:aws:appstream:us-east-1:123456789012:image-builder/TestImage
CreatedTime                 : 1/14/2019 4:33:05 AM
Description                 :
DisplayName                 : TestImage
DomainJoinInfo              :
EnableDefaultInternetAccess : False
IamRoleArn                  :
ImageArn                    : arn:aws:appstream:us-east-1::image/Base-Image-Builder-05-02-2018
ImageBuilderErrors          : {}
InstanceType                : stream.standard.large
Name                        : TestImage
NetworkAccessConfiguration  : Amazon.AppStream.Model.NetworkAccessConfiguration
Platform                    : WINDOWS
State                       : STOPPING
StateChangeReason           :
VpcConfig                   : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [StopImageBuilder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-APSFleet`
<a name="appstream_DisassociateFleet_powershell_topic"></a>

The following code example shows how to use `Unregister-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample unregisters a fleet from stack**

```
Unregister-APSFleet -StackName TestStack -FleetName TestFleet -Region us-west-2
```
+  For API details, see [DisassociateFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-APSUserStackBatch`
<a name="appstream_BatchDisassociateUserStack_powershell_topic"></a>

The following code example shows how to use `Unregister-APSUserStackBatch`.

**Tools for PowerShell V5**
**Example 1: This sample removes an user from an assigned Stack**

```
Unregister-APSUserStackBatch -UserStackAssociation @{AuthenticationType="USERPOOL";SendEmailNotification=$False;StackName="PowershellStack";UserName="TestUser1@lab.com"}
```
+  For API details, see [BatchDisassociateUserStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-APSDirectoryConfig`
<a name="appstream_UpdateDirectoryConfig_powershell_topic"></a>

The following code example shows how to use `Update-APSDirectoryConfig`.

**Tools for PowerShell V5**
**Example 1: This sample updates the Directory configuration created in AppStream**

```
Update-APSDirectoryConfig -ServiceAccountCredentials_AccountName contoso\ServiceAccount -ServiceAccountCredentials_AccountPassword MyPass@1$@# -DirectoryName contoso.com -OrganizationalUnitDistinguishedName "OU=AppStreamNew,OU=Contoso,DC=Contoso,DC=com"
```
**Output:**

```
CreatedTime           DirectoryName OrganizationalUnitDistinguishedNames           ServiceAccountCredentials
-----------           ------------- ------------------------------------           -------------------------
12/27/2019 3:50:02 PM contoso.com   {OU=AppStreamNew,OU=Contoso,DC=Contoso,DC=com} Amazon.AppStream.Model.ServiceAccountCredentials
```
+  For API details, see [UpdateDirectoryConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-APSFleet`
<a name="appstream_UpdateFleet_powershell_topic"></a>

The following code example shows how to use `Update-APSFleet`.

**Tools for PowerShell V5**
**Example 1: This sample updates properties of a fleet**

```
Update-APSFleet -Name PowershellFleet -EnableDefaultInternetAccess $True -DisconnectTimeoutInSecond 950
```
**Output:**

```
Arn                            : arn:aws:appstream:us-east-1:123456789012:fleet/PowershellFleet
ComputeCapacityStatus          : Amazon.AppStream.Model.ComputeCapacityStatus
CreatedTime                    : 4/24/2019 8:39:41 AM
Description                    : PowershellFleet
DisconnectTimeoutInSeconds     : 950
DisplayName                    : PowershellFleet
DomainJoinInfo                 :
EnableDefaultInternetAccess    : True
FleetErrors                    : {}
FleetType                      : ON_DEMAND
IamRoleArn                     :
IdleDisconnectTimeoutInSeconds : 900
ImageArn                       : arn:aws:appstream:us-east-1:123456789012:image/Powershell
ImageName                      : Powershell
InstanceType                   : stream.standard.medium
MaxUserDurationInSeconds       : 57600
Name                           : PowershellFleet
State                          : STOPPED
VpcConfig                      : Amazon.AppStream.Model.VpcConfig
```
+  For API details, see [UpdateFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-APSImagePermission`
<a name="appstream_UpdateImagePermissions_powershell_topic"></a>

The following code example shows how to use `Update-APSImagePermission`.

**Tools for PowerShell V5**
**Example 1: This sample shares an AppStream Image with other account**

```
Update-APSImagePermission -Name Powershell -SharedAccountId 123456789012 -ImagePermissions_AllowFleet $True -ImagePermissions_AllowImageBuilder $True
```
+  For API details, see [UpdateImagePermissions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-APSStack`
<a name="appstream_UpdateStack_powershell_topic"></a>

The following code example shows how to use `Update-APSStack`.

**Tools for PowerShell V5**
**Example 1: This sample updates(enables) Application settings persistence and Home Folders on a Stack **

```
Update-APSStack -Name PowershellStack -ApplicationSettings_Enabled $True -ApplicationSettings_SettingsGroup PowershellStack -StorageConnector @{ConnectorType="HOMEFOLDERS"}
```
**Output:**

```
AccessEndpoints     : {}
ApplicationSettings : Amazon.AppStream.Model.ApplicationSettingsResponse
Arn                 : arn:aws:appstream:us-east-1:123456789012:stack/PowershellStack
CreatedTime         : 4/24/2019 8:49:29 AM
Description         : PowershellStack
DisplayName         : PowershellStack
EmbedHostDomains    : {}
FeedbackURL         :
Name                : PowershellStack
RedirectURL         :
StackErrors         : {}
StorageConnectors   : {Amazon.AppStream.Model.StorageConnector, Amazon.AppStream.Model.StorageConnector}
UserSettings        : {Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting, Amazon.AppStream.Model.UserSetting}
```
+  For API details, see [UpdateStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
