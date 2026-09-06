---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-credentials.html
---

# Channels id Credentials
<a name="channels-id-credentials"></a>

## URI
<a name="channels-id-credentials-url"></a>

`/channels/{{id}}/credentials`

## HTTP methods
<a name="channels-id-credentials-http-methods"></a>

### PUT
<a name="channels-id-credentialsput"></a>

**Operation ID:** `RotateChannelCredentials`

Changes the username and password of the first IngestEndpoint on the channel.

**Important**
This API is being deprecated. Use RotateIngestEndpointCredentials instead.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you are working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Channel |  `200 OK` response<br />New WebDAV credentials are generated successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="channels-id-credentialsoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you are working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="channels-id-credentials-schemas"></a>

### Response bodies
<a name="channels-id-credentials-response-examples"></a>

#### Channel schema
<a name="channels-id-credentials-response-body-channel-example"></a>

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
<a name="channels-id-credentials-properties"></a>

### Channel
<a name="channels-id-credentials-model-channel"></a>

Channel configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The channel's unique system-generated resource name, based on the AWS record. |
| createdAt | string | False | The date and time the Channel was created. |
| description | string | False | Any descriptive information that you want to add to the channel for future identification purposes. |
| egressAccessLogs | [EgressAccessLogs](#channels-id-credentials-model-egressaccesslogs) | False | Configures egress access logs. |
| hlsIngest | [HlsIngest](#channels-id-credentials-model-hlsingest) | False | System-generated information about the channel. |
| id | string | False | Unique identifier that you assign to the channel. |
| ingressAccessLogs | [IngressAccessLogs](#channels-id-credentials-model-ingressaccesslogs) | False | Configures ingress access logs. |
| tags | [Tags](#channels-id-credentials-model-tags) | False | The tags assigned to the channel. |

### EgressAccessLogs
<a name="channels-id-credentials-model-egressaccesslogs"></a>

Egress access log configuration parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom AWS CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/EgressAccessLogs`. |

### HlsIngest
<a name="channels-id-credentials-model-hlsingest"></a>

HLS ingest configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ingestEndpoints | Array of type [IngestEndpoint](#channels-id-credentials-model-ingestendpoint) | False | The input URL where the source stream should be sent. |

### IngestEndpoint
<a name="channels-id-credentials-model-ingestendpoint"></a>

An endpoint for ingesting source content for a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The system-generated unique identifier for the IngestEndpoint. |
| password | string | False | The system-generated password for WebDAV input authentication. |
| url | string | False | The input URL where the source stream should be sent. |
| username | string | False | The system-generated username for WebDAV input authentication. |

### IngressAccessLogs
<a name="channels-id-credentials-model-ingressaccesslogs"></a>

Ingress access log configuration parameters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom AWS CloudWatch log group name for ingress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/IngressAccessLogs`. |

### Tags
<a name="channels-id-credentials-model-tags"></a>

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
<a name="channels-id-credentials-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RotateChannelCredentials
<a name="RotateChannelCredentials-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/RotateChannelCredentials)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/RotateChannelCredentials)
