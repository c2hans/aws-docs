---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-library-checking-cv-status.html
---

# Checking Vocabulary Ingestion Job Status
<a name="bda-library-checking-cv-status"></a>

```
aws bedrock-data-automation get-data-automation-library-ingestion-job \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --job-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library-ingestion-job/job-12345"
```

## Job Statuses:
<a name="bda-library-checking-cv-status-statuses"></a>
+ **IN\_PROGRESS:** Job is currently processing
+ **COMPLETED:** All entities processed successfully
+ **COMPLETED\_WITH\_ERRORS:** Some entities failed (check output for details)
+ **FAILED:** Job failed completely

## Understanding Job Output
<a name="bda-library-checking-cv-status-output"></a>

After job completion, check the S3 output location for detailed results.

```
{
  "metadata": {
    "jobId": "job-12345",
    "manifestS3Bucket": "my-bucket",
    "manifestS3Key": "manifests/vocabulary-manifest.json"
  },
  "vocabulary": {
    "successful": [
      {
        "entityId": "medical-en",
        "itemIndex": 0,
        "description": "Medical terms in English language",
        "phrases": [
          {
            "text": "acetaminophen"
          },
          {
            "text": "ibuprofen"
          },
          {
            "text": "naproxen"
          }
        ],
        "language": "EN"
      }
    ],
    "failed": [
      {
        "entityId": "medical-es",
        "itemIndex": 1,
        "errorType": "ValidationError",
        "errorMessage": "Entity validation failed: Missing required creator property 'language'"
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
