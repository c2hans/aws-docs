---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-change-type.html
---

# Changing the instance type or size outside of the Auto Scaling group
<a name="container-instance-change-type"></a>

AWS recommends that you keep your infrastructure immutable. If you need to change instance sizes, you can either:
+ Scale horizontally and add additional instances. Then, place additional tasks on those instances, or you
+ Scale vertically by launching a new, larger/smaller instance and then drain the old instance.

Both of these approaches will help minimize application availability impact.

If you used another method to change the instance, you might receive the following error:

```
Container instance type changes are not supported.
```

When you get this error, perform the following steps:

1. Launch new instances with the desired instance type.

1. Drain your old instance types. For more information, see [Draining Amazon ECS container instances](container-instance-draining.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
