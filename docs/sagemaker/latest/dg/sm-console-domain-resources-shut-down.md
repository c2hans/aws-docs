---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sm-console-domain-resources-shut-down.html
---

# Shut down SageMaker AI resources in your domain
<a name="sm-console-domain-resources-shut-down"></a>

You can shut down Amazon SageMaker AI resources in your Amazon SageMaker AI domain using the SageMaker AI console. Use the following instructions to learn how to shut down the resources tagged by the domain ARN.

The displayed SageMaker resources following this procedure are those that have the relevant `sagemaker:domain-arn` tag associated to them. Untagged resources may have been created outside the context of a domain or were created before 11/30/2022, when resources were not automatically tagged with the domain ARN. You can add a tag to untagged resources for better filtration by following the steps in [Backfill domain tags](domain-multiple-backfill.md). Resources created in other domains are automatically filtered out.

**Note**
This is not a complete list of active resources on your domain. For all active SageMaker resources, see [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/).

**To shut down SageMaker AI resources in your domain using the console**

1. [View SageMaker AI resources in your domain](sm-console-domain-resources-view.md)

1. Under a resource type section, check the boxes for the resources you wish to shut down.

1. Once the resources are selected, a shutdown option will become available at the top of the resource type section. Choose the option and follow the instructions to shut down the selected resources.

For instructions on how to delete your resources per SageMaker AI feature, see [Where to shut down resources per SageMaker AI features](sm-shut-down-resources-per-feature.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
