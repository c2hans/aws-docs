---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v10-Grafana-API-FolderDashboard-Search.html
---

# Folder/Dashboard Search API
<a name="v10-Grafana-API-FolderDashboard-Search"></a>

Use the FolderDashboard-Search API to search folders and dashboards in an Amazon Managed Grafana workspace.

**Note**
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Search folders and dashboards
<a name="v10-Grafana-API-FolderDashboard-Search-create"></a>

```
GET /api/search/
```

Query parameters:
+ **query**— Search query
+ **tag**— List of tags to search for. These are Grafana tags, not AWS tags.
+ **type**— The type to search for, either `dash-folder` or `dash-db`.
+ **dashboardIds**— List of dashboard Id's to search for.
+ **folderIds**— List of dashboard Id's to search for in dashboards.
+ **starred**— Flag to specify that only starred dashboards are to be returned.
+ **limit**— Limit the number of returned results (maximum is 5000).
+ **page**— Use this parameter to access hits beyond limit. Numbering starts at 1. The `limit` parameter acts as page size.

**Example request for retrieving folders and dashboards of the general folder**

```
GET /api/search?folderIds=0&query=&starred=false HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response for retrieving folders and dashboards of the general folder**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id": 163,
    "uid": "000000163",
    "title": "Folder",
    "url": "/dashboards/f/000000163/folder",
    "type": "dash-folder",
    "tags": [],
    "isStarred": false,
    "uri":"db/folder" // deprecated in Grafana v5.0
  },
  {
    "id":1,
    "uid": "cIBgcSjkk",
    "title":"Production Overview",
    "url": "/d/cIBgcSjkk/production-overview",
    "type":"dash-db",
    "tags":[prod],
    "isStarred":true,
    "uri":"db/production-overview" // deprecated in Grafana v5.0
  }
]
```

**Example request for searching for starred dashboards**

```
GET /api/search?query=Production%20Overview&starred=true&tag=prod HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response for searching for starred dashboards**

```
HTTP/1.1 200
Content-Type: application/json

[HTTP/1.1 200
Content-Type: application/json

[
  {
    "id":1,
    "uid": "cIBgcSjkk",
    "title":"Production Overview",
    "url": "/d/cIBgcSjkk/production-overview",
    "type":"dash-db",
    "tags":[prod],
    "isStarred":true,
    "folderId": 2,
    "folderUid": "000000163",
    "folderTitle": "Folder",
    "folderUrl": "/dashboards/f/000000163/folder",
    "uri":"db/production-overview" // deprecated in Grafana v5.0
  }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
