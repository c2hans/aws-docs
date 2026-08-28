---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/transformation-policies-api.html
---

# Transformation Policies API
<a name="transformation-policies-api"></a>

Manage image transformation policies that define how images are processed.

 **List Policies**

```
GET /policies?nextToken={token}
```

Response:

```
{
  "items": [
    {
      "policyId": "550e8400-e29b-41d4-a716-446655440000",
      "policyName": "mobile-optimized",
      "description": "Mobile device optimization policy",
      "policyJSON": "{\"transformations\":[...]}",
      "isDefault": false,
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "nextToken": "optional-token-for-next-page"
}
```

 **Create Policy**

```
POST /policies
{
  "policyName": "mobile-optimized",
  "description": "Mobile device optimization policy",
  "policyJSON": "{\"transformations\":[{\"condition\":\"width > 800\",\"operations\":[{\"resize\":{\"width\":800,\"height\":600,\"fit\":\"cover\"}},{\"format\":\"webp\"},{\"quality\":85}]}]}",
  "isDefault": false
}
```

 **Get Policy**

```
GET /policies/{policyId}
```

 **Update Policy**

```
PUT /policies/{policyId}
{
  "policyName": "updated-mobile-optimized",
  "description": "Updated mobile device optimization policy",
  "policyJSON": "{\"transformations\":[...]}"
}
```

 **Delete Policy**

```
DELETE /policies/{policyId}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
