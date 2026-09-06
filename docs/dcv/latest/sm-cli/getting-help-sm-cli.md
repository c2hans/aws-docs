---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/getting-help-sm-cli.html
---

# Getting help with commands
<a name="getting-help-sm-cli"></a>

You can get help with any command when using the Amazon DCV Session Manager CLI. To do so, simply type `--help` at the end of a command name.

**Example**
For example, the following command displays help for the general DCV SM CLI options and the available top-level commands.

```
dcvsm --help
```
The following example shows the output of the CLI help.

```
Usage: dcvsm [OPTIONS] COMMAND [ARGS]...

  Amazon DCV Session Manager CLI

Options:
  --conf TEXT           Name of the configuration file to read the
                        configuration parameters
  --broker-url TEXT     The URL of the broker
  --debug               Specify to enable the debug mode. By default is
                        disabled
  --no-verify-ssl       Specify to disable the verification of SSL
                        certification. By default is enabled
  --output-format TEXT  Specify the format of the output
  --ca-bundle TEXT      Specifies the path to a custom certificate bundle
                        (a file with a .pem extension) of CA to use when
                        establishing SSL/TLS connections
  --auth-server TEXT    URL of the authentication server used to request
                        the token
  --version             Show the version and exit.
  -h, --help            Show this message and exit.

Commands:
  close-servers                 Closes one or more Amazon DCV server
  create-session               Creates a new Amazon DCV session
  delete-session               Deletes the specified Amazon DCV session
  describe-servers             Describes one or more Amazon DCV servers
  describe-sessions            Describes one or more Amazon DCV sessions
  get-session-connection-data  Gets connection data for a specific Amazon DCV session.
  get-session-screenshots      Gets screenshots of one or more Amazon DCV sessions.
  open-servers                 Opens one or more Amazon DCV servers
  update-session-permissions   Updates the user permissions for a specific Amazon DCV session.
```
All commands accept --help for contextual help information. For example, the following command displays help for the create-session command.

```
dcvsm create-session --help
```
The following example shows the output for the `create-session --help` command.

```
Usage: dcvsm create-session [OPTIONS]

  Create sessions API

Options:
  --name TEXT                     The name for the session  [required]
  --owner TEXT                    The name of the session owner  [required]
  --type TEXT                     Session type: CONSOLE|VIRTUAL  [required]
  --init-file-path TEXT           Supported with virtual sessions on Linux
                                  Amazon DCV servers
  --autorun-file TEXT             The path to a file on the host server that
                                  is to be run inside the session
  --autorun-file-arguments TEXT   Command-line arguments passed to AutorunFile
                                  upon its execution inside the session
  --max-concurrent-clients INTEGER RANGE
                                  The maximum number of concurrent Amazon DCV
                                  clients, if provided must be between 1 and
                                  100 [1<=x<=100]
  --dcv-gl-enabled                Indicates whether the virtual session is
                                  configured to use hardware-based OpenGL.
                                  Specify to enable it, by default is disabled
  --permissions-file TEXT         The Base64-encoded contents of the
                                  permissions file
  --requirements TEXT             The requirements that the server must
                                  satisfy in order to place the session
  --storage-root TEXT             Specifies the path to the folder used for
                                  session storage
  -h, --help                          Show this message and exit.
```

The Amazon DCV SM CLI Command Reference also contains the help content for all Amazon DCV SM CLI commands. All commands in the Amazon DCV SM CLI correspond to requests made to the APIs of the broker. Each API has an API reference that can be found on the Amazon DCV Session Manager Developer Guide section.

## Parameter types
<a name="specify-parameter-types"></a>

If you're having trouble formatting an option or argument for a specific command, the help for each command describes its function and options accepted.

### String
<a name="string"></a>

String parameters can contain letters, numbers,and white space. Strings that contain white space must be surrounded by quotation marks. Strings can be surrounded by single quotation marks, double quotation marks, or without them. We recommend that you don't use symbols because it can cause unexpected results.

### List
<a name="list"></a>

One or more strings separated by comma and surrounded by quotation marks. The following example shows a list of `--session-ids`.

```
dcvsm describe-sessions --session-ids "session123,session456"
```

### Boolean
<a name="boolean"></a>

Binary flag that turns an option on or off. For example, --debug describe-sessions has a Boolean --debug option that, when specified, calls the API enabling the debugging.

```
dcvsm --debug describe-sessions
```

If you don’t specify explicitly a boolean option, it’s set to FALSE by default.

### Integer
<a name="integer"></a>

An unsigned, whole number.

```
dcvsm describe-sessions --max-results 2
```
