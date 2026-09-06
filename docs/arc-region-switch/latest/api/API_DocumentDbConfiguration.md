---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DocumentDbConfiguration.html
---

# DocumentDbConfiguration
<a name="API_DocumentDbConfiguration"></a>

Configuration for Amazon DocumentDB global clusters used in a Region switch plan.

## Contents
<a name="API_DocumentDbConfiguration_Contents"></a>

 ** behavior **   <a name="regionswitch-Type-DocumentDbConfiguration-behavior"></a>
The behavior for a global cluster, that is, only allow switchover or also allow failover.
Type: String
Valid Values: `switchoverOnly | failover`
Required: Yes

 ** databaseClusterArns **   <a name="regionswitch-Type-DocumentDbConfiguration-databaseClusterArns"></a>
The database cluster Amazon Resource Names (ARNs) for a DocumentDB global cluster.
Type: Array of strings
Pattern: `arn:aws[a-zA-Z-]*:rds:[a-z0-9-]+:\d{12}:cluster:[a-zA-Z0-9][a-zA-Z0-9-_]{0,99}`
Required: Yes

 ** globalClusterIdentifier **   <a name="regionswitch-Type-DocumentDbConfiguration-globalClusterIdentifier"></a>
The global cluster identifier for a DocumentDB global cluster.
Type: String
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-DocumentDbConfiguration-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-DocumentDbConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-DocumentDbConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-DocumentDbConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [DocumentDbUngraceful](API_DocumentDbUngraceful.md) object
Required: No

## See Also
<a name="API_DocumentDbConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/DocumentDbConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/DocumentDbConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/DocumentDbConfiguration)
