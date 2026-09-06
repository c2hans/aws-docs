---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/aws-lambda-quotas.html
---

# AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

Lambda has a 6 MB invocation payload request and response limit. For information about Lambda quotas, including the amount of compute and storage resources that you can use to run and store functions, refer to [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda Developer Guide*.

The default Lambda architecture does not support image responses larger than 6 MB. To process larger images, use the ECS architecture, which supports image responses up to 100 MB. The S3 Object Lambda option has been deprecated and is no longer available to new customers as of November 7, 2025; only customers who were already using S3 Object Lambda before that date can continue to enable it. For more information, refer to [Choosing an Architecture](choosing-deployment-architecture.md).
