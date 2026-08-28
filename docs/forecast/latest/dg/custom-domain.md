---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/custom-domain.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# CUSTOM Domain
<a name="custom-domain"></a>

The CUSTOM domain supports the following dataset types. For each dataset type, we list required and optional fields. For information on how to map the fields to columns in your training data, see [Dataset Domains and Dataset Types](howitworks-datasets-groups.md#howitworks-dataset-domainstypes).

**Topics**
+ [Target Time Series Dataset Type](#target-time-series-type-custom-domain)
+ [Related Time Series Dataset Type](#related-time-series-type-custom-domain)
+ [Item Metadata Dataset Type](#item-metadata-type-custom-domain)

## Target Time Series Dataset Type
<a name="target-time-series-type-custom-domain"></a>

The following fields are required:
+ `item_id ` (string)
+ `timestamp` (timestamp)
+ `target_value` (floating-point integer) – This is the `target` field for which Amazon Forecast generates a forecast.

Ideally, only these required fields should be included. Other additional time series information should be included in a related time series dataset.

## Related Time Series Dataset Type
<a name="related-time-series-type-custom-domain"></a>

The following fields are required:
+ `item_id` (string)
+ `timestamp` (timestamp)

In addition to the required fields, your training data can include other fields. To include other fields in the dataset, provide the fields in a schema when you create the dataset.

## Item Metadata Dataset Type
<a name="item-metadata-type-custom-domain"></a>

The following field is required:
+ `item_id` (string)

The following field is optional and might be useful in improving forecast results:
+ `category` (string)

In addition to the required and suggested optional fields, your training data can include other fields. To include other fields in the dataset, provide the fields in a schema when you create the dataset.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
