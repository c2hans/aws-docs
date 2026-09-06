---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/cli-command-syntax.html
---

# CLI command syntax
<a name="cli-command-syntax"></a>

You can use CLI commands by using the following syntax:

```
aws-vpn-client <COMMAND> [OPTIONS]
```

The CLI tool supports the following commands.

```
Usage: aws-vpn-client <COMMAND>

Commands:
  connect                Connect a profile through the AWS VPN Client
  disconnect             Disconnect a profile from the AWS VPN Client
  delete-profile         Delete a profile from the AWS VPN Client
  import-profile         Import a VPN connection profile
  list-profiles          List all VPN profiles
  get-config             Get configuration for a profile
  put-preference         Put a preference value
  list-preferences       List all preferences
  get-connection-status  Get the current connection status for a VPN profile
  list-connections       List all active VPN connections
  send-diagnostic-logs   Send diagnostic logs to AWS for troubleshooting
  help                   Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
```

## connect
<a name="cli-cmd-connect"></a>

### Description
<a name="cli-cmd-connect-description"></a>

Establish a VPN connection to a profile.

### Synopsis
<a name="cli-cmd-connect-synopsis"></a>

```
aws-vpn-client connect
  --profile-name <PROFILE>
  [--auth-user-pass <AUTH_USER_PASS>]
```

### Options
<a name="cli-cmd-connect-options"></a>

`--profile-name` (string)
The name of the profile to connect. This option is required.

`--auth-user-pass` (string)
Path to a file containing the username (line 1), password (line 2), and optional MFA code (line 3). This option is not required.

### Examples
<a name="cli-cmd-connect-examples"></a>

**Example: Connect to a VPN profile**

The following `connect` example establishes a VPN connection to a profile.

```
aws-vpn-client connect --profile-name "Production-VPN"
```

Output:

```
{
  "status": "Connected"
}
```

## disconnect
<a name="cli-cmd-disconnect"></a>

### Description
<a name="cli-cmd-disconnect-description"></a>

Terminate an active VPN connection.

### Synopsis
<a name="cli-cmd-disconnect-synopsis"></a>

```
aws-vpn-client disconnect
  --profile-name <PROFILE_NAME>
```

### Options
<a name="cli-cmd-disconnect-options"></a>

`--profile-name` (string)
The name of the connected profile to disconnect. This option is required.

### Examples
<a name="cli-cmd-disconnect-examples"></a>

**Example: Disconnect from a VPN profile**

The following `disconnect` example terminates a VPN connection. There is no output on success.

```
aws-vpn-client disconnect --profile-name "Production-VPN"
```

**Example: Disconnect error**

The following `disconnect` example shows the error when the profile is not connected.

```
aws-vpn-client disconnect --profile-name "Production-VPN"
```

Output:

```
{
  "status": "Error",
  "message": "Profile is not connected"
}
```

## import-profile
<a name="cli-cmd-import-profile"></a>

### Description
<a name="cli-cmd-import-profile-description"></a>

Import a VPN connection profile.

### Synopsis
<a name="cli-cmd-import-profile-synopsis"></a>

```
aws-vpn-client import-profile
  --profile-name <PROFILE_NAME>
  --config-path <CONFIG_PATH>
  [--global]
```

### Options
<a name="cli-cmd-import-profile-options"></a>

`--profile-name` (string)
Custom name for the imported profile. This option is required.

`--config-path` (string)
Path to the OpenVPN configuration file (.ovpn). This option is required.

`--global` (boolean)
Import as a global profile available to all users. This option requires administrator privileges.

### Examples
<a name="cli-cmd-import-profile-examples"></a>

**Example: Import a profile**

The following `import-profile` example imports a VPN connection profile.

```
aws-vpn-client import-profile --profile-name "Production-VPN" --config-path /path/to/vpn-config.ovpn
```

Output:

```
{
  "status": "Success"
}
```

**Example: Import a global profile**

The following `import-profile` example imports a global profile. This requires administrator privileges.

```
sudo aws-vpn-client import-profile --profile-name "Company-VPN" --config-path /path/to/config.ovpn --global
```

Output:

```
{
  "status": "Success"
}
```

**Example: Import error with invalid file path**

The following `import-profile` example shows the error when the configuration file is not found.

```
aws-vpn-client import-profile --profile-name "test" --config-path /invalid/path.ovpn
```

Output:

```
{
  "status": "Error",
  "message": "Failed to read OpenVPN config file: No such file or directory (os error 2)"
}
```

