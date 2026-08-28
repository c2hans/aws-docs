---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-library-getting-details.html
---

# Getting Library Details
<a name="bda-library-getting-details"></a>

Use the [GetDataAutomationLibrary](bedrock/latest/APIReference/API_data-automation_GetDataAutomationLibrary.html) API to retrieve information about an existing library.

## AWS CLI Example:
<a name="bda-library-getting-details-cli"></a>

**Request**

```
aws bedrock-data-automation get-data-automation-library \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary"
```

**Response:**

```
{
  "library": {
    "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
    "libraryName": "healthcare-vocabulary",
    "libraryDescription": "Medical terminology for transcription accuracy",
    "status": "ACTIVE",
    "creationTime": "2026-01-01T00:00:00Z",
    "entityTypes": [
      {
        "entityType": "VOCABULARY",
        "entityMetadata": "{\"entityCount\": 150}"
      }
    ]
  }
}
```

## AWS Console Example:
<a name="bda-library-getting-details-console"></a>

1. Navigate to "Manage libraries" page in BDA Console

1. Select the desired library from the list of libraries

![Custom vocabulary page showing library details and empty vocabulary lists table.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/bda/library-get-details-console.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
