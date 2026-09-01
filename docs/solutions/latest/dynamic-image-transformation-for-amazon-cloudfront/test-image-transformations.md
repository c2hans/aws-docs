---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/test-image-transformations.html
---

# Test image transformations
<a name="test-image-transformations"></a>

There are two ways to test your configuration.

 **Interactive (Playground).** For quick checks without constructing URLs by hand, use the [Playground](ecs-playground.md). You enter an image path, optionally apply transformations or device presets, and see the resulting image alongside its transformation metrics. This is the most accessible way to confirm that a mapping resolves and a policy behaves as expected.

 **Production URL.** To test the same request URL your application uses in production, request an image directly from the CloudFront distribution created by the solution.

1. Get the CloudFront distribution URL from the CloudFormation stack outputs (`CloudFrontDistributionDomainName`).

1. Access images using the pattern defined in your mappings:

   ```
   https://<cloudfront-domain>/<mapping-pattern>/<image-path>
   ```

1. Example:

   ```
   https://d1234567890.cloudfront.net/mobile/sample-image.jpg
   ```

1. The image is processed according to the transformation policy associated with the matching mapping.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
