---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/static-origin-creation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Static origin creation
<a name="static-origin-creation"></a>

 Now that the static files are stored on Amazon S3, go back to the CloudFront configuration in the CloudFront console, and configure Amazon S3 as the origin for static content. To do that, add a second origin pointing to the S3 bucket you created for that purpose. Then create two more cache behaviors, one for each of the two folders (`wp-content` and `wp-includes`) that should use the S3 origin rather than the default origin for dynamic content. Configure both in the same manner:
+  Serve HTTP GET requests only.
+  Amazon S3 does not vary its output based on cookies or HTTP headers, so you can improve caching efficiency by not forwarding them to the origin via CloudFront.
+  Despite the fact that these behaviors serve only static content (which accepts no parameters), you will forward query strings to the origin. This is so that you can use query strings as version identifiers to instantly invalidate, for example, older CSS files when deploying new versions. For more information, refer to the [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ReplacingObjects.html).

**Note**
After adding the static origin behaviors to your CloudFront distribution, check the order to ensure the behaviors for `wp-admin/*` and `wp-login.php` have higher precedence than the behaviors for static content. Otherwise, you may see strange behavior when accessing your admin panel.
