---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-auth-chg.html
---

# Disabling user authentication
<a name="conductor-live-config-auth-chg"></a>

This section describes how to disable user authentication on the cluster.

**To disable user authentication**

You disable user authentication by running the configuration script in the same way as you ran it to enable user authentication. In other words, if authentication is enabled and you include `--config-auth`, then the script disables authentication.

1. [Check if HA redundancy](config-conductor-live-ha-current-state.md) is currently enabled on the Conductor Live. If it is, [disable it ](conductor-live-config-ha-chg.md)now[Disabling Conductor Live HA (high availability)](conductor-live-config-ha-chg.md).

1. At your workstation, [start a remote terminal session](ready-conductor-live-config-access.md) to the primary Conductor Live node.

1. At the Linux prompt, log in with the *elemental* user credentials.

1. Change to the directory where the configuration script is located, then enter the configure command :

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   [elemental@hostname elemental_se]$ sudo ./configure --config-auth
   ```

1. Answer the prompts as follows:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-auth-chg.html)

   When you return to the web interface, you are not prompted to log in, and the menu to enable or disable node authentication on the worker nodes has disappeared.

1. The `configure` command in the previous step disables user authentication but leaves HTTPS enabled. Therefore, if you also want to disable HTTPS, enter the configure command as follows:

   ```
   [elemental@hostname elemental_se]$ sudo ./configure --https --skip-all
   ```

1. If applicable, [re-enable HA](conductor-live-config-ha.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
