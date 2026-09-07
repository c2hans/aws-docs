---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/error-handling.html
---

# Error handling
<a name="error-handling"></a>

The ingest, processing, and publishing workflow AWS Lambda functions, and Amazon CloudWatch Events are configured to invoke an *error handler* Lambda function that updates the Amazon DynamoDB table with error message details, and sends an Amazon Simple Notification Service (Amazon SNS) notification to a subscribed email address.

 **Video on demand solution error handling overview**

![video on demand error handling](https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/video-on-demand-error-handling.png)
