---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-id-namespace-association.html
---

# Editing ID namespace associations
<a name="edit-id-namespace-association"></a>

As a collaboration member, you can edit the ID namespace associations that you have created.

**To edit an ID namespace association**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Entity resolution** tab.

1. For **Associated ID namespaces**, choose an ID namespace.

1. On the ID namespace details page, scroll down to view the **ID namespace association details**.

1. Choose **Edit**.

1. On the **Edit ID namespace associations** page, edit any of the following:

   1. For **Association details**, update the **Name** or the **Description**.

   1. (Optional) For **Advanced ID mapping table configurations**, modify the default protections for the column that comes from the ID namepsace.

      The ID mapping table is configured by default to only allow an `INNER JOIN` on both the `sourceID` column and the `targetID` column. You can modify this configuration so that the column that comes from this ID namespace (either `sourceID` or `targetID`) can be allowed anywhere in the query.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-id-namespace-association.html)

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
