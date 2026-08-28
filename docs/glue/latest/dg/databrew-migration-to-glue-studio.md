---
source_url: https://docs.aws.amazon.com/glue/latest/dg/databrew-migration-to-glue-studio.html
---

# Migrating from AWS Glue DataBrew to AWS Glue Studio
<a name="databrew-migration-to-glue-studio"></a>

 If you have recipes in AWS Glue DataBrew, use the following checklist to migrate your recipes to AWS Glue Studio.

| If you want to | Then do this |
| --- | --- |
|  Allow users to retrieve AWS Glue DataBrew recipes, recipe versions, and recipe descriptions.  |  Add IAM permissions to a policy that allows your role to access the necessary actions. See [IAM permissions for AWS Glue DataBrew](glue-studio-data-preparation-import-recipe.md#glue-studio-databrew-permissions).  |
|  Import an existing AWS Glue DataBrew recipe into AWS Glue Studio.  |  Follow the steps in [Importing an AWS Glue DataBrew recipe](glue-studio-data-preparation-import-recipe.md#glue-studio-databrew-import-steps).  |
|  Import a recipe with JOIN and UNION.  |  Recipes with UNION and JOIN transforms are not supported. Use the Join and Union transforms in AWS Glue Studio before or after a Data Preparation Recipe node.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
