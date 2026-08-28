---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-tagcontact.html
---

# TagContact
<a name="contact-actions-tagcontact"></a>

Sets a collection of tag to the current contact. With this type of operation, either all tags are set or none are set.

Each tag on a contact is a key-value pair, that is, it is composed of a key and a value. There are two types of tags: user-defined tags and system tags. You create a user-defined tag. A system tag is automatically created by AWS services. A system tag is prefixed with `aws:`. You cannot change it.

The TagContact action parameters correspond to user-defined tags that are applied on a contact.

## Parameter object
<a name="tagcontact-parameter"></a>

```
{
"Tags": { an Object that holds the tags to be set.
       "Key1":"Value1" Both the key and value may be defined statically or dynamically.
        }
}
```

## Results and conditions
<a name="tagcontact-results"></a>

None.

## Errors
<a name="tagcontact-errors"></a>

None.

## Restrictions
<a name="tagcontact-restrictions"></a>

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI
<a name="tagcontact-ui"></a>

[Contact tags](https://docs.aws.amazon.com/connect/latest/adminguide/contact-tags-block.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
