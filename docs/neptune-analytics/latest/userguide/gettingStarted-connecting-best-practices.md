---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-best-practices.html
---

# Best practices
<a name="gettingStarted-connecting-best-practices"></a>

 Ensure the streams have been consumed and closed to be able to re-use client connections in the SDK. See the [ SDK for Java developer guide ](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices.html#bestpractice2) for more information.

 **CLI and SDK**

 Using the default settings, any CLI or SDK request will timeout in 60 seconds and attempt a retry. For the cases where you are running queries that can take longer than 60 seconds, it is recommended to set the CLI/SDK timeout to 0 (no timeout), or a much larger value to avoid unnecesssary retries. It is also recommended to set `MAX_ATTEMPTS` for CLI/SDK to `1` for `execute_query` to avoid any retries by the CLI/SDK. For the Boto client, set the `read_timeout` to `None`, and the `total_max_attempts` to `1`.

```
import boto3
from botocore.config import Config
n = boto3.client('neptune-graph',
                 config=(Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)))
```

 For the CLI, set the `--cli-read-timeout` parameter to `0` for no timeout, and set the environment variable `AWS_MAX_ATTEMPTS` to `1` to prevent retries.

```
export AWS_MAX_ATTEMPTS=1
aws neptune-graph execute-query \
--graph-identifier <graph-id> \
--region <region> \
--query-string "MATCH (p:Person)-[r:KNOWS]->(p1) RETURN *;" \
--cli-read-timeout 0
--language open_cypher /tmp/out.txt
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
