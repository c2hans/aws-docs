---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/creating-a-review-template.html
---

# Creating a review template in AWS WA Tool
<a name="creating-a-review-template"></a>

**To create a review template**

1. Select **Review templates** in the left navigation pane.

1. Choose **Create template**.

1. On the **Specify template details** page, provide a **Name** and **Description** for your review template.

1. (Optional) In the **Template notes** and **Tags** sections, add any template notes or tags you want to associate with the review template. Any notes added are applied to all workloads that use the review template, whereas tags are specific to the review template.

   For more information on tags, see [Tagging your AWS WA Tool resources](tagging.md).

1. Choose **Next**.

1. On the **Apply lenses** page, select the lenses that you want to apply to the review template. The maximum number of lenses that can be applied is 20.

    Lenses can be selected from **Custom lenses**, **Lens Catalog**, or both.
**Note**
Lenses that are shared with you cannot be applied to the review template.

1. Choose **Create template**.

**To begin answering questions for the review template you just created**

1. On the template **Overview** tab, in the **Start answering questions** information alert, select the lens in the **Answer questions** dropdown.
**Note**
You can also go to the **Lenses** section, select the lens, and choose **Answer questions**.

1. For each lens you have applied to your review template, answer the applicable questions and choose **Save and exit** when done.

Once your review template is created, you can define a new workload from it.

The **Overview** tab of the review template should reflect the total number of **Questions answered** in the **Template details** section, and the **Questions answered** for each lens in the **Lenses** section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
