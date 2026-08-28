---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/cloudfront-distribution-creation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# CloudFront distribution creation
<a name="cloudfront-distribution-creation"></a>

 Create a CloudFront web distribution by following the distribution, the default origin and behavior automatically created will be used for dynamic content. Create four additional behaviors to further customize the way both static and dynamic requests are treated. The following table summarizes the configuration properties for the five behaviors.

* Table 1: Summary of configuration properties for CloudFront behaviors *

|  Property  |  Static  |  Dynamic (admin)  |  Dynamic (front end)  |
| --- | --- | --- | --- |
|  Paths (Behaviors)  |  `wp-content/* `<br />` wp-includes/* ` | ` wp-admin/*` <br /> `wp-login.php ` |  default (\*)  |
|  Protocols  |  HTTP and HTTPS  |  Redirect to HTTPS  |  HTTP and HTTPS  |
|  HTTP methods  |  GET, HEAD  |  ALL  |  ALL  |
|  HTTP headers  |  NONE  |  ALL  |  Host <br /> CloudFront-Forwarded-Proto <br /> CloudFront-Is-Mobile-Viewer <br /> CloudFront-Is-Tablet-Viewer <br /> CloudFront-Is-Desktop-Viewer  |
|   |   |   |   |
|  Cookies  |  NONE  |  ALL  |  comment\_\* <br /> wordpress\_\* <br /> wp-settings-\*  |
|  Query Strings  |  YES (invalidation)  |  YES  |  YES  |

 For the default behavior, AWS recommends the following configuration:
+  Allow the Origin Protocol Policy to Match Viewer, so that if viewers connect to CloudFront using HTTPS, CloudFront connects to your origin using HTTPS as well, achieving end-to-end encryption. Note that this requires you install a trusted SSL certificate on the load balancer. For details, refer to [Requiring HTTPS for Communication Between CloudFront and Your Custom Origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html).
+  Allow all HTTP methods since the dynamic portions of the website require both GET and POST requests (for example, to support POST for the comment submission forms).
+  Forward only the cookies that vary the WordPress output; for example, `>wordpress_*`, `wp-settings-*`, and `comment_*`. You must extend that list if you have installed any plugins that depend on other cookies not in the list.
+  Forward only the HTTP headers that affect the output of WordPress, for example, `Host`, `CloudFront-Forwarded-Proto`, `CloudFront-is-Desktop-Viewer`, `CloudFront-is-Mobile-Viewer`, and `CloudFront-is-Tablet-Viewer`:
  +  `Host` allows multiple WordPress websites to be hosted on the same origin.
  +  `CloudFront-Forwarded-Proto` allows different versions of pages to be cached depending on whether they are accessed via HTTP or HTTPS.
  +  `CloudFront-is-Desktop-Viewer`, `CloudFront-is-Mobile-Viewer`, `CloudFront-is-Tablet-Viewer` allow you to customize the output of your themes based on the end user’s device type.
+  Forward all the query strings to cache based on their values because WordPress relies on these, they can also be used to invalidate cached objects.

 If you want to serve your website under a custom domain name (that is, not `*.cloudfront.net`), then enter the appropriate URIs under **Alternate** **Domain Names** in the Distribution Settings. In this case, you also need an SSL certificate for your custom domain name. You can [request](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request.html) SSL certificates via the AWS Certificate Manager and configure them against a CloudFront distribution.

 Now, create two more cache behaviors for dynamic content: one for the login page (path pattern: `wp-login.php`) and one for the admin dashboard (path pattern: `wp-admin/*`). These two behaviors have the exact same settings, as follows:
+  Enforce a Viewer Protocol Policy of HTTPS Only.
+  Allow all HTTP methods.
+  Cache based on all HTTP headers.
+  Forward all cookies.
+  Forward and cache based on all query strings.

The reason behind this configuration is that this section of the website is highly personalized and typically has just a few users, so caching efficiency isn’t a primary concern. The focus is to keep the configuration simple to ensure maximum compatibility with any installed plugins by passing all cookies and headers to the origin.

By default, WordPress stores everything locally on the web server, which is block storage (Amazon EBS) for [single server deployment](simple-deployment.md), and file storage (Amazon EFS) for [elastic deployment](elastic-deployment.md). In addition to reducing storage and data transfer costs, moving static assets to Amazon S3 offers scalability, data availability, security and performance. There are several plugins that make it easy to move static content to Amazon S3; one of them is [W3 Total Cache](https://wordpress.org/plugins/w3-total-cache/), also covered in [Appendix B: Plugins installation and configuration](appendix-b-plugins-installation-and-configuration.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
