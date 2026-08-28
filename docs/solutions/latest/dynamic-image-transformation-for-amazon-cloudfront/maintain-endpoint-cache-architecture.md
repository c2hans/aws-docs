---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/maintain-endpoint-cache-architecture.html
---

# Maintain existing endpoint and cache when modifying architecture type
<a name="maintain-endpoint-cache-architecture"></a>

With the release of the Object Lambda architecture, customers have the ability to enable an architecture which supports larger images. Modifying an existing distribution to use this architecture will cause a deletion and recreation of the CloudFront distribution associated with the deployment. This will result in a change to the domain name, as well as the cache being cleared. The following workaround can be used to modify the architecture type while avoiding this deletion.

**Note**
This workaround is not officially supported, and may run into instability. This workaround requires that both stacks are maintained in order to maintain functionality. Any updates to the original stack may undo some of the changes performed here. You may experience downtime

1. Follow the process for deploying a new Dynamic Image Transformation for Amazon CloudFront stack. Refer to [deploy the solution](deploy-the-solution.md) for additional guidance on this step.

1. Modify the Enable S3 Object Lambda template parameter to select your desired architecture.

1. Set Use Existing CloudFront Distribution to `Yes`

1. Set Existing CloudFront Distribution Id to the ID of the Image Handler distribution for your existing stack.

1. Set the remaining template parameters to the same values used in the original deployment.

1. Deploy the stack.

1. Upon completion of the deployment, follow the instructions in [Attaching an Existing CloudFront distribution](attaching-existing-distribution.md) to attach the CloudFront distribution referenced to the newly deployed resources. This will require that you overwrite the existing values on the distribution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
