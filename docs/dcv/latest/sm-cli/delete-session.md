---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/delete-session.html
---

# delete-session
<a name="delete-session"></a>

Deletes the specified Amazon DCV session, and removes it from the cache of the broker.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
delete-session
--session-id {{<value>}}
--owner {{<value>}}
[--force]
```

## Options
<a name="options"></a>

**`--session-id`**
The ID of the session to delete.
Type: String
Required: Yes

**`--owner`**
The owner of the session to delete.
Type: String
Required: Yes

**`--force`**
The operation to ensure a session is removed from the cache of the broker. By default, this is disabled.
Type: Boolean
Required: No

## Example
<a name="example"></a>

```
dcvsm delete-session --session-id session123 --owner sessionOwner
--force
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
