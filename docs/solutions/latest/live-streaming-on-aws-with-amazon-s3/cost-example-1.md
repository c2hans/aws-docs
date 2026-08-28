---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/cost-example-1.html
---

# Cost example 1
<a name="cost-example-1"></a>

Cost example 1 covers a use case of approximately 1,000 viewers viewing a live event for about one hour with a **SD-540p** encoding profile selected in the CloudFormation template. This cost example is based on the following factors:
+ Pricing Region: US-East-1, assuming standard pricing (no free-tier or discounts).
+ Viewers consume the highest bitrate: While bitrate consumption is a mix of all the streams, we used the highest bitrate in the calculation to show the upper cost range. Additionally, the [Quality-Defined Variable Bitrate](https://aws.amazon.com/media/tech/quality-defined-variable-bitrate-qvbr/) (QVBR) and variable video complexity can result in an output bandwidth that is 10-50% lower in price than the estimate provided in Table 1.
+ 99% cache/hit ratio between the content delivery network (CDN) and Amazon S3.

**Note**
Storage of the test player is not included in this cost estimate.

Table 1 summarizes the total pricing for the live streaming event. Tables 2 through 4 breaks down the cost for each AWS service.

 **Table 1: Cost breakdown for 1,000 viewers for a one-hour live event**

| AWS service | Function | Cost per hour [USD] |
| --- | --- | --- |
|  **AWS Elemental MediaLive**  | Input and outputs for channel | $1.71 |
|  **Amazon S3**  | Storage | $0.01 |
|  | Requests | $0.04 |
|  **Amazon CloudFront**  | Distribution | $67.24 |
|  |  **Total:**  | $69.00 |

## AWS Elemental MediaLive pricing
<a name="aws-elemental-medialive-pricing"></a>

Table 2 breaks down the MediaLive pricing which assumes HD AVC input and SD AVC outputs with less than 10 Mbps bitrate and less than 30 frames per second (fps) frame rate.

 **Table 2: MediaLive pricing**

| Input / output | Cost per hour [USD] |
| --- | --- |
|  **HD Input (AVC 10-20Mbps)**  | $0.294 |
|  **Output 1 SD (512x288, 400k)**  | $0.354 |
|  **Output 2 SD (640x360, 800k)**  | $0.354 |
|  **Output 3 SD (768x432, 1,200k)**  | $0.354 |
|  **Output 4 SD (960x540, 1,800k)**  | $0.354 |
|  **Total:**  | $1.71 |

## Amazon S3 pricing
<a name="amazon-s3-pricing"></a>

Amazon S3 charges $0.023 per Gigabyte (GB) per month for the first 50 Terabytes (TB) stored in the bucket. The volume of storage billed in a month is based on the average storage used throughout the month. This can be determined by size of objects and how long they are stored. For this example, 21 segments for 4 bitrates are stored at all times. The cost of storage per hour is as follows:

1. Add the bitrate of all streams in Kbps:
   + 400k \+ 800k \+ 1,200k \+ 1,800k = 4,200 Kbps

1. Calculate size of four-second segment (for all bitrates combined):
   + 4,200 Kbps \* 4 seconds = 16,800 Kb

1. Total size of segments stored at a time:
   + 16,800 Kb \* 21 segments = 352,800 Kb

1. Total Kb-hour usage:
   + 352,800 Kb \* 1 hour storage = 352,800 Kb-hours

1. Convert to GB-months:
   + 352,800 Kb-hours / 8 bits per byte / 1,000,000 Kb per GB / 744 hours in month = 0.00006 GB-months

 **0.00006 GB-months \* $0.023 = $0.000001 per hour of storage**

The cost will continue to accumulate per hour as long as the objects are not removed from the bucket. Cost of storage is billed monthly.

 **Table 3: Amazon S3 storage pricing**

| Input / output | Kbps |
| --- | --- |
|  **Output 1 SD (512x288, 400k)**  | 400 |
|  **Output 2 SD (640x360, 800k)**  | 800 |
|  **Output 3 SD (768x432, 1,200k)**  | 1,200 |
|  **Output 4 SD (960x540, 1,800k)**  | 1,800 |
|  **Total Kbps:**  | 4,200 |
|  **Compute total Kb stored** <br /> **4200 kbps \* 4 seconds \* 21 segments**  | 352,800 Kb |
|  **GB-month usage for one hour**  | 0.00006 GB |
|  **Cost (GB/hour \*$0.023)**  | $0.000001/hour |

Amazon S3 charges $0.005 per 1,000 requests for PUT, COPY, POST, and LIST requests. This example has four input streams, so the number of requests can be approximated by the following:

1. Calculate the number of segments:
   + 3,600 seconds of content / 4 second segments = 900 segments
   + 900 segments \* 4 input streams = 3,600 segments

1. Calculate the number of manifest updates:
   + 4 input streams \* 3,600 seconds of content / updates every 4 seconds = 3,600 manifest updates

1. Add total segments to total manifest updates to get the number of PUT requests:
   + 3,600 \+ 3,600 = 7,200 PUT requests per hour

 **Table 4: Amazon S3 request pricing**

| Request | Quantity |
| --- | --- |
|  **PUT ts segments**  | 3,600 |
|  **PUT manifest files**  | 3,600 |
|  **Total requests:**  | 7,200 |
|  **Cost (total requests/1000 \* $0.005)**  | $0.036/hour |

Data transfers from S3 to Amazon CloudFront are free of charge.

## Viewer traffic pricing
<a name="viewer-traffic-pricing"></a>

The cost estimate for viewer traffic assumes that all viewers get the highest bitrate for the one-hour live streaming event.

 **Table 5: Viewer traffic pricing**

| AWS service | Function | Cost per hour [USD] |
| --- | --- | --- |
|  **Amazon CloudFront**  | Average Mbps per viewer | 1.8 |
|  | Total MB per second (1,000 x 1.8 / 8) | 225 |
|  | Total egress per hour ( 225 / 1,024 x 60 x 60 ) | 791 GB/hour |
|  |  **Total (791 GB \* $0.085):**  | $67.24 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
