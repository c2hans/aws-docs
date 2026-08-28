---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-api.html
---

# API Reference
<a name="managed-entitlements-api"></a>

This section provides comprehensive API documentation for programmatically managing Managed Entitlements for Bedrock. All APIs interact with AWS License Manager in the us-east-1 region.

## API Overview
<a name="managed-entitlements-api-overview"></a>

The following AWS License Manager APIs are used for Managed Entitlements:

| API Operation | Purpose | Common Use Case |
| --- | --- | --- |
| CreateGrant | Create a new grant to distribute licenses | Distribute Bedrock model access to member accounts |
| ListDistributedGrants | List all grants you have created | Track which accounts have been granted access |
| ListReceivedGrants | List all grants received by your account | View licenses available in a member account |
| GetGrant | Get details about a specific grant | Check grant status and configuration |
| CreateGrantVersion | Update grant status (activate/deactivate) | Activate or deactivate a grant |
| AcceptGrant | Accept a received grant | Member account accepts license from management account |
| RejectGrant | Reject a received grant | Member account declines a license |
| DeleteGrant | Permanently delete a grant | Revoke access to a Bedrock model |
| ListReceivedLicenses | List licenses in your account | View all available Bedrock model licenses |
| GetLicense | Get details about a license | Check license status and metadata |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
