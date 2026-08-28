---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v12-Grafana-API-ShortURL.html
---

# Short URL API
<a name="v12-Grafana-API-ShortURL"></a>

Use the Short URL API to create shortened URLs. A short URL represents a longer URL containing complex query parameters in a smaller and simpler format.

**Note**
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Create short URL
<a name="v12-Grafana-API-ShortURL-create"></a>

```
POST /api/short-urls
```

Creates a short URL.

**Example request**

```
POST /api/short-urls HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "path": "d/TxKARsmGz/new-dashboard?orgId=1&from=1599389322894&to=1599410922894"
}
```

JSON body schema:
+ **path** – The path to shorten, relative to the Grafana root URL.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "uid": "AT76wBvGk",
  "url": "/goto/AT76wBvGk?orgId=1"
}
```

Status codes:
+ **200** – Created
+ **400** – Errors (invalid JSON, missing or invalid fields)

## Get short URL
<a name="v12-Grafana-API-ShortURL-get"></a>

```
GET /api/short-urls/:uid
```

Retrieves a short URL by its UID.

**Example request**

```
GET /api/short-urls/AT76wBvGk HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "uid": "AT76wBvGk",
  "path": "d/TxKARsmGz/new-dashboard?orgId=1&from=1599389322894&to=1599410922894"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
