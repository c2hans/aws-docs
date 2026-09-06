---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/channels.html
---

# Channels
<a name="channels"></a>

## URI
<a name="channels-url"></a>

`/channels`

## HTTP methods
<a name="channels-http-methods"></a>

### GET
<a name="channelsget"></a>

**Operation ID:** `ListChannels`

Lists channels that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | Pagination token from the GET list request. Use the token to fetch the next page of results. |
| maxResults | String | False | Upper bound on number of records to return. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ChannelList |  `200 OK` response<br />The list of channels is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="channelspost"></a>

**Operation ID:** `CreateChannel`

Creates a channel to receive content.

Once created, a channel provides static input URLs. These URLs remain the same throughout the lifetime of the channel, regardless of any failures or upgrades that might occur. Use these URLs to configure the outputs of your upstream encoder.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Channel |  `200 OK` response<br />The channel is created successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="channelsoptions"></a>

Enable CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="channels-schemas"></a>

### Request bodies
<a name="channels-request-examples"></a>

#### POST schema
<a name="channels-request-body-post-example"></a>

```
{
  "description": "string",
  "id": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="channels-response-examples"></a>

#### ChannelList schema
<a name="channels-response-body-channellist-example"></a>

```
{
  "channels": [
    {
      "createdAt": "string",
      "ingressAccessLogs": {
        "logGroupName": "string"
      },
      "egressAccessLogs": {
        "logGroupName": "string"
      },
      "description": "string",
      "hlsIngest": {
        "ingestEndpoints": [
          {
            "password": "string",
            "id": "string",
            "url": "string",
            "username": "string"
          }
        ]
      },
      "id": "string",
      "arn": "string",
      "tags": {
      }
    }
  ],
  "nextToken": "string"
}
```

#### Channel schema
<a name="channels-response-body-channel-example"></a>

```
{
  "createdAt": "string",
  "ingressAccessLogs": {
    "logGroupName": "string"
  },
  "egressAccessLogs": {
    "logGroupName": "string"
  },
  "description": "string",
  "hlsIngest": {
    "ingestEndpoints": [
      {
        "password": "string",
        "id": "string",
        "url": "string",
        "username": "string"
      }
    ]
  },
  "id": "string",
  "arn": "string",
  "tags": {
  }
}
```

## Properties
<a name="channels-properties"></a>

### Channel
<a name="channels-model-channel"></a>

Channel configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The channel's unique system-generated resource name, based on the AWS record. |
| createdAt | string | False | The date and time the Channel was created. |
| description | string | False | Any descriptive information that you want to add to the channel for future identification purposes. |
| egressAccessLogs | [EgressAccessLogs](#channels-model-egressaccesslogs) | False | Configures egress access logs. |
| hlsIngest | [HlsIngest](#channels-model-hlsingest) | False | System-generated information about the channel. |
| id | string | False | Unique identifier that you assign to the channel. |
| ingressAccessLogs | [IngressAccessLogs](#channels-model-ingressaccesslogs) | False | Configures ingress access logs. |
| tags | [Tags](#channels-model-tags) | False | The tags assigned to the channel. |

### ChannelCreateParameters
<a name="channels-model-channelcreateparameters"></a>

Channel configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | Any descriptive information that you want to add to the channel for future identification purposes. |
| id | string | True | Unique identifier that you assign to the channel. Supported characters are numbers, letters, underscores (\_), and dashes (-) with a length of 1 to 256 characters.  |
| tags | [Tags](#channels-model-tags) | False | The tags to assign to the channel. |

### ChannelList
<a name="channels-model-channellist"></a>

A collection of Channel records.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | Array of type [Channel](#channels-model-channel) | False | List of channel objects that are configured on this account. |
| nextToken | string | False | Pagination token. Use this token to request the next page of channel results. |

### EgressAccessLogs
<a name="channels-model-egressaccesslogs"></a>

Egress access log configuration parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom AWS CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/EgressAccessLogs`. |

### HlsIngest
<a name="channels-model-hlsingest"></a>

HLS ingest configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ingestEndpoints | Array of type [IngestEndpoint](#channels-model-ingestendpoint) | False | The input URL where the source stream should be sent. |

### IngestEndpoint
<a name="channels-model-ingestendpoint"></a>

An endpoint for ingesting source content for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The system-generated unique identifier for the IngestEndpoint. |
| password | string | False | The system-generated password for WebDAV input authentication. |
| url | string | False | The input URL where the source stream should be sent. |
| username | string | False | The system-generated username for WebDAV input authentication. |

### IngressAccessLogs
<a name="channels-model-ingressaccesslogs"></a>

Ingress access log configuration parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom AWS CloudWatch log group name for ingress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/IngressAccessLogs`. |

### Tags
<a name="channels-model-tags"></a>

A collection of tags associated with a resource.

Value description:
+  **Property**: `"{{key1}}": "{{value1}}"`
+  **Type**: string
+  **Required**: True
+  **Description**: A comma-separated list of tag key:value pairs that you define. For example:

  ```
   {
     "Key1": "Value1",
     "Key2": "Value2"
   }
  ```

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="channels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListChannels
<a name="ListChannels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/ListChannels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/ListChannels)

### CreateChannel
<a name="CreateChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/CreateChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/CreateChannel)
