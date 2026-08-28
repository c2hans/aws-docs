---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/revise-origin-request-policies.html
---

# Revise origin request policies
<a name="revise-origin-request-policies"></a>

 This solution provides you the ability to select a specific cache behavior in CloudFront configuration where token validation needs to be applied. Token validation logic takes viewer specific attributes, exposed at runtime through event object, to validate if the viewer using this token is in fact the viewer this token is for. This form of viewer uniqueness is achieved by including the token viewer specific attributes, some of them relating to the viewer’s location, like country or region. Viewer location information is available only through CloudFront generated headers that token validation code has to pull that information from. However, that category of headers will only appear in the event object when these specific headers are specified either in cache or origin request policies. To prevent negative impact on cache hit ratio, rather than using cache policies we recommend that you add the two specific geolocation headers in each origin request policy that is associated with token protected cache behaviors. In the origin request policy definition, include both `CloudFront-Viewer-Country` and `CloudFront-Viewer-Country-Region` in the headers section.

![Screenshot of origin request policy - geolocation headers.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image11.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
