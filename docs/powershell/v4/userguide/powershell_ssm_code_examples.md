---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ssm_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Systems Manager examples using Tools for PowerShell V4
<a name="powershell_ssm_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Systems Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-SSMResourceTag`
<a name="ssm_AddTagsToResource_powershell_topic"></a>

The following code example shows how to use `Add-SSMResourceTag`.

**Tools for PowerShell V4**
**Example 1: This example updates a maintenance window with new tags. There is no output if the command succeeds. The syntax used by this example requires PowerShell version 3 or later.**

```
$option1 = @{Key="Stack";Value=@("Production")}
Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $option1
```
**Example 2: With PowerShell version 2, you must use New-Object to create each tag. There is no output if the command succeeds.**

```
$tag1 = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag1.Key = "Stack"
$tag1.Value = "Production"

Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $tag1
```
+  For API details, see [AddTagsToResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-SSMDocumentPermission`
<a name="ssm_ModifyDocumentPermission_powershell_topic"></a>

The following code example shows how to use `Edit-SSMDocumentPermission`.

**Tools for PowerShell V4**
**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all
```
**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"
```
+  For API details, see [ModifyDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMActivation`
<a name="ssm_DescribeActivations_powershell_topic"></a>

The following code example shows how to use `Get-SSMActivation`.

**Tools for PowerShell V4**
**Example 1: This example provides details about the activations on your account.**

```
Get-SSMActivation
```
**Output:**

```
ActivationId        : 08e51e79-1e36-446c-8e63-9458569c1363
CreatedDate         : 3/1/2017 12:01:51 AM
DefaultInstanceName : MyWebServers
Description         :
ExpirationDate      : 3/2/2017 12:01:51 AM
Expired             : False
IamRole             : AutomationRole
RegistrationLimit   : 10
RegistrationsCount  : 0
```
+  For API details, see [DescribeActivations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAssociation`
<a name="ssm_DescribeAssociation_powershell_topic"></a>

The following code example shows how to use `Get-SSMAssociation`.

**Tools for PowerShell V4**
**Example 1: This example describes the association between an instance and a document.**

```
Get-SSMAssociation -InstanceId "i-0000293ffd8c57862" -Name "AWS-UpdateSSMAgent"
```
**Output:**

```
Name                  : AWS-UpdateSSMAgent
InstanceId            : i-0000293ffd8c57862
Date                  : 2/23/2017 6:55:22 PM
Status.Name           : Pending
Status.Date           : 2/20/2015 8:31:11 AM
Status.Message        : temp_status_change
Status.AdditionalInfo : Additional-Config-Needed
```
+  For API details, see [DescribeAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAssociationExecution`
<a name="ssm_DescribeAssociationExecutions_powershell_topic"></a>

The following code example shows how to use `Get-SSMAssociationExecution`.

**Tools for PowerShell V4**
**Example 1: This example returns the executions for the association ID provided**

```
Get-SSMAssociationExecution -AssociationId 123a45a0-c678-9012-3456-78901234db5e
```
**Output:**

```
AssociationId         : 123a45a0-c678-9012-3456-78901234db5e
AssociationVersion    : 2
CreatedTime           : 3/2/2019 8:53:29 AM
DetailedStatus        :
ExecutionId           : 123a45a0-c678-9012-3456-78901234db5e
LastExecutionDate     : 1/1/0001 12:00:00 AM
ResourceCountByStatus : {Success=4}
Status                : Success
```
+  For API details, see [DescribeAssociationExecutions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAssociationExecutionTarget`
<a name="ssm_DescribeAssociationExecutionTargets_powershell_topic"></a>

The following code example shows how to use `Get-SSMAssociationExecutionTarget`.

**Tools for PowerShell V4**
**Example 1: This example displays the resource ID and its execution status that are part of the the association execution targets**

```
Get-SSMAssociationExecutionTarget -AssociationId 123a45a0-c678-9012-3456-78901234db5e -ExecutionId 123a45a0-c678-9012-3456-78901234db5e | Select-Object ResourceId, Status
```
**Output:**

```
ResourceId           Status
----------           ------
i-0b1b2a3456f7a890b  Success
i-01c12a45d6fc7a89f  Success
i-0a1caf234f56d7dc8  Success
i-012a3fd45af6dbcfe  Failed
i-0ddc1df23c4a5fb67  Success
```
**Example 2: This command checks the particular execution of a particular automation since yesterday, where a command document is associated. It further checkes if the association execution failed, and if so, it will display the command invocation details for the execution along with the instance id**

```
$AssociationExecution= Get-SSMAssociationExecutionTarget -AssociationId 1c234567-890f-1aca-a234-5a678d901cb0 -ExecutionId 12345ca12-3456-2345-2b45-23456789012 |
    Where-Object {$_.LastExecutionDate -gt (Get-Date -Hour 00 -Minute 00).AddDays(-1)}

foreach ($execution in $AssociationExecution) {
    if($execution.Status -ne 'Success'){
        Write-Output "There was an issue executing the association $($execution.AssociationId) on $($execution.ResourceId)"
        Get-SSMCommandInvocation -CommandId $execution.OutputSource.OutputSourceId -Detail:$true | Select-Object -ExpandProperty CommandPlugins
    }
}
```
**Output:**

```
There was an issue executing the association 1c234567-890f-1aca-a234-5a678d901cb0 on i-0a1caf234f56d7dc8

Name                   : aws:runPowerShellScript
Output                 :
                         ----------ERROR-------
                         failed to run commands: exit status 1
OutputS3BucketName     :
OutputS3KeyPrefix      :
OutputS3Region         : eu-west-1
ResponseCode           : 1
ResponseFinishDateTime : 5/29/2019 11:04:49 AM
ResponseStartDateTime  : 5/29/2019 11:04:49 AM
StandardErrorUrl       :
StandardOutputUrl      :
Status                 : Failed
StatusDetails          : Failed
```
+  For API details, see [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAssociationList`
<a name="ssm_ListAssociations_powershell_topic"></a>

The following code example shows how to use `Get-SSMAssociationList`.

**Tools for PowerShell V4**
**Example 1: This example lists all the associations for an instance. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="InstanceId";Value=@("i-0000293ffd8c57862")}
Get-SSMAssociationList -AssociationFilterList $filter1
```
**Output:**

```
AssociationId      : d8617c07-2079-4c18-9847-1655fc2698b0
DocumentVersion    :
InstanceId         : i-0000293ffd8c57862
LastExecutionDate  : 2/20/2015 8:31:11 AM
Name               : AWS-UpdateSSMAgent
Overview           : Amazon.SimpleSystemsManagement.Model.AssociationOverview
ScheduleExpression :
Targets            : {InstanceIds}
```
**Example 2: This example lists all associations for a configuration document. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter2 = @{Key="Name";Value=@("AWS-UpdateSSMAgent")}
Get-SSMAssociationList -AssociationFilterList $filter2
```
**Output:**

```
AssociationId      : d8617c07-2079-4c18-9847-1655fc2698b0
DocumentVersion    :
InstanceId         : i-0000293ffd8c57862
LastExecutionDate  : 2/20/2015 8:31:11 AM
Name               : AWS-UpdateSSMAgent
Overview           : Amazon.SimpleSystemsManagement.Model.AssociationOverview
ScheduleExpression :
Targets            : {InstanceIds}
```
**Example 3: With PowerShell version 2, you must use New-Object to create each filter.**

```
$filter1 = New-Object Amazon.SimpleSystemsManagement.Model.AssociationFilter
$filter1.Key = "InstanceId"
$filter1.Value = "i-0000293ffd8c57862"

Get-SSMAssociationList -AssociationFilterList $filter1
```
**Output:**

```
AssociationId      : d8617c07-2079-4c18-9847-1655fc2698b0
DocumentVersion    :
InstanceId         : i-0000293ffd8c57862
LastExecutionDate  : 2/20/2015 8:31:11 AM
Name               : AWS-UpdateSSMAgent
Overview           : Amazon.SimpleSystemsManagement.Model.AssociationOverview
ScheduleExpression :
Targets            : {InstanceIds}
```
+  For API details, see [ListAssociations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAssociationVersionList`
<a name="ssm_ListAssociationVersions_powershell_topic"></a>

The following code example shows how to use `Get-SSMAssociationVersionList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves all versions of the association provided.**

```
Get-SSMAssociationVersionList -AssociationId 123a45a0-c678-9012-3456-78901234db5e
```
**Output:**

```
AssociationId      : 123a45a0-c678-9012-3456-78901234db5e
AssociationName    :
AssociationVersion : 2
ComplianceSeverity :
CreatedDate        : 3/12/2019 9:21:01 AM
DocumentVersion    :
MaxConcurrency     :
MaxErrors          :
Name               : AWS-GatherSoftwareInventory
OutputLocation     :
Parameters         : {}
ScheduleExpression :
Targets            : {InstanceIds}

AssociationId      : 123a45a0-c678-9012-3456-78901234db5e
AssociationName    : test-case-1234567890
AssociationVersion : 1
ComplianceSeverity :
CreatedDate        : 3/2/2019 8:53:29 AM
DocumentVersion    :
MaxConcurrency     :
MaxErrors          :
Name               : AWS-GatherSoftwareInventory
OutputLocation     :
Parameters         : {}
ScheduleExpression : rate(30minutes)
Targets            : {InstanceIds}
```
+  For API details, see [ListAssociationVersions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAutomationExecution`
<a name="ssm_GetAutomationExecution_powershell_topic"></a>

The following code example shows how to use `Get-SSMAutomationExecution`.

**Tools for PowerShell V4**
**Example 1: This example displays the details of an Automation Execution.**

```
Get-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"
```
**Output:**

```
AutomationExecutionId     : 4105a4fc-f944-11e6-9d32-8fb2db27a909
AutomationExecutionStatus : Failed
DocumentName              : AWS-UpdateLinuxAmi
DocumentVersion           : 1
ExecutionEndTime          : 2/22/2017 9:17:08 PM
ExecutionStartTime        : 2/22/2017 9:17:02 PM
FailureMessage            : Step launchInstance failed maximum allowed times. You are not authorized to perform this operation. Encoded
                            authorization failure message: B_V2QyyN7NhSZQYpmVzpEc4oSnj2GLTNYnXUHsTbqJkNMoDgubmbtthLmZyaiUYekORIrA42-fv1x-04q5Fjff6glh
                            Yb6TI5b0GQeeNrpwNvpDzmO-PSR1swlAbg9fdM9BcNjyrznspUkWpuKu9EC1Ou6v3OXU1KC9nZ7mPlWMFZNkSioQqpwWEvMw-GZktsQzm67qOhUhBNOLWYhbS
                            pkfiqzY-5nw3S0obx30fhd3EJa5O_-GjV_a0nFXQJa70ik40bFOrEh3MtCSbrQT6--DvFy_FQ8TKvkIXadyVskeJI84XOF5WmA60f1pi5GI08i-nRfZS6oDeU
                            gELBjjoFKD8s3L2aI0B6umWVxnQOjqhQRxwJ53b54sZJ2PW3v_mtg9-q0CK0ezS3xfh_y0ilaUGOAZG-xjQFuvU_JZedWpla3xi-MZsmblAifBI
                            (Service: AmazonEC2; Status Code: 403; Error Code: UnauthorizedOperation; Request ID:
                            6a002f94-ba37-43fd-99e6-39517715fce5)
Outputs                   : {[createImage.ImageId, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
Parameters                : {[AutomationAssumeRole, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]], [InstanceIamRole,
                            Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]], [SourceAmiId,
                            Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
StepExecutions            : {launchInstance, updateOSSoftware, stopInstance, createImage...}
```
**Example 2: This example lists step details for the given automation execution id**

```
Get-SSMAutomationExecution -AutomationExecutionId e1d2bad3-4567-8901-ae23-456c7c8901be | Select-Object -ExpandProperty StepExecutions | Select-Object StepName, Action, StepStatus, ValidNextSteps
```
**Output:**

```
StepName                  Action                  StepStatus ValidNextSteps
--------                  ------                  ---------- --------------
LaunchInstance            aws:runInstances        Success    {OSCompatibilityCheck}
OSCompatibilityCheck      aws:runCommand          Success    {RunPreUpdateScript}
RunPreUpdateScript        aws:runCommand          Success    {UpdateEC2Config}
UpdateEC2Config           aws:runCommand          Cancelled  {}
UpdateSSMAgent            aws:runCommand          Pending    {}
UpdateAWSPVDriver         aws:runCommand          Pending    {}
UpdateAWSEnaNetworkDriver aws:runCommand          Pending    {}
UpdateAWSNVMe             aws:runCommand          Pending    {}
InstallWindowsUpdates     aws:runCommand          Pending    {}
RunPostUpdateScript       aws:runCommand          Pending    {}
RunSysprepGeneralize      aws:runCommand          Pending    {}
StopInstance              aws:changeInstanceState Pending    {}
CreateImage               aws:createImage         Pending    {}
TerminateInstance         aws:changeInstanceState Pending    {}
```
+  For API details, see [GetAutomationExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAutomationExecutionList`
<a name="ssm_DescribeAutomationExecutions_powershell_topic"></a>

The following code example shows how to use `Get-SSMAutomationExecutionList`.

**Tools for PowerShell V4**
**Example 1: This example describes all active and terminated Automation Executions associated with your account.**

```
Get-SSMAutomationExecutionList
```
**Output:**

```
AutomationExecutionId     : 4105a4fc-f944-11e6-9d32-8fb2db27a909
AutomationExecutionStatus : Failed
DocumentName              : AWS-UpdateLinuxAmi
DocumentVersion           : 1
ExecutedBy                : admin
ExecutionEndTime          : 2/22/2017 9:17:08 PM
ExecutionStartTime        : 2/22/2017 9:17:02 PM
LogFile                   :
Outputs                   : {[createImage.ImageId, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
```
**Example 2: This example displays ExecutionID, document, execution start/end timestamp for executions with AutomationExecutionStatus other than 'Success'**

```
Get-SSMAutomationExecutionList | Where-Object AutomationExecutionStatus -ne "Success" | Select-Object AutomationExecutionId, DocumentName, AutomationExecutionStatus, ExecutionStartTime, ExecutionEndTime | Format-Table -AutoSize
```
**Output:**

```
AutomationExecutionId                DocumentName                            AutomationExecutionStatus ExecutionStartTime   ExecutionEndTime
---------------------                ------------                            ------------------------- ------------------   ----------------
e1d2bad3-4567-8901-ae23-456c7c8901be AWS-UpdateWindowsAmi                    Cancelled                 4/16/2019 5:37:04 AM 4/16/2019 5:47:29 AM
61234567-a7f8-90e1-2b34-567b8bf9012c Fixed-UpdateAmi                         Cancelled                 4/16/2019 5:33:04 AM 4/16/2019 5:40:15 AM
91234d56-7e89-0ac1-2aee-34ea5d6a7c89 AWS-UpdateWindowsAmi                    Failed                    4/16/2019 5:22:46 AM 4/16/2019 5:27:29 AM
```
+  For API details, see [DescribeAutomationExecutions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAutomationStepExecution`
<a name="ssm_DescribeAutomationStepExecutions_powershell_topic"></a>

The following code example shows how to use `Get-SSMAutomationStepExecution`.

**Tools for PowerShell V4**
**Example 1: This exmaple displays information about all active and terminated step executions in an Automation workflow.**

```
Get-SSMAutomationStepExecution -AutomationExecutionId e1d2bad3-4567-8901-ae23-456c7c8901be | Select-Object StepName, Action, StepStatus
```
**Output:**

```
StepName                  Action                  StepStatus
--------                  ------                  ----------
LaunchInstance            aws:runInstances        Success
OSCompatibilityCheck      aws:runCommand          Success
RunPreUpdateScript        aws:runCommand          Success
UpdateEC2Config           aws:runCommand          Cancelled
UpdateSSMAgent            aws:runCommand          Pending
UpdateAWSPVDriver         aws:runCommand          Pending
UpdateAWSEnaNetworkDriver aws:runCommand          Pending
UpdateAWSNVMe             aws:runCommand          Pending
InstallWindowsUpdates     aws:runCommand          Pending
RunPostUpdateScript       aws:runCommand          Pending
RunSysprepGeneralize      aws:runCommand          Pending
StopInstance              aws:changeInstanceState Pending
CreateImage               aws:createImage         Pending
TerminateInstance         aws:changeInstanceState Pending
```
+  For API details, see [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMAvailablePatch`
<a name="ssm_DescribeAvailablePatches_powershell_topic"></a>

The following code example shows how to use `Get-SSMAvailablePatch`.

**Tools for PowerShell V4**
**Example 1: This example gets all available patches for Windows Server 2012 that have a MSRC severity of Critical. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="PRODUCT";Values=@("WindowsServer2012")}
$filter2 = @{Key="MSRC_SEVERITY";Values=@("Critical")}

Get-SSMAvailablePatch -Filter $filter1,$filter2
```
**Output:**

```
Classification : SecurityUpdates
ContentUrl     : https://support.microsoft.com/en-us/kb/2727528
Description    : A security issue has been identified that could allow an unauthenticated remote attacker to compromise your system and gain control
                 over it. You can help protect your system by installing this update from Microsoft. After you install this update, you may have to
                 restart your system.
Id             : 1eb507be-2040-4eeb-803d-abc55700b715
KbNumber       : KB2727528
Language       : All
MsrcNumber     : MS12-072
MsrcSeverity   : Critical
Product        : WindowsServer2012
ProductFamily  : Windows
ReleaseDate    : 11/13/2012 6:00:00 PM
Title          : Security Update for Windows Server 2012 (KB2727528)
Vendor         : Microsoft
...
```
**Example 2: With PowerShell version 2, you must use New-Object to create each filter.**

```
$filter1 = New-Object Amazon.SimpleSystemsManagement.Model.PatchOrchestratorFilter
$filter1.Key = "PRODUCT"
$filter1.Values = "WindowsServer2012"
$filter2 = New-Object Amazon.SimpleSystemsManagement.Model.PatchOrchestratorFilter
$filter2.Key = "MSRC_SEVERITY"
$filter2.Values = "Critical"

Get-SSMAvailablePatch -Filter $filter1,$filter2
```
**Example 3: This example fetches all the updates which are released in last 20 days and applicable to products matching WindowsServer2019**

```
Get-SSMAvailablePatch | Where-Object ReleaseDate -ge (Get-Date).AddDays(-20) | Where-Object Product -eq "WindowsServer2019" | Select-Object ReleaseDate, Product, Title
```
**Output:**

```
ReleaseDate         Product           Title
-----------         -------           -----
4/9/2019 5:00:12 PM WindowsServer2019 2019-04 Security Update for Adobe Flash Player for Windows Server 2019 for x64-based Systems (KB4493478)
4/9/2019 5:00:06 PM WindowsServer2019 2019-04 Cumulative Update for Windows Server 2019 for x64-based Systems (KB4493509)
4/2/2019 5:00:06 PM WindowsServer2019 2019-03 Servicing Stack Update for Windows Server 2019 for x64-based Systems (KB4493510)
```
+  For API details, see [DescribeAvailablePatches](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMCommand`
<a name="ssm_ListCommands_powershell_topic"></a>

The following code example shows how to use `Get-SSMCommand`.

**Tools for PowerShell V4**
**Example 1: This example lists all commands requested.**

```
Get-SSMCommand
```
**Output:**

```
CommandId          : 4b75a163-d39a-4d97-87c9-98ae52c6be35
Comment            : Apply association with id at update time: 4cc73e42-d5ae-4879-84f8-57e09c0efcd0
CompletedCount     : 1
DocumentName       : AWS-RefreshAssociation
ErrorCount         : 0
ExpiresAfter       : 2/24/2017 3:19:08 AM
InstanceIds        : {i-0cb2b964d3e14fd9f}
MaxConcurrency     : 50
MaxErrors          : 0
NotificationConfig : Amazon.SimpleSystemsManagement.Model.NotificationConfig
OutputS3BucketName :
OutputS3KeyPrefix  :
OutputS3Region     :
Parameters         : {[associationIds, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
RequestedDateTime  : 2/24/2017 3:18:08 AM
ServiceRole        :
Status             : Success
StatusDetails      : Success
TargetCount        : 1
Targets            : {}
```
**Example 2: This example gets the status of a specific command.**

```
Get-SSMCommand -CommandId "4b75a163-d39a-4d97-87c9-98ae52c6be35"
```
**Example 3: This example retrieves all SSM commands invoked after 2019-04-01T00:00:00Z **

```
Get-SSMCommand -Filter @{Key="InvokedAfter";Value="2019-04-01T00:00:00Z"} | Select-Object CommandId, DocumentName, Status, RequestedDateTime | Sort-Object -Property RequestedDateTime -Descending
```
**Output:**

```
CommandId                            DocumentName               Status    RequestedDateTime
---------                            ------------               ------    -----------------
edb1b23e-456a-7adb-aef8-90e-012ac34f AWS-RunPowerShellScript    Cancelled 4/16/2019 5:45:23 AM
1a2dc3fb-4567-890d-a1ad-234b5d6bc7d9 AWS-ConfigureAWSPackage    Success   4/6/2019 9:19:42 AM
12c3456c-7e90-4f12-1232-1234f5b67893 KT-Retrieve-Cloud-Type-Win Failed    4/2/2019 4:13:07 AM
fe123b45-240c-4123-a2b3-234bdd567ecf AWS-RunInspecChecks        Failed    4/1/2019 2:27:31 PM
1eb23aa4-567d-4123-12a3-4c1c2ab34561 AWS-RunPowerShellScript    Success   4/1/2019 1:05:55 PM
1c2f3bb4-ee12-4bc1-1a23-12345eea123e AWS-RunInspecChecks        Failed    4/1/2019 11:13:09 AM
```
+  For API details, see [ListCommands](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMCommandInvocation`
<a name="ssm_ListCommandInvocations_powershell_topic"></a>

The following code example shows how to use `Get-SSMCommandInvocation`.

**Tools for PowerShell V4**
**Example 1: This example lists all the invocations of a command.**

```
Get-SSMCommandInvocation -CommandId "b8eac879-0541-439d-94ec-47a80d554f44" -Detail $true
```
**Output:**

```
CommandId          : b8eac879-0541-439d-94ec-47a80d554f44
CommandPlugins     : {aws:runShellScript}
Comment            : IP config
DocumentName       : AWS-RunShellScript
InstanceId         : i-0cb2b964d3e14fd9f
InstanceName       :
NotificationConfig : Amazon.SimpleSystemsManagement.Model.NotificationConfig
RequestedDateTime  : 2/22/2017 8:13:16 PM
ServiceRole        :
StandardErrorUrl   :
StandardOutputUrl  :
Status             : Success
StatusDetails      : Success
TraceOutput        :
```
**Example 2: This example lists CommandPlugins for invocation of the command id e1eb2e3c-ed4c-5123-45c1-234f5612345f**

```
Get-SSMCommandInvocation -CommandId e1eb2e3c-ed4c-5123-45c1-234f5612345f -Detail:$true | Select-Object -ExpandProperty CommandPlugins
```
**Output:**

```
Name                   : aws:runPowerShellScript
Output                 : Completed 17.7 KiB/17.7 KiB (40.1 KiB/s) with 1 file(s) remainingdownload: s3://dd-aess-r-ctmer/KUMO.png to ..\..\programdata\KUMO.png
                         kumo available

OutputS3BucketName     :
OutputS3KeyPrefix      :
OutputS3Region         : eu-west-1
ResponseCode           : 0
ResponseFinishDateTime : 4/3/2019 11:53:23 AM
ResponseStartDateTime  : 4/3/2019 11:53:21 AM
StandardErrorUrl       :
StandardOutputUrl      :
Status                 : Success
StatusDetails          : Success
```
+  For API details, see [ListCommandInvocations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMCommandInvocationDetail`
<a name="ssm_GetCommandInvocation_powershell_topic"></a>

The following code example shows how to use `Get-SSMCommandInvocationDetail`.

**Tools for PowerShell V4**
**Example 1: This example displays the details of a command executed on an instance.**

```
Get-SSMCommandInvocationDetail -InstanceId "i-0cb2b964d3e14fd9f" -CommandId "b8eac879-0541-439d-94ec-47a80d554f44"
```
**Output:**

```
CommandId              : b8eac879-0541-439d-94ec-47a80d554f44
Comment                : IP config
DocumentName           : AWS-RunShellScript
ExecutionElapsedTime   : PT0.004S
ExecutionEndDateTime   : 2017-02-22T20:13:16.651Z
ExecutionStartDateTime : 2017-02-22T20:13:16.651Z
InstanceId             : i-0cb2b964d3e14fd9f
PluginName             : aws:runShellScript
ResponseCode           : 0
StandardErrorContent   :
StandardErrorUrl       :
StandardOutputContent  :
StandardOutputUrl      :
Status                 : Success
StatusDetails          : Success
```
+  For API details, see [GetCommandInvocation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMComplianceItemList`
<a name="ssm_ListComplianceItems_powershell_topic"></a>

The following code example shows how to use `Get-SSMComplianceItemList`.

**Tools for PowerShell V4**
**Example 1: This example lists compliance items list for the given resource id and type, filtering compliance-type being 'Association'**

```
Get-SSMComplianceItemList -ResourceId i-1a2caf345f67d0dc2 -ResourceType ManagedInstance -Filter @{Key="ComplianceType";Values="Association"}
```
**Output:**

```
ComplianceType   : Association
Details          : {[DocumentName, AWS-GatherSoftwareInventory], [DocumentVersion, 1]}
ExecutionSummary : Amazon.SimpleSystemsManagement.Model.ComplianceExecutionSummary
Id               : 123a45a1-c234-1234-1245-67891236db4e
ResourceId       : i-1a2caf345f67d0dc2
ResourceType     : ManagedInstance
Severity         : UNSPECIFIED
Status           : COMPLIANT
Title            :
```
+  For API details, see [ListComplianceItems](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMComplianceSummaryList`
<a name="ssm_ListComplianceSummaries_powershell_topic"></a>

The following code example shows how to use `Get-SSMComplianceSummaryList`.

**Tools for PowerShell V4**
**Example 1: This example returns a summary count of compliant and non-compliant resources for all compliance types. **

```
Get-SSMComplianceSummaryList
```
**Output:**

```
ComplianceType CompliantSummary                                      NonCompliantSummary
-------------- ----------------                                      -------------------
FleetTotal     Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Association    Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Custom:InSpec  Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Patch          Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
```
+  For API details, see [ListComplianceSummaries](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMConnectionStatus`
<a name="ssm_GetConnectionStatus_powershell_topic"></a>

The following code example shows how to use `Get-SSMConnectionStatus`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the Session Manager connection status for an instance to determine whether it is connected and ready to receive Session Manager connections. **

```
Get-SSMConnectionStatus -Target i-0a1caf234f12d3dc4
```
**Output:**

```
Status    Target
------    ------
Connected i-0a1caf234f12d3dc4
```
+  For API details, see [GetConnectionStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDefaultPatchBaseline`
<a name="ssm_GetDefaultPatchBaseline_powershell_topic"></a>

The following code example shows how to use `Get-SSMDefaultPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example displays the default patch baseline.**

```
Get-SSMDefaultPatchBaseline
```
**Output:**

```
arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966
```
+  For API details, see [GetDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDeployablePatchSnapshotForInstance`
<a name="ssm_GetDeployablePatchSnapshotForInstance_powershell_topic"></a>

The following code example shows how to use `Get-SSMDeployablePatchSnapshotForInstance`.

**Tools for PowerShell V4**
**Example 1: This example displays the current snapshot for the patch baseline used by an Instance. This command must be run from the instance using the instance credentials. To ensure it uses the instance credentials, the example passes an `Amazon.Runtime.InstanceProfileAWSCredentials` object to the Credentials parameter.**

```
$credentials = [Amazon.Runtime.InstanceProfileAWSCredentials]::new()
Get-SSMDeployablePatchSnapshotForInstance -SnapshotId "4681775b-098f-4435-a956-0ef33373ac11" -InstanceId "i-0cb2b964d3e14fd9f" -Credentials $credentials
```
**Output:**

```
InstanceId          SnapshotDownloadUrl
----------          -------------------
i-0cb2b964d3e14fd9f https://patch-baseline-snapshot-us-west-2.s3-us-west-2.amazonaws.com/853d0d3db0f0cafe...1692/4681775b-098f-4435...
```
**Example 2: This example shows how to get the full SnapshotDownloadUrl. This command must be run from the instance using the instance credentials. To ensure it uses the instance credentials, the example configures the PowerShell session to use an `Amazon.Runtime.InstanceProfileAWSCredentials` object.**

```
Set-AWSCredential -Credential ([Amazon.Runtime.InstanceProfileAWSCredentials]::new())
(Get-SSMDeployablePatchSnapshotForInstance -SnapshotId "4681775b-098f-4435-a956-0ef33373ac11" -InstanceId "i-0cb2b964d3e14fd9f").SnapshotDownloadUrl
```
**Output:**

```
https://patch-baseline-snapshot-us-west-2.s3-us-west-2.amazonaws.com/853d0d3db0f0cafe...
```
+  For API details, see [GetDeployablePatchSnapshotForInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDocument`
<a name="ssm_GetDocument_powershell_topic"></a>

The following code example shows how to use `Get-SSMDocument`.

**Tools for PowerShell V4**
**Example 1: This example returns the content of a document.**

```
Get-SSMDocument -Name "RunShellScript"
```
**Output:**

```
Content
-------
{...
```
**Example 2: This example displays the complete contents of a document.**

```
(Get-SSMDocument -Name "RunShellScript").Content
{
   "schemaVersion":"2.0",
   "description":"Run an updated script",
   "parameters":{
      "commands":{
         "type":"StringList",
         "description":"(Required) Specify a shell script or a command to run.",
         "minItems":1,
         "displayType":"textarea"
      }
   },
   "mainSteps":[
      {
         "action":"aws:runShellScript",
         "name":"runShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      },
      {
         "action":"aws:runPowerShellScript",
         "name":"runPowerShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      }
   ]
}
```
+  For API details, see [GetDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDocumentDescription`
<a name="ssm_DescribeDocument_powershell_topic"></a>

The following code example shows how to use `Get-SSMDocumentDescription`.

**Tools for PowerShell V4**
**Example 1: This example returns information about a document.**

```
Get-SSMDocumentDescription -Name "RunShellScript"
```
**Output:**

```
CreatedDate     : 2/24/2017 5:25:13 AM
DefaultVersion  : 1
Description     : Run an updated script
DocumentType    : Command
DocumentVersion : 1
Hash            : f775e5df4904c6fa46686c4722fae9de1950dace25cd9608ff8d622046b68d9b
HashType        : Sha256
LatestVersion   : 1
Name            : RunShellScript
Owner           : 123456789012
Parameters      : {commands}
PlatformTypes   : {Linux}
SchemaVersion   : 2.0
Sha1            :
Status          : Active
```
+  For API details, see [DescribeDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDocumentList`
<a name="ssm_ListDocuments_powershell_topic"></a>

The following code example shows how to use `Get-SSMDocumentList`.

**Tools for PowerShell V4**
**Example 1: Lists all the configuration documents in your account.**

```
Get-SSMDocumentList
```
**Output:**

```
DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ApplyPatchBaseline
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureAWSPackage
Owner           : Amazon
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 2.0

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureCloudWatch
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2
...
```
**Example 2: This example retrieves all automation documents with name matchingi 'Platform'**

```
Get-SSMDocumentList -DocumentFilterList @{Key="DocumentType";Value="Automation"} | Where-Object Name -Match "Platform"
```
**Output:**

```
DocumentFormat  : JSON
DocumentType    : Automation
DocumentVersion : 7
Name            : KT-Get-Platform
Owner           : 987654123456
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 0.3
Tags            : {}
TargetType      :
VersionName     :
```
+  For API details, see [ListDocuments](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDocumentPermission`
<a name="ssm_DescribeDocumentPermission_powershell_topic"></a>

The following code example shows how to use `Get-SSMDocumentPermission`.

**Tools for PowerShell V4**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "RunShellScript"
```
**Output:**

```
CreatedDate          DocumentVersion IsDefaultVersion Name
-----------          --------------- ---------------- ----
2/24/2017 5:25:13 AM 1               True             RunShellScript
```
+  For API details, see [DescribeDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMDocumentVersionList`
<a name="ssm_ListDocumentVersions_powershell_topic"></a>

The following code example shows how to use `Get-SSMDocumentVersionList`.

**Tools for PowerShell V4**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "AWS-UpdateSSMAgent"
```
**Output:**

```
CreatedDate       : 6/1/2021 5:19:10 PM
DocumentFormat    : JSON
DocumentVersion   : 1
IsDefaultVersion  : True
Name              : AWS-UpdateSSMAgent
Status            : Active
```
+  For API details, see [ListDocumentVersions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMEffectiveInstanceAssociationList`
<a name="ssm_DescribeEffectiveInstanceAssociations_powershell_topic"></a>

The following code example shows how to use `Get-SSMEffectiveInstanceAssociationList`.

**Tools for PowerShell V4**
**Example 1: This example describes the effective associations for an instance.**

```
Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5
```
**Output:**

```
AssociationId                        Content
-------------                        -------
d8617c07-2079-4c18-9847-1655fc2698b0 {...
```
**Example 2: This example displays the contents of the effective associations for an instance.**

```
(Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5).Content
```
**Output:**

```
{
    "schemaVersion": "1.2",
    "description": "Update the Amazon SSM Agent to the latest version or specified version.",
    "parameters": {
        "version": {
            "default": "",
            "description": "(Optional) A specific version of the Amazon SSM Agent to install. If not specified, the agen
t will be updated to the latest version.",
            "type": "String"
        },
        "allowDowngrade": {
            "default": "false",
            "description": "(Optional) Allow the Amazon SSM Agent service to be downgraded to an earlier version. If set
 to false, the service can be upgraded to newer versions only (default). If set to true, specify the earlier version.",
            "type": "String",
            "allowedValues": [
                "true",
                "false"
            ]
        }
    },
    "runtimeConfig": {
        "aws:updateSsmAgent": {
            "properties": [
                {
                "agentName": "amazon-ssm-agent",
                "source": "https://s3.{Region}.amazonaws.com/amazon-ssm-{Region}/ssm-agent-manifest.json",
                "allowDowngrade": "{{ allowDowngrade }}",
                "targetVersion": "{{ version }}"
                }
            ]
        }
    }
}
```
+  For API details, see [DescribeEffectiveInstanceAssociations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMEffectivePatchesForPatchBaseline`
<a name="ssm_DescribeEffectivePatchesForPatchBaseline_powershell_topic"></a>

The following code example shows how to use `Get-SSMEffectivePatchesForPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example lists all patch baselines, with a maximum result list of 1.**

```
Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1
```
**Output:**

```
Patch                                      PatchStatus
-----                                      -----------
Amazon.SimpleSystemsManagement.Model.Patch Amazon.SimpleSystemsManagement.Model.PatchStatus
```
**Example 2: This example displays the patch status for all patch baselines, with a maximum result list of 1.**

```
(Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1).PatchStatus
```
**Output:**

```
ApprovalDate          DeploymentStatus
------------          ----------------
12/21/2010 6:00:00 PM APPROVED
```
+  For API details, see [DescribeEffectivePatchesForPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInstanceAssociationsStatus`
<a name="ssm_DescribeInstanceAssociationsStatus_powershell_topic"></a>

The following code example shows how to use `Get-SSMInstanceAssociationsStatus`.

**Tools for PowerShell V4**
**Example 1: This example shows details of the associations for an instance.**

```
Get-SSMInstanceAssociationsStatus -InstanceId "i-0000293ffd8c57862"
```
**Output:**

```
AssociationId    : d8617c07-2079-4c18-9847-1655fc2698b0
DetailedStatus   : Pending
DocumentVersion  : 1
ErrorCode        :
ExecutionDate    : 2/20/2015 8:31:11 AM
ExecutionSummary : temp_status_change
InstanceId       : i-0000293ffd8c57862
Name             : AWS-UpdateSSMAgent
OutputUrl        :
Status           : Pending
```
**Example 2: This example checks the instance association status for the given instance id and further, displays the execution status of those associations**

```
Get-SSMInstanceAssociationsStatus -InstanceId i-012e3cb4df567e8aa | ForEach-Object {Get-SSMAssociationExecution -AssociationId .AssociationId}
```
**Output:**

```
AssociationId         : 512a34a5-c678-1234-1234-12345678db9e
AssociationVersion    : 2
CreatedTime           : 3/2/2019 8:53:29 AM
DetailedStatus        :
ExecutionId           : 512a34a5-c678-1234-1234-12345678db9e
LastExecutionDate     : 1/1/0001 12:00:00 AM
ResourceCountByStatus : {Success=9}
Status                : Success
```
+  For API details, see [DescribeInstanceAssociationsStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInstanceInformation`
<a name="ssm_DescribeInstanceInformation_powershell_topic"></a>

The following code example shows how to use `Get-SSMInstanceInformation`.

**Tools for PowerShell V4**
**Example 1: This example shows details of each of your instances.**

```
Get-SSMInstanceInformation
```
**Output:**

```
ActivationId                           :
AgentVersion                           : 2.0.672.0
AssociationOverview                    : Amazon.SimpleSystemsManagement.Model.InstanceAggregatedAssociationOverview
AssociationStatus                      : Success
ComputerName                           : ip-172-31-44-222.us-west-2.compute.internal
IamRole                                :
InstanceId                             : i-0cb2b964d3e14fd9f
IPAddress                              : 172.31.44.222
IsLatestVersion                        : True
LastAssociationExecutionDate           : 2/24/2017 3:18:09 AM
LastPingDateTime                       : 2/24/2017 3:35:03 AM
LastSuccessfulAssociationExecutionDate : 2/24/2017 3:18:09 AM
Name                                   :
PingStatus                             : ConnectionLost
PlatformName                           : Amazon Linux AMI
PlatformType                           : Linux
PlatformVersion                        : 2016.09
RegistrationDate                       : 1/1/0001 12:00:00 AM
ResourceType                           : EC2Instance
```
**Example 2: This example shows how to use the -Filter parameter to filter results to only those AWS Systems Manager instances in region `us-east-1` with an `AgentVersion` of `2.2.800.0`. You can find a list of valid -Filter key values in the InstanceInformation API reference topic (https://docs.aws.amazon.com/systems-manager/latest/APIReference/API\_InstanceInformation.html\#systemsmanager-Type-InstanceInformation-ActivationId).**

```
$Filters = @{
    Key="AgentVersion"
    Values="2.2.800.0"
}
Get-SSMInstanceInformation -Region us-east-1 -Filter $Filters
```
**Output:**

```
ActivationId                           :
AgentVersion                           : 2.2.800.0
AssociationOverview                    : Amazon.SimpleSystemsManagement.Model.InstanceAggregatedAssociationOverview
AssociationStatus                      : Success
ComputerName                           : EXAMPLE-EXAMPLE.WORKGROUP
IamRole                                :
InstanceId                             : i-EXAMPLEb0792d98ce
IPAddress                              : 10.0.0.01
IsLatestVersion                        : False
LastAssociationExecutionDate           : 8/16/2018 12:02:50 AM
LastPingDateTime                       : 8/16/2018 7:40:27 PM
LastSuccessfulAssociationExecutionDate : 8/16/2018 12:02:50 AM
Name                                   :
PingStatus                             : Online
PlatformName                           : Microsoft Windows Server 2016 Datacenter
PlatformType                           : Windows
PlatformVersion                        : 10.0.14393
RegistrationDate                       : 1/1/0001 12:00:00 AM
ResourceType                           : EC2Instance

ActivationId                           :
AgentVersion                           : 2.2.800.0
AssociationOverview                    : Amazon.SimpleSystemsManagement.Model.InstanceAggregatedAssociationOverview
AssociationStatus                      : Success
ComputerName                           : EXAMPLE-EXAMPLE.WORKGROUP
IamRole                                :
InstanceId                             : i-EXAMPLEac7501d023
IPAddress                              : 10.0.0.02
IsLatestVersion                        : False
LastAssociationExecutionDate           : 8/16/2018 12:00:20 AM
LastPingDateTime                       : 8/16/2018 7:40:35 PM
LastSuccessfulAssociationExecutionDate : 8/16/2018 12:00:20 AM
Name                                   :
PingStatus                             : Online
PlatformName                           : Microsoft Windows Server 2016 Datacenter
PlatformType                           : Windows
PlatformVersion                        : 10.0.14393
RegistrationDate                       : 1/1/0001 12:00:00 AM
ResourceType                           : EC2Instance
```
**Example 3: This example shows how to use the -InstanceInformationFilterList parameter to filter results to only those AWS Systems Manager instances in region `us-east-1` with `PlatformTypes` of `Windows` or `Linux`. You can find a list of valid -InstanceInformationFilterList key values in the InstanceInformationFilter API reference topic (https://docs.aws.amazon.com/systems-manager/latest/APIReference/API\_InstanceInformationFilter.html).**

```
$Filters = @{
   Key="PlatformTypes"
   ValueSet=("Windows","Linux")
}
Get-SSMInstanceInformation -Region us-east-1 -InstanceInformationFilterList $Filters
```
**Output:**

```
ActivationId                           :
AgentVersion                           : 2.2.800.0
AssociationOverview                    : Amazon.SimpleSystemsManagement.Model.InstanceAggregatedAssociationOverview
AssociationStatus                      : Success
ComputerName                           : EXAMPLE-EXAMPLE.WORKGROUP
IamRole                                :
InstanceId                             : i-EXAMPLEb0792d98ce
IPAddress                              : 10.0.0.27
IsLatestVersion                        : False
LastAssociationExecutionDate           : 8/16/2018 12:02:50 AM
LastPingDateTime                       : 8/16/2018 7:40:27 PM
LastSuccessfulAssociationExecutionDate : 8/16/2018 12:02:50 AM
Name                                   :
PingStatus                             : Online
PlatformName                           : Ubuntu Server 18.04 LTS
PlatformType                           : Linux
PlatformVersion                        : 18.04
RegistrationDate                       : 1/1/0001 12:00:00 AM
ResourceType                           : EC2Instance

ActivationId                           :
AgentVersion                           : 2.2.800.0
AssociationOverview                    : Amazon.SimpleSystemsManagement.Model.InstanceAggregatedAssociationOverview
AssociationStatus                      : Success
ComputerName                           : EXAMPLE-EXAMPLE.WORKGROUP
IamRole                                :
InstanceId                             : i-EXAMPLEac7501d023
IPAddress                              : 10.0.0.100
IsLatestVersion                        : False
LastAssociationExecutionDate           : 8/16/2018 12:00:20 AM
LastPingDateTime                       : 8/16/2018 7:40:35 PM
LastSuccessfulAssociationExecutionDate : 8/16/2018 12:00:20 AM
Name                                   :
PingStatus                             : Online
PlatformName                           : Microsoft Windows Server 2016 Datacenter
PlatformType                           : Windows
PlatformVersion                        : 10.0.14393
RegistrationDate                       : 1/1/0001 12:00:00 AM
ResourceType                           : EC2Instance
```
**Example 4: This example lists ssm managed instances and exports InstanceId, PingStatus, LastPingDateTime and PlatformName to a csv file.**

```
Get-SSMInstanceInformation | Select-Object InstanceId, PingStatus, LastPingDateTime, PlatformName | Export-Csv Instance-details.csv -NoTypeInformation
```
+  For API details, see [DescribeInstanceInformation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInstancePatch`
<a name="ssm_DescribeInstancePatches_powershell_topic"></a>

The following code example shows how to use `Get-SSMInstancePatch`.

**Tools for PowerShell V4**
**Example 1: This example gets the patch compliance details for an instance.**

```
Get-SSMInstancePatch -InstanceId "i-08ee91c0b17045407"
```
+  For API details, see [DescribeInstancePatches](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInstancePatchState`
<a name="ssm_DescribeInstancePatchStates_powershell_topic"></a>

The following code example shows how to use `Get-SSMInstancePatchState`.

**Tools for PowerShell V4**
**Example 1: This example gets the patch summary states for an instance.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407"
```
**Example 2: This example gets the patch summary states for two instances.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407","i-09a618aec652973a9"
```
+  For API details, see [DescribeInstancePatchStates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInstancePatchStatesForPatchGroup`
<a name="ssm_DescribeInstancePatchStatesForPatchGroup_powershell_topic"></a>

The following code example shows how to use `Get-SSMInstancePatchStatesForPatchGroup`.

**Tools for PowerShell V4**
**Example 1: This example gets the patch summary states per-instance for a patch group.**

```
Get-SSMInstancePatchStatesForPatchGroup -PatchGroup "Production"
```
+  For API details, see [DescribeInstancePatchStatesForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInventory`
<a name="ssm_GetInventory_powershell_topic"></a>

The following code example shows how to use `Get-SSMInventory`.

**Tools for PowerShell V4**
**Example 1: This example gets the custom metadata for your inventory.**

```
Get-SSMInventory
```
**Output:**

```
Data                                                                                  Id
----                                                                                  --
{[AWS:InstanceInformation, Amazon.SimpleSystemsManagement.Model.InventoryResultItem]} i-0cb2b964d3e14fd9f
```
+  For API details, see [GetInventory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInventoryEntriesList`
<a name="ssm_ListInventoryEntries_powershell_topic"></a>

The following code example shows how to use `Get-SSMInventoryEntriesList`.

**Tools for PowerShell V4**
**Example 1: This example lists all the custom inventory entries for an instance.**

```
Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo"
```
**Output:**

```
CaptureTime   : 2016-08-22T10:01:01Z
Entries       : {Amazon.Runtime.Internal.Util.AlwaysSendDictionary`2[System.String,System.String]}
InstanceId    : i-0cb2b964d3e14fd9f
NextToken     :
SchemaVersion : 1.0
TypeName      : Custom:RackInfo
```
**Example 2: This example lists the details.**

```
(Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo").Entries
```
**Output:**

```
Key          Value
---          -----
RackLocation Bay B/Row C/Rack D/Shelf E
```
+  For API details, see [ListInventoryEntries](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInventoryEntryList`
<a name="ssm_Get-SSMInventoryEntryList_powershell_topic"></a>

The following code example shows how to use `Get-SSMInventoryEntryList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves `AWS:Network` type inventory entries for the instance.**

```
Get-SSMInventoryEntryList -InstanceId mi-088dcb0ecea37b076 -TypeName AWS:Network | Select-Object -ExpandProperty Entries
```
**Output:**

```
Key        Value
---        -----
DHCPServer 172.31.11.2
DNSServer  172.31.0.1
Gateway    172.31.11.2
IPV4       172.31.11.222
IPV6       fe12::3456:7da8:901a:12a3
MacAddress 1A:23:4E:5B:FB:67
Name       Amazon Elastic Network Adapter
SubnetMask 255.255.240.0
```
+  For API details, see [Get-SSMInventoryEntryList](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMInventorySchema`
<a name="ssm_GetInventorySchema_powershell_topic"></a>

The following code example shows how to use `Get-SSMInventorySchema`.

**Tools for PowerShell V4**
**Example 1: This example returns a list of inventory type names for the account.**

```
Get-SSMInventorySchema
```
+  For API details, see [GetInventorySchema](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMLatestEC2Image`
<a name="ssm_Get-SSMLatestEC2Image_powershell_topic"></a>

The following code example shows how to use `Get-SSMLatestEC2Image`.

**Tools for PowerShell V4**
**Example 1: This example lists all the lastest Windows AMIs.**

```
PS Get-SSMLatestEC2Image -Path ami-windows-latest
```
**Output:**

```
Name                                                                    Value
----                                                                    -----
Windows_Server-2008-R2_SP1-English-64Bit-SQL_2012_SP4_Express           ami-0e5ddd288daff4fab
Windows_Server-2012-R2_RTM-Chinese_Simplified-64Bit-Base                ami-0c5ea64e6bec1cb50
Windows_Server-2012-R2_RTM-Chinese_Traditional-64Bit-Base               ami-09775eff0bf8c113d
Windows_Server-2012-R2_RTM-Dutch-64Bit-Base                             ami-025064b67e28cf5df
...
```
**Example 2: This example retrieves the AMI id of a specific Amazon Linux image for the us-west-2 region.**

```
PS Get-SSMLatestEC2Image -Path ami-amazon-linux-latest -ImageName amzn-ami-hvm-x86_64-ebs -Region us-west-2
```
**Output:**

```
ami-09b92cd132204c704
```
**Example 3: This example lists all the lastest Windows AMIs matching the specified wildcard expression.**

```
Get-SSMLatestEC2Image -Path ami-windows-latest -ImageName *Windows*2019*English*
```
**Output:**

```
Name                                                     Value
----                                                     -----
Windows_Server-2019-English-Full-SQL_2017_Web            ami-085e9d27da5b73a42
Windows_Server-2019-English-STIG-Core                    ami-0bfd85c29148c7f80
Windows_Server-2019-English-Full-SQL_2019_Web            ami-02099560d7fb11f20
Windows_Server-2019-English-Full-SQL_2016_SP2_Standard   ami-0d7ae2d81c07bd598
...
```
+  For API details, see [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindow`
<a name="ssm_GetMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example gets details about a maintenance window.**

```
Get-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d"
```
**Output:**

```
AllowUnassociatedTargets : False
CreatedDate              : 2/20/2017 6:14:05 PM
Cutoff                   : 1
Duration                 : 2
Enabled                  : True
ModifiedDate             : 2/20/2017 6:14:05 PM
Name                     : TestMaintWin
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
+  For API details, see [GetMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowExecution`
<a name="ssm_GetMaintenanceWindowExecution_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowExecution`.

**Tools for PowerShell V4**
**Example 1: This example lists information about a task executed as part of a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecution -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"
```
**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
TaskIds           : {ac0c6ae1-daa3-4a89-832e-d384503b6586}
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```
+  For API details, see [GetMaintenanceWindowExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowExecutionList`
<a name="ssm_DescribeMaintenanceWindowExecutions_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowExecutionList`.

**Tools for PowerShell V4**
**Example 1: This example lists all of the executions for a maintenance window.**

```
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d"
```
**Output:**

```
EndTime           : 2/20/2017 6:30:17 PM
StartTime         : 2/20/2017 6:30:16 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
WindowExecutionId : 6f3215cf-4101-4fa0-9b7b-9523269599c7
WindowId          : mw-03eb9db42890fb82d
```
**Example 2: This example lists all of the executions for a maintenance window before a specified date.**

```
$option1 = @{Key="ExecutedBefore";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1
```
**Example 3: This example lists all of the executions for a maintenance window after a specified date.**

```
$option1 = @{Key="ExecutedAfter";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1
```
+  For API details, see [DescribeMaintenanceWindowExecutions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowExecutionTask`
<a name="ssm_GetMaintenanceWindowExecutionTask_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowExecutionTask`.

**Tools for PowerShell V4**
**Example 1: This example lists information about a task that was part of a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecutionTask -TaskId "ac0c6ae1-daa3-4a89-832e-d384503b6586" -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"
```
**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
MaxConcurrency    : 1
MaxErrors         : 1
Priority          : 10
ServiceRole       : arn:aws:iam::123456789012:role/MaintenanceWindowsRole
StartTime         : 2/21/2017 4:00:34 PM
Status            : FAILED
StatusDetails     : The maximum error count was exceeded.
TaskArn           : AWS-RunShellScript
TaskExecutionId   : ac0c6ae1-daa3-4a89-832e-d384503b6586
TaskParameters    : {Amazon.Runtime.Internal.Util.AlwaysSendDictionary`2[System.String,Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskPara
                    meterValueExpression]}
Type              : RUN_COMMAND
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```
+  For API details, see [GetMaintenanceWindowExecutionTask](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowExecutionTaskInvocationList`
<a name="ssm_DescribeMaintenanceWindowExecutionTaskInvocations_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowExecutionTaskInvocationList`.

**Tools for PowerShell V4**
**Example 1: This example lists the invocations for a task executed as part of a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecutionTaskInvocationList -TaskId "ac0c6ae1-daa3-4a89-832e-d384503b6586" -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"
```
**Output:**

```
EndTime           : 2/21/2017 4:00:34 PM
ExecutionId       :
InvocationId      : e274b6e1-fe56-4e32-bd2a-8073c6381d8b
OwnerInformation  :
Parameters        : {"documentName":"AWS-RunShellScript","instanceIds":["i-0000293ffd8c57862"],"parameters":{"commands":["df"]},"maxConcurrency":"1",
                    "maxErrors":"1"}
StartTime         : 2/21/2017 4:00:34 PM
Status            : FAILED
StatusDetails     : The instance IDs list contains an invalid entry.
TaskExecutionId   : ac0c6ae1-daa3-4a89-832e-d384503b6586
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
WindowTargetId    :
```
+  For API details, see [DescribeMaintenanceWindowExecutionTaskInvocations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowExecutionTaskList`
<a name="ssm_DescribeMaintenanceWindowExecutionTasks_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowExecutionTaskList`.

**Tools for PowerShell V4**
**Example 1: This example lists the tasks associated with a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecutionTaskList -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"
```
**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : SUCCESS
TaskArn           : AWS-RunShellScript
TaskExecutionId   : ac0c6ae1-daa3-4a89-832e-d384503b6586
TaskType          : RUN_COMMAND
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```
+  For API details, see [DescribeMaintenanceWindowExecutionTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowList`
<a name="ssm_DescribeMaintenanceWindows_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowList`.

**Tools for PowerShell V4**
**Example 1: This example lists all maintenance windows on your account.**

```
Get-SSMMaintenanceWindowList
```
**Output:**

```
Cutoff   : 1
Duration : 4
Enabled  : True
Name     : My-First-Maintenance-Window
WindowId : mw-06d59c1a07c022145
```
+  For API details, see [DescribeMaintenanceWindows](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowTarget`
<a name="ssm_DescribeMaintenanceWindowTargets_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowTarget`.

**Tools for PowerShell V4**
**Example 1: This example lists all of the targets for a maintenance window.**

```
Get-SSMMaintenanceWindowTarget -WindowId "mw-06cf17cbefcb4bf4f"
```
**Output:**

```
OwnerInformation : Single instance
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : 350d44e6-28cc-44e2-951f-4b2c985838f6

OwnerInformation : Two instances in a list
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : e078a987-2866-47be-bedd-d9cf49177d3a
```
+  For API details, see [DescribeMaintenanceWindowTargets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMMaintenanceWindowTaskList`
<a name="ssm_DescribeMaintenanceWindowTasks_powershell_topic"></a>

The following code example shows how to use `Get-SSMMaintenanceWindowTaskList`.

**Tools for PowerShell V4**
**Example 1: This example lists all of the tasks for a maintenance window.**

```
Get-SSMMaintenanceWindowTaskList -WindowId "mw-06cf17cbefcb4bf4f"
```
**Output:**

```
LoggingInfo    :
MaxConcurrency : 1
MaxErrors      : 1
Priority       : 10
ServiceRoleArn : arn:aws:iam::123456789012:role/MaintenanceWindowsRole
Targets        : {InstanceIds}
TaskArn        : AWS-RunShellScript
TaskParameters : {[commands, Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression]}
Type           : RUN_COMMAND
WindowId       : mw-06cf17cbefcb4bf4f
WindowTaskId   : a23e338d-ff30-4398-8aa3-09cd052ebf17
```
+  For API details, see [DescribeMaintenanceWindowTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMParameterHistory`
<a name="ssm_GetParameterHistory_powershell_topic"></a>

The following code example shows how to use `Get-SSMParameterHistory`.

**Tools for PowerShell V4**
**Example 1: This example lists the value history for a parameter.**

```
Get-SSMParameterHistory -Name "Welcome"
```
**Output:**

```
Description      :
KeyId            :
LastModifiedDate : 3/3/2017 6:55:25 PM
LastModifiedUser : arn:aws:iam::123456789012:user/admin
Name             : Welcome
Type             : String
Value            : helloWorld
```
+  For API details, see [GetParameterHistory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMParameterList`
<a name="ssm_DescribeParameters_powershell_topic"></a>

The following code example shows how to use `Get-SSMParameterList`.

**Tools for PowerShell V4**
**Example 1: This example lists all parameters.**

```
Get-SSMParameterList
```
**Output:**

```
Description      :
KeyId            :
LastModifiedDate : 3/3/2017 6:58:23 PM
LastModifiedUser : arn:aws:iam::123456789012:user/admin
Name             : Welcome
Type             : String
```
+  For API details, see [DescribeParameters](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMParameterValue`
<a name="ssm_GetParameters_powershell_topic"></a>

The following code example shows how to use `Get-SSMParameterValue`.

**Tools for PowerShell V4**
**Example 1: This example lists the values for a parameter.**

```
Get-SSMParameterValue -Name "Welcome"
```
**Output:**

```
InvalidParameters Parameters
----------------- ----------
{}                {Welcome}
```
**Example 2: This example lists the details of the value.**

```
(Get-SSMParameterValue -Name "Welcome").Parameters
```
**Output:**

```
Name    Type   Value
----    ----   -----
Welcome String Good day, Sunshine!
```
+  For API details, see [GetParameters](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMPatchBaseline`
<a name="ssm_DescribePatchBaselines_powershell_topic"></a>

The following code example shows how to use `Get-SSMPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example lists all patch baselines.**

```
Get-SSMPatchBaseline
```
**Output:**

```
BaselineDescription                                             BaselineId                                                            BaselineName
-------------------                                             ----------                                                            ------------
Default Patch Baseline Provided by AWS.                         arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultP...
Baseline containing all updates approved for production systems pb-045f10b4f382baeda                                                  Production-B...
Baseline containing all updates approved for production systems pb-0a2f1059b670ebd31                                                  Production-B...
```
**Example 2: This example lists all patch baselines provided by AWS. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("AWS")}
```
**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```
**Example 3: This example lists all patch baselines with you as the owner. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("Self")}
```
**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```
**Example 4: With PowerShell version 2, you must use New-Object to create each tag.**

```
$filter1 = New-Object Amazon.SimpleSystemsManagement.Model.PatchOrchestratorFilter
$filter1.Key = "OWNER"
$filter1.Values = "AWS"

Get-SSMPatchBaseline -Filter $filter1
```
**Output:**

```
BaselineDescription                     BaselineId                                                            BaselineName             DefaultBaselin
                                                                                                                                       e
-------------------                     ----------                                                            ------------             --------------
Default Patch Baseline Provided by AWS. arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultPatchBaseline True
```
+  For API details, see [DescribePatchBaselines](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMPatchBaselineDetail`
<a name="ssm_GetPatchBaseline_powershell_topic"></a>

The following code example shows how to use `Get-SSMPatchBaselineDetail`.

**Tools for PowerShell V4**
**Example 1: This example displays the details for a patch baseline.**

```
Get-SSMPatchBaselineDetail -BaselineId "pb-03da896ca3b68b639"
```
**Output:**

```
ApprovalRules   : Amazon.SimpleSystemsManagement.Model.PatchRuleGroup
ApprovedPatches : {}
BaselineId      : pb-03da896ca3b68b639
CreatedDate     : 3/3/2017 5:02:19 PM
Description     : Baseline containing all updates approved for production systems
GlobalFilters   : Amazon.SimpleSystemsManagement.Model.PatchFilterGroup
ModifiedDate    : 3/3/2017 5:02:19 PM
Name            : Production-Baseline
PatchGroups     : {}
RejectedPatches : {}
```
+  For API details, see [GetPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMPatchBaselineForPatchGroup`
<a name="ssm_GetPatchBaselineForPatchGroup_powershell_topic"></a>

The following code example shows how to use `Get-SSMPatchBaselineForPatchGroup`.

**Tools for PowerShell V4**
**Example 1: This example displays the patch baseline for a patch group.**

```
Get-SSMPatchBaselineForPatchGroup -PatchGroup "Production"
```
**Output:**

```
BaselineId           PatchGroup
----------           ----------
pb-045f10b4f382baeda Production
```
+  For API details, see [GetPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMPatchGroup`
<a name="ssm_DescribePatchGroups_powershell_topic"></a>

The following code example shows how to use `Get-SSMPatchGroup`.

**Tools for PowerShell V4**
**Example 1: This example lists the patch group registrations.**

```
Get-SSMPatchGroup
```
**Output:**

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```
+  For API details, see [DescribePatchGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMPatchGroupState`
<a name="ssm_DescribePatchGroupState_powershell_topic"></a>

The following code example shows how to use `Get-SSMPatchGroupState`.

**Tools for PowerShell V4**
**Example 1: This example gets the high-level patch compliance summary for a patch group.**

```
Get-SSMPatchGroupState -PatchGroup "Production"
```
**Output:**

```
Instances                          : 4
InstancesWithFailedPatches         : 1
InstancesWithInstalledOtherPatches : 4
InstancesWithInstalledPatches      : 3
InstancesWithMissingPatches        : 0
InstancesWithNotApplicablePatches  : 0
```
+  For API details, see [DescribePatchGroupState](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMResourceComplianceSummaryList`
<a name="ssm_ListResourceComplianceSummaries_powershell_topic"></a>

The following code example shows how to use `Get-SSMResourceComplianceSummaryList`.

**Tools for PowerShell V4**
**Example 1: This example gets a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts for products that match "Windows10". Because the MaxResult default is 100 if the parameter is not specified, and this value is not valid, MaxResult parameter is added, and the value is set to 50.**

```
$FilterValues = @{
		"Key"="Product"
        "Type"="EQUAL"
        "Values"="Windows10"
}
        Get-SSMResourceComplianceSummaryList -Filter $FilterValues -MaxResult 50
```
+  For API details, see [ListResourceComplianceSummaries](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SSMResourceTag`
<a name="ssm_ListTagsForResource_powershell_topic"></a>

The following code example shows how to use `Get-SSMResourceTag`.

**Tools for PowerShell V4**
**Example 1: This example lists the tags for a maintenance window.**

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"
```
**Output:**

```
Key   Value
---   -----
Stack Production
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMActivation`
<a name="ssm_CreateActivation_powershell_topic"></a>

The following code example shows how to use `New-SSMActivation`.

**Tools for PowerShell V4**
**Example 1: This example creates a managed instance.**

```
New-SSMActivation -DefaultInstanceName "MyWebServers" -IamRole "SSMAutomationRole" -RegistrationLimit 10
```
**Output:**

```
ActivationCode       ActivationId
--------------       ------------
KWChhOxBTiwDcKE9BlKC 08e51e79-1e36-446c-8e63-9458569c1363
```
+  For API details, see [CreateActivation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMAssociation`
<a name="ssm_CreateAssociation_powershell_topic"></a>

The following code example shows how to use `New-SSMAssociation`.

**Tools for PowerShell V4**
**Example 1: This example associates a configuration document with an instance, using instance IDs.**

```
New-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"
```
**Output:**

```
Name                  : AWS-UpdateSSMAgent
InstanceId            : i-0000293ffd8c57862
Date                  : 2/23/2017 6:55:22 PM
Status.Name           : Associated
Status.Date           : 2/20/2015 8:31:11 AM
Status.Message        : Associated with AWS-UpdateSSMAgent
Status.AdditionalInfo :
```
**Example 2: This example associates a configuration document with an instance, using targets.**

```
$target = @{Key="instanceids";Values=@("i-0cb2b964d3e14fd9f")}
New-SSMAssociation -Name "AWS-UpdateSSMAgent" -Target $target
```
**Output:**

```
Name                  : AWS-UpdateSSMAgent
InstanceId            :
Date                  : 3/1/2017 6:22:21 PM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
**Example 3: This example associates a configuration document with an instance, using targets and parameters.**

```
$target = @{Key="instanceids";Values=@("i-0cb2b964d3e14fd9f")}
$params = @{
  "action"="configure"
  "mode"="ec2"
  "optionalConfigurationSource"="ssm"
  "optionalConfigurationLocation"=""
  "optionalRestart"="yes"
}
New-SSMAssociation -Name "Configure-CloudWatch" -AssociationName "CWConfiguration" -Target $target -Parameter $params
```
**Output:**

```
Name                  : Configure-CloudWatch
InstanceId            :
Date                  : 5/17/2018 3:17:44 PM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
**Example 4: This example creates an association with all instances in the region, with `AWS-GatherSoftwareInventory`. It also provides custom files and registry locations in the parameters to collect**

```
$params = [Collections.Generic.Dictionary[String,Collections.Generic.List[String]]]::new()
$params["windowsRegistry"] ='[{"Path":"HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\MachineImage","Recursive":false,"ValueNames":["AMIName"]}]'
$params["files"] = '[{"Path":"C:\Program Files","Pattern":["*.exe"],"Recursive":true}, {"Path":"C:\ProgramData","Pattern":["*.log"],"Recursive":true}]'
New-SSMAssociation -AssociationName new-in-mum -Name AWS-GatherSoftwareInventory -Target @{Key="instanceids";Values="*"} -Parameter $params -region ap-south-1 -ScheduleExpression "rate(720 minutes)"
```
**Output:**

```
Name                  : AWS-GatherSoftwareInventory
InstanceId            :
Date                  : 6/9/2019 8:57:56 AM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
+  For API details, see [CreateAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMAssociationFromBatch`
<a name="ssm_CreateAssociationBatch_powershell_topic"></a>

The following code example shows how to use `New-SSMAssociationFromBatch`.

**Tools for PowerShell V4**
**Example 1: This example associates a configuration document with multiple instances. The output returns a list of successful and failed operations, if applicable.**

```
$option1 = @{InstanceId="i-0cb2b964d3e14fd9f";Name=@("AWS-UpdateSSMAgent")}
$option2 = @{InstanceId="i-0000293ffd8c57862";Name=@("AWS-UpdateSSMAgent")}
New-SSMAssociationFromBatch -Entry $option1,$option2
```
**Output:**

```
Failed  Successful
------  ----------
{}      {Amazon.SimpleSystemsManagement.Model.FailedCreateAssociation, Amazon.SimpleSystemsManagement.Model.FailedCreateAsso...
```
**Example 2: This example will show the full details of a successful operation.**

```
$option1 = @{InstanceId="i-0cb2b964d3e14fd9f";Name=@("AWS-UpdateSSMAgent")}
$option2 = @{InstanceId="i-0000293ffd8c57862";Name=@("AWS-UpdateSSMAgent")}
(New-SSMAssociationFromBatch -Entry $option1,$option2).Successful
```
+  For API details, see [CreateAssociationBatch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMDocument`
<a name="ssm_CreateDocument_powershell_topic"></a>

The following code example shows how to use `New-SSMDocument`.

**Tools for PowerShell V4**
**Example 1: This example creates a document in your account. The document must be in JSON format. For more information about writing a configuration document, see Configuration Document in the SSM API Reference.**

```
New-SSMDocument -Content (Get-Content -Raw "c:\temp\RunShellScript.json") -Name "RunShellScript" -DocumentType "Command"
```
**Output:**

```
CreatedDate     : 3/1/2017 1:21:33 AM
DefaultVersion  : 1
Description     : Run an updated script
DocumentType    : Command
DocumentVersion : 1
Hash            : 1d5ce820e999ff051eb4841ed887593daf77120fd76cae0d18a53cc42e4e22c1
HashType        : Sha256
LatestVersion   : 1
Name            : RunShellScript
Owner           : 809632081692
Parameters      : {commands}
PlatformTypes   : {Linux}
SchemaVersion   : 2.0
Sha1            :
Status          : Creating
```
+  For API details, see [CreateDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMMaintenanceWindow`
<a name="ssm_CreateMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `New-SSMMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example creates a new maintenance window with the specified name that runs at 4 PM on every Tuesday for 4 hours, with a 1 hour cutoff, and that allows unassociated targets.**

```
New-SSMMaintenanceWindow -Name "MyMaintenanceWindow" -Duration 4 -Cutoff 1 -AllowUnassociatedTarget $true -Schedule "cron(0 16 ? * TUE *)"
```
**Output:**

```
mw-03eb53e1ea7383998
```
+  For API details, see [CreateMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-SSMPatchBaseline`
<a name="ssm_CreatePatchBaseline_powershell_topic"></a>

The following code example shows how to use `New-SSMPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example creates a patch baseline that approves patches, seven days after they are released by Microsoft, for managed instances running Windows Server 2019 in a production environment.**

```
$rule = New-Object Amazon.SimpleSystemsManagement.Model.PatchRule
$rule.ApproveAfterDays = 7

$ruleFilters = New-Object Amazon.SimpleSystemsManagement.Model.PatchFilterGroup

$patchFilter = New-Object Amazon.SimpleSystemsManagement.Model.PatchFilter
$patchFilter.Key="PRODUCT"
$patchFilter.Values="WindowsServer2019"

$severityFilter = New-Object Amazon.SimpleSystemsManagement.Model.PatchFilter
$severityFilter.Key="MSRC_SEVERITY"
$severityFilter.Values.Add("Critical")
$severityFilter.Values.Add("Important")
$severityFilter.Values.Add("Moderate")

$classificationFilter = New-Object Amazon.SimpleSystemsManagement.Model.PatchFilter
$classificationFilter.Key = "CLASSIFICATION"
$classificationFilter.Values.Add( "SecurityUpdates" )
$classificationFilter.Values.Add( "Updates" )
$classificationFilter.Values.Add( "UpdateRollups" )
$classificationFilter.Values.Add( "CriticalUpdates" )

$ruleFilters.PatchFilters.Add($severityFilter)
$ruleFilters.PatchFilters.Add($classificationFilter)
$ruleFilters.PatchFilters.Add($patchFilter)
$rule.PatchFilterGroup = $ruleFilters

New-SSMPatchBaseline -Name "Production-Baseline-Windows2019" -Description "Baseline containing all updates approved for production systems" -ApprovalRules_PatchRule $rule
```
**Output:**

```
pb-0z4z6221c4296b23z
```
+  For API details, see [CreatePatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-SSMDefaultPatchBaseline`
<a name="ssm_RegisterDefaultPatchBaseline_powershell_topic"></a>

The following code example shows how to use `Register-SSMDefaultPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example registers a patch baseline as the default patch baseline.**

```
Register-SSMDefaultPatchBaseline -BaselineId "pb-03da896ca3b68b639"
```
**Output:**

```
pb-03da896ca3b68b639
```
+  For API details, see [RegisterDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-SSMPatchBaselineForPatchGroup`
<a name="ssm_RegisterPatchBaselineForPatchGroup_powershell_topic"></a>

The following code example shows how to use `Register-SSMPatchBaselineForPatchGroup`.

**Tools for PowerShell V4**
**Example 1: This example registers a patch baseline for a patch group.**

```
Register-SSMPatchBaselineForPatchGroup -BaselineId "pb-03da896ca3b68b639" -PatchGroup "Production"
```
**Output:**

```
BaselineId           PatchGroup
----------           ----------
pb-03da896ca3b68b639 Production
```
+  For API details, see [RegisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-SSMTargetWithMaintenanceWindow`
<a name="ssm_RegisterTargetWithMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Register-SSMTargetWithMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example registers an instance with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"
```
**Output:**

```
d8e47760-23ed-46a5-9f28-927337725398
```
**Example 2: This example registers multiple instances with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862","i-0cb2b964d3e14fd9f")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"
```
**Output:**

```
6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```
**Example 3: This example registers an instance with a maintenance window using EC2 tags.**

```
$option1 = @{Key="tag:Environment";Values=@("Production")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Production Web Servers" -ResourceType "INSTANCE"
```
**Output:**

```
2994977e-aefb-4a71-beac-df620352f184
```
+  For API details, see [RegisterTargetWithMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-SSMTaskWithMaintenanceWindow`
<a name="ssm_RegisterTaskWithMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Register-SSMTaskWithMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example registers a task with a maintenance window using an instance ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

Register-SSMTaskWithMaintenanceWindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="InstanceIds";Values="i-0000293ffd8c57862" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters
```
**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```
**Example 2: This example registers a task with a maintenance window using a target ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

register-ssmtaskwithmaintenancewindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="WindowTargetIds";Values="350d44e6-28cc-44e2-951f-4b2c985838f6" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters
```
**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```
**Example 3: This example creates a parameter object for the run command document `AWS-RunPowerShellScript` and creates a task with given maintenance window using target ID. The return output is the task ID.**

```
$parameters = [Collections.Generic.Dictionary[String,Collections.Generic.List[String]]]::new()
$parameters.Add("commands",@("ipconfig","dir env:\computername"))
$parameters.Add("executionTimeout",@(3600))

$props = @{
    WindowId = "mw-0123e4cce56ff78ae"
    ServiceRoleArn = "arn:aws:iam::123456789012:role/MaintenanceWindowsRole"
    MaxConcurrency = 1
    MaxError = 1
    TaskType = "RUN_COMMAND"
    TaskArn = "AWS-RunPowerShellScript"
    Target = @{Key="WindowTargetIds";Values="fe1234ea-56d7-890b-12f3-456b789bee0f"}
    Priority = 1
    RunCommand_Parameter = $parameters
    Name = "set-via-cmdlet"
}

Register-SSMTaskWithMaintenanceWindow @props
```
**Output:**

```
f1e2ef34-5678-12e3-456a-12334c5c6cbe
```
**Example 4: This example registers an AWS Systems Manager Automation task by using a document named `Create-Snapshots`.**

```
$automationParameters = @{}
$automationParameters.Add( "instanceId", @("{{ TARGET_ID }}") )
$automationParameters.Add( "AutomationAssumeRole", @("{arn:aws:iam::111111111111:role/AutomationRole}") )
$automationParameters.Add( "SnapshotTimeout", @("PT20M") )
Register-SSMTaskWithMaintenanceWindow -WindowId mw-123EXAMPLE456`
    -ServiceRoleArn "arn:aws:iam::123456789012:role/MW-Role"`
    -MaxConcurrency 1 -MaxError 1 -TaskArn "CreateVolumeSnapshots"`
    -Target @{ Key="WindowTargetIds";Values="4b5acdf4-946c-4355-bd68-4329a43a5fd1" }`
    -TaskType "AUTOMATION"`
    -Priority 4`
    -Automation_DocumentVersion '$DEFAULT' -Automation_Parameter $automationParameters -Name "Create-Snapshots"
```
+  For API details, see [RegisterTaskWithMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMActivation`
<a name="ssm_DeleteActivation_powershell_topic"></a>

The following code example shows how to use `Remove-SSMActivation`.

**Tools for PowerShell V4**
**Example 1: This example deletes an activation. There is no output if the command succeeds.**

```
Remove-SSMActivation -ActivationId "08e51e79-1e36-446c-8e63-9458569c1363"
```
+  For API details, see [DeleteActivation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMAssociation`
<a name="ssm_DeleteAssociation_powershell_topic"></a>

The following code example shows how to use `Remove-SSMAssociation`.

**Tools for PowerShell V4**
**Example 1: This example deletes the association between an instance and a document. There is no output if the command succeeds.**

```
Remove-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"
```
+  For API details, see [DeleteAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMDocument`
<a name="ssm_DeleteDocument_powershell_topic"></a>

The following code example shows how to use `Remove-SSMDocument`.

**Tools for PowerShell V4**
**Example 1: This example deletes a document. There is no output if the command succeeds.**

```
Remove-SSMDocument -Name "RunShellScript"
```
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMMaintenanceWindow`
<a name="ssm_DeleteMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Remove-SSMMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example removes a maintenance window.**

```
Remove-SSMMaintenanceWindow -WindowId "mw-06d59c1a07c022145"
```
**Output:**

```
mw-06d59c1a07c022145
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMParameter`
<a name="ssm_DeleteParameter_powershell_topic"></a>

The following code example shows how to use `Remove-SSMParameter`.

**Tools for PowerShell V4**
**Example 1: This example deletes a parameter. There is no output if the command succeeds.**

```
Remove-SSMParameter -Name "helloWorld"
```
+  For API details, see [DeleteParameter](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMPatchBaseline`
<a name="ssm_DeletePatchBaseline_powershell_topic"></a>

The following code example shows how to use `Remove-SSMPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example deletes a patch baseline.**

```
Remove-SSMPatchBaseline -BaselineId "pb-045f10b4f382baeda"
```
**Output:**

```
pb-045f10b4f382baeda
```
+  For API details, see [DeletePatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-SSMResourceTag`
<a name="ssm_RemoveTagsFromResource_powershell_topic"></a>

The following code example shows how to use `Remove-SSMResourceTag`.

**Tools for PowerShell V4**
**Example 1: This example removes a tag from a maintenance window. There is no output if the command succeeds.**

```
Remove-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -TagKey "Production"
```
+  For API details, see [RemoveTagsFromResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Send-SSMCommand`
<a name="ssm_SendCommand_powershell_topic"></a>

The following code example shows how to use `Send-SSMCommand`.

**Tools for PowerShell V4**
**Example 1: This example runs an echo command on a target instance.**

```
Send-SSMCommand -DocumentName "AWS-RunPowerShellScript" -Parameter @{commands = "echo helloWorld"} -Target @{Key="instanceids";Values=@("i-0cb2b964d3e14fd9f")}
```
**Output:**

```
CommandId          : d8d190fc-32c1-4d65-a0df-ff5ff3965524
Comment            :
CompletedCount     : 0
DocumentName       : AWS-RunPowerShellScript
ErrorCount         : 0
ExpiresAfter       : 3/7/2017 10:48:37 PM
InstanceIds        : {}
MaxConcurrency     : 50
MaxErrors          : 0
NotificationConfig : Amazon.SimpleSystemsManagement.Model.NotificationConfig
OutputS3BucketName :
OutputS3KeyPrefix  :
OutputS3Region     :
Parameters         : {[commands, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
RequestedDateTime  : 3/7/2017 9:48:37 PM
ServiceRole        :
Status             : Pending
StatusDetails      : Pending
TargetCount        : 0
Targets            : {instanceids}
```
**Example 2: This example shows how to run a command that accepts nested parameters.**

```
Send-SSMCommand -DocumentName "AWS-RunRemoteScript" -Parameter @{ sourceType="GitHub";sourceInfo='{"owner": "me","repository": "amazon-ssm","path": "Examples/Install-Win32OpenSSH"}'; "commandLine"=".\Install-Win32OpenSSH.ps1"} -InstanceId i-0cb2b964d3e14fd9f
```
+  For API details, see [SendCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Start-SSMAutomationExecution`
<a name="ssm_StartAutomationExecution_powershell_topic"></a>

The following code example shows how to use `Start-SSMAutomationExecution`.

**Tools for PowerShell V4**
**Example 1: This example runs a document specifying an Automation role, an AMI source ID, and an Amazon EC2 instance role.**

```
Start-SSMAutomationExecution -DocumentName AWS-UpdateLinuxAmi -Parameter @{'AutomationAssumeRole'='arn:aws:iam::123456789012:role/SSMAutomationRole';'SourceAmiId'='ami-f173cc91';'InstanceIamRole'='EC2InstanceRole'}
```
**Output:**

```
3a532a4f-0382-11e7-9df7-6f11185f6dd1
```
+  For API details, see [StartAutomationExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Start-SSMSession`
<a name="ssm_StartSession_powershell_topic"></a>

The following code example shows how to use `Start-SSMSession`.

**Tools for PowerShell V4**
**Example 1: This example initiates a connection to a target for a Session Manager session, enabling port forwarding.**

```
Start-SSMSession -Target 'i-064578e5e7454488f' -DocumentName 'AWS-StartPortForwardingSession' -Parameter @{ localPortNumber = '8080'; portNumber = '80' }
```
**Output:**

```
SessionId    StreamUrl
----------    ----------
random-id0    wss://ssmmessages.amazonaws.com/v1/data-channel/random-id
```
+  For API details, see [StartSession](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-SSMAutomationExecution`
<a name="ssm_StopAutomationExecution_powershell_topic"></a>

The following code example shows how to use `Stop-SSMAutomationExecution`.

**Tools for PowerShell V4**
**Example 1: This example stops an Automation Execution. There is no output if the command succeeds.**

```
Stop-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"
```
+  For API details, see [StopAutomationExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-SSMCommand`
<a name="ssm_CancelCommand_powershell_topic"></a>

The following code example shows how to use `Stop-SSMCommand`.

**Tools for PowerShell V4**
**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"
```
+  For API details, see [CancelCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-SSMManagedInstance`
<a name="ssm_DeregisterManagedInstance_powershell_topic"></a>

The following code example shows how to use `Unregister-SSMManagedInstance`.

**Tools for PowerShell V4**
**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"
```
+  For API details, see [DeregisterManagedInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-SSMPatchBaselineForPatchGroup`
<a name="ssm_DeregisterPatchBaselineForPatchGroup_powershell_topic"></a>

The following code example shows how to use `Unregister-SSMPatchBaselineForPatchGroup`.

**Tools for PowerShell V4**
**Example 1: This example deregisters a patch group from a patch baseline.**

```
Unregister-SSMPatchBaselineForPatchGroup -BaselineId "pb-045f10b4f382baeda" -PatchGroup "Production"
```
**Output:**

```
BaselineId           PatchGroup
----------           ----------
pb-045f10b4f382baeda Production
```
+  For API details, see [DeregisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-SSMTargetFromMaintenanceWindow`
<a name="ssm_DeregisterTargetFromMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Unregister-SSMTargetFromMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example removes a target from a maintenance window.**

```
Unregister-SSMTargetFromMaintenanceWindow -WindowTargetId "6ab5c208-9fc4-4697-84b7-b02a6cc25f7d" -WindowId "mw-06cf17cbefcb4bf4f"
```
**Output:**

```
WindowId             WindowTargetId
--------             --------------
mw-06cf17cbefcb4bf4f 6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```
+  For API details, see [DeregisterTargetFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-SSMTaskFromMaintenanceWindow`
<a name="ssm_DeregisterTaskFromMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Unregister-SSMTaskFromMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example removes a task from a maintenance window.**

```
Unregister-SSMTaskFromMaintenanceWindow -WindowTaskId "f34a2c47-ddfd-4c85-a88d-72366b69af1b" -WindowId "mw-03a342e62c96d31b0"
```
**Output:**

```
WindowId             WindowTaskId
--------             ------------
mw-03a342e62c96d31b0 f34a2c47-ddfd-4c85-a88d-72366b69af1b
```
+  For API details, see [DeregisterTaskFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMAssociation`
<a name="ssm_UpdateAssociation_powershell_topic"></a>

The following code example shows how to use `Update-SSMAssociation`.

**Tools for PowerShell V4**
**Example 1: This example updates an association with a new document version.**

```
Update-SSMAssociation -AssociationId "93285663-92df-44cb-9f26-2292d4ecc439" -DocumentVersion "1"
```
**Output:**

```
Name                  : AWS-UpdateSSMAgent
InstanceId            :
Date                  : 3/1/2017 6:22:21 PM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
+  For API details, see [UpdateAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMAssociationStatus`
<a name="ssm_UpdateAssociationStatus_powershell_topic"></a>

The following code example shows how to use `Update-SSMAssociationStatus`.

**Tools for PowerShell V4**
**Example 1: This example updates the association status of the association between an instance and a configuration document.**

```
Update-SSMAssociationStatus -Name "AWS-UpdateSSMAgent" -InstanceId "i-0000293ffd8c57862" -AssociationStatus_Date "2015-02-20T08:31:11Z" -AssociationStatus_Name "Pending" -AssociationStatus_Message "temporary_status_change" -AssociationStatus_AdditionalInfo "Additional-Config-Needed"
```
**Output:**

```
Name                  : AWS-UpdateSSMAgent
InstanceId            : i-0000293ffd8c57862
Date                  : 2/23/2017 6:55:22 PM
Status.Name           : Pending
Status.Date           : 2/20/2015 8:31:11 AM
Status.Message        : temporary_status_change
Status.AdditionalInfo : Additional-Config-Needed
```
+  For API details, see [UpdateAssociationStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMDocument`
<a name="ssm_UpdateDocument_powershell_topic"></a>

The following code example shows how to use `Update-SSMDocument`.

**Tools for PowerShell V4**
**Example 1: This creates a new version of a document with the updated contents of the json file you specify. The document must be in JSON format. You can obtain the document version with the "Get-SSMDocumentVersionList" cmdlet.**

```
Update-SSMDocument -Name RunShellScript -DocumentVersion "1" -Content (Get-Content -Raw "c:\temp\RunShellScript.json")
```
**Output:**

```
CreatedDate     : 3/1/2017 2:59:17 AM
DefaultVersion  : 1
Description     : Run an updated script
DocumentType    : Command
DocumentVersion : 2
Hash            : 1d5ce820e999ff051eb4841ed887593daf77120fd76cae0d18a53cc42e4e22c1
HashType        : Sha256
LatestVersion   : 2
Name            : RunShellScript
Owner           : 809632081692
Parameters      : {commands}
PlatformTypes   : {Linux}
SchemaVersion   : 2.0
Sha1            :
Status          : Updating
```
+  For API details, see [UpdateDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMDocumentDefaultVersion`
<a name="ssm_UpdateDocumentDefaultVersion_powershell_topic"></a>

The following code example shows how to use `Update-SSMDocumentDefaultVersion`.

**Tools for PowerShell V4**
**Example 1: This updates the default version of a document. You can obtain the available document versions with the "Get-SSMDocumentVersionList" cmdlet.**

```
Update-SSMDocumentDefaultVersion -Name "RunShellScript" -DocumentVersion "2"
```
**Output:**

```
DefaultVersion Name
-------------- ----
2              RunShellScript
```
+  For API details, see [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMMaintenanceWindow`
<a name="ssm_UpdateMaintenanceWindow_powershell_topic"></a>

The following code example shows how to use `Update-SSMMaintenanceWindow`.

**Tools for PowerShell V4**
**Example 1: This example updates the name of a maintenance window.**

```
Update-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d" -Name "My-Renamed-MW"
```
**Output:**

```
AllowUnassociatedTargets : False
Cutoff                   : 1
Duration                 : 2
Enabled                  : True
Name                     : My-Renamed-MW
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
**Example 2: This example enables a maintenance window.**

```
Update-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d" -Enabled $true
```
**Output:**

```
AllowUnassociatedTargets : False
Cutoff                   : 1
Duration                 : 2
Enabled                  : True
Name                     : My-Renamed-MW
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
**Example 3: This example disables a maintenance window.**

```
Update-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d" -Enabled $false
```
**Output:**

```
AllowUnassociatedTargets : False
Cutoff                   : 1
Duration                 : 2
Enabled                  : False
Name                     : My-Renamed-MW
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
+  For API details, see [UpdateMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMManagedInstanceRole`
<a name="ssm_UpdateManagedInstanceRole_powershell_topic"></a>

The following code example shows how to use `Update-SSMManagedInstanceRole`.

**Tools for PowerShell V4**
**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"
```
+  For API details, see [UpdateManagedInstanceRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-SSMPatchBaseline`
<a name="ssm_UpdatePatchBaseline_powershell_topic"></a>

The following code example shows how to use `Update-SSMPatchBaseline`.

**Tools for PowerShell V4**
**Example 1: This example adds two patches as rejected and one patch as approved to an existing patch baseline.**

```
Update-SSMPatchBaseline -BaselineId "pb-03da896ca3b68b639" -RejectedPatch "KB2032276","MS10-048" -ApprovedPatch "KB2124261"
```
**Output:**

```
ApprovalRules   : Amazon.SimpleSystemsManagement.Model.PatchRuleGroup
ApprovedPatches : {KB2124261}
BaselineId      : pb-03da896ca3b68b639
CreatedDate     : 3/3/2017 5:02:19 PM
Description     : Baseline containing all updates approved for production systems
GlobalFilters   : Amazon.SimpleSystemsManagement.Model.PatchFilterGroup
ModifiedDate    : 3/3/2017 5:22:10 PM
Name            : Production-Baseline
RejectedPatches : {KB2032276, MS10-048}
```
+  For API details, see [UpdatePatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-SSMComplianceItem`
<a name="ssm_PutComplianceItems_powershell_topic"></a>

The following code example shows how to use `Write-SSMComplianceItem`.

**Tools for PowerShell V4**
**Example 1: This example writes a custom compliance item for the given managed instance**

```
$item = [Amazon.SimpleSystemsManagement.Model.ComplianceItemEntry]::new()
$item.Id = "07Jun2019-3"
$item.Severity="LOW"
$item.Status="COMPLIANT"
$item.Title="Fin-test-1 - custom"
Write-SSMComplianceItem -ResourceId mi-012dcb3ecea45b678 -ComplianceType Custom:VSSCompliant2 -ResourceType ManagedInstance -Item $item -ExecutionSummary_ExecutionTime "07-Jun-2019"
```
+  For API details, see [PutComplianceItems](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-SSMInventory`
<a name="ssm_PutInventory_powershell_topic"></a>

The following code example shows how to use `Write-SSMInventory`.

**Tools for PowerShell V4**
**Example 1: This example assigns rack location information to an instance. There is no output if the command succeeds.**

```
$data = New-Object "System.Collections.Generic.Dictionary[System.String,System.String]"
$data.Add("RackLocation", "Bay B/Row C/Rack D/Shelf F")

$items = New-Object "System.Collections.Generic.List[System.Collections.Generic.Dictionary[System.String, System.String]]"
$items.Add($data)

$customInventoryItem = New-Object Amazon.SimpleSystemsManagement.Model.InventoryItem
$customInventoryItem.CaptureTime = "2016-08-22T10:01:01Z"
$customInventoryItem.Content = $items
$customInventoryItem.TypeName = "Custom:TestRackInfo2"
$customInventoryItem.SchemaVersion = "1.0"

$inventoryItems = @($customInventoryItem)

Write-SSMInventory -InstanceId "i-0cb2b964d3e14fd9f" -Item $inventoryItems
```
+  For API details, see [PutInventory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-SSMParameter`
<a name="ssm_PutParameter_powershell_topic"></a>

The following code example shows how to use `Write-SSMParameter`.

**Tools for PowerShell V4**
**Example 1: This example creates a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "helloWorld"
```
**Example 2: This example changes a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "Good day, Sunshine!" -Overwrite $true
```
+  For API details, see [PutParameter](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
