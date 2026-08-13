---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_directory-service_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Directory Service examples using Tools for PowerShell V5
<a name="powershell_directory-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Directory Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-DSIpRoute`
<a name="directory-service_AddIpRoutes_powershell_topic"></a>

The following code example shows how to use `Add-DSIpRoute`.

**Tools for PowerShell V5**
**Example 1: This command removes the Resource Tag assigned to the specified Directory-id**

```
Add-DSIpRoute -DirectoryId d-123456ijkl -IpRoute @{CidrIp ="203.0.113.5/32"} -UpdateSecurityGroupForDirectoryController $true
```
+  For API details, see [AddIpRoutes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Add-DSResourceTag`
<a name="directory-service_AddTagsToResource_powershell_topic"></a>

The following code example shows how to use `Add-DSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This command adds the Resource Tag to the specified Directory-id**

```
Add-DSResourceTag -ResourceId d-123456ijkl -Tag @{Key="myTag"; Value="mytgValue"}
```
+  For API details, see [AddTagsToResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Approve-DSTrust`
<a name="directory-service_VerifyTrust_powershell_topic"></a>

The following code example shows how to use `Approve-DSTrust`.

**Tools for PowerShell V5**
**Example 1: This example calls the AWS Directory Service VerifyTrust API operation for specified Trustid.**

```
Approve-DSTrust -TrustId t-9067157123
```
+  For API details, see [VerifyTrust](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Confirm-DSSharedDirectory`
<a name="directory-service_AcceptSharedDirectory_powershell_topic"></a>

The following code example shows how to use `Confirm-DSSharedDirectory`.

**Tools for PowerShell V5**
**Example 1: This example accepts a directory sharing request sent from the directory owner AWS account.**

```
Confirm-DSSharedDirectory -SharedDirectoryId d-9067012345
```
**Output:**

```
CreatedDateTime     : 12/30/2019 4:20:27 AM
LastUpdatedDateTime : 12/30/2019 4:21:40 AM
OwnerAccountId      : 123456781234
OwnerDirectoryId    : d-123456ijkl
SharedAccountId     : 123456784321
SharedDirectoryId   : d-9067012345
ShareMethod         :
ShareNotes          : This is test sharing
ShareStatus         : Sharing
```
+  For API details, see [AcceptSharedDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Connect-DSDirectory`
<a name="directory-service_ConnectDirectory_powershell_topic"></a>

The following code example shows how to use `Connect-DSDirectory`.

**Tools for PowerShell V5**
**Example 1: This example creates an AD Connector to connect to an on-premises directory.**

```
Connect-DSDirectory -Name contoso.com -ConnectSettings_CustomerUserName Administrator -Password $Password -ConnectSettings_CustomerDnsIp 172.31.36.96 -ShortName CONTOSO -Size Small -ConnectSettings_VpcId vpc-123459da -ConnectSettings_SubnetId subnet-1234ccaa, subnet-5678ffbb
```
+  For API details, see [ConnectDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Deny-DSSharedDirectory`
<a name="directory-service_RejectSharedDirectory_powershell_topic"></a>

The following code example shows how to use `Deny-DSSharedDirectory`.

**Tools for PowerShell V5**
**Example 1: This example rejects a directory sharing request that was sent from the directory owner account. **

```
Deny-DSSharedDirectory -SharedDirectoryId d-9067012345
```
**Output:**

```
d-9067012345
```
+  For API details, see [RejectSharedDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-DSDirectoryShare`
<a name="directory-service_UnshareDirectory_powershell_topic"></a>

The following code example shows how to use `Disable-DSDirectoryShare`.

**Tools for PowerShell V5**
**Example 1: This example stops the directory sharing between the directory owner and consumer account. **

```
Disable-DSDirectoryShare -DirectoryId d-123456ijkl -UnshareTarget_Id 123456784321 -UnshareTarget_Type ACCOUNT
```
**Output:**

```
d-9067012345
```
+  For API details, see [UnshareDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-DSLDAPS`
<a name="directory-service_DisableLDAPS_powershell_topic"></a>

The following code example shows how to use `Disable-DSLDAPS`.

**Tools for PowerShell V5**
**Example 1: This example deactivates LDAP secure calls for the specified directory.**

```
Disable-DSLDAPS -DirectoryId d-123456ijkl -Type Client
```
+  For API details, see [DisableLDAPS](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-DSRadius`
<a name="directory-service_DisableRadius_powershell_topic"></a>

The following code example shows how to use `Disable-DSRadius`.

**Tools for PowerShell V5**
**Example 1: This example disables RADIUS server configured for an AD Connector or Microsoft AD directory.**

```
Disable-DSRadius -DirectoryId d-123456ijkl
```
+  For API details, see [DisableRadius](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-DSSso`
<a name="directory-service_DisableSso_powershell_topic"></a>

The following code example shows how to use `Disable-DSSso`.

**Tools for PowerShell V5**
**Example 1: This example disables single sign-on for a directory.**

```
Disable-DSSso -DirectoryId d-123456ijkl
```
+  For API details, see [DisableSso](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-DSDirectoryShare`
<a name="directory-service_ShareDirectory_powershell_topic"></a>

The following code example shows how to use `Enable-DSDirectoryShare`.

**Tools for PowerShell V5**
**Example 1: This example shares a specified directory in your AWS account with another AWS Account using Handshake method. **

```
Enable-DSDirectoryShare -DirectoryId d-123456ijkl -ShareTarget_Id 123456784321 -ShareMethod HANDSHAKE -ShareTarget_Type ACCOUNT
```
**Output:**

```
d-9067012345
```
+  For API details, see [ShareDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-DSLDAPS`
<a name="directory-service_EnableLDAPS_powershell_topic"></a>

The following code example shows how to use `Enable-DSLDAPS`.

**Tools for PowerShell V5**
**Example 1: This example activates the switch for the specific directory to always use LDAP secure calls.**

```
Enable-DSLDAPS -DirectoryId d-123456ijkl -Type Client
```
+  For API details, see [EnableLDAPS](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-DSRadius`
<a name="directory-service_EnableRadius_powershell_topic"></a>

The following code example shows how to use `Enable-DSRadius`.

**Tools for PowerShell V5**
**Example 1: This example enables multi-factor authentication (MFA) with the provided RADIUS server configuration for an AD Connector or Microsoft AD directory.**

```
Enable-DSRadius -DirectoryId d-123456ijkl
-RadiusSettings_AuthenticationProtocol PAP
-RadiusSettings_DisplayLabel Radius
-RadiusSettings_RadiusPort 1812
-RadiusSettings_RadiusRetry 4
-RadiusSettings_RadiusServer 10.4.185.113
-RadiusSettings_RadiusTimeout 50
-RadiusSettings_SharedSecret wJalrXUtnFEMI
```
+  For API details, see [EnableRadius](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-DSSso`
<a name="directory-service_EnableSso_powershell_topic"></a>

The following code example shows how to use `Enable-DSSso`.

**Tools for PowerShell V5**
**Example 1: This example enables single sign-on for a directory. **

```
Enable-DSSso -DirectoryId d-123456ijkl
```
+  For API details, see [EnableSso](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSCertificate`
<a name="directory-service_DescribeCertificate_powershell_topic"></a>

The following code example shows how to use `Get-DSCertificate`.

**Tools for PowerShell V5**
**Example 1: This example displays information about the certificate registered for a secured LDAP connection.**

```
Get-DSCertificate -DirectoryId d-123456ijkl -CertificateId c-906731e34f
```
**Output:**

```
CertificateId      : c-906731e34f
CommonName         : contoso-EC2AMAZ-CTGG2NM-CA
ExpiryDateTime     : 4/15/2025 6:34:15 PM
RegisteredDateTime : 4/15/2020 6:38:56 PM
State              : Registered
StateReason        : Certificate registered successfully.
```
+  For API details, see [DescribeCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSCertificateList`
<a name="directory-service_ListCertificates_powershell_topic"></a>

The following code example shows how to use `Get-DSCertificateList`.

**Tools for PowerShell V5**
**Example 1: This example lists all the certificates registered for a secured LDAP connection for specified directory.**

```
Get-DSCertificateList -DirectoryId d-123456ijkl
```
**Output:**

```
CertificateId CommonName                 ExpiryDateTime       State
------------- ----------                 --------------       -----
c-906731e34f  contoso-EC2AMAZ-CTGG2NM-CA 4/15/2025 6:34:15 PM Registered
```
+  For API details, see [ListCertificates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSConditionalForwarder`
<a name="directory-service_DescribeConditionalForwarders_powershell_topic"></a>

The following code example shows how to use `Get-DSConditionalForwarder`.

**Tools for PowerShell V5**
**Example 1: This command gets all configured Conditional Forwarders of given Directory-id. **

```
Get-DSConditionalForwarder -DirectoryId d-123456ijkl
```
**Output:**

```
DnsIpAddrs      RemoteDomainName ReplicationScope
----------      ---------------- ----------------
{172.31.77.239} contoso.com      Domain
```
+  For API details, see [DescribeConditionalForwarders](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSDirectory`
<a name="directory-service_DescribeDirectories_powershell_topic"></a>

The following code example shows how to use `Get-DSDirectory`.

**Tools for PowerShell V5**
**Example 1: This command Obtains information about the directories that belong to this account.**

```
Get-DSDirectory | Select-Object DirectoryId, Name, DnsIpAddrs, Type
```
**Output:**

```
DirectoryId  Name           DnsIpAddrs                     Type
-----------  ----           ----------                     ----
d-123456abcd abcd.example.com {172.31.74.189, 172.31.13.145} SimpleAD
d-123456efgh wifi.example.com {172.31.16.108, 172.31.10.56}  ADConnector
d-123456ijkl lan2.example.com {172.31.10.56, 172.31.16.108}  MicrosoftAD
```
+  For API details, see [DescribeDirectories](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSDirectoryLimit`
<a name="directory-service_GetDirectoryLimits_powershell_topic"></a>

The following code example shows how to use `Get-DSDirectoryLimit`.

**Tools for PowerShell V5**
**Example 1: This example dislpays the directory limit information for the us-east-1 region. **

```
Get-DSDirectoryLimit -Region us-east-1
```
**Output:**

```
CloudOnlyDirectoriesCurrentCount : 1
CloudOnlyDirectoriesLimit        : 10
CloudOnlyDirectoriesLimitReached : False
CloudOnlyMicrosoftADCurrentCount : 1
CloudOnlyMicrosoftADLimit        : 20
CloudOnlyMicrosoftADLimitReached : False
ConnectedDirectoriesCurrentCount : 1
ConnectedDirectoriesLimit        : 10
```
+  For API details, see [GetDirectoryLimits](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSDomainControllerList`
<a name="directory-service_DescribeDomainControllers_powershell_topic"></a>

The following code example shows how to use `Get-DSDomainControllerList`.

**Tools for PowerShell V5**
**Example 1: This command gets the detailed list of Domain Controllers launched for mentioned directory-id**

```
Get-DSDomainControllerList -DirectoryId d-123456ijkl
```
**Output:**

```
AvailabilityZone          : us-east-1b
DirectoryId               : d-123456ijkl
DnsIpAddr                 : 172.31.16.108
DomainControllerId        : dc-1234567aa6
LaunchTime                : 4/4/2019 4:53:43 AM
Status                    : Active
StatusLastUpdatedDateTime : 4/24/2019 1:37:54 PM
StatusReason              :
SubnetId                  : subnet-1234kkaa
VpcId                     : vpc-123459d

AvailabilityZone          : us-east-1d
DirectoryId               : d-123456ijkl
DnsIpAddr                 : 172.31.10.56
DomainControllerId        : dc-1234567aa7
LaunchTime                : 4/4/2019 4:53:43 AM
Status                    : Active
StatusLastUpdatedDateTime : 4/4/2019 5:14:31 AM
StatusReason              :
SubnetId                  : subnet-5678ffbb
VpcId                     : vpc-123459d
```
+  For API details, see [DescribeDomainControllers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSEventTopic`
<a name="directory-service_DescribeEventTopics_powershell_topic"></a>

The following code example shows how to use `Get-DSEventTopic`.

**Tools for PowerShell V5**
**Example 1: This command shows information of configured SNS Topic for notification while directory status changes.**

```
Get-DSEventTopic -DirectoryId d-123456ijkl
```
**Output:**

```
CreatedDateTime : 12/13/2019 11:15:32 AM
DirectoryId     : d-123456ijkl
Status          : Registered
TopicArn        : arn:aws:sns:us-east-1:123456781234:snstopicname
TopicName       : snstopicname
```
+  For API details, see [DescribeEventTopics](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSIpRouteList`
<a name="directory-service_ListIpRoutes_powershell_topic"></a>

The following code example shows how to use `Get-DSIpRouteList`.

**Tools for PowerShell V5**
**Example 1: This command gets the public IP address blocks configured in Directory IP Routing**

```
Get-DSIpRouteList -DirectoryId d-123456ijkl
```
**Output:**

```
AddedDateTime       : 12/13/2019 12:27:22 PM
CidrIp              : 203.0.113.5/32
Description         : Public IP of On-Prem DNS Server
DirectoryId         : d-123456ijkl
IpRouteStatusMsg    : Added
IpRouteStatusReason :
```
+  For API details, see [ListIpRoutes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSLDAPSSetting`
<a name="directory-service_DescribeLDAPSSettings_powershell_topic"></a>

The following code example shows how to use `Get-DSLDAPSSetting`.

**Tools for PowerShell V5**
**Example 1: This example describes the status of LDAP security for the specified directory.**

```
Get-DSLDAPSSetting -DirectoryId d-123456ijkl
```
**Output:**

```
LastUpdatedDateTime  LDAPSStatus LDAPSStatusReason
-------------------  ----------- -----------------
4/15/2020 6:51:03 PM Enabled     LDAPS is enabled successfully.
```
+  For API details, see [DescribeLDAPSSettings](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSLogSubscriptionList`
<a name="directory-service_ListLogSubscriptions_powershell_topic"></a>

The following code example shows how to use `Get-DSLogSubscriptionList`.

**Tools for PowerShell V5**
**Example 1: This command gets the log subscriptions information of specified directory-id **

```
Get-DSLogSubscriptionList -DirectoryId d-123456ijkl
```
**Output:**

```
DirectoryId  LogGroupName                                        SubscriptionCreatedDateTime
-----------  ------------                                        ---------------------------
d-123456ijkl /aws/directoryservice/d-123456ijkl-lan2.example.com 12/14/2019 9:05:23 AM
```
+  For API details, see [ListLogSubscriptions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSResourceTag`
<a name="directory-service_ListTagsForResource_powershell_topic"></a>

The following code example shows how to use `Get-DSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This command gets all the Tags of specified Directory.**

```
Get-DSResourceTag -ResourceId d-123456ijkl
```
**Output:**

```
Key   Value
---   -----
myTag myTagValue
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSSchemaExtension`
<a name="directory-service_ListSchemaExtensions_powershell_topic"></a>

The following code example shows how to use `Get-DSSchemaExtension`.

**Tools for PowerShell V5**
**Example 1: This example lists all schema extensions applied to a Microsoft AD Directory.**

```
Get-DSSchemaExtension -DirectoryId d-123456ijkl
```
**Output:**

```
Description                 : ManagedADSchemaExtension
DirectoryId                 : d-123456ijkl
EndDateTime                 : 4/12/2020 10:30:49 AM
SchemaExtensionId           : e-9067306643
SchemaExtensionStatus       : Completed
SchemaExtensionStatusReason : Schema updates are complete.
StartDateTime               : 4/12/2020 10:28:42 AM
```
+  For API details, see [ListSchemaExtensions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSSharedDirectory`
<a name="directory-service_DescribeSharedDirectories_powershell_topic"></a>

The following code example shows how to use `Get-DSSharedDirectory`.

**Tools for PowerShell V5**
**Example 1: This example gets the shared directories of your AWS Account**

```
Get-DSSharedDirectory -OwnerDirectoryId d-123456ijkl -SharedDirectoryId d-9067012345
```
**Output:**

```
CreatedDateTime     : 12/30/2019 4:34:37 AM
LastUpdatedDateTime : 12/30/2019 4:35:22 AM
OwnerAccountId      : 123456781234
OwnerDirectoryId    : d-123456ijkl
SharedAccountId     : 123456784321
SharedDirectoryId   : d-9067012345
ShareMethod         : HANDSHAKE
ShareNotes          : This is a test Sharing
ShareStatus         : Shared
```
+  For API details, see [DescribeSharedDirectories](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSSnapshot`
<a name="directory-service_DescribeSnapshots_powershell_topic"></a>

The following code example shows how to use `Get-DSSnapshot`.

**Tools for PowerShell V5**
**Example 1: This command gets information about the specified directory snapshots that belong to this account.**

```
Get-DSSnapshot -DirectoryId d-123456ijkl
```
**Output:**

```
DirectoryId : d-123456ijkl
Name        :
SnapshotId  : s-9064bd1234
StartTime   : 12/13/2019 6:33:01 PM
Status      : Completed
Type        : Auto

DirectoryId : d-123456ijkl
Name        :
SnapshotId  : s-9064bb4321
StartTime   : 12/9/2019 9:48:11 PM
Status      : Completed
Type        : Auto
```
+  For API details, see [DescribeSnapshots](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSSnapshotLimit`
<a name="directory-service_GetSnapshotLimits_powershell_topic"></a>

The following code example shows how to use `Get-DSSnapshotLimit`.

**Tools for PowerShell V5**
**Example 1: This command gets the manual snapshot limits for a specified directory.**

```
Get-DSSnapshotLimit -DirectoryId d-123456ijkl
```
**Output:**

```
ManualSnapshotsCurrentCount ManualSnapshotsLimit ManualSnapshotsLimitReached
--------------------------- -------------------- ---------------------------
0                           5                    False
```
+  For API details, see [GetSnapshotLimits](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DSTrust`
<a name="directory-service_DescribeTrusts_powershell_topic"></a>

The following code example shows how to use `Get-DSTrust`.

**Tools for PowerShell V5**
**Example 1: This command gets the information of trust relationships created for specified directory-id.**

```
Get-DSTrust -DirectoryId d-123456abcd
```
**Output:**

```
CreatedDateTime          : 7/5/2019 4:55:42 AM
DirectoryId              : d-123456abcd
LastUpdatedDateTime      : 7/5/2019 4:56:04 AM
RemoteDomainName         : contoso.com
SelectiveAuth            : Disabled
StateLastUpdatedDateTime : 7/5/2019 4:56:04 AM
TrustDirection           : One-Way: Incoming
TrustId                  : t-9067157123
TrustState               : Created
TrustStateReason         :
TrustType                : Forest
```
+  For API details, see [DescribeTrusts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSAlias`
<a name="directory-service_CreateAlias_powershell_topic"></a>

The following code example shows how to use `New-DSAlias`.

**Tools for PowerShell V5**
**Example 1: This command creates an alias for a directory and assigns the alias to the specified directory-id.**

```
New-DSAlias -DirectoryId d-123456ijkl -Alias MyOrgName
```
**Output:**

```
Alias     DirectoryId
-----     -----------
myorgname d-123456ijkl
```
+  For API details, see [CreateAlias](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSComputer`
<a name="directory-service_CreateComputer_powershell_topic"></a>

The following code example shows how to use `New-DSComputer`.

**Tools for PowerShell V5**
**Example 1: This example creates a new Active Directory computer object.**

```
New-DSComputer -DirectoryId d-123456ijkl -ComputerName ADMemberServer -Password $Password
```
**Output:**

```
ComputerAttributes                  ComputerId                                    ComputerName
------------------                  ----------                                    ------------
{WindowsSamName, DistinguishedName} S-1-5-21-1191241402-978882507-2717148213-1662 ADMemberServer
```
+  For API details, see [CreateComputer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSConditionalForwarder`
<a name="directory-service_CreateConditionalForwarder_powershell_topic"></a>

The following code example shows how to use `New-DSConditionalForwarder`.

**Tools for PowerShell V5**
**Example 1: This example creates a Conditional forwarder in specified AWS Directory-id. **

```
New-DSConditionalForwarder -DirectoryId d-123456ijkl -DnsIpAddr 172.31.36.96,172.31.10.56 -RemoteDomainName contoso.com
```
+  For API details, see [CreateConditionalForwarder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSDirectory`
<a name="directory-service_CreateDirectory_powershell_topic"></a>

The following code example shows how to use `New-DSDirectory`.

**Tools for PowerShell V5**
**Example 1: This example create a new Simple AD directory.**

```
New-DSDirectory -Name corp.example.com -Password $Password -Size Small -VpcSettings_VpcId vpc-123459d -VpcSettings_SubnetIds subnet-1234kkaa,subnet-5678ffbb
```
+  For API details, see [CreateDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSLogSubscription`
<a name="directory-service_CreateLogSubscription_powershell_topic"></a>

The following code example shows how to use `New-DSLogSubscription`.

**Tools for PowerShell V5**
**Example 1: This example creates a subscription to forward real-time Directory Service domain controller security logs to the specified Amazon CloudWatch log group in your AWS account.**

```
New-DSLogSubscription -DirectoryId d-123456ijkl -LogGroupName /aws/directoryservice/d-123456ijkl-lan2.example.com
```
+  For API details, see [CreateLogSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSMicrosoftAD`
<a name="directory-service_CreateMicrosoftAD_powershell_topic"></a>

The following code example shows how to use `New-DSMicrosoftAD`.

**Tools for PowerShell V5**
**Example 1: This example creates new Microsoft AD Directory in AWS Cloud.**

```
New-DSMicrosoftAD -Name corp.example.com -Password $Password -edition Standard -VpcSettings_VpcId vpc-123459d -VpcSettings_SubnetIds subnet-1234kkaa,subnet-5678ffbb
```
+  For API details, see [CreateMicrosoftAD](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSSnapshot`
<a name="directory-service_CreateSnapshot_powershell_topic"></a>

The following code example shows how to use `New-DSSnapshot`.

**Tools for PowerShell V5**
**Example 1: This example creates a directory snapshot**

```
New-DSSnapshot -DirectoryId d-123456ijkl
```
+  For API details, see [CreateSnapshot](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DSTrust`
<a name="directory-service_CreateTrust_powershell_topic"></a>

The following code example shows how to use `New-DSTrust`.

**Tools for PowerShell V5**
**Example 1: This example creates Two-Way Forestwide trust between your AWS Managed Microsoft AD directory, and existing on-premises Microsoft Active Directory.**

```
New-DSTrust -DirectoryId d-123456ijkl -RemoteDomainName contoso.com -TrustDirection Two-Way -TrustType Forest -TrustPassword $Password -ConditionalForwarderIpAddr 172.31.36.96
```
**Output:**

```
t-9067157123
```
+  For API details, see [CreateTrust](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-DSCertificate`
<a name="directory-service_RegisterCertificate_powershell_topic"></a>

The following code example shows how to use `Register-DSCertificate`.

**Tools for PowerShell V5**
**Example 1: This example registers a certificate for secured LDAP connection.**

```
$Certificate = Get-Content contoso.cer -Raw
Register-DSCertificate -DirectoryId d-123456ijkl -CertificateData $Certificate
```
**Output:**

```
c-906731e350
```
+  For API details, see [RegisterCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-DSEventTopic`
<a name="directory-service_RegisterEventTopic_powershell_topic"></a>

The following code example shows how to use `Register-DSEventTopic`.

**Tools for PowerShell V5**
**Example 1: This example associate a directory as a publisher with an SNS topic.**

```
Register-DSEventTopic -DirectoryId d-123456ijkl -TopicName snstopicname
```
+  For API details, see [RegisterEventTopic](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSConditionalForwarder`
<a name="directory-service_DeleteConditionalForwarder_powershell_topic"></a>

The following code example shows how to use `Remove-DSConditionalForwarder`.

**Tools for PowerShell V5**
**Example 1: This example removes the conditional forwarder that has been set up for your AWS Direcotry.**

```
Remove-DSConditionalForwarder -DirectoryId d-123456ijkl -RemoteDomainName contoso.com
```
+  For API details, see [DeleteConditionalForwarder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSDirectory`
<a name="directory-service_DeleteDirectory_powershell_topic"></a>

The following code example shows how to use `Remove-DSDirectory`.

**Tools for PowerShell V5**
**Example 1: This example deletes an AWS Directory service directory (Simple AD/Microsoft AD/AD Connector)**

```
Remove-DSDirectory -DirectoryId d-123456ijkl
```
+  For API details, see [DeleteDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSIpRoute`
<a name="directory-service_RemoveIpRoutes_powershell_topic"></a>

The following code example shows how to use `Remove-DSIpRoute`.

**Tools for PowerShell V5**
**Example 1: This command removes the specified IP from Configured IP routes of Directory-id. **

```
Remove-DSIpRoute -DirectoryId d-123456ijkl -CidrIp 203.0.113.5/32
```
+  For API details, see [RemoveIpRoutes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSLogSubscription`
<a name="directory-service_DeleteLogSubscription_powershell_topic"></a>

The following code example shows how to use `Remove-DSLogSubscription`.

**Tools for PowerShell V5**
**Example 1: This command removes the Log Subscription of specified Directory-id**

```
Remove-DSLogSubscription -DirectoryId d-123456ijkl
```
+  For API details, see [DeleteLogSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSResourceTag`
<a name="directory-service_RemoveTagsFromResource_powershell_topic"></a>

The following code example shows how to use `Remove-DSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This command removes the Resource Tag assigned to the specified Directory-id**

```
Remove-DSResourceTag -ResourceId d-123456ijkl -TagKey myTag
```
+  For API details, see [RemoveTagsFromResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSSnapshot`
<a name="directory-service_DeleteSnapshot_powershell_topic"></a>

The following code example shows how to use `Remove-DSSnapshot`.

**Tools for PowerShell V5**
**Example 1: This example removes the manually created snapshot.**

```
Remove-DSSnapshot -SnapshotId s-9068b488kc
```
+  For API details, see [DeleteSnapshot](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DSTrust`
<a name="directory-service_DeleteTrust_powershell_topic"></a>

The following code example shows how to use `Remove-DSTrust`.

**Tools for PowerShell V5**
**Example 1: This example removes the exsisting trust relationhip between your AWS Managed AD Directory and an external domain.**

```
Get-DSTrust -DirectoryId d-123456ijkl -Select Trusts.TrustId | Remove-DSTrust
```
**Output:**

```
t-9067157123
```
+  For API details, see [DeleteTrust](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Reset-DSUserPassword`
<a name="directory-service_ResetUserPassword_powershell_topic"></a>

The following code example shows how to use `Reset-DSUserPassword`.

**Tools for PowerShell V5**
**Example 1: This example resets the password of Active Direcotry user named ADUser in AWS Managed microsoft AD or Simple AD Directory**

```
Reset-DSUserPassword -UserName ADuser -DirectoryId d-123456ijkl -NewPassword $Password
```
+  For API details, see [ResetUserPassword](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Restore-DSFromSnapshot`
<a name="directory-service_RestoreFromSnapshot_powershell_topic"></a>

The following code example shows how to use `Restore-DSFromSnapshot`.

**Tools for PowerShell V5**
**Example 1: This example restores a directory using an exsisting directory snapshot.**

```
Restore-DSFromSnapshot -SnapshotId s-9068b488kc
```
+  For API details, see [RestoreFromSnapshot](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-DSDomainControllerCount`
<a name="directory-service_UpdateNumberOfDomainControllers_powershell_topic"></a>

The following code example shows how to use `Set-DSDomainControllerCount`.

**Tools for PowerShell V5**
**Example 1: This example sets the number of domain controller to 3 for specified directory-id.**

```
Set-DSDomainControllerCount -DirectoryId d-123456ijkl -DesiredNumber 3
```
+  For API details, see [UpdateNumberOfDomainControllers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Start-DSSchemaExtension`
<a name="directory-service_StartSchemaExtension_powershell_topic"></a>

The following code example shows how to use `Start-DSSchemaExtension`.

**Tools for PowerShell V5**
**Example 1: This Example Applies a schema extension to a Microsoft AD directory.**

```
$ldif = Get-Content D:\Users\Username\Downloads\ExtendedSchema.ldf -Raw
Start-DSSchemaExtension -DirectoryId d-123456ijkl -CreateSnapshotBeforeSchemaExtension $true -Description ManagedADSchemaExtension -LdifContent $ldif
```
**Output:**

```
e-9067306643
```
+  For API details, see [StartSchemaExtension](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Stop-DSSchemaExtension`
<a name="directory-service_CancelSchemaExtension_powershell_topic"></a>

The following code example shows how to use `Stop-DSSchemaExtension`.

**Tools for PowerShell V5**
**Example 1: This example cancels an in-progress schema extension to a Microsoft AD directory.**

```
Stop-DSSchemaExtension -DirectoryId d-123456ijkl -SchemaExtensionId e-9067306643
```
+  For API details, see [CancelSchemaExtension](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-DSCertificate`
<a name="directory-service_DeregisterCertificate_powershell_topic"></a>

The following code example shows how to use `Unregister-DSCertificate`.

**Tools for PowerShell V5**
**Example 1: This example deletes from the system the certificate that was registered for a secured LDAP connection..**

```
Unregister-DSCertificate -DirectoryId d-123456ijkl -CertificateId c-906731e34f
```
+  For API details, see [DeregisterCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-DSEventTopic`
<a name="directory-service_DeregisterEventTopic_powershell_topic"></a>

The following code example shows how to use `Unregister-DSEventTopic`.

**Tools for PowerShell V5**
**Example 1: This example removes the specefied directory as a publisher to the specified SNS topic. **

```
Unregister-DSEventTopic -DirectoryId d-123456ijkl -TopicName snstopicname
```
+  For API details, see [DeregisterEventTopic](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-DSConditionalForwarder`
<a name="directory-service_UpdateConditionalForwarder_powershell_topic"></a>

The following code example shows how to use `Update-DSConditionalForwarder`.

**Tools for PowerShell V5**
**Example 1: This example updates a conditional forwarder that has been set up for your AWS directory.**

```
Update-DSConditionalForwarder -DirectoryId d-123456ijkl -DnsIpAddr 172.31.36.96,172.31.16.108 -RemoteDomainName contoso.com
```
+  For API details, see [UpdateConditionalForwarder](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-DSRadius`
<a name="directory-service_UpdateRadius_powershell_topic"></a>

The following code example shows how to use `Update-DSRadius`.

**Tools for PowerShell V5**
**Example 1: This example updates RADIUS server information for an AD Connector or Microsoft AD directory.**

```
Update-DSRadius -DirectoryId d-123456ijkl -RadiusSettings_RadiusRetry 3
```
+  For API details, see [UpdateRadius](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-DSTrust`
<a name="directory-service_UpdateTrust_powershell_topic"></a>

The following code example shows how to use `Update-DSTrust`.

**Tools for PowerShell V5**
**Example 1: This example updates the SelectiveAuth parameter of specified trust-id from Disabled to Enabled.**

```
Update-DSTrust -TrustId t-9067157123 -SelectiveAuth Enabled
```
**Output:**

```
RequestId                            TrustId
---------                            -------
138864a7-c9a8-4ad1-a828-eae479e85b45 t-9067157123
```
+  For API details, see [UpdateTrust](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
