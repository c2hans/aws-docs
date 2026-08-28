---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/actions-GetClientConfiguration.html
---

# GetClientConfiguration
<a name="actions-GetClientConfiguration"></a>

Returns video and audio configurations that optimize the viewing experience based on the client’s hardware and software configuration, user preferences, and limits of the video service.

## Request Syntax
<a name="actions-GetClientConfiguration-request-syntax"></a>

```
POST /GetClientConfiguration
https://ingest.contribute.live-video.net/api/v3/GetClientConfiguration HTTP/1.1
Content-type: application/json
{
   "authentication": "string",
   "capabilities": {
      "cpu": {
         "logical_cores": number,
         "name": "string",
         "physical_cores": number,
         "speed": number
      },
      "gaming_features": {
         "game_dvr_enabled": boolean,
         "hags_enabled": boolean
      },
      "gpu": [
         {
            "dedicated_video_memory": number,
            "device_id": number,
            "driver_version": "string",
            "luid": "string",
            "model": string,
            "shared_system_memory": number,
            "vendor_id": number
         }
      ],
      "memory": {
         "free": number,
         "total": number
      },
      "system": {
         "arm": boolean,
         "arm_emulation": boolean,
         "bits": number,
         "build": number,
         "name": "string",
         "release": "string",
         "revision": "string",
         "version": "string"
      }
   },
   "client": {
      "name": "string",
      "version": "string",
      "supported_codecs": [ "string" ]
   },
   "preferences": {
      "canvas_height": number,
      "canvas_width": number,
      "composition_gpu_index": number,
      "framerate": {
        "denominator": number,
        "numerator": number
      },
      "height": number,
      "maximum_streaming_bandwidth": number,
      "maximum_resolution": "string",
      "maximum_video_tracks": number,
      "vod_track_audio": boolean,
      "width": number
   },
   "schema_version": "string",
   "service": "string",
   "stream_attempt_start_time": "string"
}
```

## URI Request Parameters
<a name="actions-GetClientConfiguration-uri-request-params"></a>

The request does not use any URI parameters.

## Request Body
<a name="actions-GetClientConfiguration-request-body"></a>

The request accepts the following data in JSON format.
+ **authentication**
  + Stream key associated with the channel.
  + Type: String
  + Required: Yes
+ **capabilities**
  + Description of the client’s capabilities.
  + Type: [CapabilitiesDescription](structures-CapabilitiesDescription.md) object
  + Required: Yes
+ **client**
  + Client software characteristics.
  + Type: [Client](structures-Client.md) object
  + Required: Yes
+ **preferences**
  + Preferences configured on the client.
  + Type: [PreferencesDescription](structures-PreferencesDescription.md) object
  + Required: No
+ **service**
  + Name of the video service.
  + Type: String
  + Valid Values: `IVS`
  + Required: Yes
+ **schema\_version**
  + Schema version supported by the client. The schema version format is `YYYY-MM-DD`.
  + Type: String
  + Valid Values: `2024-06-04`
  + Required: Yes
+ **stream\_attempt\_start\_time**
  + Attempted stream start time, in the [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) format.
  + Type: String
  + Required: Yes

## Response Syntax
<a name="actions-GetClientConfiguration-response-syntax"></a>

```
HTTP/1.1 200
Content-type: application/json
{
   "audio_configurations": {
      "live": [
         {
            "channels": number,
            "codec": "string",
            "settings": [
               "bitrate": number
            ],
            "track_id": number
         }
      ],
      "vod": [
         {
            "channels": number,
            "codec": "string",
            "settings": [
               "bitrate": number
            ],
            "track_id": number
         }
      ]
   },
   "encoder_configurations": [
      {
         "bitrate_interpolation_points": [ number ],
         "framerate": {
            "denominator": number,
            "numerator": number
         },
         "gpu_scale_type": "string",
         "height": number,
         "settings": {
            "bf": number,
            "bitrate": number,
            "keyint_sec": number,
            "lookahead": boolean,
            "preset2": "string",
            "profile": "string",
            "psycho_aq": boolean,
            "rate_control": "string",
            "tune": "string"
         },
         "type": "string",
         "width": number
      },
   ],
   "ingest_endpoints": [
      {
         "authentication": "string",
         "protocol": "string",
         "url_template": "string"
      }
   ],
   "meta": {
      "config_id": "string",
      "schema_version": "string",
      "service": "string"
   },
   "status": {
      "html_en_us": "string",
      "result": "string"
   }
}
```

## Response Elements
<a name="actions-GetClientConfiguration-response-elements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.
+ **audio\_configurations**
  + Audio configurations for the live stream and for video on demand based on the client configuration and preferences.
  + Type: [AudioConfiguration](structures-AudioConfiguration.md) object
  + Required: Yes
+ **encoder\_configurations**
  + Encoder configurations that the client should use based on the client configuration and preferences.
  + Type: Array of [EncoderConfiguration](structures-EncoderConfiguration.md) objects
  + Required: Yes
+ **ingest\_endpoints**
  + Available ingest endpoints based on the client configuration and preferences.
  + Type: Array of [IngestEndpoint](structures-IngestEndpoint.md) objects
  + Required: Yes
+ **meta**
  + Information identifying the configuration.
  + Type: [ConfigurationMetadata](structures-ConfigurationMetadata.md) object
  + Required: Yes
+ **status**
  + Error or warning information to be exposed to the broadcaster.
  + Type: [ClientConfigurationStatus](structures-ClientConfigurationStatus.md) object
  + Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
