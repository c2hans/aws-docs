---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/security-traffic-privacy.html
---

# Traffic privacy
<a name="security-traffic-privacy"></a>

You can improve the security of your builds by configuring CodeBuild to use an interface VPC endpoint. To do this, you do not need an internet gateway, NAT device, or virtual private gateway. It also is not required to configure PrivateLink, though it is recommended. For more information, see [Use VPC endpoints](use-vpc-endpoints-with-codebuild.md). For more information about PrivateLink and VPC endpoints, see [AWS PrivateLink](https://aws.amazon.com/privatelink/) and [Accessing AWS services through PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Introduction.html#what-is-privatelink).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
