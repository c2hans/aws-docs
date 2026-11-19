---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/implementation-options.html
---

# Implementation Options

This section describes four implementation options, each addressing a different aspect of the operational visibility gap. Option 1 is the primary pattern and should be deployed in all cases. Options 2 through 4 are complementary and should be added based on specific operational requirements.

## Option 1: Cross-Account IAM Role Delegation (Primary)
<a name="option-1--cross-account-iam-role-delegation--primary-.314a13e8-e970-5827-94e2-343325139cde"></a>

Cross-account IAM role delegation is the foundation of this framework. It provides the WSP/ESP with programmatic, read-only access to three categories of Direct Connect telemetry: connection configuration via Describe APIs, performance metrics via CloudWatch, and operational metadata via resource tags. The customer deploys a single CloudFormation stack that creates the IAM policy and the IAM role with its trust policy. Governance validation (for example, tag compliance monitoring) is optional and implemented outside of this stack.

The baseline permissions are organized into six IAM policy statements, each scoped to a specific function. Statement 1 grants directconnect:Describe\* and directconnect:List\* for viewing all DX connections, virtual interfaces, LAGs, and their configuration. Statement 2 grants CloudWatch read permissions (cloudwatch:GetMetricData, cloudwatch:GetMetricStatistics, cloudwatch:ListMetrics) without an IAM namespace condition, because the CloudWatch Service Authorization Reference does not list cloudwatch:namespace as an applicable condition key for these read actions. The monitoring system should scope its queries to the AWS/DX namespace operationally. Statement 3 grants cloudwatch:DescribeAlarms and cloudwatch:DescribeAlarmsForMetric as a separate statement for unrestricted alarm discovery. Statement 4 grants tag:GetResources, tag:GetTagKeys, and tag:GetTagValues without an aws:ResourceTag condition in the IAM policy, because the Resource Groups Tagging API does not support resource-level authorization or service-specific condition keys for tag filtering. Statement 5 grants IAM self-audit permissions (iam:GetRole, iam:GetPolicy, iam:GetPolicyVersion) scoped to the operator role and policy ARNs only. Statement 6 conditionally grants ec2:Describe permissions for VPC and Transit Gateway resources, controlled by CloudFormation parameters.

Tag-based scoping in this framework is implemented as a governance control rather than a resource-level IAM enforcement mechanism. The WSP/ESP monitoring system must include TagFilters in its tag:GetResources API requests to retrieve only resources tagged with DXInfoSharing=enabled. The enforcement of which resources are eligible for sharing is achieved operationally through tagging discipline, periodic audits, and compliance automation — not through IAM resource-level conditions. This is an important distinction that security reviewers should understand when evaluating the framework access model.

Two optional permission sets are exposed as CloudFormation parameters, both disabled by default. EnableVPCAccess adds ec2:Describe permissions for VPCs, VPC peering connections, route tables, VPN connections, VPN gateways, and customer gateways — useful when the WSP/ESP needs VPC routing context for troubleshooting. EnableTGWAccess adds ec2:Describe permissions for Transit Gateways, Transit Gateway attachments, Transit Gateway route tables, and Transit Gateway route searches — useful for customers using Transit Gateway as their DX attachment point.

The primary advantage of this option is breadth: it provides the WSP/ESP with the most complete view of the customer's Direct Connect environment. The primary limitation is that it is polling-based. The WSP/ESP must periodically assume the role and query the APIs to detect changes. For organizations that need real-time push notifications, Option 2 provides a complementary event-driven mechanism.

## Security Considerations for Cross-Account Delegation
<a name="security-considerations-for-cross-account-delegation.6e5ad9f1-86c1-5c97-b6da-7024c42a2fe8"></a>

Cross-account IAM role delegation introduces a trust relationship that must be managed with the same rigor as any privileged access grant. The following considerations apply specifically to this framework.

