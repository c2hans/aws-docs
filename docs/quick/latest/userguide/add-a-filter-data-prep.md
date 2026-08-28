---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/add-a-filter-data-prep.html
---

# Adding filters
<a name="add-a-filter-data-prep"></a>

You can add filters to a dataset or an analysis. Use the following procedures to learn how.

## Adding filters to datasets
<a name="add-a-filter-data-prep-datasets"></a>

Use the following procedure to add filters to datasets.

**To add a filter to a dataset**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. From the Quick homepage, choose **Data** at left.

1. In the **Datasets** tab, choose the dataset that you want, and then choose **Edit dataset**.

1. On the data preparation page that opens, choose **Add filter** at lower left, and then choose a field that you want to filter.

   The filter is added to the **Filters** pane.

1. Choose the new filter in the pane to configure the filter. Or you can choose the three dots to the right of the new filter and choose **Edit**.

   Depending on the data type of the field, your options for configuring the filter vary. For more information about the types of filters that you can create and their configurations, see [Filter types in Amazon Quick](filtering-types.md).

1. When finished, choose **Apply**.
**Note**
The data preview shows you the results of your combined filters only as they apply to the first 1,000 rows. If all of the first 1,000 rows are filtered out, then no rows show in the preview. This effect occurs even when rows after the first 1,000 aren't filtered out.

## Adding filters in analyses
<a name="add-a-filter-data-prep-analyses"></a>

Use the following procedure to add filters to analyses.

**To add a filter to an analysis**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. From the Quick homepage, choose **Analyses**.

1. On the **Analyses** page, choose the analysis that you want to work with.

1. In the analysis, choose the **Filter** icon to open the **Filters** pane, and then choose **ADD**.

1. Choose the new filter in the pane to configure it. Or you can choose the three dots to the right of the new filter and choose **Edit**.

1. In the **Edit filter** pane that opens, for **Applied to**, choose one of the following options.
   + **Single visual** – The filter applies to the selected item only.
   + **Single sheet** – The filter applies to a single sheet.
   + **Cross sheet** – The filter applies to multiple sheets in the dataset.

   Depending on the data type of the field, your remaining options for configuring the filter vary. For more information about the types of filters you can create and their configurations, see [Filter types in Amazon Quick](filtering-types.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
