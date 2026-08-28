---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-access-control.html
---

# Cached data access control
<a name="pipelines-access-control"></a>

When a SageMaker AI pipeline runs, it caches the parameters and metadata associated with the SageMaker AI jobs launched by the pipeline and saves them for reuse in subsequent runs. This metadata is accessible through a variety of sources in addition to cached pipeline steps, and includes the following types:
+ `Describe*Job` requests
+ CloudWatch Logs
+ CloudWatch Events
+ CloudWatch Metrics
+ SageMaker AI Search

Note that access to each data source in the list is controlled by its own set of IAM permissions. Removing a particular role’s access to one data source does not affect the level of access to the others. For example, an account admin might remove IAM permissions for `Describe*Job` requests from a caller’s role. While the caller can no longer make `Describe*Job` requests, they can still retrieve the metadata from a pipeline run with cached steps as long as they have permission to run the pipeline. If an account admin wants to remove access to the metadata from a particular SageMaker AI job completely, they need to remove permissions for each of the relevant services that provide access to the data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
