---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/appendix-a---partitional-service-guidance.html
---

# Appendix A - Partitional service guidance
<a name="appendix-a---partitional-service-guidance"></a>

 For partitional services, you should implement static stability in order to maintain resilience of your workload during an AWS service control plane impairment. The following provides prescriptive guidance on how to consider dependencies on partitional services as well as what will and may not work during a control plane impairment.

## AWS Identity and Access Management (IAM)
<a name="aws-iam"></a>

 The AWS Identity and Access Management (IAM) control plane consists of all public IAM APIs (including Access Advisor but not Access Analyzer or IAM Roles Anywhere). This includes actions like `CreateRole`, `AttachRolePolicy`, `ChangePassword`, `UpdateSAMLProvider`, and `UpdateLoginProfile`. The IAM data plane provides authentication and authorization for IAM principals in each AWS Region. During a control plane impairment, CRUDL type operations for IAM may not work, but authentication and authorization for existing principals will continue to work. STS is a data plane-only service that is separate from IAM, and does not depend on the IAM control plane.

 What this means is that when you are planning for dependencies on IAM, you should not rely on the IAM control plane in your recovery path. For example, a statically-stable design for a “break-glass” admin user would be to create a user with the appropriate permissions attached, have the password set and the access key and secret access key provisioned, and then lock those credentials in a physical or virtual vault. When required during an emergency, retrieve the user credentials from the vault and use them as needed. A non-statically-stable design would be to provision the user during a failure, or having the user pre-provisioned, but only attaching the admin policy when required. These approaches would depend on the IAM control plane.

## AWS Organizations
<a name="aws-organizations"></a>

 The AWS Organizations control plane consists of all public Organizations APIs like `AcceptHandshake`, `AttachPolicy`, `CreateAccount`, `CreatePolicy`, and `ListAccounts`. There is not a data plane for AWS Organizations. It orchestrates the data plane for other services like IAM. During a control plane impairment, CRUDL type operations for Organizations may not work, but the policies, like Service Control Policies (SCP) and Tag Policies, will continue to work and be evaluated as part of the IAM authorization process. Delegated admin capabilities and multi-account features in other AWS services that are supported by Organizations will also continue to work.

 What this means is that when you are planning for dependencies on AWS Organizations, you should not rely on the Organizations control plane in your recovery path. Instead, implement static stability in your recovery plan. For example, a non-statically-stable approach might be to update SCPs to remove restrictions on allowed AWS Regions via the `aws:RequestedRegion` condition, or to enable admin permissions for specific IAM roles. This relies on the Organizations control plane to make these updates. A better approach would be to use [session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) to grant the use of admin permissions. Your Identity Provider (IdP) can include session tags that can be evaluated against the `aws:PrincipalTag` condition, which helps you to dynamically configure permissions for certain principals while helping your SCPs to remain static. This removes dependencies on control planes and only utilizes data plane actions.

## AWS Account Management
<a name="aws-account-management"></a>

 The AWS Account Management control plane is hosted in us-east-1 and consists of all [public APIs](https://docs.aws.amazon.com/accounts/latest/reference/api-reference.html) for managing an AWS account, such as `GetContactInformation` and `PutContactInformation`. It also includes creating or closing a new AWS account through the management console. The APIs for `CloseAccount`, `CreateAccount`, `CreateGovCloudAccount`, and `DescribeAccount` are part of the AWS Organizations control plane, which is also hosted in us-east-1. Additionally, [creating a GovCloud account outside of AWS Organizations](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html) relies on the AWS account management control plane in us-east-1. Also, GovCloud accounts [must be 1:1 linked](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html) to an AWS account in the `aws` partition. Creating accounts in the `aws-cn` partition does not rely on us-east-1. The data plane for AWS accounts is the accounts themselves. During a control plane impairment, CRUDL-type operations (like creating a new account or getting and updating contact information) for AWS accounts may not work. References to the account in IAM policies will continue to work.

 What this means is that when you are planning for dependencies on AWS Account Management, you should not rely on the Account Management control plane in your recovery path. Although the Account Management control plane doesn’t provide direct functionality that you would typically use in a recovery situation, there may be times when you would. For example, a statically-stable design would be to pre-provision all of the AWS accounts you need for failover. A non-statically-stable design would be to create new AWS accounts during a failure event to host your DR resources.

## Route 53 Application Recovery Controller
<a name="route-53-application-recovery-controller"></a>

 The control plane for Route 53 ARC consists of the APIs for recovery control and recovery readiness, as identified at: [Amazon Route 53 Application Recovery Controller endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html). You manage readiness checks, routing controls, and cluster operations by using the control plane. The data plane of ARC is your recovery cluster, which manages the routing control values that are queried by Route 53 health checks, and also implements the safety rules. The [data plane functionality](https://docs.aws.amazon.com/routing-control/latest/APIReference/Welcome.html) of Route 53 ARC is accessed through your recovery cluster APIs like `https://aaaaaaaa.route53-recovery-cluster.eu-west-1.amazonaws.com`.

 What this means is that you shouldn’t rely on the Route 53 ARC control plane in your recovery path. There are two [best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html) that help implement this guidance:
+  First, bookmark or hard code the five Regional cluster endpoints. This removes the need to use the DescribeCluster control plane operation during a failover scenario to discover the endpoint values.
+  Second, use the Route 53 ARC cluster APIs by using the CLI or SDK to perform updates to routing controls and not the AWS Management Console. This removes the management console as a dependency for your failover plan and ensures it depends on only data plane actions.

## AWS Network Manager
<a name="aws-network-manager"></a>

 The AWS Network Manager service is primarily a control plane-only system hosted in us-west-2. Its purpose is to centrally manage the configuration of your AWS Cloud wide area networking (WAN) core network and your AWS Transit Gateway network across AWS accounts, Regions, and on-premises locations. It also aggregates your Cloud WAN metrics in us-west-2, which can also be accessed through the CloudWatch data plane. If Network Manager is impaired, the data plane of the services it orchestrates will not be impacted. The CloudWatch metrics for Cloud WAN are also available in us-west-2. If you want historical metric data, like bytes in and out per Region, to understand how much traffic might shift to other Regions during a failure impacting us-west-2, or for other operational purposes, you can export those metrics as CSV data directly from the CloudWatch console or using this method: [Publish Amazon CloudWatch metrics to a CSV file](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/publish-amazon-cloudwatch-metrics-to-a-csv-file.html). The data can be found under the `AWS/Network Manager` namespace and you can perform this on a schedule you choose and store it in S3 or in another data store you select. To implement a statically-stable recovery plan, do not use AWS Network Manager to make updates to your network, or rely on data from its control plane operations for failover input.

## Route 53 Private DNS
<a name="route-53-private-dns"></a>

 Route 53 private hosted zones are supported in each partition; however, the considerations for private hosted zones and public hosted zones in Route 53 are the same. Refer to *Amazon Route 53* in *[Appendix B - Edge network global service guidance](appendix-b---edge-network-global-service-guidance.md)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
