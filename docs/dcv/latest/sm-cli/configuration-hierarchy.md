---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/configuration-hierarchy.html
---

# Configuring the CLI settings
<a name="configuration-hierarchy"></a>

The Amazon DCV Session Manager uses credentials and configuration settings that are located in multiple places. These include user environment variables, local Amazon DCV Session Manager configuration file, or explicitly declared on the command line as a parameter. Certain locations take precedence over others.

The Amazon DCV Session Manager CLI credentials and configuration settings take precedence in the following order:
+ Command line options– Overrides settings in any other location.
+ Environment variables– Some values can be stored in your system's environment variables.
+ CLI configuration file– Specify options in the configuration file.

**Topics**
+ [Command line options](command-line-options.md)
+ [Environment variables](environment-variables.md)
+ [Configuration file](configuration-file.md)
