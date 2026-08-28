---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-delete-a-schedule.html
---

# DELETE: Delete a Schedule
<a name="channel-scheduling-delete-a-schedule"></a>

Permanently delete a schedule.

## HTTP Request and Response
<a name="channel-scheduling-delete-a-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-delete-a-schedule-http-request-response-url"></a>

```
DELETE http://<Conductor IP Address>/channels/<channel ID>/schedules/<schedule ID>
```

### Call Header
<a name="channel-scheduling-delete-a-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-delete-a-schedule-http-request-response-response"></a>

The system deletes the schedule but does not return a response. To confirm that the schedule has been changed, run a GET on the schedule as described in [GET: Get the Attributes of a Schedule](channel-scheduling-get-attributes-of-a-schedule.md). The GET should return an error similar to this one:

```
<errors>
    <error>Couldn't find Elemental::Live247::Schedule with id=13 [WHERE "live247_schedules"."schedulable_id" = 1 AND "live247_schedules"."schedulable_type" = 'Elemental::Live247::Channel']</error>
</errors>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
