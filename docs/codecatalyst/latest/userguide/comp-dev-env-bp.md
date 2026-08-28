---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-dev-env-bp.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding Dev Environments components to a blueprint
<a name="comp-dev-env-bp"></a>

Managed development environments (MDE) are used to create and stand up MDE Workspaces in CodeCatalyst. The component generates a `devfile.yaml` file. For more information, see [Introduction to Devfile](https://redhat-developer.github.io/devfile/) and [Editing a repository devfile for a Dev Environment](devenvironment-devfile-moving.md).

```
new Workspace(this, repository, SampleWorkspaces.default);
```

**To import Amazon CodeCatalyst blueprints workspaces components**

In your `blueprint.ts` file, add the following:

```
import {...} from '@amazon-codecatalyst/codecatalyst-workspaces'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
