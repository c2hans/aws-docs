---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_GetDashboard_section.html
---

# Use `GetDashboard` with an AWS SDK or CLI
<a name="example_cloudwatch_GetDashboard_section"></a>

The following code examples show how to use `GetDashboard`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Creating a monitoring dashboard with function name as a variable](example_cloudwatch_GettingStarted_031_section.md)
+  [Using property variables in monitoring dashboards to monitor multiple serverless functions](example_iam_GettingStarted_032_section.md)

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get information on a dashboard.
    /// </summary>
    /// <param name="dashboardName">The name of the dashboard.</param>
    /// <returns>A JSON object with dashboard information.</returns>
    public async Task<string> GetDashboard(string dashboardName)
    {
        var dashboardResponse = await _amazonCloudWatch.GetDashboardAsync(
            new GetDashboardRequest()
            {
                DashboardName = dashboardName
            });

        return dashboardResponse.DashboardBody;
    }
```
+  For API details, see [GetDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDashboard) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To retrieve information about a Dashboard**
The following `get-dashboard` example displays information about the dashboard named `Dashboard-A` in the specified account.

```
aws cloudwatch get-dashboard \
    --dashboard-name {{Dashboard-A}}
```
Output:

```
{
    "DashboardArn": "arn:aws:cloudwatch::123456789012:dashboard/Dashboard-A",
    "DashboardBody": "{\"widgets\":[{\"type\":\"metric\",\"x\":0,\"y\":0,\"width\":6,\"height\":6,\"properties\":{\"view\":\"timeSeries\",\"stacked\":false,\"metrics\":[[\"AWS/EC2\",\"NetworkIn\",\"InstanceId\",\"i-0131f062232ade043\"],[\".\",\"NetworkOut\",\".\",\".\"]],\"region\":\"us-east-1\"}}]}",
    "DashboardName": "Dashboard-A"
}
```
For more information, see [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
+  For API details, see [GetDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
