---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-install-worker.html
---

# Installing AWS Elemental Server on a worker node
<a name="migrate-topic-install-worker"></a>

This install procedure isn't the same as the install procedure on a newly obtained appliance. You don't have to configure the node.

This install procedure is very similar to the upgrade procedure, but there are significant differences in the options you include.

1. From the Linux command line, log in to the worker node. Use the **elemental** user credentials.

1. Run the installer. Use the appropriate command:
   + For GPU versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_server_2.18.0.12345.run --skip-all --start -xeula
     ```
   + For CPU-only versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_server_cpu_2.18.0.12345.run --skip-all --start -xeula
     ```

   Where:

   `--skip-all` skips all the prompts. There is no need to view prompts about configuration because when you restore the database to the node, all the configuration data is copied over and overwrites any configuration data already on the node.

   `--start` restarts the software after installation.

   `--xeula` skips the display of the license agreement. There is no need to view this prompt because you have previously accepted the agreement.

1. When the installation is complete, restart the node:

   ```
   [elemental@hostname ~] sudo reboot
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