## delete-profile
<a name="cli-cmd-delete-profile"></a>

### Description
<a name="cli-cmd-delete-profile-description"></a>

Delete a profile from the client.

### Synopsis
<a name="cli-cmd-delete-profile-synopsis"></a>

```
aws-vpn-client delete-profile
  --profile-name <PROFILE_NAME>
```

### Options
<a name="cli-cmd-delete-profile-options"></a>

`--profile-name` (string)
The name of the profile to delete. This option is required.

### Examples
<a name="cli-cmd-delete-profile-examples"></a>

**Example: Delete a profile**

The following `delete-profile` example deletes a VPN profile. There is no output on success.

```
aws-vpn-client delete-profile --profile-name "Production-VPN"
```

**Example: Delete error with nonexistent profile**

The following `delete-profile` example shows the error when the profile does not exist.

```
aws-vpn-client delete-profile --profile-name "nonexistent"
```

Output:

```
{
  "status": "Error",
  "message": "Profile not found"
}
```

## list-profiles
<a name="cli-cmd-list-profiles"></a>

### Description
<a name="cli-cmd-list-profiles-description"></a>

List all VPN profiles.

### Synopsis
<a name="cli-cmd-list-profiles-synopsis"></a>

```
aws-vpn-client list-profiles
```

### Examples
<a name="cli-cmd-list-profiles-examples"></a>

**Example: List all VPN profiles**

The following `list-profiles` example lists all imported VPN profiles.

```
aws-vpn-client list-profiles
```

Output:

```
[
  {
    "profile-name": "Production-VPN",
    "owned-by": "jdoe",
    "auth-type": "saml",
    "imported-at": "2026-07-21T13:04:42-07:00"
  },
  {
    "profile-name": "Staging-VPN",
    "owned-by": "jdoe",
    "auth-type": "ma",
    "imported-at": "2026-07-22T10:30:00-07:00"
  }
]
```

**Note**
Global profiles (imported with `--global`) do not have an `owned-by` field.

## get-config
<a name="cli-cmd-get-config"></a>

### Description
<a name="cli-cmd-get-config-description"></a>

Retrieve the OpenVPN configuration for a profile.

### Synopsis
<a name="cli-cmd-get-config-synopsis"></a>

```
aws-vpn-client get-config
  --profile-name <PROFILE_NAME>
```

### Options
<a name="cli-cmd-get-config-options"></a>

`--profile-name` (string)
The name of the profile to retrieve configuration for. This option is required.

### Examples
<a name="cli-cmd-get-config-examples"></a>

**Example: Retrieve OpenVPN configuration**

The following `get-config` example retrieves the OpenVPN configuration for a profile.

```
aws-vpn-client get-config --profile-name "Production-VPN"
```

Output:

```
client
dev tun
proto udp
remote cvpn-endpoint-0123456789abcdef0.prod.clientvpn.us-east-1.amazonaws.com 443
remote-random-hostname
resolv-retry infinite
nobind
remote-cert-tls server
cipher AES-256-GCM
verb 3
<ca>
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
</ca>
auth-user-pass
reneg-sec 0
```

## get-connection-status
<a name="cli-cmd-get-connection-status"></a>

### Description
<a name="cli-cmd-get-connection-status-description"></a>

Get the current connection status for a VPN profile.

### Synopsis
<a name="cli-cmd-get-connection-status-synopsis"></a>

```
aws-vpn-client get-connection-status
  --profile-name <PROFILE_NAME>
  [--show-details]
```

### Options
<a name="cli-cmd-get-connection-status-options"></a>

`--profile-name` (string)
The name of the profile to retrieve connection status for. This option is required.

`--show-details` (boolean)
Include connection byte statistics in the output.

### Examples
<a name="cli-cmd-get-connection-status-examples"></a>

**Example: Get connection status**

The following `get-connection-status` example retrieves the connection status for a profile.

```
aws-vpn-client get-connection-status --profile-name "Production-VPN"
```

Output:

```
{
  "connection-status": "Connected",
  "latest-connection-attempt": {
    "initiated-by": "jdoe",
    "updated-at": "2026-07-24T15:50:36-07:00"
  }
}
```

**Example: Get connection status with details**

The following `get-connection-status` example includes byte statistics by using the `--show-details` option.

```
aws-vpn-client get-connection-status --profile-name "Production-VPN" --show-details
```

Output:

