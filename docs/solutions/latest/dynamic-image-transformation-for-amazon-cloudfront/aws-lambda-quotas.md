---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/aws-lambda-quotas.html
---

# AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

Lambda has a 6 MB invocation payload request and response limit. For information about Lambda quotas, including the amount of compute and storage resources that you can use to run and store functions, refer to [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda Developer Guide*.

The default architecture for this solution does not support image responses larger than 6 MB, to allow for this functionality, use the S3 Object Lambda architecture by setting the Enable S3 Object Lambda template parameter to Yes. For more information, refer to .