ExternalId generation and rotation: The ExternalId should be a unique, non-guessable value. A UUID (version 4) is recommended. For guidance on securely using ExternalId for cross-account access, see the IAM User Guide: [https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_third-party.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html). For details on the confused deputy problem that ExternalId is designed to mitigate, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). The ExternalId should be stored in a consistent, retrievable location accessible to the teams managing the trust relationship. The ExternalId should be reviewed periodically and rotated when required by organizational security policy, when the trust relationship changes (for example, WSP/ESP personnel turnover or contract renegotiation), or if compromise is suspected.

Three rotation strategies are supported, each with a distinct tradeoff:

Rotation Option A — Coordinated Rotation (Recommended): The customer updates the ExternalId in the CloudFormation stack and coordinates with the WSP/ESP to update their monitoring configuration. Between the time the customer applies the new ExternalId and the WSP/ESP completes their update, role assumption will fail and telemetry visibility is temporarily impaired. This window can be minimized if the WSP/ESP monitoring system implements retry logic for failed AssumeRole calls, automatically retrying with the new ExternalId value upon receiving an AccessDenied response. This option preserves confused deputy protection throughout the rotation.

Rotation Option B — Remove-then-Rotate (Minimizes Visibility Impairment): The customer temporarily removes the ExternalId condition from the trust policy (switching to Deployment Model B), then coordinates the ExternalId value exchange with the WSP/ESP, and finally re-adds the ExternalId condition with the new value. This eliminates the visibility impairment window because the WSP/ESP can assume the role without an ExternalId during the transition. The tradeoff is that confused deputy protection is not enforced for the duration of the transition period. This option is appropriate only when the WSP/ESP account is fully trusted and the transition window is kept as short as possible.

Rotation C - Create a new role and migrate to the new role. Parallel Role Migration (Recommended for Enterprise Environments): The customer creates a new IAM role (for example, DXNetworkOperatorRole-v2) with the same permissions as the existing role but configured with a new ExternalId value. The customer then provides the new role ARN and ExternalId to the WSP/ESP and allows them to update and validate their monitoring configuration against the new role. During the migration period, both roles remain active, ensuring uninterrupted telemetry visibility while preserving confused deputy protection. Once the WSP/ESP confirms successful operation using the new role, the customer decommissions the original role. This approach avoids both the telemetry visibility impairment associated with coordinated rotation and the temporary reduction in confused deputy protection associated with removing the ExternalId condition. The tradeoff is the temporary management overhead of maintaining two roles during the migration period.

RoleSessionName conventions: Organizations should enforce a naming convention for the RoleSessionName parameter used during sts:AssumeRole calls. A descriptive session name (for example, wsp-monitoring-system or noc-operator-jsmith) enables meaningful CloudTrail analysis. Consider adding a Service Control Policy or IAM condition to require a specific session name prefix.

CloudTrail review cadence: CloudTrail logs for the DXNetworkOperatorRole should be reviewed periodically for anomalous access patterns, such as role assumption from unexpected source IP addresses, unusual API call volumes, or access outside of expected business hours. The review frequency should align with the organization's security operations cadence. Integrate CloudTrail with a SIEM or log analytics platform for automated alerting.

Offboarding procedure: When the WSP/ESP contract is terminated or the business relationship ends, execute the role deletion procedure as part of the contract offboarding process. Review CloudTrail logs for a period preceding termination to identify any anomalous activity. Remove all DXInfoSharing tags from resources. Disable any governance validation mechanisms. Document the revocation date and reason.

Explicit permission boundaries: The framework grants no iam:PassRole, no iam:Create\*, no iam:Update\*, no iam:Delete\*, and no iam:Attach\* permissions. The WSP/ESP cannot modify, escalate, or extend its own access. The IAM self-audit permissions (iam:GetRole, iam:GetPolicy, iam:GetPolicyVersion) are scoped exclusively to the DXNetworkOperatorRole and DXNetworkOperatorPolicy ARNs, preventing enumeration of other IAM resources in the customer's account.

