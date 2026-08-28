---
source_url: https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints.html
---

# Origin\_endpoints
<a name="origin_endpoints"></a>

## URI
<a name="origin_endpoints-url"></a>

`/origin_endpoints`

## HTTP methods
<a name="origin_endpoints-http-methods"></a>

### GET
<a name="origin_endpointsget"></a>

**Operation ID:** `ListOriginEndpoints`

Lists endpoints that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | Pagination token from the GET list request. Use the token to fetch the next page of results. |
| maxResults | String | False | Upper bound on number of records to return. |
| channelId | String | False | Limits results to endpoints associated with the given channel ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | OriginEndpointList |  `200 OK` response<br />The list of endpoints is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="origin_endpointspost"></a>

**Operation ID:** `CreateOriginEndpoint`

Create an endpoint on an AWS Elemental MediaPackage channel.

An endpoint represents a single delivery point of a channel, and defines content output handling through various components, such as packaging protocols, DRM and encryption integration, and more.

Once created, an endpoint provides a fixed public URL. This URL remains the same throughout the lifetime of the endpoint, regardless of any failures or upgrades that might occur. Integrate the URL with a downstream CDN (such as Amazon CloudFront) or playback device.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | OriginEndpoint |  `200 OK` response<br />The endpoint is created successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="origin_endpointsoptions"></a>

Enable CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="origin_endpoints-schemas"></a>

### Request bodies
<a name="origin_endpoints-request-examples"></a>

#### POST schema
<a name="origin_endpoints-request-body-post-example"></a>

```
{
  "startoverWindowSeconds": integer,
  "manifestName": "string",
  "description": "string",
  "dashPackage": {
    "manifestWindowSeconds": integer,
    "segmentDurationSeconds": integer,
    "utcTimingUri": "string",
    "profile": enum,
    "utcTiming": enum,
    "manifestLayout": enum,
    "segmentTemplateFormat": enum,
    "minUpdatePeriodSeconds": integer,
    "minBufferTimeSeconds": integer,
    "encryption": {
      "keyRotationIntervalSeconds": integer,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "includeIframeOnlyStream": boolean,
    "periodTriggers": [
      enum
    ],
    "suggestedPresentationDelaySeconds": integer,
    "adTriggers": [
      enum
    ],
    "adsOnDeliveryRestrictions": enum
  },
  "whitelist": [
    "string"
  ],
  "cmafPackage": {
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "keyRotationIntervalSeconds": integer,
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "adMarkers": enum,
        "playlistWindowSeconds": integer,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "playlistType": enum,
        "id": "string",
        "includeIframeOnlyStream": boolean,
        "adTriggers": [
          enum
        ],
        "adsOnDeliveryRestrictions": enum
      }
    ],
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "segmentPrefix": "string"
  },
  "hlsPackage": {
    "useAudioRenditionGroup": boolean,
    "segmentDurationSeconds": integer,
    "adMarkers": enum,
    "encryption": {
      "repeatExtXKey": boolean,
      "constantInitializationVector": "string",
      "keyRotationIntervalSeconds": integer,
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "playlistWindowSeconds": integer,
    "includeDvbSubtitles": boolean,
    "programDateTimeIntervalSeconds": integer,
    "playlistType": enum,
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "includeIframeOnlyStream": boolean,
    "adTriggers": [
      enum
    ],
    "adsOnDeliveryRestrictions": enum
  },
  "tags": {
  },
  "authorization": {
    "cdnIdentifierSecret": "string",
    "secretsRoleArn": "string"
  },
  "origination": enum,
  "timeDelaySeconds": integer,
  "id": "string",
  "channelId": "string",
  "mssPackage": {
    "manifestWindowSeconds": integer,
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    }
  }
}
```

### Response bodies
<a name="origin_endpoints-response-examples"></a>

#### OriginEndpointList schema
<a name="origin_endpoints-response-body-originendpointlist-example"></a>

