---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/describe-sessions.html
---

# describe-sessions
<a name="describe-sessions"></a>

Describes one or more Amazon DCV servers.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
describe-sessions
[--session-ids {{<value>}}]
[--next-token {{<value>}}]
[--owner {{<value>}}]
[--max-results {{<value>}}]
```

## Options
<a name="options"></a>

**`--session-ids`**
The comma-separated list of IDs of the Amazon DCV sessions to describe.
Type: String
Required: No

**`--next-token`**
The token to retrieve the next page of results.
Type: String
Required: No

**`--owner`**
The owner of the session to describe.
Type: String
Required: No

**`--max-results`**
The number of results to show. If provided, must be between 1 and 1000.
Type: Integer
Required: No

## Example
<a name="example"></a>

```
dcvsm describe-sessions --session-ids "session123,session456"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
