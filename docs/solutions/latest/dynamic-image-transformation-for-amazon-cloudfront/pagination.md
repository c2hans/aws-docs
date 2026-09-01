---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/pagination.html
---

# Pagination
<a name="pagination"></a>

The list endpoints (`GET /policies`, `GET /origins`, and `GET /mappings`) return results in pages. When more results are available, the response includes a `nextToken` value. To retrieve the next page, pass it back as the `nextToken` query parameter on the same endpoint. When the response omits `nextToken`, you have reached the last page.

```
GET /policies?nextToken=<token-from-previous-response>
```

The `nextToken` value is an opaque, encrypted cursor. Treat it as an opaque string: don’t parse, construct, or modify it. Each token is bound to the deployment’s AWS account and expires 24 hours after it is issued, so tokens can’t be reused across deployments. If you submit an expired, tampered, or otherwise invalid token, the API returns the first page of results rather than failing the request.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
