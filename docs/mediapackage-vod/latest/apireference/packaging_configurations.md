---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations.html
---

# Packaging\_configurations
<a name="packaging_configurations"></a>

## URI
<a name="packaging_configurations-url"></a>

`/packaging_configurations`

## HTTP methods
<a name="packaging_configurations-http-methods"></a>

### GET
<a name="packaging_configurationsget"></a>

**Operation ID:** `ListPackagingConfigurations`

Lists packaging configurations that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| packagingGroupId | String | False | Limits the results to records that are associated with the given packaging group. |
| nextToken | String | False | Pagination token. Use this token to request the next page of record results. |
| maxResults | String | False | Upper bound on number of records to return. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PackagingConfigurationList |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="packaging_configurationspost"></a>

**Operation ID:** `CreatePackagingConfiguration`

Creates a packaging configuration in a packaging group.

The packaging configuration represents a single delivery point for an asset. It determines how the output from this endpoint is formatted.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PackagingConfiguration |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="packaging_configurationsoptions"></a>

Enable cross-origin resource sharing (CORS) by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None |  `200 OK` response<br />The list of tags is returned successfully. |

## Schemas
<a name="packaging_configurations-schemas"></a>

### Request bodies
<a name="packaging_configurations-request-examples"></a>

#### POST schema
<a name="packaging_configurations-request-body-post-example"></a>

```
{
  "packagingGroupId": "string",
  "dashPackage": {
    "includeEncoderConfigurationInSegments": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "segmentTemplateFormat": enum,
    "includeIframeOnlyStream": boolean,
    "periodTriggers": [
      enum
    ],
    "dashManifests": [
      {
        "minBufferTimeSeconds": integer,
        "manifestName": "string",
        "profile": enum,
        "manifestLayout": enum,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "scteMarkersSource": enum
      }
    ]
  },
  "id": "string",
  "cmafPackage": {
    "includeEncoderConfigurationInSegments": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "repeatExtXKey": boolean,
        "adMarkers": enum,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean
      }
    ]
  },
  "hlsPackage": {
    "useAudioRenditionGroup": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "repeatExtXKey": boolean,
        "adMarkers": enum,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean
      }
    ],
    "includeDvbSubtitles": boolean
  },
  "mssPackage": {
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "mssManifests": [
      {
        "manifestName": "string",
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        }
      }
    ]
  },
  "tags": {
  }
}
```

### Response bodies
<a name="packaging_configurations-response-examples"></a>

#### PackagingConfigurationList schema
<a name="packaging_configurations-response-body-packagingconfigurationlist-example"></a>

```
{
  "nextToken": "string",
  "packagingConfigurations": [
    {
      "createdAt": "string",
      "packagingGroupId": "string",
      "dashPackage": {
        "includeEncoderConfigurationInSegments": boolean,
        "segmentDurationSeconds": integer,
        "encryption": {
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "segmentTemplateFormat": enum,
        "includeIframeOnlyStream": boolean,
        "periodTriggers": [
          enum
        ],
        "dashManifests": [
          {
            "minBufferTimeSeconds": integer,
            "manifestName": "string",
            "profile": enum,
            "manifestLayout": enum,
            "streamSelection": {
              "streamOrder": enum,
              "maxVideoBitsPerSecond": integer,
              "minVideoBitsPerSecond": integer
            },
            "scteMarkersSource": enum
          }
        ]
      },
      "id": "string",
      "arn": "string",
      "cmafPackage": {
        "includeEncoderConfigurationInSegments": boolean,
        "segmentDurationSeconds": integer,
        "encryption": {
          "constantInitializationVector": "string",
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "hlsManifests": [
          {
            "repeatExtXKey": boolean,
            "adMarkers": enum,
            "manifestName": "string",
            "programDateTimeIntervalSeconds": integer,
            "streamSelection": {
              "streamOrder": enum,
              "maxVideoBitsPerSecond": integer,
              "minVideoBitsPerSecond": integer
            },
            "includeIframeOnlyStream": boolean
          }
        ]
      },
      "hlsPackage": {
        "useAudioRenditionGroup": boolean,
        "segmentDurationSeconds": integer,
        "encryption": {
          "constantInitializationVector": "string",
          "encryptionMethod": enum,
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "hlsManifests": [
          {
            "repeatExtXKey": boolean,
            "adMarkers": enum,
            "manifestName": "string",
            "programDateTimeIntervalSeconds": integer,
            "streamSelection": {
              "streamOrder": enum,
              "maxVideoBitsPerSecond": integer,
              "minVideoBitsPerSecond": integer
            },
            "includeIframeOnlyStream": boolean
          }
        ],
        "includeDvbSubtitles": boolean
      },
      "mssPackage": {
        "segmentDurationSeconds": integer,
        "encryption": {
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "mssManifests": [
          {
            "manifestName": "string",
            "streamSelection": {
              "streamOrder": enum,
              "maxVideoBitsPerSecond": integer,
              "minVideoBitsPerSecond": integer
            }
          }
        ]
      },
      "tags": {
      }
    }
  ]
}
```

