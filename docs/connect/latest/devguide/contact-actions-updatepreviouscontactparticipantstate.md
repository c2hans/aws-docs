---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatepreviouscontactparticipantstate.html
---

# UpdatePreviousContactParticipantState
<a name="contact-actions-updatepreviouscontactparticipantstate"></a>

This action is primarily used to prevent previous participants on the contact from observing the contact. Common use cases are disconnecting the agent that initiates a transfer when they transfer a contact to a secure destination, or putting the agent on hold when transferring to a quick connect that securely gathers customer input such as credit card numbers.

## Parameter object
<a name="updatepreviouscontactparticipantstate-parameter"></a>

```
{
    "PreviousContactParticipantState": One of ["AgentOnHold", "CustomerOnHold", "OffHold"], which are only supported for voice contacts.
}
```

## Execution results and conditions
<a name="updatepreviouscontactparticipantstate-results"></a>

None.

## Errors
<a name="updatepreviouscontactparticipantstate-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatepreviouscontactparticipantstate-restrictions"></a>

This action is supported only in inbound contact flows and transfer flows.

## Corresponding block in the UI
<a name="updatepreviouscontactparticipantstate-ui"></a>

[Hold customer or agent](https://docs.aws.amazon.com/connect/latest/adminguide/hold-customer-agent.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
