---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-training-data-formats.html
---

# IP Insights Training Data Formats
<a name="ip-insights-training-data-formats"></a>

The following are the available data input formats for the IP Insights algorithm. Amazon SageMaker AI built-in algorithms adhere to the common input training format described in [Common Data Formats for Training](cdf-training.md). However, the SageMaker AI IP Insights algorithm currently supports only the CSV data input format.

## IP Insights Training Data Input Formats
<a name="ip-insights-training-input-format-requests"></a>

### INPUT: CSV
<a name="ip-insights-input-csv"></a>

The CSV file must have two columns. The first column is an opaque string that corresponds to an entity's unique identifier. The second column is the IPv4 address of the entity's access event in decimal-dot notation.

content-type: text/csv

```
entity_id_1, 192.168.1.2
entity_id_2, 10.10.1.2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
