---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/origins-api.html
---

# Origins API
<a name="origins-api"></a>

Manage origin configurations that define source locations for images.

 **List Origins**

```
GET /origins?nextToken={token}
```

Response:

```
{
  "items": [
    {
      "originId": "550e8400-e29b-41d4-a716-446655440001",
      "originName": "my-s3-origin",
      "originDomain": "my-images-bucket.s3.amazonaws.com",
      "originPath": "/images",
      "originHeaders": {
        "x-custom-header": "value"
      },
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "nextToken": "optional-token-for-next-page"
}
```

 **Create Origin**

```
POST /origins
{
  "originName": "my-s3-origin",
  "originDomain": "my-images-bucket.s3.amazonaws.com",
  "originPath": "/images",
  "originHeaders": {
    "x-custom-header": "value"
  }
}
```

 **Get Origin**

```
GET /origins/{originId}
```

 **Update Origin**

```
PUT /origins/{originId}
{
  "originName": "updated-origin-name",
  "originDomain": "updated-bucket.s3.amazonaws.com"
}
```

 **Delete Origin**

```
DELETE /origins/{originId}
```
