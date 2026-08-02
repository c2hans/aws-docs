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
