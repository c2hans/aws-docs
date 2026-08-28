---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.start-practice-run.html
---

# Start an on-demand practice run
<a name="getting-started-cli-zonal-autoshift.start-practice-run"></a>

You can start an on-demand practice run zonal shift with the CLI by using the `start-practice-run` command.

For example, to start a practice run for a resource, use a command like the following:

```
aws arc-zonal-shift start-practice-run
    --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
    "awayFrom": "usw2-az1",
```

```
{
    "awayFrom": "usw2-az1",
    "comment": "Practice run started. Shifting traffic away from Availability Zone usw2-az1.",
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
