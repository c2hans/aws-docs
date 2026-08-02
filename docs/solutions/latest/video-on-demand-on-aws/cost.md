---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution, which can vary based on the following factors:
+ The size of your videos.
+ The number of outputs created.
+ The number of views the published content receives through CloudFront.

  MediaConvert composes the majority of the cost. For more information about MediaConvert pricing, refer to [MediaConvert Pricing](https://aws.amazon.com/mediaconvert/pricing/).

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](architecture-details.md#aws-services-in-this-solution).

## Example cost for a 60-minute source video
<a name="example-cost-for-a-60-minute-source-video"></a>

As of this revision, the estimated cost for using this solution with the default encoding settings to process a 60-minute source video in the US East (N. Virginia) Region is approximately **$4.23**. This estimate may vary depending on the source video size and format. The following test was run with a 1080p 60-minute input video file. This does not include Amazon S3 storage costs, which vary depending on input file size. 4K video input will increase costs.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| AWS Elemental MediaConvert | Output profile: AVC code 1 pass quality 30 fps | $ 4.23 |
| Amazon CloudFront | Using the price of $0.085 per GB for CloudFront. A 60-minute video with the default job settings streamed to 1,000 users would cost approximately:<br />0.75 MB/s \* 1000 users \* 3600 seconds \~= 2700 GB/hour.<br />2700 GB/hour \* $0.085 = $229.50 an hour | $ 229.50 |
| AWS Step Functions | Free tier cost is negligible even beyond free tier | $ 0.00 |
| AWS Lambda | A 60-minute video will invoke around 24 lambda functions. When all free tier is used up, $0.0000002 \* 24 requests = $0.0000048 | $ 0.0000048 |
| Amazon S3 | A 60-minute video will at most use 9GB of storage on S3 depending on the complexity of the video content. $0.023 per GB \* 9GB = $0.207. | $ 0.21 |
| Amazon DynamoDB | Free tier. Cost is negligible even beyond free tier | $ 0.00 |
| Amazon CloudWatch | Free tier. Cost is negligible even beyond free tier | $ 0.00 |
| Amazon Simple Queue Service (Amazon SQS) | Free tier. Cost is negligible even beyond free tier | $ 0.00 |
| Amazon Simple Notification Service (Amazon SNS) | Free tier. Cost is negligible even beyond free tier | $ 0.00 |
|  |  **Total:**  |  **$ 233.94**  |
|  | (Optional) AWS Elemental MediaPackage | $ 0.05 |

The following table lists the professional tier costs for the MediaConvert settings used in this example:

| Output | Cost [USD] |
| --- | --- |
| SD resolution | $ 0.0075/min |
| HD resolution | $ 0.024/min |

Output with calculations:

HLS profile: 3 SD and 2 HD (3 x 60 x $ 0.0075) \+ (2 x 60 x $ 0.024)

Total cost = $ 1.35 \+ $ 2.88 = **$ 4.23**

The costs for CloudFront and Amazon S3 storage varies depending on the number and format of outputs created and the number of requests to view the content delivered through CloudFront. To calculate your average cost, use the data size of your output multiplied by the average number of viewers for your stream.