```
{
  "originEndpoints": [
    {
      "startoverWindowSeconds": integer,
      "manifestName": "string",
      "description": "string",
      "dashPackage": {
        "manifestWindowSeconds": integer,
        "segmentDurationSeconds": integer,
        "utcTimingUri": "string",
        "profile": enum,
        "utcTiming": enum,
        "manifestLayout": enum,
        "segmentTemplateFormat": enum,
        "minUpdatePeriodSeconds": integer,
        "minBufferTimeSeconds": integer,
        "encryption": {
          "keyRotationIntervalSeconds": integer,
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "resourceId": "string",
            "certificateArn": "string",
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean,
        "periodTriggers": [
          enum
        ],
        "suggestedPresentationDelaySeconds": integer,
        "adTriggers": [
          enum
        ],
        "adsOnDeliveryRestrictions": enum
      },
      "whitelist": [
        "string"
      ],
      "cmafPackage": {
        "segmentDurationSeconds": integer,
        "encryption": {
          "constantInitializationVector": "string",
          "keyRotationIntervalSeconds": integer,
          "encryptionMethod": enum,
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "resourceId": "string",
            "certificateArn": "string",
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "hlsManifests": [
          {
            "adMarkers": enum,
            "playlistWindowSeconds": integer,
            "manifestName": "string",
            "programDateTimeIntervalSeconds": integer,
            "playlistType": enum,
            "id": "string",
            "includeIframeOnlyStream": boolean,
            "url": "string"
          }
        ],
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "segmentPrefix": "string"
      },
      "hlsPackage": {
        "useAudioRenditionGroup": boolean,
        "segmentDurationSeconds": integer,
        "adMarkers": enum,
        "encryption": {
          "repeatExtXKey": boolean,
          "constantInitializationVector": "string",
          "keyRotationIntervalSeconds": integer,
          "encryptionMethod": enum,
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "resourceId": "string",
            "certificateArn": "string",
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "playlistWindowSeconds": integer,
        "includeDvbSubtitles": boolean,
        "programDateTimeIntervalSeconds": integer,
        "playlistType": enum,
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        },
        "includeIframeOnlyStream": boolean,
        "adTriggers": [
          enum
        ],
        "adsOnDeliveryRestrictions": enum
      },
      "url": "string",
      "tags": {
      },
      "authorization": {
        "cdnIdentifierSecret": "string",
        "secretsRoleArn": "string"
      },
      "createdAt": "string",
      "origination": enum,
      "timeDelaySeconds": integer,
      "id": "string",
      "arn": "string",
      "channelId": "string",
      "mssPackage": {
        "manifestWindowSeconds": integer,
        "segmentDurationSeconds": integer,
        "encryption": {
          "spekeKeyProvider": {
            "encryptionContractConfiguration": {
              "presetSpeke20Audio": enum,
              "presetSpeke20Video": enum
            },
            "resourceId": "string",
            "certificateArn": "string",
            "systemIds": [
              "string"
            ],
            "roleArn": "string",
            "url": "string"
          }
        },
        "streamSelection": {
          "streamOrder": enum,
          "maxVideoBitsPerSecond": integer,
          "minVideoBitsPerSecond": integer
        }
      }
    }
  ],
  "nextToken": "string"
}
```

#### OriginEndpoint schema
<a name="origin_endpoints-response-body-originendpoint-example"></a>

