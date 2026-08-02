---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ElasticsearchSettings.html
---

# ElasticsearchSettings
<a name="API_ElasticsearchSettings"></a>

Provides information that defines an OpenSearch endpoint.

## Contents
<a name="API_ElasticsearchSettings_Contents"></a>

 ** EndpointUri **   <a name="DMS-Type-ElasticsearchSettings-EndpointUri"></a>
The endpoint for the OpenSearch cluster. AWS DMS uses HTTPS if a transport protocol (http/https) is not specified.
Type: String
Required: Yes

 ** ServiceAccessRoleArn **   <a name="DMS-Type-ElasticsearchSettings-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.
Type: String
Required: Yes

 ** ErrorRetryDuration **   <a name="DMS-Type-ElasticsearchSettings-ErrorRetryDuration"></a>
The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.
Type: Integer
Required: No

 ** FullLoadErrorPercentage **   <a name="DMS-Type-ElasticsearchSettings-FullLoadErrorPercentage"></a>
The maximum percentage of records that can fail to be written before a full load operation stops.
To avoid early failure, this counter is only effective after 1000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.
Type: Integer
Required: No

 ** UseNewMappingType **   <a name="DMS-Type-ElasticsearchSettings-UseNewMappingType"></a>
Set this option to `true` for DMS to migrate documentation using the documentation type `_doc`. OpenSearch and an Elasticsearch cluster only support the \_doc documentation type in versions 7. x and later. The default value is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_ElasticsearchSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ElasticsearchSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ElasticsearchSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ElasticsearchSettings)
