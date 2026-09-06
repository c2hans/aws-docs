---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/cloudfront-prerequisites.html
---

# CloudFront prerequisites
<a name="cloudfront-prerequisites"></a>

 The Secure Media Delivery at the Edge on AWS solution has been designed to enhance the security of an existing video streaming workload that already utilizes CloudFront for content distribution to the viewers. As you prepare to integrate the solution into your architecture, the following requirements and preceding steps must be reviewed before activating the solution for your workloads.

 **At the video origin level:**

 The only requirement that must be met in terms of configuration of your video at origin which produces media segments and corresponding manifest files is to ensure that all media objects that need to be protected by secure tokens, are referenced in the video manifest with a relative rather than absolute path. This solution operates on the basis of inserting a token at the beginning of the playback URL path and the assertion that client’s player will repeat the token when subsequent elements that need to be processed are relative to the same root of the path, which is an inserted viewer token. Most of the video originating services compose the media manifest in that way. Once you confirm this also applies for your workload, proceed with the next steps to integrate the solution. If all or some of the objects in the manifest use absolute paths, which would override the token part when player makes a request for it, you must change your video origin configuration to replace absolute paths with relative paths. If this is not possible for all the objects, you can also exclude these specific objects from token validation step with the right adjustments in the CloudFront distribution configuration.

 **At the CloudFront distribution level:**

 In the existing CloudFront distributions used for the delivery of original video content, you must verify the following before you integrate this solution.
+  Do the path patterns defined in cache behaviors match request URLs after you start inserting the access tokens? Comparing the URL path for the same object before and after secure tokens are added, you will find that a token appears as abstracted top-level directory in the URL path referencing video objects.
  +  Before adding token: https://d1234.cloudfront.net/video\_path\_top\_dir/video\_path\_subdir/object
  +  After adding the token: https://d1234.cloudfront.net/**token**/video\_path\_top\_dir/video\_path\_subdir/object

 When verified against CloudFront distribution configuration, make sure that after token insertion appropriate cache behaviors match modified URL path including unique token values. Cache behavior requires the use of a wildcard at the beginning of the URL path pattern to match the arbitrary token value included in each request. In a common configuration in which you separate cache behavior for manifest files and video segments would like this:

![Screenshot of cache behavior - wildcard .](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image8.png)

 That configuration requires no changes in the path pattern definition as preceding wildcard covers additional path component introduced by token presence. However, if you have more explicit path pattern definitions (for example, when you run multiple streaming channels), your cache behaviors configuration may resemble this:

![Screenshot of cache behavior – explicit path pattern.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image9.png)

 In that scenario, requests originated from the viewers with token included will not match with any of the listed cache behaviors as it starts with a fixed path pattern that does not accommodate part of an arbitrary token value at the beginning of the path. To change that, referenced path patterns can be modified as follows:

![Screenshot of cache behavior – non-fixed path pattern.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image10.png)

+  Because the token validation logic is operated by CloudFront Functions code generated as one of the solution resources, before that function can be associated with viewer request triggers for the appropriate cache behaviors, you must make sure there is no Lambda@Edge function associated with either viewer request or viewer response triggers for the same set of cache behaviors. It is not possible to combine Lambda@Edge and CloudFront Functions associations for the same cache behavior.
+  If you plan to leverage the session revocation feature offered by the solution, an AWS WAF web ACL must be created first and associated with the CloudFront distribution that will be integrated with the solution. If you run multiple CloudFront distributions that require token-based protection and session revocation capability, we recommend you run multiple stacks of the solution and associate created WAF rule group with separate AWS WAF web ACL dedicated for each distribution. This ensures efficient use of WAF Capacity Units (WCU) as each rule group will only store the sessions that are in use for a given distribution.
+  Integrating your video streaming CloudFront distribution with auto session revocation requires additional steps to make the detail about all the incoming request accessible for Athena to distill suspicious sessions. Activating CloudFront access logs is the first step which delivers log files to the S3 bucket of your choice. For Athena to be able to run queries against these log files it needs additional metadata that will instruct how to parse and interpret log files, and also how to map column names to specific fields. You must define that information by creating database and table definitions in AWS Glue Data catalog. Refer to [Querying Amazon CloudFront logs](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html) for a basic use case and additional information.
