---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html
---

# Global services
<a name="global-services"></a>

 In addition to Regional and zonal AWS services, there is a small set of AWS services whose control planes and data planes don’t exist independently in each Region. Because their resources are not Region-specific, they are commonly referred to as *global*. Global AWS services still follow the conventional AWS design pattern of separating the control plane and data plane in order to achieve static stability. The significant difference for most global services is that their control plane is hosted in a *single* AWS Region, while their data plane is globally distributed. There are three different types of global services and a set of services that can appear to be global based on your selected configuration.

 The following sections will identify each type of global service and how their control planes and data planes are separated. You can use this information to guide how you build reliable high availability (HA) and disaster recovery (DR) mechanisms without needing to depend on a global service control plane. This approach helps remove single points of failure in your architecture and avoids potential cross-Region impacts, even when you are operating in a Region that is different from where the global service control plane is hosted. It also helps you safely implement failover mechanisms that do not rely on global service control planes.

## Global services that are unique by partition
<a name="global-services-that-are-unique-by-partition"></a>

 Some global AWS services exist in each partition (referred to in this paper as *partitional* services). Partitional services provide their control plane in a single AWS Region. Some partitional services, such as AWS Network Manager, are control plane-only and orchestrate the data plane of other services. Other partitional services, such as IAM, have their own data plane that is isolated and distributed across all of the AWS Regions in the partition. Failures in a partitional service do not impact other partitions. In the `aws` partition, the IAM service’s control plane is in the `us-east-1` Region, with isolated data planes in each Region of the partition. Partitional services also have independent control planes and data planes in the `aws-us-gov` and `aws-cn` partitions. The separation of control plane and data plane for IAM is shown in the following diagram.

![This image illustrates that IAM has a single control plane and regionalized data plane](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/iam-single-control-plane-and-regionalized-data-plane.png)

 The following are partitional services and their control plane location in the `aws` partition:
+ AWS IAM (`us-east-1`)
+ AWS Organizations (`us-east-1`)
+ AWS Account Management (`us-east-1`)
+ Route 53 Application Recovery Controller (ARC) (`us-west-2`) - This service is only present in the `aws` partition
+ AWS Network Manager (`us-west-2`)
+ Route 53 Private DNS (`us-east-1`)

 If any of these service control planes have an availability-impacting event, you may be unable to use the CRUDL-type operations provided by these services. Thus, if your recovery strategy has a dependency on these operations, an availability impact to the control plane or the Region hosting the control plane will reduce your chances of successful recovery. [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) provides strategies for removing dependencies on global service control planes during recovery.

****Recommendation****
Do not rely on the control planes of partitional services in your recovery path. Instead, rely on the data plane operations of these services. See [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) for additional details on how you should design for partitional services.

## Global services in the edge network
<a name="global-services-in-the-edge-network"></a>

 The next set of global AWS services have a control plane in the `aws` partition and host their data planes in the global [points of presence](points-of-presence.md) (PoP) infrastructure (and potentially AWS Regions as well). The data planes hosted in PoPs can be accessed from resources in any partition as well as the internet. For example, Route 53 operates its control plane in the `us-east-1` Region, but its data plane is distributed across hundreds of PoPs globally, as well as each AWS Region (to support Route 53 Public and Private DNS within the Region). Route 53 health checks are also part of the data plane, and are performed from eight AWS Regions in the `aws` partition. Clients can resolve DNS using Route 53 public hosted zones from anywhere on the internet, including other partitions like GovCloud, as well as from an AWS Virtual Private Cloud (VPC). The following are global edge network services and their control plane location in the `aws` partition:
+ Route 53 Public DNS (`us-east-1`)
+ Amazon CloudFront (`us-east-1`)
+ AWS WAF Classic for CloudFront (`us-east-1`)
+ AWS WAF for CloudFront (`us-east-1`)
+ Amazon Certificate Manager (ACM) for CloudFront (`us-east-1`)
+ AWS Global Accelerator (AGA) (`us-west-2`)
+ AWS Shield Advanced (`us-east-1`)

 If you use AGA health checks for EC2 instances or Elastic IP addresses, these use Route 53 health checks. Creating or updating AGA health checks would depend on the Route 53 control plane in `us-east-1`. The execution of the AGA health checks utilizes the Route 53 health check data plane.

 During a failure impacting the Region hosting the control planes for these services, or a failure impacting the control plane itself, you may be unable to use the CRUDL-type operations provided by these services. If you have taken dependencies on these operations in your recovery strategy, that strategy may be less likely to succeed than if you only rely on the data plane of these services.

