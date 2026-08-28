---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-redundancy-run.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step C: Run the Redundancy Install Script
<a name="config-cond-cf-cg-redundancy-run"></a>

This install script configures Conductor redundancy.

1. On the primary Conductor, enter the following command to run the database redundancy install script.

   ```
   [elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure dbrepl_config.yml primary
   ```

   where <dbrepl\_config> is the file that you created above.

1. You are prompted to restart the Conductor node.

   ```
   [elemental@hostname ~]$ sudo /etc/init.d/elemental_se restart
   ```

1. On the secondary Conductor, enter the following command to configure the secondary Conductor.

   ```
   [elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure dbrepl_config.yml secondary
   ```

   where <dbrepl\_config> is the file you created above.

1. You are prompted to restart the Conductor node.

   ```
   [elemental@hostname ~]$ sudo /etc/init.d/elemental_se restart
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
