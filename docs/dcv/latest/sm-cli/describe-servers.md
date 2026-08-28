---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/describe-servers.html
---

# describe-servers
<a name="describe-servers"></a>

Describe the specified Amazon DCV server.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
describe-servers
[--server-ids {{<value>}}]
[--next-token {{<value>}}]
[--max-results {{<value>}}]
```

## Options
<a name="options"></a>

**`--server-ids`**
The comma-separated list of IDs of the Amazon DCV servers to describe.
Type: String
Required: No

**`--next-token`**
The token to use to retrieve the next page of results.
Type: String
Required: No

**`--max-results`**
The maximum number of results to be returned by the request in paginated output. If provided, this must be a number between 1 and 1000.
Type: Integer
Required: No

## Example
<a name="example"></a>

```
dcvsm describe-servers --server-ids "server123,server456"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
