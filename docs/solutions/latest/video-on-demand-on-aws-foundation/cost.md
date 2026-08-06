---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this solution. The total cost for running this solution depends on the size of your videos, the number of outputs created, and the number of views the published content receives through CloudFront. After encoding all of your videos with this solution, the monthly cost will be for Amazon S3 storage, and any CloudFront costs from streaming your new video content to users.

 As of this revision, the estimated cost of running this solution for a 60-minute video with the dimensions listed in the following table, in the US East (N. Virginia) Region, is approximately **$232.86 per month per job**.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)  through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](architecture-details.md#aws-services-in-this-solution).

## Cost table for a 60-minute source video
<a name="cost-table-for-a-60-minute-source-video"></a>

 The following table provides a sample cost breakdown for processing a 60-minute source video using the solution deployed with the default parameters in the US East (N. Virginia) Region.

<table>
<thead>
  <tr><th> AWS service </th><th> Dimensions </th><th> Cost [USD] </th></tr>
</thead>
<tbody>
  <tr><td> Amazon CloudFront </td><td> Using the price of $0.085 per GB for CloudFront, a 60-minute video with the default job settings streamed to 1,000 users would cost approximately: <br /> *0.75 MB/s × 1000 users × 3600 seconds = 2700 GB/hour* <br /> *2700 GB/hour × $0.085 per GB = $229.50 an hour* </td><td> $229.50 </td></tr>
  <tr><td> Amazon S3 </td><td> A 60-minute video uses a maximum of 9 GB of storage on Amazon S3, depending on the complexity of the video content. <br /> *$0.023 per GB × 9 GB = $0.207*  Source videos uploaded to Amazon S3 add to this cost. After MediaConvert processing, delete source content from Amazon S3 to reduce storage costs. </td><td> $0.207 </td></tr>
  <tr><td> AWS Lambda </td><td> 4 Lambda requests per file using $0.20 per million requests <br /> *$0.0000002 × 4 requests = $0.0000008* </td><td> $0.0000008 </td></tr>
  <tr><td> Amazon CloudWatch </td><td> [AWS Free Tier](https://aws.amazon.com/free/). [See Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) for more information. </td><td> $0.00 </td></tr>
  <tr><td>Amazon EventBridge</td><td> [AWS Free Tier](https://aws.amazon.com/free/). [See Amazon EventBridge Pricing](https://aws.amazon.com/eventbridge/pricing/) for more information. </td><td> $0.00 </td></tr>
  <tr><td> Amazon SNS </td><td> [AWS Free Tier](https://aws.amazon.com/free/). See [Amazon SNS Pricing](https://aws.amazon.com/sns/pricing/) for more information. </td><td> $0.00 </td></tr>
  <tr><td> AWS Elemental MediaConvert </td><td> HLS output profile: +   3 SD resolution at 30 fps or less  <br />+   2 HD resolution at 30 fps or less  </td><td> $3.15 </td></tr>
  <tr><td colspan="2"> Total: </td><td> $232.86 </td></tr>
</tbody>
</table>

## MediaConvert cost
<a name="mediaconvert-cost"></a>

 A significant cost of running this solution comes from MediaConvert. This section breaks down the MediaConvert costs for the sample 60-minute source video.

 The video outputs in the [Cost table for a 60-minute source video](#cost-table-for-a-60-minute-source-video) use the following Basic tier MediaConvert settings:
+  AVC codec
+  1 pass quality
+  30 fps

 This solution's CloudFormation template creates a destination S3 bucket where the processed videos are stored. The solution stores each processed result in a folder with the same name as the process ID. Pricing increases when using higher frame rates than 30 fps. For more information about MediaConvert pricing, refer to [AWS Elemental MediaConvert Pricing](https://aws.amazon.com/mediaconvert/pricing/).
