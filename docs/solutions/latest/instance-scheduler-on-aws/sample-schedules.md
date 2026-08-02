---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/sample-schedules.html
---

# Sample schedules
<a name="sample-schedules"></a>

Instance Scheduler on AWS allows you to automatically start and stop Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances. The following section provides some example schedules that can be adapted to many common use cases.

## Standard 9-5 working hours
<a name="standard-9-5-working-hours"></a>

This schedule shows how to run instances on weekdays from 9 AM to 5 PM in London.

### Periods
<a name="periods-1"></a>

This period will start instances at 9 AM and stop instances at 5 PM on weekdays (Mon-Fri).

| Field | Type | Value |
| --- | --- | --- |
|  `begintime`  |  `String`  |  `09:00`  |
|  `endtime`  |  `String`  |  `16:59`  |
|  `name`  |  `String`  |  `weekdays-9-5`  |
|  `weekdays`  |  `StringSet`  |  `mon-fri`  |

### Schedule
<a name="schedule"></a>

The schedule name provides the tag value that must be applied to instances and the timezone that will be used.

| Field | Type | Value |
| --- | --- | --- |
|  `name`  |  `String`  |  `london-working-hours`  |
|  `periods`  |  `StringSet`  |  `weekdays-9-5`  |
|  `timezone`  |  `String`  |  `Europe/London`  |

### Instance tag
<a name="instance-tag"></a>

To apply this schedule to instances, you must add the `Schedule=london-working-hours` tag to the instances. If you change the default tag name in the AWS CloudFormation **Instance Scheduler tag name** parameter, your tag will be different. For example, if you entered `Sked` as your tag name, your tag will be `Sked=london-working-hours`. For more information, refer to [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-ec2-resources-table) in the *Amazon Elastic Compute Cloud User Guide*.

### Scheduler CLI
<a name="scheduler-cli-1"></a>

To configure the above schedule using the [Instance Scheduler CLI](scheduler-cli-4.md) use the following commands:

```
scheduler-cli create-period --stack <stackname> --name weekdays-9-5 --weekdays mon-fri --begintime 9:00 --endtime 16:59

scheduler-cli create-schedule --stack <stackname> --name london-working-hours --periods weekdays-9-5 --timezone Europe/London

Europe/London
```

### Custom resource
<a name="custom-resource"></a>

The following CloudFormation template will create the above schedule using the [schedule custom resource](manage-schedules-using-infrastructure-as-code-iac.md).

To deploy this template, you will need to provide the **ServiceInstanceScheduleServiceToken** ARN that can be found in the AWS CloudFormation console by selecting the [previously deployed Instance Scheduler Hub Stack](step-1-launch-the-instance-scheduler-hub-stack.md) and then select **Outputs**.

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ServiceInstanceScheduleServiceTokenARN:
    Type: String
    Description: (Required) service token arn taken from InstanceScheduler outputs
Metadata:
  'AWS::CloudFormation::Designer': {}
Resources:
  LondonWorkingWeek:
    Type: 'Custom::ServiceInstanceSchedule'
    Properties:
      NoStackPrefix: 'True'
      Name: london-working-hours
      Description: run instances from 9am to 5pm in London on weekdays
      ServiceToken: !Ref ServiceInstanceScheduleServiceTokenARN
      Timezone: Europe/London
      Periods:
     - Description: 9am to 5pm on weekdays
        BeginTime: '09:00'
        EndTime: '16:59'
        WeekDays: mon-fri
