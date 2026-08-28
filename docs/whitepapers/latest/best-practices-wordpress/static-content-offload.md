---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/static-content-offload.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Static content offload
<a name="static-content-offload"></a>

 This includes CSS, JavaScript, and image files – either those that are part of your WordPress themes or those media files uploaded by the content administrators. All these files can be stored in Amazon Simple Storage Service (Amazon S3) using a plugin such as W3 Total Cache and served to users in a scalable and highly available manner. [Amazon S3](https://aws.amazon.com/s3/) offers a highly scalable, reliable, and low-latency data storage infrastructure at low cost, which is accessible via REST APIs. Amazon S3 redundantly stores your objects, not only on multiple devices, but also across multiple facilities in an AWS Region, thus providing exceptionally high levels of durability.

 This has the positive side effect of offloading this workload from your Lightsail instance and letting it focus on dynamic content generation. This reduces the load on the server and is an important step towards creating a stateless architecture (a prerequisite before implementing automatic scaling).

 You can subsequently configure Amazon S3 as an origin for CloudFront to improve delivery of those static assets to users around the world. Although WordPress isn’t integrated with Amazon S3 and CloudFront out-of-the-box, a variety of plugins add support for these services (for example, W3 Total Cache).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
