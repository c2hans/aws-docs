---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/actions-FindIngest.html
---

# FindIngest
<a name="actions-FindIngest"></a>

Returns a list of available ingest endpoints.

## Request Syntax
<a name="actions-FindIngest-request-syntax"></a>

```
GET https://ingest.contribute.live-video.net/api/v2/FindIngest
HTTP/1.1
```

## URI Request Parameters
<a name="actions-FindIngest-uri-request-params"></a>

The request does not use any URI parameters.

## Response Syntax
<a name="actions-FindIngest-response-syntax"></a>

```
HTTP/1.1 200
Content-type: application/json
{
  "ingests": [
    {
      "_id": number,
      "availability": number,
      "default": boolean,
      "name": "string",
      "priority": number,
      "url_template": "string",
      "url_template_secure": "string"
    }
  ]
}
```

## Response Elements
<a name="actions-FindIngest-response-elements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.
+ **ingests**
  + Available ingest endpoints.
  + Type: Array of [Ingest](structures-Ingest.md) objects
  + Required: Yes