```

## Stop instances after 5 PM
<a name="stop-instances-after-5-pm"></a>

Instances can be started freely at any time during the day and this schedule will ensure that a stop command is automatically sent to them at 5 PM ET every day.

### Periods
<a name="periods-2"></a>

This period will stop instances at 5 PM every day.

| Field | Type | Value |
| --- | --- | --- |
|  `endtime`  |  `String`  |  `16:59`  |
|  `name`  |  `String`  |  `stop-at-5`  |

### Schedule
<a name="schedule-1"></a>

The schedule name provides the tag value that must be applied to instances and the timezone that will be used.

| Field |  | Value |
| --- | --- | --- |
|  `name`  |  `String`  |  `stop-at-5-new-york`  |
|  `periods`  |  `StringSet`  |  `stop-at-5`  |
|  `timezone`  |  `String`  |  `America/New York`  |

### Instance tag
<a name="instance-tag-1"></a>

To apply this schedule to instances, you must add the `Schedule=stop-at-5-new-york` tag to the instances. If you changed the default tag name in the AWS CloudFormation **Instance Scheduler tag name** parameter, your tag will be different. For example, if you entered `Sked` as your tag name, your tag will be `Sked=stop-at-5-new-york` . For more information, refer to [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-ec2-resources-table) in the *Amazon Elastic Compute Cloud User Guide*.

### Scheduler CLI
<a name="scheduler-cli-2"></a>

To configure the above schedule using the [Instance Scheduler CLI](scheduler-cli-4.md), use the following commands:

```
scheduler-cli create-period --stack <stackname> --name stop-at-5 --endtime 16:59

scheduler-cli create-schedule --stack <stackname> --name stop-at-5-new-york --periods stop-at-5 --timezone America/New_York
```

### Custom resource
<a name="custom-resource-1"></a>

The following CloudFormation template will create the above schedule using the [schedule custom resource](manage-schedules-using-infrastructure-as-code-iac.md).

To deploy this template, you will need to provide the **ServiceInstanceScheduleServiceToken** ARN that can be found in the AWS CloudFormation console by clicking on the [previously deployed Instance Scheduler Hub Stack](step-1-launch-the-instance-scheduler-hub-stack.md) and selecting **Outputs**.

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ServiceInstanceScheduleServiceTokenARN:
    Type: String
    Description: (Required) service token arn taken from InstanceScheduler outputs
Metadata:
  'AWS::CloudFormation::Designer': {}
Resources:
  StopAfter5:
    Type: 'Custom::ServiceInstanceSchedule'
    Properties:
      NoStackPrefix: 'True'
      Name: stop-at-5-new-york
      Description: stop instances at 5pm ET every day
      ServiceToken: !Ref ServiceInstanceScheduleServiceTokenARN
      Timezone: America/New_York
      Periods:
      - Description: stop at 5pm
        EndTime: '16:59'
```

## Stop instances over the weekend
<a name="stop-instances-over-the-weekend"></a>

This schedule shows how to run instances from Monday 9 AM ET to Friday 5 PM ET. Since Monday and Friday are not full days, this schedule includes three periods to accommodate: Monday, Tuesday-Thursday, and Friday.

### Periods
<a name="periods-3"></a>

The first period starts tagged instances at 9 AM Monday and stops at midnight. This period includes the following fields and values.

| Field | Type | Value |
| --- | --- | --- |
|  `begintime`  |  `String`  |  `09:00`  |
|  `endtime`  |  `String`  |  `23:59`  |
|  `name`  |  `String`  |  `mon-start-9am`  |
|  `weekdays`  |  `StringSet`  |  `mon`  |

The second period runs tagged instances all day Tuesday through Thursday. This period includes the following fields and values.

| Field |  | Value |
| --- | --- | --- |
|  `name`  |  `String`  |  `tue-thu-full-day`  |
|  `weekdays`  |  `StringSet`  |  `tue-thu`  |

The third period stops tagged instances at 5 PM on Friday. This period includes the following fields and values.

| Field |  | Value |
| --- | --- | --- |
|  `begintime`  |  `String`  |  `00:00`  |
|  `endtime`  |  `String`  |  `16:59`  |
|  `name`  |  `String`  |  `fri-stop-5pm`  |
|  `weekdays`  |  `StringSet`  |  `fri`  |

### Schedule
<a name="schedule-2"></a>

The schedule combines the three periods into the schedule for tagged instances. The schedule includes the following fields and values.

| Field |  | Value |
| --- | --- | --- |
|  `name`  |  `String`  | mon-9am-fri-5pm |
|  `periods`  |  `StringSet`  | mon-start-9am,tue-thu-full-day,fri-stop-5pm |
|  `timezone`  |  `String`  | America/New\_York |

### Instance tag
<a name="instance-tag-2"></a>