****Recommendation****
Do not rely on the control plane of edge network services in your recovery path. Instead, rely on the data plane operations of these services. See [Appendix B - Edge network global service guidance](appendix-b---edge-network-global-service-guidance.md) for additional details on how to design for global services in the edge network.

## Global Single-Region operations
<a name="global-single-region-operations"></a>

 The final category is composed of specific control plane operations within a service that have a global impact scope, not entire services like the previous categories. While you interact with zonal and Regional services in the Region you specify, certain operations have an underlying dependency on a single Region that is different from where the resource is located. These are different than services that are only provided in a single Region; refer to [Appendix C - Single-Region services](appendix-c---single-region-services.md) for a list of those services.

 During a failure impacting the underlying global dependency, you may be unable to use the CRUDL-type actions of the dependent operations. If you have taken dependencies on these operations in your recovery strategy, that strategy may be less likely to succeed than if you only rely on the data plane of these services. You should avoid dependencies on these operations for your recovery strategy.

 The following is a list of services that other services may take dependencies on, which have global scope:
+  **Route 53**

  Several AWS services create resources that provide a resource-specific DNS name(s). For example, when you provision an Elastic Load Balancer (ELB), the service creates public DNS records and health checks in Route 53 for the ELB. This relies on the Route 53 control plane in `us-east-1`. Other services that you use might also need to provision an ELB, create public Route 53 DNS records, or create Route 53 health checks as part of their control plane workflows. For example, provisioning an Amazon API Gateway REST API resource, Amazon ELB load balancer, or an Amazon OpenSearch Service domain all result in creating DNS records in Route 53. The following is a list of services whose control plane depends on the Route 53 control plane in `us-east-1` to create, update, or delete DNS records, hosted zones, and/or create Route 53 health checks. This list is not exhaustive; it is meant to highlight some of the most commonly-used services whose control plane actions for creating, updating, or deleting resources depend on the Route 53 control plane:
  + Amazon API Gateway REST and HTTP APIs
  + Amazon ELB load balancers
  + AWS PrivateLink VPC endpoints
  + AWS Lambda URLs
  + Amazon ElastiCache
  + Amazon OpenSearch Service
  + Amazon CloudFront
  + Amazon MemoryDB
  + Amazon Neptune
  + Amazon DynamoDB Accelerator (DAX)
  + AGA
  + Amazon Elastic Container Service (Amazon ECS) with DNS-based Service Discovery (which uses the AWS Cloud Map API to manage Route 53 DNS)
  + Amazon EKS Kubernetes control plane

    It is important to note that the VPC DNS service for [EC2 instance hostnames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) exists independently in each AWS Region and does not depend on the Route 53 control plane. Records that AWS creates for EC2 instances in the VPC DNS service, like `ip-10-0-10.ec2.internal`, `ip-10-0-1-5.compute.us-west-2.compute.internal`, `i-0123456789abcdef.ec2.internal`, and `i-0123456789abcdef.us-west-2.compute.internal`, do not rely on the Route 53 control plane in `us-east-1`.
