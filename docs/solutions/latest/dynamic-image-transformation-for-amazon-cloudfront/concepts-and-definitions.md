---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **origin**

The source location where original images are stored, which can be an Amazon S3 bucket or an external HTTP-accessible domain.

 **transformation policy**

A reusable configuration that defines a set of image transformations, output settings, and conditional logic that can be applied to image requests.

 **mapping**

Configuration that routes image requests to specific origins based on request path patterns or host headers.

 **cross-origin resource sharing (CORS)**

Defines a way for client web applications that are loaded in one domain to interact with resources in a different domain.

 **fallback image**

Image that you set to show when the intended image doesn’t load.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
