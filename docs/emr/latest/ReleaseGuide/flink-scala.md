---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-scala.html
---

# Use the Scala shell
<a name="flink-scala"></a>

The Flink Scala shell for EMR clusters is only configured to start new YARN sessions. You can use the Scala shell by following the procedure below.

**Use the Flink Scala shell on the primary node**

1. Log in to the primary node with SSH as described in [Connect to the primary node with SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html).

1. Type the following to start a shell:

   In Amazon EMR version 5.5.0 and later, you can use the following command to start a Yarn cluster for the Scala Shell with one TaskManager.

   ```
   % flink-scala-shell yarn {{1}}
   ```

   In earlier versions of Amazon EMR, use:

   ```
   % /usr/lib/flink/bin/start-scala-shell.sh yarn {{1}}
   ```

   This starts the Flink Scala shell so you can interactively use Flink. Just as with other interfaces and options, you can scale the `-n` option value used in the example based on the number of tasks you want to run from the shell.

   For more information, see [Scala REPL](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/deployment/repls/scala_shell/) in the official Apache Flink documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
