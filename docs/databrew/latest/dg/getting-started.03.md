---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/getting-started.03.html
---

# Step 3: Add more transformations
<a name="getting-started.03"></a>

In this step, you add more transformations to your recipe and publish another version of it. To refine our example, we use the information that not all chess games result in a clear winner; some games are played to a draw.

**To add more recipe transformations and republish**

1. From the transformation toolbar, choose **Filter**, **By Condition**, **Is not** to remove the games that were played to a draw.

1. Set these options as follows:
   + **Source column** - `victory_status`
   + **Filter condition** – Is not `draw`

   To add this transform to your recipe, choose **Apply**.

1. Change the data in `victory_status` so that it's more meaningful. To do this, from the transformation toolbar choose **Clean**, **Replace**, **Replace value or pattern**.

1. Set these options as follows:
   + **Source column** - `victory_status`
   + **Specify values to replace** – Value or pattern
   + **Value to be replaced** - `mate`
   + **Replace with value** - `checkmate`

   To add this transform to your recipe, choose **Apply**.

1. Repeat the previous step, but change `resign` to `other player resigned`.

1. Repeat the previous step, but change `outoftime` to `time ran out`.

1. Choose **Publish** to save your work, at right on the recipe pane.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
