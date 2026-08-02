---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/topics-data-calculated-fields.html
---

# Adding calculated fields to a Amazon Quick Sight topic dataset
<a name="topics-data-calculated-fields"></a>

You can create new fields in a topic by creating calculated fields. *Calculated fields* are fields that use a combination of one or two fields from a dataset with a supported function to create new data.

For example, if your dataset contains columns for sales and expenses, you can combine them in a calculated field with a simple function to create a profit column. The function might look like the following: `sum({Sales}) - sum({Expenses})`.

**To add a calculated field to a topic**

1. Open the topic that you want to change.

1. In the topic, choose the **Data** tab.

1. For **Actions**, choose **Add calculated field**.

1. In the calculations editor that opens, do the following:

   1. Give the calculated field a friendly name.

   1. For **Datasets** at right, choose a dataset that you want to use for the calculated field.

   1. Enter a calculation in the calculation editor at left.

      You can see a list of fields in the dataset in the **Fields** pane at right. You can also see a list of supported functions in the **Functions** pane at right.

      For more information about the functions and operators you can use to create calculations in Quick Sight, see the [Calculated field function and operator reference for Amazon QuickFunctions and operators](calculated-field-reference.md).

1. When finished, choose **Save**.

   The calculated field is added to the list of fields in the topic. You can add a description to it and configure metadata for it to make it more natural language friendly.
