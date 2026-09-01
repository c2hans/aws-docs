---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/include-custom-response-headers.html
---

# Include custom response headers
<a name="include-custom-response-headers"></a>

This solution allows you to include headers you’d like returned alongside the response, as part of your request.
+  **headers (optional, object)** - Includes the provided headers in the response. Header should be written in Pascal-Case and cannot overwrite headers that would otherwise be present in the response (Except for Cache-Control).

  ```
  const imageRequest = JSON.stringify({
      bucket: "<myImageBucket>",
      key: "<myImage.jpeg>",
      headers: {
          "Cache-Control":"max-age=86400,public",
          "Custom-Header":"some-custom-value"
      }
  })
  ```

**Note**
A deny-list is maintained which restricts which headers can be included with this feature. Headers which may serve a purpose for the browser or are used to support authentication/authorization are included in this deny-list. For an exact list of the regular expressions which are restricted, visit [constants.ts](https://github.com/aws-solutions/serverless-image-handler/blob/main/source/image-handler/lib/constants.ts) on the Solution GitHub repository.
The presence of the `expires` query parameter will cause the Cache-Control header to be overridden, regardless of any value provided in the headers field.
If your deployment is using the S3 Object Lambda Architecture , the headers at [this link](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-function-restrictions-all.html#function-restrictions-disallowed-headers) cannot be included as custom headers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