#### PackagingConfiguration schema
<a name="packaging_configurations-response-body-packagingconfiguration-example"></a>

```
{
  "createdAt": "string",
  "packagingGroupId": "string",
  "dashPackage": {
    "includeEncoderConfigurationInSegments": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "segmentTemplateFormat": enum,
    "includeIframeOnlyStream": boolean,
    "periodTriggers": [
      enum
    ],
    "dashManifests": [
      {
        "minBufferTimeSeconds": integer,
        "manifestName": "string",
        "profile": enum,
        "manifestLayout": enum,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "scteMarkersSource": enum
      }
    ]
  },
  "id": "string",
  "arn": "string",
  "cmafPackage": {
    "includeEncoderConfigurationInSegments": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "repeatExtXKey": boolean,
        "adMarkers": enum,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean
      }
    ]
  },
  "hlsPackage": {
    "useAudioRenditionGroup": boolean,
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "repeatExtXKey": boolean,
        "adMarkers": enum,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean
      }
    ],
    "includeDvbSubtitles": boolean
  },
  "mssPackage": {
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "mssManifests": [
      {
        "manifestName": "string",
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        }
      }
    ]
  },
  "tags": {
  }
}
```

## Properties
<a name="packaging_configurations-properties"></a>

### CmafEncryption
<a name="packaging_configurations-model-cmafencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantInitializationVector | string | False | An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV). |
| spekeKeyProvider | [SpekeKeyProvider](#packaging_configurations-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### CmafPackage
<a name="packaging_configurations-model-cmafpackage"></a>

Parameters for a packaging configuration that uses Common Media Application Format (CMAF) packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [CmafEncryption](#packaging_configurations-model-cmafencryption) | False | Parameters for encrypting content. |
| hlsManifests | Array of type [HlsManifest](#packaging_configurations-model-hlsmanifest) | True | A list of HLS manifest configurations available from this endpoint. |
| includeEncoderConfigurationInSegments | boolean | False | When true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source fragment duration.  |

### DashEncryption
<a name="packaging_configurations-model-dashencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spekeKeyProvider | [SpekeKeyProvider](#packaging_configurations-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### DashManifest
<a name="packaging_configurations-model-dashmanifest"></a>

Parameters for a DASH manifest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestLayout | string<br />Values: `FULL \| COMPACT` | False | Determines the position of some tags in the Media Presentation Description (MPD).<br />Value description:+   `FULL` - Elements like `SegmentTemplate` and `ContentProtection` are included in each `Representation`. <br />+   `COMPACT` - Duplicate elements are combined and presented at the `AdaptationSet` level.  |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration. |
| minBufferTimeSeconds | integer | False | Minimum amount of content (measured in seconds) that a player must keep available in the buffer. |
| profile | string<br />Values: `NONE \| HBBTV_1_5` | False | The DASH profile type for the ouput.<br />Value description:+   `NONE` - The output doesn't use a DASH profile. <br />+   `HBBTV_1_5` - The output is compliant with HbbTV v1.5. For information about HbbTV v1.5, see the [HbbTV specification website](https://www.hbbtv.org/resource-library/specifications/).  |
| scteMarkersSource | string<br />Values: `SEGMENTS \| MANIFEST` | False | The source of scte markers used.<br />Value description:+  `SEGMENTS` - The scte markers are sourced from the segments of the ingested content. <br />+  `MANIFEST` - the scte markers are sourced from the manifest of the ingested content. The MANIFEST value is compatible with source HLS playlists using the SCTE-35 Enhanced syntax (`EXT-OATCLS-SCTE35` tags). SCTE-35 Elemental and SCTE-35 Daterange syntaxes are not supported with this option.  |
| streamSelection | [StreamSelection](#packaging_configurations-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate. |

### DashPackage
<a name="packaging_configurations-model-dashpackage"></a>

Parameters for a packaging configuration that uses DASH packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dashManifests | Array of type [DashManifest](#packaging_configurations-model-dashmanifest) | True | A list of DASH manifest configurations available from this endpoint. |
| encryption | [DashEncryption](#packaging_configurations-model-dashencryption) | False | Parameters for encrypting content. |
| includeEncoderConfigurationInSegments | boolean | False | When true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback. |
| includeIframeOnlyStream | boolean | False | This applies only to stream sets with a single video track. When true, the stream set includes an additional I-frame trick-play only stream, along with the other tracks. If false, this extra stream is not included. |
| periodTriggers | Array of type string<br />Values: `ADS` | False | A list of triggers that controls when the outgoing DASH Media Presentation Description (MPD) will be partitioned into multiple periods.<br />Value description:+  `NONE` - The entire duration of the ouput manifest is included in a single period. <br />+  `ADS` - Multiple periods are added to the output manifest based on SCTE-35 ad markers in the source video stream.  |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source segment duration.  |
| segmentTemplateFormat | string<br />Values: `NUMBER_WITH_TIMELINE \| TIME_WITH_TIMELINE \| NUMBER_WITH_DURATION` | False | Determines the type of SegmentTemplate included in the MPD.<br />Value description:+   `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate`. <br />+   `TIME_WITH_TIMELINE` - The `$Time$` variable is used in the `media` URL. The value of this variable is the timestamp of when the segment starts. A full `SegmentTimeline` object is presented in each `SegmentTemplate`. <br />+   `NUMBER_WITH_DURATION` - The `$Number$` variable is used in the `media ` URL and a `duration` attribute is added to the segment template. The `SegmentTimeline` object is removed from the representation.  |

### EncryptionContractConfiguration
<a name="packaging_configurations-model-encryptioncontractconfiguration"></a>

Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines the content keys used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. For more information about these presets, see [SPEKE Version 2.0 Presets](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html).

Note the following considerations when using `encryptionContractConfiguration`:
+ You can use `encryptionContractConfiguration` for DASH endpoints that use SPEKE Version 2.0. SPEKE Version 2.0 relies on the CPIX Version 2.3 specification.
+ You cannot combine an `UNENCRYPTED` preset with `UNENCRYPTED` or `SHARED` presets across `presetSpeke20Audio` and `presetSpeke20Video`.
+ When you use a `SHARED` preset, you must use it for both `presetSpeke20Audio` and `presetSpeke20Video`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| presetSpeke20Audio | string<br />Values: `PRESET-AUDIO-1 \| PRESET-AUDIO-2 \| PRESET-AUDIO-3 \| SHARED \| UNENCRYPTED` | True | A collection of audio encryption presets.<br />Value description:+  `PRESET-AUDIO-1` - Use one content key to encrypt all of the audio tracks in your stream. <br />+  `PRESET-AUDIO-2` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks. <br />+  `PRESET-AUDIO-3` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels. <br />+  `SHARED` - Use the same content key for all of the audio and video tracks in your stream. <br />+  `UNENCRYPTED` - Don't encrypt any of the audio tracks in your stream.  |
| presetSpeke20Video | string<br />Values: `PRESET-VIDEO-1 \| PRESET-VIDEO-2 \| PRESET-VIDEO-3 \| PRESET-VIDEO-4 \| PRESET-VIDEO-5 \| PRESET-VIDEO-6 \| PRESET-VIDEO-7 \| PRESET-VIDEO-8 \| SHARED \| UNENCRYPTED` | True | A collection of video encryption presets.<br />Value description: +   `PRESET-VIDEO-1` - Use one content key to encrypt all of the video tracks in your stream. <br />+   `PRESET-VIDEO-2` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks. <br />+   `PRESET-VIDEO-3` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-4` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `PRESET-VIDEO-5` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `PRESET-VIDEO-6` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-7` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-8` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `SHARED` - Use the same content key for all of the video and audio tracks in your stream. <br />+   `UNENCRYPTED` - Don't encrypt any of the video tracks in your stream.  |

### HlsEncryption
<a name="packaging_configurations-model-hlsencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantInitializationVector | string | False | A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a constant initialization vector (IV), MediaPackage periodically rotates the IV. |
| encryptionMethod | string<br />Values: `AES_128 \| SAMPLE_AES` | False | HLS encryption type. |
| spekeKeyProvider | [SpekeKeyProvider](#packaging_configurations-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### HlsManifest
<a name="packaging_configurations-model-hlsmanifest"></a>

Parameters for an HLS manifest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | string<br />Values: `NONE \| SCTE35_ENHANCED \| PASSTHROUGH` | False | This setting controls ad markers in the packaged content.<br />Value description:+  `NONE` - Omits SCTE-35 ad markers from the output. <br />+  `SCTE35_ENHANCED` - Generates ad markers and blackout tags in the output, based on SCTE-35 messages in the source content. <br />+  `PASSTHROUGH` - Copies SCTE-35 ad markers from the source content to the output.  |
| includeIframeOnlyStream | boolean | False | Applies to stream sets with a single video track only. When enabled, the output includes an additional I-frame only trick-play stream, along with the other tracks. |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration. |
| programDateTimeIntervalSeconds | integer | False | Inserts `EXT-X-PROGRAM-DATE-TIME` tags in the output manifest at the interval that you specify. Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested.<br />Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it's passed through to the HLS output.<br />Omit this attribute or enter `0` to indicate that the `EXT-X-PROGRAM-DATE-TIME` tags are not included in the manifest. |
| repeatExtXKey | boolean | False | Repeat the `EXT-X-KEY` directive for every media segment. This might result in an increase in client requests to the DRM server. |
| streamSelection | [StreamSelection](#packaging_configurations-model-streamselection) | False | Video bitrate limitations for outputs from this packaging configuration. |

### HlsPackage
<a name="packaging_configurations-model-hlspackage"></a>

Parameters for a packaging configuration that uses HTTP Live Streaming (HLS) packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [HlsEncryption](#packaging_configurations-model-hlsencryption) | False | Parameters for encrypting content. |
| hlsManifests | Array of type [HlsManifest](#packaging_configurations-model-hlsmanifest) | True | A list of HLS manifest configurations available from this endpoint. |
| includeDvbSubtitles | boolean | False | When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.  |
| useAudioRenditionGroup | boolean | False | When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group. |

### MssEncryption
<a name="packaging_configurations-model-mssencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spekeKeyProvider | [SpekeKeyProvider](#packaging_configurations-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### MssManifest
<a name="packaging_configurations-model-mssmanifest"></a>

Parameters for a Microsoft Smooth manifest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration. |
| streamSelection | [StreamSelection](#packaging_configurations-model-streamselection) | False | Video bitrate limitations for outputs from this packaging configuration. |

### MssPackage
<a name="packaging_configurations-model-msspackage"></a>

Parameters for a packaging configuration that uses Microsoft Smooth Streaming (MSS) packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [MssEncryption](#packaging_configurations-model-mssencryption) | False | Parameters for encrypting content. |
| mssManifests | Array of type [MssManifest](#packaging_configurations-model-mssmanifest) | True | A list of Microsoft Smooth manifest configurations available from this endpoint. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration. |

### PackagingConfiguration
<a name="packaging_configurations-model-packagingconfiguration"></a>

PackagingConfiguration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) for the packaging configuration. You can get this from the response to any request to the packaging configuration. |
| cmafPackage | [CmafPackage](#packaging_configurations-model-cmafpackage) | False | Parameters for CMAF packaging. |
| createdAt | string | False | The date and time the PackagingConfiguration was created. |
| dashPackage | [DashPackage](#packaging_configurations-model-dashpackage) | False | Parameters for DASH-ISO packaging. |
| hlsPackage | [HlsPackage](#packaging_configurations-model-hlspackage) | False | Parameters for Apple HLS packaging. |
| id | string | False | Unique identifier that you assign to the packaging configuration. |
| mssPackage | [MssPackage](#packaging_configurations-model-msspackage) | False | Parameters for Microsoft Smooth Streaming packaging. |
| packagingGroupId | string | False | The ID of the packaging group associated with this packaging configuration. |
| tags | [Tags](#packaging_configurations-model-tags) | False | The tags to assign to the packaging configuration. |

### PackagingConfigurationCreateParameters
<a name="packaging_configurations-model-packagingconfigurationcreateparameters"></a>

Parameters for creating a packaging configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cmafPackage | [CmafPackage](#packaging_configurations-model-cmafpackage) | False | Parameters for CMAF packaging. |
| dashPackage | [DashPackage](#packaging_configurations-model-dashpackage) | False | Parameters for DASH-ISO packaging. |
| hlsPackage | [HlsPackage](#packaging_configurations-model-hlspackage) | False | Parameters for Apple HLS packaging. |
| id | string | True | Unique identifier that you assign to the packaging configuration. |
| mssPackage | [MssPackage](#packaging_configurations-model-msspackage) | False | Parameters for Microsoft Smooth Streaming packaging.  |
| packagingGroupId | string | True | The ID of the packaging group associated with this packaging configuration. |
| tags | [Tags](#packaging_configurations-model-tags) | False | The tags to assign to the packaging configuration. |

### PackagingConfigurationList
<a name="packaging_configurations-model-packagingconfigurationlist"></a>

A collection of PackagingConfiguration records.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Pagination token. Use this token to request the next page of packaging configuration results. |
| packagingConfigurations | Array of type [PackagingConfiguration](#packaging_configurations-model-packagingconfiguration) | False | A list of PackagingConfiguration records. |

### SpekeKeyProvider
<a name="packaging_configurations-model-spekekeyprovider"></a>

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionContractConfiguration | [EncryptionContractConfiguration](#packaging_configurations-model-encryptioncontractconfiguration) | False | Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. |
| roleArn | string | True | The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows AWS Elemental MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Valid format: `arn:aws:iam::{accountID}:role/{name}`  |
| systemIds | Array of type string | True | List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.  |
| url | string | True | URL for the key provider’s key retrieval API endpoint. Must start with https://. |

### StreamSelection
<a name="packaging_configurations-model-streamselection"></a>

Limitations for outputs from the endpoint, based on the video bitrate.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxVideoBitsPerSecond | integer | False | The upper limit of the bitrates that this endpoint serves. If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.  |
| minVideoBitsPerSecond | integer | False | The lower limit of the bitrates that this endpoint serves. If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.  |
| streamOrder | string<br />Values: `ORIGINAL \| VIDEO_BITRATE_ASCENDING \| VIDEO_BITRATE_DESCENDING` | False | Order in which the different video bitrates are presented to the player. |

### Tags
<a name="packaging_configurations-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |
