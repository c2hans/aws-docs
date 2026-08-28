---
source_url: https://docs.aws.amazon.com/ses/latest/dg/content-encodings.html
---

# Content encodings supported by Amazon SES
<a name="content-encodings"></a>

The following is provided for reference.

Amazon SES supports the following content encodings:
+ `deflate`
+ `gzip`
+ `identity`

Amazon SES also supports the following Accept-Encoding header format, according to the [RFC 7231](https://tools.ietf.org/html/rfc7231#section-5.3.4) specification:
+ `Accept-Encoding:deflate,gzip`
+ `Accept-Encoding:`
+ `Accept-Encoding:*`
+ `Accept-Encoding:deflate;q=0.5,gzip;q=1.0`
+ `Accept-Encoding:gzip;q=1.0,identity;q=0.5,*;q=0`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
