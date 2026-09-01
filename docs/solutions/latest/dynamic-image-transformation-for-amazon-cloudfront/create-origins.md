---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-origins.html
---

# Create origins
<a name="create-origins"></a>

An origin defines a source location for your images. The Admin UI validates each field as you enter it; the examples below use values that satisfy those validation rules.

 **Navigation:** In the Admin UI left navigation, select **Origins**, and then choose **Create origin**.

Provide the following fields:
+  **Name**: A unique name for the origin, 1-100 characters, using letters, numbers, spaces, underscores, or hyphens (for example, `Product images bucket`).
+  **Origin domain**: A valid DNS domain name (up to 253 characters) for an S3 bucket or HTTP server. Do not include a scheme (`https://`) or path.
+  **Origin path - optional**: A path prefix prepended to every origin request. When provided, it must start with `/`, contain only letters, numbers, underscores, or hyphens in each segment, and not end in a filename (for example, `/images`).
+  **Origin headers - optional**: One or more header name/value pairs added to every request the solution makes to this origin.

After completing the fields, choose **Save** to create the origin.

**Example: Amazon S3 origin**

| Field | Value |
| --- | --- |
| Name |  `Product images bucket`  |
| Origin domain |  `my-product-images.s3.us-east-1.amazonaws.com`  |
| Origin path - optional |  `/catalog`  |
| Origin headers - optional |  *(none)*  |

**Example: external HTTP origin**

| Field | Value |
| --- | --- |
| Name |  `Marketing CDN origin`  |
| Origin domain |  `assets.example.com`  |
| Origin path - optional |  `/media`  |
| Origin headers - optional |  `x-origin-source` = `dit`  |

 **Screenshot of the Origins > Create origin form in the Admin UI.**

![Admin UI Create origin form](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/admin-ui-create-origin.png)

 **Screenshot of the Origins list view in the Admin UI.**

![Admin UI Origins list view](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/admin-ui-origins-list.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
