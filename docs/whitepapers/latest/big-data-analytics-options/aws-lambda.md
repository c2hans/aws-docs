---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/aws-lambda.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Lambda
<a name="aws-lambda"></a>

 [AWS Lambda](https://aws.amazon.com/lambda/) enables you to run code without provisioning or managing servers. You pay only for the compute time you consume – there is no charge when your code is not running. With Lambda, you can run code for virtually any type of application or backend service – all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

## Ideal usage patterns
<a name="ideal-usage-patterns-lambda"></a>

 AWS Lambda enables you to run code in response to triggers such as changes in data, shifts in system state, or actions by users. Lambda can be directly triggered by AWS services such as [Amazon S3](https://aws.amazon.com/s3/), [DynamoDB](https://aws.amazon.com/dynamodb/), [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS), and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), enabling you to build a variety of real-time data processing systems:
+  **Real-time file processing –** You can trigger Lambda to invoke a process where a file has been uploaded to Amazon S3 or modified. For example, to change an image from color to gray scale after it has been uploaded to Amazon S3.
+  **Real-time stream processing** – You can use Kinesis Data Streams and Lambda to process streaming data for click stream analysis, log filtering, and social media analysis.
+  **Extract, transform, load** **(ETL)** – You can use Lambda to run code that transforms data and loads that data into one data repository to another.
+  **Replace Cron** – Use schedule expressions to run a Lambda function at regular intervals as a cheaper and more available solution than running cron on an EC2 instance.
+  **Process AWS Events** – Many other services, such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), can act as event sources simply by logging to Amazon S3 and using S3 bucket notifications to trigger Lambda functions.

## Cost model
<a name="cost-model-lambda"></a>

 With AWS Lambda you only pay for what you use. You are charged based on the number of requests for your functions and the time your code runs. The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month. You are charged $0.20 per 1 million requests thereafter ($0.0000002 per request). Additionally, the duration of your code running is priced in relation to memory allocated. You are charged $0.00001667 for every GB-second used.

See [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) for more details.

## Performance
<a name="performance-lambda"></a>

After deploying your code into Lambda for the first time, your functions are typically ready to call within seconds of upload. Lambda is designed to process events within milliseconds. Latency will be higher immediately after a Lambda function is created, updated, or if it has not been used recently. To improve performance, Lambda may choose to retain an instance of your function and reuse it to serve a subsequent request, rather than creating a new copy.

The Lambda [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) feature provides customers greater control over performance of their serverless applications at any scale. Functions using provisioned concurrency run with consistent start-up latency, making them ideal for building interactive mobile or web backends, latency sensitive microservices, and synchronously invoked APIs. With provisioned concurrency, functions can instantaneously serve a burst of traffic with consistent start-up latency for every invoke up to the specified scale.

To learn more about how Lambda reuses function instances, see [Getting started with Lambda](http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html). Your code should not assume that this reuse will always happen.

## Durability and availability
<a name="durability-and-availability-lambda"></a>

 AWS Lambda is designed to use replication and redundancy to provide high availability for both the service itself and for the Lambda functions it operates. There are no maintenance windows or scheduled downtimes for either. On failure, Lambda functions being invoked synchronously respond with an exception. Lambda functions being invoked asynchronously are retried at least three times, after which the event may be rejected.

## Scalability and elasticity
<a name="scalability-and-elasticity-lambda"></a>

There is no limit on the number of Lambda functions that you can run. However, Lambda has a default safety throttle of 1,000 concurrent runs per account per Region. A member of the AWS support team can increase this limit. Lambda is designed to scale automatically on your behalf. There are no fundamental limits to scaling a function. Lambda dynamically allocates capacity to match the rate of incoming events.

## Interfaces
<a name="interfaces-lambda"></a>

 Lambda functions can be managed in a variety of ways. You can easily list, delete, update, and monitor your Lambda functions using the dashboard in the Lambda console. You also can use the AWS CLI and AWS SDK to manage your Lambda functions.

 You can trigger a Lambda function from an AWS event, such as Amazon S3 bucket notifications, Amazon DynamoDB Streams, Amazon CloudWatch logs, [Amazon Simple Email Service](https://aws.amazon.com/ses/) (Amazon SES), Amazon Kinesis Data Streams, Amazon SNS, [Amazon Cognito](https://aws.amazon.com/cognito/), and more. Any API call in any service that supports AWS CloudTrail can be processed as an event in Lambda by responding to CloudTrail audit logs. For more information about event sources, see [Lambda Event Sources](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-event-sources.html).

 AWS Lambda supports code written in Node.js (JavaScript), Python, Java (Java 8 compatible), C\# (.NET Core), Go, PowerShell and Ruby. Your code can include existing libraries, even native ones. See AWS documentation on using [Node.js](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-create-deployment-pkg.html), [Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html), [Java](https://docs.aws.amazon.com/lambda/latest/dg/lambda-java-how-to-create-deployment-package.html), [C\#](https://docs.aws.amazon.com/lambda/latest/dg/lambda-csharp.html), [Go](https://docs.aws.amazon.com/lambda/latest/dg/lambda-golang.html), [PowerShell](https://docs.aws.amazon.com/lambda/latest/dg/powershell-programming-model.html), and [Ruby](https://aws.amazon.com/developers/getting-started/ruby/).

You can package your Lambda function code and dependencies as a container image, using tools such as the Docker CLI. You can then upload the image to your container registry hosted on Amazon ECR. Note that you must create the Lambda function from the same account as the container registry in Amazon ECR.

## Anti-patterns
<a name="anti-patterns-lambda"></a>

AWS Lambda has the following anti-patterns:
+  **Long running application** — Each Lambda function must complete within 900 seconds. For long running applications that may require jobs to run longer than fifteen minutes, Amazon EC2, Amazon EKS, or Amazon ECS is recommended. Alternately, you can use [Step Functions](https://aws.amazon.com/step-functions/).
+  **Dynamic websites** — While it is possible to run a static website with AWS Lambda, running a highly dynamic and large volume website can be performance prohibitive. Utilizing Amazon EC2, Amazon EKS, or Amazon ECS and AWS CloudFormation is a recommended use-case.
+  **Stateful applications** — Lambda code must be written in a “stateless” style, meaning it should assume there is no affinity to the underlying compute infrastructure. Local file system access, child processes, and similar artifacts may not extend beyond the lifetime of the request, and any persistent state should be stored in Amazon S3, DynamoDB, or another internet-available storage service.
