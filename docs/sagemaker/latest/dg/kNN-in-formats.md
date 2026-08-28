---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/kNN-in-formats.html
---

# Data Formats for k-NN Training Input
<a name="kNN-in-formats"></a>

All Amazon SageMaker AI built-in algorithms adhere to the common input training formats described in [Common Data Formats - Training](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html). This topic contains a list of the available input formats for the SageMaker AI k-nearest-neighbor algorithm.

## CSV Data Format
<a name="kNN-training-data-csv"></a>

content-type: text/csv; label\_size=1

```
4,1.2,1.3,9.6,20.3
```

The first `label_size` columns are interpreted as the label vector for that row.

## RECORDIO Data Format
<a name="kNN-training-data-recordio"></a>

content-type: application/x-recordio-protobuf

```
[
    Record = {
        features = {
            'values': {
                values: [1.2, 1.3, 9.6, 20.3]  # float32
            }
        },
        label = {
            'values': {
                values: [4]  # float32
            }
        }
    }
]

}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
