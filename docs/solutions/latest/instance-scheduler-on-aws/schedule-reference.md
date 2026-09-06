---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/schedule-reference.html
---

# Schedule reference
<a name="schedule-reference"></a>

Schedules specify when instances tagged with that schedule should run. Each schedule must have a unique name, which is used as the tag *value* that identifies the schedule you want to apply to the tagged resource.

## Periods
<a name="periods"></a>

Each schedule must contain at least one period that defines the time(s) the instance should run. A schedule can contain more than one period. When more than one period is used in a schedule, Instance Scheduler on AWS will apply the appropriate start action when at least one of the periods is true. For more information, refer to [Period reference](period-reference.md).

## Time zone
<a name="time-zone"></a>

You can also specify a time zone for the schedule. If you do not specify a time zone, the schedule will use the default time zone you specify when you launch the solution. For a list of acceptable time zone values, refer to the **TZ** column of the [List of TZ database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## Stop new instances field
<a name="stop-new-instances-field"></a>

The stop\_new\_instances field controls whether Instance Scheduler should stop an instance the first time it is tagged for scheduling if it is currently running outside of a running period. By default, this field is set to true.

When set to true, if you tag a running instance that is outside its scheduled running period, Instance Scheduler will immediately stop the instance. When set to false, Instance Scheduler will leave the instance running until the next scheduled stop time.

## Hibernate field
<a name="hibernate-field"></a>

The hibernate field allows you to use hibernation for stopped Amazon EC2 instances. If this field is set to true, your EC2 instances must use an Amazon Machine Image (AMI) that supports hibernation. For more information, refer to [Supported Linux AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html#hibernation-prereqs-supported-amis) in the *Amazon EC2 User Guide*. Hibernation saves the contents from the instance memory (RAM) to your Amazon Elastic Block Store (Amazon EBS) root volume. If this field is set to true, instances are hibernated instead of stopped when the solution stops them.

If you set the solution to use hibernation, but your instances are not [configured for hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling-hibernation.html) or they do not meet the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html), the solution logs a warning and the instances are stopped without hibernation. For more information, refer to [Hibernate your On-Demand Instance or Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.

## Enforced field
<a name="enforced-field"></a>

Schedules contain an enforced field that allows you to prevent an instance from being manually started outside of a running period, or manually stopped during a running period. If this field is set to true and a user manually starts an instance outside of a running period, the solution will stop the instance. If this field is set to true, it also restarts an instance if it is manually stopped during a running period.

## Retain running field
<a name="retain-running-field"></a>

The retain\_running field prevents the solution from stopping an instance at the end of a running period if the instance was manually started before the beginning of the period. For example, if an instance with a period that runs from 9 AM to 5 PM is manually started before 9 AM, the solution will not stop the instance at 5 PM.

## Systems Manager maintenance window field (only applies to EC2 instances)
<a name="systems-manager-maintenance-window-field-only-applies-to-ec2-instances"></a>

The ssm-maintenance-window field allows you to automatically add AWS Systems Manager maintenance windows as a running periods to a schedule. When you specify the name of a maintenance window that exists in the same account and AWS Region as your Amazon EC2 instances, the solution will start the instance at least 10 minutes before the start of the maintenance window and stop the instance at the end of the maintenance window if no other running period specifies that the instance should run.

Once the SSM Maintenance window is created and the schedule is configured with the name of the SSM maintenance window, the changes are picked up at the next scheduled run of the Lambda. For example, if you selected a frequency of 5 minutes for the scheduler Lambda to run, the maintenance window changes will be picked up by the Lambda on the next 5-minute interval.

Instance Scheduler on AWS will ensure that your instances are started at least 10 minutes before the maintenance window begins. Depending on the value you set for the **Scheduling Interval** AWS CloudFormation parameter, this may result in your instance being started 10\+interval minutes before the beginning of the maintenance window in order to guarantee that the instance starts at least 10 minutes early. For example, if you set the Scheduling Interval to 30 minutes, the scheduler will start the instance between 10-40 minutes before the beginning of the maintenance window.

**Note**
In order to use this feature, the Enable EC2 SSM Maintenance Windows CloudFormation parameter in the solution hub stack must be set to `yes`.

For more information, refer to [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) in the *AWS Systems Manager user guide*.

## Instance type
<a name="instance-type"></a>

For Amazon EC2 instances only, a schedule allows you to specify an optional desired instance type for each period in a schedule. When you specify an instance type in the period, the solution will automatically resize EC2 instances to match the requested instance type.

To specify an instance type, use the syntax *<period-name>@<instance-type>*. For example, `weekends@t2.nano`. Note that if you specify an instance type for a period that schedules Amazon EC2 instances and Amazon RDS instances, the instance type will be ignored for Amazon RDS instances.

If the instance type of a running instance is different than the instance type specified for the period, the solution will stop the running instance and restart the instance with the specified instance type. For more information, refer to [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-limitations) in the *Amazon EC2 User Guide for Linux Instances*.

## Schedule definitions
<a name="schedule-definitions"></a>

The Instance Scheduler on AWS configuration table in Amazon DynamoDB contains schedule definitions. A schedule definition can contain the following fields:

| Field | Description |
| --- | --- |
|  `description`  | An optional description of the schedule. |
|  `hibernate`  | Choose whether to hibernate Amazon EC2 instances running Amazon Linux. When this field is set to true, the scheduler will hibernate instances when it stops them. Note that your instances must [turn on hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html#enabling-hibernation) and must meet the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html#hibernating-prerequisites). |
|  `enforced`  | Choose whether to enforce the schedule. When this field is set to true, the scheduler will stop a running instance if it is manually started outside of the running period or it will start an instance if it is stopped manually during the running period. |
|  `name`  | The name used to identify the schedule. This name must be unique and include only alpha-numerics, hyphens (-), and underscores (\_). |
|  `periods`  | The name of the periods that are used in this schedule. Enter the name(s) exactly as it appears in the period name field.<br />You can also specify an instance type for the period using the syntax *<period-name>@<instance-type>*. For example, `weekdays@t2.large`. |
|  `retain_running`  | Choose whether to prevent the solution from stopping an instance at the end of a running period if the instance was manually started before the beginning of the period. |
|  `use_maintenance_window`  | Choose whether to include Amazon RDS maintenance window as a running period to an Amazon RDS instance schedule, or an AWS Systems Manager maintenance window as a running period to an Amazon EC2 instance schedule. This field is enabled by default and can be disabled by setting its value to "false" |
|  `ssm_maintenance_window`  | Choose whether to add AWS Systems Manager maintenance window(s) as additional running period for this schedule. Accepts a StringSet of maintenance window names that will be matched against the names of windows in the same account/region as scheduled EC2 instances.<br /> **Note:** This feature only applies to EC2 instances. |
|  `stop_new_instances`  | Choose whether to stop an instance the first time it is tagged if it is running outside of the running period. By default, this field is set to true. |
|  `timezone`  | The time zone the schedule will use. If no time zone is specified, the default time zone (UTC) is used. For a list of acceptable time zone values, refer to the **TZ** column of the [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
|  `use_metrics`  | Choose whether to turn on CloudWatch metrics at the schedule level. This field overwrites the CloudWatch metrics setting you specified at deployment.<br /> **Note:** Enabling this feature will incur charges of $0.90/month per schedule or scheduled service. |
