---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-speed-comparison.html
---

# Using the Amazon S3 Transfer Acceleration Speed Comparison tool
<a name="transfer-acceleration-speed-comparison"></a>

You can use the [Amazon S3 Transfer Acceleration Speed Comparison tool](https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html) to compare accelerated and non-accelerated upload speeds across Amazon S3 Regions. The Speed Comparison tool uses multipart uploads to transfer a file from your browser to various Amazon S3 Regions with and without using Transfer Acceleration.

You can access the Speed Comparison tool by using either of the following methods:
+ Copy the following URL into your browser window, replacing `{{region}}` with the AWS Region that you are using (for example, `us-west-2`) and `{{{{amzn-s3-demo-bucket}}}}` with the name of the bucket that you want to evaluate:

  `https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html?region={{region}}&origBucketName={{{{amzn-s3-demo-bucket}}}}`

  For a list of the Regions supported by Amazon S3, see [Amazon S3 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *AWS General Reference*.
+ Use the Amazon S3 console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
