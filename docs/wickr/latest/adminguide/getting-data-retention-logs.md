---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/getting-data-retention-logs.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Get the data retention logs for your Wickr network
<a name="getting-data-retention-logs"></a>

The software running on the data retention bot Docker image will output to log files in the `/tmp/{{<botname>}}/logs` directory. They will rotate to a maximum of 5 files. You can get the logs by running the following command.

```
docker logs {{<botname>}}
```

Example:

```
docker logs {{compliance_1234567890_bot}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
