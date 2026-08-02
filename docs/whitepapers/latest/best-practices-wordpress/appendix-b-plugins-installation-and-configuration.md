---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/appendix-b-plugins-installation-and-configuration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix B: Static content configuration
<a name="appendix-b-plugins-installation-and-configuration"></a>

 By default, WordPress stores everything locally on the web server, which is block storage (Amazon EBS) for [single server deployment](simple-deployment.md), and file storage (Amazon EFS) for [elastic deployment](elastic-deployment.md). In addition to reducing storage and data transfer costs, moving static asset to Amazon S3 offers scalability, data availability, security and performance.

 In this example, the W3 Total Cache (W3TC) plugin is used to store static assets on Amazon S3. However, there are other plugins available with similar capabilities. If you want to use an alternative you can adjust the following steps accordingly. The steps only refer to features or settings relevant to this example. A detailed description of all settings is beyond the scope of this document. Refer to the [W3 Total Cache plugin page](https://wordpress.org/plugins/w3-total-cache/) at [wordpress.org](https://wordpress.org/) for more information.
