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
