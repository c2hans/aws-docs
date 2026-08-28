---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-library-updating.html
---

# Updating Library Metadata
<a name="bda-library-updating"></a>

Use the [UpdateDataAutomationLibrary](bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationLibrary.html) API to update the library metadata

```
aws bedrock-data-automation update-data-automation-library \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --library-description "Updated: Medical terminology for healthcare transcription"
```

**Response:**

```
{
  "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
  "status": "ACTIVE"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
