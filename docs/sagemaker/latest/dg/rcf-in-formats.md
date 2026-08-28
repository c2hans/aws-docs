---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/rcf-in-formats.html
---

# RCF Response Formats
<a name="rcf-in-formats"></a>

All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in [Common Data Formats - Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html). Note that SageMaker AI Random Cut Forest supports both dense and sparse JSON and RecordIO formats. This topic contains a list of the available output formats for the SageMaker AI RCF algorithm.

## JSON Response Format
<a name="RCF-json"></a>

ACCEPT: application/json.

```
    {
        "scores":    [
            {"score": 0.02},
            {"score": 0.25}
        ]
    }
```

### JSONLINES Response Format
<a name="RCF-jsonlines"></a>

ACCEPT: application/jsonlines.

```
{"score": 0.02},
{"score": 0.25}
```

## RECORDIO Response Format
<a name="rcf-recordio"></a>

ACCEPT: application/x-recordio-protobuf.

```
    [
         Record = {
             features = {},
             label = {
                 'score': {
                     keys: [],
                     values: [0.25]  # float32
                 }
             }
         },
         Record = {
             features = {},
             label = {
                 'score': {
                     keys: [],
                     values: [0.23]  # float32
                 }
             }
         }
    ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
