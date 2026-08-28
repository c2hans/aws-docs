---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-describe-project.html
---

# Describing a project version
<a name="managing-adapters-describe-project"></a>

You can list and describe adapters associated with a project by using the [DescribeProjectVersions](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions.html) operation. You can specify up to 10 model versions in ProjectVersionArns. If you don't specify a value, descriptions for all model versions in the project are returned.

To describe a project version with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md) .

1. Use the following code to describe a project version:

------
#### [ CLI ]

```
aws rekognition describe-project-versions
  --project-arn {{project_arn}} \
  --version-names {{[versions]}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
