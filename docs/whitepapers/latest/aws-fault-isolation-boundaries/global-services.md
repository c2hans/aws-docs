---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html
---

# Global services
<a name="global-services"></a>

 In addition to regional and zonal AWS services, there’s a small set of AWS services whose scope is considered *global*. This is because their resources aren’t Region-specific. Global AWS services still follow the conventional AWS design pattern of separating the control plane and data plane to achieve static stability. The significant difference for most global services is that their control plane is hosted in a single AWS Region, while their data plane is globally distributed.

 Using a global service control plane in your runtime operations, or multi-AZ or multi-Region recovery workflows can introduce single points of failure in your platforms and applications. You should avoid single point of failure dependencies that prevent your applications from recovering. However, you shouldn’t expect failure simultaneously in multiple Regions, so this risk is present typically in two situations.
+ Your multi-AZ or multi-Region application runs in the same Region as a global service control plane whose services you depend on during failover and recovery
+ Your application depends on a global service control plane for runtime operations outside of the Region your application operates in

 To make your applications more resilient to the impairment of global AWS services, you should remove global service control plane dependencies in your recovery path and be able to gracefully degrade if you use them in your runtime operations. This allows your applications to be statically stable to global service control plane impairments. There are three different types of global services you should consider as you build resilience in your applications and platforms.

