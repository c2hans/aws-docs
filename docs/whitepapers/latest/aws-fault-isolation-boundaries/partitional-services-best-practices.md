---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitional-services-best-practices.html
---

# Partitional services best practices
<a name="partitional-services-best-practices"></a>

This section provides best practices for using partitional services in your recovery operations.

This section covers the following topics:
+ [AWS Identity and Access Management](#aws-identity-and-access-management)
+ [AWS Organizations](#aws-organizations)
+ [AWS Account Management](#aws-account-management)
+ [Amazon Application Recovery Controller (ARC)](#amazon-application-recovery-controller)
+ [AWS Network Manager](#aws-network-manager)
+ [Amazon Route 53](#amazon-route-53)
+ [Amazon CloudFront](#amazon-cloudfront)
  + [Lambda@Edge](#lambda-at-edge)
  + [Amazon CloudFront Functions](#amazon-cloudfront-functions)
  + [Amazon CloudFront KeyValueStore](#amazon-cloudfront-keyvaluestore)
  + [AWS Certificate Manager (ACM) for CloudFront](#aws-certificate-manager-for-cloudfront)
  + [AWS Web Application Firewall (WAF) and WAF Classic](#aws-waf-and-waf-classic)
+ [AWS Global Accelerator](#aws-global-accelerator-bp)
+ [AWS Shield Advanced](#aws-shield-advanced)

## AWS Identity and Access Management
<a name="aws-identity-and-access-management"></a>

 The IAM control plane consists of all public IAM APIs (including Access Advisor but not IAM Access Analyzer or IAM Roles Anywhere). This includes actions like `CreateRole`, `AttachRolePolicy`, `ChangePassword`, `UpdateSAMLProvider`, and `UpdateLoginProfile`. The IAM data plane provides authentication and authorization for IAM principals in each AWS Region. During a control plane impairment, CRUDL type operations for IAM might not work, but authentication and authorization for existing principals will continue to work.

 When you’re planning for dependencies on IAM, you shouldn’t rely on the IAM control plane in your recovery path. For example, a statically stable design for a break-glass admin user would be to create a user with the appropriate permissions attached, have the password set and the access key and secret access key provisioned, and then lock those credentials in a physical or virtual vault. When required during an emergency, retrieve the user credentials from the vault and use them as needed.

 During a failover, you should not rely on the IAM control plane. Instead, pre-provision IAM roles to use with resources that you provision as part of your recovery. For example, use an existing role with a [Lambda](https://aws.amazon.com/lambda) function that you provision in your recovery workflow. A common pitfall when you provision your resources using infrastructure as code (IaC) is including all the IAM resources required for your application in the same IaC as the application itself. When you attempt to provision your recovery environment using your IaC definition, it also attempts to provision IAM resources. Instead, separate out the IAM resources from your application and reference them through parameters. By doing this, you can deploy your IAM resources once and then deploy the same application stack in multiple Regions without a dependency on IAM resource provisioning.

 A non-statically stable approach would be to provision IAM users during a failure, or having the user pre-provisioned, but only attaching the admin policy when required. Similarly, provisioning IAM resources during a failover process, for example a backup and restore approach where you launch IaC, would also not be statically stable. Both approaches depend on the IAM control plane to succeed.

## AWS Organizations
<a name="aws-organizations"></a>

 The [AWS Organizations](https://aws.amazon.com/organizations) control plane consists of all public Organizations APIs like `AcceptHandshake`, `AttachPolicy`, `CreateAccount`, `CreatePolicy`, and `ListAccounts`. There’s no data plane for AWS Organizations. The service orchestrates the data plane for other services like IAM. During a control plane impairment, CRUDL type operations for Organizations might not work, but the policies, like service control policies (SCP), resource control policies (RCP), and tag policies, will continue to work and be evaluated as part of the IAM authorization process. Delegated admin capabilities and multi-account features in other AWS services that are supported by Organizations will also continue to work.

 When you’re planning for dependencies on AWS Organizations, you shouldn’t rely on the Organizations control plane in your recovery path. Instead, implement static stability in your recovery plan. For example, a non-statically stable approach might be to update SCPs to remove restrictions on allowed AWS Regions using the `aws:RequestedRegion` condition, or to enable admin permissions for specific IAM roles. This relies on the Organizations control plane to make these updates. A statically stable approach would be to use [session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) to grant the use of admin permissions. Your identity provider (IdP) can include session tags that can be evaluated against the `aws:PrincipalTag` condition, which helps you to dynamically configure permissions for certain principals while allowing your SCPs and RCPs to remain static. This removes dependencies on the Organizations control plane.

## AWS Account Management
<a name="aws-account-management"></a>

 The AWS Account Management control plane consists of all [public APIs](https://docs.aws.amazon.com/accounts/latest/reference/api-reference.html) for managing an AWS account, such as `GetContactInformation` and `PutContactInformation`. It also includes creating or closing a new AWS account through the management console. The APIs for `CloseAccount`, `CreateAccount`, `CreateGovCloudAccount`, and `DescribeAccount` are part of the AWS Organizations control plane. [Creating an AWS GovCloud (US) account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html) relies on the AWS Account Management control plane. Also, AWS GovCloud (US) accounts [must be 1:1 linked](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html) to an AWS account in the `aws` partition. Creating accounts in the `aws-cn` and `aws-eusc` partitions doesn’t rely on resources in the `aws` partition. The data plane for AWS accounts is the accounts themselves. During a control plane impairment, CRUDL-type operations (like creating a new account or getting and updating contact information) for AWS accounts might not work. References to the account in IAM policies will continue to work.

 When you’re planning for dependencies on AWS Account Management, you shouldn’t rely on the account management control plane in your recovery path. Although the account management control plane doesn’t provide functionality that you would typically use in a recovery situation, there might be times when you would. For example, a statically stable design would be to pre-provision all the AWS accounts you need for failover. A non-statically stable design would be to create new AWS accounts during a failure event to host your failover resources.

## Amazon Application Recovery Controller (ARC)
<a name="amazon-application-recovery-controller"></a>

 [Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) provides three separate functions: routing control, Region switch, and zonal shift. Zonal shift is a regional service. The global control plane for ARC routing control consists of the [Recovery Readiness API](https://docs.aws.amazon.com/recovery-readiness/latest/api/what-is-recovery-readiness.html) and the [Recovery Control Configuration API](https://docs.aws.amazon.com/recovery-cluster/latest/api/what-is-recovery-control.html). The control plane for the [Region switch API](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.region-switch.html) is also global. These are documented in the [Amazon Application Recovery Controller endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/arc.html). You manage readiness checks, routing control setup, cluster operations, and Region switch plans by using these global control planes.

 The recovery control data plane of ARC is your recovery cluster, which manages the routing control values that are queried by Route 53 health checks and implements the safety rules. The data plane functionality of ARC is accessed through your recovery cluster APIs such as `https://aaaaaaaa.route53-recovery-cluster.eu-west-1.amazonaws.com`.

 Region switch has independent data planes in each AWS Region. You should use the data plane for recovery actions, that is, for executing Region switch plans. For a list of the data plane operations, see the Region switch API operations.

 You shouldn’t rely on the ARC global control plane in your recovery path. For ARC recovery control, there are two [best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.regional.html) that help implement this guidance. First, bookmark or hard code the five regional cluster endpoints. This removes the need to use the `DescribeCluster` control plane operation during a failover scenario to discover the endpoint values. Second, use the ARC cluster APIs by using the AWS CLI or AWS SDK to perform updates to routing controls instead of the console. This removes the console as a dependency for your failover plan and helps make sure that it depends only on data plane actions.

## AWS Network Manager
<a name="aws-network-manager"></a>

 The [AWS Network Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-manager.html) service is primarily a control plane-only system. Its purpose is to centrally manage the configuration of your AWS Cloud wide area networking (WAN) core network and your [AWS Transit Gateway](https://aws.amazon.com/transit-gateway) network across AWS accounts, Regions, and on-premises locations. It also aggregates your Cloud WAN metrics in `us-west-2`, which can also be accessed through the CloudWatch data plane. If Network Manager is impaired, the data plane of the services it orchestrates will not be impacted. The CloudWatch metrics for Cloud WAN are also available in `us-west-2`. If you want historical metric data, like bytes in and out per Region, to understand how much traffic might shift to other Regions during a failure impacting `us-west-2`, or for other operational purposes, you can export those metrics as CSV data directly from the CloudWatch console or using this method: [Publish Amazon CloudWatch metrics to a CSV file](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/publish-amazon-cloudwatch-metrics-to-a-csv-file.html). The data can be found under the `AWS/Network Manager` namespace and you can perform this on a schedule you choose and store it in Amazon S3 or in another data store you select. To implement a statically stable recovery plan, don’t use AWS Network Manager to make updates to your network or rely on data from its control plane operations for failover input.

## Amazon Route 53
<a name="amazon-route-53"></a>

 The Route 53 control plane consists of all public Route 53 APIs covering functionality for hosted zones, records, health checks, DNS query logs, reusable delegation sets, traffic policies, and cost allocation tags. It’s hosted in `us-east-1` with an optional [accelerated recovery option](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/accelerated-recovery.html) for public hosted zones in `us-west-2`. Domain registration is only hosted in `us-east-1`.

 The data plane for Route 53 consists of three parts, the public authoritative DNS resolution service, the private DNS service, and the health check service. In the `aws` partition, the data plane for public hosted zones runs across hundreds of PoP locations and in each AWS Region. In other partitions like `aws-us-gov` and `aws-cn`, the data plane for public hosted zones runs in multiple AWS Regions in the partition. The data plane for private hosted zones runs in each AWS Region in the partition. The data plane for the health check service runs across multiple AWS Regions where it performs the health checks, aggregates the results, and delivers them to the data plane of Route 53 public and private DNS and AGA. During a control plane impairment, CRUDL-type operations for Route 53 might not work, but DNS resolution and health checks, and updates to routing resulting from changes in health checks, will continue to work.

 The accelerated recovery option is best suited for situations where you must provision new resources that have new IP addresses that can’t be pre-provisioned and failed over with Route 53 health checks. For example, if you’re using service discovery and you need to replace a failed Amazon EC2 instance with a new one. When you’re planning for dependencies on Route 53, you shouldn’t rely on the Route 53 control plane in your recovery path for failover and recovery between Regions or to shift away from an Availability Zone. Instead, you should implement a statically stable design that uses the status of health checks to perform multi-Region failover or use [zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) for Multi-AZ recovery. Route 53 health checks can monitor:
+ [Amazon Application Recovery Controller (ARC) routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html)
+ [Amazon ARC Region Switch health check execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-health-check-block.html)
+ HTTP/S and TCP endpoints
+ CloudWatch alarms
+ Calculated health checks

 When configuring Route 53 health checks, you should have a manual way to force failover and optionally, an automated approach as well. Amazon ARC routing controls and the Amazon ARC Region Switch health check execution block options provide this capability. You can also perform manual failover using an HTTP/S or TCP endpoint where you control the response, like an Amazon S3 bucket as described in [Creating Disaster Recovery Mechanisms using Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/). This can also be performed with a CloudWatch alarm where you publish metrics directly that would cause the alarm to transition to the ALARM state (in this case the alarm isn’t monitoring metrics published by your applications, but rather metrics that a failover system publishes for the sole purpose of triggering failover).

 When using the CloudWatch alarm approach there are several important things to consider. First, the health checks for CloudWatch alarms are performed in two Availability Zones in three Regions to gather six signals (as opposed to the eight Regions that are used for HTTP/S and TCP endpoints). The health checkers must still consider at least 18% of their results to be healthy to consider the health check to pass, which requires two or more data points for CloudWatch alarms.

 Next, the health checkers must collect data from CloudWatch metrics to make their health evaluation. If there are no data points in the metric data, Route 53 relies on the `InsufficientDataHealthStatus`, which might be healthy, unhealthy, or last known status. If the metric will be unavailable frequently or for long periods (longer than a few hours), we recommend that you [not use the last known status](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-values.html#health-checks-creating-values-cloudwatch). If the metric is unavailable, meaning it can’t be retrieved by the health checker rather than only missing data, the health checks always use the last known status.

 If the alarm is in the same Region that’s impaired, for either automatic or manual failover, the health check system might not be able to retrieve CloudWatch metrics and will continue to use the last known status. To help make sure correlated impairments to CloudWatch in the Region you’re trying to fail away from don’t prevent you from failing over, you should place the alarm in an alternate Region. For example, if you primarily operate in `us-east-1`, you can place the alarm in `us-west-2`. If the alarm is monitoring application metrics, they would also need to exist in the other Region, which might require updates to your observability solution.

 To implement a pattern that allows for both automated failover and manual failover, you can use a calculated health check in Route 53 where one of the checks is based on your alarm in the primary Region and another monitors an option where you control the response to the health check. You would configure the health check to use `Report healthy when all health checks are healthy (AND)`. This makes sure that if either target is unhealthy, the overall record is considered unhealthy.

 A non-statically stable design would be to update the value of a Route 53 resource record using the `ChangeResourceRecordSets` API, change the weight of a weighted record, or create new records to perform failover. These approaches depend on the Route 53 control plane.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 The Amazon CloudFront control plane consists of all public CloudFront APIs for managing distributions. The data plane is the distribution itself served from the PoPs in the edge network. It performs the request handling, routing, and caching of your origin content. During a control plane impairment, CRUDL-type operations for CloudFront (including [invalidation requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation_Requests.html)) might not work, but your content will continue to be cached and served, [origin failovers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) will continue to work, and any associated CloudFront functions will continue to execute.

 When you’re planning for dependencies on CloudFront, you shouldn’t rely on the CloudFront control plane in your recovery path. For example, a statically stable design would be to use automated origin failovers to mitigate the impact from an impairment to one of your origins. Alternatively, you can use approaches described in the preceding [Amazon Route 53](#amazon-route-53) section to failover to a different CloudFront origin using DNS. You can also combine these approaches as described in [Improve web application availability with CloudFront and Route 53 hybrid origin failover](https://aws.amazon.com/blogs/networking-and-content-delivery/improve-web-application-availability-with-cloudfront-and-route53-hybrid-origin-failover/). A non-statically stable design would be to manually update the configuration of your distribution and origins in response to an origin failure or send invalidation requests. This approach would depend on the CloudFront control plane.

### Lambda@Edge
<a name="lambda-at-edge"></a>

 The [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) service runs its data plane in the CloudFront Regional Edge Caches (REC). The service’s control plane is hosted in `us-east-1`. The PoP location that receives the request forwards it to a pre-determined REC to handle the function invocation. You can’t control which Region handles Lambda@Edge invocations from specific PoPs, but CloudFront can shift invocations to other RECs when they observe a service disruption in one Region.

 Don’t rely on deploying or updating Lambda@Edge functions as part of your recovery path. Instead, a statically stable design would be to use dynamic lookups to the data plane of other services. For example, instead of changing the function code to rewrite the origin domain of a request, use a [DynamoDB](https://aws.amazon.com/dynamodb) Global Table to look up the correct origin domain to send the request. This avoids control plane dependencies to perform failover with Lambda@Edge functions.

 Although very unlikely, internet routing protocols might send a user request to a PoP that isn’t the closest geographically to the user. CloudFront doesn’t have control over this routing and as a result, an unexpected REC might process a user request. If Lambda@Edge invocations are impaired in a Region, users from other geographic areas might see impact. If the event is impacting services in `us-east-1`, both Lambda@Edge invocations and the control plane for Lambda@Edge or CloudFront might be impacted simultaneously.

 As a result, you may not be able to recover from the service disruption by disabling Lambda@Edge processing or modifying your CloudFront distribution. Lambda@Edge can shift invocations away from a Region on your behalf in response to a service disruption. However, depending on your use case, you should consider whether CloudFront Functions, which execute in the PoP rather than in a Region, provides a more resilient alternative.

### Amazon CloudFront Functions
<a name="amazon-cloudfront-functions"></a>

 [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions.html) is a global service whose control plane is hosted in `us-east-1` and consists of all public APIs for the service. The service’s data plane runs in each PoP location alongside your distribution. Don’t rely on deploying or updating CloudFront Functions as part of your recovery path. Instead, a statically stable approach for recovery from an origin disruption would be to use automatic origin failover or origin failover with DNS as described in the preceding section.

### Amazon CloudFront KeyValueStore
<a name="amazon-cloudfront-keyvaluestore"></a>

 The [CloudFront KeyValueStore](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html) is a global service hosted in `us-east-1` that consists of the APIs for creating, updating, reading, and deleting key stores and values. The contents of each KeyValueStore are distributed to all edge locations for low latency reads and can be performed without dependency on `us-east-1`.

 CloudFront functions can be used to [rewrite the request origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/helper-functions-origin-modification.html) to perform dynamic origin failover. If your function looks up the health status of each origin from a KeyValueStore to perform dynamic failover, updates to that health status key value depends on the CloudFront KeyValueStore API in `us-east-1`, which might not succeed if the API in `us-east-1` is impaired. A statically stable approach for recovery from an origin disruption would be to use automatic origin failover or origin failover with DNS as described in the preceding section.

### AWS Certificate Manager (ACM) for CloudFront
<a name="aws-certificate-manager-for-cloudfront"></a>

 If you’re using custom certificates with your CloudFront distribution, you also have a dependency on ACM. Using custom certificates with your CloudFront distribution relies on the ACM control plane in `us-east-1`. During a control plane impairment, your existing certificates configured in your distribution will continue to work as will automatic certificate renewals. Don’t rely on changing the distribution’s configuration or creating new certificates as part of your recovery path.

### AWS Web Application Firewall (WAF) and WAF Classic
<a name="aws-waf-and-waf-classic"></a>

 If you’re using [AWS WAF](https://aws.amazon.com/WAF) with your CloudFront distribution, you have a dependency on the WAF control plane, which is also hosted in `us-east-1`. During a control plane impairment, the configured web access control lists (ACLs) and their associated rules continue to function. Don’t rely on updating your WAF web ACLs as part of your recovery path.

## AWS Global Accelerator
<a name="aws-global-accelerator-bp"></a>

 The Global Accelerator control plane consists of all public Global Accelerator APIs. The data plane is the network routing of the anycast IP addresses provided by Global Accelerator to your registered endpoints. Global Accelerator also uses Route 53 health checks to determine the health of your Global Accelerator endpoints, which is part of the Route 53 data plane. During a control plane impairment, CRUDL-type operations for Global Accelerator might not work. Routing to your existing endpoints, along with existing health checks, traffic dials, and endpoint weight configurations used to route or shift traffic to other endpoints and endpoint groups will continue to work.

 When you’re planning for dependencies on AGA, you shouldn’t rely on the Global Accelerator control plane in your recovery path. For example, a statically stable design would be to use the status of the configured health checks to fail away from unhealthy endpoints. See [Deploying multi-Region applications in AWS using AWS Global Accelerator](https://aws.amazon.com/blogs/networking-and-content-delivery/deploying-multi-region-applications-in-aws-using-aws-global-accelerator/) for examples of this configuration. A non-statically stable design would be to modify the Global Accelerator traffic dial percentages, edit endpoint groups, or remove an endpoint from an endpoint group during an impairment. These approaches would depend on the Global Accelerator control plane.

## AWS Shield Advanced
<a name="aws-shield-advanced"></a>

 The [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) control plane consists of all public Shield Advanced APIs. This includes functionality like `CreateProtection`, `CreateProtectionGroup`, `AssociateHealthCheck`, `DescribeDRTAccess`, and `ListProtections`. The data plane is the distributed denial of service (DDoS) protection provided by Shield Advanced and the creation of Shield Advanced metrics. Shield Advanced also uses Route 53 health checks (which are part of the Route 53 data plane) if you’ve configured them. During a control plane impairment, CRUDL-type operations for Shield Advanced might not work, but the DDoS protection configured for your resources, in addition to responses to changes in health checks, will continue to function.

 When planning for dependencies on Shield Advanced, you shouldn’t rely on its control plane in your recovery path. Although the Shield Advanced control plane doesn’t provide direct functionality that you would typically use in a recovery situation, there might be certain situations when you would. For example, a statically stable design would be to have your DR resources already configured to be part of a protection group and have health checks associated with them as opposed to configuring that protection after the failure occurs. This prevents depending on the Shield Advanced control plane for recovery.