## ExternalId Enforcement and Console Compatibility Considerations
<a name="externalid-enforcement-and-console-compatibility-considerations.61ea4a71-09e7-547d-9702-c0d6dfd09078"></a>

ExternalId is an optional value passed in an sts:AssumeRole request and evaluated by the role trust policy through the sts:ExternalId condition key. In third-party cross-account access scenarios, ExternalId is commonly used to mitigate the confused deputy problem by ensuring that the caller provides the expected customer-specific value when assuming the role.

In the original design, the IAM trust policy for DXNetworkOperatorRole included a Condition block requiring the caller to provide a matching sts:ExternalId value during sts:AssumeRole. This condition aligns with AWS guidance for third-party cross-account access scenarios, as documented in the IAM User Guide.

However, the AWS Management Console Switch Role feature does not support passing an ExternalId parameter when it calls sts:AssumeRole on behalf of the user. As a result, when ExternalId enforcement is enabled in the trust policy, console-based role assumption fails by design. The AWS CLI and AWS SDKs support the --external-id parameter during programmatic role assumption.

ExternalId enforcement is documented as configurable. Organizations may choose to remove the ExternalId condition from the trust policy to enable AWS Console role switching for operational simplicity. This design decision trades confused deputy protection for console compatibility. Removing ExternalId weakens confused deputy protection and should only be adopted when the ESP account is fully trusted, the Principal in the trust policy is tightly scoped, least-privilege permissions are enforced in the attached policy, and monitoring and auditing controls (CloudTrail logging, periodic access reviews) remain in place.

Supported Deployment Models

This framework intentionally supports two deployment models. The choice between them is an architectural decision that must align with organizational security policy and the established trust relationship with the WSP/ESP.

Deployment Model A — ExternalId Enforced (Security-Optimized Mode)
+ Trust policy includes sts:ExternalId condition
+ Mitigates confused deputy attacks
+ Role assumption supported via AWS CLI and AWS SDK only
+ AWS Console Switch Role is not supported
+ Recommended for third-party managed service provider access

Deployment Model B — Console-Compatible Mode (Operational Simplicity Mode)
+ Trust policy does not include sts:ExternalId condition
+ AWS Console Switch Role supported
+ AWS CLI and SDK role assumption supported
+ Confused deputy mitigation depends on tightly scoped Principal, least-privilege IAM policy, and CloudTrail monitoring
+ Appropriate when ESP account is fully trusted and operational simplicity is prioritized

Both deployment models are supported by this framework. Organizations must document which model they adopt as part of their security governance review.

## Trust Policy Modification
<a name="trust-policy-modification.6f07e72e-c320-5685-aa8a-c8fae83e66bf"></a>

Previous trust policy (with ExternalId enforcement):

```
AssumeRolePolicyDocument:
  Version: '2012-10-17'
  Statement:
    - Sid: AllowESPAssumeRole
      Effect: Allow
      Principal:
        AWS: arn:aws:iam::<ESPAccountId>:root
      Action: sts:AssumeRole
      Condition:
        StringEquals:
          sts:ExternalId: <ExternalId-Value>
```

Updated trust policy (without ExternalId enforcement):

```
AssumeRolePolicyDocument:
  Version: '2012-10-17'
  Statement:
    - Sid: AllowESPAssumeRole
      Effect: Allow
      Principal:
        AWS: arn:aws:iam::<ESPAccountId>:root
      Action: sts:AssumeRole
```

With the ExternalId condition removed, console-based Switch Role is supported. CLI and SDK-based role assumption continues to function without change. Confused deputy mitigation via ExternalId is no longer enforced at the IAM layer. Organizations that require ExternalId enforcement should retain the original trust policy and accept that console-based role switching will not be available.

## Role Assumption Validation Methods
<a name="role-assumption-validation-methods.262afd0c-bac7-57cb-8bc8-2d13c1d021ab"></a>

