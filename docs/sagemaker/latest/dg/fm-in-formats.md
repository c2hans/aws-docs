---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/fm-in-formats.html
---

# Factorization Machines Response Formats
<a name="fm-in-formats"></a>

Amazon SageMaker AI provides several response formats for getting inference from the Factorization Machines model, such as JSON, JSONLINES, and RECORDIO, with specific structures for binary classification and regression tasks.

## JSON Response Format
<a name="fm-json"></a>

Binary classification

```
let response =   {
    "predictions":    [
        {
            "score": 0.4,
            "predicted_label": 0
        }
    ]
}
```

Regression

```
let response =   {
    "predictions":    [
        {
            "score": 0.4
        }
    ]
}
```

## JSONLINES Response Format
<a name="fm-jsonlines"></a>

Binary classification

```
{"score": 0.4, "predicted_label": 0}
```

Regression

```
{"score": 0.4}
```

## RECORDIO Response Format
<a name="fm-recordio"></a>

Binary classification

```
[
    Record = {
        features = {},
        label = {
            'score’: {
                keys: [],
                values: [0.4]  # float32
            },
            'predicted_label': {
                keys: [],
                values: [0.0]  # float32
            }
        }
    }
]
```

Regression

```
[
    Record = {
        features = {},
        label = {
            'score’: {
                keys: [],
                values: [0.4]  # float32
            }
        }
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
