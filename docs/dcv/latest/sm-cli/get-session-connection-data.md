---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/get-session-connection-data.html
---

# get-session-connection-data
<a name="get-session-connection-data"></a>

Gets connection information for a specific user's connection to a specific Amazon DCV session.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
get-session-connection-data
--session-id {{<value>}}
--user {{<value>}}
```

## Options
<a name="options"></a>

**`--session-id`**
The ID of the Amazon DCV sessions to get connection data from.
Type: String
Required: Yes

**`--user`**
The name of the user to view connection information for.
Type: Boolean
Required: Yes

## Example
<a name="example"></a>

```
./dcvsm get-session-connection-data --session-id session123
--user dcvuser
```
