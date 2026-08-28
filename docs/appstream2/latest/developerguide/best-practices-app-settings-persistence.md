---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/best-practices-app-settings-persistence.html
---

# Best Practices for Enabling Application Settings Persistence
<a name="best-practices-app-settings-persistence"></a>

To enable application settings persistence without providing internet access to your instances, use a VPC endpoint. This endpoint must be in the VPC to which your WorkSpaces Applications instances are connected. You must attach a custom policy to enable WorkSpaces Applications access to the endpoint. For information about how to create the custom policy, see the *Home Folders and VPC Endpoints* section in [Networking and Access for Amazon WorkSpaces Applications](managing-network.md). For more information about private Amazon S3 endpoints, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) and [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
