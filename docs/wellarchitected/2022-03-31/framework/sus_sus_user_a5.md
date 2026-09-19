---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_user_a5.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP04 Optimize geographic placement of workloads for user locations
<a name="sus_sus_user_a5"></a>

 Analyze network access patterns to identify where your customers are connecting from geographically. Select Regions and services that reduce the distance network traffic must travel to decrease the total network resources required to support your workload.

 ** Common anti-patterns: **
+  You select the workload's Region based on your own location.

 **Benefits of establishing this best practice:** Placing a workload close to its customers provides the lowest latency while decreasing data movement across the network and lowering environmental impact.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Select the Regions for your workload deployment based on the following key elements:
  +  **Your Sustainability goal:** as explained in [Region selection](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/region-selection.html).
  +  **Where your data is located:** For data-heavy applications (such as big data and machine learning), application code should execute as close to the data as possible.
  +  **Where your users are located:** For user-facing applications, choose a Region close to your workload’s customer base.
  + **Other constraints:** Consider constraints such as security and compliance as explained in [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/).
+  Use [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to run workloads like video rendering and graphics-intensive virtual desktop applications. Local Zones allow you to benefit from having compute and storage resources closer to end users.
+  Use local caching or [AWS Caching Solutions](https://aws.amazon.com/caching/aws-caching/) for frequently used resources to improve performance, reduce data movement, and lower environmental impact.

<table>
<thead>
  <tr><th>Service</th><th>When to use</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://aws.amazon.com/cloudfront/">Amazon CloudFront</a></td><td>Use to cache static content such as images, scripts, and videos, as well as dynamic content such as API responses or web applications.</td></tr>
  <tr><td><a href="https://aws.amazon.com/elasticache/">Amazon ElastiCache</a></td><td>Use to cache content for web applications.</td></tr>
  <tr><td><a href="https://aws.amazon.com/dynamodb/dax/">DynamoDB Accelerator</a></td><td>Use to add in-memory acceleration to your DynamoDB tables.</td></tr>
</tbody>
</table>

+  Use services that can help you run code closer to users of your workload:

<table>
<thead>
  <tr><th>Service</th><th>When to use</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://aws.amazon.com/lambda/edge/">Lambda@Edge</a></td><td>Use for compute-heavy operations that are executed when objects are not in the cache. </td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html">Amazon CloudFront Functions</a></td><td>Use for simple use cases like HTTP(s) request or response manipulations that can be executed by short-lived functions.</td></tr>
  <tr><td><a href="https://aws.amazon.com/greengrass/">AWS IoT Greengrass</a></td><td>Use to run local compute, messaging, and data caching for connected devices. </td></tr>
</tbody>
</table>

+  Use connection pooling to enable connection reuse, and reduce required resources.
+  Use distributed data stores that don’t rely on persistent connections and synchronous updates for consistency to serve regional populations.
+  Replace pre-provisioned static network capacity with shared dynamic capacity, and share the sustainability impact of network capacity with other subscribers.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimizing your AWS Infrastructure for Sustainability, Part III: Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/)
+  [Amazon ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/index.html)
+  [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+  [Amazon CloudFront Key Features](https://aws.amazon.com/cloudfront/features/)
+  [Lambda@Edge](https://aws.amazon.com/lambda/edge/)
+  [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)
+ [AWS IoT Greengrass](https://aws.amazon.com/greengrass/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)

 **Related examples:**
+  [AWS Networking Workshops](https://catalog.workshops.aws/networking/en-US)
