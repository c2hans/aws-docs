---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.delete-practice-run-config.html
---

# Delete a practice run configuration
<a name="getting-started-cli-zonal-autoshift.delete-practice-run-config"></a>

You can delete a practice run configuration for a resource, but you must first disable zonal autoshift for the resource. A resource is required to have a practice run configuration to have zonal autoshift enabled. Regular practice runs help you to make sure that your application can run normally without one Availability Zone.

To delete a practice run configuration by using the CLI, first, disable zonal autoshift, if needed by using the `update-zonal-autoshift` command. Then, to delete the practice run configuration, use the `delete-practice-run-configuration` command.

First, disable zonal autoshift for the resource, using a command like the following:

```
aws arc-zonal-shift update-zonal-autoshift-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}" \
      --zonal-autoshift-status="DISABLED"
```

```
{
   "resourceIdentifier": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "zonalAutoshiftStatus": "DISABLED"
}
```

Then, delete the practice run configuration, using a command like the following:

```
aws arc-zonal-shift delete-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:{{Region}}:{{111122223333}}:{{ExampleALB123456890}}"
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "TestResource",
   "zonalAutoshiftStatus": "DISABLED"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
