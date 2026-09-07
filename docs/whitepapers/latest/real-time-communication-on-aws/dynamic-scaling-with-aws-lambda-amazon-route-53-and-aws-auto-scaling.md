---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/dynamic-scaling-with-aws-lambda-amazon-route-53-and-aws-auto-scaling.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Dynamic scaling with AWS Lambda, Amazon Route 53, and Amazon EC2 Auto Scaling
<a name="dynamic-scaling-with-aws-lambda-amazon-route-53-and-aws-auto-scaling"></a>

AWS allows the chaining of features and the ability to incorporate custom serverless functions as a service based on infrastructure events. One such design pattern that has many versatile uses in RTC applications is the combination of automatic scaling lifecycle hooks with [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html), Amazon Route 53, and [AWS Lambda](https://aws.amazon.com/lambda/) functions. AWS Lambda functions can embed any action or logic. The following figure demonstrates how these features chained together can enhance system reliability and scalability with automation.

![A diagram depicting automatic scaling with dynamic updates to Amazon Route 53 .](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/auto-scaling-dynamic-updates.jpg)
