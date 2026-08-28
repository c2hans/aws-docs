---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/cdns.html
---

# Working with AWS Elemental MediaPackage and CDNs
<a name="cdns"></a>

You can use a content delivery network (CDN) such as [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) to serve the content that you store in AWS Elemental MediaPackage. A CDN is a globally distributed set of servers that caches content such as videos. When a user requests your content, the CDN routes the request to the edge location that provides the lowest latency. If your content is already cached in that edge location, the CDN delivers it immediately. If your content is not currently in that edge location, the CDN retrieves it from your origin (in this case, the MediaPackage endpoint) and distributes it to the user. The following illustration shows this process.

![This illustration shows how content that's stored in MediaPackage is distributed using a CDN.](http://docs.aws.amazon.com/mediapackage/latest/userguide/images/cf_flow.png)

The following sections provide more information about using a CDN in your MediaPackage workflow.

**Topics**
+ [CDN configuration recommendations](cdn-recommendations.md)
+ [Secure MediaPackage content with CDN authorization](cdn-auth.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
