---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_cloudwatch_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudWatch examples using Tools for PowerShell V4
<a name="powershell_4_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with CloudWatch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CWAlarm`
<a name="cloudwatch_DescribeAlarms_powershell_4_topic"></a>

The following code example shows how to use `Get-CWAlarm`.

**Tools for PowerShell V4**
**Example 1: Returns all the alarms including Composite and Metric Alarms from CloudWatch.**

```
Get-CWAlarm -MaxRecords 1
```
**Output:**

```
CompositeAlarms MetricAlarms         NextToken
--------------- ------------         ---------
                {MetricAlarms-01}    NextToken-01
                {MetricAlarms-02}    NextToken-02
                {MetricAlarms-03}    NextToken-03
```
**Example 2: Returns only the composite alarms data from CloudWatch after setting -AlarmType parameter to CompositeAlarms.**

```
Get-CWAlarm -AlarmType 'CompositeAlarms'
```
**Output:**

```
CompositeAlarms        MetricAlarms NextToken
---------------        ------------ ---------
{CompositeAlarms-01}
{CompositeAlarms-02}
{CompositeAlarms-03}
```
+  For API details, see [DescribeAlarms](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CWDashboard`
<a name="cloudwatch_GetDashboard_powershell_4_topic"></a>

The following code example shows how to use `Get-CWDashboard`.

**Tools for PowerShell V4**
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
+  For API details, see [GetDashboard](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CWDashboardList`
<a name="cloudwatch_ListDashboards_powershell_4_topic"></a>

The following code example shows how to use `Get-CWDashboardList`.

**Tools for PowerShell V4**
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
+  For API details, see [ListDashboards](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-CWDashboard`
<a name="cloudwatch_DeleteDashboards_powershell_4_topic"></a>

The following code example shows how to use `Remove-CWDashboard`.

**Tools for PowerShell V4**
**Example 1: Deletes the specified dashboard, promoting for confirmation before proceeding. To bypass confirmation add the -Force switch to the command.**

```
Remove-CWDashboard -DashboardName Dashboard1
```
+  For API details, see [DeleteDashboards](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-CWDashboard`
<a name="cloudwatch_PutDashboard_powershell_4_topic"></a>

The following code example shows how to use `Write-CWDashboard`.

**Tools for PowerShell V4**
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
+  For API details, see [PutDashboard](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-CWMetricData`
<a name="cloudwatch_PutMetricData_powershell_4_topic"></a>

The following code example shows how to use `Write-CWMetricData`.

**Tools for PowerShell V4**
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
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
