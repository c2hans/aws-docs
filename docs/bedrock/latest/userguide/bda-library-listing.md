---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-library-listing.html
---

# Listing Libraries
<a name="bda-library-listing"></a>

Use the [ListDataAutomationLibraries](bedrock/latest/APIReference/API_data-automation_ListDataAutomationLibraries.html) API to retrieve the list of libraries.

## AWS CLI Example:
<a name="bda-library-listing-cli"></a>

**Request**

```
aws bedrock-data-automation list-data-automation-libraries \
    --max-results 50
```

**Response:**

```
{
  "libraries": [
    {
      "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
      "creationTime": "2026-01-01T00:00:00Z",
      "libraryName": "healthcare-vocabulary"
    }
  ],
  "next_token": "<pagination-token>"
}
```

## AWS Console Example:
<a name="bda-library-listing-console"></a>

1. Navigate to "Manage libraries" page in BDA Console. This page will list libraries associated in this account.

![Libraries table showing healthcare-vocabulary library with Active status and Custom vocabulary entity type.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/bda/library-list-console.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
