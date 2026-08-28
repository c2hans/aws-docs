---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-describe-projects.html
---

# Describing projects
<a name="managing-adapters-describe-projects"></a>

You can use the [DescribeProjects](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjects.html) API to get information about your projects, including information about all the adapters associated with a project.

To describe projects with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md) .

1. Use the following code to describe a project:

------
#### [ CLI ]

```
# Request
# Getting CONTENT_MODERATION project details
aws rekognition describe-projects \
    --features CONTENT_MODERATION
    --profile {{profile-name}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
