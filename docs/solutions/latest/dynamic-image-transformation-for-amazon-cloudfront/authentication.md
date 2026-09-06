---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/authentication.html
---

# Authentication
<a name="authentication"></a>

All Admin API requests require authentication through Amazon Cognito:

```
Authorization: Bearer <cognito-jwt-token>
Content-Type: application/json
```
