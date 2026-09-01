---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-end-to-end-example.html
---

# End-to-end example
<a name="ecs-end-to-end-example"></a>

This example ties the three configuration entities together to serve WebP-optimized product images from an Amazon S3 bucket under the `/products/*` path. It assumes your source images live in an S3 bucket reachable at `my-product-images.s3.us-east-1.amazonaws.com` under a `catalog/` prefix.

1.  **Create the origin.** Following [Create origins](create-origins.md), create an origin named `Product images bucket` with the origin domain `my-product-images.s3.us-east-1.amazonaws.com` and the origin path `/catalog`.

1.  **Create the transformation policy.** Following [Create transformation policies](create-transformation-policies.md), create a policy named `Optimization policy` using the format \+ quality \+ autosize optimization example. This serves WebP or AVIF to browsers that support them and an appropriate resolution for each device.

1.  **Create the mapping.** Following [Create mappings](create-mappings.md), create a mapping named `Product image route` with the path pattern `/products/*`, the `Product images bucket` origin, and the `Optimization policy` transformation policy.

1.  **Test the result.** Get the CloudFront domain name from the stack output `CloudFrontDistributionDomainName`, then request an image under the mapped path:

   ```
   https://<cloudfront-domain>/products/shoes/01.jpg
   ```

   The solution matches the request to the `Product image route` mapping, fetches `01.jpg` from the S3 origin (resolving to `catalog/products/shoes/01.jpg` after the origin path is applied), applies the `Optimization policy`, and returns an optimized image. A browser that supports WebP receives a WebP image; a browser that does not receives the JPEG fallback.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
