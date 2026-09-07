---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-cron-syntax-summary.html
---

# CRON Syntax Summary
<a name="channel-scheduling-cron-syntax-summary"></a>

The CRON expression is composed of five parts, separated by spaces, representing minute, hour, day of month, month, and day of week respectively, as illustrated below.

![The CRON expression is composed of five parts, separated by spaces, representing minute, hour, day of month, month, and day of week respectively.](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/images/channel-scheduling-cron-syntax.png)

The channel runs when the fields in the expression match the current time and date. An asterisk (\*) acts as a wildcard and represents all values. If both “day of month” and “day of week” are specified (not \*s), then the schedule will run for both.

Each part can specify either one value or a repeating value. A number by itself represents a single value while a number preceded by an asterisk and a forward slash represents a repeating value. For example, in the second position, “5” means “on the fifth hour (5:00 AM)” and “\*/5” means “every fifth hour (5:00 AM, 10:00 AM, 3:00 PM, etc).” The table below provides some examples.

|  Position 1  (min)  |  Position 2 (hour)  |  Position 3 (day of month)  |  Position 4 (month)  |  Position 5 (day of week)  |  Resulting Schedule  |
| --- | --- | --- | --- | --- | --- |
| 0 | 3 | \* | \* | 1 | Every Monday at 8:00 PM Pacific Daylight Time (UTC-07:00)<br />**Note:** The hour in position 2 must be provided in UTC, not your local time. |
| 0 | 3 | \* | \* | 1,2,3,4,5 | Every weekday at 8:00 PM Pacific Daylight Time (UTC-07:00)<br />**Note:** The hour in position 2 must be provided in UTC, not your local time. |
| 15 | 1 | \* | \* | 1,2,3,4,5 | Every weekday at 8:15 PM Eastern Standard Time (UTC-05:00)<br />**Note:** The hour in position 2 must be provided in UTC, not your local time. |
| 17 | \*/4 | \* | \* | \* | Every four hours on the 17th minute every day. 4:17 AM, 8:17 AM, etc. |
| 0 | \*/1 | \* | \* | 1 | Every Monday, each hour at the top of the hour. |
