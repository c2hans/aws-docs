---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/command-line-options.html
---

# Command line options
<a name="command-line-options"></a>

In the Amazon DCV Session Manager, you can use the following command line options to override the default configuration settings, any corresponding profile setting, or environment variable setting for that single command. You can't use command line options to directly specify credentials. Each option that takes an argument requires a space or equals sign (=) separating the argument from the option name.

**`--conf`**
Specifies the path of the configuration file. If it’s not defined the CLI will use the default configuration file. For more information about the configureation file, see [Configuration file](configuration-file.md).
Type: String

**`--broker-url`**
Specifies the URL to send the request to.
Type: String

**`--debug`**
A Boolean switch that enables debug logging. By default, the DCV SM CLI provides cleaned up information regarding any successes or failures regarding command outcomes in the command output. The --debug option provides the full logs. This includes additional stderr diagnostic information about the operation of the command that can be useful when troubleshooting why a command provides unexpected results.
Type: Boolean
Type: String

**`--no-verify-ssl`**
With this option, you can disable SSL certificate verification, but it's discouraged for security reasons. By default, the DCV SM CLI uses SSL when communicating with broker services.
Type: Boolean

**`--ca-bundle`**
Specifies the path to a custom certificate bundle (a file with a `.pem` extension) of CA to use when establishing SSL/TLS connections

**`--auth-server-url`**
Specifies the hostname of the authentication server that's used to request the OAuth 2.0 access token. If it’s not specified, the broker url is used.
Type: String

**`--version`**
Displays the current version of the DCV SM CLI program that's running.
Type: String

**`--help`**
Display the list of options and commands of the DCV SM CLI.
Type: String

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
