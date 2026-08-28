---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-workflow.html
---

# Workflow overview
<a name="managed-entitlements-workflow"></a>

**Step 1 - Subscribe**: Subscribe to a third-party Bedrock serverless model through AWS Marketplace (either through auto-enablement or private offer).

**Step 2 - License creation**: A license is automatically generated in us-east-1, representing your entitlement. You can view this license in the License Manager console under Granted Licenses.

**Steps 3 - Create and distribute grants**: Create grants to distribute the license. Grants can target individual AWS account IDs, your entire organization ID, or specific organizational units (OUs).
+ Individual AWS account IDs - grant appears in recipient's License Manager console
+ Organization ID - grants automatically distributed to all member accounts
+ Organizational units (OUs) - grants distributed to all accounts in the OU

**Step 4 - Activate**: Grants must be activated before the model can be used:
+ Individual grants: Recipient accepts and activates their own grant
+ Organization/OU grants: Management account can bulk-activate all grants, or recipients activate individually

**Step 5 - Use the model**: After activation, you can invoke the model in your entitled account using the Amazon Bedrock console, AWS CLI, or AWS SDKs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
