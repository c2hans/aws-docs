---
source_url: https://docs.aws.amazon.com/athena/latest/ug/saved-queries.html
---

# Use saved queries
<a name="saved-queries"></a>

You can use the Athena console to save, edit, run, rename, and delete the queries that you create in the query editor.

## Considerations and limitations
<a name="saved-queries-considerations-and-limitations"></a>
+ You can update the name, description, and query text of saved queries.
+ You can only update the queries in your own account.
+ You cannot change the workgroup or database to which the query belongs.
+ Athena does not keep a history of query modifications. If you want to keep a particular version of a query, save it with a different name.

**Note**
Amazon Athena resources can now be accessed within Amazon SageMaker Unified Studio (Preview), which helps you access your organization's data and act on it with the best tools. You can migrate saved queries from an Athena workgroup to a SageMaker Unified Studio project, configure projects with existing Athena workgroups, and maintain necessary permissions through IAM role updates. For more information, see [Migrating Amazon Athena resources to Amazon SageMaker Unified Studio (Preview)](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena).

**Topics**
+ [Considerations and limitations](#saved-queries-considerations-and-limitations)
+ [Save a query with a name](saved-queries-name.md)
+ [Run a saved query](saved-queries-run.md)
+ [Edit a saved query](saved-queries-edit.md)
+ [Rename or delete a saved query](saved-queries-rename-or-delete.md)
+ [Rename an undisplayed saved query](saved-queries-rename-not-displayed.md)
+ [Delete an undisplayed saved query](saved-queries-delete-not-displayed.md)
+ [Use the Athena API to update saved queries](saved-queries-update-with-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
