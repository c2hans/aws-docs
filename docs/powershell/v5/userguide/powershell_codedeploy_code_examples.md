---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_codedeploy_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# CodeDeploy examples using Tools for PowerShell V5
<a name="powershell_codedeploy_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with CodeDeploy.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-CDOnPremiseInstanceTag`
<a name="codedeploy_AddTagsToOnPremisesInstances_powershell_topic"></a>

The following code example shows how to use `Add-CDOnPremiseInstanceTag`.

**Tools for PowerShell V5**
**Example 1: This example adds an on-premises instance tag with the specified key and value for the specified on-premises instance.**

```
Add-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [AddTagsToOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDApplication`
<a name="codedeploy_GetApplication_powershell_topic"></a>

The following code example shows how to use `Get-CDApplication`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified application.**

```
Get-CDApplication -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
```
+  For API details, see [GetApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDApplicationBatch`
<a name="codedeploy_BatchGetApplications_powershell_topic"></a>

The following code example shows how to use `Get-CDApplicationBatch`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified applications.**

```
Get-CDApplicationBatch -ApplicationName CodeDeployDemoApplication, CodePipelineDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
1ecfd602-62f1-4038-8f0d-06688EXAMPLE    CodePipelineDemoApplication  8/13/2015 5:53:26 PM    False
```
+  For API details, see [BatchGetApplications](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDApplicationList`
<a name="codedeploy_ListApplications_powershell_topic"></a>

The following code example shows how to use `Get-CDApplicationList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available applications.**

```
Get-CDApplicationList
```
**Output:**

```
CodeDeployDemoApplication
CodePipelineDemoApplication
```
+  For API details, see [ListApplications](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDApplicationRevision`
<a name="codedeploy_GetApplicationRevision_powershell_topic"></a>

The following code example shows how to use `Get-CDApplicationRevision`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified application revision.**

```
$revision = Get-CDApplicationRevision -ApplicationName CodeDeployDemoApplication -S3Location_Bucket amzn-s3-demo-bucket -Revision_RevisionType S3 -S3Location_Key 5xd27EX.zip -S3Location_BundleType zip -S3Location_ETag 4565c1ac97187f190c1a90265EXAMPLE
Write-Output ("Description = " + $revision.RevisionInfo.Description + ", RegisterTime = " + $revision.RevisionInfo.RegisterTime)
```
**Output:**

```
Description = Application revision registered by Deployment ID: d-CX9CHN3EX, RegisterTime = 07/20/2015 23:46:42
```
+  For API details, see [GetApplicationRevision](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDApplicationRevisionList`
<a name="codedeploy_ListApplicationRevisions_powershell_topic"></a>

The following code example shows how to use `Get-CDApplicationRevisionList`.

**Tools for PowerShell V5**
**Example 1: This example gets information about available revisions for the specified application.**

```
ForEach ($revision in (Get-CDApplicationRevisionList -ApplicationName CodeDeployDemoApplication -Deployed Ignore)) {
>>   If ($revision.RevisionType -Eq "S3") {
>>     Write-Output ("Type = S3, Bucket = " + $revision.S3Location.Bucket + ", BundleType = " + $revision.S3Location.BundleType + ", ETag = " + $revision.S3Location.ETag + ", Key = " + $revision.S3Location.Key)
>>   }
>>   If ($revision.RevisionType -Eq "GitHub") {
>>     Write-Output ("Type = GitHub, CommitId = " + $revision.GitHubLocation.CommitId + ", Repository = " + $revision.GitHubLocation.Repository)
>>   }
>> }
>>
```
**Output:**

```
Type = S3, Bucket = amzn-s3-demo-bucket, BundleType = zip, ETag = 4565c1ac97187f190c1a90265EXAMPLE, Key = 5xd27EX.zip
Type = GitHub, CommitId = f48933c3...76405362, Repository = MyGitHubUser/CodeDeployDemoRepo
```
+  For API details, see [ListApplicationRevisions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeployment`
<a name="codedeploy_GetDeployment_powershell_topic"></a>

The following code example shows how to use `Get-CDDeployment`.

**Tools for PowerShell V5**
**Example 1: This example gets summary information about the specified deployment.**

```
Get-CDDeployment -DeploymentId d-QZMRGSTEX
```
**Output:**

```
ApplicationName               : CodeDeployDemoApplication
CompleteTime                  : 7/23/2015 11:26:04 PM
CreateTime                    : 7/23/2015 11:24:43 PM
Creator                       : user
DeploymentConfigName          : CodeDeployDefault.OneAtATime
DeploymentGroupName           : CodeDeployDemoFleet
DeploymentId                  : d-QZMRGSTEX
DeploymentOverview            : Amazon.CodeDeploy.Model.DeploymentOverview
Description                   :
ErrorInformation              :
IgnoreApplicationStopFailures : False
Revision                      : Amazon.CodeDeploy.Model.RevisionLocation
StartTime                     : 1/1/0001 12:00:00 AM
Status                        : Succeeded
```
**Example 2: This example gets information about the status of instances that are participating in the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).DeploymentOverview
```
**Output:**

```
Failed     : 0
InProgress : 0
Pending    : 0
Skipped    : 0
Succeeded  : 3
```
**Example 3: This example gets information about the application revision for the specified deployment.**

```
(Get-CDDeployment -DeploymentId d-QZMRGSTEX).Revision.S3Location
```
**Output:**

```
Bucket     : amzn-s3-demo-bucket
BundleType : zip
ETag       : cfbb81b304ee5e27efc21adaed3EXAMPLE
Key        : clzfqEX
Version    :
```
+  For API details, see [GetDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentBatch`
<a name="codedeploy_BatchGetDeployments_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentBatch`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified deployments.**

```
Get-CDDeploymentBatch -DeploymentId d-QZMRGSTEX, d-RR0T5KTEX
```
**Output:**

```
ApplicationName               : CodeDeployDemoApplication
CompleteTime                  : 7/23/2015 11:26:04 PM
CreateTime                    : 7/23/2015 11:24:43 PM
Creator                       : user
DeploymentConfigName          : CodeDeployDefault.OneAtATime
DeploymentGroupName           : CodeDeployDemoFleet
DeploymentId                  : d-QZMRGSTEX
DeploymentOverview            : Amazon.CodeDeploy.Model.DeploymentOverview
Description                   :
ErrorInformation              :
IgnoreApplicationStopFailures : False
Revision                      : Amazon.CodeDeploy.Model.RevisionLocation
StartTime                     : 1/1/0001 12:00:00 AM
Status                        : Succeeded

ApplicationName               : CodePipelineDemoApplication
CompleteTime                  : 7/23/2015 6:07:30 PM
CreateTime                    : 7/23/2015 6:06:29 PM
Creator                       : user
DeploymentConfigName          : CodeDeployDefault.OneAtATime
DeploymentGroupName           : CodePipelineDemoFleet
DeploymentId                  : d-RR0T5KTEX
DeploymentOverview            : Amazon.CodeDeploy.Model.DeploymentOverview
Description                   :
ErrorInformation              :
IgnoreApplicationStopFailures : False
Revision                      : Amazon.CodeDeploy.Model.RevisionLocation
StartTime                     : 1/1/0001 12:00:00 AM
Status                        : Succeeded
```
+  For API details, see [BatchGetDeployments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentConfig`
<a name="codedeploy_GetDeploymentConfig_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentConfig`.

**Tools for PowerShell V5**
**Example 1: This example gets summary information about the specified deployment configuration.**

```
Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy
```
**Output:**

```
CreateTime              DeploymentConfigId                      DeploymentConfigName    MinimumHealthyHosts
----------              ------------------                      --------------------    -------------------
10/3/2014 4:32:30 PM    518a3950-d034-46a1-9d2c-3c949EXAMPLE    ThreeQuartersHealthy    Amazon.CodeDeploy.Model.MinimumHealthyHosts
```
**Example 2: This example gets information about the definition of the specified deployment configuration.**

```
Write-Output ((Get-CDDeploymentConfig -DeploymentConfigName ThreeQuartersHealthy).MinimumHealthyHosts)
```
**Output:**

```
Type             Value
----             -----
FLEET_PERCENT    75
```
+  For API details, see [GetDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentConfigList`
<a name="codedeploy_ListDeploymentConfigs_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentConfigList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available deployment configurations.**

```
Get-CDDeploymentConfigList
```
**Output:**

```
ThreeQuartersHealthy
CodeDeployDefault.OneAtATime
CodeDeployDefault.AllAtOnce
CodeDeployDefault.HalfAtATime
```
+  For API details, see [ListDeploymentConfigs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentGroup`
<a name="codedeploy_GetDeploymentGroup_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentGroup`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified deployment group.**

```
Get-CDDeploymentGroup -ApplicationName CodeDeployDemoApplication -DeploymentGroupName CodeDeployDemoFleet
```
**Output:**

```
ApplicationName              : CodeDeployDemoApplication
AutoScalingGroups            : {}
DeploymentConfigName         : CodeDeployDefault.OneAtATime
DeploymentGroupId            : 7d7c098a-b444-4b27-96ef-22791EXAMPLE
DeploymentGroupName          : CodeDeployDemoFleet
Ec2TagFilters                : {Name}
OnPremisesInstanceTagFilters : {}
ServiceRoleArn               : arn:aws:iam::80398EXAMPLE:role/CodeDeploySampleStack-4ph6EX-CodeDeployTrustRole-O9MWP7XTL8EX
TargetRevision               : Amazon.CodeDeploy.Model.RevisionLocation
```
+  For API details, see [GetDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentGroupList`
<a name="codedeploy_ListDeploymentGroups_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentGroupList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of deployment groups for the specified application.**

```
Get-CDDeploymentGroupList -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationName              DeploymentGroups                                    NextToken
---------------              ----------------                                    ---------
CodeDeployDemoApplication    {CodeDeployDemoFleet, CodeDeployProductionFleet}
```
+  For API details, see [ListDeploymentGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentInstance`
<a name="codedeploy_GetDeploymentInstance_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentInstance`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified instance for the specified deployment.**

```
Get-CDDeploymentInstance -DeploymentId d-QZMRGSTEX -InstanceId i-254e22EX
```
**Output:**

```
DeploymentId    : d-QZMRGSTEX
InstanceId      : arn:aws:ec2:us-east-1:80398EXAMPLE:instance/i-254e22EX
LastUpdatedAt   : 7/23/2015 11:25:24 PM
LifecycleEvents : {ApplicationStop, DownloadBundle, BeforeInstall, Install...}
Status          : Succeeded
```
+  For API details, see [GetDeploymentInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentInstanceList`
<a name="codedeploy_ListDeploymentInstances_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentInstanceList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of instance IDs for the specified deployment.**

```
Get-CDDeploymentInstanceList -DeploymentId d-QZMRGSTEX
```
**Output:**

```
i-254e22EX
i-274e22EX
i-3b4e22EX
```
+  For API details, see [ListDeploymentInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDDeploymentList`
<a name="codedeploy_ListDeployments_powershell_topic"></a>

The following code example shows how to use `Get-CDDeploymentList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of deployment IDs for the specified application and deployment group.**

```
Get-CDDeploymentList -ApplicationName CodeDeployDemoApplication -DeploymentGroupName CodeDeployDemoFleet
```
**Output:**

```
d-QZMRGSTEX
d-RR0T5KTEX
```
+  For API details, see [ListDeployments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDOnPremiseInstance`
<a name="codedeploy_GetOnPremisesInstance_powershell_topic"></a>

The following code example shows how to use `Get-CDOnPremiseInstance`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified on-premises instance.**

```
Get-CDOnPremiseInstance -InstanceName AssetTag12010298EX
```
**Output:**

```
DeregisterTime : 1/1/0001 12:00:00 AM
IamUserArn     : arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser
InstanceArn    : arn:aws:codedeploy:us-east-1:80398EXAMPLE:instance/AssetTag12010298EX_rDH556dxEX
InstanceName   : AssetTag12010298EX
RegisterTime   : 4/3/2015 6:36:24 PM
Tags           : {Name}
```
+  For API details, see [GetOnPremisesInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDOnPremiseInstanceBatch`
<a name="codedeploy_BatchGetOnPremisesInstances_powershell_topic"></a>

The following code example shows how to use `Get-CDOnPremiseInstanceBatch`.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified on-premises instances.**

```
Get-CDOnPremiseInstanceBatch -InstanceName AssetTag12010298EX, AssetTag12010298EX-2
```
**Output:**

```
DeregisterTime : 1/1/0001 12:00:00 AM
IamUserArn     : arn:aws:iam::80398EXAMPLE:user/CodeDeployFRWUser
InstanceArn    : arn:aws:codedeploy:us-east-1:80398EXAMPLE:instance/AssetTag12010298EX-2_XmeSz18rEX
InstanceName   : AssetTag12010298EX-2
RegisterTime   : 4/3/2015 6:38:52 PM
Tags           : {Name}

DeregisterTime : 1/1/0001 12:00:00 AM
IamUserArn     : arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser
InstanceArn    : arn:aws:codedeploy:us-east-1:80398EXAMPLE:instance/AssetTag12010298EX_rDH556dxEX
InstanceName   : AssetTag12010298EX
RegisterTime   : 4/3/2015 6:36:24 PM
Tags           : {Name}
```
+  For API details, see [BatchGetOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CDOnPremiseInstanceList`
<a name="codedeploy_ListOnPremisesInstances_powershell_topic"></a>

The following code example shows how to use `Get-CDOnPremiseInstanceList`.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available on-premises instance names.**

```
Get-CDOnPremiseInstanceList
```
**Output:**

```
AssetTag12010298EX
AssetTag12010298EX-2
```
+  For API details, see [ListOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CDApplication`
<a name="codedeploy_CreateApplication_powershell_topic"></a>

The following code example shows how to use `New-CDApplication`.

**Tools for PowerShell V5**
**Example 1: This example creates a new application with the specified name.**

```
New-CDApplication -ApplicationName MyNewApplication
```
**Output:**

```
f19e4b61-2231-4328-b0fd-e57f5EXAMPLE
```
+  For API details, see [CreateApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CDDeployment`
<a name="codedeploy_CreateDeployment_powershell_topic"></a>

The following code example shows how to use `New-CDDeployment`.

**Tools for PowerShell V5**
**Example 1: This example creates a new deployment for the specified application and deployment group with the specified deployment configuration and application revision.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3
```
**Output:**

```
d-ZHROG7UEX
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeployment -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -IgnoreApplicationStopFailures $True -S3Location_Key aws-codedeploy_linux-master.zip -RevisionType S3 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
d-ZHROG7UEX
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CDDeploymentConfig`
<a name="codedeploy_CreateDeploymentConfig_powershell_topic"></a>

The following code example shows how to use `New-CDDeploymentConfig`.

**Tools for PowerShell V5**
**Example 1: This example creates a new deployment configuration with the specified name and behavior.**

```
New-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts -MinimumHealthyHosts_Type HOST_COUNT -MinimumHealthyHosts_Value 2
```
**Output:**

```
0f3e8187-44ef-42da-aeed-b6823EXAMPLE
```
+  For API details, see [CreateDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CDDeploymentGroup`
<a name="codedeploy_CreateDeploymentGroup_powershell_topic"></a>

The following code example shows how to use `New-CDDeploymentGroup`.

**Tools for PowerShell V5**
**Example 1: This example creates a deployment group with the specified name, Auto Scaling group, deployment configuration, tag, and service role, for the specified application.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
+  For API details, see [CreateDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-CDApplicationRevision`
<a name="codedeploy_RegisterApplicationRevision_powershell_topic"></a>

The following code example shows how to use `Register-CDApplicationRevision`.

**Tools for PowerShell V5**
**Example 1: This example registers an application revision with the specified Amazon S3 location, for the specified application.**

```
Register-CDApplicationRevision -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -S3Location_Key aws-codedeploy_linux-master.zip -Revision_RevisionType S3
```
+  For API details, see [RegisterApplicationRevision](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-CDOnPremiseInstance`
<a name="codedeploy_RegisterOnPremisesInstance_powershell_topic"></a>

The following code example shows how to use `Register-CDOnPremiseInstance`.

**Tools for PowerShell V5**
**Example 1: This example registers an on-premises instance with the specified name and IAM user.**

```
Register-CDOnPremiseInstance -IamUserArn arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser -InstanceName AssetTag12010298EX
```
+  For API details, see [RegisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CDApplication`
<a name="codedeploy_DeleteApplication_powershell_topic"></a>

The following code example shows how to use `Remove-CDApplication`.

**Tools for PowerShell V5**
**Example 1: This example deletes the application with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the application without a prompt.**

```
Remove-CDApplication -ApplicationName MyNewApplication
```
+  For API details, see [DeleteApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CDDeploymentConfig`
<a name="codedeploy_DeleteDeploymentConfig_powershell_topic"></a>

The following code example shows how to use `Remove-CDDeploymentConfig`.

**Tools for PowerShell V5**
**Example 1: This example deletes the deployment configuration with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment configuration without a prompt.**

```
Remove-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts
```
+  For API details, see [DeleteDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CDDeploymentGroup`
<a name="codedeploy_DeleteDeploymentGroup_powershell_topic"></a>

The following code example shows how to use `Remove-CDDeploymentGroup`.

**Tools for PowerShell V5**
**Example 1: This example deletes the deployment group with the specified name for the specified application. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the deployment group without a prompt.**

```
Remove-CDDeploymentGroup -ApplicationName MyNewApplication -DeploymentGroupName MyNewDeploymentGroup
```
+  For API details, see [DeleteDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CDOnPremiseInstanceTag`
<a name="codedeploy_RemoveTagsFromOnPremisesInstances_powershell_topic"></a>

The following code example shows how to use `Remove-CDOnPremiseInstanceTag`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified tag for the on-premises instance with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the tag without a prompt.**

```
Remove-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [RemoveTagsFromOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Stop-CDDeployment`
<a name="codedeploy_StopDeployment_powershell_topic"></a>

The following code example shows how to use `Stop-CDDeployment`.

**Tools for PowerShell V5**
**Example 1: This example attempts to stop the deployment with the specified deployment ID.**

```
Stop-CDDeployment -DeploymentId d-LJQNREYEX
```
**Output:**

```
Status     StatusMessage
------     -------------
Pending    Stopping Pending. Stopping to schedule commands in the deployment instances
```
+  For API details, see [StopDeployment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-CDOnPremiseInstance`
<a name="codedeploy_DeregisterOnPremisesInstance_powershell_topic"></a>

The following code example shows how to use `Unregister-CDOnPremiseInstance`.

**Tools for PowerShell V5**
**Example 1: This example deregisters the on-premises instance with the specified name.**

```
Unregister-CDOnPremiseInstance -InstanceName AssetTag12010298EX
```
+  For API details, see [DeregisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CDApplication`
<a name="codedeploy_UpdateApplication_powershell_topic"></a>

The following code example shows how to use `Update-CDApplication`.

**Tools for PowerShell V5**
**Example 1: This example changes the name of the specified application.**

```
Update-CDApplication -ApplicationName MyNewApplication -NewApplicationName MyNewApplication-2
```
+  For API details, see [UpdateApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CDDeploymentGroup`
<a name="codedeploy_UpdateDeploymentGroup_powershell_topic"></a>

The following code example shows how to use `Update-CDDeploymentGroup`.

**Tools for PowerShell V5**
**Example 1: This example changes the name of the specified deployment group for the specified application.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
+  For API details, see [UpdateDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
