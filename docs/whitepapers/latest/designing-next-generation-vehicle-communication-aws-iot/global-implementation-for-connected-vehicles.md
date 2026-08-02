---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/global-implementation-for-connected-vehicles.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Global implementation for connected vehicles
<a name="global-implementation-for-connected-vehicles"></a>

 When building a connected vehicle architecture on AWS, customers need to be aware that most of the AWS services are regional services. When it comes to high availability (HA) and durability, many services already are, or can provide, support for building highly available solutions within a Region (like [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/disaster-recovery-resiliency.html), or [Amazon S3](https://aws.amazon.com/s3/faqs/)).

 We see customers with the need to deploy workloads in multiple regions as the vehicles will also be distributed globally to ensure regional latency is minimized between the vehicle and the cloud.

 This scope of this whitepaper is not to provide a generalized solution to align for all business use cases, but will dive into a few considerations and explain the patterns we see repeated between OEMs.

![Reference architecture diagram showing a global implementation for connected vehicles.](http://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/images/global-implementation-connected-vehicles.png)

## Global endpoints
<a name="global-endpoints"></a>

 Each regional AWS IoT Core endpoint is reachable either by the [individual service endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html) defined by AWS or the customer is also able to create [configurable endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html) to connect vehicle gateways.

**Note**
Using a configurable endpoint over the default AWS IoT Core endpoint is highly recommended to be stay flexible throughout the vehicle lifetime.

Either way, for the vehicle devices the customer will want to minimize a static configuration on the vehicle to stay flexible throughout the lifetime of the vehicle; this flexibility should also cover the endpoint that the vehicle connects to for communicating with the backend systems. With this reason in mind the customer should leverage [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html), the globally highly available DNS web service provided by AWS, or any other DNS Server as the global endpoint that will manage the routing logic for the vehicles.

 Amazon Route 53 offers [geolocation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html) or [latency](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html) based routing logic to direct the vehicle to the right AWS IoT Core endpoint. How this can be configured is described in detail in [this blog post](https://aws.amazon.com/blogs/iot/automate-global-device-provisioning-with-aws-iot-core-and-amazon-route-53/).

 Additionally, to the endpoint and routing logic, customers implement a vehicle registry table with the vehicle information which contains the existing regional endpoint for the vehicle gateway. The vehicle registry table is normally initially populated with the device information during manufacturing time prior to connecting to AWS IoT Core. This table can be coupled with the Amazon Route 53 setup by adding an Amazon API gateway as interface and then additionally use Amazon Lambda for the compute logic which interacts with the table.

 Depending to your business requirements, the customer might want to add logic to the device itself that allows it to reconnect to AWS Route 53 on location change (which also might be needed for some countries where specific or all data is not allowed to be stored or transmitted depending on country requirements). This approach is normally limited in scope to smaller OEMs and mobility providers.

### Static regional endpoint
<a name="static-regional-endpoint"></a>

 Slightly larger OEMs, with limited regional opportunities for sales markets, are choosing the market at the end of the production line, knowing that vehicle gateway will be pointed to the single region for the lifetime of the vehicle gateway. This simplifies the process for the OEMs to have a single workflow in the device-VIN pairing process to burn into the vehicle gateway the IoT Core endpoint.

**Note**
This endpoint can still be redirected to other AWS IoT Core endpoints or other cloud provider if necessary, as the DNS lookup in Amazon Route 53 or the DNS server of your choosing can be modified, but would be limited to a single endpoint change across the fleet, rather than reconfiguring a single vehicle to point to a new endpoint.

### Regional vehicle provisioning process using AWS IoT Core JITR
<a name="regional-vehicle-provisioning-process-utilizing-aws-iot-core-jitr"></a>

 Since the customer might not know which Region a device will connect to throughout its lifetime, the implementation will need to leverage a provisioning flow that allows the connection for every region the connected vehicle platform will support.

 From a best practices perspective, the AWS team recommends the just-in-time registration (JITR) flow as the best practice in the connected vehicle space providing the most flexibility and extensibility for regional vehicle provisioning (this is discussed in the previous section of Onboarding and Provisioning). For JITR, the customer will first need to import the certificate of the Subordinate/signing CA (either managed on-premises or by AWS Private CA) to AWS IoT Core. There are [two modes to register CA](https://docs.aws.amazon.com/iot/latest/apireference/API_CACertificateDescription.html#iot-Type-CACertificateDescription-certificateMode) certificates: DEFAULT and SNI\_ONLY. If the certificate is registered in different regions, those can all be in DEFAULT mode. Within a region (and then multiple accounts) only one CA can be registered in DEFAULT mode and the others need to be [registered in SNI\_ONLY mode](https://aws.amazon.com/blogs/iot/simplify-multi-account-device-provisioning-and-certificate-authority-registration-using-aws-iot-core/). The CA will need to be registered in every account and region, in which the vehicles could eventually connect to, namely where your connected vehicle platforms exist.

 The implementation/platform will deploy all other resources required for JITR (Lambdas, Private CA, etc.) using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) (or the preferred infrastructure-as-code solution). This allows the customer to also make this part of your version control solution in place, track any changes (also allow for roll backs) and provide the exact same functionality across all required regions.

### Replication of data between Regions
<a name="replication-of-data-between-regions"></a>

 Another consideration for a global location is the reconfiguration of endpoints during the lifetime of a vehicle. An example would be that a person moves from Europe to the United States and also moves the vehicle that they own.

 The simplest solution is to determine the minimum data and configuration necessary to mirror over to new region. The vehicle needs to reconnect to the global endpoint on Region change (which needs to be implemented on vehicle side) and the AWS Lambda function can then check the vehicle registry table to incorporate the regional reconfiguration of locations and clean up and replicate anything in the old region to the new region if necessary.

 Customers often switch to this approach, which is the simplest solution, after they first propose to keep all regions in sync. This would firstly be very cost intensive and not only impact AWS IoT Core, its data and configuration but also any downstream environments (examples are, but not limited to, ETL solutions, Machine Learning models, Analytics and Databases). A few of the AWS services allow for multi-region data synchronization like [Amazon Dynamo DB](https://aws.amazon.com/dynamodb/global-tables/) or [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html). You also need to keep the data end user in mind and our recommendation is to only take the hard requirements into account for replicating not only storage but also transfer and transformation. Also be aware that some data might not be allowed to leave a region and be synchronized to a different one based on country laws. For setting up this logic of replication Figure 3 mentions AWS CloudFormation stack resources which you deploy into the regions needed and facilitate the logic needed on cloud side.
