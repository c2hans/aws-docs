---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/environment-variables.html
---

# Environment variables
<a name="environment-variables"></a>

Environment variables provide another way to specify some configuration options and credentials.

The following examples describe how you can configure environment variables for the default user.

## Set environment variables on Linux or macOS
<a name="linux-cli-variables"></a>

Run the following commands to set environment variables on Linux or macOS:

```
$  export DCV_SM_AUTH_SERVER_URL=https://example.com
```

```
$  export DCV_SM_CLIENT_ID=ExampleClientID
```

Setting the environment variable changes the value that's used until the end of your shell session, or until you set the variable to a different value. You can make the variables persistent across future sessions by setting them in the startup script of your shell.

## Set environment variables on Windows
<a name="windows-cli-variables"></a>

Run the following commands to set environment variables on Windows Command Prompt:

```
$  setx DCV_SM_AUTH_SERVER_URL https://example.com
```

```
$  setx DCV_SM_CLIENT_ID ExampleClientID
```

Using `[set](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/set_1)` to set an environment variable changes the value that's used until the end of the current command prompt session. Or, it's until you set the variable to a different value. Using `[setx](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/setx)` to set an environment variable changes the value that's used in both the current command prompt session and all command prompt sessions. These sessions you create after running the command. It doesn't affect other command shells that are already running at the time you run the command.

## Set environment variables using PowerShell
<a name="powershell-cli-variables"></a>

Run the following commands to set environment variables using PowerShell:

```
$  $Env:DCV_SM_AUTH_SERVER_URL="https://example.com"
```

```
$  $Env:DCV_SM_CLIENT_ID="ExampleClientID"
```

If you set an environment variable at the PowerShell prompt as shown in the previous examples, it saves the value for only the duration of the current session. To make the environment variable setting persistent across all PowerShell and Command Prompt sessions, store it by using the \*System\* application in \*Control Panel\*. Alternatively, you can set the variable for all future PowerShell sessions by adding it to your PowerShell profile. For more information about storing environment variables or persisting them across session, see [the PowerShell documentation](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables).

## Amazon DCV Session Manager supported environment variables
<a name="sm-cli-supported-variables"></a>

Amazon DCV Session Manager supports the following environment variables:
+ `DCV_SM_AUTH_SERVER_URL`

  Specifies the hostname of the authentication server that's used to request the OAuth 2.0 access token. If defined, this environment variable overrides the value of the configuration file.
+ `DCV_SM_CLIENT_ID`

  The unique client ID that's used by the Session Manager client to retrieve an OAuth 2.0 access token.
+ `DCV_SM_CLIENT_PASSWORD`

  The password that's used by the Session Manager client to retrieve an OAuth 2.0 access token.
+ `DCV_SM_OAUTH2_TOKEN`

  The access token that's used to make an API request.
