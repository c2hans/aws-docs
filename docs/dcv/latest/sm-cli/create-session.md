---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/create-session.html
---

# create-session
<a name="create-session"></a>

Creates a new Amazon DCV session with the specified details.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
create-session
--name {{<value>}}
--owner {{<value>}}
--type {{<value>}}
[--init-file-path {{<value>}}]
[--autorun-file {{<value>}}]
[--autorun-file-arguments {{<value>}}]
[--max-concurrents-clients {{<value>}}]
[--dcv-gl-enabled]
[--permissions-file {{<value>}}]
[--requirements {{<value>}}]
[--storage-root {{<value>}}]
[--enqueue-request {{<value>}}]
```

## Options
<a name="options"></a>

**`--name`**
The name of the session.
Type: String
Required: Yes

**`--owner`**
The name of the session owner.
Type: String
Required: Yes

**`--type`**
The session type. This is either `Console` or `Virtual`.
Type: Choice
Required: Yes

**`--init-file-path`**
The path to the custom script on the Amazon DCV server to run for initializing the session when it's created. The file path is relative to the `init` directory specified for the `agent.init-folder` Agent configuration parameter.
Type: String
Required: No

**`--autorun-file`**
The path to a file on the host server that's to be run inside the session. The file path is relative to the `autorun` directory specified for the `agent.autorun-folder` Agent configuration parameter.
Type: String
Required: No

**`--autorun-file-arguments`**
The command-line arguments passed to `AutorunFile` when it's run inside the session.
Type: String
Required: No

**`--max_concurrent-clients`**
The maximum number of concurrent Amazon DCV clients. If provided, this must be between 1 and 100.
Type: Integer
Required: No

**`--dcv-gl-enabled`**
Configures the virtual session to use hardware-based OpenGL. It's disabled by default.
Type: Boolean
Required: No

**`--permissions-file`**
The path to the permissions file.
Type: String
Required: No

**`--requirements`**
The requirements that the server must meet to place the session.
Type: String
Required: No

**`--storage-root`**
The path to the folder used for session storage.
Type: String
Required: No

**`--enqueue-request`**
Indicates whether to queue the request if it cannot be immediately fulfilled. Requests are not enqueued by default.
Type: Boolean
Required: No

## Example
<a name="example"></a>

```
dcvsm create-session --name session123 --owner sessionOwner
--type Console --requirements "server:Host.Os.Family = 'windows'"
```
