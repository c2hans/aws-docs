---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ConfigurationMetadata.html
---

# ConfigurationMetadata
<a name="structures-ConfigurationMetadata"></a>

Object specifying the metadata for the configuration returned by [GetClientConfiguration](actions-GetClientConfiguration.md).

## Contents
<a name="structures-ConfigurationMetadata-contente"></a>
+ **config\_id**
  + Configuration ID uniquely identifying this response.
  + Type: String
  + Required: Yes
+ **schema\_version**
  + Schema version of the configuration based on the schema version specified in the request. The schema version format is `YYYY-MM-DD`.
  + Type: String
  + Valid Value: `2024-06-04`
  + Required: Yes
+ **service**
  + Name of the video service.
  + Type: String
  + Valid Values: `IVS`
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
