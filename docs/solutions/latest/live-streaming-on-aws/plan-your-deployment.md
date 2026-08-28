---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

Plan your Live Streaming on AWS deployment

This section describes the [cost](#cost), [Security](#security), [Regions](#supported-aws-regions), and [quota considerations](#quotas) for planning your deployment.

<a name="supported-aws-regions"></a>== Supported AWS Regions

This solution uses AWS Elemental MediaLive, MediaPackage, and MediaConnect, which are currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where these services are available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). If you use MediaConnect as input, you must deploy this solution in the same Region as your MediaConnect flows.

<a name="cost"></a>== Cost

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution in the US East (N. Virginia) with:
+ Approximately 1,000 viewers for a one-hour live event using a standard definition (SD)-540p encoding profile is approximately **$2.50** for live encoding and packaging \+ **$67.24** for 791GB distribution = **$69.74 for the one-hour event**.
+ Approximately 10,000 viewers for a one-hour live event using a high definition (HD)-1080p encoding profile is approximately **$13.04** for live encoding and packaging \+ **$1,492.56** for 18,017GB distribution = **$1,505.60 for the one-hour event**.
+ Approximately 100 viewers for 200 hours live events each month using a high definition (HD)-1080p encoding profile is approximately **$904.69** for live encoding and packaging \+ **$2,934.00** for 36,035 GB distribution = **$3,838.69 for the total of 200 hours each month.**

These cost estimates depend on many factors, which are detailed in the following cost examples.

**Note**
The examples provided are likely higher than the actual costs of running this solution. The intent was to provide a guide to the pricing that is easily understood. Where assumptions were needed, we used factors that were straightforward to calculate and also likely be more expensive than the actual cost.

