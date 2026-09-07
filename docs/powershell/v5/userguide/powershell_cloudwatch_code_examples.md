---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_cloudwatch_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# CloudWatch examples using Tools for PowerShell V5
<a name="powershell_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with CloudWatch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CWDashboard`
<a name="cloudwatch_GetDashboard_powershell_topic"></a>

The following code example shows how to use `Get-CWDashboard`.

**Tools for PowerShell V5**
**Example 1: Returns the arn the body of the specified dashboard.**

```
Get-CWDashboard -DashboardName Dashboard1
```
**Output:**

```
DashboardArn                                          DashboardBody
------------                                          -------------
arn:aws:cloudwatch::123456789012:dashboard/Dashboard1 {...
```
+  For API details, see [GetDashboard](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CWDashboardList`
<a name="cloudwatch_ListDashboards_powershell_topic"></a>

The following code example shows how to use `Get-CWDashboardList`.

**Tools for PowerShell V5**
**Example 1: Returns the collection of dashboards for your account.**

```
Get-CWDashboardList
```
**Output:**

```
DashboardArn DashboardName LastModified        Size
------------ ------------- ------------        ----
arn:...      Dashboard1    7/6/2017 8:14:15 PM 252
```
**Example 2: Returns the collection of dashboards for your account whose names start with the prefix 'dev'.**

```
Get-CWDashboardList -DashboardNamePrefix dev
```
+  For API details, see [ListDashboards](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CWDashboard`
<a name="cloudwatch_DeleteDashboards_powershell_topic"></a>

The following code example shows how to use `Remove-CWDashboard`.

**Tools for PowerShell V5**
**Example 1: Deletes the specified dashboard, promoting for confirmation before proceeding. To bypass confirmation add the -Force switch to the command.**

```
Remove-CWDashboard -DashboardName Dashboard1
```
+  For API details, see [DeleteDashboards](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-CWDashboard`
<a name="cloudwatch_PutDashboard_powershell_topic"></a>

The following code example shows how to use `Write-CWDashboard`.

**Tools for PowerShell V5**
**Example 1: Creates or updates the dashboard named 'Dashboard1' to include two metric widgets side by side.**

```
$dashBody = @"
{
    "widgets":[
        {
             "type":"metric",
             "x":0,
             "y":0,
             "width":12,
             "height":6,
             "properties":{
                "metrics":[
                   [
                      "AWS/EC2",
                      "CPUUtilization",
                      "InstanceId",
                      "i-012345"
                   ]
                ],
                "period":300,
                "stat":"Average",
                "region":"us-east-1",
                "title":"EC2 Instance CPU"
             }
        },
        {
             "type":"metric",
             "x":12,
             "y":0,
             "width":12,
             "height":6,
             "properties":{
                "metrics":[
                   [
                      "AWS/S3",
                      "BucketSizeBytes",
                      "BucketName",
                      "amzn-s3-demo-bucket"
                   ]
                ],
                "period":86400,
                "stat":"Maximum",
                "region":"us-east-1",
                "title":"amzn-s3-demo-bucket bytes"
            }
        }
    ]
}
"@

Write-CWDashboard -DashboardName Dashboard1 -DashboardBody $dashBody
```
**Example 2: Creates or updates the dashboard, piping the content describing the dashboard into the cmdlet.**

```
$dashBody = @"
{
...
}
"@

$dashBody | Write-CWDashboard -DashboardName Dashboard1
```
+  For API details, see [PutDashboard](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-CWMetricData`
<a name="cloudwatch_PutMetricData_powershell_topic"></a>

The following code example shows how to use `Write-CWMetricData`.

**Tools for PowerShell V5**
**Example 1: Creates a new MetricDatum object, and writes it to Amazon Web Services CloudWatch Metrics.**

```
### Create a MetricDatum .NET object
$Metric = New-Object -TypeName Amazon.CloudWatch.Model.MetricDatum
$Metric.Timestamp = [DateTime]::UtcNow
$Metric.MetricName = 'CPU'
$Metric.Value = 50

### Write the metric data to the CloudWatch service
Write-CWMetricData -Namespace instance1 -MetricData $Metric
```
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
