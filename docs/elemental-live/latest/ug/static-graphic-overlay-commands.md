---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/static-graphic-overlay-commands.html
---

# Static graphic overlay commands
<a name="static-graphic-overlay-commands"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| Create Event | POST | <Live IP address>/live\_events | Create an event that includes static overlay information. |
| Modify Event | PUT | <Live IP address>/live\_events/live\_event/<event ID> | Modify an event (that is not running) and add, modify or delete static overlay information. |
| Modify Static Overlay, Running Event | POST | /live\_event/<event ID>/image\_inserter | All outputs: add, modify or delete static information in a running event. |
| Modify Static Overlay, Running Event | POST | `<Live IP Address>/live_events/<event ID>/ image_inserter/output/<output id>`<br />Where `<output id>` is the unique ID automatically assigned to this output when the event is created. | Specific output: add, modify or delete static information in a running event. |
| Modify Static Overlay, Running Event | POST | `<Live IP Address>/live_events/<event ID>/ image_inserter/output/by_stream/<stream id>`<br />Where `<stream id>` is the unique ID automatically assigned to this stream when the event is created. The ID can change while the event is running (for example, if another stream is deleted), so you may need to obtain the current ID before sending this command. | All outputs associated with a specific stream: add, modify or delete static information in a running event. |
| Modify Static Overlay, Running Event | POST | `<Live IP Address>/live_events/<event ID>/ image_inserter/input/<input id>`<br />Where `<input id>` is the unique ID automatically assigned to this input when the event is created or when the input is added to the event. | Specific input, all outputs associated with it: add, modify or delete static information in a running event. |
| Modify Static Overlay, Running Event | POST | `<Live IP Address>/live_events/<event ID>/ image_inserter/input/by_label/<input label>`<br />Where `<input label>` is the input label you assigned when you created this event or created this input. Input labels are always optional. | Specific input, all outputs associated with it: add, modify or delete static information in a running event. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
