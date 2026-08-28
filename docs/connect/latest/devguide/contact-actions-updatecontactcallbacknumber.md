---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontactcallbacknumber.html
---

# UpdateContactCallbackNumber
<a name="contact-actions-updatecontactcallbacknumber"></a>

Updates the contact callback number, which is the number used by the CreateCallbackContact action. This value defaults to the customer participant caller ID if this action is never used.

## Parameter object
<a name="updatecontactcallbacknumber-parameter"></a>

```
{
    "CallbackNumber": The callback number to set. Must be a single, valid JSONPath reference, and cannot be set statically.
}
```

## Results and conditions
<a name="updatecontactcallbacknumber-results"></a>

None.

## Errors
<a name="updatecontactcallbacknumber-errors"></a>
+ InvalidCallbackNumber - The callback number specified was not a valid (e.164) phone number.
+ CallbackNumberNotDialable - The callback number specified is not dialable by the instance.

## Restrictions
<a name="updatecontactcallbacknumber-restrictions"></a>

This is supported only in contact flows, transfer flows, and customer queue flows. This is not supported in whispers or hold flows.

## Corresponding block in the UI
<a name="updatecontactcallbacknumber-ui"></a>

[Set callback number](https://docs.aws.amazon.com/connect/latest/adminguide/set-callback-number.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
