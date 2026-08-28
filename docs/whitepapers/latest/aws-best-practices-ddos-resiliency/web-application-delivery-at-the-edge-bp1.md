---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/web-application-delivery-at-the-edge-bp1.html
---

# Web application delivery at the edge (BP1)
<a name="web-application-delivery-at-the-edge-bp1"></a>

 You can use Amazon CloudFront to deliver your entire website including static, dynamic, streaming, and interactive content. Persistent connections and variable time-to-live (TTL) settings can be used to offload traffic from your origin, even if you aren't serving cacheable content. Use of these CloudFront features reduces the number of requests and TCP connections back to your origin, helping protect your web application from HTTP floods.

 CloudFront only accepts well-formed connections, which helps prevent many common DDoS attacks, such as SYN floods and UDP reflection attacks, from reaching your origin. DDoS attacks are also geographically isolated close to the source, which prevents the traffic from impacting other locations. These capabilities can greatly improve your ability to continue serving traffic to users during large DDoS attacks. You can use CloudFront to protect an origin on AWS or elsewhere on the internet.

 If you're using [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) to serve static content on the internet, AWS recommends you use Amazon CloudFront to protect your bucket providing the following benefits:
+  Restricts access to the Amazon S3 bucket so that it's not publicly accessible.
+  Helps ensure sure that viewers (users) can access the content in the bucket only through the specified CloudFront distribution—that is, prevents them from accessing the content directly from the bucket.
+  Lower latency for end users by serving content from edge locations closer to them.
+  Reduced cost for requests to S3 origins (data transfer from S3 to CloudFront is free).

 To achieve this, configure CloudFront to send authenticated requests to Amazon S3, and configure Amazon S3 to only allow access to authenticated requests from CloudFront. CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). We recommend using OAC because it supports:
+  All Amazon S3 buckets in all AWS Regions, including opt-in Regions launched after December 2022
+  Amazon S3 [server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) with AWS KMS (SSE-KMS)
+  Dynamic requests (`PUT` and `DELETE`) to Amazon S3

 For more information about OAC and OAI, see [Restricting access to Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

 For more information about protecting and optimizing the performance of web applications with Amazon CloudFront, see [Getting Started with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html) and the diagram in Mitigation Techniques.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
