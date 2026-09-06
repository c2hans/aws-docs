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
