---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/mlopsfaq.html
---

# Amazon SageMaker AI MLOps troubleshooting
<a name="mlopsfaq"></a>

Use the following to troubleshoot issues with MLOps in SageMaker AI. This topic provides information about common errors and how to resolve them.

## If I try to delete a SageMaker AI project created from a SageMaker AI template and receive an error due to non-empty Amazon S3 buckets or Amazon ECR repositories, how can I delete the project?
<a name="collapsible-section-14"></a>

If you try to delete your SageMaker AI project and get one of the following error messages:

```
The bucket you tried to delete is not empty
```

```
The repository with name '{{repository-name}}' in registry
        with id '{{id}}' cannot be deleted because it still contains images
```

then you have non-empty Amazon S3 buckets or Amazon ECR repositories which you need to manually delete before you delete the SageMaker AI project. CloudFormation does not automatically delete non-empty Amazon S3 buckets or Amazon ECR repositories for you.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
