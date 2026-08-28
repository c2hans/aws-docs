---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-delete.html
---

# Delete a deployment configuration with CodeDeploy
<a name="deployment-configurations-delete"></a>

You can use the AWS CLI or the CodeDeploy APIs to delete custom deployment configurations associated with your AWS account. You cannot delete built-in deployment configurations, such as `CodeDeployDefault.AllAtOnce`, `CodeDeployDefault.HalfAtATime`, and `CodeDeployDefault.OneAtATime`.

**Warning**
You cannot delete a custom deployment configuration that is still in use. If you delete an unused, custom deployment configuration, you will no longer be able to associate it with new deployments and new deployment groups. This action cannot be undone.

To use the AWS CLI to delete a deployment configuration, call the [delete-deployment-config](https://docs.aws.amazon.com/cli/latest/reference/deploy/delete-deployment-config.html) command, specifying the deployment configuration name. To view a list of deployment configuration names, call the [list-deployment-configs](https://docs.aws.amazon.com/cli/latest/reference/deploy/list-deployment-configs.html) command.

The following example deletes a deployment configuration named ThreeQuartersHealthy.

```
aws deploy delete-deployment-config --deployment-config-name ThreeQuartersHealthy
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
