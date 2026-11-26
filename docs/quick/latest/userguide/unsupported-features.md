---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/unsupported-features.html
---

# Expanded feature support in the data preparation experience

Starting in November 2026, Quick Sight brings most of the previously missing legacy features to the data preparation experience, so it now supports most of the capabilities from the legacy experience. You can now use more of your existing workflows alongside visual transformations and an upgraded data processing engine. The data preparation experience also includes capabilities that help make your datasets AI ready.

## Editing an existing dataset
<a name="editing-existing-dataset"></a>

When you choose **Edit dataset** for a supported legacy dataset, Quick Sight automatically opens it in the data preparation experience. Your existing data sources, joins, transformations, and calculated fields carry over, so you don't need to recreate the dataset or perform a separate upgrade. You can continue to prepare your data and use the additional capabilities in the data preparation experience.

**Note**
[Dataset parameters](dataset-parameters.md) are not yet supported in the data preparation experience. Continue to use the legacy data preparation experience for workflows that require dataset parameters. We plan to support dataset parameters.

## Feature support at a glance
<a name="feature-support-glance"></a>

Quick Sight now supports more legacy capabilities in the data preparation experience. The following table describes these capabilities and identifies the remaining file-related limitations.

| Category | Feature | Details |
| --- | --- | --- |
| Data sources | Salesforce | Now supported. Create and prepare Salesforce datasets in the data preparation experience. |
| Data sources | Google Sheets | Now supported. Create datasets from Google Sheets tabs and prepare them in the data preparation experience. |
| Dataset management | Column folders | Now supported. Organize columns into folders so that authors and readers can find fields faster. |
| Dataset management | Column descriptions | Now supported. Add descriptions to columns to help users understand each field and give AI features in Quick Sight business context. |
| Geospatial | Geospatial data type | Now supported. Set a geospatial type, such as Country, State, City, Postcode, Latitude, or Longitude, on the **Output** tab. |
| Geospatial | Geo hierarchy | Not yet supported. Continue to use the legacy data preparation experience to create a geo hierarchy. |
| Calculated fields | Unmaterialized calculated columns (UMCC) | Supported only for datasets that you upgrade from the legacy experience. When you edit a legacy dataset in the data preparation experience, existing unmaterialized calculated columns carry over. You can't create new unmaterialized calculated columns in the data preparation experience. To add new calculations, use the analysis page. |
| Parent datasets | Legacy SPICE and Direct Query datasets as parents | Now supported. Use a legacy SPICE or Direct Query dataset as the parent of a dataset in the data preparation experience. |

## Capabilities available in the new experience
<a name="new-experience-capabilities"></a>

In addition to the preceding features, the data preparation experience includes the following capabilities.

Dataset semantics
Add business context to a dataset, such as a dataset description, column descriptions, and custom instructions. This context grounds Quick Sight AI answers in your own definitions.

Topics and semantic models
Build topics and semantic models from your datasets to define business terms, metrics, and relationships once and reuse them across questions.

Dataset evaluation
Measure the accuracy of AI answers on a dataset before and after you add semantics, and get recommended semantics that improve accuracy.

Visual transformations
Build step-by-step visual workflows, including Append, Aggregate, Pivot, and Divergence.

Upgraded data processing engine
Prepare and ingest data with an upgraded processing engine for faster ingestion and up to 20 times higher cross-source join limits.

## Setting the geospatial type
<a name="setting-geospatial-type"></a>

**Note**
You set the geospatial type on the **Output** tab, not through **Change data type** on the **Transform** tab. Geospatial types, such as latitude and longitude, aren't part of the regular data types. Because Quick Sight doesn't apply further transformations to these columns, it places them on the **Output** tab.

To set the geospatial type of a column

1. On the data preparation page, choose the **Output** tab at the top, next to **Transform**.

1. In the **Schema** pane on the left, choose the column that you want to set, for example, **City**.

1. Open the **Geospatial type** dropdown and choose a value, such as **Country**, **State**, **County**, **City**, **Postcode**, **Latitude**, or **Longitude**. To clear the geospatial type, choose **Unspecified**.

**Note**
For now, you can switch to the legacy data preparation experience from the user interface. However, we plan to deprecate the legacy experience soon, so we recommend that you prepare your data in the data preparation experience.
