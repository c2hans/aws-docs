---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/additional-aws-service-logs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Additional AWS Service Logs
<a name="additional-aws-service-logs"></a>

Although application and operating system monitoring can give a focused view on how an application is behaving, sometimes it’s necessary to monitor the wider environment of AWS services.

[Amazon VPC](https://aws.amazon.com/vpc) Flow Logs allow you to monitor IP traffic for your AWS resources. Flow Logs creates logs for network traffic going in and out of your VPC networks. For each flow log, you can choose to filter the traffic it records and also choose to store the logs in Amazon CloudWatch or S3. Flow logs are useful for troubleshooting a number of networking issues, such as overly-restrictive security group rules, and can also be used to audit the traffic passing through the network.

Closely related to Flow Logs, [Amazon Route 53 Query Logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-monitoring.html) can track queries for DNS public hosted zones and can send logs to CloudWatch Logs.

When running .NET applications on EC2 instances or in containers, Elastic Load Balancing allows you to spread load across multiple instances, letting your application scale and letting you take advantage of elasticity. You can use ELB Access Logs to monitor HTTP/HTTPS traffic to Application Load Balancers and TCP traffic to Network Load Balancers. Logs are captured as compressed files and stored in an S3 bucket, and can be used to analyze traffic patterns and troubleshoot load-balancing issues.

For high volume ASP.NET websites with a global presence, it’s a common requirement to reduce load on the web servers. The Amazon CloudFront Content Delivery Network helps by moving static content closer to users, tracking detailed information about every request, and storing the resulting logs in an S3 bucket.

For applications that need to store or share files, S3 provides a simple service to store and serve objects at scale. You can use [S3 Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html) to track access requests to your S3 buckets for troubleshooting and security audit purposes.
