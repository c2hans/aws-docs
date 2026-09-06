---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/update-session-permissions.html
---

# update-session-permissions
<a name="update-session-permissions"></a>

Updates the user permissions for a specific Amazon DCV session.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
update-session-permissions
--session-id {{<value>}}
--owner {{<value>}}
--permission-file {{<value>}}
```

## Options
<a name="options"></a>

**`--session-id`**
The ID of the session to change the permissions for.
Type: String
Required: Yes

**`--owner`**
The owner of the session to change the permissions for.
Type: String
Required: Yes

**`--permission-file`**
The path to the permissions file.
Type: String
Required: Yes

## Example
<a name="example"></a>

```
./dcvsm update-session-permissions --session-id session123
--owner Owner --permission-file path_to_file
```
