---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/shared-storage-amazon-s3-and-amazon-efs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared storage (Amazon S3 and Amazon EFS)
<a name="shared-storage-amazon-s3-and-amazon-efs"></a>

 By default, WordPress stores user uploads on the local file system and so isn’t stateless. Therefore, we need to move the WordPress installation and all user customizations (such as configuration, plugins, themes, and user-generated uploads) into a shared data platform to help reduce load on the web servers and to make the web tier stateless.

 [Amazon Elastic File System](https://aws.amazon.com/efs/details/) (Amazon EFS) provides scalable network file systems for use with EC2 instances. Amazon EFS file systems are distributed across an unconstrained number of storage servers, enabling file systems to grow elastically and allowing massively parallel access from EC2 instances. The distributed design of Amazon EFS avoids the bottlenecks and constraints inherent to traditional file servers.

 By moving the entire WordPress installation directory onto an EFS file system and mounting it into each of your EC2 instances when they boot, your WordPress site and all its data is automatically stored on a distributed file system that isn’t dependent on any one EC2 instance, making your web tier completely stateless. The benefit of this architecture is that you don’t need to install plugins and themes on each new instance launch, and you can significantly speed up the installation and recovery of WordPress instances. It is also easier to deploy changes to plugins and themes in WordPress, as outlined in the [Deployment Considerations](appendix-a-cloudfront-configuration.md) section of this document.

 To ensure optimal performance of your website when running from an EFS file system, check the recommended configuration settings for Amazon EFS and OPcache on the [AWS Reference Architecture for WordPress](https://github.com/awslabs/aws-refarch-wordpress#opcache).

 You also have the option to offload all static assets, such as image, CSS, and JavaScript files, to an S3 bucket with CloudFront caching in front. The mechanism for doing this in a multi-server architecture is exactly the same as for a single-server architecture, as discussed in the [Static Content](accelerating-content-delivery.md) section of this whitepaper. The benefits are the same as in the single-server architecture—you can offload the work associated with serving your static assets to Amazon S3 and CloudFront, thereby allowing your web servers to focus on generating dynamic content only and serve more user requests per web server.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