## Global services that are unique by partition
<a name="global-services-that-are-unique-by-partition"></a>

 Some global AWS services exist uniquely in each AWS partition (referred to in this paper as *partitional* services). Some partitional services, such as [AWS Network Manager](https://docs.aws.amazon.com/managedservices/latest/userguide/networking-manager.html), are control plane-only and orchestrate the data plane of other services. Other partitional services, such as IAM, operate their data plane independently across all Regions in the partition. Failures in a partitional service data plane don’t impact services in other partitions. There are also some global services that operate their data planes in the global points of presence network and within some or all the AWS Regions in the partition. This separation of control plane and data plane for IAM in a single partition is shown in the following figure.

![This image shows that the IAM control plane is hosted in a single AWS Region and its data plane is globally distributed within each Region in the partition](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/iam-single-control-plane-and-regionalized-data-plane.png)

 The following table lists the partitional AWS services, where their control plane is located in the `aws` partition, and whether their data plane runs in the Regions of the partition, the PoP network, or both. Not all services are available in all partitions.

| Service | Control plane | Data plane in Regions | Data plane in PoPs |
| --- | --- | --- | --- |
| IAM | us-east-1 | X |  |
| AWS Organizations\* | us-east-1 |  |  |
| AWS Account Management | us-east-1 | X |  |
| Amazon Application Recovery Controller (ARC) | us-west-2 | X |  |
| AWS Network Manager\* | us-west-2 |  |  |
| Amazon Route 53\*\* | us-east-1 | X | X |
| Amazon CloudFront | us-east-1 | X | X |
| AWS WAF Classic for CloudFront | us-east-1 |  | X |
| AWS WAF for CloudFront | us-east-1 |  | X |
| AWS Certificate Manager for CloudFront | us-east-1 |  | X |
| AWS Global Accelerator | us-west-2 |  | X |
| AWS Shield Advanced | us-east-1 | X | X |

\*These are control plane-only services that don’t provide a distinct data plane that you use directly

\*\*This includes private hosted zones, public hosted zones, and health checks. Private hosted zones and health checks aren’t hosted in the PoP network.

 During a failure impacting the Region hosting the control planes for these services, or a failure impacting the control plane itself, you might be unable to use the CRUDL-type operations provided by these services. If you have taken dependencies on these operations in your recovery strategy, that strategy might be less likely to succeed than if you only rely on the data plane of these services. You should also consider that most AWS global services also provide a global AWS Management Console hosted in the same Region as their control plane. You should avoid console dependencies for these services in the same fashion as their control planes.

**Global services best practices**
To be statically stable to a global service control plane impairment, you shouldn’t rely on the control plane functionality or the AWS Management Console functionality of the global service for recovery. If your service has a runtime dependency on one of these global service control planes, you should plan to gracefully degrade when the control plane is degraded or unavailable.

## Globally scoped operations
<a name="globally-scoped-operations"></a>

 This category is composed of specific control plane operations within a service that have a global impact scope, not entire services like the previous category. These service operations have a cross-Region control plane dependency. During a failure impacting the underlying global dependency, you might be unable to use the CRUDL-type actions of the dependent operations. These operations are described in the following sections.

### Provisioning resources with DNS in Amazon Route 53
<a name="provisioning-resources-with-dns-in-amazon-route-53"></a>

 Many AWS services create resources with resource-specific DNS names. For example, when you provision a load balancer, the Elastic Load Balancing service creates a public DNS record like `name-id.elb.us-east-2.amazonaws.com` and health checks in Route 53 for the ELB. This relies on the Route 53 control plane in `us-east-1`. Other services that you use might also need to provision an ELB, create Route 53 DNS records, or create Route 53 health checks as part of their control plane workflows.

 In December 2025, we announced that Route 53 supports [a standby control plane endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/accelerated-recovery.html) in `us-west-2`. This gives your applications and AWS services the ability to continue to publish, update, or delete public Route 53 records as part of your runtime provisioning or recovery operations after an event impacting the primary control plane in `us-east-1`. Some AWS services use an internal version of this feature to continue resource provisioning and perform recovery during a service disruption in `us-east-1`.

 The following is a list of services whose control plane depends on the Route 53 control plane in `us-east-1` to create, update, or delete DNS records, hosted zones, or create Route 53 health checks. This list isn’t exhaustive; it’s meant to highlight some of the most commonly used services whose control plane actions for creating, updating, or deleting resources depend on the Route 53 control plane, and which use the internal recovery endpoint (at the time of publication, October 2026).

| Service | Uses recovery endpoint |
| --- | --- |
| [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/) | X |
| Amazon Relational Database Service | X |
| Elastic Load Balancing (ELB) | X |
| [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | X |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | X |
| [Amazon Redshift and Redshift Serverless](https://aws.amazon.com/redshift/) | X |
| [Amazon ElastiCache](https://aws.amazon.com/elasticache/) | X |
| [Amazon MemoryDB](https://aws.amazon.com/memorydb/) | X |
| Amazon DynamoDB Accelerator (DAX) | X |
| [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) | X |
| [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) | X |
| Amazon CloudFront | X |
| Amazon EKS |  |
| Amazon API Gateway REST and HTTP APIs |  |
| [AWS PrivateLink VPC endpoints](https://aws.amazon.com/privatelink/) |  |
| AWS Lambda URLs |  |
| AWS Global Accelerator |  |
| [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) |  |
| [Amazon Elastic Container Service ](https://aws.amazon.com/ecs/)(Amazon ECS)\* |  |

\*With DNS-based Service Discovery, which uses the AWS Cloud Map API to manage Route 53 DNS

### Amazon S3
<a name="amazon-s3-globally-scoped"></a>

 The following Amazon S3 control plane operations have an underlying dependency on `us-east-1` in the `aws` partition. A failure impacting the Amazon S3 control plane in `us-east-1` might cause these control plane actions to be impaired in other Regions:

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

 Amazon S3 [bucket names are globally unique](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) and all calls to the `CreateBucket` and `DeleteBucket` APIs depend on `us-east-1` in the `aws` partition to help make sure name uniqueness, even though the API call is directed at the specific Region in which you want to create or delete the bucket. If you have critical bucket creation workflows, you shouldn’t depend on the availability of any specific spelling of a bucket name, particularly those following a discernible pattern.

 The control plane for Amazon S3 Multi-Region Access Points (MRAP) is [hosted only in `us-west-2`](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) and requests to create, update, or delete MRAPs target that Region directly. The control plane for MRAP also has underlying dependencies on Global Accelerator in `us-west-2`, Route 53 in `us-east-1`, and [ACM](https://aws.amazon.com/acm) in each Region where the MRAP is configured to serve content from. You shouldn’t depend on the availability of the MRAP control plane in your recovery path or in your own systems’ data planes. This is distinct from [MRAP failover controls](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapFailover.html) that are used to specify active or passive routing status for each of your buckets in the MRAP. These APIs are hosted in [five AWS Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html#update-mrap-route-configuration) through integration with Amazon Application Recovery Controller routing controls and can be used to effectively shift traffic through data plane operations, without a dependency on a control plane.

### Amazon API Gateway edge-optimized endpoints
<a name="amazon-api-gateway-edge-optimized-endpoints"></a>

 [Amazon API Gateway](https://aws.amazon.com/api-gateway) provides [edge-optimized API endpoints](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html#api-gateway-api-endpoint-types-edge-optimized). Creating these endpoints depends on the CloudFront control plane in `us-east-1` to create the distribution in front of the API Gateway regional endpoint.

**Globally scoped operations best practices**
All the operations discussed in this section are control plane actions, not data plane. If your applications are configured to be statically stable, these dependencies shouldn’t impact your recovery path, keeping in mind that static stability requires additional work or services to implement.

## Global endpoints
<a name="global-endpoints"></a>

 Another subset of AWS services provide global API endpoints that don’t specify an AWS Region in their domain name. AWS hosts these global endpoints in a single Region while also offering regional endpoints. These include the [AWS Security Token Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) (AWS STS), the AWS Management Console, and the AWS Sign-In APIs. The capabilities offered by these services with global endpoints are equivalent in all Regions. For example, the credentials vended from a regional AWS STS endpoint are valid in any Region. Similarly, instead of relying on the console global endpoint to redirect you to your last used Region, you can access the management console of that Region directly.

**Global endpoint best practices**
Use the Region-specific endpoint for services that offer a global endpoint to avoid unintended dependencies on other Regions.

## Single-Region services
<a name="single-region-services"></a>

 A few AWS services are only supported in a single Region or can only be deployed in a single Region of your choosing. The same guidance for implementing static stability provided for other global services applies to these services when you need to plan for dependencies on their control planes and data planes.
+ [AWS HealthScribe](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html#health-scribe-availability) – This feature of Amazon Transcribe is only offered in `us-east-1`.
+ [AWS Marketplace](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html) – The following AWS Marketplace services are only offered in `us-east-1`: AWS Marketplace Catalog API, AWS Marketplace Commerce Analytics, and AWS Marketplace Entitlement Service
+ [Billing and Cost Management](https://docs.aws.amazon.com/general/latest/gr/billing.html) – The following billing and cost management services are only offered in `us-east-1`: AWS Cost Explorer, AWS Cost and Usage Reports, AWS Cost Optimization Hub, AWS Data Exports, and AWS Free Tier
+ [AWS Billing Conductor](https://docs.aws.amazon.com/general/latest/gr/billingconductor.html) – This service is only offered in `us-east-1`.
+ [Amazon Chime](https://docs.aws.amazon.com/general/latest/gr/chime.html) – This service is only offered in `us-east-1`.
+ [Amazon Chime SDK](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) – The Legacy Chime SDK service is only offered in `us-east-1`.
+ [AWS DeepRacer](https://docs.aws.amazon.com/general/latest/gr/deepracer.html) – This service is only offered in `us-east-1`.
+ [AWS Device Farm](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html) – This service is only offered in `us-west-2`.

**Single-Region services best practices**
Avoid using single-Region services in your recovery workflows.
