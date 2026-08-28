---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloudtrail_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# CloudTrail examples using Tools for PowerShell V4
<a name="powershell_cloudtrail_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with CloudTrail.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Find-CTEvent`
<a name="cloudtrail_LookupEvents_powershell_topic"></a>

The following code example shows how to use `Find-CTEvent`.

**Tools for PowerShell V4**
**Example 1: Returns all events that have occurred over the last seven days. The cmdlet by default automatically makes multiple calls to deliver all events, exiting when the service indicates no further data is available.**

```
Find-CTEvent
```
**Example 2: Returns all events that have occurred over the last seven days specifying a region that is not the current shell default.**

```
Find-CTEvent -Region eu-central-1
```
**Example 3: Returns all events that are associated with the RunInstances API call.**

```
Find-CTEvent -LookupAttribute @{ AttributeKey="EventName"; AttributeValue="RunInstances" }
```
**Example 4: Returns the first 5 available events.**

```
Find-CTEvent -MaxResult 5
```
+  For API details, see [LookupEvents](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CTTrail`
<a name="cloudtrail_DescribeTrails_powershell_topic"></a>

The following code example shows how to use `Get-CTTrail`.

**Tools for PowerShell V4**
**Example 1: Returns the settings of all trails associated with the current region for your account.**

```
Get-CTTrail
```
**Example 2: Returns the settings for the specified trails.**

```
Get-CTTrail -TrailNameList trail1,trail2
```
**Example 3: Returns the settings for the specified trails that were created in a region other than the current shell default (in this case the Frankfurt (eu-central-1) region).**

```
Get-CTTrail -TrailNameList trailABC,trailDEF -Region eu-central-1
```
+  For API details, see [DescribeTrails](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CTTrailStatus`
<a name="cloudtrail_GetTrailStatus_powershell_topic"></a>

The following code example shows how to use `Get-CTTrailStatus`.

**Tools for PowerShell V4**
**Example 1: Returns status information for the trail with name 'myExampleTrail'. Returned data includes information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for the trail. This example assumes the trail was created in the same region as the current shell default.**

```
Get-CTTrailStatus -Name myExampleTrail
```
**Example 2: Returns status information for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Get-CTTrailStatus -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [GetTrailStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CTTrail`
<a name="cloudtrail_CreateTrail_powershell_topic"></a>

The following code example shows how to use `New-CTTrail`.

**Tools for PowerShell V4**
**Example 1: Creates a trail that will use the bucket 'amzn-s3-demo-bucket' for log file storage.**

```
New-CTTrail -Name "awscloudtrail-example" -S3BucketName "amzn-s3-demo-bucket"
```
**Example 2: Creates a trail that will use the bucket 'amzn-s3-demo-bucket' for log file storage. The S3 objects representing the logs will have a common key prefix of 'mylogs'. When new logs are delivered to the bucket a notification will be sent to the SNS topic 'mlog-deliverytopic'. This example using splatting to supply the parameter values to the cmdlet.**

```
$params = @{
    Name="awscloudtrail-example"
    S3BucketName="amzn-s3-demo-bucket"
    S3KeyPrefix="mylogs"
    SnsTopicName="mlog-deliverytopic"
}
New-CTTrail @params
```
+  For API details, see [CreateTrail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-CTTrail`
<a name="cloudtrail_DeleteTrail_powershell_topic"></a>

The following code example shows how to use `Remove-CTTrail`.

**Tools for PowerShell V4**
**Example 1: Deletes the specified trail. You will be prompted for confirmation before the command is run. To suppress confirmation, add the -Force switch parameter.**

```
Remove-CTTrail -Name "awscloudtrail-example"
```
+  For API details, see [DeleteTrail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Start-CTLogging`
<a name="cloudtrail_StartLogging_powershell_topic"></a>

The following code example shows how to use `Start-CTLogging`.

**Tools for PowerShell V4**
**Example 1: Starts the recording of AWS API calls and log file delivery for the trail named 'myExampleTrail'. This example assumes the trail was created in the same region as the current shell default.**

```
Start-CTLogging -Name myExampleTrail
```
**Example 2: Starts the recording of AWS API calls and log file delivery for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Start-CTLogging -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [StartLogging](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-CTLogging`
<a name="cloudtrail_StopLogging_powershell_topic"></a>

The following code example shows how to use `Stop-CTLogging`.

**Tools for PowerShell V4**
**Example 1: Suspends the recording of AWS API calls and log file delivery for the trail named 'myExampleTrail'. This example assumes the trail was created in the same region as the current shell default.**

```
Stop-CTLogging -Name myExampleTrail
```
**Example 2: Suspends the recording of AWS API calls and log file delivery for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Stop-CTLogging -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [StopLogging](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-CTTrail`
<a name="cloudtrail_UpdateTrail_powershell_topic"></a>

The following code example shows how to use `Update-CTTrail`.

**Tools for PowerShell V4**
**Example 1: Updates the specified trail so that global service events (such as those from IAM) are recorded and changes the common key prefix of the log files going forwards to be 'globallogs'.**

```
Update-CTTrail -Name "awscloudtrail-example" -IncludeGlobalServiceEvents $true -S3KeyPrefix "globallogs"
```
**Example 2: Updates the specified trail so notifications about new log deliveries are sent to the specified SNS topic.**

```
Update-CTTrail -Name "awscloudtrail-example" -SnsTopicName "mlog-deliverytopic2"
```
**Example 3: Updates the specified trail so logs are delivered to a different bucket.**

```
Update-CTTrail -Name "awscloudtrail-example" -S3BucketName "otherlogs"
```
+  For API details, see [UpdateTrail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
