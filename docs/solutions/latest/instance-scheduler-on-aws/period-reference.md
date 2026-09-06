---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/period-reference.html
---

# Period reference
<a name="period-reference"></a>

Periods contain conditions that allow you to set the specific hours, days, and months an instance will run. A period can contain multiple conditions, but all conditions must be true for the Instance Scheduler on AWS to apply the appropriate start or stop action.

## Start and stop times
<a name="start-and-stop-times"></a>

The `begintime` and `endtime` fields define when the Instance Scheduler on AWS will start and stop instances. If you specify a start time only, the instance must be stopped manually. Note that if you specify a value in the [weekdays](#days-of-the-week) field, the solution uses that value to determine when to stop the instance. For example, if you specify a `begintime` of 9 AM with no `endtime` and a weekdays value of Monday through Friday, the instance will be stopped at 11:59 PM on Friday unless you have scheduled an adjacent period.

Similarly, if you only specify a stop time, the instance must be started manually. If you don’t specify either time, this solution uses the days of the week, days of the month, or months rules to start and stop instances at the beginning/end of each day as appropriate.

The `begintime` and `endtime` values for your period must be in the time zone specified in the schedule. If you do not specify a time zone in the schedule, the solution will use the time zone specified when you launch the solution.

If your schedule contains multiple periods, we recommend that you always specify both a `begintime` and `endtime` in your periods.

If you start an instance before the specified start time, the instance will run until the end of the running period. For example, a user might define a period that starts an instance daily at 9 AM and stops that instance at 5 PM.

 **9-5 scheduled start and stop**

![image6](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/image6.png)

If you manually start that instance at 5 AM, the solution will stop the instance at 5 PM. If you use the [retain running field](schedule-reference.md#retain-running-field), the solution will not stop the instance at 5 PM.

 **5 AM scheduled stop**

![image7](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/image7.png)

If you stop an instance before the specified stop time, the instance will not run until the beginning of the next running period. Continuing from the previous example, if the user stops the instance at 1 PM on Wednesday, the solution will not start the instance until 9 AM on Thursday.

 **Timeline showing scheduled start at 9 am, manual stop at 1 pm, and scheduled stop at 5 pm.**

![image8](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/image8.png)

### Adjacent periods
<a name="adjacent-periods"></a>

The solution will not stop running instances if the schedule contains two adjacent running periods. For example, if you have a schedule with one period with an `endtime` of 11:59 PM and another period with a `begintime` of midnight the following day, the solution will not stop running instances, if there are no `weekdays`, `monthdays`, or `months` rules that stop the instances.

To implement a schedule that runs instances from 9 AM Monday to 5 PM Friday, the solution requires three periods. The first period runs applicable instances from 9 AM to 11:59 PM Monday. The second period runs the instances from midnight Tuesday to 11:59 PM Thursday. The third period runs the instances from midnight Friday to 5 PM Friday. For more information, refer to [Sample schedules](sample-schedules.md).

## Days of the week
<a name="days-of-the-week"></a>

The `weekdays` field defines which days during the week an instance will run. You can specify a list of days, a range of days, the n^th^ occurrence of that day in a month, or the last occurrence of that day in a month. The solution supports abbreviated day names (Mon) and numbers (0).

## Days of the month
<a name="days-of-the-month"></a>

The `monthdays`, field defines which days during the month an instance will run. You can specify a list of days, a range of days, every n^th^ day of the month, the last day of the month, or the nearest weekday to a specific date.

## Months
<a name="months"></a>

The `months` field defines which months an instance will run. You can specify a list of months, a range of months, or every n^th^ month. The solution supports abbreviated month names (Jan) and numbers (1).

## Period definitions
<a name="period-definitions"></a>

The Instance Scheduler on AWS configuration table in Amazon DynamoDB contains period definitions. A period definition can contain the following fields. Note that some fields support [Cron non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-Standard_Characters).

**Important**
You must specify at least one of the following items: begintime, endtime, weekdays, months, or monthdays.

| Field | Description |
| --- | --- |
|  `begintime`  | The time, in **HH:MM** format, that the instance will start. |
|  `description`  | An optional description of the period. |
|  `endtime`  | The time, in **HH:MM** format, that the instance will stop. |
|  `months`  | Enter a comma-delimited list of months, or a hyphenated range of months, during which the instance will run. For example, enter `jan, feb, mar` or `1, 2, 3` to run an instance during those months. Or, you can enter `jan-mar` or `1-3`.<br />You can also schedule an instance to run every n^th^ month or every n^th^ month in a range. For example, enter `Jan/3` or `1/3` to run an instance every third month starting in January. Enter `Jan-Jul/2` to run every other month from January to July. |
|  `monthdays`  | Enter a comma-delimited list of days of the month, or a hyphenated range of days, during which the instance will run. For example, enter `1, 2, 3` or `1-3` to run an instance during the first three days of the month. You can also enter multiple ranges. For example, enter `1-3`, `7-9` to run an instance from the 1^st^ to the 3^rd^ and the 7^th^ through the 9^th^.<br />You can also schedule an instance to run every n^th^ day of the month or every n^th^ day of the month in a range. For example, enter `1/7` to run an instance every seventh day starting on the 1^st^. Enter `1-15/2` to run an instance every other day from the 1^st^ to the 15^th^.<br />Enter `L` to run an instance on the last day of the month. Enter a date and W to run an instance on the nearest weekday to the specified date. For example, enter `15W` to run an instance on the nearest weekday to the 15^th^. |
|  `name`  | The name used to identify the period. This name must be unique and include only alpha-numerics, hyphens (-), and underscores (\_). |
|  `weekdays`  | Enter a comma-delimited list of days of the week, or a range of days of the week, during which the instance will run. For example, enter `0, 1, 2` or `0-2` to run an instance Monday through Wednesday. You can also enter multiple ranges. For example, enter `0-2`, `4-6` to run an instance every day except Thursday.<br />You can also schedule an instance to run every n^th^ occurrence of a weekday in the month. For example, enter `Mon#1` or `0#1` to run an instance the first Monday of the month.<br />Enter a day and L to run an instance on the last occurrence of that weekday in the month. For example, enter `friL` or `4L` to run an instance on the last Friday of the month. |

When a period contains multiple conditions, note that all conditions must be true for Instance Scheduler on AWS to apply the appropriate action. For example, a period that contains a `weekdays` field with a value of `Mon#1` and a months field with a value of `Jan/3` will apply the action on the first Monday of the quarter.
