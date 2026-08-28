---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/record-single-action-interaction.html
---

# Recording a single action interaction event
<a name="record-single-action-interaction"></a>

After you create an Action interactions dataset, you are ready to record action interaction events with the [PutActionInteractions](API_UBS_PutActionInteractions.md) operation. The following code shows a `PutActionInteractions` operation that passes a TAKEN event. You might record this event when you show a user recommendations from Amazon Personalize and they take an action, such as applying for your credit card.

The `actionInteractions` is an array of ActionInteraction objects. The `trackingId` comes from the event tracker Amazon Personalize created when you created your Action interactions dataset. For more information, see [Finding the ID of your action interaction event tracker](action-interaction-tracker-id.md).

Your application generates a unique `sessionId` when a user first visits your website or uses your application. You must use the same `sessionId` in all events throughout the session. Amazon Personalize uses the `sessionId` to associate events with the user before they log in (is anonymous). For more information, see [Recording events for anonymous users](recording-events.md#recording-anonymous-user-events).

The `userId`, `actionId`, and `sentAt` parameters map to the USER\_ID, ACTION\_ID, EVENT\_TYPE, and TIMESTAMP fields of the Action interactions dataset.

**Corresponding Action interactions dataset**

```
USER_ID, ACTION_ID, TIMESTAMP, EVENT_TYPE
user123, action-xyz, 1543631760, TAKEN
```

**Code example**

------
#### [ AWS CLI ]

```
aws personalize-events put-action-interactions \
--tracking-id {{12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx}} \
--action-interactions '[{
  "userId": "{{user123}}",
  "sessionId": "{{abcdefg}}",
  "timestamp": {{1543631760}},
  "eventType": "{{TAKEN}}",
  "actionId": "{{action-xyz}}"}]'
```

------
#### [ SDK for Python (Boto3) ]

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

response = personalize_events.put_action_interactions(
  trackingId='{{12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx}}',
  actionInteractions=[{
    'userId': '{{user123}}',
    'sessionId': '{{abcdefg}}',
    'timestamp': {{1543631760}},
    'eventType': '{{Taken}}',
    'actionId': '{{action-xyz}}'
  }]
)
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
