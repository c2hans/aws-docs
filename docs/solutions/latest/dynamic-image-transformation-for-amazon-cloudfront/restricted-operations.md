---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/restricted-operations.html
---

# Restricted operations
<a name="restricted-operations"></a>

Certain Sharp operations are restricted by the solution to help enhance security. This includes (but may not be limited to):
+ clone
+ metadata
+ stats
+ composite (Though this is permitted through the use of overlayWith)
+ certain [output options](https://sharp.pixelplumbing.com/api-output) (Including toFile, toBuffer, tile and raw)

For an exact list of allow-listed Sharp operations, you can visit [constants.ts](https://github.com/aws-solutions/serverless-image-handler/blob/main/source/image-handler/lib/constants.ts) on the Solution GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
