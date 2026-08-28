---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-Ingest.html
---

# Ingest
<a name="structures-Ingest"></a>

Object specifying ingest endpoints returned by [FindIngest](actions-FindIngest.md).

## Contents
<a name="structures-Ingest-contente"></a>
+ **\_id**
  + Sequential index of the ingest endpoint.
  + Type: Integer
  + Required: Yes
+ **availability**
  + Indicates whether the ingest endpoint is available. The ingest endpoint is available If `availability` is `1.0`. It is unavailable if `availability` is `0`. Availability may change over time.
  + Type: Integer
  + Valid Values: `0` \| `1.0`
  + Required: Yes
+ **default**
  + Identifies the default ingest endpoint for auto-selection. Only one ingest endpoint in the response will have `default` set to `true`. The ingest endpoint with `default` set to `true` should be auto-selected as long as its `availability` is `1.0`.
  + Type: Boolean
  + Required: Yes
+ **name**
  + Name of the ingest endpoint.
  + Type: String
  + Required: Yes
+ **priority**
  + Priority of the ingest endpoint. Servers with the lowest priority should be used first.
  + Type: Integer
  + Required: Yes
+ **url\_template**
  + URL template using the RTMP protocol. Insert a stream key to create a URL from the template.
  + Type: String
  + Required: Yes
+ **url\_template\_secure**
  + URL template using the RTMPS protocol. Insert a stream key to create a URL from the template.
  + Type: String
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
