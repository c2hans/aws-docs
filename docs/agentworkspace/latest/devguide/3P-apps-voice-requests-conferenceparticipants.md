---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-conferenceparticipants.html
---

# Conference all participants on a contact in Connect Customer agent workspace
<a name="3P-apps-voice-requests-conferenceparticipants"></a>

Conferences all participants on a contact together, removing any hold states and enabling all participants to communicate with each other.

 **Signature**

```
conferenceParticipants(contactId: string): Promise<void>
```

 **Usage**

```
await voiceClient.conferenceParticipants("contact-123");
console.log("All participants are now conferenced");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| contactId Required | string | The unique identifier for the contact |