```
{
  "startoverWindowSeconds": integer,
  "manifestName": "string",
  "description": "string",
  "dashPackage": {
    "manifestWindowSeconds": integer,
    "segmentDurationSeconds": integer,
    "utcTimingUri": "string",
    "profile": enum,
    "utcTiming": enum,
    "manifestLayout": enum,
    "segmentTemplateFormat": enum,
    "minUpdatePeriodSeconds": integer,
    "minBufferTimeSeconds": integer,
    "encryption": {
      "keyRotationIntervalSeconds": integer,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "includeIframeOnlyStream": boolean,
    "periodTriggers": [
      enum
    ],
    "suggestedPresentationDelaySeconds": integer,
    "adTriggers": [
      enum
    ],
    "adsOnDeliveryRestrictions": enum
  },
  "whitelist": [
    "string"
  ],
  "cmafPackage": {
    "segmentDurationSeconds": integer,
    "encryption": {
      "constantInitializationVector": "string",
      "keyRotationIntervalSeconds": integer,
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "hlsManifests": [
      {
        "adMarkers": enum,
        "playlistWindowSeconds": integer,
        "manifestName": "string",
        "programDateTimeIntervalSeconds": integer,
        "playlistType": enum,
        "id": "string",
        "includeIframeOnlyStream": boolean,
        "url": "string"
      }
    ],
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "segmentPrefix": "string"
  },
  "hlsPackage": {
    "useAudioRenditionGroup": boolean,
    "segmentDurationSeconds": integer,
    "adMarkers": enum,
    "encryption": {
      "repeatExtXKey": boolean,
      "constantInitializationVector": "string",
      "keyRotationIntervalSeconds": integer,
      "encryptionMethod": enum,
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "playlistWindowSeconds": integer,
    "includeDvbSubtitles": boolean,
    "programDateTimeIntervalSeconds": integer,
    "playlistType": enum,
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    },
    "includeIframeOnlyStream": boolean,
    "adTriggers": [
      enum
    ],
    "adsOnDeliveryRestrictions": enum
  },
  "url": "string",
  "tags": {
  },
  "authorization": {
    "cdnIdentifierSecret": "string",
    "secretsRoleArn": "string"
  },
  "createdAt": "string",
  "origination": enum,
  "timeDelaySeconds": integer,
  "id": "string",
  "arn": "string",
  "channelId": "string",
  "mssPackage": {
    "manifestWindowSeconds": integer,
    "segmentDurationSeconds": integer,
    "encryption": {
      "spekeKeyProvider": {
        "encryptionContractConfiguration": {
          "presetSpeke20Audio": enum,
          "presetSpeke20Video": enum
        },
        "resourceId": "string",
        "certificateArn": "string",
        "systemIds": [
          "string"
        ],
        "roleArn": "string",
        "url": "string"
      }
    },
    "streamSelection": {
      "streamOrder": enum,
      "maxVideoBitsPerSecond": integer,
      "minVideoBitsPerSecond": integer
    }
  }
}
```

## Properties
<a name="origin_endpoints-properties"></a>

### AdsOnDeliveryRestrictions
<a name="origin_endpoints-model-adsondeliveryrestrictions"></a>

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad.

Value description:
+  `NONE` - No SCTE-35 messages become ads.
+  `RESTRICTED` - SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads.
+  `UNRESTRICTED` - SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads.
+  `BOTH` - All SCTE-35 messages of the types specified in AdTriggers will be treated as ads.

For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).
+ `NONE`
+ `RESTRICTED`
+ `UNRESTRICTED`
+ `BOTH`

### Authorization
<a name="origin_endpoints-model-authorization"></a>

Parameters for enabling CDN authorization on the endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cdnIdentifierSecret | string | True | The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that your Content Delivery Network (CDN) uses for authorization to access your endpoint.  |
| secretsRoleArn | string | True | The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.  |

