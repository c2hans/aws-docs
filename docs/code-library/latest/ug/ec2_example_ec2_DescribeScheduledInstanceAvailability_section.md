---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DescribeScheduledInstanceAvailability_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeScheduledInstanceAvailability` with a CLI
<a name="ec2_example_ec2_DescribeScheduledInstanceAvailability_section"></a>

The following code examples show how to use `DescribeScheduledInstanceAvailability`.

------
#### [ CLI ]

**AWS CLI**
**To describe an available schedule**
This example describes a schedule that occurs every week on Sunday, starting on the specified date.
Command:

```
aws ec2 describe-scheduled-instance-availability --recurrence {{Frequency=Weekly,Interval=1,OccurrenceDays=[1]}} --first-slot-start-time-range {{EarliestTime=2016-01-31T00:00:00Z,LatestTime=2016-01-31T04:00:00Z}}
```
Output:

```
{
  "ScheduledInstanceAvailabilitySet": [
    {
        "AvailabilityZone": "us-west-2b",
        "TotalScheduledInstanceHours": 1219,
        "PurchaseToken": "eyJ2IjoiMSIsInMiOjEsImMiOi...",
        "MinTermDurationInDays": 366,
        "AvailableInstanceCount": 20,
        "Recurrence": {
            "OccurrenceDaySet": [
                1
            ],
            "Interval": 1,
            "Frequency": "Weekly",
            "OccurrenceRelativeToEnd": false
        },
        "Platform": "Linux/UNIX",
        "FirstSlotStartTime": "2016-01-31T00:00:00Z",
        "MaxTermDurationInDays": 366,
        "SlotDurationInHours": 23,
        "NetworkPlatform": "EC2-VPC",
        "InstanceType": "c4.large",
        "HourlyPrice": "0.095"
    },
    ...
  ]
}
```
To narrow the results, you can add filters that specify the operating system, network, and instance type.
Command:
--filters Name=platform,Values=Linux/UNIX Name=network-platform,Values=EC2-VPC Name=instance-type,Values=c4.large
+  For API details, see [DescribeScheduledInstanceAvailability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instance-availability.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes a schedule that occurs every week on Sunday, starting on the specified date.**

```
Get-EC2ScheduledInstanceAvailability -Recurrence_Frequency Weekly -Recurrence_Interval 1 -Recurrence_OccurrenceDay 1 -FirstSlotStartTimeRange_EarliestTime 2016-01-31T00:00:00Z -FirstSlotStartTimeRange_LatestTime 2016-01-31T04:00:00Z
```
**Output:**

```
AvailabilityZone            : us-west-2b
AvailableInstanceCount      : 20
FirstSlotStartTime          : 1/31/2016 8:00:00 AM
HourlyPrice                 : 0.095
InstanceType                : c4.large
MaxTermDurationInDays       : 366
MinTermDurationInDays       : 366
NetworkPlatform             : EC2-VPC
Platform                    : Linux/UNIX
PurchaseToken               : eyJ2IjoiMSIsInMiOjEsImMiOi...
Recurrence                  : Amazon.EC2.Model.ScheduledInstanceRecurrence
SlotDurationInHours         : 23
TotalScheduledInstanceHours : 1219

...
```
**Example 2: To narrow the results, you can add filters for criteria such as operating system, network, and instance type.**

```
-Filter @{ Name="platform";Values="Linux/UNIX" },@{ Name="network-platform";Values="EC2-VPC" },@{ Name="instance-type";Values="c4.large" }
```
+  For API details, see [DescribeScheduledInstanceAvailability](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes a schedule that occurs every week on Sunday, starting on the specified date.**

```
Get-EC2ScheduledInstanceAvailability -Recurrence_Frequency Weekly -Recurrence_Interval 1 -Recurrence_OccurrenceDay 1 -FirstSlotStartTimeRange_EarliestTime 2016-01-31T00:00:00Z -FirstSlotStartTimeRange_LatestTime 2016-01-31T04:00:00Z
```
**Output:**

```
AvailabilityZone            : us-west-2b
AvailableInstanceCount      : 20
FirstSlotStartTime          : 1/31/2016 8:00:00 AM
HourlyPrice                 : 0.095
InstanceType                : c4.large
MaxTermDurationInDays       : 366
MinTermDurationInDays       : 366
NetworkPlatform             : EC2-VPC
Platform                    : Linux/UNIX
PurchaseToken               : eyJ2IjoiMSIsInMiOjEsImMiOi...
Recurrence                  : Amazon.EC2.Model.ScheduledInstanceRecurrence
SlotDurationInHours         : 23
TotalScheduledInstanceHours : 1219

...
```
**Example 2: To narrow the results, you can add filters for criteria such as operating system, network, and instance type.**

```
-Filter @{ Name="platform";Values="Linux/UNIX" },@{ Name="network-platform";Values="EC2-VPC" },@{ Name="instance-type";Values="c4.large" }
```
+  For API details, see [DescribeScheduledInstanceAvailability](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