```
{
  "connection-status": "Connected",
  "latest-connection-attempt": {
    "initiated-by": "jdoe",
    "updated-at": "2026-07-24T15:50:36-07:00",
    "details": {
      "tunnel-bytes-in": 0,
      "tunnel-bytes-out": 0,
      "transport-bytes-in": 9674,
      "transport-bytes-out": 11413
    }
  }
}
```

## list-connections
<a name="cli-cmd-list-connections"></a>

### Description
<a name="cli-cmd-list-connections-description"></a>

List all active VPN connections.

### Synopsis
<a name="cli-cmd-list-connections-synopsis"></a>

```
aws-vpn-client list-connections
```

### Examples
<a name="cli-cmd-list-connections-examples"></a>

**Example: List active connections**

The following `list-connections` example lists all active VPN connections.

```
aws-vpn-client list-connections
```

Output:

```
[
  {
    "profile-name": "Production-VPN",
    "initiated-by": "jdoe",
    "connection-status": "Connected",
    "last-updated-at": "2026-07-24T15:50:36-07:00"
  }
]
```

**Example: No active connections**

The following `list-connections` example shows the output when there are no active connections.

```
aws-vpn-client list-connections
```

Output:

```
[]
```

## put-preference
<a name="cli-cmd-put-preference"></a>

### Description
<a name="cli-cmd-put-preference-description"></a>

Set a global configuration preference. Most settings require administrator privileges.

### Synopsis
<a name="cli-cmd-put-preference-synopsis"></a>

```
aws-vpn-client put-preference
  --key <PREFERENCE_KEY>
  --value <PREFERENCE_VALUE>
```

### Options
<a name="cli-cmd-put-preference-options"></a>

`--key` (string)
The name of the preference key to set. This option is required.

`--value` (string)
The value to set for the preference key. This option is required.

The following preference keys are available:

`enable-telemetry`
Enable or disable telemetry (true/false).

`enable-user-profile-management`
Allow or disallow end users to import or delete profiles (true/false).

`max-connections`
Maximum number of concurrent connections (integer, 1-5).

### Examples
<a name="cli-cmd-put-preference-examples"></a>

**Example: Set a preference**

The following `put-preference` example sets the maximum number of connections. This requires administrator privileges. There is no output on success.

```
sudo aws-vpn-client put-preference --key max-connections --value 4
```

**Example: Error without administrator privileges**

The following `put-preference` example shows the error when you run the command without administrator privileges.

```
aws-vpn-client put-preference --key max-connections --value 4
```

Output:

```
{
  "status": "Error",
  "message": "Permission denied: admin privileges required"
}
```

**Example: Error with invalid value**

The following `put-preference` example shows the error when you provide an invalid value.

```
sudo aws-vpn-client put-preference --key max-connections --value 8
```

Output:

```
{
  "status": "Error",
  "message": "Preference value is invalid"
}
```

## list-preferences
<a name="cli-cmd-list-preferences"></a>

### Description
<a name="cli-cmd-list-preferences-description"></a>

Display all global configuration preferences and current values.

### Synopsis
<a name="cli-cmd-list-preferences-synopsis"></a>

```
aws-vpn-client list-preferences
```

### Examples
<a name="cli-cmd-list-preferences-examples"></a>

**Example: List all preferences**

The following `list-preferences` example displays all global configuration preferences and their current values.

```
aws-vpn-client list-preferences
```

Output:

```
{
  "enable-telemetry": true,
  "enable-user-profile-management": true,
  "max-connections": 1
}
```

## send-diagnostic-logs
<a name="cli-cmd-send-diagnostic-logs"></a>

### Description
<a name="cli-cmd-send-diagnostic-logs-description"></a>

Collect and submit diagnostic logs to AWS for troubleshooting.

### Synopsis
<a name="cli-cmd-send-diagnostic-logs-synopsis"></a>

```
aws-vpn-client send-diagnostic-logs
```

### Examples
<a name="cli-cmd-send-diagnostic-logs-examples"></a>

**Example: Send diagnostic logs**

The following `send-diagnostic-logs` example collects and submits diagnostic logs to AWS.

```
aws-vpn-client send-diagnostic-logs
```

Output:

```
{
  "reference-id": "us-west-2:78ff6531-5dc4-c706-7149-e6cfd8adadc7/2026-07-24-16-03-55.zip"
}
```

**Note**
Share the `reference-id` value with AWS Support when reporting issues.

## Exit codes
<a name="cli-cmd-exit-codes"></a>

The AWS Client VPN CLI tool returns the following exit codes.

| Exit code | Meaning |
| --- | --- |
| 0 | Success |
| 1 | General error |
| 2 | Invalid command syntax |
