---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-delete.html
---

# Delete a shadow test
<a name="shadow-tests-view-monitor-edit-delete"></a>

 You can delete a test that you no longer need. Deleting your test only deletes the test metadata and not your endpoint, variants, or data captured in Amazon S3. If you want your endpoint to stop running, you must delete your endpoint. For more information about deleting an endpoint, see [Delete Endpoints and Resources](realtime-endpoints-delete-resources.md)

 To delete a test through the console, do the following:

1.  Select the test you want to delete from the **Shadow test** section on the **Shadow tests** page.

1.  From the **Actions** dropdown list, choose **Delete**. The **Delete shadow test** dialog box appears.

1.  In the **To confirm deletion, type *delete* in the field.** text box, enter **delete**.

1.  Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
