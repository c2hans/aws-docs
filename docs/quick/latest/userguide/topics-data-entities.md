---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/topics-data-entities.html
---

# Adding named entities to a Amazon Quick Sight topic dataset
<a name="topics-data-entities"></a>

When asking questions about your topic, your readers might refer to multiple columns of data without stating each column explicitly. For example, they might ask for the address of a transaction. What they actually mean is that they want the branch name, state, and city of where the transaction was made. To support requests like this, you can create a named entity.

A *named entity* is a collection of fields that display together in an answer. For example, using the transaction address example, you can create a named entity called `Address`. You can then add the `Branch Name`, `State`, and `City` columns to it, which already exist in the dataset. When someone asks a question about address, the answer displays the branch, state, and city where a transaction took place.

**To add a named entity to a topic**

1. Open the topic that you want to change.

1. In the topic, choose the **Data** tab.

1. For **Actions**, choose **Add named entity**.

1. In the **Named entity** page that opens, do the following:

   1. For **Dataset**, choose a dataset.

   1. For **Name**, enter a friendly name for the named entity.

   1. For **Description**, enter a description of the named entity.

   1. (Optional) For **Synonyms**, add any alternate names that you think your readers might use to refer to the named entity or the data it contains.

   1. Choose **Add field**, and then choose a field from the list.

      Choose **Add field** again to add another field.

      The ordering of the fields listed here are the order they appear in answers. To move a field, choose the six dots at left of the field name and drag and drop the field to the order that you want.

   1. When finished, choose **Save**.

   The named entity is added to the list of fields in the topic. You can add edit the description for it and add synonyms to it to make it more natural language friendly.