When ExternalId enforcement is enabled, the role must be assumed using the AWS CLI or an AWS SDK. Console-based Switch Role will fail with an AccessDenied error because the Console does not pass the ExternalId parameter. When ExternalId enforcement is removed, both console-based Switch Role and CLI/SDK-based assumption are supported.

CLI example (with ExternalId, when enforcement is enabled):

```
aws sts assume-role \
  --role-arn arn:aws:iam::<AccountId>:role/DXNetworkOperatorRole \
  --role-session-name dx-test \
  --external-id "<ExternalId-Value>"
```

The --external-id parameter is required only when ExternalId enforcement is enabled in the trust policy. When enforcement is removed, the parameter may be omitted.

## Option 2: EventBridge Cross-Account Event Bus
<a name="option-2--eventbridge-cross-account-event-bus.f9536c21-4b41-5f28-a4e7-2f6dc1e27e72"></a>

For organizations that require immediate notification when a Direct Connect connection changes state, Amazon EventBridge provides a cross-account event delivery mechanism. The customer creates an EventBridge rule that matches Direct Connect events (source: aws.directconnect) and forwards them to a target in the WSP/ESP account, such as an SQS queue, Lambda function, or SNS topic.

It is important to understand how Direct Connect events reach EventBridge. Direct Connect events are delivered to Amazon EventBridge via AWS CloudTrail integration. Delivery is best-effort and intended for notification use cases rather than guaranteed real-time telemetry. The events represent API-level activity recorded by CloudTrail rather than instantaneous connection state transitions. CloudWatch metrics remain the authoritative source for circuit health telemetry, including ConnectionState, optical light levels, and throughput. Despite this constraint, EventBridge integration is valuable for detecting configuration changes, BGP session modifications, and maintenance-related API activity.

This option does not replace Option 1. EventBridge events do not include CloudWatch metrics, resource tags, or detailed connection configuration. They provide notification of a change, but the WSP/ESP still needs the IAM role from Option 1 to query the details of what changed.

## Option 3: Synthetic Monitoring via Network Monitor
<a name="option-3--synthetic-monitoring-via-network-monitor.0e1c5749-eb0e-5258-abb2-4ab8905b465f"></a>

Amazon CloudWatch Network Synthetic Monitor is a fully managed service that sends network probes from VPC subnets to on-premises destinations, measuring round-trip time (RTT), packet loss, and a Network Health Indicator (NHI) that isolates whether degradation is within the AWS network or the customer's on-premises network. This fault isolation capability is particularly valuable for Direct Connect troubleshooting, where the root cause may lie in the AWS fabric, the WSP's transport network, or the customer's premises equipment.

For a detailed overview of monitoring hybrid connectivity using CloudWatch Network Synthetic Monitor, see the official AWS blog: [https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/)

CloudWatch Network Synthetic Monitor publishes its metrics to CloudWatch under the AWS/NetworkMonitor namespace. To share these metrics with the WSP/ESP, the monitoring system should include the AWS/NetworkMonitor namespace in its CloudWatch queries alongside AWS/DX. CloudWatch Network Synthetic Monitor does not support cross-account resource creation and does not have a native sharing feature. The only way to share its metrics with a third party is through cross-account IAM role delegation. Verify CloudWatch Network Synthetic Monitor availability in your destination partition(s) before incorporating in your design.

## Option 4: AWS Health Event Integration
<a name="option-4--aws-health-event-integration.e591c322-3f88-5eec-8132-0367b81adca3"></a>

AWS Health provides events for Direct Connect service issues that originate on the AWS side: planned maintenance windows, service degradations, and infrastructure outages. These events represent AWS's perspective on the health of the Direct Connect infrastructure and complement the customer-side metrics available through Option 1.

The customer creates an EventBridge rule matching source aws.health with detail-type AWS Health Event and forwards matching events to the WSP/ESP account. This gives the WSP/ESP advance notice of planned maintenance and real-time awareness of AWS-side issues, enabling them to correlate customer-reported problems with known AWS events.
