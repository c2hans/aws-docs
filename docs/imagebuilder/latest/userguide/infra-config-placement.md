---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/infra-config-placement.html
---

# Instance placement and tenancy
<a name="infra-config-placement"></a>

Use placement settings to control where Image Builder launches your build and test instances. By default, Amazon EC2 instances run on shared tenancy hardware, which means multiple AWS accounts might share the same physical server. You can change the tenancy to run on single-tenant hardware or a Dedicated Host. You can also pin instances to a specific Availability Zone.

For the placement field names, their valid values, and constraints, see [Placement](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Placement.html) in the *EC2 Image Builder API Reference*.

**Note**
Mac instances require a Dedicated Host. Set `tenancy` to `host` for macOS images. If your Dedicated Host has auto-placement enabled and you don't specify a `hostId` or `hostResourceGroupArn`, Amazon EC2 finds an available host for you. For more information, see [Auto-placement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-understanding.html#dedicated-hosts-auto-placement) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
