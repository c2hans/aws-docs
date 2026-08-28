---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-delete-with-scaling.html
---

# Delete endpoints configured for auto scaling
<a name="endpoint-delete-with-scaling"></a>

If you delete an endpoint, Application Auto Scaling checks to see whether any of the models on that endpoint are targets for auto scaling. If any are and you have permission to deregister the model, Application Auto Scaling deregisters those models as scalable targets without notifying you. If you use a custom permission policy that doesn't provide permission for the [DeregisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html) action, you must request access to this action before deleting the endpoint.

**Note**
As an IAM user, you might not have sufficient permission to delete an endpoint if another user configured auto scaling for a variant on that endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
