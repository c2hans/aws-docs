---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/configuration-file.html
---

# Configuration file
<a name="configuration-file"></a>

The configuration file is the third way to specify some configuration options and credentials. By default, it's provided in the zip file at `/conf/dcvsmcli.conf`.

The user can specify the path of the configuration file at command line. If the user does not specify it explicitly the config file it will be read by default from a specific folder depending on the operating systems:
+ Unix based systems: `$XDG_CONFIG_HOME/dcvsmcli.conf`
+ Windows systems: `%UserProfile%\dcvsmcli.conf`

If the configuration file isn't found, the CLI reads the file from the path `/conf/dcvsmcli.conf` provided with the zip file. The configuration file is structured as follows:

```
[output]
# The formatting style for command output.
output-format = json

# Turn on debug logging
debug = true

[security]
# Disable SSL certificates verification.
no-verify-ssl = true

# CA certificate bundle to use when verifying SSL certificates.
ca-bundle = ca-bundle.pem

[authentication]
# hostname of the authentication server used to request the token
auth-server-url = https://broker-host:broker-port/oauth2/token?grant_type=client_credentials

# The client ID
client-id = username

# The client password
client-password = password

[broker]
# hostname or IP of the broker
url = https://broker-host:broker-port
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
