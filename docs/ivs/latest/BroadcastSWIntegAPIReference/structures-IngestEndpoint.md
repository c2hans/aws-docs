---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-IngestEndpoint.html
---

# IngestEndpoint
<a name="structures-IngestEndpoint"></a>

Object specifying ingest endpoints returned by [GetClientConfiguration](actions-GetClientConfiguration.md).

## Contents
<a name="structures-IngestEndpoint-contente"></a>
+ **authentication**
  + Stream key associated with the ingest endpoint.
  + Type: String
  + Required: Yes
+ **protocol**
  + Protocol for ingest.
  + Type: String
  + Valid Values: `RTMP` \| `RTMPS`
  + Required: Yes
+ **url\_template**
  + Template for the endpoint URL. Insert the stream key returned in `authentication` to create a URL from this template.
  + Type: String
  + Required: Yes
