---
source_url: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-access-summary-evaluation-manifest.html
---

# Accessing the summary file and evaluation manifest snapshot (SDK)
<a name="im-access-summary-evaluation-manifest"></a>

To get training results, you call [DescribeProjectVersions](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions). For example code, see [Describing a model (SDK)](md-describing-model-sdk.md).

The location of the metrics is returned in the `ProjectVersionDescription` response from `DescribeProjectVersions`.
+ `EvaluationResult` – The location of the summary file.
+ `TestingDataResult` – The location of the evaluation manifest snapshot used for testing.

The F1 score and summary file location are returned in `EvaluationResult`. For example:

```
"EvaluationResult": {
                "F1Score": 1.0,
                "Summary": {
                    "S3Object": {
                        "Bucket": "echo-dot-scans",
                        "Name": "test-output/EvaluationResultSummary-my-echo-dots-project-v2.json"
                    }
                }
            }
```

The evaluation manifest snapshot is stored in the location specified in the ` --output-config` input parameter that you specified in [Training a model (SDK)](training-model.md#tm-sdk).

**Note**
The amount of time, in seconds, that you are billed for training is returned in `BillableTrainingTimeInSeconds`.

For information about the metrics that are returned by the Amazon Rekognition Custom Labels, see [Accessing Amazon Rekognition Custom Labels evaluation metrics (SDK)](im-metrics-api.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
