---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_health_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# AWS Health examples using Tools for PowerShell V5
<a name="powershell_health_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS Health.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-HLTHEvent`
<a name="health_DescribeEvents_powershell_topic"></a>

The following code example shows how to use `Get-HLTHEvent`.

**Tools for PowerShell V5**
**Example 1: This command returns events from AWS Personal Health Dashboard. The user adds the -Region parameter to see events available to the service in the US East (N. Virginia) Region, but the -Filter\_Region parameter filters for events that are logged in the EU (London) and US West (Oregon) Regions (eu-west-2 and us-west-2). The -Filter\_StartTime parameter filters for a range of times that events can start, while the -Filter\_EndTime parameter filters for a range of times that events can end. The result is a scheduled maintenance event for RDS that starts within the specified -Filter\_StartTime range, and ends within the scheduled -Filter\_EndTime range.**

```
Get-HLTHEvent -Region us-east-1 -Filter_Region "eu-west-2","us-west-2" -Filter_StartTime @{from="3/14/2019 6:30:00AM";to="3/15/2019 5:00:00PM"} -Filter_EndTime @{from="3/21/2019 7:00:00AM";to="3/21/2019 5:00:00PM"}
```
**Output:**

```
Arn               : arn:aws:health:us-west-2::event/RDS/AWS_RDS_HARDWARE_MAINTENANCE_SCHEDULED/AWS_RDS_HARDWARE_MAINTENANCE_SCHEDULED_USW2_20190314_20190321
AvailabilityZone  :
EndTime           : 3/21/2019 2:00:00 PM
EventTypeCategory : scheduledChange
EventTypeCode     : AWS_RDS_HARDWARE_MAINTENANCE_SCHEDULED
LastUpdatedTime   : 2/28/2019 2:26:07 PM
Region            : us-west-2
Service           : RDS
StartTime         : 3/14/2019 2:00:00 PM
StatusCode        : open
```
+  For API details, see [DescribeEvents](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
