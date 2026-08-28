---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_GetTrailStatus_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetTrailStatus` with a CLI
<a name="cloudtrail_example_cloudtrail_GetTrailStatus_section"></a>

The following code examples show how to use `GetTrailStatus`.

------
#### [ CLI ]

**AWS CLI**
**To get the status of a trail**
The following `get-trail-status` command returns the delivery and logging details for `Trail1`:

```
aws cloudtrail get-trail-status --name {{Trail1}}
```
Output:

```
{
  "LatestNotificationTime": 1454022144.869,
  "LatestNotificationAttemptSucceeded": "2016-01-28T23:02:24Z",
  "LatestDeliveryAttemptTime": "2016-01-28T23:02:24Z",
  "LatestDeliveryTime": 1454022144.869,
  "TimeLoggingStarted": "2015-11-06T18:36:38Z",
  "LatestDeliveryAttemptSucceeded": "2016-01-28T23:02:24Z",
  "IsLogging": true,
  "LatestCloudWatchLogsDeliveryTime": 1454022144.918,
  "StartLoggingTime": 1446834998.695,
  "StopLoggingTime": 1446834996.933,
  "LatestNotificationAttemptTime": "2016-01-28T23:02:24Z",
  "TimeLoggingStopped": "2015-11-06T18:36:36Z"
}
```
+  For API details, see [GetTrailStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail-status.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
**Example 1: Returns status information for the trail with name 'myExampleTrail'. Returned data includes information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for the trail. This example assumes the trail was created in the same region as the current shell default.**

```
Get-CTTrailStatus -Name myExampleTrail
```
**Example 2: Returns status information for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Get-CTTrailStatus -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [GetTrailStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
