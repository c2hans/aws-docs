---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-untagcontact.html
---

# UnTagContact
<a name="contact-actions-untagcontact"></a>

Removes a collection of tags on the current contact. With this type of operation, either all tags are set or none are set.

You cannot remove system-defined tags. You can only remove already existing user-defined tags from a contact.

## Parameter object
<a name="untagcontact-parameter"></a>

```
{
"TagKeys": [ an Object that holds the tag-keys for the tags to be removed.
     "Key1" Key(s) can only be set statically.
      ]
}
```

## Results and conditions
<a name="untagcontact-results"></a>

None.

## Errors
<a name="untagcontact-errors"></a>
+  NoMatchingError - if no other Error matches

## Restrictions
<a name="untagcontact-restrictions"></a>

This action is supported across all the Connect Customer media channels.

This action can be used in flows of all types.

## Corresponding block in the UI
<a name="untagcontact-ui"></a>

[Contact tags](https://docs.aws.amazon.com/connect/latest/adminguide/contact-tags-block.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
