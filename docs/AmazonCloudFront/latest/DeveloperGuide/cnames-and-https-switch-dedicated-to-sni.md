---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-switch-dedicated-to-sni.html
---

# Switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI
<a name="cnames-and-https-switch-dedicated-to-sni"></a>

If you configured CloudFront to use a custom SSL/TLS certificate with dedicated IP addresses, you can switch to using a custom SSL/TLS certificate with SNI instead and eliminate the charge that is associated with dedicated IP addresses.

**Important**
This update to your CloudFront configuration has no effect on viewers that support SNI. Viewers can access your content before and after the change, as well as while the change is propagating to CloudFront edge locations. Viewers that don't support SNI can't access your content after the change. For more information, see [Choose how CloudFront serves HTTPS requests](cnames-https-dedicated-ip-or-sni.md).

## Switch from a custom certificate to SNI
<a name="cloudfront-switch-custom-cert-sni"></a>

The following procedure shows you how to switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI.<a name="cnames-and-https-switch-dedicated-to-sni-proc"></a>

**To switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Choose the ID of the distribution that you want to view or update.

1. Choose **Distribution Settings**.

1. On the **General** tab, choose **Edit**.

1. Under **Custom SSL certification – *optional***, deselect **Legacy clients support**.

1. Choose **Yes, Edit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