****Recommendation****
Do not rely on creating, updating, or deleting resources that require the creation, updating, or deletion of Route 53 resource records, hosted zones, or health checks in your recovery path. Pre-provision these resources, like ELBs, to prevent a dependency on the Route 53 control plane in your recovery path.
+  **Amazon S3**

  The following Amazon S3 control plane operations have an underlying dependency on `us-east-1` in the `aws` partition. A failure impacting Amazon S3 or other services in `us-east-1` could cause these control planes actions to be impaired in other Regions:

  ```
  PutBucketCors
  DeleteBucketCors
  PutAccelerateConfiguration
  PutBucketRequestPayment
  PutBucketObjectLockConfiguration
  PutBucketTagging
  DeleteBucketTagging
  PutBucketReplication
  DeleteBucketReplication
  PutBucketEncryption
  DeleteBucketEncryption
  PutBucketLifecycle
  DeleteBucketLifecycle
  PutBucketNotification
  PutBucketLogging
  DeleteBucketLogging
  PutBucketVersioning
  PutBucketPolicy
  DeleteBucketPolicy
  PutBucketOwnershipControls
  DeleteBucketOwnershipControls
  PutBucketAcl
  PutBucketPublicAccessBlock
  DeleteBucketPublicAccessBlock
  ```

  The control plane for Amazon S3 Multi-Region Access Points (MRAP) is [hosted only in `us-west-2`](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) and requests to create, update, or delete MRAPs target that Region directly. The control plane for MRAP also has underlying dependencies on AGA in `us-west-2`, Route 53 in `us-east-1`, and ACM in each Region where the MRAP is configured to serve content from. You should not depend on the availability of the MRAP control plane in your recovery path or in your own systems’ data planes. This is distinct from [MRAP failover controls](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapFailover.html) that are used to specify active or passive routing status for each of your buckets in the MRAP. These APIs are hosted in [five AWS Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html#update-mrap-route-configuration) and can be used to effectively shift traffic using the service's data plane.

  Additionally, Amazon S3 [bucket names are globally unique](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) and all calls to the `CreateBucket` and `DeleteBucket` APIs depend on `us-east-1`, in the `aws` partition, to ensure name uniqueness, even though the API call is directed at the specific Region in which you want to create the bucket. Finally, if you have critical bucket creation workflows, you should not depend on the availability of any specific spelling of a bucket name, particularly those following a discernible pattern.
****Recommendation****
Do not rely on deleting or creating new S3 buckets or updating S3 bucket configurations as part of your recovery path. Pre-provision all required S3 buckets with the necessary configurations so that you do not need to make changes in order to recover from a failure. This approach applies to MRAPs as well.
+  **CloudFront**

   Amazon API Gateway provides [edge-optimized API endpoints](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html#api-gateway-api-endpoint-types-edge-optimized). Creating these endpoints depends on the CloudFront control plane in `us-east-1` to create the distribution in front of the gateway endpoint.
****Recommendation****
Do not rely on creating new edge-optimized API Gateway endpoints as part of your recovery path. Pre-provision all required API Gateway endpoints.

  All of the dependencies discussed in this section are control plane actions, not data plane actions. If your workloads are configured to be statically-stable, these dependencies should not impact your recovery path, keeping in mind that static stability requires additional work or services to implement.

## Services that use default global endpoints
<a name="services-that-use-default-global-endpoints"></a>

 In a few cases, AWS services provide a default, global endpoint, like AWS Security Token Service ([AWS STS](https://docs.aws.amazon.com/general/latest/gr/sts.html)). Other services may use this default, global endpoint in their default configuration. This means that a Regional service you are using could have a global dependency on a single AWS Region. The following details explain how to remove unintended dependencies on default global endpoints that will help you use the service in a Regional way.

 **AWS STS:** STS is a web service that enables you to request temporary, limited-privilege credentials for IAM users or for users you authenticate (federated users). STS usage from the AWS software development kit (SDK) and command line interface (CLI) defaults to `us-east-1`. The STS service also provides Regional endpoints. These endpoints are enabled by default in Regions that are also enabled by default. You can take advantage of these at any time by configuring your SDK or CLI following these directions: [AWS STS Regionalized endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html). Using SigV4A also [requires temporary credentials requested from a Regional STS endpoint](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html#signature-versions). You cannot use the global STS endpoint for this operation.

****Recommendation****
Update your SDK and CLI configuration to use the Regional STS endpoints.

 **Security Assertion Markup Language (SAML) Sign-in:** SAML services exist in all AWS Regions. To use this service, choose the appropriate regional SAML endpoint, like [https://us-west-2.signin.aws.amazon.com/saml](https://us-west-2.signin.aws.amazon.com/saml). You must make updates to configurations in your trust policies and Identity Provider (IdP) to use the regional endpoints. Refer to the [AWS SAML documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) for specific details.

 If you are using an IdP that is also hosted on AWS, there is a risk that they may also be impacted during an AWS failure event. This could result in you not being able to update your IdP configuration or you may be unable to federate entirely. You should pre-provision “break-glass” users in case your IdP is impaired or unavailable. Refer to [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) for details on how to create break-glass users in a statically-stable way.

****Recommendation****
Update your IAM role trust policies to accept SAML logins from multiple Regions. During a failure, update your IdP configuration to use a different Regional SAML endpoint if your preferred endpoint is impaired. Create a break-glass user(s) in case your IdP is impaired or unavailable.

 **Amazon S3 Storage Lens:** Storage Lens provides a default dashboard called default-account-dashboard. The dashboard configuration and its associated metrics are stored in `us-east-1`. You can create additional dashboards in other Regions by specifying the [home Region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html#storage_lens_basics_home_region) for the dashboard configuration and metric data.

****Recommendation****
If you require data from the default S3 Storage Lens dashboard during a failure impacting the service in `us-east-1`, create an additional dashboard in an alternate home Region. You can also duplicate any other custom dashboards you have created in additional Regions.

## Global services summary
<a name="global-services-summary"></a>

 The data planes for global services apply similar isolation and independence principles as Regional AWS services. A failure impacting the data plane of IAM in a Region doesn’t affect the operation of the IAM data plane in another AWS Region. Similarly, a failure impacting the data plane of Route 53 in a PoP doesn’t affect the operation of the Route 53 data plane in the rest of the PoPs. Therefore, what we must consider are service availability events that affect the Region where the control plane operates or affect the control plane itself. Because there is only a single control plane for each global service, a failure affecting that control plane could have cross-Region effects on CRUDL-type operations (which are the configuration operations that are typically used to set up or configure a service as opposed to the direct use of the service).

 The most effective way to architect workloads to use global services resiliently is to use static stability. During a failure scenario, design your workload not to need to make changes with a control plane to mitigate the impact or failover to a different location. Refer to [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) and [Appendix B - Edge network global service guidance](appendix-b---edge-network-global-service-guidance.md) for prescriptive guidance on how to utilize these types of global services in order to remove control plane dependencies and eliminate single points of failure. If you require the data from a control plane operation for recovery, cache this data in a data store that can be accessed through its data plane, like an [AWS Systems Manager](https://aws.amazon.com/systems-manager/) Parameter Store (SSM Parameter Store) parameter, a DynamoDB table, or an S3 bucket. For redundancy, you may also choose to store that data in an additional Region. For example, following the [best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html) for Route 53 Application Recovery Controller (ARC), you should hardcode or bookmark your five Regional cluster endpoints. During a failure event, you might not be able to access some API operations, including Route 53 ARC API operations that are not hosted on the extremely reliable data plane cluster. You can list the endpoints for your Route 53 ARC clusters by using the `DescribeCluster` API operation.

 The following is a summary of some of the most common misconfigurations or anti-patterns that introduce dependencies on global services’ control planes:
+  Making changes to Route 53 records, like updating an A record’s value or changing a weighted record set’s weights, to perform failover.
+  Creating or updating IAM resources, including IAM roles and policies, during a failover. This typically isn’t intentional, but might be a result of an untested failover plan.
+  Making changes to AGA traffic dial weights to manually perform a Regional failover.
+  Updating a CloudFront distribution’s origin configuration to fail away from an impaired origin.
+  Provisioning disaster recovery (DR) resources, like ELBs and RDS instances during a failure event, that depend on creating DNS records in Route 53.

 The following is a summary of the recommendations provided in this section for using global services in a resilient way that would help prevent the previous common anti-patterns.

****Recommendation summary****
Do not rely on the control planes of partitional services in your recovery path. Instead, rely on the data plane operations of these services. See [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) for additional details on how you should design for partitional services.
 Do not rely on the control plane of edge network services in your recovery path. Instead, rely on the data plane operations of these services. See [Appendix B - Edge network global service guidance](appendix-b---edge-network-global-service-guidance.md) for additional details on how to design for global services in the edge network.
 Do not rely on creating, updating, or deleting resources that require the creation, updating, or deletion of Route 53 resource records, hosted zones, or health checks in your recovery path. Pre-provision these resources, like ELBs, to prevent a dependency on the Route 53 control plane in your recovery path.
 Do not rely on deleting or creating new S3 buckets or updating S3 bucket configurations as part of your recovery path. Pre-provision all required S3 buckets with the necessary configurations so that you do not need to make changes in order to recover from a failure. This approach applies to MRAPs as well.
 Do not rely on creating new edge-optimized API Gateway endpoints as part of your recovery path. Pre-provision all required API Gateway endpoints.
 Update your SDK and CLI configuration to use the Regional STS endpoints.
 Update your IAM role trust policies to accept SAML logins from multiple Regions. During a failure, update your IdP configuration to use a different Regional SAML endpoint if your preferred endpoint is impaired. Create break-glass users in case your IdP is impaired or unavailable.
 If you require data from the default S3 Storage Lens dashboard during a failure impacting the service in `us-east-1`, create an additional dashboard in an alternate home Region. You can also duplicate any other custom dashboards you have created in additional Regions.
