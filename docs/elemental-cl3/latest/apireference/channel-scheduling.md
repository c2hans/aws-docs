---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling.html
---

# Channel Scheduling
<a name="channel-scheduling"></a>

Conductor Live schedules channels to run either at a specific time or on a repeating schedule. Specific times are provided via the REST interface within <run\_at> tags in the format specified in the ISO 8601 standard as combined date and time with UTC offset, such as “2016-07-05T10:09:00-07:00”.

Repeating schedules are provided within `<cron>` tags and represented as CRON elements as specified at [crontab.org](http://crontab.org/). The syntax for the schedules is summarized below.

**Topics**
+ [CRON Syntax Summary](channel-scheduling-cron-syntax-summary.md)
+ [POST: Create a One-Time Schedule](channel-scheduling-create-a-one-time-schedule.md)
+ [POST: Create a Repeating Schedule](channel-scheduling-create-a-repeating-schedule.md)
+ [POST: Activate a Schedule](channel-scheduling-activate-a-schedule.md)
+ [DELETE: Deactivate a Schedule](channel-scheduling-deactivate-a-schedule.md)
+ [PUT: Update a Schedule](channel-scheduling-update-a-schedule.md)
+ [GET List: Get List of All Channel Schedules](channel-scheduling-get-list-of-all-channel-schedules.md)
+ [GET: Get the Attributes of a Schedule](channel-scheduling-get-attributes-of-a-schedule.md)
+ [GET: Get Schedule Events](channel-scheduling-get-schedule-events.md)
+ [DELETE: Delete a Schedule](channel-scheduling-delete-a-schedule.md)
