---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-HTTP-validation.html
---

# Troubleshooting HTTP validation problems
<a name="troubleshooting-HTTP-validation"></a>

Consult the following guidance if you're having trouble validating a certificate with HTTP.

The first step in HTTP troubleshooting is to check the current status of your domain with tools such as the following:
+ **curl** — [Linux and Windows](https://curl.se/docs/manpage.html)
+ **wget** — [Linux and Windows](https://www.gnu.org/software/wget/manual/wget.html)

**Topics**
+ [Content mismatch between RedirectFrom and RedirectTo locations](#http-validation-content-mismatch)
+ [Incorrect CloudFront configuration](#http-validation-cloudfront-configuration)
+ [HTTP redirect issues](http-validation-redirect-issues.md)
+ [Validation timeout](http-validation-timeout.md)

## Content mismatch between RedirectFrom and RedirectTo locations
<a name="http-validation-content-mismatch"></a>

If the content at the `RedirectFrom` location doesn't match the content at the `RedirectTo` location, validation will fail. Ensure that the content is identical for each domain in the certificate.

## Incorrect CloudFront configuration
<a name="http-validation-cloudfront-configuration"></a>

Make sure your CloudFront distribution is correctly configured to serve the validation content. Check that the origin and behavior settings are correct and that the distribution is deployed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