To apply this schedule to instances, you must add the `Schedule=mon-9am-fri-5pm` tag to the instances. Note that if you changed the default tag name in the AWS CloudFormation **Instance Scheduler tag name** parameter, your tag will be different. For example, if you entered Sked as your tag name, your tag will be `Sked=mon-9am-fri-5pm`. For more information, refer to [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-ec2-resources-table) in the *Amazon Elastic Compute Cloud User Guide*.

### Scheduler CLI
<a name="scheduler-cli-3"></a>

To configure the above schedule using the [Instance Scheduler CLI](scheduler-cli-4.md), use the following commands:

```
scheduler-cli create-period --stack <stackname> --name
mon-start-9am --weekdays mon --begintime 9:00 --endtime 23:59
scheduler-cli create-period --stack <stackname> --name
tue-thu-full-day --weekdays tue-thu
scheduler-cli create-period --stack <stackname> --namefri-stop-5pm --weekdays fri --begintime 0:00 --endtime 17:00

scheduler-cli create-schedule --stack <stackname> --name
mon-9am-fri-5pm --periods
mon-start-9am,tue-thu-full-day,fri-stop-5pm -timezone
America/New_York
```

### Custom resource
<a name="custom-resource-2"></a>

The following CloudFormation template will create the above schedule using the [schedule custom resource](manage-schedules-using-infrastructure-as-code-iac.md).

To deploy this template, you will need to provide the **ServiceInstanceScheduleServiceToken** ARN that can be found in the AWS CloudFormation console by selecting the [previously deployed Instance Scheduler Hub Stack](step-1-launch-the-instance-scheduler-hub-stack.md) and then select **Outputs**.

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ServiceInstanceScheduleServiceTokenARN:
    Type: String
    Description: (Required) service token arn taken from InstanceScheduler outputs
Metadata:
  'AWS::CloudFormation::Designer': {}
Resources:
  StopOnWeekends:
    Type: 'Custom::ServiceInstanceSchedule'
    Properties:
      NoStackPrefix: 'True'
      Name: mon-9am-fri-5pm
      Description: start instances at 9am on monday and stop them at 5pm on friday
      ServiceToken: !Ref ServiceInstanceScheduleServiceTokenARN
      Timezone: America/New_York
      Periods:
      - Description: 9am monday start
        BeginTime: '09:00'
        EndTime: '23:59'
        WeekDays: mon
      - Description: all day tuesday-thursday
        WeekDays: tue-thu
      - Description: 5pm friday stop
        BeginTime: '00:00'
        EndTime: '16:59'
        WeekDays: fri
```

## Solution resources
<a name="solution-resources"></a>

The following resources are created as part of the Instance Scheduler on AWS stack.

| Resource name | Type | Description |
| --- | --- | --- |
|  **Main**  |  `AWS::Lambda::Function`  | Instance Scheduler on AWS Lambda function. |
|  **Scheduler Config Helper**  |  `Custom::ServiceSetup`  | Stores global configuration settings in Amazon DynamoDB. |
|  **Scheduler Invoke Permission**  |  `AWS::Lambda::Permission`  | Allows the Amazon CloudWatch event to invoke the Instance Scheduler’s AWS Lambda function. |
|  **Scheduler Logs**  |  `AWS::Logs::LogGroup`  | CloudWatch Log Group for Instance Scheduler. |
|  **Scheduler Policy**  |  `AWS::IAM::Policy`  | Policy that allows scheduler to perform start and stop actions, change Amazon EC2 instance attributes, set tags, and access scheduler resources. |
|  **Scheduler Rule**  |  `AWS::Events::Rule`  | Amazon EventBridge event rule that invokes the scheduler’s Lambda function. |
|  **Configuration Metrics Event Rule**  |  `AWS::Events::Rule`  | Amazon EventBridge event rule that periodically invokes the configuration description anonymized metrics function. Disabled when anonymized metrics are disabled. |
|  **State Table**  |  `AWS::DynamamoDB::Table`  | DynamoDB table that stores last desired state of instances. |
|  **Config Table**  |  `AWS::DynamamoDB::Table`  | DynamoDB table that stores global configuration, schedule, and period data. |
|  **Instance Scheduler SNS Topic**  |  `AWS::SNS::Topic`  | Sends warning and error messages to subscribed email addresses. |
