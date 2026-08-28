---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/delete-a-channel.html
---

# DELETE: Delete a Channel
<a name="delete-a-channel"></a>

Delete the channel that has the specified ID. To get the ID of a specific channel, see [GET List: Get List of Channels](get-list-of-channels.md).

The channel must be in a state that allows it to be deleted. To check the status, use GET Channel. For information on the status, see [Channel Status Elements](monitoring-manage-channels.md#monitoring-manage-channels-status).

## HTTP Request and Response
<a name="delete-a-channel-http-request-response"></a>

### Request URL
<a name="delete-a-channel-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/channels/<ID of channel>
```

### Call Header
<a name="delete-a-channel-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="delete-a-channel-example"></a>

This request deletes the channel with the ID 2.

```
DELETE http://198.51.100.0/channels/2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
