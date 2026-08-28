---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/scheduler-cli-4.html
---

# Scheduler CLI
<a name="scheduler-cli-4"></a>

The Instance Scheduler on AWS command line interface (CLI) allows you to configure schedules and periods, and estimate cost savings for a given schedule.

## Prerequisites
<a name="prerequisites"></a>

The CLI in this solution requires Python 3.8\+ and the latest version of boto3.

## Credentials
<a name="credentials"></a>

To use the scheduler CLI, you must have credentials for the AWS CLI. For more information, refer to [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html) in the *AWS CLI User Guide*.

Your credentials must have the following permissions:
+  `lambda:InvokeFunction` - To invoke the InstanceSchedulerMain function in the scheduler stack, and to update the schedule and period information in the scheduler configuration database from the command line
+  `cloudformation:DescribeStackResource` - To retrieve the physical resource ID of the AWS Lambda function from the stack to handle the CLI request

Requests made by the scheduler CLI and responses are logged in the `AdminCliRequestHandler-yyyymmdd` log stream.

**Note**
If you specify a profile using the profile-name argument, the profile you specify must have these permissions. For more information about the profile-name argument, refer to [Common Arguments](#common-arguments).

## Install the Scheduler CLI
<a name="install-the-scheduler-cli"></a>

1.  [Download](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance_scheduler_cli.zip) the scheduler CLI package ** *(instance\_scheduler\_cli.zip)* ** and place it in a directory on your computer.
**Important**
The installation will fail if you don’t place the files into their own directory, and then install them from that directory.

1. Unzip the zip archive into its own directory (instance\_scheduler\_cli).

1. From the same directory in which you placed the unzipped CLI package, install the scheduler-cli to your environment:
**Note**
Scheduler-CLI requires Python 3.8 or above and the latest versions of pip and boto3. If you do not have all of these installed on your local machine, please refer to [pip’s official documentation](https://pip.pypa.io/en/stable/getting-started/) for installation instructions before attempting to install the Scheduler-CLI.

   ```
   pip install --no-index --find-links=instance_scheduler_cli instance_scheduler_cli
   ```

1. Verify the installation succeeded with:

   ```
   scheduler-cli --help
   ```

**Note**
If preferred, an [sdist of the CLI](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance_scheduler_cli-3.0.0.tar.gz) and can be installed using the same process as above.

## Command structure
<a name="command-structure"></a>

The scheduler CLI uses a multipart structure on the command line. The next part specifies the scheduler CLI python script. The scheduler CLI has commands that specify the operations to perform on periods and schedules. The specific arguments for an operation can be specified on the command line in any order.

```
scheduler-cli <command> <arguments>
```

## Common arguments
<a name="common-arguments"></a>

The scheduler CLI supports the following arguments that all commands can use:

| Argument | Description |
| --- | --- |
|  `--stack [replaceable]<stackname>`  | The name of the scheduler stack.<br /> **Important:** This argument is required for all commands. |
|  `--region [replaceable]<regionname>`  | The name of the region where the scheduler stack is deployed.<br /> **Note:** You must use this argument when the default configuration and credential files are not installed in the same region as the solution stack. |
|  `--profile-name [replaceable] <profilename>`  | The name of the profile to use to run commands. If no profile name is specified, the default profile is used. |
|  `--query`  | A JMESPath expression that controls the command output. For more information on controlling output, refer to [Controlling Command Output from the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html) in the *AWS CLI User Guide*. |
|  `--help`  | Shows valid commands and arguments for the scheduler CLI. When used with a specific command, it shows valid subcommands and arguments for that command. |
|  `--version`  | Shows the version number of the scheduler CLI. |

## Available commands
<a name="available-commands"></a>
+  [create-period](#create-period)
+  [create-schedule](#create-schedule)
+  [delete-period](#delete-period)
+  [delete-schedule](#delete-schedule)
+  [describe-periods](#describe-periods)
+  [describe-schedules](#describe-schedules)
+  [describe-schedule-usage](#describe-schedule-usage)
+  [update-period](#update-period)
+  [update-schedule](#update-schedule)
+  [help](#help)

## create-period
<a name="create-period"></a>

### Description
<a name="create-period-description"></a>

Creates a period. A period must contain at least one of the following items: `begintime`, `endtime`, `weekdays`, `months`, or `monthdays`.

### Arguments
<a name="create-period-arguments"></a>

 `--name`
+ The name of the period

  Type: String

  Required: Yes

 `--description`
+ A description of the period

  Type: String

  Required: No

 `--begintime`
+ The time when the running period starts. If `begintime` and `endtime` are not specified, the running period is 00:00 - 23:59.

  Type: String

  Constraints: `H:MM` or `HH:MM` format

  Required: No

 `--endtime`
+ The time when the running period stops. If `begintime` and `endtime` are not specified, the running period is 00:00 - 23:59.

  Type: String

  Constraints: `H:MM` or `HH:MM` format

  Required: No

 `--weekdays`
+ The days of the week for the period

  Type: String

  Constraints: Comma-delimited list of abbreviated day names (mon) or numbers (0). Use - to specify a range. Use / to specify every n^th^ day of the week.

  Required: No

 `--months`
+ The months of the period

  Type: String

  Constraints: Comma-delimited list of abbreviated months names (jan) or numbers (1). Use - to specify a range. Use / to specify every n^th^ month.

  Required: No

 `--monthdays`
+ The days of the month for the period

  Type: String

  Constraints: Comma-delimited list of abbreviated months names (jan) or numbers (1). Use - to specify a range. Use / to specify every n^th^ day of the month.

  Required: No

### Example
<a name="create-period-example"></a>

```
$ scheduler-cli create-period --name "weekdays" --begintime 09:00 --endtime 18:00 --weekdays mon-fri --stack Scheduler
{
   "Period": {
      "Name": "weekdays",
      "Endtime": "18:00",
      "Type": "period",
      "Begintime": "09:00",
      "Weekdays": [
         "mon-fri"
      ]
   }
    }
```

## create-schedule
<a name="create-schedule"></a>

### Description
<a name="create-schedule-description"></a>

Creates a schedule.

### Arguments
<a name="create-schedule-arguments"></a>

 `--name`
+ The name of the schedule

  Type: String

  Required: Yes

 `--description`
+ A description of the schedule

  Type: String

  Required: No

 `--enforced`
+ Enforces the scheduled state for the instance

  Required: No

 `--use-metrics`
+ Collect Amazon CloudWatch metrics

  Required: No

 `--periods`
+ A list of running periods for the schedule. If multiple periods are specified, the solution will start an instance if one of the periods evaluates to `true`.

  Type: String

  Constraints: Comma-delimited list of periods. Use `<period-name>@[replaceable]<instance type>` to specify an instance type for a period. For example, `weekdays@t2.large`.

  Required: Yes

 `--retain-running`
+ Prevents an instance from being stopped by the solution at the end of a running period, if the instance was manually started before the beginning of the period.

  Required: No

 `--ssm-maintenance-window`
+ Adds an AWS Systems Manager maintenance window as a running period to an Amazon EC2 instance schedule.

  Type: String

  Required: No

 `--do-not-stop-new-instances`
+ Do not stop an instance the first time it is tagged if it is running outside of a running period

  Required: No

 `--timezone`
+ The time zone the schedule will use

  Type: Array of strings

  Required: No (If this argument is not used, the default time zone from main solution stack is used.)

 `--use-maintenance-window`
+ Adds an Amazon RDS maintenance window as a running period to an Amazon RDS instance schedule, or an AWS Systems Manager maintenance window as a running period to an Amazon EC2 instance schedule

  Type: true/false

  Required: No (default true)

### Example
<a name="create-schedule-example"></a>

```
$ scheduler-cli create-schedule --name LondonOfficeHours --periods weekdays,weekends --timezone Europe/London --stack Scheduler
{
   "Schedule": {
      "Enforced": false,
      "Name": "LondonOfficeHours",
      "StopNewInstances": true,
      "Periods": [
         "weekends",
         "weekdays"
      ],
      "Timezone": "Europe/London",
      "Type": "schedule"
   }
}
```

## delete-period
<a name="delete-period"></a>

 `--name`
+ The name of the applicable period

  Type: String

  Required: Yes

**Important**
If the period is used in existing schedules, you must remove it from those schedules *before* you delete it.

 **Example**

```
$ scheduler-cli delete-period --name weekdays --stack Scheduler
{
   "Period": "weekdays"
}
```

## delete-schedule
<a name="delete-schedule"></a>

### Description
<a name="delete-schedule-description"></a>

Deletes an existing schedule

### Arguments
<a name="delete-schedule-arguments"></a>

 `--name`
+ The name of the applicable schedule

  Type: String

  Required: Yes

### Example
<a name="delete-schedule-example"></a>

```
$ scheduler-cli delete-schedule --name LondonOfficeHours --stack Scheduler
{
   "Schedule": "LondonOfficeHours"
}
```

## describe-periods
<a name="describe-periods"></a>

### Description
<a name="describe-periods-description"></a>

Lists the configured periods for the Instance Scheduler stack

### Arguments
<a name="describe-periods-arguments"></a>

 `--name`
+ The name of a specific period you want described

  Type: String

  Required: No

### Example
<a name="describe-periods-example"></a>

```
$ scheduler-cli describe-periods --stack Scheduler
{
   "Periods": [
      {
         "Name": "first-monday-in-quarter",
         "Months": [
            "jan/3"
         ],
         "Type": "period",
         "Weekdays": [
            "mon#1"
         ],
         "Description": "Every first Monday of each quarter"
      },
      {
         "Description": "Office hours",
         "Weekdays": [
            "mon-fri"
         ],
         "Begintime": "09:00",
         "Endtime": "17:00",
         "Type": "period",
         "Name": "office-hours"
      },

      {
         "Name": "weekdays",
         "Endtime": "18:00",
         "Type": "period",
         "Weekdays": [
            "mon-fri"
         ],
         "Begintime": "09:00"
      },
      {
         "Name": "weekends",
         "Type": "period",
         "Weekdays": [
            "sat-sun"
         ],
         "Description": "Days in weekend"
      }
   ]
}
```

## describe-schedules
<a name="describe-schedules"></a>

### Description
<a name="describe-schedules-description"></a>

Lists the configured schedules for the Instance Scheduler stack.

### Arguments
<a name="describe-schedules-arguments"></a>

 `--name`
+ The name of a specific schedule you want described

  Type: String

  Required: No

### Example
<a name="describe-schedules-example"></a>

```
$ scheduler-cli describe-schedules --stack Scheduler

{
   "Schedules": [
      {
         "OverrideStatus": "running",
         "Type": "schedule",
         "Name": "Running",
         "UseMetrics": false
      },
      {
         "Timezone": "UTC",
         "Type": "schedule",
         "Periods": [
            "working-days@t2.micro",
            "weekends@t2.nano"
         ],
         "Name": "scale-up-down"
      },
      {
         "Timezone": "US/Pacific",
         "Type": "schedule",
         "Periods": [
            "office-hours"
         ],
         "Name": "seattle-office-hours"
      },
      {
         "OverrideStatus": "stopped",
         "Type": "schedule",
         "Name": "stopped",
         "UseMetrics": true
      }
   ]
}
```

## describe-schedule-usage
<a name="describe-schedule-usage"></a>

### Description
<a name="describe-schedule-usage-description"></a>

Lists all the periods running within a schedule and calculates the billing hours for instances. Use this command to simulate a schedule to calculate potential savings, and running periods after creating or updating a schedule.

### Arguments
<a name="describe-schedule-usage-arguments"></a>

 `--name`
+ The name of the applicable schedule

  Type: String

  Required: Yes

 `--startdate`
+ The start date of the period used for calculation. The default date is the current date.

  Type: String

  Required: No

 `--enddate`
+ The end date of the period used for calculation. The default date is the current date.

  Type: String

  Required: No

### Example
<a name="describe-schedule-usage-example"></a>

```
$ scheduler-cli describe-schedule-usage --stack InstanceScheduler --name seattle-office-hours
{
   "Usage": {
      "2017-12-04": {
         "BillingHours": 8,
         "RunningPeriods": {
            "Office-hours": {
               "Begin": "12/04/17 09:00:00",
               "End": "12/04/17 17:00:00",
               "BillingHours": 8,
               "BillingSeconds": 28800
            }
         },
         "BillingSeconds": 28800
      }
   },
   "Schedule": "seattle-office-hours"
```

## update-period
<a name="update-period"></a>

### Description
<a name="update-period-description"></a>

Updates an existing period

### Arguments
<a name="update-period-arguments"></a>

The `update-period` command supports the same arguments as the `create-period` command. For more information on the arguments, refer to the [create period command](#create-period).

**Important**
If you do not specify an argument, that argument will be removed from the period.

## update-schedule
<a name="update-schedule"></a>

### Description
<a name="update-schedule-description"></a>

Updates an existing schedule

### Arguments
<a name="update-schedule-arguments"></a>

The `update-schedule` command supports the same arguments as the `create-schedule` command. For more information on the arguments, refer to the [create schedule command](#create-schedule).

**Important**
If you do not specify an argument, that argument will be removed from the schedule.

## help
<a name="help"></a>

### Description
<a name="help-description"></a>

Displays a list of valid commands and arguments for the scheduler CLI.

### Example
<a name="help-example"></a>

```
$ scheduler-cli --help
usage: scheduler-cli [-h] [--version]
                     {create-period,create-schedule,delete-period,delete-schedule,describe-periods,describe-schedule-usage,describe-schedules,update-period,update-schedule}
                     ...

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

subcommands:
  Valid subcommands

  {create-period,create-schedule,delete-period,delete-schedule,describe-periods,describe-schedule-usage,describe-schedules,update-period,update-schedule}
                        Commands help
    create-period       Creates a period
    create-schedule     Creates a schedule
    delete-period       Deletes a period
    delete-schedule     Deletes a schedule
    describe-periods    Describes configured periods
    describe-schedule-usage
                        Calculates periods and billing hours in which
                        instances are running
    describe-schedules  Described configured schedules
    update-period       Updates a period
    update-schedule     Updates a schedule
```

When used with a specific command, the `--help` argument shows valid subcommands and arguments for that command.

### Specific command example
<a name="help-example-specific-command"></a>

```
$ scheduler-cli describe-schedules --help
usage: scheduler-cli describe-schedules [-h] [--name NAME] [--query QUERY]
                                        [--region REGION] --stack STACK

optional arguments:
  -h, --help         show this help message and exit
  --name NAME        Name of the schedule
  --query QUERY      JMESPath query to transform or filter the result
  --region REGION    Region in which the Instance Scheduler stack is
                        deployed
  --stack STACK, -s STACK
                     Name of the Instance Scheduler stack
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
