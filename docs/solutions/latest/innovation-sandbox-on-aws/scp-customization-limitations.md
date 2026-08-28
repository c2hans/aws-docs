---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/scp-customization-limitations.html
---

# SCP customization limitations
<a name="scp-customization-limitations"></a>

The following limitations apply when using the AccountPool stack’s SCP customization parameters (`AdditionalAllowedServices`, `AdditionalPrincipalExceptions`, and `BedrockInferenceProfilePatterns`).

## Additive changes only
<a name="additive-changes-only"></a>

The CloudFormation parameters only support appending services or principal ARN patterns to existing SCP statements. You cannot use these parameters to remove solution-managed actions, modify existing conditions, or add entirely new SCP statements. If your use case requires changes beyond what the parameters support, open a feature request in the [GitHub repository](https://github.com/aws-solutions/innovation-sandbox-on-aws).

## Manual cleanup required for services not supported by AWS Nuke
<a name="manual-cleanup-required-for-services-not-supported-by-aws-nuke"></a>

Adding a service to the allowed services list by using the `AdditionalAllowedServices` parameter does not automatically add cleanup support for that service. If a sandbox user creates resources in a service that AWS Nuke does not support, the solution will not automatically clean up those resources at the end of the lease. You must manually remove any such resources before the account can be returned to the pool. For the full list of services allowed by default, refer to [Allowed services in sandbox accounts](allowed-services-reference.md).

## SCP size limit constrains customization
<a name="scp-size-limit-constrains-customization"></a>

Each SCP has a maximum size of 10,240 characters (minified). The entries you add consume space from this budget. If the merged policy exceeds the limit, the AccountPool stack update fails.

## Direct SCP edits in the AWS Organizations console are overwritten
<a name="direct-scp-edits-in-the-aws-organizations-console-are-overwritten"></a>

The solution manages all SCP content through CloudFormation. Any modifications made directly in the AWS Organizations console will be overwritten the next time the AccountPool stack is updated. Always use the CloudFormation parameters to apply and preserve SCP customizations. For instructions on migrating existing console edits, refer to [Migrating existing SCP customizations](update-the-solution.md#v1-3-0-scp-migration).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
