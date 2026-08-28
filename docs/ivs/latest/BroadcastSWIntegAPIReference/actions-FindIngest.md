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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
