---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-CFront.html
---

# Requirements for Amazon CloudFront
<a name="requirements-for-CFront"></a>

MediaLive includes a workflow wizard. One of the options in the wizard is to deliver output to AWS Elemental MediaPackage and from there to Amazon CloudFront. Therefore, for users to create a workflow with delivery to MediaPackage, users need permissions in CloudFront.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| Use the workflow wizard to create the CloudFront distribution that is associated with a MediaPackage channel, if your organization supports MediaPackage as an output destination.Use the workflow wizard to delete a workflow that includes a CloudFront distribution. | CloudFront | `ListDistributions`<br />`DescribeDistribution`<br />`CreateDistribution`<br />`DeleteDistribution`  |

CloudFrontCreate and delete a CloudFront distribution, if your organization supports MediaPackage as an output destination.

Note how the required permissions here are very different from the permissions because the workflow wizard actually creates the distribution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
