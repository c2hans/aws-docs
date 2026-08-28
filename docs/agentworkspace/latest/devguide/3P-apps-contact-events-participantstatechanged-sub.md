---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantstatechanged-sub.html
---

# Subscribe to participant state change events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantstatechanged-sub"></a>

Subscribes to participant state change events. This event fires when a participant's state changes (e.g., from connecting to connected, or to hold).

 **Signature**

```
onParticipantStateChanged(handler: ParticipantStateChangedHandler, participantId?: string): void
```

 **Usage**

```
    const handleStateChanged = (event) => {
    console.log(
    `Participant ${event.participantId} state changed to: ${event.state.value}`
    );

    if (event.state.value === "connected") {
    console.log("Participant is now connected");
    } else if (event.state.value === "hold") {
    console.log("Participant is now on hold");
    }
    };

    // Subscribe to all participants
    contactClient.onParticipantStateChanged(handleStateChanged);

    // Or subscribe to a specific participant
    contactClient.onParticipantStateChanged(handleStateChanged, "participant-456");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantStateChangedHandler | Event handler function to call when participant states change |
| participantId | string | Optional participant ID to filter events for a specific participant |

 **Event Structure - ParticipantStateChanged**

The handler receives a ParticipantStateChanged event with:
+ `participantId`: string - The ID of the participant whose state changed
+ `state`: ParticipantState - The new state of the participant

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
