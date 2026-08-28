---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-library-dissociating.html
---

# Dissociation of Library from a Project
<a name="bda-library-dissociating"></a>

You can dissociate a library from a project using the [UpdateDataAutomationProject](bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationProject.html) API.

## AWS CLI Example:
<a name="bda-library-dissociating-cli"></a>

```
aws bedrock-data-automation update-data-automation-project \
    --project-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-project/audio-transcription-project" \
    --data-automation-libraries '[]'
```

## AWS Console Example:
<a name="bda-library-dissociating-console"></a>

1. Navigate to the "Library details" page for your library

1. Expand "Associated projects"

1. Choose the desired project

1. Choose "Dissociate project"

![Associated projects table showing one project named custom-vocab-project with its ID, ARN, and modification date.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/bda/library-dissociate-console.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
