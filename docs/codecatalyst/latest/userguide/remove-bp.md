---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/remove-bp.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Removing a custom blueprint from a space blueprints catalog
<a name="remove-bp"></a>

A custom blueprint can be removed from your space's blueprints catalog if you no longer want it being used to create new projects or applied to existing projects.

**Note**
If you remove a custom blueprint from a space's blueprints catalog, it doesn't affect a project created from the blueprint or a project that applied the blueprint. Resources of the blueprint aren't removed from the project.

**Important**
To remove a custom blueprint from your CodeCatalyst space's blueprints catalog, you must be signed in with an account that has the **Space administrator** or **Power user** role in the space.

**To remove a custom blueprint from a space blueprints catalog**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the CodeCatalyst console, navigate to the space dashboard with your custom blueprint

1. On the space dashboard, choose the **Settings** tab, and then choose **Blueprints**.

1. Choose the blueprint name you want to remove, and then choose **Remove blueprint from catalog**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
