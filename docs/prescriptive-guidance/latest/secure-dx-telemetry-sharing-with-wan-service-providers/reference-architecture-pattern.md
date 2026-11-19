---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/reference-architecture-pattern.html
---

# Reference Architecture Pattern

The reference architecture is intentionally simple. It consists of two AWS accounts — the customer account and the WSP/ESP account — connected by a single IAM trust relationship. This simplicity is a design choice: the fewer moving parts in a cross-account access pattern, the easier it is to audit, maintain, and revoke.

In the customer account, the framework deploys two categories of resources. First, an IAM managed policy (DXNetworkOperatorPolicy) that defines the read-only permissions. Second, an IAM role (DXNetworkOperatorRole) with a trust policy that allows the WSP/ESP account to assume it, conditioned on the correct ExternalId. Governance validation is optional and is implemented outside of this stack. Customers may use AWS Config (where supported) with custom rules, or alternative compliance validation mechanisms (for example, scheduled audits), to verify tag integrity and adherence to governance policy.

In the WSP/ESP account, no resources are deployed by this framework. The WSP/ESP's monitoring system simply calls sts:AssumeRole with the customer's Role ARN and the pre-shared ExternalId. AWS STS validates the trust policy, confirms the ExternalId, and returns temporary credentials. The WSP/ESP then uses these credentials to call Direct Connect Describe APIs, CloudWatch GetMetricData (scoping queries to the AWS/DX namespace operationally), and the Resource Groups Tagging API (applying TagFilters for DXInfoSharing=enabled).

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/images/guide-img/a27cfbe8-ee56-4f7e-8dbe-badf176580a2/images/d3ccc217-8a78-4ba3-9b89-343f3a8fbeba.png)

## Figure 1: Reference Architecture — Cross-Account IAM Role Delegation (v6)
<a name="figure-1--reference-architecture---cross-account-iam-role-delegation--v6-.4828fd71-037b-57e1-946b-a487601494df"></a>

The sequence of operations proceeds as follows. The WSP/ESP monitoring system initiates the flow by calling sts:AssumeRole. STS validates the trust policy and returns temporary credentials valid for up to one hour. The WSP/ESP uses these credentials to call directconnect:DescribeConnections and directconnect:DescribeVirtualInterfaces to retrieve connection configuration. It calls cloudwatch:GetMetricData, scoping its queries to the AWS/DX namespace, to retrieve performance metrics such as ConnectionState, ConnectionBpsEgress, ConnectionBpsIngress, ConnectionLightLevelTx, and ConnectionLightLevelRx. It calls tag:GetResources with the TagFilters parameter specifying DXInfoSharing=enabled to retrieve operational metadata including contacts, circuit identifiers, and maintenance windows. The tag filter is applied at the API request level by the WSP/ESP's monitoring system, not enforced by IAM conditions. Each of these API calls is logged in the customer's CloudTrail, providing a complete and immutable audit record.

*Note: An important technical clarification: Direct Connect Describe APIs (DescribeConnections, DescribeVirtualInterfaces) do not support tag-based filtering. These APIs return all connections and virtual interfaces in the account regardless of tags. The DXInfoSharing=enabled tag controls visibility of operational metadata through the Resource Groups Tagging API (tag:GetResources), not through the describe APIs themselves. This means the WSP/ESP can see connection IDs and state for all connections in the account, but can only retrieve POC contacts, circuit details, and other operational metadata for resources that the customer has explicitly tagged for sharing. This distinction is important for customers who want to understand exactly what information the WSP/ESP can access.*
