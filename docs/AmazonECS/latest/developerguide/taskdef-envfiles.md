---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html
---

# Pass an individual environment variable to an Amazon ECS container
<a name="taskdef-envfiles"></a>

**Important**
We recommend storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md).
Environment variables specified in the task definition are readable by all users and roles that are allowed the `DescribeTaskDefinition` action for the task definition.

You can pass environment variables to your containers in the following ways:
+ Individually using the `environment` container definition parameter. This maps to the `--env` option to [**docker container run**](https://docs.docker.com/reference/cli/docker/container/run/).
+ In bulk, using the `environmentFiles` container definition parameter to list one or more files that contain the environment variables. The file must be hosted in Amazon S3. This maps to the `--env-file` option to [**docker run**](https://docs.docker.com/reference/cli/docker/container/run/).

The following is a snippet of a task definition showing how to specify individual environment variables.

```
{
    "family": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            ...
            "environment": [
                {
                    "name": "{{variable}}",
                    "value": "{{value}}"
                }
            ],
            ...
        }
    ],
    ...
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