### CmafEncryption
<a name="origin_endpoints-model-cmafencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantInitializationVector | string | False | An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV). |
| encryptionMethod | [CmafEncryptionMethod](#origin_endpoints-model-cmafencryptionmethod) | False | The encryption method to use. |
| keyRotationIntervalSeconds | integer | False | Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to `0` to disable key rotation.  |
| spekeKeyProvider | [SpekeKeyProvider](#origin_endpoints-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### CmafEncryptionMethod
<a name="origin_endpoints-model-cmafencryptionmethod"></a>

The encryption method to use.
+ `SAMPLE_AES`
+ `AES_CTR`

### CmafPackage
<a name="origin_endpoints-model-cmafpackage"></a>

Parameters for Common Media Application Format (CMAF) packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [CmafEncryption](#origin_endpoints-model-cmafencryption) | False | Parameters for encrypting content. |
| hlsManifests | Array of type [HlsManifest](#origin_endpoints-model-hlsmanifest) | False | A list of HLS manifest configurations available from this endpoint. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each segment. Actual segments are rounded to the nearest multiple of the source segment duration. |
| segmentPrefix | string | False | An optional custom string that is prepended to the name of each segment. If not specified, the segment prefix defaults to the ChannelId. |
| streamSelection | [StreamSelection](#origin_endpoints-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate.  |

### CmafPackageCreateOrUpdateParameters
<a name="origin_endpoints-model-cmafpackagecreateorupdateparameters"></a>

Parameters for creating an endpoint that supports Common Media Application Format (CMAF) packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [CmafEncryption](#origin_endpoints-model-cmafencryption) | False | Parameters for encrypting content. |
| hlsManifests | Array of type [HlsManifestCreateOrUpdateParameters](#origin_endpoints-model-hlsmanifestcreateorupdateparameters) | False | A list of HLS manifest configurations available from this endpoint. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each segment. Actual segments are rounded to the nearest multiple of the source segment duration.  |
| segmentPrefix | string | False | An optional custom string that is prepended to the name of each segment. If not specified, the segment prefix defaults to the ChannelId. |
| streamSelection | [StreamSelection](#origin_endpoints-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate.  |

### DashEncryption
<a name="origin_endpoints-model-dashencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| keyRotationIntervalSeconds | integer | False | Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to `0` to disable key rotation.  |
| spekeKeyProvider | [SpekeKeyProvider](#origin_endpoints-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### DashPackage
<a name="origin_endpoints-model-dashpackage"></a>

Parameters for DASH packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adsOnDeliveryRestrictions | [AdsOnDeliveryRestrictions](#origin_endpoints-model-adsondeliveryrestrictions) | False | The flags on SCTE-35 segmentation descriptors that have to be present for MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| adTriggers | Array of type string | False | The SCTE-35 message types that MediaPackage treats as ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| encryption | [DashEncryption](#origin_endpoints-model-dashencryption) | False | Parameters for encrypting content. |
| includeIframeOnlyStream | boolean | False | When enabled, an I-Frame only stream will be included in the output. |
| manifestLayout | string<br />Values: `FULL \| COMPACT` | False | Determines the position of some tags in the manifest. <br />Value description: +   `FULL` - Elements like `SegmentTemplate` and `ContentProtection` are included in each `Representation`. <br />+   `COMPACT` - Duplicate elements are combined and presented at the `AdaptationSet` level.  |
| manifestWindowSeconds | integer | False | Time window (in seconds) contained in each manifest. |
| minBufferTimeSeconds | integer | False | Minimum amount of content (measured in seconds) that a player must keep available in the buffer. |
| minUpdatePeriodSeconds | integer | False | Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. |
| periodTriggers | Array of type string<br />Values: `ADS` | False | A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Type **ADS** to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see [Multi-period DASH in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html).  |
| profile | string<br />Values: `NONE \| HBBTV_1_5 \| HYBRIDCAST \| DVB_DASH_2014` | False | The DASH profile for the output.<br />Value description: +   `NONE` - The output doesn't use a DASH profile. <br />+   `HBBTV_1_5` - The output is compliant with HbbTV v1.5. For information about HbbTV v1.5, see the [HbbTV specification website](https://www.hbbtv.org/resource-library/specifications/). <br />+   `HYBRIDCAST` - The output is compliant with Hybridcast. For more information about Hybridcast, see the [IPTV Forum Japan Hybridcast specification](https://www.iptvforum.jp/en/hybridcast/specification.html). <br />+   `DVB_DASH_2014` - The output is compliant with DVB-DASH 2014. For more information about DVB-DASH 2014, see the [DVB-DASH specification](https://www.etsi.org/deliver/etsi_ts/103200_103299/103285/01.01.01_60/ts_103285v010101p.pdf).  |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.  |
| segmentTemplateFormat | string<br />Values: `NUMBER_WITH_TIMELINE \| TIME_WITH_TIMELINE \| NUMBER_WITH_DURATION` | False | Determines the type of variable used in the `media` URL of the `SegmentTemplate` tag in the manifest. Also specifies if segment timeline information is included in `SegmentTimeline` or `SegmentTemplate`.<br />Value description: +   `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate`. <br />+   `NUMBER_WITH_DURATION` - The `$Number$` variable is used in the `media ` URL and a `duration` attribute is added to the segment template. The `SegmentTimeline` object is removed from the representation. <br />+   `TIME_WITH_TIMELINE` - The `$Time$` variable is used in the `media` URL. The value of this variable is the timestamp of when the segment starts. A full `SegmentTimeline` object is presented in each `SegmentTemplate`.  |
| streamSelection | [StreamSelection](#origin_endpoints-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate. |
| suggestedPresentationDelaySeconds | integer | False | Amount of time (in seconds) that the player should be from the live point at the end of the manifest. |
| utcTiming | string<br />Values: `NONE \| HTTP-HEAD \| HTTP-ISO \| HTTP-XSDATE` | False | Determines the type of UTC timing included in the DASH Media Presentation Description (MPD). |
| utcTimingUri | string | False | Specifies the value attribute of the UTC timing field when utcTiming is set to `HTTP-ISO` or `HTTP-HEAD`. |

### EncryptionContractConfiguration
<a name="origin_endpoints-model-encryptioncontractconfiguration"></a>

Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines the content keys used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. For more information about these presets, see [SPEKE Version 2.0 Presets](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html)

Note the following considerations when using `encryptionContractConfiguration`:
+ You can use `encryptionContractConfiguration` for DASH endpoints that use SPEKE Version 2.0. SPEKE Version 2.0 relies on the CPIX Version 2.3 specification.
+ You must disable key rotation for this endpoint by setting `keyRotationIntervalSeconds` to `0`.
+ You cannot combine an `UNENCRYPTED` preset with `UNENCRYPTED` or `SHARED` presets across `presetSpeke20Audio` and `presetSpeke20Video`.
+ When you use a `SHARED` preset, you must use it for both `presetSpeke20Audio` and `presetSpeke20Video`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| presetSpeke20Audio | string<br />Values: `PRESET-AUDIO-1 \| PRESET-AUDIO-2 \| PRESET-AUDIO-3 \| SHARED \| UNENCRYPTED` | True | A collection of audio encryption presets.<br />Value description: +  `PRESET-AUDIO-1` - Use one content key to encrypt all of the audio tracks in your stream. <br />+  `PRESET-AUDIO-2` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks. <br />+  `PRESET-AUDIO-3` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels. <br />+  `SHARED` - Use the same content key for all of the audio and video tracks in your stream. <br />+  `UNENCRYPTED` - Don't encrypt any of the audio tracks in your stream.  |
| presetSpeke20Video | string<br />Values: `PRESET-VIDEO-1 \| PRESET-VIDEO-2 \| PRESET-VIDEO-3 \| PRESET-VIDEO-4 \| PRESET-VIDEO-5 \| PRESET-VIDEO-6 \| PRESET-VIDEO-7 \| PRESET-VIDEO-8 \| SHARED \| UNENCRYPTED` | True | A collection of video encryption presets.<br />Value description: +   `PRESET-VIDEO-1` - Use one content key to encrypt all of the video tracks in your stream. <br />+   `PRESET-VIDEO-2` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks. <br />+   `PRESET-VIDEO-3` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-4` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `PRESET-VIDEO-5` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `PRESET-VIDEO-6` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-7` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. <br />+   `PRESET-VIDEO-8` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. <br />+   `SHARED` - Use the same content key for all of the video and audio tracks in your stream. <br />+   `UNENCRYPTED` - Don't encrypt any of the video tracks in your stream.  |

### HlsEncryption
<a name="origin_endpoints-model-hlsencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantInitializationVector | string | False | A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. |
| encryptionMethod | string<br />Values: `AES_128 \| SAMPLE_AES` | False | HLS encryption type.  |
| keyRotationIntervalSeconds | integer | False | Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to `0` to disable key rotation.  |
| repeatExtXKey | boolean | False | Repeat the EXT-X-KEY directive for every media segment. This might result in an increase in client requests to the DRM server.  |
| spekeKeyProvider | [SpekeKeyProvider](#origin_endpoints-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### HlsManifest
<a name="origin_endpoints-model-hlsmanifest"></a>

A HTTP Live Streaming (HLS) manifest configuration on a CMAF endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | string<br />Values: `NONE \| SCTE35_ENHANCED \| PASSTHROUGH \| DATERANGE` | False | Controls how ad markers are included in the packaged endpoint.<br />Value description: +   `NONE` - Omits all SCTE-35 ad markers from the output. <br />+   `PASSTHROUGH` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. <br />+   `SCTE35_ENHANCED` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest. <br />+   `DATERANGE` - Inserts SCTE-35 `EXT-X-DATERANGE` tags to signal ad and program transition events in HLS and CMAF manifests. If you use `DATERANGE`, you must set a `programDateTimeIntervalSeconds` value greater than `0`. To learn more about `DATERANGE`, see [SCTE-35 Ad Marker EXT-X-DATERANGE](https://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html).  |
| id | string | True | The manifest ID is required and must be unique within the OriginEndpoint. The ID can't be changed after the endpoint is created. |
| includeIframeOnlyStream | boolean | False | Applies to stream sets with a single video track only. When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object. |
| playlistType | string<br />Values: `NONE \| EVENT \| VOD` | False | When specified as either `event` or `vod`, a corresponding EXT-X-PLAYLIST-TYPE entry is included in the media playlist. Indicates if the playlist is live to VOD content.  |
| playlistWindowSeconds | integer | False | Time window (in seconds) contained in each parent manifest. |
| programDateTimeIntervalSeconds | integer | False | Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify in seconds between each EXT-XPROGRAM-DATE-TIME tag. If the interval is not specified, or is set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted in the manifest.<br />Omit this attribute or enter `0` to indicate that the EXT-X-PROGRAM-DATE-TIME tags are not included in the manifest.<br />Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. |
| url | string | False | The URL that's used to request this manifest from this endpoint. |

### HlsManifestCreateOrUpdateParameters
<a name="origin_endpoints-model-hlsmanifestcreateorupdateparameters"></a>

Parameters for creating an HTTP Live Streaming (HLS) manifest configuration on a CMAF endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | string<br />Values: `NONE \| SCTE35_ENHANCED \| PASSTHROUGH \| DATERANGE` | False | Controls how ad markers are included in the packaged endpoint. <br />Value description: +   `NONE` - Omits all SCTE-35 ad markers from the output. <br />+   `PASSTHROUGH` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. <br />+   `SCTE35_ENHANCED` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest. <br />+   `DATERANGE` - Inserts SCTE-35 `EXT-X-DATERANGE` tags to signal ad and program transition events in HLS and CMAF manifests. If you use `DATERANGE`, you must set a `programDateTimeIntervalSeconds` value greater than `0`. To learn more about `DATERANGE`, see [SCTE-35 Ad Marker EXT-X-DATERANGE](https://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html).  |
| adsOnDeliveryRestrictions | [AdsOnDeliveryRestrictions](#origin_endpoints-model-adsondeliveryrestrictions) | False | The flags on SCTE-35 segmentation descriptors that have to be present for MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| adTriggers | Array of type string | False | The SCTE-35 message types that MediaPackage treats as ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| id | string | True | The manifest ID is required and must be unique within the OriginEndpoint. The ID can't be changed after the endpoint is created. |
| includeIframeOnlyStream | boolean | False | Applies to stream sets with a single video track only. When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object. |
| playlistType | string<br />Values: `NONE \| EVENT \| VOD` | False | When specified as either `event` or `vod`, a corresponding EXT-X-PLAYLIST-TYPE entry is included in the media playlist. Indicates if the playlist is live to VOD content.  |
| playlistWindowSeconds | integer | False | Time window (in seconds) contained in each parent manifest. |
| programDateTimeIntervalSeconds | integer | False | Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify in seconds between each EXT-XPROGRAM-DATE-TIME tag. If the interval is not specified, or is set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted in the manifest.<br />Omit this attribute or enter `0` to indicate that the EXT-X-PROGRAM-DATE-TIME tags are not included in the manifest.<br />Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. |

### HlsPackage
<a name="origin_endpoints-model-hlspackage"></a>

Parameters for Apple HLS packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | string<br />Values: `NONE \| SCTE35_ENHANCED \| PASSTHROUGH \| DATERANGE` | False | Controls how ad markers are included in the packaged endpoint.<br />Value description: +   `NONE` - Omits all SCTE-35 ad markers from the output. <br />+   `PASSTHROUGH` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. <br />+   `SCTE35_ENHANCED` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest. <br />+   `DATERANGE` - Inserts SCTE-35 `EXT-X-DATERANGE` tags to signal ad and program transition events in HLS and CMAF manifests. If you use `DATERANGE`, you must set a `programDateTimeIntervalSeconds` value greater than `0`. To learn more about `DATERANGE`, see [SCTE-35 Ad Marker EXT-X-DATERANGE](https://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html).  |
| adsOnDeliveryRestrictions | [AdsOnDeliveryRestrictions](#origin_endpoints-model-adsondeliveryrestrictions) | False | The flags on SCTE-35 segmentation descriptors that have to be present for MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| adTriggers | Array of type string | False | The SCTE-35 message types that MediaPackage treats as ad markers in the output manifest. For information about SCTE-35 in MediaPackage, see [SCTE-35 Message Options in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html).  |
| encryption | [HlsEncryption](#origin_endpoints-model-hlsencryption) | False | Parameters for encrypting content. |
| includeDvbSubtitles | boolean | False | When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output. |
| includeIframeOnlyStream | boolean | False | Only applies to stream sets with a single video track. When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included.  |
| playlistType | string<br />Values: `NONE \| EVENT \| VOD` | False | When specified as either `event` or `vod`, a corresponding EXT-X-PLAYLIST-TYPE entry is included in the media playlist. Indicates if the playlist is live to VOD content.  |
| playlistWindowSeconds | integer | False | Time window (in seconds) contained in each parent manifest. |
| programDateTimeIntervalSeconds | integer | False | Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify in seconds between each EXT-XPROGRAM-DATE-TIME tag. If the interval is not specified, or is set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted in the manifest.<br />Omit this attribute or enter `0` to indicate that the EXT-X-PROGRAM-DATE-TIME tags are not included in the manifest.<br />Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.  |
| streamSelection | [StreamSelection](#origin_endpoints-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate. |
| useAudioRenditionGroup | boolean | False | When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group. |

### MssEncryption
<a name="origin_endpoints-model-mssencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spekeKeyProvider | [SpekeKeyProvider](#origin_endpoints-model-spekekeyprovider) | True | Parameters for the SPEKE key provider. |

### MssPackage
<a name="origin_endpoints-model-msspackage"></a>

Parameters for Microsoft Smooth Streaming packaging.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryption | [MssEncryption](#origin_endpoints-model-mssencryption) | False | Parameters for encrypting content. |
| manifestWindowSeconds | integer | False | Time window (in seconds) contained in each manifest. |
| segmentDurationSeconds | integer | False | Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration. |
| streamSelection | [StreamSelection](#origin_endpoints-model-streamselection) | False | Limitations for outputs from the endpoint, based on the video bitrate.  |

### OriginEndpoint
<a name="origin_endpoints-model-originendpoint"></a>

OriginEndpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The endpoint's unique system-generated resource name, based on the AWS record. |
| authorization | [Authorization](#origin_endpoints-model-authorization) | False | Parameters for CDN authorization. |
| channelId | string | False | The ID of the channel associated with this endpoint. |
| cmafPackage | [CmafPackage](#origin_endpoints-model-cmafpackage) | False | Parameters for CMAF packaging. |
| createdAt | string | False | The date and time the OriginEndpoint was created. |
| dashPackage | [DashPackage](#origin_endpoints-model-dashpackage) | False | Parameters for DASH packaging. |
| description | string | False | Any descriptive information that you want to add to the endpoint for future identification purposes. |
| hlsPackage | [HlsPackage](#origin_endpoints-model-hlspackage) | False | Parameters for Apple HLS packaging. |
| id | string | False | The endpoint identifier. |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint. |
| mssPackage | [MssPackage](#origin_endpoints-model-msspackage) | False | Parameters for Microsoft Smooth Streaming packaging. |
| origination | string<br />Values: `ALLOW \| DENY` | False | Controls video origination from this endpoint. <br />Value description: +   `ALLOW` - Enables this endpoint to serve content to requesting devices. <br />+   `DENY` - Prevents this endpoint from serving content. Denying origination is helpful for harvesting live-to-VOD assets. For more information about harvesting and origination, see [Live-to-VOD Requirements](https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html).  |
| startoverWindowSeconds | integer | False | Maximum duration (seconds) of content to retain for startover playback. A `0` indicates that startover playback is disabled for this endpoint.  |
| tags | [Tags](#origin_endpoints-model-tags) | False | The tags assigned to the endpoint. |
| timeDelaySeconds | integer | False | Minimum duration (seconds) of delay to enforce on the playback of live content. A `0` indicates that there is no time delay in effect for this endpoint  |
| url | string | False | The URL that's used to request content from this endpoint. |
| whitelist | Array of type string | False | The IP addresses that can access this endpoint. |

### OriginEndpointCreateParameters
<a name="origin_endpoints-model-originendpointcreateparameters"></a>

OriginEndpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#origin_endpoints-model-authorization) | False | Parameters for CDN authorization. |
| channelId | string | True | The ID of the channel associated with this endpoint.  |
| cmafPackage | [CmafPackageCreateOrUpdateParameters](#origin_endpoints-model-cmafpackagecreateorupdateparameters) | False | Parameters for Common Media Application Format (CMAF) packaging. |
| dashPackage | [DashPackage](#origin_endpoints-model-dashpackage) | False | Parameters for DASH packaging. |
| description | string | False | Any descriptive information that you want to add to the endpoint for future identification purposes. |
| hlsPackage | [HlsPackage](#origin_endpoints-model-hlspackage) | False | Parameters for Apple HLS packaging. |
| id | string | True | The endpoint ID is required and must be unique for your account in this region. The ID can't be changed after the endpoint is created.  |
| manifestName | string | False | A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint. |
| mssPackage | [MssPackage](#origin_endpoints-model-msspackage) | False | Parameters for Microsoft Smooth Streaming packaging. |
| origination | string<br />Values: `ALLOW \| DENY` | False | Controls video origination from this endpoint. <br />Value description: +   `ALLOW` - Enables this endpoint to serve content to requesting devices. <br />+   `DENY` - Prevents this endpoint from serving content. Denying origination is helpful for harvesting live-to-VOD assets. For more information about harvesting and origination, see [Live-to-VOD Requirements](https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html).  |
| startoverWindowSeconds | integer | False | Maximum duration (seconds) of content to retain for startover playback. Omit this attribute or enter `0` to indicate that startover playback is disabled for this endpoint.  |
| tags | [Tags](#origin_endpoints-model-tags) | False | The tags to assign to the endpoint. |
| timeDelaySeconds | integer | False | Minimum duration (seconds) of delay to enforce on the playback of live content. Omit this attribute or enter `0` to indicate that there is no time delay in effect for this endpoint  |
| whitelist | Array of type string | False | The IP addresses that can access this endpoint. |

### OriginEndpointList
<a name="origin_endpoints-model-originendpointlist"></a>

A collection of OriginEndpoint records.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Pagination token. Use this token to request the next page of channel results. |
| originEndpoints | Array of type [OriginEndpoint](#origin_endpoints-model-originendpoint) | False | List of endpoints that are configured on this account and the channel that you specified in the request parameters. |

### SpekeKeyProvider
<a name="origin_endpoints-model-spekekeyprovider"></a>

Keyprovider settings for DRM.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string | False | The Amazon Resource Name (ARN) for the certificate that you imported to AWS Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.  |
| encryptionContractConfiguration | [EncryptionContractConfiguration](#origin_endpoints-model-encryptioncontractconfiguration) | False | Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. |
| resourceId | string | True | Unique identifier for this endpoint, as it is configured in the key provider service.  |
| roleArn | string | True | The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows AWS Elemental MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Valid format: `arn:aws:iam::{{accountID}}:role/{{name}}`  |
| systemIds | Array of type string | True | List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.  |
| url | string | True | URL for the key provider’s key retrieval API endpoint. Must start with https://. |

### StreamSelection
<a name="origin_endpoints-model-streamselection"></a>

Limitations for outputs from the endpoint, based on the video bitrate.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxVideoBitsPerSecond | integer | False | The upper limit of the bitrates that this endpoint serves. If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.  |
| minVideoBitsPerSecond | integer | False | The lower limit of the bitrates that this endpoint serves. If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.  |
| streamOrder | string<br />Values: `ORIGINAL \| VIDEO_BITRATE_ASCENDING \| VIDEO_BITRATE_DESCENDING` | False | Order in which the different video bitrates are presented to the player. |

### Tags
<a name="origin_endpoints-model-tags"></a>

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
<a name="origin_endpoints-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListOriginEndpoints
<a name="ListOriginEndpoints-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/ListOriginEndpoints)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/ListOriginEndpoints)

### CreateOriginEndpoint
<a name="CreateOriginEndpoint-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for Python](/goto/boto3/mediapackage-2017-10-12/CreateOriginEndpoint)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediapackage-2017-10-12/CreateOriginEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
