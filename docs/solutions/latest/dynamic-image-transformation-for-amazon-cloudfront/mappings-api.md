---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/mappings-api.html
---

# Mappings API
<a name="mappings-api"></a>

Manage path-based or host-header based routing to map requests to specific origins and policies.

 **List Mappings**

```
GET /mappings?nextToken={token}
```

Response:

```
{
  "items": [
    {
      "mappingId": "550e8400-e29b-41d4-a716-446655440002",
      "mappingName": "mobile-path-mapping",
      "description": "Mobile path routing",
      "mappingType": "PATH_MAPPING",
      "pattern": "/mobile/*",
      "originId": "550e8400-e29b-41d4-a716-446655440001",
      "policyId": "550e8400-e29b-41d4-a716-446655440000",
      "priority": 100,
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "nextToken": "optional-token-for-next-page"
}
```

 **Create Path Mapping**

```
POST /mappings
{
  "mappingName": "mobile-path-mapping",
  "description": "Mobile path routing",
  "mappingType": "PATH_MAPPING",
  "pattern": "/mobile/*",
  "originId": "550e8400-e29b-41d4-a716-446655440001",
  "policyId": "550e8400-e29b-41d4-a716-446655440000",
  "priority": 100
}
```

 **Create Host Header Mapping**

```
POST /mappings
{
  "mappingName": "subdomain-mapping",
  "description": "Subdomain routing",
  "mappingType": "HOST_HEADER_MAPPING",
  "pattern": "*.example.com",
  "originId": "550e8400-e29b-41d4-a716-446655440001",
  "policyId": "550e8400-e29b-41d4-a716-446655440000",
  "priority": 200
}
```

 **Get Mapping**

```
GET /mappings/{mappingId}
```

 **Update Mapping**

```
PUT /mappings/{mappingId}
{
  "mappingName": "updated-mapping-name",
  "pattern": "/updated-path/*",
  "priority": 150
}
```

 **Delete Mapping**

```
DELETE /mappings/{mappingId}
```
