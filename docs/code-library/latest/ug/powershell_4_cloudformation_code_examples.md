---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_cloudformation_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudFormation examples using Tools for PowerShell V4
<a name="powershell_4_cloudformation_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with CloudFormation.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CFNStack`
<a name="cloudformation_DescribeStacks_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Returns a collection of Stack instances describing all of the user's stacks.**

```
Get-CFNStack
```
**Example 2: Returns a Stack instance describing the specified stack**

```
Get-CFNStack -StackName "myStack"
```
+  For API details, see [DescribeStacks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNStackEvent`
<a name="cloudformation_DescribeStackEvents_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStackEvent`.

**Tools for PowerShell V4**
**Example 1: Returns all stack related events for the specified stack.**

```
Get-CFNStackEvent -StackName "myStack"
```
+  For API details, see [DescribeStackEvents](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNStackResource`
<a name="cloudformation_DescribeStackResource_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStackResource`.

**Tools for PowerShell V4**
**Example 1: Returns the description of a resource identified in the template associated with the specified stack by the logical ID "MyDBInstance".**

```
Get-CFNStackResource -StackName "myStack" -LogicalResourceId "MyDBInstance"
```
+  For API details, see [DescribeStackResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNStackResourceList`
<a name="cloudformation_DescribeStackResources_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStackResourceList`.

**Tools for PowerShell V4**
**Example 1: Returns the AWS resource descriptions for up to 100 resources associated with the specified stack. To obtain details of all resources associated with a stack use the Get-CFNStackResourceSummary, which also supports manual paging of the results.**

```
Get-CFNStackResourceList -StackName "myStack"
```
**Example 2: Returns the description of the Amazon EC2 instance identified in the template associated with the specified stack by the logical ID "Ec2Instance".**

```
Get-CFNStackResourceList -StackName "myStack" -LogicalResourceId "Ec2Instance"
```
**Example 3: Returns the description of up to 100 resources associated with the stack containing an Amazon EC2 instance identified by instance ID "i-123456". To obtain details of all resources associated with a stack use the Get-CFNStackResourceSummary, which also supports manual paging of the results.**

```
Get-CFNStackResourceList -PhysicalResourceId "i-123456"
```
**Example 4: Returns the description of the Amazon EC2 instance identified by the logical ID "Ec2Instance" in the template for a stack. The stack is identified using the physical resource ID of a resource it contains, in this case also an Amazon EC2 instance with instance ID "i-123456". A different physical resource could also be used to identify the stack depending on the template content, for example an Amazon S3 bucket.**

```
Get-CFNStackResourceList -PhysicalResourceId "i-123456" -LogicalResourceId "Ec2Instance"
```
+  For API details, see [DescribeStackResources](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNStackResourceSummary`
<a name="cloudformation_ListStackResources_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStackResourceSummary`.

**Tools for PowerShell V4**
**Example 1: Returns descriptions of all the resources associated with the specified stack.**

```
Get-CFNStackResourceSummary -StackName "myStack"
```
+  For API details, see [ListStackResources](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNStackSummary`
<a name="cloudformation_ListStacks_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNStackSummary`.

**Tools for PowerShell V4**
**Example 1: Returns summary information for all stacks.**

```
Get-CFNStackSummary
```
**Example 2: Returns summary information for all stacks that are currently being created.**

```
Get-CFNStackSummary -StackStatusFilter "CREATE_IN_PROGRESS"
```
**Example 3: Returns summary information for all stacks that are currently being created or updated.**

```
Get-CFNStackSummary -StackStatusFilter @("CREATE_IN_PROGRESS", "UPDATE_IN_PROGRESS")
```
+  For API details, see [ListStacks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFNTemplate`
<a name="cloudformation_GetTemplate_powershell_4_topic"></a>

The following code example shows how to use `Get-CFNTemplate`.

**Tools for PowerShell V4**
**Example 1: Returns the template associated with the specified stack.**

```
Get-CFNTemplate -StackName "myStack"
```
+  For API details, see [GetTemplate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Measure-CFNTemplateCost`
<a name="cloudformation_EstimateTemplateCost_powershell_4_topic"></a>

The following code example shows how to use `Measure-CFNTemplateCost`.

**Tools for PowerShell V4**
**Example 1: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is obtained from the specified Amazon S3 URL and the single customization parameter applied. The parameter can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
                        -Region us-west-1 `
                        -Parameter @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" }
```
**Example 2: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content and the customization parameters applied (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType'). The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" `
                        -Parameter @( @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" },`
                                      @{ ParameterKey="InstanceType"; ParameterValue="m1.large" })
```
**Example 3: Uses New-Object to build the set of template parameters and returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content, with customization parameters (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType').**

```
$p1 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p1.ParameterKey = "KeyName"
$p1.ParameterValue = "myKeyPairName"

$p2 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p2.ParameterKey = "InstanceType"
$p2.ParameterValue = "m1.large"

Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" -Parameter @( $p1, $p2 )
```
+  For API details, see [EstimateTemplateCost](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CFNStack`
<a name="cloudformation_CreateStack_powershell_4_topic"></a>

The following code example shows how to use `New-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Creates a new stack with the specified name. The template is parsed from the supplied content with customization parameters ('PK1' and 'PK2' represent the names of parameters declared in the template content, 'PV1' and 'PV2' represent the values for those parameters. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'. If creation of the stack fails, it will not be rolled back.**

```
New-CFNStack -StackName "myStack" `
             -TemplateBody "{TEMPLATE CONTENT HERE}" `
             -Parameter @( @{ ParameterKey="PK1"; ParameterValue="PV1" }, @{ ParameterKey="PK2"; ParameterValue="PV2" }) `
             -DisableRollback $true
```
**Example 2: Creates a new stack with the specified name. The template is parsed from the supplied content with customization parameters ('PK1' and 'PK2' represent the names of parameters declared in the template content, 'PV1' and 'PV2' represent the values for those parameters. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'. If creation of the stack fails, it will be rolled back.**

```
$p1 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p1.ParameterKey = "PK1"
$p1.ParameterValue = "PV1"

$p2 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p2.ParameterKey = "PK2"
$p2.ParameterValue = "PV2"

New-CFNStack -StackName "myStack" `
             -TemplateBody "{TEMPLATE CONTENT HERE}" `
             -Parameter @( $p1, $p2 ) `
             -OnFailure "ROLLBACK"
```
**Example 3: Creates a new stack with the specified name. The template is obtained from the Amazon S3 URL with customization parameters ('PK1' represents the name of a parameter declared in the template content, 'PV1' represents the value for the parameter. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'. If creation of the stack fails, it will be rolled back (same as specifying -DisableRollback $false).**

```
New-CFNStack -StackName "myStack" `
             -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
             -Parameter @{ ParameterKey="PK1"; ParameterValue="PV1" }
```
**Example 4: Creates a new stack with the specified name. The template is obtained from the Amazon S3 URL with customization parameters ('PK1' represents the name of a parameter declared in the template content, 'PV1' represents the value for the parameter. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'. If creation of the stack fails, it will be rolled back (same as specifying -DisableRollback $false). The specified notification AENs will receive published stack-related events.**

```
New-CFNStack -StackName "myStack" `
             -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
             -Parameter @{ ParameterKey="PK1"; ParameterValue="PV1" } `
             -NotificationARN @( "arn1", "arn2" )
```
+  For API details, see [CreateStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-CFNStack`
<a name="cloudformation_DeleteStack_powershell_4_topic"></a>

The following code example shows how to use `Remove-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Deletes the specified stack.**

```
Remove-CFNStack -StackName "myStack"
```
+  For API details, see [DeleteStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Resume-CFNUpdateRollback`
<a name="cloudformation_ContinueUpdateRollback_powershell_4_topic"></a>

The following code example shows how to use `Resume-CFNUpdateRollback`.

**Tools for PowerShell V4**
**Example 1: Continues rollback of the named stack, which should be in the state 'UPDATE\_ROLLBACK\_FAILED'. If the continued rollback is successful, the stack will enter state 'UPDATE\_ROLLBACK\_COMPLETE'.**

```
Resume-CFNUpdateRollback -StackName "myStack"
```
+  For API details, see [ContinueUpdateRollback](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-CFNUpdateStack`
<a name="cloudformation_CancelUpdateStack_powershell_4_topic"></a>

The following code example shows how to use `Stop-CFNUpdateStack`.

**Tools for PowerShell V4**
**Example 1: Cancels an update on the specified stack.**

```
Stop-CFNUpdateStack -StackName "myStack"
```
+  For API details, see [CancelUpdateStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Test-CFNStack`
<a name="cloudformation_Test-CFNStack_powershell_4_topic"></a>

The following code example shows how to use `Test-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Tests if the stack has reached one of the states UPDATE\_ROLLBACK\_COMPLETE, CREATE\_COMPLETE, ROLLBACK\_COMPLETE or UPDATE\_COMPLETE.**

```
Test-CFNStack -StackName MyStack
```
**Output:**

```
False
```
**Example 2: Tests if the stack has reached a status of either UPDATE\_COMPLETE or UPDATE\_ROLLBACK\_COMPLETE.**

```
Test-CFNStack -StackName MyStack -Status UPDATE_COMPLETE,UPDATE_ROLLBACK_COMPLETE
```
**Output:**

```
True
```
+  For API details, see [Test-CFNStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Test-CFNTemplate`
<a name="cloudformation_ValidateTemplate_powershell_4_topic"></a>

The following code example shows how to use `Test-CFNTemplate`.

**Tools for PowerShell V4**
**Example 1: Validates the specified template content. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateBody "{TEMPLATE CONTENT HERE}"
```
**Example 2: Validates the specified template accessed via an Amazon S3 URL. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template
```
+  For API details, see [ValidateTemplate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-CFNStack`
<a name="cloudformation_UpdateStack_powershell_4_topic"></a>

The following code example shows how to use `Update-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Updates the stack 'myStack' with the specified template and customization parameters. 'PK1' represents the name of a parameter declared in the template and 'PV1' represents its value. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Update-CFNStack -StackName "myStack" `
                -TemplateBody "{Template Content Here}" `
                -Parameter @{ ParameterKey="PK1"; ParameterValue="PV1" }
```
**Example 2: Updates the stack 'myStack' with the specified template and customization parameters. 'PK1' and 'PK2' represent the names of parameters declared in the template, 'PV1' and 'PV2' represents their requested values. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Update-CFNStack -StackName "myStack" `
                -TemplateBody "{Template Content Here}" `
                -Parameter @( @{ ParameterKey="PK1"; ParameterValue="PV1" }, @{ ParameterKey="PK2"; ParameterValue="PV2" } )
```
**Example 3: Updates the stack 'myStack' with the specified template and customization parameters. 'PK1' represents the name of a parameter declared in the template and 'PV2' represents its value. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Update-CFNStack -StackName "myStack" -TemplateBody "{Template Content Here}" -Parameters @{ ParameterKey="PK1"; ParameterValue="PV1" }
```
**Example 4: Updates the stack 'myStack' with the specified template, obtained from Amazon S3, and customization parameters. 'PK1' and 'PK2' represent the names of parameters declared in the template, 'PV1' and 'PV2' represents their requested values. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Update-CFNStack -StackName "myStack" `
                -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
                -Parameter @( @{ ParameterKey="PK1"; ParameterValue="PV1" }, @{ ParameterKey="PK2"; ParameterValue="PV2" } )
```
**Example 5: Updates the stack 'myStack', which is assumed in this example to contain IAM resources, with the specified template, obtained from Amazon S3, and customization parameters. 'PK1' and 'PK2' represent the names of parameters declared in the template, 'PV1' and 'PV2' represents their requested values. The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'. Stacks containing IAM resources require you to specify the -Capabilities "CAPABILITY\_IAM" parameter otherwise the update will fail with an 'InsufficientCapabilities' error.**

```
Update-CFNStack -StackName "myStack" `
                -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
                -Parameter @( @{ ParameterKey="PK1"; ParameterValue="PV1" }, @{ ParameterKey="PK2"; ParameterValue="PV2" } ) `
                -Capabilities "CAPABILITY_IAM"
```
+  For API details, see [UpdateStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Wait-CFNStack`
<a name="cloudformation_Wait-CFNStack_powershell_4_topic"></a>

The following code example shows how to use `Wait-CFNStack`.

**Tools for PowerShell V4**
**Example 1: Tests if the stack has reached one of the states UPDATE\_ROLLBACK\_COMPLETE, CREATE\_COMPLETE, ROLLBACK\_COMPLETE or UPDATE\_COMPLETE. If the stack is not at one of the states the command sleeps for two seconds before testing status again. This is repeated until the stack reaches one of the requested states or the default timeout period of 60 seconds elapses. If the timeout period is exceeded an exception is thrown. If the stack reaches one of the requested states within the timeout period it is returned to the pipeline.**

```
$stack = Wait-CFNStack -StackName MyStack
```
**Example 2: This example waits for a total of 5 minutes (300 seconds) for the stack to reach either of the specified states. In this example the state is reached before the timeout and therefore the stack object is returned to the pipeline.**

```
Wait-CFNStack -StackName MyStack -Timeout 300 -Status CREATE_COMPLETE,ROLLBACK_COMPLETE
```
**Output:**

```
Capabilities      : {CAPABILITY_IAM}
ChangeSetId       :
CreationTime      : 6/1/2017 9:29:33 AM
Description       : AWS CloudFormation Sample Template ec2_instance_with_instance_profile: Create an EC2 instance with an associated instance profile. **WARNING** This template creates one or more Amazon EC2
                    instances and an Amazon SQS queue. You will be billed for the AWS resources used if you create a stack from this template.
DisableRollback   : False
LastUpdatedTime   : 1/1/0001 12:00:00 AM
NotificationARNs  : {}
Outputs           : {}
Parameters        : {}
RoleARN           :
StackId           : arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/7ea87b50-46e7-11e7-9c9b-503a90a9c4d1
StackName         : MyStack
StackStatus       : CREATE_COMPLETE
StackStatusReason :
Tags              : {}
TimeoutInMinutes  : 0
```
**Example 3: This example shows the error output when a stack does not reach one of the requested states within the timeout period (in this case the default period of 60 seconds).**

```
Wait-CFNStack -StackName MyStack -Status CREATE_COMPLETE,ROLLBACK_COMPLETE
```
**Output:**

```
Wait-CFNStack : Timed out after 60 seconds waiting for CloudFormation stack MyStack in region us-west-2 to reach one of state(s): UPDATE_ROLLBACK_COMPLETE,CREATE_COMPLETE,ROLLBACK_COMPLETE,UPDATE_COMPLETE
At line:1 char:1
+ Wait-CFNStack -StackName MyStack -State CREATE_COMPLETE,ROLLBACK_COMPLETE
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (Amazon.PowerShe...tCFNStackCmdlet:WaitCFNStackCmdlet) [Wait-CFNStack], InvalidOperationException
    + FullyQualifiedErrorId : InvalidOperationException,Amazon.PowerShell.Cmdlets.CFN.WaitCFNStackCmdlet
```
+  For API details, see [Wait-CFNStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