For an additional cost example for streaming a live event, refer to the [FAQs about live streaming on AWS](https://aws.amazon.com/blogs/media/frequently-asked-questions-about-the-cost-of-live-streaming/) blog in the *AWS Media Blog*.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

<a name="cost-example1"></a>=== Cost example 1

Cost example 1 covers a use case of approximately 1,000 viewers viewing a live event for about one hour with a **SD-540p** encoding profile selected in the AWS CloudFormation template. This cost example is based on the following factors:
+ Pricing Region: US-East-1, assuming standard pricing (no free-tier or discounts).
+ Viewers consume the highest bitrate: Note that bitrate consumption is a mix of all the streams, but the highest bitrate is used in the calculation to show the upper cost range. Additionally, the [Quality-Defined Variable Bitrate](https://aws.amazon.com/media/tech/quality-defined-variable-bitrate-qvbr/) (QVBR) and variable video complexity can result in an output bandwidth that is 10-50% lower in price than the estimate provided in Table 1.
+ 99% cache/hit ratio between the content delivery network (CDN) and [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/).

**Note**
Storage of the test player is not included in this cost estimate.

Table 1 summarizes the total pricing for the live streaming event. Tables 2 through 4 break down the cost for each AWS service.

 **Table 1: Cost breakdown for 1,000 viewers for a one-hour live event**

| AWS service | Function | Cost per hour [USD] |
| --- | --- | --- |
| AWS Elemental MediaLive | Input and outputs for channel | $1.99 |
| AWS Elemental MediaPackage | Ingest of channel | $0.11 |
|  | Packaging and origination | $0.40 |
| Amazon CloudFront | Distribution | $67.24 |
|  |  **Total:**  |  **$69.74/hour**  |

<a name="medialive-pricing"></a>==== AWS Elemental MediaLive pricing

Table 2 breaks down the AWS Elemental MediaLive pricing which assumes HD AVC input and SD AVC outputs with less than 10 Mbps bitrate and less than 30 frames per second (fps) frame rate.

 **Table 2: MediaLive pricing**

| Input / Output | Cost per hour [USD] |
| --- | --- |
| HD Input (AVC 10-20Mbps) | $0.234 |
| Output 1 SD (512x288, 400k) | $0.44 |
| Output 2 SD (640x360, 800k) | $0.44 |
| Output 3 SD (768x432, 1200k) | $0.44 |
| Output 4 SD (960x540, 1800k) | $0.44 |
|  **Total:**  |  **$1.99/hour**  |

<a name="mediapackage-pricing"></a>==== AWS Elemental MediaPackage pricing

MediaPackage charges $0.03 per Gigabyte (GB) per hour for standard Live ingest, based on the aggregate bitrate of all live input streams. This example has four input streams, so the rate of GB streaming per hour is determined by:

1. Adding the bitrate of all streams in either kbps or Mbps:
   + 400k \+ 800k \+ 1200k \+ 1800k = 4200 kbps
   + .4 \+ .8 \+ 1.2 \+ 1.8 = 4.2 Mbps

1. Convert kbps or Mbps to Gigabits (Gbit) per second (ps). 1024 Mb = 1 Gbit:
   + 4.2 Mbps / 1024 = 0.0041015625 Gbits ps

1. Convert Gbits to GB. 1 Gbit = 0.125 (or 1/8) GB.
   + 0.0041015625 Gbits ps \* 0.125 = 0.0005126953125 GBps

1. Convert GB per second to GB per hour:
   + 0.0005126953125 GBps \* 60s \* 60mins = 1.845703125 or 1.85 GB/hour

      sum of stream bitrates in Kbps) / 1024 (Mbps conversion / 1024 (Gbit conversion) \* .125 (bits to Bytes conversion) \* 60 seconds \* 60 minutes = GB / hour

 **Table 3: MediaPackage ingest pricing**

| Input / Output | kbps |
| --- | --- |
| Output 1 SD (512x288, 400k) | 400 |
| Output 2 SD (640x360, 800k) | 800 |
| Output 3 SD (768x432, 1200k) | 1,200 |
| Output 4 SD (960x540, 1800k) | 1,800 |
|  **Total kbps:**  | 4,200 |
| Convert kbps to GB/hour<br />4,200 kbps / 8 (bits to bytes) / 1024 (kbps to Mbps) / 1024 (Mbps to Gbps) x 60 (seconds) x 60 (minutes) | 1.85 GB/hour |
| GB/hour with redundancy | 3.70 GB/hour |
|  **Cost (GB/hour \* $0.03)**  |  **$0.11/hour**  |

 **Table 4: MediaPackage packaging and origin pricing**

| AWS service | Cost per hour [USD] |
| --- | --- |
| Total MediaPackage with 1% of egress<br />(7.91 GB x $0.05) | $0.40 |

**Note**
We assume that MediaPackage serves 1% of the traffic to CloudFront and viewers, and the rest is served by CloudFront. Table 5 provides the 1% of egress for the MediaPackage estimate in Table 4.

<a name="viewer-traffic-pricing"></a>==== Viewer traffic pricing

The cost estimate for viewer traffic assumes that all viewers get the highest bitrate for the one-hour live streaming event.

 **Table 5: Viewer traffic pricing**

| AWS service | Function | Total |
| --- | --- | --- |
| Amazon CloudFront | Average Mbps per viewer | 1.8 |
|  | Total MB per sec (1000 x 1.8 / 8) | 225 |
|  | Total Egress per hour ( 225 / 1024 x 60 x 60 ) | 791 GB/hour |
|  |  **Total cost (791 GB \* $0.085):**  |  **$67.24/hour**  |

<a name="cost-example2"></a>=== Cost example 2

Cost example 2 covers a use case of approximately 10,000 viewers viewing a live event for about one hour with an HD-1080p encoding profile selected in the CloudFormation template. This cost example is based on the following factors:
+ Pricing Region: US-East-1, assuming standard pricing (no free-tier or discounts).
+ Viewers consume the highest bitrate: Note that bitrate consumption is a mix of all the streams, but the highest bitrate is used in the calculation to show the upper cost range. Additionally, the QVBR and variable video complexity can result in an output bandwidth that is 10-50% lower in price than the estimate provided in Table 6.
+ 99% cache/hit ratio between the CDN and AWS Elemental MediaPackage.

**Note**
Storage of the test player is not included in this cost estimate.

Table 6 summarizes the total pricing for the live streaming event. Tables 7 through 10 breaks down the cost for each AWS service.

 **Table 6: Cost breakdown for 10,000 viewers for a one-hour live event**

| AWS service | Function | Cost per hour [USD] |
| --- | --- | --- |
| AWS Elemental MediaLive | Input and outputs for channel | $3.75 |
| AWS Elemental MediaPackage | Ingest of channel | $0.28 |
|  | Packaging and origination | $9.01 |
| Amazon CloudFront | Distribution | $1,492.56 |
|  |  **Total:**  |  **$1,505.60/hour**  |

<a name="medialive-pricing2"></a>==== AWS Elemental MediaLive pricing

Table 7 breaks down the AWS Elemental MediaLive pricing which assumes HD AVC input and both SD and HD AVC outputs with less than 10 Mbps bit rate and less than 30 fps frame rate.

 **Table 7: MediaLive pricing**

| Input / Output | Cost per hour [USD] |
| --- | --- |
| HD Input (AVC 10-20Mbps) | $0.234 |
| Output 1 SD (512x288, 400k) | $0.44 |
| Output 2 SD (640x360, 800k) | $0.44 |
| Output 3 SD (768x432, 1200k) | $0.44 |
| Output 4 SD (960x540, 1800k) | $0.44 |
| Output 5 HD (1280x720p, 2700k) | $0.88 |
| Output 6 HD (1920x1080p, 4100k) | $0.88 |
|  **Total:**  |  **$3.75/hour**  |

<a name="mediapackage-ingest-pricing"></a>==== AWS Elemental MediaPackage ingest pricing

As detailed in Cost Example 1, MediaPackage pricing is based on GB ingested per second across all streams of live output. Table 8 shows the conversion from kbps to Mbps to Gbits/second to GB/hour.

 **Table 8: MediaPackage ingest pricing**

| Input / output | kbps |
| --- | --- |
| Output 1 SD (512x288, 400k) | 400 |
| Output 2 SD (640x360, 800k) | 800 |
| Output 3 SD (768x432, 1200k) | 1,200 |
| Output 4 SD (960x540, 1800k) | 1,800 |
| Output 5 (1280x720p\_2700k) | 2,700 |
| Output 6 (1920x1080p\_4100k) | 4,100 |
|  **Total kbps:**  | 11,000 |
| Convert kbps to GB/hour<br />11000 kbps / 8 (bits to bytes) / 1024 (kbps to Mbps) / 1024 (Mbps to Gbps) x 60 (seconds) x 60 (minutes) | 4.83 |
| GB/hour with redundancy | 9.66 |
|  **Total (GB/hour \* $0.03)**  |  **$0.28/hour**  |

 **Table 9: MediaPackage packaging and origin pricing**

| AWS service | Cost per hour [USD] |
| --- | --- |
| Total MediaPackage with 1% of egress<br />(180 GB x $0.05) | $9.01 |

**Note**
We assume that MediaPackage serves 1% of the traffic to CloudFront and viewers, and the rest is served by CloudFront. Table 10 provides the 1% of egress for the MediaPackage estimate in Table 9.

<a name="estimate-viewer-traffic"></a>==== Estimating the viewer traffic

The cost estimate for viewer traffic assumes that all viewers get the highest bitrate for the one-hour live streaming event.

 **Table 10: Viewer traffic pricing**

| AWS service | Function | Total |
| --- | --- | --- |
| Amazon CloudFront | Average Mbps per viewer | 4.1 |
|  | Total MB per sec (10,000 x 4.1 / 8) | 5125 |
|  | Total Egress per hour ( 5125 / 1024 x 60 x 60 ) | 18,017 GB/hour |
|  |  **Total cost ** **10,240 GB \* $0.085 \+ 7,777 GB \* 0.08):**  |  **$1,531.49/hour**  |

**Note**
Pricing is per minute, with a minimum of 10 minutes. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

<a name="cost-example3"></a>==== Cost example 3

Cost example 3 covers a use case of approximately 100 viewers viewing live events for about two hundred hours every month with an HD-1080p encoding profile selected in the CloudFormation template. This cost example is based on the following factors
+ Pricing Region: US-East-1, assuming standard pricing (no free-tier or discounts).
+ Viewers consume the highest bitrate: Note that bitrate consumption is a mix of all the streams, but the highest bitrate is used in the calculation to show the upper cost range. Additionally, the QVBR and variable video complexity can result in an output bandwidth that is 10-50% lower in price than the estimate provided in Table 11.
+ 99% cache/hit ratio between the CDN and AWS Elemental MediaPackage.

**Note**
Storage of the test player is not included in this cost estimate.

Table 11summarizes the total pricing for the live streaming event. Tables 7 through 10 breaks down the cost for each AWS service.

 **Table 11: Cost breakdown for 10,000 viewers for a one-hour live event**

| AWS service | Function | Cost per 200 hours [USD] |
| --- | --- | --- |
| AWS Elemental MediaLive | Input and outputs for channel | $750.00 |
| AWS Elemental MediaPackage | Ingest of channel | $58.01 |
|  | Packaging and origination | $96.68 |
| Amazon CloudFront | Distribution | $2,934.00 |
|  |  **Total:**  |  **$3838.69/hour**  |

<a name="medialive-pricing2"></a>===== AWS Elemental MediaLive pricing

Table 12 breaks down the AWS Elemental MediaLive pricing which assumes HD AVC input and both SD and HD AVC outputs with less than 10 Mbps bit rate and less than 30 fps frame rate.

 **Table 12: MediaLive pricing**

| Input / Output | Cost per hour [USD] |
| --- | --- |
| HD Input (AVC 10-20Mbps) | $0.234 \* 200 = $46.80 |
| Output 1 SD (512x288, 400k) | $0.438 \* 200 = $87.60 |
| Output 2 SD (640x360, 800k) | $0.438 \* 200 = $87.60 |
| Output 3 SD (768x432, 1200k) | $0.438 \* 200 = $87.60 |
| Output 4 SD (960x540, 1800k) | $0.438 \* 200 = $87.60 |
| Output 5 HD (1280x720p, 2700k) | $0.882 \* 200 = $176.40 |
| Output 6 HD (1920x1080p, 4100k) | $0.882 \* 200 = $176.40 |
|  **Total:**  |  **$750 for 200 hours**  |

<a name="mediapackage-ingest-pricing"></a>===== AWS Elemental MediaPackage ingest pricing

As detailed in Cost Example 1, MediaPackage pricing is based on GB ingested per second across all streams of live output. Table13 shows the conversion from kbps to Mbps to Gbits/second to GB/hour.

 **Table 13: MediaPackage ingest pricing**

| Input / output | kbps |
| --- | --- |
| Output 1 SD (512x288, 400k) | 400 |
| Output 2 SD (640x360, 800k) | 800 |
| Output 3 SD (768x432, 1200k) | 1,200 |
| Output 4 SD (960x540, 1800k) | 1,800 |
| Output 5 (1280x720p\_2700k) | 2,700 |
| Output 6 (1920x1080p\_4100k) | 4,100 |
|  **Total kbps:**  | 11,000 |
| Convert kbps to GB/hour<br />Convert kbps to GB/200 hours (11,000 kbps / 10 (kbps to Mbps) / 1024 (Mbps to Gbps) / 8 (Gbps to GB/s) x 60 (seconds) x 60 (minutes) x 200 (hours) | 966.79 |
| GB/200 hours with redundancy | 1,933.59 |
|  **Total (GB/hour \* $0.03)**  |  **$58.01**  |

 **Table 14: MediaPackage packaging and origin pricing**

| AWS service | Cost per hour [USD] |
| --- | --- |
| Total MediaPackage with 1% of egress<br />(180 GB x $0.05) | $96.68 |

**Note**
We assume that MediaPackage serves 1% of the traffic to CloudFront and viewers, and the rest is served by CloudFront. Table 15 provides the 1% of egress for the MediaPackage estimate in Table 14.

<a name="estimate-viewer-traffic"></a>===== Estimating the viewer traffic

The cost estimate for viewer traffic assumes that all viewers get the highest bitrate for the one-hour live streaming event.

 **Table 15: Viewer traffic pricing**

| AWS service | Function | Total |
| --- | --- | --- |
| Amazon CloudFront | Average Mbps per viewer | 4.1 |
|  | Total MB per sec (10,000 x 4.1 / 8) | 51.25 |
|  | Total Egress per hour ( 5125 / 1024 x 60 x 60 ) | 36,035 GB/ 200 hours |
|  |  **Total cost (10,240 GB \* $0.085 \+ 25,795 GB) \* 0.08:**  |  **$2,934.00/ 200 hours**  |

**Note**
Pricing is per minute, with a minimum of 10 minutes. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

<a name="security"></a>== Security

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, virtualization layer, and physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

<a name="cloudfront"></a>=== Amazon CloudFront

This solution deploys a static website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To help reduce latency and improve security, this solution includes an Amazon CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to the solution’s website bucket contents. For more information, refer to [Restricting Access to Amazon S3 Content by Using an Origin Access Identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

<a name="quotas"></a>== Quotas

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

<a name="quotas-for-aws-services-in-this-solution"></a>=== Quotas for AWS services in this solution

Click one of the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

<a name="aws-cloudformation-quotas"></a>=== AWS CloudFormation quotas

Your AWS account has CloudFormation quotas that you should be aware of when launching the stack for this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, refer to [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation Users Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
