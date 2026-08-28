---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListPlaybackConfigurations.html
---

# ListPlaybackConfigurations
<a name="API_ListPlaybackConfigurations"></a>

Retrieves existing playback configurations. For information about MediaTailor configurations, see [Working with Configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).

## Request Syntax
<a name="API_ListPlaybackConfigurations_RequestSyntax"></a>

```
GET /playbackConfigurations?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPlaybackConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListPlaybackConfigurations_RequestSyntax) **   <a name="mediatailor-ListPlaybackConfigurations-request-uri-MaxResults"></a>
The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` playback configurations, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListPlaybackConfigurations_RequestSyntax) **   <a name="mediatailor-ListPlaybackConfigurations-request-uri-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListPlaybackConfigurations` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.

## Request Body
<a name="API_ListPlaybackConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPlaybackConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AdConditioningConfiguration": {
            "StreamingMediaFileConditioning": "string"
         },
         "AdDecisionServerConfiguration": {
            "HttpRequest": {
               "Body": "string",
               "CompressRequest": "string",
               "Headers": {
                  "string" : "string"
               },
               "Method": "string"
            },
            "VastResponse": {
               "AdSequencingMode": "string"
            }
         },
         "AdDecisionServerUrl": "string",
         "AdsPersonalizationConcurrency": {
            "EnableVodVastParallelization": boolean,
            "MaxConcurrentAdsRequests": number
         },
         "AdsPersonalizationTimeouts": {
            "AdsRequestTimeoutMilliseconds": number,
            "LiveMaximumAdsPersonalizationTimeMilliseconds": number,
            "PrefetchAdsRequestTimeoutMilliseconds": number,
            "PrefetchMaximumAdsPersonalizationTimeMilliseconds": number,
            "VodMaximumAdsPersonalizationTimeMilliseconds": number
         },
         "AvailSuppression": {
            "FillPolicy": "string",
            "Mode": "string",
            "Value": "string"
         },
         "Bumper": {
            "EndUrl": "string",
            "StartUrl": "string"
         },
         "CdnConfiguration": {
            "AdSegmentUrlPrefix": "string",
            "ContentSegmentUrlPrefix": "string"
         },
         "ConfigurationAliases": {
            "string" : {
               "string" : "string"
            }
         },
         "DashConfiguration": {
            "DualStackManifestEndpointPrefix": "string",
            "ManifestEndpointPrefix": "string",
            "MpdLocation": "string",
            "OriginManifestType": "string"
         },
         "DualStackPlaybackEndpointPrefix": "string",
         "DualStackSessionInitializationEndpointPrefix": "string",
         "FunctionMapping": {
            "string" : "string"
         },
         "HlsConfiguration": {
            "DualStackManifestEndpointPrefix": "string",
            "ManifestEndpointPrefix": "string"
         },
         "InsertionMode": "string",
         "LivePreRollConfiguration": {
            "AdDecisionServerConfiguration": {
               "VastResponse": {
                  "AdSequencingMode": "string"
               }
            },
            "AdDecisionServerUrl": "string",
            "MaxDurationSeconds": number
         },
         "LogConfiguration": {
            "AdsInteractionLog": {
               "ExcludeEventTypes": [ "string" ],
               "PublishOptInEventTypes": [ "string" ]
            },
            "EnabledLoggingStrategies": [ "string" ],
            "ManifestServiceInteractionLog": {
               "ExcludeEventTypes": [ "string" ],
               "PublishOptInEventTypes": [ "string" ]
            },
            "PercentEnabled": number
         },
         "ManifestProcessingRules": {
            "AdMarkerPassthrough": {
               "Enabled": boolean
            }
         },
         "Name": "string",
         "PersonalizationThresholdSeconds": number,
         "PlaybackConfigurationArn": "string",
         "PlaybackEndpointPrefix": "string",
         "SessionInitializationEndpointPrefix": "string",
         "SlateAdUrl": "string",
         "tags": {
            "string" : "string"
         },
         "TranscodeProfileName": "string",
         "VideoContentSourceUrl": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListPlaybackConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListPlaybackConfigurations_ResponseSyntax) **   <a name="mediatailor-ListPlaybackConfigurations-response-Items"></a>
Array of playback configurations. This might be all the available configurations or a subset, depending on the settings that you provide and the total number of configurations stored.
Type: Array of [PlaybackConfiguration](API_PlaybackConfiguration.md) objects

 ** [NextToken](#API_ListPlaybackConfigurations_ResponseSyntax) **   <a name="mediatailor-ListPlaybackConfigurations-response-NextToken"></a>
Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListPlaybackConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListPlaybackConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListPlaybackConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListPlaybackConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
