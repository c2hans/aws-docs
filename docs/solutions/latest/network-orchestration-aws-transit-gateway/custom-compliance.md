---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/custom-compliance.html
---

# Custom compliance for network changes
<a name="custom-compliance"></a>

This section provides instructions for custom compliance.

## Add tags to transit gateway route table
<a name="add-tags-to-transit-gateway-route-table"></a>

Each transit gateway route table is tagged with an **ApprovalRequired** tag key with a default value of `No`. You can set the value to:
+  `Yes` to enforce manual approval
+  `Conditional` and add custom rules for compliance

| Key | Value | Description |
| --- | --- | --- |
|  **ApprovalRequired**  |  `No`  | The default value is `No`. This default setting allows any auto-approved or manually approved association and propagation changes. |
|  **ApprovalRequired**  |  `Yes`  | This setting enforces the manually approved workflow for any change in the association and propagation changes. |
|  **ApprovalRequired**  |  `Conditional`  | You can use this setting to automate approving or rejecting requests separately for associations and propagations. You can also optionally define rules based on the requesting account’s OU. |

## Custom compliance rules
<a name="custom-compliance-rules"></a>

Administrators can change from the default automatic approval setup to manual approval by changing the **ApprovalRequired** tag value for every transit gateway route table individually.

See [View transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#view-tgw-route-tables) for instuctions on viewing your transit gateway route tables and updating tags.

The following tag keys and values are required with at least one rule if the **ApprovalRequired** is set to `Conditional`.

| Key | Value | Description |
| --- | --- | --- |
|  **ApprovalRule-Default-Association**  |  `Reject \|Accept \|ApprovalRequired`  | Default approval action for `Associate-with` route tables if none of the custom rules match. Enter `Reject`, `Accept`, or `ApprovalRequired` to match your desired action. |
|  **ApprovalRule-Default-Propagation**  |  `Reject \|Accept \|ApprovalRequired`  | Default approval action for `Propagate-to` route tables if none of the custom rules match. Enter `Reject`, `Accept`, or `ApprovalRequired` to match your desired action. |
|  **ApprovalRule-{{<NN>}}-InOUs \| ApprovalRule-{{<NN>}}-NotInOUs**  |  `Root/OUName1, Root/OUName2`  | A comma-separated list of OU paths starting with `Root/`.<br />If you enter the key with the `InOUs` string, the rule checks if the account is in one of these OUs.<br />If you enter the key with the `NotInOUs` string, the rule checks if the account isn’t in any of the specified OUs.  {{<NN>}} denotes a two-digit number `01-99`. Review [service quotas](quotas.md) for the tags for each resource in your account.  |
|  **ApprovalRule--*<NN>*-Association**  |  `Reject \| Accept \| ApprovalRequired`  | The approval action to take for a VPC that associates with this route table if the `ApprovalRule-{{<NN>}}-InOUs` or `ApprovalRule-{{<NN>}}-NotInOUs` check matches. Enter `Reject`, `Accept`, or `ApprovalRequired` to match your desired action.  {{<NN>}} denotes a two-digit number `01-99`. Review [service quotas](quotas.md) for the tags for each resource in your account.  |
|  **ApprovalRule--{{<NN>}}-Propagation**  |  `Reject \|Accept \|ApprovalRequired`  | The approval action to take for a VPC that propagates to this route table if the `ApprovalRule-{{<NN>}}-InOUs` or `ApprovalRule-{{<NN>}}-NotInOUs` check matches. Enter `Reject`, `Accept`, or `ApprovalRequired` to match your desired action.  {{<NN>}} denotes a two-digit number `01-99`. Review [service quotas](quotas.md) for the tags for each resource in your account.  |

**Note**
If you don’t provide a value for the **ApprovalRule** keys, the default value is ApprovalRequired\_.\_

## Example: Infrastructure route table rules using OU membership
<a name="example-infrastructure-route-table-rules-using-ou-membership"></a>

If your VPCs provide organization-wide shared services, such as Microsoft Active Directory and patching servers, and are limited to AWS accounts in the Infrastructure or Security OU, you can use the following rules to ensure that only VPCs in those OUs associate with the Infrastructure route table without approval. This prevents workload VPCs accidentally associating with the Infrastructure route table, which could inadvertently expose them to the entire organization.

This example also demonstrates how you can prevent VPCs in Sandbox OUs from accessing the organizational shared services. Together, the following rules auto-reject associations or propagations from Sandbox VPCs for the Infrastructure route table.

| Infrastructure Route Table Tag Key | Value |
| --- | --- |
|  **Name**  |  `Infrastructure`  |
|  **ApprovalRequired**  |  `Conditional`  |
|  **ApprovalRule-Default-Association**  |  `ApprovalRequired`  |
|  **ApprovalRule-Default-Propagation**  |  `ApprovalRequired`  |
|  **ApprovalRule-01-InOUs**  |  `Root/Infrastructure/, Root/Security/`  |
|  **ApprovalRule-01-Association**  |  `Accept`  |
|  **ApprovalRule-01-Propagation**  |  `Accept`  |
|  **ApprovalRule-02-InOUs**  |  `Root/Sandbox/`  |
|  **ApprovalRule-02-Association**  |  `Reject`  |
|  **ApprovalRule-02-Propagation**  |  `Reject`  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
