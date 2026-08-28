---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/km-in-formats.html
---

# K-Means Response Formats
<a name="km-in-formats"></a>

All SageMaker AI built-in algorithms adhere to the common input inference format described in [Common Data Formats - Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html). This topic contains a list of the available output formats for the SageMaker AI k-means algorithm.

## JSON Response Format
<a name="km-json"></a>

```
{
    "predictions": [
        {
            "closest_cluster": 1.0,
            "distance_to_cluster": 3.0,
        },
        {
            "closest_cluster": 2.0,
            "distance_to_cluster": 5.0,
        },

        ....
    ]
}
```

## JSONLINES Response Format
<a name="km-jsonlines"></a>

```
{"closest_cluster": 1.0, "distance_to_cluster": 3.0}
{"closest_cluster": 2.0, "distance_to_cluster": 5.0}
```

## RECORDIO Response Format
<a name="km-recordio"></a>

```
[
    Record = {
        features = {},
        label = {
            'closest_cluster': {
                keys: [],
                values: [1.0, 2.0]  # float32
            },
            'distance_to_cluster': {
                keys: [],
                values: [3.0, 5.0]  # float32
            },
        }
    }
]
```

## CSV Response Format
<a name="km-csv"></a>

The first value in each line corresponds to `closest_cluster`.

The second value in each line corresponds to `distance_to_cluster`.

```
1.0,3.0
2.0,5.0
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
