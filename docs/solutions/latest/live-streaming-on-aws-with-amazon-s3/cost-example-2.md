---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/cost-example-2.html
---

# Cost example 2
<a name="cost-example-2"></a>

Cost example 2 covers a use case of approximately 10,000 viewers viewing a live event for about one hour with an **HD-1080p** encoding profile selected in the CloudFormation template. This cost example is based on the following factors:
+ Pricing Region: US-East-1, assuming standard pricing (no free-tier or discounts).
+ Viewers consume the highest bitrate: Note that bitrate consumption is a mix of all the streams, but the highest bitrate is used in the calculation to show the upper cost range. Additionally, the QVBR and variable video complexity can result in an output bandwidth that is 10-50% lower in price than the estimate provided in Table 6.
+ 99% cache/hit ratio between the CDN and Amazon S3.

 **Note:** Storage of the test player is not included in this cost estimate.

Table 6 summarizes the total pricing for the live streaming event. Tables 7 through 10 break down the cost for each AWS service.

 **Table 6: Cost breakdown for 10,000 viewers for a one-hour live event**

| AWS service | Function | Cost per hour [USD] |
| --- | --- | --- |
|  **AWS Elemental MediaLive**  | Input and outputs for channel | $3.11 |
|  **Amazon S3**  | Storage | $0.01 |
|  | Requests | $0.06 |
|  **Amazon CloudFront**  | Distribution | $1,531.49 |
|  |  **Total:**  | $1,534.67 |

## AWS Elemental MediaLive pricing
<a name="aws-elemental-medialive-pricing-1"></a>

Table 7 breaks down the MediaLive pricing which assumes HD AVC input and both SD and HD AVC outputs with less than 10 Mbps bit rate and less than 30 fps frame rate.

 **Table 7: MediaLive pricing**

| Input / output | Cost per hour [USD] |
| --- | --- |
|  **HD Input (AVC, 10-20Mpbs)**  | $0.294 |
|  **Output 1 SD (512x288, 400k)**  | $0.354 |
|  **Output 2 SD (640x360, 800k)**  | $0.354 |
|  **Output 3 SD (768x432, 1,200k)**  | $0.354 |
|  **Output 4 SD (960x540, 1,800k)**  | $0.354 |
|  **Output 5 HD (1280x720p, 2,700k)**  | $0.702 |
|  **Output 6 HD (1920x1080p, 4,100k)**  | $0.702 |
|  **Total:**  | $3.11 |

## Amazon S3 pricing
<a name="amazon-s3-pricing-1"></a>

As detailed in Cost Example 1, Amazon S3 pricing is based on GB of storage per month. Table 8 shows the conversion from Kbps to Kb stored to GB/month usage to get the total GB of storage for the hour-long stream.

 **Table 8 : Amazon S3 storage pricing**

| Input / output | Kbps |
| --- | --- |
|  **Output 1 (512x288\_400k)**  | 400 |
|  **Output 2 (640x360\_800k)**  | 800 |
|  **Output 3 (768x432\_1,200k)**  | 1,200 |
|  **Output 4 (960x540\_1,800k)**  | 1,800 |
|  **Output 5 (1280x720p\_2,700k)**  | 2,700 |
|  **Output 6 (1920x1080p\_4,100k)**  | 4,100 |
|  **Total Kbps**  | 11,000 |
|  **Compute total Kb stored** <br /> **11,000 Kbps \* 4 seconds \* 21 segments**  | 924,000 Kb |
|  **GB-month usage for one hour** <br /> **924,000 Kb-hours / 8 bits per byte / 1,000,000 Kb per GB / 744 hours**  | 0.0002 |
|  **Total (GB/hour \* $0.023)**  | $ 0.000005 |

 **Table 9: Amazon S3 request pricing**

| Request | Quantity |
| --- | --- |
|  **PUT ts segments**  | 5,400 |
|  **PUT manifest files**  | 5,400 |
|  **Total requests:**  | 10,800 |
|  **Cost (total requests/1000 \* $0.005)**  | $0.054/hour |

## Estimating the viewer traffic
<a name="estimating-the-viewer-traffic"></a>

The cost estimate for viewer traffic assumes that all viewers get the highest bitrate for the one-hour live streaming event.

 **Table 10: Viewer traffic pricing**

| AWS service | Function | Total |
| --- | --- | --- |
|  **Amazon CloudFront**  | Average Mbps per viewer | 4.10 |
|  | Total MB per sec (10,000 x 4.1 / 8) | 5,125 |
|  | Total egress per hour (5,125 / 1,024 x 60 x 60) | 18,017 GB/hour |
|  |  **Total cost (18,017 GB \*$0.085):**  | $1,531.49 |

**Note**
Pricing is per minute, with a minimum of 10 minutes. Prices are subject to change.
