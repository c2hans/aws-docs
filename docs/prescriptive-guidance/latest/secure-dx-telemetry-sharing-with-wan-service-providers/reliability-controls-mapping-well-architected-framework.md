---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/reliability-controls-mapping-well-architected-framework.html
---

# Reliability Controls Mapping (Well-Architected Framework)

The AWS Well-Architected Framework Reliability Pillar focuses on the ability of a workload to perform its intended function correctly and consistently. For Direct Connect, reliability is achieved through redundant connections deployed according to one of three resiliency models defined by the AWS Direct Connect Resiliency Toolkit. This framework enhances reliability by providing the WSP/ESP with visibility into the customer's entire resiliency topology.

## Direct Connect Resiliency Models Overview
<a name="direct-connect-resiliency-models-overview.0e46cb1e-1a0b-59c7-ad33-ef9b7ee5b242"></a>

The AWS Direct Connect Resiliency Toolkit defines three deployment models that provide increasing levels of redundancy. These models are documented in the AWS Direct Connect User Guide and align with the Well-Architected Reliability Pillar best practice REL02-BP02 (Provision redundant connectivity between private networks in the cloud and on-premises environments). Understanding which model a customer has deployed is essential for the WSP/ESP to accurately assess the impact of a connection failure.

The Maximum Resiliency model provides the highest level of protection. It requires separate connections terminating on separate devices in more than one AWS Direct Connect location. A typical deployment includes four or more connections distributed across at least two geographically distinct locations. This topology protects against device failure, fiber cut, and complete location failure. If one location becomes unavailable, traffic fails over to connections at the other location. AWS recommends this model for mission-critical production workloads.

The High Resiliency model provides protection against connectivity failure and helps prevent complete location failure. It uses two single connections, each terminating at a different AWS Direct Connect location. This topology protects against fiber cuts and device failures at a single location. It does not provide the same level of device-level redundancy within each location as the Maximum Resiliency model, but it does ensure that a complete location outage does not result in total loss of connectivity.

The Development and Test model provides redundancy within a single location. It uses separate connections terminating on separate devices at one AWS Direct Connect location. This topology protects against individual device failure but does not protect against a complete location failure. AWS recommends this model for non-critical workloads where the cost of multi-location redundancy is not justified.

When a WSP/ESP has visibility into the customer's deployed resiliency model, it can make informed decisions during an incident. For example, if a connection in a Maximum Resiliency topology fails, the WSP/ESP can verify that redundant connections at the alternate location are healthy before escalating. Conversely, if a connection in a Development and Test topology fails, the WSP/ESP knows there is no geographic redundancy and can prioritize restoration accordingly. This topology awareness directly reduces mean time to recovery by eliminating the need for the WSP/ESP to request topology information from the customer during an incident.

This framework does not create, enforce, or validate the customer's resiliency topology. It provides the WSP/ESP with visibility into the connections and virtual interfaces that the customer has tagged for sharing. Customers are responsible for deploying their Direct Connect connections according to the resiliency model appropriate for their workload requirements.

|
|
| Best Practice | Framework Implementation |
| --- |--- |
| REL02-BP02 Provision redundant connectivity | Framework monitors all connections across Maximum Resiliency (4\+ connections, 2\+ locations), High Resiliency (2\+ connections, 2\+ locations), and Dev/Test topologies. |
| REL06-BP01 Monitor all components of the workload | CloudWatch metrics (ConnectionState, BPS, LightLevel) provide real-time health visibility to both customer and WSP/ESP. |
| REL06-BP04 Automate responses | EventBridge integration (Option 2) enables automated alerting on DX state changes, triggering WSP/ESP incident workflows. |
| REL10-BP01 Deploy the workload to multiple locations | Partition-independent design supports deployment across all AWS Partitions. |

The connection between this framework and REL02-BP02 deserves emphasis. AWS recommends that customers deploy Direct Connect using the Maximum Resiliency model for critical workloads, which requires separate connections terminating on separate devices in more than one location. When customers tag all connections in their resiliency topology with DXInfoSharing=enabled, the WSP/ESP gains visibility into the complete redundancy model. This enables the WSP/ESP to assess the impact of a single connection failure in the context of the overall topology — for example, determining whether a failed connection in one location is covered by a redundant connection in another location, or whether the failure represents a single point of failure that requires immediate escalation.
