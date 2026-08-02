---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution. This solution includes:
+ A CloudFormation hub template (`aws-transit-network-orchestrator-hub.template`) that you deploy in the [hub account](concepts-and-definitions.md). This template launches all the components necessary to automatically connect your VPCs to Transit Gateway. The template also deploys a web UI. For recommendations on choosing a hub account, refer to [AWS accounts](aws-accounts-for-multi-account-environments.md).
+ A CloudFormation spoke template (`aws-transit-network-orchestrator-spoke.template`) to deploy in your spoke account(s).
+ A CloudFormation organization role template (`aws-transit-network-orchestrator-organization-role.template`) to optionally deploy in your Organizations management account.
