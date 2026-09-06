---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-region-api-gateway-with-cloudfront/multi-region-api-gateway-with-cloudfront.html
---

# Multi-region API Gateway with CloudFront
<a name="multi-region-api-gateway-with-cloudfront"></a>

Publication date: **April 19, 2022 ([Diagram history](#diagram-history))**

This architecture shows how you can reduce latency for end-users, while increasing an application’s availability by providing API Gateway endpoints in multiple AWS Regions. Each endpoint offers read-local write-global data synchronization supported by the Amazon Aurora Global Database.

## Multi-region API Gateway with CloudFront
<a name="diagram1"></a>

![Reference architecture diagram showing how you can reduce latency for end-users, while increasing an application’s availability by providing API Gateway endpoints in multiple AWS Regions. Each endpoint offers read-local write-global data synchronization supported by the Amazon Aurora Global Database.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-region-api-gateway-with-cloudfront/images/multi-region-gateway.png)

1. Deploy an API endpoint in two or more AWS Regions using **Amazon API Gateway**, then handle requests using **AWS Lambda** connected to an **Amazon Aurora** relational database.

1. To keep data in sync across all AWS Regions, enable the **Aurora** Global Database feature. **Aurora** automatically routes write requests to the primary node to support data transactions, and replicates the changes to all nodes across AWS Regions.

1. To support custom domains, upload the domain’s SSL Certificate into **AWS Certificate Manager** (ACM) and attach it to an **Amazon CloudFront** distribution.

1. Point your domain name to **CloudFront** by using **Amazon Route 53** as your DNS name resolution service.

1. Set up a routing rule on **Route 53** to route your global clients to the AWS Region with least latency to their location.

1. Ensure clients can authenticate seamlessly to **API Gateway** endpoints in any Region by using **AWS Lambda** @Edge to query Route 53 for the best AWS Region to forward the request to. This normalizes authorization by abstracting the specifics of each regional endpoint.

1. Clients across the globe can then connect to your APIs using a single endpoint available in edge locations.

1. **CloudFront** will seamlessly route client requests from edge locations to the API in the AWS Region with the lowest latency to the client’s location.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 19, 2022 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
