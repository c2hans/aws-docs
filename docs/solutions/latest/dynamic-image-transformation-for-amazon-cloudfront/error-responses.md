---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/error-responses.html
---

# Error Responses
<a name="error-responses"></a>

All APIs return structured error responses:

```
{
  "errorCode": "POLICY_NOT_FOUND",
  "message": "Policy with ID 550e8400-e29b-41d4-a716-446655440000 not found"
}
```

Common error codes: - `BAD_REQUEST`: Invalid request format or parameters - `INVALID_JSON`: Malformed JSON in request body - `MISSING_REQUIRED_FIELD`: Required field missing from request - `INVALID_FIELD_VALUE`: Field value doesn’t meet validation requirements - `NOT_FOUND`: Resource not found - `POLICY_NOT_FOUND`: Transformation policy not found - `ORIGIN_NOT_FOUND`: Origin configuration not found - `INTERNAL_SERVER_ERROR`: Server-side error

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
