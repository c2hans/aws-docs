---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/ntm-in-formats.html
---

# NTM Response Formats
<a name="ntm-in-formats"></a>

All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in [Common Data Formats - Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html). This topic contains a list of the available output formats for the SageMaker AI NTM algorithm.

## JSON Response Format
<a name="ntm-json"></a>

```
{
    "predictions":    [
        {"topic_weights": [0.02, 0.1, 0,...]},
        {"topic_weights": [0.25, 0.067, 0,...]}
    ]
}
```

## JSONLINES Response Format
<a name="ntm-jsonlines"></a>

```
{"topic_weights": [0.02, 0.1, 0,...]}
{"topic_weights": [0.25, 0.067, 0,...]}
```

## RECORDIO Response Format
<a name="ntm-recordio"></a>

```
[
    Record = {
        features = {},
        label = {
            'topic_weights': {
                keys: [],
                values: [0.25, 0.067, 0, ...]  # float32
            }
        }
    },
    Record = {
        features = {},
        label = {
            'topic_weights': {
                keys: [],
                values: [0.25, 0.067, 0, ...]  # float32
            }
        }
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
