---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/channels.html
---

# Channels
<a name="channels"></a>

## URI
<a name="channels-url"></a>

`/prod/channels`

## HTTP methods
<a name="channels-http-methods"></a>

### GET
<a name="channelsget"></a>

**Operation ID:** `ListChannels`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| sortOrder | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |
| sortBy | String | False |  |
| filterQuery | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListChannelsResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### POST
<a name="channelspost"></a>

**Operation ID:** `CreateChannel`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateChannelResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 409 | ResourceConflict | 409 response |
| 422 | ChannelConfigurationValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="channels-schemas"></a>

### Request bodies
<a name="channels-request-examples"></a>

#### POST schema
<a name="channels-request-body-post-example"></a>

```
{
  "anywhereSettings": {
    "channelPlacementGroupId": "string",
    "clusterId": "string"
  },
  "cdiInputSpecification": {
    "resolution": enum
  },
  "channelClass": enum,
  "channelEngineVersion": {
    "version": "string"
  },
  "channelSecurityGroups": [
    "string"
  ],
  "destinations": [
    {
      "id": "string",
      "logicalInterfaceNames": [
        "string"
      ],
      "mediaConnectRouterSettings": [
        {
          "encryptionType": enum,
          "secretArn": "string"
        }
      ],
      "mediaPackageSettings": [
        {
          "channelEndpointId": "string",
          "channelGroup": "string",
          "channelId": "string",
          "channelName": "string",
          "mediaPackageRegionName": "string"
        }
      ],
      "multiplexSettings": {
        "multiplexId": "string",
        "programName": "string"
      },
      "settings": [
        {
          "passwordParam": "string",
          "streamName": "string",
          "url": "string",
          "username": "string",
          "virtualSourceAddress": "string"
        }
      ],
      "srtSettings": [
        {
          "connectionMode": enum,
          "encryptionPassphraseSecretArn": "string",
          "listenerPort": integer,
          "streamId": "string",
          "url": "string"
        }
      ]
    }
  ],
  "dryRun": boolean,
  "encoderSettings": {
    "audioDescriptions": [
      {
        "audioDashRoles": [
          enum
        ],
        "audioNormalizationSettings": {
          "algorithm": enum,
          "algorithmControl": enum,
          "targetLkfs": number,
          "peakCalculation": enum,
          "peakLimiterThreshold": number
        },
        "audioSelectorName": "string",
        "audioType": enum,
        "audioTypeControl": enum,
        "audioWatermarkingSettings": {
          "nielsenWatermarksSettings": {
            "nielsenCbetSettings": {
              "cbetCheckDigitString": "string",
              "cbetStepaside": enum,
              "csid": "string"
            },
            "nielsenDistributionType": enum,
            "nielsenNaesIiNwSettings": {
              "checkDigitString": "string",
              "sid": number,
              "timezone": enum
            },
            "nielsenNwOnlySettings": {
              "checkDigitString": "string",
              "sid": number,
              "timezone": enum
            }
          }
        },
        "codecSettings": {
          "aacSettings": {
            "bitrate": number,
            "codingMode": enum,
            "inputType": enum,
            "profile": enum,
            "rateControlMode": enum,
            "rawFormat": enum,
            "sampleRate": number,
            "spec": enum,
            "vbrQuality": enum
          },
          "ac3Settings": {
            "attenuationControl": enum,
            "bitrate": number,
            "bitstreamMode": enum,
            "codingMode": enum,
            "dialnorm": integer,
            "drcProfile": enum,
            "lfeFilter": enum,
            "metadataControl": enum
          },
          "eac3AtmosSettings": {
            "bitrate": number,
            "codingMode": enum,
            "dialnorm": integer,
            "drcLine": enum,
            "drcRf": enum,
            "heightTrim": number,
            "surroundTrim": number
          },
          "eac3Settings": {
            "attenuationControl": enum,
            "bitrate": number,
            "bitstreamMode": enum,
            "codingMode": enum,
            "dcFilter": enum,
            "dialnorm": integer,
            "drcLine": enum,
            "drcRf": enum,
            "lfeControl": enum,
            "lfeFilter": enum,
            "loRoCenterMixLevel": number,
            "loRoSurroundMixLevel": number,
            "ltRtCenterMixLevel": number,
            "ltRtSurroundMixLevel": number,
            "metadataControl": enum,
            "passthroughControl": enum,
            "phaseControl": enum,
            "stereoDownmix": enum,
            "surroundExMode": enum,
            "surroundMode": enum
          },
          "mp2Settings": {
            "bitrate": number,
            "codingMode": enum,
            "sampleRate": number
          },
          "passThroughSettings": {
          },
          "wavSettings": {
            "bitDepth": number,
            "codingMode": enum,
            "sampleRate": number
          }
        },
        "dvbDashAccessibility": enum,
        "languageCode": "string",
        "languageCodeControl": enum,
        "name": "string",
        "remixSettings": {
          "channelMappings": [
            {
              "inputChannelLevels": [
                {
                  "gain": integer,
                  "inputChannel": integer
                }
              ],
              "outputChannel": integer
            }
          ],
          "channelsIn": integer,
          "channelsOut": integer
        },
        "streamName": "string"
      }
    ],
    "availBlanking": {
      "availBlankingImage": {
        "passwordParam": "string",
        "uri": "string",
        "username": "string"
      },
      "state": enum
    },
    "availConfiguration": {
      "availSettings": {
        "esam": {
          "acquisitionPointId": "string",
          "adAvailOffset": integer,
          "passwordParam": "string",
          "poisEndpoint": "string",
          "username": "string",
          "zoneIdentity": "string"
        },
        "scte35SpliceInsert": {
          "adAvailOffset": integer,
          "noRegionalBlackoutFlag": enum,
          "webDeliveryAllowedFlag": enum
        },
        "scte35TimeSignalApos": {
          "adAvailOffset": integer,
          "noRegionalBlackoutFlag": enum,
          "webDeliveryAllowedFlag": enum
        }
      },
      "scte35SegmentationScope": enum
    },
    "blackoutSlate": {
      "blackoutSlateImage": {
        "passwordParam": "string",
        "uri": "string",
        "username": "string"
      },
      "networkEndBlackout": enum,
      "networkEndBlackoutImage": {
        "passwordParam": "string",
        "uri": "string",
        "username": "string"
      },
      "networkId": "string",
      "state": enum
    },
    "captionDescriptions": [
      {
        "accessibility": enum,
        "captionDashRoles": [
          enum
        ],
        "captionSelectorName": "string",
        "destinationSettings": {
          "aribDestinationSettings": {
          },
          "burnInDestinationSettings": {
            "alignment": enum,
            "backgroundColor": enum,
            "backgroundOpacity": integer,
            "font": {
              "passwordParam": "string",
              "uri": "string",
              "username": "string"
            },
            "fontColor": enum,
            "fontOpacity": integer,
            "fontResolution": integer,
            "fontSize": "string",
            "outlineColor": enum,
            "outlineSize": integer,
            "shadowColor": enum,
            "shadowOpacity": integer,
            "shadowXOffset": integer,
            "shadowYOffset": integer,
            "subtitleRows": enum,
            "teletextGridControl": enum,
            "xPosition": integer,
            "yPosition": integer
          },
          "dvbSubDestinationSettings": {
            "alignment": enum,
            "backgroundColor": enum,
            "backgroundOpacity": integer,
            "font": {
              "passwordParam": "string",
              "uri": "string",
              "username": "string"
            },
            "fontColor": enum,
            "fontOpacity": integer,
            "fontResolution": integer,
            "fontSize": "string",
            "outlineColor": enum,
            "outlineSize": integer,
            "shadowColor": enum,
            "shadowOpacity": integer,
            "shadowXOffset": integer,
            "shadowYOffset": integer,
            "subtitleRows": enum,
            "teletextGridControl": enum,
            "xPosition": integer,
            "yPosition": integer
          },
          "ebuTtDDestinationSettings": {
            "copyrightHolder": "string",
            "defaultFontSize": integer,
            "defaultLineHeight": integer,
            "fillLineGap": enum,
            "fontFamily": "string",
            "styleControl": enum
          },
          "embeddedDestinationSettings": {
            "position": {
              "yPositionLine": integer
            },
            "styleControl": enum
          },
          "embeddedPlusScte20DestinationSettings": {
          },
          "rtmpCaptionInfoDestinationSettings": {
          },
          "scte20PlusEmbeddedDestinationSettings": {
          },
          "scte27DestinationSettings": {
          },
          "smpteTtDestinationSettings": {
          },
          "teletextDestinationSettings": {
          },
          "ttmlDestinationSettings": {
            "position": {
              "yPositionPercentage": integer
            },
            "styleControl": enum
          },
          "webvttDestinationSettings": {
            "position": {
              "yPositionPercentage": integer
            },
            "styleControl": enum
          }
        },
        "dvbDashAccessibility": enum,
        "languageCode": "string",
        "languageDescription": "string",
        "name": "string"
      }
    ],
    "colorCorrectionSettings": {
      "globalColorCorrections": [
        {
          "inputColorSpace": enum,
          "outputColorSpace": enum,
          "uri": "string"
        }
      ]
    },
    "featureActivations": {
      "inputPrepareScheduleActions": enum,
      "outputStaticImageOverlayScheduleActions": enum
    },
    "globalConfiguration": {
      "initialAudioGain": integer,
      "inputEndAction": enum,
      "inputLossBehavior": {
        "blackFrameMsec": integer,
        "inputLossImageColor": "string",
        "inputLossImageSlate": {
          "passwordParam": "string",
          "uri": "string",
          "username": "string"
        },
        "inputLossImageType": enum,
        "repeatFrameMsec": integer
      },
      "outputLockingMode": enum,
      "outputLockingSettings": {
        "disabledLockingSettings": {
          "customEpoch": "string"
        },
        "epochLockingSettings": {
          "customEpoch": "string",
          "jamSyncTime": "string"
        },
        "pipelineLockingSettings": {
          "customEpoch": "string",
          "pipelineLockingMethod": enum
        }
      },
      "outputTimingSource": enum,
      "supportLowFramerateInputs": enum
    },
    "motionGraphicsConfiguration": {
      "motionGraphicsInsertion": enum,
      "motionGraphicsSettings": {
        "htmlMotionGraphicsSettings": {
        }
      }
    },
    "nielsenConfiguration": {
      "distributorId": "string",
      "nielsenPcmToId3Tagging": enum
    },
    "outputGroups": [
      {
        "name": "string",
        "outputGroupSettings": {
          "archiveGroupSettings": {
            "archiveCdnSettings": {
              "archiveS3Settings": {
                "cannedAcl": enum,
                "logUploads": enum
              }
            },
            "destination": {
              "destinationRefId": "string"
            },
            "rolloverInterval": integer
          },
          "cmafIngestGroupSettings": {
            "additionalDestinations": [
              {
                "destination": {
                  "destinationRefId": "string"
                }
              }
            ],
            "captionLanguageMappings": [
              {
                "captionChannel": integer,
                "languageCode": "string"
              }
            ],
            "destination": {
              "destinationRefId": "string"
            },
            "id3Behavior": enum,
            "id3NameModifier": "string",
            "klvBehavior": enum,
            "klvNameModifier": "string",
            "nielsenId3Behavior": enum,
            "nielsenId3NameModifier": "string",
            "scte35NameModifier": "string",
            "scte35Type": enum,
            "segmentLength": integer,
            "segmentLengthUnits": enum,
            "sendDelayMs": integer,
            "timedMetadataId3Frame": enum,
            "timedMetadataId3Period": integer,
            "timedMetadataPassthrough": enum,
            "watermarkingSettings": {
              "cmafIngestAbWatermarkerIrdetoSettings": {
                "additionalDestinationsAlternateDestinations": [
                  {
                    "destinationRefId": "string"
                  }
                ],
                "alternateDestination": {
                  "destinationRefId": "string"
                },
                "customProfile": {
                  "embeddingFrequency": number,
                  "sceneCut": number,
                  "targetPsnr": number
                },
                "license": "string",
                "operatorId": integer,
                "polyPeriod": integer,
                "profile": enum,
                "watermarkIdLength": enum
              }
            }
          },
          "frameCaptureGroupSettings": {
            "destination": {
              "destinationRefId": "string"
            },
            "frameCaptureCdnSettings": {
              "frameCaptureS3Settings": {
                "cannedAcl": enum,
                "logUploads": enum
              }
            }
          },
          "hlsGroupSettings": {
            "adMarkers": [
              enum
            ],
            "baseUrlContent": "string",
            "baseUrlContent1": "string",
            "baseUrlManifest": "string",
            "baseUrlManifest1": "string",
            "captionLanguageMappings": [
              {
                "captionChannel": integer,
                "languageCode": "string",
                "languageDescription": "string"
              }
            ],
            "captionLanguageSetting": enum,
            "clientCache": enum,
            "codecSpecification": enum,
            "constantIv": "string",
            "destination": {
              "destinationRefId": "string"
            },
            "directoryStructure": enum,
            "discontinuityTags": enum,
            "encryptionType": enum,
            "hlsCdnSettings": {
              "hlsAkamaiSettings": {
                "connectionRetryInterval": integer,
                "filecacheDuration": integer,
                "httpTransferMode": enum,
                "numRetries": integer,
                "restartDelay": integer,
                "salt": "string",
                "token": "string"
              },
              "hlsBasicPutSettings": {
                "connectionRetryInterval": integer,
                "filecacheDuration": integer,
                "numRetries": integer,
                "restartDelay": integer
              },
              "hlsMediaStoreSettings": {
                "connectionRetryInterval": integer,
                "filecacheDuration": integer,
                "mediaStoreStorageClass": enum,
                "numRetries": integer,
                "restartDelay": integer
              },
              "hlsS3Settings": {
                "cannedAcl": enum,
                "logUploads": enum
              },
              "hlsWebdavSettings": {
                "connectionRetryInterval": integer,
                "filecacheDuration": integer,
                "httpTransferMode": enum,
                "numRetries": integer,
                "restartDelay": integer
              }
            },
            "hlsId3SegmentTagging": enum,
            "iFrameOnlyPlaylists": enum,
            "incompleteSegmentBehavior": enum,
            "indexNSegments": integer,
            "inputLossAction": enum,
            "ivInManifest": enum,
            "ivSource": enum,
            "keepSegments": integer,
            "keyFormat": "string",
            "keyFormatVersions": "string",
            "keyProviderSettings": {
              "staticKeySettings": {
                "keyProviderServer": {
                  "passwordParam": "string",
                  "uri": "string",
                  "username": "string"
                },
                "staticKeyValue": "string"
              }
            },
            "manifestCompression": enum,
            "manifestDurationFormat": enum,
            "minSegmentLength": integer,
            "mode": enum,
            "outputSelection": enum,
            "programDateTime": enum,
            "programDateTimeClock": enum,
            "programDateTimePeriod": integer,
            "redundantManifest": enum,
            "segmentLength": integer,
            "segmentationMode": enum,
            "segmentsPerSubdirectory": integer,
            "streamInfResolution": enum,
            "timedMetadataId3Frame": enum,
            "timedMetadataId3Period": integer,
            "timestampDeltaMilliseconds": integer,
            "tsFileMode": enum
          },
          "mediaConnectRouterGroupSettings": {
            "availabilityZones": [
              "string"
            ]
          },
          "mediaPackageGroupSettings": {
            "destination": {
              "destinationRefId": "string"
            },
            "mediapackageV2GroupSettings": {
              "additionalDestinations": [
                {
                  "destination": {
                    "destinationRefId": "string"
                  }
                }
              ],
              "captionLanguageMappings": [
                {
                  "captionChannel": integer,
                  "languageCode": "string",
                  "languageDescription": "string"
                }
              ],
              "captionLanguageSetting": enum,
              "id3Behavior": enum,
              "klvBehavior": enum,
              "nielsenId3Behavior": enum,
              "scte35Type": enum,
              "segmentLength": integer,
              "segmentLengthUnits": enum,
              "timedMetadataId3Frame": enum,
              "timedMetadataId3Period": integer,
              "timedMetadataPassthrough": enum,
              "watermarkingSettings": {
                "mediaPackageV2AbWatermarkerIrdetoSettings": {
                  "additionalDestinationsAlternateDestinations": [
                    {
                      "destinationRefId": "string"
                    }
                  ],
                  "alternateDestination": {
                    "destinationRefId": "string"
                  },
                  "customProfile": {
                    "embeddingFrequency": number,
                    "sceneCut": number,
                    "targetPsnr": number
                  },
                  "license": "string",
                  "operatorId": integer,
                  "polyPeriod": integer,
                  "profile": enum,
                  "watermarkIdLength": enum
                }
              }
            }
          },
          "msSmoothGroupSettings": {
            "acquisitionPointId": "string",
            "audioOnlyTimecodeControl": enum,
            "certificateMode": enum,
            "connectionRetryInterval": integer,
            "destination": {
              "destinationRefId": "string"
            },
            "eventId": "string",
            "eventIdMode": enum,
            "eventStopBehavior": enum,
            "filecacheDuration": integer,
            "fragmentLength": integer,
            "inputLossAction": enum,
            "numRetries": integer,
            "restartDelay": integer,
            "segmentationMode": enum,
            "sendDelayMs": integer,
            "sparseTrackType": enum,
            "streamManifestBehavior": enum,
            "timestampOffset": "string",
            "timestampOffsetMode": enum
          },
          "multiplexGroupSettings": {
          },
          "rtmpGroupSettings": {
            "adMarkers": [
              enum
            ],
            "authenticationScheme": enum,
            "cacheFullBehavior": enum,
            "cacheLength": integer,
            "captionData": enum,
            "includeFillerNalUnits": enum,
            "inputLossAction": enum,
            "restartDelay": integer
          },
          "srtGroupSettings": {
            "inputLossAction": enum
          },
          "udpGroupSettings": {
            "inputLossAction": enum,
            "timedMetadataId3Frame": enum,
            "timedMetadataId3Period": integer
          }
        },
        "outputs": [
          {
            "audioDescriptionNames": [
              "string"
            ],
            "captionDescriptionNames": [
              "string"
            ],
            "outputName": "string",
            "outputSettings": {
              "archiveOutputSettings": {
                "containerSettings": {
                  "m2tsSettings": {
                    "absentInputAudioBehavior": enum,
                    "arib": enum,
                    "aribCaptionsPid": "string",
                    "aribCaptionsPidControl": enum,
                    "audioBufferModel": enum,
                    "audioFramesPerPes": integer,
                    "audioPids": "string",
                    "audioStreamType": enum,
                    "bitrate": integer,
                    "bufferModel": enum,
                    "ccDescriptor": enum,
                    "dvbNitSettings": {
                      "networkId": integer,
                      "networkName": "string",
                      "repInterval": integer
                    },
                    "dvbSdtSettings": {
                      "outputSdt": enum,
                      "repInterval": integer,
                      "serviceName": "string",
                      "serviceProviderName": "string"
                    },
                    "dvbSubPids": "string",
                    "dvbTdtSettings": {
                      "repInterval": integer
                    },
                    "dvbTeletextPid": "string",
                    "ebif": enum,
                    "ebpAudioInterval": enum,
                    "ebpLookaheadMs": integer,
                    "ebpPlacement": enum,
                    "ecmPid": "string",
                    "esRateInPes": enum,
                    "etvPlatformPid": "string",
                    "etvSignalPid": "string",
                    "fragmentTime": number,
                    "klv": enum,
                    "klvDataPids": "string",
                    "nielsenId3Behavior": enum,
                    "nullPacketBitrate": number,
                    "patInterval": integer,
                    "pcrControl": enum,
                    "pcrPeriod": integer,
                    "pcrPid": "string",
                    "pmtInterval": integer,
                    "pmtPid": "string",
                    "programNum": integer,
                    "rateMode": enum,
                    "scte27Pids": "string",
                    "scte35Control": enum,
                    "scte35Pid": "string",
                    "scte35PrerollPullupMilliseconds": number,
                    "segmentationMarkers": enum,
                    "segmentationStyle": enum,
                    "segmentationTime": number,
                    "timedMetadataBehavior": enum,
                    "timedMetadataPid": "string",
                    "transportStreamId": integer,
                    "videoPid": "string"
                  },
                  "rawSettings": {
                  }
                },
                "extension": "string",
                "nameModifier": "string"
              },
              "cmafIngestOutputSettings": {
                "nameModifier": "string"
              },
              "frameCaptureOutputSettings": {
                "nameModifier": "string"
              },
              "hlsOutputSettings": {
                "h265PackagingType": enum,
                "hlsSettings": {
                  "audioOnlyHlsSettings": {
                    "audioGroupId": "string",
                    "audioOnlyImage": {
                      "passwordParam": "string",
                      "uri": "string",
                      "username": "string"
                    },
                    "audioTrackType": enum,
                    "segmentType": enum
                  },
                  "fmp4HlsSettings": {
                    "audioRenditionSets": "string",
                    "nielsenId3Behavior": enum,
                    "timedMetadataBehavior": enum
                  },
                  "frameCaptureHlsSettings": {
                  },
                  "standardHlsSettings": {
                    "audioRenditionSets": "string",
                    "m3u8Settings": {
                      "audioFramesPerPes": integer,
                      "audioPids": "string",
                      "ecmPid": "string",
                      "klvBehavior": enum,
                      "klvDataPids": "string",
                      "nielsenId3Behavior": enum,
                      "patInterval": integer,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "pcrPid": "string",
                      "pmtInterval": integer,
                      "pmtPid": "string",
                      "programNum": integer,
                      "scte35Behavior": enum,
                      "scte35Pid": "string",
                      "timedMetadataBehavior": enum,
                      "timedMetadataPid": "string",
                      "transportStreamId": integer,
                      "videoPid": "string"
                    }
                  }
                },
                "nameModifier": "string",
                "segmentModifier": "string"
              },
              "mediaConnectRouterOutputSettings": {
                "connectedRouterInputs": {
                  "pipeline0": "string",
                  "pipeline1": "string"
                },
                "containerSettings": {
                  "m2tsSettings": {
                    "absentInputAudioBehavior": enum,
                    "arib": enum,
                    "aribCaptionsPid": "string",
                    "aribCaptionsPidControl": enum,
                    "audioBufferModel": enum,
                    "audioFramesPerPes": integer,
                    "audioPids": "string",
                    "audioStreamType": enum,
                    "bitrate": integer,
                    "bufferModel": enum,
                    "ccDescriptor": enum,
                    "dvbNitSettings": {
                      "networkId": integer,
                      "networkName": "string",
                      "repInterval": integer
                    },
                    "dvbSdtSettings": {
                      "outputSdt": enum,
                      "repInterval": integer,
                      "serviceName": "string",
                      "serviceProviderName": "string"
                    },
                    "dvbSubPids": "string",
                    "dvbTdtSettings": {
                      "repInterval": integer
                    },
                    "dvbTeletextPid": "string",
                    "ebif": enum,
                    "ebpAudioInterval": enum,
                    "ebpLookaheadMs": integer,
                    "ebpPlacement": enum,
                    "ecmPid": "string",
                    "esRateInPes": enum,
                    "etvPlatformPid": "string",
                    "etvSignalPid": "string",
                    "fragmentTime": number,
                    "klv": enum,
                    "klvDataPids": "string",
                    "nielsenId3Behavior": enum,
                    "nullPacketBitrate": number,
                    "patInterval": integer,
                    "pcrControl": enum,
                    "pcrPeriod": integer,
                    "pcrPid": "string",
                    "pmtInterval": integer,
                    "pmtPid": "string",
                    "programNum": integer,
                    "rateMode": enum,
                    "scte27Pids": "string",
                    "scte35Control": enum,
                    "scte35Pid": "string",
                    "scte35PrerollPullupMilliseconds": number,
                    "segmentationMarkers": enum,
                    "segmentationStyle": enum,
                    "segmentationTime": number,
                    "timedMetadataBehavior": enum,
                    "timedMetadataPid": "string",
                    "transportStreamId": integer,
                    "videoPid": "string"
                  }
                },
                "destination": {
                  "destinationRefId": "string"
                }
              },
              "mediaPackageOutputSettings": {
                "mediaPackageV2DestinationSettings": {
                  "audioGroupId": "string",
                  "audioRenditionSets": "string",
                  "hlsAutoSelect": enum,
                  "hlsDefault": enum,
                  "outputUsage": [
                    enum
                  ]
                }
              },
              "msSmoothOutputSettings": {
                "h265PackagingType": enum,
                "nameModifier": "string"
              },
              "multiplexOutputSettings": {
                "containerSettings": {
                  "multiplexM2tsSettings": {
                    "absentInputAudioBehavior": enum,
                    "arib": enum,
                    "audioBufferModel": enum,
                    "audioFramesPerPes": integer,
                    "audioStreamType": enum,
                    "ccDescriptor": enum,
                    "ebif": enum,
                    "esRateInPes": enum,
                    "klv": enum,
                    "nielsenId3Behavior": enum,
                    "pcrControl": enum,
                    "pcrPeriod": integer,
                    "scte35Control": enum,
                    "scte35PrerollPullupMilliseconds": number
                  }
                },
                "destination": {
                  "destinationRefId": "string"
                }
              },
              "rtmpOutputSettings": {
                "certificateMode": enum,
                "connectionRetryInterval": integer,
                "destination": {
                  "destinationRefId": "string"
                },
                "numRetries": integer
              },
              "srtOutputSettings": {
                "bufferMsec": integer,
                "containerSettings": {
                  "m2tsSettings": {
                    "absentInputAudioBehavior": enum,
                    "arib": enum,
                    "aribCaptionsPid": "string",
                    "aribCaptionsPidControl": enum,
                    "audioBufferModel": enum,
                    "audioFramesPerPes": integer,
                    "audioPids": "string",
                    "audioStreamType": enum,
                    "bitrate": integer,
                    "bufferModel": enum,
                    "ccDescriptor": enum,
                    "dvbNitSettings": {
                      "networkId": integer,
                      "networkName": "string",
                      "repInterval": integer
                    },
                    "dvbSdtSettings": {
                      "outputSdt": enum,
                      "repInterval": integer,
                      "serviceName": "string",
                      "serviceProviderName": "string"
                    },
                    "dvbSubPids": "string",
                    "dvbTdtSettings": {
                      "repInterval": integer
                    },
                    "dvbTeletextPid": "string",
                    "ebif": enum,
                    "ebpAudioInterval": enum,
                    "ebpLookaheadMs": integer,
                    "ebpPlacement": enum,
                    "ecmPid": "string",
                    "esRateInPes": enum,
                    "etvPlatformPid": "string",
                    "etvSignalPid": "string",
                    "fragmentTime": number,
                    "klv": enum,
                    "klvDataPids": "string",
                    "nielsenId3Behavior": enum,
                    "nullPacketBitrate": number,
                    "patInterval": integer,
                    "pcrControl": enum,
                    "pcrPeriod": integer,
                    "pcrPid": "string",
                    "pmtInterval": integer,
                    "pmtPid": "string",
                    "programNum": integer,
                    "rateMode": enum,
                    "scte27Pids": "string",
                    "scte35Control": enum,
                    "scte35Pid": "string",
                    "scte35PrerollPullupMilliseconds": number,
                    "segmentationMarkers": enum,
                    "segmentationStyle": enum,
                    "segmentationTime": number,
                    "timedMetadataBehavior": enum,
                    "timedMetadataPid": "string",
                    "transportStreamId": integer,
                    "videoPid": "string"
                  }
                },
                "destination": {
                  "destinationRefId": "string"
                },
                "encryptionType": enum,
                "latency": integer
              },
              "udpOutputSettings": {
                "bufferMsec": integer,
                "containerSettings": {
                  "m2tsSettings": {
                    "absentInputAudioBehavior": enum,
                    "arib": enum,
                    "aribCaptionsPid": "string",
                    "aribCaptionsPidControl": enum,
                    "audioBufferModel": enum,
                    "audioFramesPerPes": integer,
                    "audioPids": "string",
                    "audioStreamType": enum,
                    "bitrate": integer,
                    "bufferModel": enum,
                    "ccDescriptor": enum,
                    "dvbNitSettings": {
                      "networkId": integer,
                      "networkName": "string",
                      "repInterval": integer
                    },
                    "dvbSdtSettings": {
                      "outputSdt": enum,
                      "repInterval": integer,
                      "serviceName": "string",
                      "serviceProviderName": "string"
                    },
                    "dvbSubPids": "string",
                    "dvbTdtSettings": {
                      "repInterval": integer
                    },
                    "dvbTeletextPid": "string",
                    "ebif": enum,
                    "ebpAudioInterval": enum,
                    "ebpLookaheadMs": integer,
                    "ebpPlacement": enum,
                    "ecmPid": "string",
                    "esRateInPes": enum,
                    "etvPlatformPid": "string",
                    "etvSignalPid": "string",
                    "fragmentTime": number,
                    "klv": enum,
                    "klvDataPids": "string",
                    "nielsenId3Behavior": enum,
                    "nullPacketBitrate": number,
                    "patInterval": integer,
                    "pcrControl": enum,
                    "pcrPeriod": integer,
                    "pcrPid": "string",
                    "pmtInterval": integer,
                    "pmtPid": "string",
                    "programNum": integer,
                    "rateMode": enum,
                    "scte27Pids": "string",
                    "scte35Control": enum,
                    "scte35Pid": "string",
                    "scte35PrerollPullupMilliseconds": number,
                    "segmentationMarkers": enum,
                    "segmentationStyle": enum,
                    "segmentationTime": number,
                    "timedMetadataBehavior": enum,
                    "timedMetadataPid": "string",
                    "transportStreamId": integer,
                    "videoPid": "string"
                  }
                },
                "destination": {
                  "destinationRefId": "string"
                },
                "fecOutputSettings": {
                  "columnDepth": integer,
                  "includeFec": enum,
                  "rowLength": integer
                }
              }
            },
            "videoDescriptionName": "string"
          }
        ]
      }
    ],
    "thumbnailConfiguration": {
      "state": enum
    },
    "timecodeConfig": {
      "source": enum,
      "syncThreshold": integer
    },
    "videoDescriptions": [
      {
        "border": integer,
        "codecSettings": {
          "av1Settings": {
            "afdSignaling": enum,
            "bitDepth": enum,
            "bitrate": integer,
            "bufSize": integer,
            "colorSpaceSettings": {
              "colorSpacePassthroughSettings": {
              },
              "hdr10Settings": {
                "maxCll": integer,
                "maxFall": integer
              },
              "hlg2020Settings": {
              },
              "rec601Settings": {
              },
              "rec709Settings": {
              }
            },
            "fixedAfd": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer,
            "gopSize": number,
            "gopSizeUnits": enum,
            "level": enum,
            "lookAheadRateControl": enum,
            "maxBitrate": integer,
            "minBitrate": integer,
            "minIInterval": integer,
            "parDenominator": integer,
            "parNumerator": integer,
            "qvbrQualityLevel": integer,
            "rateControlMode": enum,
            "sceneChangeDetect": enum,
            "spatialAq": enum,
            "temporalAq": enum,
            "timecodeBurninSettings": {
              "fontSize": enum,
              "position": enum,
              "prefix": "string"
            },
            "timecodeInsertion": enum
          },
          "frameCaptureSettings": {
            "captureInterval": integer,
            "captureIntervalUnits": enum,
            "timecodeBurninSettings": {
              "fontSize": enum,
              "position": enum,
              "prefix": "string"
            }
          },
          "h264Settings": {
            "adaptiveQuantization": enum,
            "allowExplicitWeightedPrediction": enum,
            "afdSignaling": enum,
            "bitrate": integer,
            "bufFillPct": integer,
            "bufSize": integer,
            "colorMetadata": enum,
            "colorSpaceSettings": {
              "colorSpacePassthroughSettings": {
              },
              "rec601Settings": {
              },
              "rec709Settings": {
              }
            },
            "entropyEncoding": enum,
            "filterSettings": {
              "bandwidthReductionFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              },
              "temporalFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              }
            },
            "fixedAfd": enum,
            "flickerAq": enum,
            "forceFieldPictures": enum,
            "framerateControl": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer,
            "gopBReference": enum,
            "gopClosedCadence": integer,
            "gopNumBFrames": integer,
            "gopSize": number,
            "gopSizeUnits": enum,
            "level": enum,
            "lookAheadRateControl": enum,
            "maxBitrate": integer,
            "minBitrate": integer,
            "minIInterval": integer,
            "minQp": integer,
            "numRefFrames": integer,
            "parControl": enum,
            "parDenominator": integer,
            "parNumerator": integer,
            "profile": enum,
            "qualityLevel": enum,
            "qvbrQualityLevel": integer,
            "rateControlMode": enum,
            "scanType": enum,
            "sceneChangeDetect": enum,
            "slices": integer,
            "softness": integer,
            "spatialAq": enum,
            "subgopLength": enum,
            "syntax": enum,
            "temporalAq": enum,
            "timecodeBurninSettings": {
              "fontSize": enum,
              "position": enum,
              "prefix": "string"
            },
            "timecodeInsertion": enum
          },
          "h265Settings": {
            "adaptiveQuantization": enum,
            "afdSignaling": enum,
            "alternativeTransferFunction": enum,
            "bitrate": integer,
            "bufSize": integer,
            "colorMetadata": enum,
            "colorSpaceSettings": {
              "colorSpacePassthroughSettings": {
              },
              "dolbyVision81Settings": {
              },
              "hdr10Settings": {
                "maxCll": integer,
                "maxFall": integer
              },
              "hlg2020Settings": {
              },
              "rec601Settings": {
              },
              "rec709Settings": {
              }
            },
            "deblocking": enum,
            "filterSettings": {
              "bandwidthReductionFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              },
              "temporalFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              }
            },
            "fixedAfd": enum,
            "flickerAq": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer,
            "gopBReference": enum,
            "gopClosedCadence": integer,
            "gopNumBFrames": integer,
            "gopSize": number,
            "gopSizeUnits": enum,
            "level": enum,
            "lookAheadRateControl": enum,
            "maxBitrate": integer,
            "minBitrate": integer,
            "minIInterval": integer,
            "minQp": integer,
            "mvOverPictureBoundaries": enum,
            "mvTemporalPredictor": enum,
            "parDenominator": integer,
            "parNumerator": integer,
            "profile": enum,
            "qvbrQualityLevel": integer,
            "rateControlMode": enum,
            "scanType": enum,
            "sceneChangeDetect": enum,
            "slices": integer,
            "subgopLength": enum,
            "tier": enum,
            "tileHeight": integer,
            "tilePadding": enum,
            "tileWidth": integer,
            "timecodeBurninSettings": {
              "fontSize": enum,
              "position": enum,
              "prefix": "string"
            },
            "timecodeInsertion": enum,
            "treeblockSize": enum
          },
          "mpeg2Settings": {
            "adaptiveQuantization": enum,
            "afdSignaling": enum,
            "colorMetadata": enum,
            "colorSpace": enum,
            "displayAspectRatio": enum,
            "filterSettings": {
              "temporalFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              }
            },
            "fixedAfd": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer,
            "gopClosedCadence": integer,
            "gopNumBFrames": integer,
            "gopSize": number,
            "gopSizeUnits": enum,
            "scanType": enum,
            "subgopLength": enum,
            "timecodeBurninSettings": {
              "fontSize": enum,
              "position": enum,
              "prefix": "string"
            },
            "timecodeInsertion": enum
          }
        },
        "cropRectangle": {
          "height": integer,
          "width": integer,
          "x": integer,
          "y": integer
        },
        "height": integer,
        "name": "string",
        "outputPositionRectangle": {
          "height": integer,
          "width": integer,
          "x": integer,
          "y": integer
        },
        "respondToAfd": enum,
        "scalingBehavior": enum,
        "sharpness": integer,
        "width": integer
      }
    ]
  },
  "inputAttachments": [
    {
      "automaticInputFailoverSettings": {
        "errorClearTimeMsec": integer,
        "failoverConditions": [
          {
            "failoverConditionSettings": {
              "audioSilenceSettings": {
                "audioSelectorName": "string",
                "audioSilenceThresholdMsec": integer
              },
              "inputLossSettings": {
                "inputLossThresholdMsec": integer
              },
              "videoBlackSettings": {
                "blackDetectThreshold": number,
                "videoBlackThresholdMsec": integer
              }
            }
          }
        ],
        "inputPreference": enum,
        "secondaryInputId": "string"
      },
      "inputAttachmentName": "string",
      "inputId": "string",
      "inputSettings": {
        "audioSelectors": [
          {
            "name": "string",
            "selectorSettings": {
              "audioHlsRenditionSelection": {
                "groupId": "string",
                "name": "string"
              },
              "audioLanguageSelection": {
                "languageCode": "string",
                "languageSelectionPolicy": enum
              },
              "audioPidSelection": {
                "pid": integer,
                "pids": [
                  {
                    "dolbyEDecode": {
                      "programSelection": enum
                    },
                    "pid": integer,
                    "premixSettings": {
                      "audioNormalizationSettings": {
                        "algorithm": enum,
                        "algorithmControl": enum,
                        "targetLkfs": number,
                        "peakCalculation": enum,
                        "peakLimiterThreshold": number
                      },
                      "channels": integer,
                      "gainDb": number,
                      "remixSettings": {
                        "channelMappings": [
                          {
                            "inputChannelLevels": [
                              {
                                "gain": integer,
                                "inputChannel": integer
                              }
                            ],
                            "outputChannel": integer
                          }
                        ],
                        "channelsIn": integer,
                        "channelsOut": integer
                      }
                    }
                  }
                ]
              },
              "audioTrackSelection": {
                "dolbyEDecode": {
                  "programSelection": enum
                },
                "tracks": [
                  {
                    "track": integer,
                    "premixSettings": {
                      "audioNormalizationSettings": {
                        "algorithm": enum,
                        "algorithmControl": enum,
                        "targetLkfs": number,
                        "peakCalculation": enum,
                        "peakLimiterThreshold": number
                      },
                      "channels": integer,
                      "gainDb": number,
                      "remixSettings": {
                        "channelMappings": [
                          {
                            "inputChannelLevels": [
                              {
                                "gain": integer,
                                "inputChannel": integer
                              }
                            ],
                            "outputChannel": integer
                          }
                        ],
                        "channelsIn": integer,
                        "channelsOut": integer
                      }
                    }
                  }
                ]
              }
            }
          }
        ],
        "captionSelectors": [
          {
            "languageCode": "string",
            "name": "string",
            "selectorSettings": {
              "ancillarySourceSettings": {
                "sourceAncillaryChannelNumber": integer
              },
              "aribSourceSettings": {
              },
              "dvbSubSourceSettings": {
                "ocrLanguage": enum,
                "pid": integer
              },
              "embeddedSourceSettings": {
                "convert608To708": enum,
                "scte20Detection": enum,
                "source608ChannelNumber": integer,
                "source608TrackNumber": integer
              },
              "scte20SourceSettings": {
                "convert608To708": enum,
                "source608ChannelNumber": integer
              },
              "scte27SourceSettings": {
                "ocrLanguage": enum,
                "pid": integer
              },
              "smartSubtitleSourceSettings": {
                "captionSynchronizationMode": enum,
                "inferenceFeedOutput": "string"
              },
              "teletextSourceSettings": {
                "outputRectangle": {
                  "height": number,
                  "leftOffset": number,
                  "topOffset": number,
                  "width": number
                },
                "pageNumber": "string"
              }
            }
          }
        ],
        "deblockFilter": enum,
        "denoiseFilter": enum,
        "filterStrength": integer,
        "inputFilter": enum,
        "networkInputSettings": {
          "hlsInputSettings": {
            "bandwidth": integer,
            "bufferSegments": integer,
            "retries": integer,
            "retryInterval": integer,
            "scte35Source": enum
          },
          "multicastInputSettings": {
            "sourceIpAddress": "string"
          },
          "serverValidation": enum
        },
        "scte35Pid": integer,
        "smpte2038DataPreference": enum,
        "sourceEndBehavior": enum,
        "videoSelector": {
          "colorSpace": enum,
          "colorSpaceSettings": {
            "hdr10Settings": {
              "maxCll": integer,
              "maxFall": integer
            }
          },
          "colorSpaceUsage": enum,
          "selectorSettings": {
            "videoSelectorPid": {
              "pid": integer
            },
            "videoSelectorProgramId": {
              "programId": integer
            }
          }
        }
      },
      "logicalInterfaceNames": [
        "string"
      ]
    }
  ],
  "inputSpecification": {
    "codec": enum,
    "maximumBitrate": enum,
    "resolution": enum
  },
  "linkedChannelSettings": {
    "followerChannelSettings": {
      "linkedChannelType": enum,
      "primaryChannelArn": "string"
    },
    "primaryChannelSettings": {
      "linkedChannelType": enum
    }
  },
  "logLevel": enum,
  "maintenance": {
    "maintenanceDay": enum,
    "maintenanceStartTime": "string"
  },
  "name": "string",
  "requestId": "string",
  "reserved": "string",
  "roleArn": "string",
  "tags": {
  },
  "vpc": {
    "publicAddressAllocationIds": [
      "string"
    ],
    "securityGroupIds": [
      "string"
    ],
    "subnetIds": [
      "string"
    ]
  },
  "inferenceSettings": {
    "audioFeedInputs": [
      {
        "audioSelectorName": "string",
        "feedInput": "string"
      }
    ],
    "enrichmentMethods": [
      enum
    ],
    "feedArn": "string"
  }
}
```

### Response bodies
<a name="channels-response-examples"></a>

#### ListChannelsResultModel schema
<a name="channels-response-body-listchannelsresultmodel-example"></a>

```
{
  "channels": [
    {
      "arn": "string",
      "cdiInputSpecification": {
        "resolution": enum
      },
      "channelClass": enum,
      "destinations": [
        {
          "id": "string",
          "logicalInterfaceNames": [
            "string"
          ],
          "mediaConnectRouterSettings": [
            {
              "encryptionType": enum,
              "secretArn": "string"
            }
          ],
          "mediaPackageSettings": [
            {
              "channelEndpointId": "string",
              "channelGroup": "string",
              "channelId": "string",
              "channelName": "string",
              "mediaPackageRegionName": "string"
            }
          ],
          "multiplexSettings": {
            "multiplexId": "string",
            "programName": "string"
          },
          "settings": [
            {
              "passwordParam": "string",
              "streamName": "string",
              "url": "string",
              "username": "string",
              "virtualSourceAddress": "string"
            }
          ],
          "srtSettings": [
            {
              "connectionMode": enum,
              "encryptionPassphraseSecretArn": "string",
              "listenerPort": integer,
              "streamId": "string",
              "url": "string"
            }
          ]
        }
      ],
      "egressEndpoints": [
        {
          "sourceIp": "string"
        }
      ],
      "id": "string",
      "inputAttachments": [
        {
          "automaticInputFailoverSettings": {
            "errorClearTimeMsec": integer,
            "failoverConditions": [
              {
                "failoverConditionSettings": {
                  "audioSilenceSettings": {
                    "audioSelectorName": "string",
                    "audioSilenceThresholdMsec": integer
                  },
                  "inputLossSettings": {
                    "inputLossThresholdMsec": integer
                  },
                  "videoBlackSettings": {
                    "blackDetectThreshold": number,
                    "videoBlackThresholdMsec": integer
                  }
                }
              }
            ],
            "inputPreference": enum,
            "secondaryInputId": "string"
          },
          "inputAttachmentName": "string",
          "inputId": "string",
          "inputSettings": {
            "audioSelectors": [
              {
                "name": "string",
                "selectorSettings": {
                  "audioHlsRenditionSelection": {
                    "groupId": "string",
                    "name": "string"
                  },
                  "audioLanguageSelection": {
                    "languageCode": "string",
                    "languageSelectionPolicy": enum
                  },
                  "audioPidSelection": {
                    "pid": integer,
                    "pids": [
                      {
                        "dolbyEDecode": {
                          "programSelection": enum
                        },
                        "pid": integer,
                        "premixSettings": {
                          "audioNormalizationSettings": {
                            "algorithm": enum,
                            "algorithmControl": enum,
                            "targetLkfs": number,
                            "peakCalculation": enum,
                            "peakLimiterThreshold": number
                          },
                          "channels": integer,
                          "gainDb": number,
                          "remixSettings": {
                            "channelMappings": [
                              {
                                "inputChannelLevels": [
                                  {
                                    "gain": integer,
                                    "inputChannel": integer
                                  }
                                ],
                                "outputChannel": integer
                              }
                            ],
                            "channelsIn": integer,
                            "channelsOut": integer
                          }
                        }
                      }
                    ]
                  },
                  "audioTrackSelection": {
                    "dolbyEDecode": {
                      "programSelection": enum
                    },
                    "tracks": [
                      {
                        "track": integer,
                        "premixSettings": {
                          "audioNormalizationSettings": {
                            "algorithm": enum,
                            "algorithmControl": enum,
                            "targetLkfs": number,
                            "peakCalculation": enum,
                            "peakLimiterThreshold": number
                          },
                          "channels": integer,
                          "gainDb": number,
                          "remixSettings": {
                            "channelMappings": [
                              {
                                "inputChannelLevels": [
                                  {
                                    "gain": integer,
                                    "inputChannel": integer
                                  }
                                ],
                                "outputChannel": integer
                              }
                            ],
                            "channelsIn": integer,
                            "channelsOut": integer
                          }
                        }
                      }
                    ]
                  }
                }
              }
            ],
            "captionSelectors": [
              {
                "languageCode": "string",
                "name": "string",
                "selectorSettings": {
                  "ancillarySourceSettings": {
                    "sourceAncillaryChannelNumber": integer
                  },
                  "aribSourceSettings": {
                  },
                  "dvbSubSourceSettings": {
                    "ocrLanguage": enum,
                    "pid": integer
                  },
                  "embeddedSourceSettings": {
                    "convert608To708": enum,
                    "scte20Detection": enum,
                    "source608ChannelNumber": integer,
                    "source608TrackNumber": integer
                  },
                  "scte20SourceSettings": {
                    "convert608To708": enum,
                    "source608ChannelNumber": integer
                  },
                  "scte27SourceSettings": {
                    "ocrLanguage": enum,
                    "pid": integer
                  },
                  "smartSubtitleSourceSettings": {
                    "captionSynchronizationMode": enum,
                    "inferenceFeedOutput": "string"
                  },
                  "teletextSourceSettings": {
                    "outputRectangle": {
                      "height": number,
                      "leftOffset": number,
                      "topOffset": number,
                      "width": number
                    },
                    "pageNumber": "string"
                  }
                }
              }
            ],
            "deblockFilter": enum,
            "denoiseFilter": enum,
            "filterStrength": integer,
            "inputFilter": enum,
            "networkInputSettings": {
              "hlsInputSettings": {
                "bandwidth": integer,
                "bufferSegments": integer,
                "retries": integer,
                "retryInterval": integer,
                "scte35Source": enum
              },
              "multicastInputSettings": {
                "sourceIpAddress": "string"
              },
              "serverValidation": enum
            },
            "scte35Pid": integer,
            "smpte2038DataPreference": enum,
            "sourceEndBehavior": enum,
            "videoSelector": {
              "colorSpace": enum,
              "colorSpaceSettings": {
                "hdr10Settings": {
                  "maxCll": integer,
                  "maxFall": integer
                }
              },
              "colorSpaceUsage": enum,
              "selectorSettings": {
                "videoSelectorPid": {
                  "pid": integer
                },
                "videoSelectorProgramId": {
                  "programId": integer
                }
              }
            }
          },
          "logicalInterfaceNames": [
            "string"
          ]
        }
      ],
      "inputSpecification": {
        "codec": enum,
        "maximumBitrate": enum,
        "resolution": enum
      },
      "logLevel": enum,
      "maintenance": {
        "maintenanceDay": enum,
        "maintenanceDeadline": "string",
        "maintenanceScheduledDate": "string",
        "maintenanceStartTime": "string"
      },
      "name": "string",
      "pipelinesRunningCount": integer,
      "roleArn": "string",
      "state": enum,
      "tags": {
      },
      "vpc": {
        "availabilityZones": [
          "string"
        ],
        "networkInterfaceIds": [
          "string"
        ],
        "securityGroupIds": [
          "string"
        ],
        "subnetIds": [
          "string"
        ]
      }
    }
  ],
  "nextToken": "string"
}
```

#### CreateChannelResultModel schema
<a name="channels-response-body-createchannelresultmodel-example"></a>

```
{
  "channel": {
    "arn": "string",
    "cdiInputSpecification": {
      "resolution": enum
    },
    "channelClass": enum,
    "destinations": [
      {
        "id": "string",
        "logicalInterfaceNames": [
          "string"
        ],
        "mediaConnectRouterSettings": [
          {
            "encryptionType": enum,
            "secretArn": "string"
          }
        ],
        "mediaPackageSettings": [
          {
            "channelEndpointId": "string",
            "channelGroup": "string",
            "channelId": "string",
            "channelName": "string",
            "mediaPackageRegionName": "string"
          }
        ],
        "multiplexSettings": {
          "multiplexId": "string",
          "programName": "string"
        },
        "settings": [
          {
            "passwordParam": "string",
            "streamName": "string",
            "url": "string",
            "username": "string",
            "virtualSourceAddress": "string"
          }
        ],
        "srtSettings": [
          {
            "connectionMode": enum,
            "encryptionPassphraseSecretArn": "string",
            "listenerPort": integer,
            "streamId": "string",
            "url": "string"
          }
        ]
      }
    ],
    "egressEndpoints": [
      {
        "sourceIp": "string"
      }
    ],
    "encoderSettings": {
      "audioDescriptions": [
        {
          "audioDashRoles": [
            enum
          ],
          "audioNormalizationSettings": {
            "algorithm": enum,
            "algorithmControl": enum,
            "targetLkfs": number,
            "peakCalculation": enum,
            "peakLimiterThreshold": number
          },
          "audioSelectorName": "string",
          "audioType": enum,
          "audioTypeControl": enum,
          "audioWatermarkingSettings": {
            "nielsenWatermarksSettings": {
              "nielsenCbetSettings": {
                "cbetCheckDigitString": "string",
                "cbetStepaside": enum,
                "csid": "string"
              },
              "nielsenDistributionType": enum,
              "nielsenNaesIiNwSettings": {
                "checkDigitString": "string",
                "sid": number,
                "timezone": enum
              },
              "nielsenNwOnlySettings": {
                "checkDigitString": "string",
                "sid": number,
                "timezone": enum
              }
            }
          },
          "codecSettings": {
            "aacSettings": {
              "bitrate": number,
              "codingMode": enum,
              "inputType": enum,
              "profile": enum,
              "rateControlMode": enum,
              "rawFormat": enum,
              "sampleRate": number,
              "spec": enum,
              "vbrQuality": enum
            },
            "ac3Settings": {
              "attenuationControl": enum,
              "bitrate": number,
              "bitstreamMode": enum,
              "codingMode": enum,
              "dialnorm": integer,
              "drcProfile": enum,
              "lfeFilter": enum,
              "metadataControl": enum
            },
            "eac3AtmosSettings": {
              "bitrate": number,
              "codingMode": enum,
              "dialnorm": integer,
              "drcLine": enum,
              "drcRf": enum,
              "heightTrim": number,
              "surroundTrim": number
            },
            "eac3Settings": {
              "attenuationControl": enum,
              "bitrate": number,
              "bitstreamMode": enum,
              "codingMode": enum,
              "dcFilter": enum,
              "dialnorm": integer,
              "drcLine": enum,
              "drcRf": enum,
              "lfeControl": enum,
              "lfeFilter": enum,
              "loRoCenterMixLevel": number,
              "loRoSurroundMixLevel": number,
              "ltRtCenterMixLevel": number,
              "ltRtSurroundMixLevel": number,
              "metadataControl": enum,
              "passthroughControl": enum,
              "phaseControl": enum,
              "stereoDownmix": enum,
              "surroundExMode": enum,
              "surroundMode": enum
            },
            "mp2Settings": {
              "bitrate": number,
              "codingMode": enum,
              "sampleRate": number
            },
            "passThroughSettings": {
            },
            "wavSettings": {
              "bitDepth": number,
              "codingMode": enum,
              "sampleRate": number
            }
          },
          "dvbDashAccessibility": enum,
          "languageCode": "string",
          "languageCodeControl": enum,
          "name": "string",
          "remixSettings": {
            "channelMappings": [
              {
                "inputChannelLevels": [
                  {
                    "gain": integer,
                    "inputChannel": integer
                  }
                ],
                "outputChannel": integer
              }
            ],
            "channelsIn": integer,
            "channelsOut": integer
          },
          "streamName": "string"
        }
      ],
      "availBlanking": {
        "availBlankingImage": {
          "passwordParam": "string",
          "uri": "string",
          "username": "string"
        },
        "state": enum
      },
      "availConfiguration": {
        "availSettings": {
          "esam": {
            "acquisitionPointId": "string",
            "adAvailOffset": integer,
            "passwordParam": "string",
            "poisEndpoint": "string",
            "username": "string",
            "zoneIdentity": "string"
          },
          "scte35SpliceInsert": {
            "adAvailOffset": integer,
            "noRegionalBlackoutFlag": enum,
            "webDeliveryAllowedFlag": enum
          },
          "scte35TimeSignalApos": {
            "adAvailOffset": integer,
            "noRegionalBlackoutFlag": enum,
            "webDeliveryAllowedFlag": enum
          }
        },
        "scte35SegmentationScope": enum
      },
      "blackoutSlate": {
        "blackoutSlateImage": {
          "passwordParam": "string",
          "uri": "string",
          "username": "string"
        },
        "networkEndBlackout": enum,
        "networkEndBlackoutImage": {
          "passwordParam": "string",
          "uri": "string",
          "username": "string"
        },
        "networkId": "string",
        "state": enum
      },
      "captionDescriptions": [
        {
          "accessibility": enum,
          "captionDashRoles": [
            enum
          ],
          "captionSelectorName": "string",
          "destinationSettings": {
            "aribDestinationSettings": {
            },
            "burnInDestinationSettings": {
              "alignment": enum,
              "backgroundColor": enum,
              "backgroundOpacity": integer,
              "font": {
                "passwordParam": "string",
                "uri": "string",
                "username": "string"
              },
              "fontColor": enum,
              "fontOpacity": integer,
              "fontResolution": integer,
              "fontSize": "string",
              "outlineColor": enum,
              "outlineSize": integer,
              "shadowColor": enum,
              "shadowOpacity": integer,
              "shadowXOffset": integer,
              "shadowYOffset": integer,
              "subtitleRows": enum,
              "teletextGridControl": enum,
              "xPosition": integer,
              "yPosition": integer
            },
            "dvbSubDestinationSettings": {
              "alignment": enum,
              "backgroundColor": enum,
              "backgroundOpacity": integer,
              "font": {
                "passwordParam": "string",
                "uri": "string",
                "username": "string"
              },
              "fontColor": enum,
              "fontOpacity": integer,
              "fontResolution": integer,
              "fontSize": "string",
              "outlineColor": enum,
              "outlineSize": integer,
              "shadowColor": enum,
              "shadowOpacity": integer,
              "shadowXOffset": integer,
              "shadowYOffset": integer,
              "subtitleRows": enum,
              "teletextGridControl": enum,
              "xPosition": integer,
              "yPosition": integer
            },
            "ebuTtDDestinationSettings": {
              "copyrightHolder": "string",
              "defaultFontSize": integer,
              "defaultLineHeight": integer,
              "fillLineGap": enum,
              "fontFamily": "string",
              "styleControl": enum
            },
            "embeddedDestinationSettings": {
              "position": {
                "yPositionLine": integer
              },
              "styleControl": enum
            },
            "embeddedPlusScte20DestinationSettings": {
            },
            "rtmpCaptionInfoDestinationSettings": {
            },
            "scte20PlusEmbeddedDestinationSettings": {
            },
            "scte27DestinationSettings": {
            },
            "smpteTtDestinationSettings": {
            },
            "teletextDestinationSettings": {
            },
            "ttmlDestinationSettings": {
              "position": {
                "yPositionPercentage": integer
              },
              "styleControl": enum
            },
            "webvttDestinationSettings": {
              "position": {
                "yPositionPercentage": integer
              },
              "styleControl": enum
            }
          },
          "dvbDashAccessibility": enum,
          "languageCode": "string",
          "languageDescription": "string",
          "name": "string"
        }
      ],
      "colorCorrectionSettings": {
        "globalColorCorrections": [
          {
            "inputColorSpace": enum,
            "outputColorSpace": enum,
            "uri": "string"
          }
        ]
      },
      "featureActivations": {
        "inputPrepareScheduleActions": enum,
        "outputStaticImageOverlayScheduleActions": enum
      },
      "globalConfiguration": {
        "initialAudioGain": integer,
        "inputEndAction": enum,
        "inputLossBehavior": {
          "blackFrameMsec": integer,
          "inputLossImageColor": "string",
          "inputLossImageSlate": {
            "passwordParam": "string",
            "uri": "string",
            "username": "string"
          },
          "inputLossImageType": enum,
          "repeatFrameMsec": integer
        },
        "outputLockingMode": enum,
        "outputLockingSettings": {
          "disabledLockingSettings": {
            "customEpoch": "string"
          },
          "epochLockingSettings": {
            "customEpoch": "string",
            "jamSyncTime": "string"
          },
          "pipelineLockingSettings": {
            "customEpoch": "string",
            "pipelineLockingMethod": enum
          }
        },
        "outputTimingSource": enum,
        "supportLowFramerateInputs": enum
      },
      "motionGraphicsConfiguration": {
        "motionGraphicsInsertion": enum,
        "motionGraphicsSettings": {
          "htmlMotionGraphicsSettings": {
          }
        }
      },
      "nielsenConfiguration": {
        "distributorId": "string",
        "nielsenPcmToId3Tagging": enum
      },
      "outputGroups": [
        {
          "name": "string",
          "outputGroupSettings": {
            "archiveGroupSettings": {
              "archiveCdnSettings": {
                "archiveS3Settings": {
                  "cannedAcl": enum,
                  "logUploads": enum
                }
              },
              "destination": {
                "destinationRefId": "string"
              },
              "rolloverInterval": integer
            },
            "cmafIngestGroupSettings": {
              "additionalDestinations": [
                {
                  "destination": {
                    "destinationRefId": "string"
                  }
                }
              ],
              "captionLanguageMappings": [
                {
                  "captionChannel": integer,
                  "languageCode": "string"
                }
              ],
              "destination": {
                "destinationRefId": "string"
              },
              "id3Behavior": enum,
              "id3NameModifier": "string",
              "klvBehavior": enum,
              "klvNameModifier": "string",
              "nielsenId3Behavior": enum,
              "nielsenId3NameModifier": "string",
              "scte35NameModifier": "string",
              "scte35Type": enum,
              "segmentLength": integer,
              "segmentLengthUnits": enum,
              "sendDelayMs": integer,
              "timedMetadataId3Frame": enum,
              "timedMetadataId3Period": integer,
              "timedMetadataPassthrough": enum,
              "watermarkingSettings": {
                "cmafIngestAbWatermarkerIrdetoSettings": {
                  "additionalDestinationsAlternateDestinations": [
                    {
                      "destinationRefId": "string"
                    }
                  ],
                  "alternateDestination": {
                    "destinationRefId": "string"
                  },
                  "customProfile": {
                    "embeddingFrequency": number,
                    "sceneCut": number,
                    "targetPsnr": number
                  },
                  "license": "string",
                  "operatorId": integer,
                  "polyPeriod": integer,
                  "profile": enum,
                  "watermarkIdLength": enum
                }
              }
            },
            "frameCaptureGroupSettings": {
              "destination": {
                "destinationRefId": "string"
              },
              "frameCaptureCdnSettings": {
                "frameCaptureS3Settings": {
                  "cannedAcl": enum,
                  "logUploads": enum
                }
              }
            },
            "hlsGroupSettings": {
              "adMarkers": [
                enum
              ],
              "baseUrlContent": "string",
              "baseUrlContent1": "string",
              "baseUrlManifest": "string",
              "baseUrlManifest1": "string",
              "captionLanguageMappings": [
                {
                  "captionChannel": integer,
                  "languageCode": "string",
                  "languageDescription": "string"
                }
              ],
              "captionLanguageSetting": enum,
              "clientCache": enum,
              "codecSpecification": enum,
              "constantIv": "string",
              "destination": {
                "destinationRefId": "string"
              },
              "directoryStructure": enum,
              "discontinuityTags": enum,
              "encryptionType": enum,
              "hlsCdnSettings": {
                "hlsAkamaiSettings": {
                  "connectionRetryInterval": integer,
                  "filecacheDuration": integer,
                  "httpTransferMode": enum,
                  "numRetries": integer,
                  "restartDelay": integer,
                  "salt": "string",
                  "token": "string"
                },
                "hlsBasicPutSettings": {
                  "connectionRetryInterval": integer,
                  "filecacheDuration": integer,
                  "numRetries": integer,
                  "restartDelay": integer
                },
                "hlsMediaStoreSettings": {
                  "connectionRetryInterval": integer,
                  "filecacheDuration": integer,
                  "mediaStoreStorageClass": enum,
                  "numRetries": integer,
                  "restartDelay": integer
                },
                "hlsS3Settings": {
                  "cannedAcl": enum,
                  "logUploads": enum
                },
                "hlsWebdavSettings": {
                  "connectionRetryInterval": integer,
                  "filecacheDuration": integer,
                  "httpTransferMode": enum,
                  "numRetries": integer,
                  "restartDelay": integer
                }
              },
              "hlsId3SegmentTagging": enum,
              "iFrameOnlyPlaylists": enum,
              "incompleteSegmentBehavior": enum,
              "indexNSegments": integer,
              "inputLossAction": enum,
              "ivInManifest": enum,
              "ivSource": enum,
              "keepSegments": integer,
              "keyFormat": "string",
              "keyFormatVersions": "string",
              "keyProviderSettings": {
                "staticKeySettings": {
                  "keyProviderServer": {
                    "passwordParam": "string",
                    "uri": "string",
                    "username": "string"
                  },
                  "staticKeyValue": "string"
                }
              },
              "manifestCompression": enum,
              "manifestDurationFormat": enum,
              "minSegmentLength": integer,
              "mode": enum,
              "outputSelection": enum,
              "programDateTime": enum,
              "programDateTimeClock": enum,
              "programDateTimePeriod": integer,
              "redundantManifest": enum,
              "segmentLength": integer,
              "segmentationMode": enum,
              "segmentsPerSubdirectory": integer,
              "streamInfResolution": enum,
              "timedMetadataId3Frame": enum,
              "timedMetadataId3Period": integer,
              "timestampDeltaMilliseconds": integer,
              "tsFileMode": enum
            },
            "mediaConnectRouterGroupSettings": {
              "availabilityZones": [
                "string"
              ]
            },
            "mediaPackageGroupSettings": {
              "destination": {
                "destinationRefId": "string"
              },
              "mediapackageV2GroupSettings": {
                "additionalDestinations": [
                  {
                    "destination": {
                      "destinationRefId": "string"
                    }
                  }
                ],
                "captionLanguageMappings": [
                  {
                    "captionChannel": integer,
                    "languageCode": "string",
                    "languageDescription": "string"
                  }
                ],
                "captionLanguageSetting": enum,
                "id3Behavior": enum,
                "klvBehavior": enum,
                "nielsenId3Behavior": enum,
                "scte35Type": enum,
                "segmentLength": integer,
                "segmentLengthUnits": enum,
                "timedMetadataId3Frame": enum,
                "timedMetadataId3Period": integer,
                "timedMetadataPassthrough": enum,
                "watermarkingSettings": {
                  "mediaPackageV2AbWatermarkerIrdetoSettings": {
                    "additionalDestinationsAlternateDestinations": [
                      {
                        "destinationRefId": "string"
                      }
                    ],
                    "alternateDestination": {
                      "destinationRefId": "string"
                    },
                    "customProfile": {
                      "embeddingFrequency": number,
                      "sceneCut": number,
                      "targetPsnr": number
                    },
                    "license": "string",
                    "operatorId": integer,
                    "polyPeriod": integer,
                    "profile": enum,
                    "watermarkIdLength": enum
                  }
                }
              }
            },
            "msSmoothGroupSettings": {
              "acquisitionPointId": "string",
              "audioOnlyTimecodeControl": enum,
              "certificateMode": enum,
              "connectionRetryInterval": integer,
              "destination": {
                "destinationRefId": "string"
              },
              "eventId": "string",
              "eventIdMode": enum,
              "eventStopBehavior": enum,
              "filecacheDuration": integer,
              "fragmentLength": integer,
              "inputLossAction": enum,
              "numRetries": integer,
              "restartDelay": integer,
              "segmentationMode": enum,
              "sendDelayMs": integer,
              "sparseTrackType": enum,
              "streamManifestBehavior": enum,
              "timestampOffset": "string",
              "timestampOffsetMode": enum
            },
            "multiplexGroupSettings": {
            },
            "rtmpGroupSettings": {
              "adMarkers": [
                enum
              ],
              "authenticationScheme": enum,
              "cacheFullBehavior": enum,
              "cacheLength": integer,
              "captionData": enum,
              "includeFillerNalUnits": enum,
              "inputLossAction": enum,
              "restartDelay": integer
            },
            "srtGroupSettings": {
              "inputLossAction": enum
            },
            "udpGroupSettings": {
              "inputLossAction": enum,
              "timedMetadataId3Frame": enum,
              "timedMetadataId3Period": integer
            }
          },
          "outputs": [
            {
              "audioDescriptionNames": [
                "string"
              ],
              "captionDescriptionNames": [
                "string"
              ],
              "outputName": "string",
              "outputSettings": {
                "archiveOutputSettings": {
                  "containerSettings": {
                    "m2tsSettings": {
                      "absentInputAudioBehavior": enum,
                      "arib": enum,
                      "aribCaptionsPid": "string",
                      "aribCaptionsPidControl": enum,
                      "audioBufferModel": enum,
                      "audioFramesPerPes": integer,
                      "audioPids": "string",
                      "audioStreamType": enum,
                      "bitrate": integer,
                      "bufferModel": enum,
                      "ccDescriptor": enum,
                      "dvbNitSettings": {
                        "networkId": integer,
                        "networkName": "string",
                        "repInterval": integer
                      },
                      "dvbSdtSettings": {
                        "outputSdt": enum,
                        "repInterval": integer,
                        "serviceName": "string",
                        "serviceProviderName": "string"
                      },
                      "dvbSubPids": "string",
                      "dvbTdtSettings": {
                        "repInterval": integer
                      },
                      "dvbTeletextPid": "string",
                      "ebif": enum,
                      "ebpAudioInterval": enum,
                      "ebpLookaheadMs": integer,
                      "ebpPlacement": enum,
                      "ecmPid": "string",
                      "esRateInPes": enum,
                      "etvPlatformPid": "string",
                      "etvSignalPid": "string",
                      "fragmentTime": number,
                      "klv": enum,
                      "klvDataPids": "string",
                      "nielsenId3Behavior": enum,
                      "nullPacketBitrate": number,
                      "patInterval": integer,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "pcrPid": "string",
                      "pmtInterval": integer,
                      "pmtPid": "string",
                      "programNum": integer,
                      "rateMode": enum,
                      "scte27Pids": "string",
                      "scte35Control": enum,
                      "scte35Pid": "string",
                      "scte35PrerollPullupMilliseconds": number,
                      "segmentationMarkers": enum,
                      "segmentationStyle": enum,
                      "segmentationTime": number,
                      "timedMetadataBehavior": enum,
                      "timedMetadataPid": "string",
                      "transportStreamId": integer,
                      "videoPid": "string"
                    },
                    "rawSettings": {
                    }
                  },
                  "extension": "string",
                  "nameModifier": "string"
                },
                "cmafIngestOutputSettings": {
                  "nameModifier": "string"
                },
                "frameCaptureOutputSettings": {
                  "nameModifier": "string"
                },
                "hlsOutputSettings": {
                  "h265PackagingType": enum,
                  "hlsSettings": {
                    "audioOnlyHlsSettings": {
                      "audioGroupId": "string",
                      "audioOnlyImage": {
                        "passwordParam": "string",
                        "uri": "string",
                        "username": "string"
                      },
                      "audioTrackType": enum,
                      "segmentType": enum
                    },
                    "fmp4HlsSettings": {
                      "audioRenditionSets": "string",
                      "nielsenId3Behavior": enum,
                      "timedMetadataBehavior": enum
                    },
                    "frameCaptureHlsSettings": {
                    },
                    "standardHlsSettings": {
                      "audioRenditionSets": "string",
                      "m3u8Settings": {
                        "audioFramesPerPes": integer,
                        "audioPids": "string",
                        "ecmPid": "string",
                        "klvBehavior": enum,
                        "klvDataPids": "string",
                        "nielsenId3Behavior": enum,
                        "patInterval": integer,
                        "pcrControl": enum,
                        "pcrPeriod": integer,
                        "pcrPid": "string",
                        "pmtInterval": integer,
                        "pmtPid": "string",
                        "programNum": integer,
                        "scte35Behavior": enum,
                        "scte35Pid": "string",
                        "timedMetadataBehavior": enum,
                        "timedMetadataPid": "string",
                        "transportStreamId": integer,
                        "videoPid": "string"
                      }
                    }
                  },
                  "nameModifier": "string",
                  "segmentModifier": "string"
                },
                "mediaConnectRouterOutputSettings": {
                  "connectedRouterInputs": {
                    "pipeline0": "string",
                    "pipeline1": "string"
                  },
                  "containerSettings": {
                    "m2tsSettings": {
                      "absentInputAudioBehavior": enum,
                      "arib": enum,
                      "aribCaptionsPid": "string",
                      "aribCaptionsPidControl": enum,
                      "audioBufferModel": enum,
                      "audioFramesPerPes": integer,
                      "audioPids": "string",
                      "audioStreamType": enum,
                      "bitrate": integer,
                      "bufferModel": enum,
                      "ccDescriptor": enum,
                      "dvbNitSettings": {
                        "networkId": integer,
                        "networkName": "string",
                        "repInterval": integer
                      },
                      "dvbSdtSettings": {
                        "outputSdt": enum,
                        "repInterval": integer,
                        "serviceName": "string",
                        "serviceProviderName": "string"
                      },
                      "dvbSubPids": "string",
                      "dvbTdtSettings": {
                        "repInterval": integer
                      },
                      "dvbTeletextPid": "string",
                      "ebif": enum,
                      "ebpAudioInterval": enum,
                      "ebpLookaheadMs": integer,
                      "ebpPlacement": enum,
                      "ecmPid": "string",
                      "esRateInPes": enum,
                      "etvPlatformPid": "string",
                      "etvSignalPid": "string",
                      "fragmentTime": number,
                      "klv": enum,
                      "klvDataPids": "string",
                      "nielsenId3Behavior": enum,
                      "nullPacketBitrate": number,
                      "patInterval": integer,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "pcrPid": "string",
                      "pmtInterval": integer,
                      "pmtPid": "string",
                      "programNum": integer,
                      "rateMode": enum,
                      "scte27Pids": "string",
                      "scte35Control": enum,
                      "scte35Pid": "string",
                      "scte35PrerollPullupMilliseconds": number,
                      "segmentationMarkers": enum,
                      "segmentationStyle": enum,
                      "segmentationTime": number,
                      "timedMetadataBehavior": enum,
                      "timedMetadataPid": "string",
                      "transportStreamId": integer,
                      "videoPid": "string"
                    }
                  },
                  "destination": {
                    "destinationRefId": "string"
                  }
                },
                "mediaPackageOutputSettings": {
                  "mediaPackageV2DestinationSettings": {
                    "audioGroupId": "string",
                    "audioRenditionSets": "string",
                    "hlsAutoSelect": enum,
                    "hlsDefault": enum,
                    "outputUsage": [
                      enum
                    ]
                  }
                },
                "msSmoothOutputSettings": {
                  "h265PackagingType": enum,
                  "nameModifier": "string"
                },
                "multiplexOutputSettings": {
                  "containerSettings": {
                    "multiplexM2tsSettings": {
                      "absentInputAudioBehavior": enum,
                      "arib": enum,
                      "audioBufferModel": enum,
                      "audioFramesPerPes": integer,
                      "audioStreamType": enum,
                      "ccDescriptor": enum,
                      "ebif": enum,
                      "esRateInPes": enum,
                      "klv": enum,
                      "nielsenId3Behavior": enum,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "scte35Control": enum,
                      "scte35PrerollPullupMilliseconds": number
                    }
                  },
                  "destination": {
                    "destinationRefId": "string"
                  }
                },
                "rtmpOutputSettings": {
                  "certificateMode": enum,
                  "connectionRetryInterval": integer,
                  "destination": {
                    "destinationRefId": "string"
                  },
                  "numRetries": integer
                },
                "srtOutputSettings": {
                  "bufferMsec": integer,
                  "containerSettings": {
                    "m2tsSettings": {
                      "absentInputAudioBehavior": enum,
                      "arib": enum,
                      "aribCaptionsPid": "string",
                      "aribCaptionsPidControl": enum,
                      "audioBufferModel": enum,
                      "audioFramesPerPes": integer,
                      "audioPids": "string",
                      "audioStreamType": enum,
                      "bitrate": integer,
                      "bufferModel": enum,
                      "ccDescriptor": enum,
                      "dvbNitSettings": {
                        "networkId": integer,
                        "networkName": "string",
                        "repInterval": integer
                      },
                      "dvbSdtSettings": {
                        "outputSdt": enum,
                        "repInterval": integer,
                        "serviceName": "string",
                        "serviceProviderName": "string"
                      },
                      "dvbSubPids": "string",
                      "dvbTdtSettings": {
                        "repInterval": integer
                      },
                      "dvbTeletextPid": "string",
                      "ebif": enum,
                      "ebpAudioInterval": enum,
                      "ebpLookaheadMs": integer,
                      "ebpPlacement": enum,
                      "ecmPid": "string",
                      "esRateInPes": enum,
                      "etvPlatformPid": "string",
                      "etvSignalPid": "string",
                      "fragmentTime": number,
                      "klv": enum,
                      "klvDataPids": "string",
                      "nielsenId3Behavior": enum,
                      "nullPacketBitrate": number,
                      "patInterval": integer,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "pcrPid": "string",
                      "pmtInterval": integer,
                      "pmtPid": "string",
                      "programNum": integer,
                      "rateMode": enum,
                      "scte27Pids": "string",
                      "scte35Control": enum,
                      "scte35Pid": "string",
                      "scte35PrerollPullupMilliseconds": number,
                      "segmentationMarkers": enum,
                      "segmentationStyle": enum,
                      "segmentationTime": number,
                      "timedMetadataBehavior": enum,
                      "timedMetadataPid": "string",
                      "transportStreamId": integer,
                      "videoPid": "string"
                    }
                  },
                  "destination": {
                    "destinationRefId": "string"
                  },
                  "encryptionType": enum,
                  "latency": integer
                },
                "udpOutputSettings": {
                  "bufferMsec": integer,
                  "containerSettings": {
                    "m2tsSettings": {
                      "absentInputAudioBehavior": enum,
                      "arib": enum,
                      "aribCaptionsPid": "string",
                      "aribCaptionsPidControl": enum,
                      "audioBufferModel": enum,
                      "audioFramesPerPes": integer,
                      "audioPids": "string",
                      "audioStreamType": enum,
                      "bitrate": integer,
                      "bufferModel": enum,
                      "ccDescriptor": enum,
                      "dvbNitSettings": {
                        "networkId": integer,
                        "networkName": "string",
                        "repInterval": integer
                      },
                      "dvbSdtSettings": {
                        "outputSdt": enum,
                        "repInterval": integer,
                        "serviceName": "string",
                        "serviceProviderName": "string"
                      },
                      "dvbSubPids": "string",
                      "dvbTdtSettings": {
                        "repInterval": integer
                      },
                      "dvbTeletextPid": "string",
                      "ebif": enum,
                      "ebpAudioInterval": enum,
                      "ebpLookaheadMs": integer,
                      "ebpPlacement": enum,
                      "ecmPid": "string",
                      "esRateInPes": enum,
                      "etvPlatformPid": "string",
                      "etvSignalPid": "string",
                      "fragmentTime": number,
                      "klv": enum,
                      "klvDataPids": "string",
                      "nielsenId3Behavior": enum,
                      "nullPacketBitrate": number,
                      "patInterval": integer,
                      "pcrControl": enum,
                      "pcrPeriod": integer,
                      "pcrPid": "string",
                      "pmtInterval": integer,
                      "pmtPid": "string",
                      "programNum": integer,
                      "rateMode": enum,
                      "scte27Pids": "string",
                      "scte35Control": enum,
                      "scte35Pid": "string",
                      "scte35PrerollPullupMilliseconds": number,
                      "segmentationMarkers": enum,
                      "segmentationStyle": enum,
                      "segmentationTime": number,
                      "timedMetadataBehavior": enum,
                      "timedMetadataPid": "string",
                      "transportStreamId": integer,
                      "videoPid": "string"
                    }
                  },
                  "destination": {
                    "destinationRefId": "string"
                  },
                  "fecOutputSettings": {
                    "columnDepth": integer,
                    "includeFec": enum,
                    "rowLength": integer
                  }
                }
              },
              "videoDescriptionName": "string"
            }
          ]
        }
      ],
      "thumbnailConfiguration": {
        "state": enum
      },
      "timecodeConfig": {
        "source": enum,
        "syncThreshold": integer
      },
      "videoDescriptions": [
        {
          "border": integer,
          "codecSettings": {
            "av1Settings": {
              "afdSignaling": enum,
              "bitDepth": enum,
              "bitrate": integer,
              "bufSize": integer,
              "colorSpaceSettings": {
                "colorSpacePassthroughSettings": {
                },
                "hdr10Settings": {
                  "maxCll": integer,
                  "maxFall": integer
                },
                "hlg2020Settings": {
                },
                "rec601Settings": {
                },
                "rec709Settings": {
                }
              },
              "fixedAfd": enum,
              "framerateDenominator": integer,
              "framerateNumerator": integer,
              "gopSize": number,
              "gopSizeUnits": enum,
              "level": enum,
              "lookAheadRateControl": enum,
              "maxBitrate": integer,
              "minBitrate": integer,
              "minIInterval": integer,
              "parDenominator": integer,
              "parNumerator": integer,
              "qvbrQualityLevel": integer,
              "rateControlMode": enum,
              "sceneChangeDetect": enum,
              "spatialAq": enum,
              "temporalAq": enum,
              "timecodeBurninSettings": {
                "fontSize": enum,
                "position": enum,
                "prefix": "string"
              },
              "timecodeInsertion": enum
            },
            "frameCaptureSettings": {
              "captureInterval": integer,
              "captureIntervalUnits": enum,
              "timecodeBurninSettings": {
                "fontSize": enum,
                "position": enum,
                "prefix": "string"
              }
            },
            "h264Settings": {
              "adaptiveQuantization": enum,
              "allowExplicitWeightedPrediction": enum,
              "afdSignaling": enum,
              "bitrate": integer,
              "bufFillPct": integer,
              "bufSize": integer,
              "colorMetadata": enum,
              "colorSpaceSettings": {
                "colorSpacePassthroughSettings": {
                },
                "rec601Settings": {
                },
                "rec709Settings": {
                }
              },
              "entropyEncoding": enum,
              "filterSettings": {
                "bandwidthReductionFilterSettings": {
                  "postFilterSharpening": enum,
                  "strength": enum
                },
                "temporalFilterSettings": {
                  "postFilterSharpening": enum,
                  "strength": enum
                }
              },
              "fixedAfd": enum,
              "flickerAq": enum,
              "forceFieldPictures": enum,
              "framerateControl": enum,
              "framerateDenominator": integer,
              "framerateNumerator": integer,
              "gopBReference": enum,
              "gopClosedCadence": integer,
              "gopNumBFrames": integer,
              "gopSize": number,
              "gopSizeUnits": enum,
              "level": enum,
              "lookAheadRateControl": enum,
              "maxBitrate": integer,
              "minBitrate": integer,
              "minIInterval": integer,
              "minQp": integer,
              "numRefFrames": integer,
              "parControl": enum,
              "parDenominator": integer,
              "parNumerator": integer,
              "profile": enum,
              "qualityLevel": enum,
              "qvbrQualityLevel": integer,
              "rateControlMode": enum,
              "scanType": enum,
              "sceneChangeDetect": enum,
              "slices": integer,
              "softness": integer,
              "spatialAq": enum,
              "subgopLength": enum,
              "syntax": enum,
              "temporalAq": enum,
              "timecodeBurninSettings": {
                "fontSize": enum,
                "position": enum,
                "prefix": "string"
              },
              "timecodeInsertion": enum
            },
            "h265Settings": {
              "adaptiveQuantization": enum,
              "afdSignaling": enum,
              "alternativeTransferFunction": enum,
              "bitrate": integer,
              "bufSize": integer,
              "colorMetadata": enum,
              "colorSpaceSettings": {
                "colorSpacePassthroughSettings": {
                },
                "dolbyVision81Settings": {
                },
                "hdr10Settings": {
                  "maxCll": integer,
                  "maxFall": integer
                },
                "hlg2020Settings": {
                },
                "rec601Settings": {
                },
                "rec709Settings": {
                }
              },
              "deblocking": enum,
              "filterSettings": {
                "bandwidthReductionFilterSettings": {
                  "postFilterSharpening": enum,
                  "strength": enum
                },
                "temporalFilterSettings": {
                  "postFilterSharpening": enum,
                  "strength": enum
                }
              },
              "fixedAfd": enum,
              "flickerAq": enum,
              "framerateDenominator": integer,
              "framerateNumerator": integer,
              "gopBReference": enum,
              "gopClosedCadence": integer,
              "gopNumBFrames": integer,
              "gopSize": number,
              "gopSizeUnits": enum,
              "level": enum,
              "lookAheadRateControl": enum,
              "maxBitrate": integer,
              "minBitrate": integer,
              "minIInterval": integer,
              "minQp": integer,
              "mvOverPictureBoundaries": enum,
              "mvTemporalPredictor": enum,
              "parDenominator": integer,
              "parNumerator": integer,
              "profile": enum,
              "qvbrQualityLevel": integer,
              "rateControlMode": enum,
              "scanType": enum,
              "sceneChangeDetect": enum,
              "slices": integer,
              "subgopLength": enum,
              "tier": enum,
              "tileHeight": integer,
              "tilePadding": enum,
              "tileWidth": integer,
              "timecodeBurninSettings": {
                "fontSize": enum,
                "position": enum,
                "prefix": "string"
              },
              "timecodeInsertion": enum,
              "treeblockSize": enum
            },
            "mpeg2Settings": {
              "adaptiveQuantization": enum,
              "afdSignaling": enum,
              "colorMetadata": enum,
              "colorSpace": enum,
              "displayAspectRatio": enum,
              "filterSettings": {
                "temporalFilterSettings": {
                  "postFilterSharpening": enum,
                  "strength": enum
                }
              },
              "fixedAfd": enum,
              "framerateDenominator": integer,
              "framerateNumerator": integer,
              "gopClosedCadence": integer,
              "gopNumBFrames": integer,
              "gopSize": number,
              "gopSizeUnits": enum,
              "scanType": enum,
              "subgopLength": enum,
              "timecodeBurninSettings": {
                "fontSize": enum,
                "position": enum,
                "prefix": "string"
              },
              "timecodeInsertion": enum
            }
          },
          "cropRectangle": {
            "height": integer,
            "width": integer,
            "x": integer,
            "y": integer
          },
          "height": integer,
          "name": "string",
          "outputPositionRectangle": {
            "height": integer,
            "width": integer,
            "x": integer,
            "y": integer
          },
          "respondToAfd": enum,
          "scalingBehavior": enum,
          "sharpness": integer,
          "width": integer
        }
      ]
    },
    "id": "string",
    "inputAttachments": [
      {
        "automaticInputFailoverSettings": {
          "errorClearTimeMsec": integer,
          "failoverConditions": [
            {
              "failoverConditionSettings": {
                "audioSilenceSettings": {
                  "audioSelectorName": "string",
                  "audioSilenceThresholdMsec": integer
                },
                "inputLossSettings": {
                  "inputLossThresholdMsec": integer
                },
                "videoBlackSettings": {
                  "blackDetectThreshold": number,
                  "videoBlackThresholdMsec": integer
                }
              }
            }
          ],
          "inputPreference": enum,
          "secondaryInputId": "string"
        },
        "inputAttachmentName": "string",
        "inputId": "string",
        "inputSettings": {
          "audioSelectors": [
            {
              "name": "string",
              "selectorSettings": {
                "audioHlsRenditionSelection": {
                  "groupId": "string",
                  "name": "string"
                },
                "audioLanguageSelection": {
                  "languageCode": "string",
                  "languageSelectionPolicy": enum
                },
                "audioPidSelection": {
                  "pid": integer,
                  "pids": [
                    {
                      "dolbyEDecode": {
                        "programSelection": enum
                      },
                      "pid": integer,
                      "premixSettings": {
                        "audioNormalizationSettings": {
                          "algorithm": enum,
                          "algorithmControl": enum,
                          "targetLkfs": number,
                          "peakCalculation": enum,
                          "peakLimiterThreshold": number
                        },
                        "channels": integer,
                        "gainDb": number,
                        "remixSettings": {
                          "channelMappings": [
                            {
                              "inputChannelLevels": [
                                {
                                  "gain": integer,
                                  "inputChannel": integer
                                }
                              ],
                              "outputChannel": integer
                            }
                          ],
                          "channelsIn": integer,
                          "channelsOut": integer
                        }
                      }
                    }
                  ]
                },
                "audioTrackSelection": {
                  "dolbyEDecode": {
                    "programSelection": enum
                  },
                  "tracks": [
                    {
                      "track": integer,
                      "premixSettings": {
                        "audioNormalizationSettings": {
                          "algorithm": enum,
                          "algorithmControl": enum,
                          "targetLkfs": number,
                          "peakCalculation": enum,
                          "peakLimiterThreshold": number
                        },
                        "channels": integer,
                        "gainDb": number,
                        "remixSettings": {
                          "channelMappings": [
                            {
                              "inputChannelLevels": [
                                {
                                  "gain": integer,
                                  "inputChannel": integer
                                }
                              ],
                              "outputChannel": integer
                            }
                          ],
                          "channelsIn": integer,
                          "channelsOut": integer
                        }
                      }
                    }
                  ]
                }
              }
            }
          ],
          "captionSelectors": [
            {
              "languageCode": "string",
              "name": "string",
              "selectorSettings": {
                "ancillarySourceSettings": {
                  "sourceAncillaryChannelNumber": integer
                },
                "aribSourceSettings": {
                },
                "dvbSubSourceSettings": {
                  "ocrLanguage": enum,
                  "pid": integer
                },
                "embeddedSourceSettings": {
                  "convert608To708": enum,
                  "scte20Detection": enum,
                  "source608ChannelNumber": integer,
                  "source608TrackNumber": integer
                },
                "scte20SourceSettings": {
                  "convert608To708": enum,
                  "source608ChannelNumber": integer
                },
                "scte27SourceSettings": {
                  "ocrLanguage": enum,
                  "pid": integer
                },
                "smartSubtitleSourceSettings": {
                  "captionSynchronizationMode": enum,
                  "inferenceFeedOutput": "string"
                },
                "teletextSourceSettings": {
                  "outputRectangle": {
                    "height": number,
                    "leftOffset": number,
                    "topOffset": number,
                    "width": number
                  },
                  "pageNumber": "string"
                }
              }
            }
          ],
          "deblockFilter": enum,
          "denoiseFilter": enum,
          "filterStrength": integer,
          "inputFilter": enum,
          "networkInputSettings": {
            "hlsInputSettings": {
              "bandwidth": integer,
              "bufferSegments": integer,
              "retries": integer,
              "retryInterval": integer,
              "scte35Source": enum
            },
            "multicastInputSettings": {
              "sourceIpAddress": "string"
            },
            "serverValidation": enum
          },
          "scte35Pid": integer,
          "smpte2038DataPreference": enum,
          "sourceEndBehavior": enum,
          "videoSelector": {
            "colorSpace": enum,
            "colorSpaceSettings": {
              "hdr10Settings": {
                "maxCll": integer,
                "maxFall": integer
              }
            },
            "colorSpaceUsage": enum,
            "selectorSettings": {
              "videoSelectorPid": {
                "pid": integer
              },
              "videoSelectorProgramId": {
                "programId": integer
              }
            }
          }
        },
        "logicalInterfaceNames": [
          "string"
        ]
      }
    ],
    "inputSpecification": {
      "codec": enum,
      "maximumBitrate": enum,
      "resolution": enum
    },
    "logLevel": enum,
    "maintenance": {
      "maintenanceDay": enum,
      "maintenanceDeadline": "string",
      "maintenanceScheduledDate": "string",
      "maintenanceStartTime": "string"
    },
    "name": "string",
    "pipelineDetails": [
      {
        "activeInputAttachmentName": "string",
        "activeInputSwitchActionName": "string",
        "activeMotionGraphicsActionName": "string",
        "activeMotionGraphicsUri": "string",
        "pipelineId": "string"
      }
    ],
    "pipelinesRunningCount": integer,
    "roleArn": "string",
    "state": enum,
    "tags": {
    },
    "vpc": {
      "availabilityZones": [
        "string"
      ],
      "networkInterfaceIds": [
        "string"
      ],
      "securityGroupIds": [
        "string"
      ],
      "subnetIds": [
        "string"
      ]
    },
    "inferenceSettings": {
      "audioFeedInputs": [
        {
          "audioSelectorName": "string",
          "feedInput": "string"
        }
      ],
      "enrichmentMethods": [
        enum
      ],
      "feedArn": "string"
    }
  }
}
```

#### InvalidRequest schema
<a name="channels-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="channels-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="channels-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### ChannelConfigurationValidationError schema
<a name="channels-response-body-channelconfigurationvalidationerror-example"></a>

```
{
  "message": "string",
  "validationErrors": [
    {
      "elementPath": "string",
      "errorMessage": "string"
    }
  ]
}
```

#### LimitExceeded schema
<a name="channels-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="channels-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="channels-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="channels-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="channels-properties"></a>

### AacCodingMode
<a name="channels-model-aaccodingmode"></a>

Aac Coding Mode
+ `AD_RECEIVER_MIX`
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_5_1`

### AacInputType
<a name="channels-model-aacinputtype"></a>

Aac Input Type
+ `BROADCASTER_MIXED_AD`
+ `NORMAL`

### AacProfile
<a name="channels-model-aacprofile"></a>

Aac Profile
+ `HEV1`
+ `HEV2`
+ `LC`

### AacRateControlMode
<a name="channels-model-aacratecontrolmode"></a>

Aac Rate Control Mode
+ `CBR`
+ `VBR`

### AacRawFormat
<a name="channels-model-aacrawformat"></a>

Aac Raw Format
+ `LATM_LOAS`
+ `NONE`

### AacSettings
<a name="channels-model-aacsettings"></a>

Aac Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. Valid values depend on rate control mode and profile. |
| codingMode | [AacCodingMode](#channels-model-aaccodingmode) | False | Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E. |
| inputType | [AacInputType](#channels-model-aacinputtype) | False | Set to "broadcasterMixedAd" when input contains pre-mixed main audio \+ AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to "normal" when input does not contain pre-mixed audio \+ AD. |
| profile | [AacProfile](#channels-model-aacprofile) | False | AAC Profile. |
| rateControlMode | [AacRateControlMode](#channels-model-aacratecontrolmode) | False | Rate Control Mode. |
| rawFormat | [AacRawFormat](#channels-model-aacrawformat) | False | Sets LATM / LOAS AAC output for raw containers. |
| sampleRate | number | False | Sample rate in Hz. Valid values depend on rate control mode and profile. |
| spec | [AacSpec](#channels-model-aacspec) | False | Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers. |
| vbrQuality | [AacVbrQuality](#channels-model-aacvbrquality) | False | VBR Quality Level - Only used if rateControlMode is VBR. |

### AacSpec
<a name="channels-model-aacspec"></a>

Aac Spec
+ `MPEG2`
+ `MPEG4`

### AacVbrQuality
<a name="channels-model-aacvbrquality"></a>

Aac Vbr Quality
+ `HIGH`
+ `LOW`
+ `MEDIUM_HIGH`
+ `MEDIUM_LOW`

### AbWatermarkerIdLength
<a name="channels-model-abwatermarkeridlength"></a>

Ab Watermarker Id Length
+ `ID_2048`
+ `ID_512`

### AbWatermarkingCustomProfile
<a name="channels-model-abwatermarkingcustomprofile"></a>

The vendor-specified custom profile options

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| embeddingFrequency | number<br />Minimum: 250<br />Maximum: 5000 | True | The frequency with which watermarks will be embedded, in milliseconds. |
| sceneCut | number<br />Minimum: -1<br />Maximum: 5 | True | The number of frames after scene-cut to embed the watermark. |
| targetPsnr | number<br />Minimum: 32<br />Maximum: 46 | True | The target PSNR of the watermarked frame |

### AbWatermarkingProfile
<a name="channels-model-abwatermarkingprofile"></a>

Ab Watermarking Profile
+ `CAMCORDING`
+ `CUSTOM`
+ `DEFAULT`
+ `HQ`
+ `MEZZANINE`
+ `ROBUST`

### Ac3AttenuationControl
<a name="channels-model-ac3attenuationcontrol"></a>

Ac3 Attenuation Control
+ `ATTENUATE_3_DB`
+ `NONE`

### Ac3BitstreamMode
<a name="channels-model-ac3bitstreammode"></a>

Ac3 Bitstream Mode
+ `COMMENTARY`
+ `COMPLETE_MAIN`
+ `DIALOGUE`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `MUSIC_AND_EFFECTS`
+ `VISUALLY_IMPAIRED`
+ `VOICE_OVER`

### Ac3CodingMode
<a name="channels-model-ac3codingmode"></a>

Ac3 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`

### Ac3DrcProfile
<a name="channels-model-ac3drcprofile"></a>

Ac3 Drc Profile
+ `FILM_STANDARD`
+ `NONE`

### Ac3LfeFilter
<a name="channels-model-ac3lfefilter"></a>

Ac3 Lfe Filter
+ `DISABLED`
+ `ENABLED`

### Ac3MetadataControl
<a name="channels-model-ac3metadatacontrol"></a>

Ac3 Metadata Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Ac3Settings
<a name="channels-model-ac3settings"></a>

Ac3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attenuationControl | [Ac3AttenuationControl](#channels-model-ac3attenuationcontrol) | False | Applies a 3 dB attenuation to the surround channels. Applies only when the coding mode parameter is CODING\_MODE\_3\_2\_LFE. |
| bitrate | number | False | Average bitrate in bits/second. Valid bitrates depend on the coding mode. |
| bitstreamMode | [Ac3BitstreamMode](#channels-model-ac3bitstreammode) | False | Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values. |
| codingMode | [Ac3CodingMode](#channels-model-ac3codingmode) | False | Dolby Digital coding mode. Determines number of channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through. |
| drcProfile | [Ac3DrcProfile](#channels-model-ac3drcprofile) | False | If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification. |
| lfeFilter | [Ac3LfeFilter](#channels-model-ac3lfefilter) | False | When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode. |
| metadataControl | [Ac3MetadataControl](#channels-model-ac3metadatacontrol) | False | When set to "followInput", encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |

### AccessDenied
<a name="channels-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### AccessibilityType
<a name="channels-model-accessibilitytype"></a>

Accessibility Type
+ `DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES`
+ `IMPLEMENTS_ACCESSIBILITY_FEATURES`

### AdditionalDestinations
<a name="channels-model-additionaldestinations"></a>

Additional output destinations for a CMAF Ingest output group

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | The destination location |

### AfdSignaling
<a name="channels-model-afdsignaling"></a>

Afd Signaling
+ `AUTO`
+ `FIXED`
+ `NONE`

### AncillarySourceSettings
<a name="channels-model-ancillarysourcesettings"></a>

Ancillary Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceAncillaryChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the number (1 to 4) of the captions channel you want to extract from the ancillary captions. If you plan to convert the ancillary captions to another format, complete this field. If you plan to choose Embedded as the captions destination in the output (to pass through all the channels in the ancillary captions), leave this field blank because MediaLive ignores the field. |

### AnywhereSettings
<a name="channels-model-anywheresettings"></a>

Elemental anywhere settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelPlacementGroupId | string | False | The ID of the channel placement group for the channel. |
| clusterId | string | False | The ID of the cluster for the channel. |

### ArchiveCdnSettings
<a name="channels-model-archivecdnsettings"></a>

Archive Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveS3Settings | [ArchiveS3Settings](#channels-model-archives3settings) | False |  |

### ArchiveContainerSettings
<a name="channels-model-archivecontainersettings"></a>

Archive Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| m2tsSettings | [M2tsSettings](#channels-model-m2tssettings) | False |  |
| rawSettings | [RawSettings](#channels-model-rawsettings) | False |  |

### ArchiveGroupSettings
<a name="channels-model-archivegroupsettings"></a>

Archive Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveCdnSettings | [ArchiveCdnSettings](#channels-model-archivecdnsettings) | False | Parameters that control interactions with the CDN. |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | A directory and base filename where archive files should be written. |
| rolloverInterval | integer<br />Minimum: 1 | False | Number of seconds to write to archive file before closing and starting a new one. |

### ArchiveOutputSettings
<a name="channels-model-archiveoutputsettings"></a>

Archive Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| containerSettings | [ArchiveContainerSettings](#channels-model-archivecontainersettings) | True | Settings specific to the container type of the file. |
| extension | string | False | Output file extension. If excluded, this will be auto-selected from the container type. |
| nameModifier | string | False | String concatenated to the end of the destination filename. Required for multiple outputs of the same type. |

### ArchiveS3LogUploads
<a name="channels-model-archives3loguploads"></a>

Archive S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### ArchiveS3Settings
<a name="channels-model-archives3settings"></a>

Archive S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [ArchiveS3LogUploads](#channels-model-archives3loguploads) | False | When set to enabled, each upload to CDN or server will be logged. |

### AribDestinationSettings
<a name="channels-model-aribdestinationsettings"></a>

Arib Destination Settings

### AribSourceSettings
<a name="channels-model-aribsourcesettings"></a>

Arib Source Settings

### AudioChannelMapping
<a name="channels-model-audiochannelmapping"></a>

Audio Channel Mapping

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputChannelLevels | Array of type [InputChannelLevel](#channels-model-inputchannellevel) | True | Indices and gain values for each input channel that should be remixed into this output channel. |
| outputChannel | integer<br />Minimum: 0<br />Maximum: 7 | True | The index of the output channel being produced. |

### AudioCodecSettings
<a name="channels-model-audiocodecsettings"></a>

Audio Codec Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aacSettings | [AacSettings](#channels-model-aacsettings) | False |  |
| ac3Settings | [Ac3Settings](#channels-model-ac3settings) | False |  |
| eac3AtmosSettings | [Eac3AtmosSettings](#channels-model-eac3atmossettings) | False |  |
| eac3Settings | [Eac3Settings](#channels-model-eac3settings) | False |  |
| mp2Settings | [Mp2Settings](#channels-model-mp2settings) | False |  |
| passThroughSettings | [PassThroughSettings](#channels-model-passthroughsettings) | False |  |
| wavSettings | [WavSettings](#channels-model-wavsettings) | False |  |

### AudioDescription
<a name="channels-model-audiodescription"></a>

Audio Description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDashRoles | Array of type [DashRoleAudio](#channels-model-dashroleaudio) | False | Identifies the DASH roles to assign to this audio output. Applies only when the audio output is configured for DVB DASH accessibility signaling. |
| audioNormalizationSettings | [AudioNormalizationSettings](#channels-model-audionormalizationsettings) | False | Advanced audio normalization settings. |
| audioSelectorName | string | True | The name of the AudioSelector used as the source for this AudioDescription. |
| audioType | [AudioType](#channels-model-audiotype) | False | Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1. |
| audioTypeControl | [AudioDescriptionAudioTypeControl](#channels-model-audiodescriptionaudiotypecontrol) | False | Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd. |
| audioWatermarkingSettings | [AudioWatermarkSettings](#channels-model-audiowatermarksettings) | False | Settings to configure one or more solutions that insert audio watermarks in the audio encode |
| codecSettings | [AudioCodecSettings](#channels-model-audiocodecsettings) | False | Audio codec settings. |
| dvbDashAccessibility | [DvbDashAccessibility](#channels-model-dvbdashaccessibility) | False | Identifies DVB DASH accessibility signaling in this audio output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers. |
| languageCode | string<br />MinLength: 1<br />MaxLength: 35 | False | RFC 5646 language code representing the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input. |
| languageCodeControl | [AudioDescriptionLanguageCodeControl](#channels-model-audiodescriptionlanguagecodecontrol) | False | Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input. |
| name | string<br />MaxLength: 255 | True | The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event. |
| remixSettings | [RemixSettings](#channels-model-remixsettings) | False | Settings that control how input audio channels are remixed into the output audio channels. |
| streamName | string | False | Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary). |

### AudioDescriptionAudioTypeControl
<a name="channels-model-audiodescriptionaudiotypecontrol"></a>

Audio Description Audio Type Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioDescriptionLanguageCodeControl
<a name="channels-model-audiodescriptionlanguagecodecontrol"></a>

Audio Description Language Code Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioDolbyEDecode
<a name="channels-model-audiodolbyedecode"></a>

Audio Dolby EDecode

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| programSelection | [DolbyEProgramSelection](#channels-model-dolbyeprogramselection) | True | Applies only to Dolby E. Enter the program ID (according to the metadata in the audio) of the Dolby E program to extract from the specified track. One program extracted per audio selector. To select multiple programs, create multiple selectors with the same Track and different Program numbers. “All channels” means to ignore the program IDs and include all the channels in this selector; useful if metadata is known to be incorrect. |

### AudioFeedInput
<a name="channels-model-audiofeedinput"></a>

Maps an audio selector in the channel to a feed input on the associated Elemental Inference feed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectorName | string | False | The name of the audio selector in the channel that will be sent to the Elemental Inference feed input. |
| feedInput | string | False | The name of the feed input on the Elemental Inference feed that will receive the audio from the specified audio selector. |

### AudioHlsRenditionSelection
<a name="channels-model-audiohlsrenditionselection"></a>

Audio Hls Rendition Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| groupId | string<br />MinLength: 1 | True | Specifies the GROUP-ID in the \#EXT-X-MEDIA tag of the target HLS audio rendition. |
| name | string<br />MinLength: 1 | True | Specifies the NAME in the \#EXT-X-MEDIA tag of the target HLS audio rendition. |

### AudioLanguageSelection
<a name="channels-model-audiolanguageselection"></a>

Audio Language Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | True | Selects a specific three-letter language code from within an audio source. |
| languageSelectionPolicy | [AudioLanguageSelectionPolicy](#channels-model-audiolanguageselectionpolicy) | False | When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language. |

### AudioLanguageSelectionPolicy
<a name="channels-model-audiolanguageselectionpolicy"></a>

Audio Language Selection Policy
+ `LOOSE`
+ `STRICT`

### AudioNormalizationAlgorithm
<a name="channels-model-audionormalizationalgorithm"></a>

Audio Normalization Algorithm
+ `ITU_1770_1`
+ `ITU_1770_2`
+ `ITU_1770_3`
+ `ITU_1770_4`

### AudioNormalizationAlgorithmControl
<a name="channels-model-audionormalizationalgorithmcontrol"></a>

Audio Normalization Algorithm Control
+ `CORRECT_AUDIO`

### AudioNormalizationPeakCalculation
<a name="channels-model-audionormalizationpeakcalculation"></a>

Specifies the method for calculating peak loudness during audio normalization.
+ `NONE`
+ `TRUE_PEAK`

### AudioNormalizationSettings
<a name="channels-model-audionormalizationsettings"></a>

Audio Normalization Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [AudioNormalizationAlgorithm](#channels-model-audionormalizationalgorithm) | False | The audio normalization algorithm to use. Valid values:+ ITU\_1770\_1 – ITU-R BS.1770-1 (ungated loudness). Measures average loudness for an entire piece of content. Suitable for short-form content under ATSC A/85. Supports up to 5.1 audio channels.<br />+ ITU\_1770\_2 – ITU-R BS.1770-2 (gated loudness). Measures gated average loudness compliant with EBU R128. Supports up to 5.1 audio channels.<br />+ ITU\_1770\_3 – ITU-R BS.1770-3 (modified peak). Uses the ITU-R BS.1770-2 algorithm with an updated true peak measurement.<br />+ ITU\_1770\_4 – ITU-R BS.1770-4 (higher channel count). Supports more audio channels, including 7.1 configurations. |
| algorithmControl | [AudioNormalizationAlgorithmControl](#channels-model-audionormalizationalgorithmcontrol) | False | When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted. |
| peakCalculation | [AudioNormalizationPeakCalculation](#channels-model-audionormalizationpeakcalculation) | False | Specifies whether to calculate true peak loudness for each output audio track. When set to TRUE\_PEAK, the service calculates true peak values for every output. |
| peakLimiterThreshold | number<br />Minimum: -8<br />Maximum: 0 | False | The peak limiter threshold, in decibels relative to true peak (dBTP), when TRUE\_PEAK peak calculation is enabled. When TRUE\_PEAK is not enabled, the threshold applies as decibels relative to full scale (dBFS). |
| targetLkfs | number<br />Minimum: -59<br />Maximum: 0 | False | Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS. |

### AudioOnlyHlsSegmentType
<a name="channels-model-audioonlyhlssegmenttype"></a>

Audio Only Hls Segment Type
+ `AAC`
+ `FMP4`

### AudioOnlyHlsSettings
<a name="channels-model-audioonlyhlssettings"></a>

Audio Only Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioGroupId | string | False | Specifies the group to which the audio Rendition belongs. |
| audioOnlyImage | [InputLocation](#channels-model-inputlocation) | False | Optional. Specifies the .jpg or .png image to use as the cover art for an audio-only output. We recommend a low bit-size file because the image increases the output audio bandwidth. The image is attached to the audio as an ID3 tag, frame type APIC, picture type 0x10, as per the "ID3 tag version 2.4.0 - Native Frames" standard. |
| audioTrackType | [AudioOnlyHlsTrackType](#channels-model-audioonlyhlstracktype) | False | Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO |
| segmentType | [AudioOnlyHlsSegmentType](#channels-model-audioonlyhlssegmenttype) | False | Specifies the segment type. |

### AudioOnlyHlsTrackType
<a name="channels-model-audioonlyhlstracktype"></a>

Audio Only Hls Track Type
+ `ALTERNATE_AUDIO_AUTO_SELECT`
+ `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
+ `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
+ `AUDIO_ONLY_VARIANT_STREAM`

### AudioPid
<a name="channels-model-audiopid"></a>

Contains the packet identifier (PID) value and optional pre-mixer settings for a single audio stream within a source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dolbyEDecode | [AudioDolbyEDecode](#channels-model-audiodolbyedecode) | False | Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337. When using the 'pids' array, if this field is not specified and Dolby E content is present, the decoder will extract the specified program. To maintain legacy behavior (allPrograms), explicitly set programSelection to "allChannels". |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | True | The packet identifier (PID) value from within the source. |
| premixSettings | [AudioPreMixerSettings](#channels-model-audiopremixersettings) | False | The optional audio pre-mixer settings for this PID. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this PID before interleaving. |

### AudioPidSelection
<a name="channels-model-audiopidselection"></a>

Audio Pid Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | True | Selects a specific PID from within a source. |
| pids | Array of type [AudioPid](#channels-model-audiopid) | False | Selects one or more unique packet identifiers (PIDs) from within a source. When using PIDs, you can specify per-PID audio pre-mixer settings. |

### AudioPreMixerSettings
<a name="channels-model-audiopremixersettings"></a>

Contains settings for preprocessing audio before interleaving, including loudness normalization, channel remixing, and gain adjustment. Apply these settings to individual PIDs or audio tracks to control audio output characteristics before the tracks are combined.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioNormalizationSettings | [AudioNormalizationSettings](#channels-model-audionormalizationsettings) | False | The audio normalization settings for loudness control. When specified, the service normalizes audio loudness according to the chosen algorithm. |
| channels | integer<br />Minimum: 1<br />Maximum: 16 | False | The number of audio channels to remix the audio to. If you don't specify a value, the service passes through the original channel count. The remixSettings setting overrides this value when specified. |
| gainDb | number<br />Minimum: -60<br />Maximum: 60 | False | The gain adjustment, in decibels (dB), to apply to this audio. |
| remixSettings | [RemixSettings](#channels-model-remixsettings) | False | The settings that control how the service remixes input audio channels. When specified, these settings provide fine-grained control over channel mapping and gain levels, and take precedence over the channels setting. |

### AudioSelector
<a name="channels-model-audioselector"></a>

Audio Selector

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string<br />MinLength: 1 | True | The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input. |
| selectorSettings | [AudioSelectorSettings](#channels-model-audioselectorsettings) | False | The audio selector settings. |

### AudioSelectorSettings
<a name="channels-model-audioselectorsettings"></a>

Audio Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioHlsRenditionSelection | [AudioHlsRenditionSelection](#channels-model-audiohlsrenditionselection) | False |  |
| audioLanguageSelection | [AudioLanguageSelection](#channels-model-audiolanguageselection) | False |  |
| audioPidSelection | [AudioPidSelection](#channels-model-audiopidselection) | False |  |
| audioTrackSelection | [AudioTrackSelection](#channels-model-audiotrackselection) | False |  |

### AudioSilenceFailoverSettings
<a name="channels-model-audiosilencefailoversettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectorName | string | True | The name of the audio selector in the input that MediaLive should monitor to detect silence. Select your most important rendition. If you didn't create an audio selector in this input, leave blank. |
| audioSilenceThresholdMsec | integer<br />Minimum: 1000 | False | The amount of time (in milliseconds) that the active input must be silent before automatic input failover occurs. Silence is defined as audio loss or audio quieter than -50 dBFS. |

### AudioTrack
<a name="channels-model-audiotrack"></a>

Audio Track

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| premixSettings | [AudioPreMixerSettings](#channels-model-audiopremixersettings) | False | The optional audio pre-mixer settings for this track. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this track before interleaving. |
| track | integer<br />Minimum: 1 | True | 1-based integer value that maps to a specific audio track |

### AudioTrackSelection
<a name="channels-model-audiotrackselection"></a>

Audio Track Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dolbyEDecode | [AudioDolbyEDecode](#channels-model-audiodolbyedecode) | False | Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337 |
| tracks | Array of type [AudioTrack](#channels-model-audiotrack) | True | Selects one or more unique audio tracks from within a source. |

### AudioType
<a name="channels-model-audiotype"></a>

Audio Type
+ `CLEAN_EFFECTS`
+ `HEARING_IMPAIRED`
+ `UNDEFINED`
+ `VISUAL_IMPAIRED_COMMENTARY`

### AudioWatermarkSettings
<a name="channels-model-audiowatermarksettings"></a>

Audio Watermark Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nielsenWatermarksSettings | [NielsenWatermarksSettings](#channels-model-nielsenwatermarkssettings) | False | Settings to configure Nielsen Watermarks in the audio encode |

### AuthenticationScheme
<a name="channels-model-authenticationscheme"></a>

Authentication Scheme
+ `AKAMAI`
+ `COMMON`

### AutomaticInputFailoverSettings
<a name="channels-model-automaticinputfailoversettings"></a>

The settings for Automatic Input Failover.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorClearTimeMsec | integer<br />Minimum: 1 | False | This clear time defines the requirement a recovered input must meet to be considered healthy. The input must have no failover conditions for this length of time. Enter a time in milliseconds. This value is particularly important if the input\_preference for the failover pair is set to PRIMARY\_INPUT\_PREFERRED, because after this time, MediaLive will switch back to the primary input. |
| failoverConditions | Array of type [FailoverCondition](#channels-model-failovercondition) | False | A list of failover conditions. If any of these conditions occur, MediaLive will perform a failover to the other input. |
| inputPreference | [InputPreference](#channels-model-inputpreference) | False | Input preference when deciding which input to make active when a previously failed input has recovered. |
| secondaryInputId | string | True | The input ID of the secondary input in the automatic input failover pair. |

### Av1BitDepth
<a name="channels-model-av1bitdepth"></a>

Av1 Bit Depth
+ `DEPTH_10`
+ `DEPTH_8`

### Av1ColorSpaceSettings
<a name="channels-model-av1colorspacesettings"></a>

Av1 Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpacePassthroughSettings | [ColorSpacePassthroughSettings](#channels-model-colorspacepassthroughsettings) | False |  |
| hdr10Settings | [Hdr10Settings](#channels-model-hdr10settings) | False |  |
| hlg2020Settings | [Hlg2020Settings](#channels-model-hlg2020settings) | False |  |
| rec601Settings | [Rec601Settings](#channels-model-rec601settings) | False |  |
| rec709Settings | [Rec709Settings](#channels-model-rec709settings) | False |  |

### Av1GopSizeUnits
<a name="channels-model-av1gopsizeunits"></a>

Av1 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### Av1Level
<a name="channels-model-av1level"></a>

Av1 Level
+ `AV1_LEVEL_2`
+ `AV1_LEVEL_2_1`
+ `AV1_LEVEL_3`
+ `AV1_LEVEL_3_1`
+ `AV1_LEVEL_4`
+ `AV1_LEVEL_4_1`
+ `AV1_LEVEL_5`
+ `AV1_LEVEL_5_1`
+ `AV1_LEVEL_5_2`
+ `AV1_LEVEL_5_3`
+ `AV1_LEVEL_6`
+ `AV1_LEVEL_6_1`
+ `AV1_LEVEL_6_2`
+ `AV1_LEVEL_6_3`
+ `AV1_LEVEL_AUTO`

### Av1LookAheadRateControl
<a name="channels-model-av1lookaheadratecontrol"></a>

Av1 Look Ahead Rate Control
+ `HIGH`
+ `LOW`
+ `MEDIUM`

### Av1RateControlMode
<a name="channels-model-av1ratecontrolmode"></a>

Av1 Rate Control Mode
+ `CBR`
+ `QVBR`

### Av1SceneChangeDetect
<a name="channels-model-av1scenechangedetect"></a>

Av1 Scene Change Detect
+ `DISABLED`
+ `ENABLED`

### Av1Settings
<a name="channels-model-av1settings"></a>

Av1 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| afdSignaling | [AfdSignaling](#channels-model-afdsignaling) | False | Configures whether MediaLive will write AFD values into the video. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: the AFD value will be the value configured in the fixedAfd parameter. NONE: MediaLive won't write AFD into the video |
| bitDepth | [Av1BitDepth](#channels-model-av1bitdepth) | False | Specifies the bit depth for the output encode. Choose a value. Or leave the field empty to use the default, which is 8 bit. |
| bitrate | integer<br />Minimum: 50000<br />Maximum: 12000000 | False | Average bitrate in bits/second. Required when the rate control mode is CBR. Not used for QVBR. |
| bufSize | integer<br />Minimum: 50000<br />Maximum: 24000000 | False | The size of the buffer (HRD buffer model) in bits. |
| colorSpaceSettings | [Av1ColorSpaceSettings](#channels-model-av1colorspacesettings) | False | Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source. |
| fixedAfd | [FixedAfd](#channels-model-fixedafd) | False | Complete this property only if you set the afdSignaling property to FIXED. Choose the AFD value (4 bits) to write on all frames of the video encode. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 3003 | True | The denominator for the framerate. Framerate is a fraction, for example, 24000 / 1001. |
| framerateNumerator | integer<br />Minimum: 1 | True | The numerator for the framerate. Framerate is a fraction, for example, 24000 / 1001. |
| gopSize | number<br />Minimum: 0 | False | The GOP size (keyframe interval). If GopSizeUnits is frames, GopSize must be a whole number and must be greater than or equal to 1. If GopSizeUnits is seconds, GopSize must be greater than 0, but it can be a decimal. |
| gopSizeUnits | [Av1GopSizeUnits](#channels-model-av1gopsizeunits) | False | Choose the units for the GOP size: FRAMES or SECONDS. For SECONDS, MediaLive converts the size into a frame count at run time. |
| level | [Av1Level](#channels-model-av1level) | False | Sets the level. This parameter is one of the properties of the encoding scheme for AV1. |
| lookAheadRateControl | [Av1LookAheadRateControl](#channels-model-av1lookaheadratecontrol) | False | Sets the amount of lookahead. A value of LOW can decrease latency and memory usage. A value of HIGH can produce better quality for certain content. |
| maxBitrate | integer<br />Minimum: 50000<br />Maximum: 12000000 | False | The maximum bitrate to assign. For recommendations, see the description for qvbrQualityLevel. |
| minBitrate | integer<br />Minimum: 0<br />Maximum: 8000000 | False | Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Applies only if you enable SceneChangeDetect. Sets the interval between frames. This property ensures a minimum separation between repeated (cadence) I-frames and any I-frames inserted by scene change detection (SCD frames). Enter a number for the interval, measured in number of frames. If an SCD frame and a cadence frame are closer than the specified number of frames, MediaLive shrinks or stretches the GOP to include the SCD frame. Then normal cadence resumes in the next GOP. For GOP stretch to succeed, you must enable LookAheadRateControl. Note that the maximum GOP stretch = (GOP size) \+ (Minimum I-interval) - 1 |
| parDenominator | integer<br />Minimum: 1 | False | The denominator for the output pixel aspect ratio (PAR). |
| parNumerator | integer<br />Minimum: 1 | False | The numerator for the output pixel aspect ratio (PAR). |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Controls the target quality for the video encode. With QVBR rate control mode, the final quality is the target quality, constrained by the maxBitrate. Set values for the qvbrQualityLevel property and maxBitrate property that suit your most important viewing devices. To let MediaLive set the quality level (AUTO mode), leave the qvbrQualityLevel field empty. In this case, MediaLive uses the maximum bitrate, and the quality follows from that: more complex content might have a lower quality. Or set a target quality level and a maximum bitrate. With more complex content, MediaLive will try to achieve the target quality, but it won't exceed the maximum bitrate. With less complex content, This option will use only the bitrate needed to reach the target quality. Recommended values are: Primary screen: qvbrQualityLevel: Leave empty. maxBitrate: 4,000,000 PC or tablet: qvbrQualityLevel: Leave empty. maxBitrate: 1,500,000 to 3,000,000 Smartphone: qvbrQualityLevel: Leave empty. maxBitrate: 1,000,000 to 1,500,000 |
| rateControlMode | [Av1RateControlMode](#channels-model-av1ratecontrolmode) | False | Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. |
| sceneChangeDetect | [Av1SceneChangeDetect](#channels-model-av1scenechangedetect) | False | Controls whether MediaLive inserts I-frames when it detects a scene change. ENABLED or DISABLED. |
| spatialAq | [Av1SpatialAq](#channels-model-av1spatialaq) | False | Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. Enabled: MediaLive will determine the appropriate level of spatial AQ to apply. Disabled: No spatial AQ. For more information, see the topic about video adaptive quantization in the MediaLive user guide. |
| temporalAq | [Av1TemporalAq](#channels-model-av1temporalaq) | False | Temporal AQ makes adjustments within each frame based on variations in content complexity over time. Enabled: MediaLive will determine the appropriate level of temporal AQ to apply. Disabled: No temporal AQ. For more information, see the topic about video adaptive quantization in the MediaLive user guide. |
| timecodeBurninSettings | [TimecodeBurninSettings](#channels-model-timecodeburninsettings) | False | Configures the timecode burn-in feature. If you enable this feature, the timecode will become part of the video. |
| timecodeInsertion | [Av1TimecodeInsertionBehavior](#channels-model-av1timecodeinsertionbehavior) | False | Controls how MediaLive inserts timecodes into the video output encode. DISABLED: Do not insert timecodes. METADATA\_OBU: Include timecodes. MediaLive inserts timecode metadata based on the timecode from the source specified in the Timecode Config property. The timecode metadata is a metadata OBU (Open Bitstream Unit) of type METADATA\_TYPE\_TIMECODE, in accordance with https://aomediacodec.github.io/av1-spec/\#metadata-timecode-syntax. |

### Av1SpatialAq
<a name="channels-model-av1spatialaq"></a>

Av1 Spatial Aq
+ `DISABLED`
+ `ENABLED`

### Av1TemporalAq
<a name="channels-model-av1temporalaq"></a>

Av1 Temporal Aq
+ `DISABLED`
+ `ENABLED`

### Av1TimecodeInsertionBehavior
<a name="channels-model-av1timecodeinsertionbehavior"></a>

Av1 Timecode Insertion Behavior
+ `DISABLED`
+ `METADATA_OBU`

### AvailBlanking
<a name="channels-model-availblanking"></a>

Avail Blanking

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availBlankingImage | [InputLocation](#channels-model-inputlocation) | False | Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported. |
| state | [AvailBlankingState](#channels-model-availblankingstate) | False | When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added. |

### AvailBlankingState
<a name="channels-model-availblankingstate"></a>

Avail Blanking State
+ `DISABLED`
+ `ENABLED`

### AvailConfiguration
<a name="channels-model-availconfiguration"></a>

Avail Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availSettings | [AvailSettings](#channels-model-availsettings) | False | Ad avail settings. |
| scte35SegmentationScope | [Scte35SegmentationScope](#channels-model-scte35segmentationscope) | False | Configures whether SCTE 35 passthrough triggers segment breaks in all output groups that use segmented outputs. Insertion of a SCTE 35 message typically results in a segment break, in addition to the regular cadence of breaks. The segment breaks appear in video outputs, audio outputs, and captions outputs (if any). ALL\_OUTPUT\_GROUPS: Default. Insert the segment break in all output groups that have segmented outputs. This is the legacy behavior. SCTE35\_ENABLED\_OUTPUT\_GROUPS: Insert the segment break only in output groups that have SCTE 35 passthrough enabled. This is the recommended value, because it reduces unnecessary segment breaks. |

### AvailSettings
<a name="channels-model-availsettings"></a>

Avail Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| esam | [Esam](#channels-model-esam) | False |  |
| scte35SpliceInsert | [Scte35SpliceInsert](#channels-model-scte35spliceinsert) | False |  |
| scte35TimeSignalApos | [Scte35TimeSignalApos](#channels-model-scte35timesignalapos) | False |  |

### BadGatewayException
<a name="channels-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BandwidthReductionFilterSettings
<a name="channels-model-bandwidthreductionfiltersettings"></a>

Bandwidth Reduction Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| postFilterSharpening | [BandwidthReductionPostFilterSharpening](#channels-model-bandwidthreductionpostfiltersharpening) | False | Configures the sharpening control, which is available when the bandwidth reduction filter is enabled. This control sharpens edges and contours, which produces a specific artistic effect that you might want. We recommend that you test each of the values (including DISABLED) to observe the sharpening effect on the content. |
| strength | [BandwidthReductionFilterStrength](#channels-model-bandwidthreductionfilterstrength) | False | Enables the bandwidth reduction filter. The filter strengths range from 1 to 4. We recommend that you always enable this filter and use AUTO, to let MediaLive apply the optimum filtering for the context. |

### BandwidthReductionFilterStrength
<a name="channels-model-bandwidthreductionfilterstrength"></a>

Bandwidth Reduction Filter Strength
+ `AUTO`
+ `STRENGTH_1`
+ `STRENGTH_2`
+ `STRENGTH_3`
+ `STRENGTH_4`

### BandwidthReductionPostFilterSharpening
<a name="channels-model-bandwidthreductionpostfiltersharpening"></a>

Bandwidth Reduction Post Filter Sharpening
+ `DISABLED`
+ `SHARPENING_1`
+ `SHARPENING_2`
+ `SHARPENING_3`

### BlackoutSlate
<a name="channels-model-blackoutslate"></a>

Blackout Slate

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackoutSlateImage | [InputLocation](#channels-model-inputlocation) | False | Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported. |
| networkEndBlackout | [BlackoutSlateNetworkEndBlackout](#channels-model-blackoutslatenetworkendblackout) | False | Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the "Network Blackout Image" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in "Network ID". |
| networkEndBlackoutImage | [InputLocation](#channels-model-inputlocation) | False | Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster. |
| networkId | string<br />MinLength: 34<br />MaxLength: 34 | False | Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C"). |
| state | [BlackoutSlateState](#channels-model-blackoutslatestate) | False | When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata. |

### BlackoutSlateNetworkEndBlackout
<a name="channels-model-blackoutslatenetworkendblackout"></a>

Blackout Slate Network End Blackout
+ `DISABLED`
+ `ENABLED`

### BlackoutSlateState
<a name="channels-model-blackoutslatestate"></a>

Blackout Slate State
+ `DISABLED`
+ `ENABLED`

### BurnInAlignment
<a name="channels-model-burninalignment"></a>

Burn In Alignment
+ `CENTERED`
+ `LEFT`
+ `SMART`

### BurnInBackgroundColor
<a name="channels-model-burninbackgroundcolor"></a>

Burn In Background Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### BurnInDestinationSettings
<a name="channels-model-burnindestinationsettings"></a>

Burn In Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [BurnInAlignment](#channels-model-burninalignment) | False | If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match. |
| backgroundColor | [BurnInBackgroundColor](#channels-model-burninbackgroundcolor) | False | Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| font | [InputLocation](#channels-model-inputlocation) | False | External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match. |
| fontColor | [BurnInFontColor](#channels-model-burninfontcolor) | False | Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match. |
| fontSize | string | False | When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match. |
| outlineColor | [BurnInOutlineColor](#channels-model-burninoutlinecolor) | False | Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| shadowColor | [BurnInShadowColor](#channels-model-burninshadowcolor) | False | Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| shadowXOffset | integer | False | Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match. |
| shadowYOffset | integer | False | Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match. |
| subtitleRows | [BurnInDestinationSubtitleRows](#channels-model-burnindestinationsubtitlerows) | False | Applies only when the input captions are Teletext and the output captions are DVB-Sub or Burn-In. Choose the number of lines for the captions bitmap. The captions bitmap is 700 wide × 576 high and will be laid over the video. For example, a value of 16 divides the bitmap into 16 lines, with each line 36 pixels high (16 × 36 = 576). The default is 24 (24 pixels high). Enter the same number in every encode in every output that converts the same Teletext source to DVB-Sub or Burn-in. |
| teletextGridControl | [BurnInTeletextGridControl](#channels-model-burninteletextgridcontrol) | False | Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs. |
| xPosition | integer<br />Minimum: 0 | False | Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match. |
| yPosition | integer<br />Minimum: 0 | False | Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match. |

### BurnInDestinationSubtitleRows
<a name="channels-model-burnindestinationsubtitlerows"></a>

Burn In Destination Subtitle Rows
+ `ROWS_16`
+ `ROWS_20`
+ `ROWS_24`

### BurnInFontColor
<a name="channels-model-burninfontcolor"></a>

Burn In Font Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### BurnInOutlineColor
<a name="channels-model-burninoutlinecolor"></a>

Burn In Outline Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### BurnInShadowColor
<a name="channels-model-burninshadowcolor"></a>

Burn In Shadow Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### BurnInTeletextGridControl
<a name="channels-model-burninteletextgridcontrol"></a>

Burn In Teletext Grid Control
+ `FIXED`
+ `SCALED`

### CaptionDescription
<a name="channels-model-captiondescription"></a>

Caption Description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibility | [AccessibilityType](#channels-model-accessibilitytype) | False | Indicates whether the caption track implements accessibility features such as written descriptions of spoken dialog, music, and sounds. |
| captionDashRoles | Array of type [DashRoleCaption](#channels-model-dashrolecaption) | False | Identifies the DASH roles to assign to this captions output. Applies only when the captions output is configured for DVB DASH accessibility signaling. |
| captionSelectorName | string | True | Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name. |
| destinationSettings | [CaptionDestinationSettings](#channels-model-captiondestinationsettings) | False | Additional settings for captions destination that depend on the destination type. |
| dvbDashAccessibility | [DvbDashAccessibility](#channels-model-dvbdashaccessibility) | False | Identifies DVB DASH accessibility signaling in this captions output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers. |
| languageCode | string | False | ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/ |
| languageDescription | string | False | Human readable information to indicate captions available for players (eg. English, or Spanish). |
| name | string | True | Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event. |

### CaptionDestinationSettings
<a name="channels-model-captiondestinationsettings"></a>

Caption Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aribDestinationSettings | [AribDestinationSettings](#channels-model-aribdestinationsettings) | False |  |
| burnInDestinationSettings | [BurnInDestinationSettings](#channels-model-burnindestinationsettings) | False |  |
| dvbSubDestinationSettings | [DvbSubDestinationSettings](#channels-model-dvbsubdestinationsettings) | False |  |
| ebuTtDDestinationSettings | [EbuTtDDestinationSettings](#channels-model-ebuttddestinationsettings) | False |  |
| embeddedDestinationSettings | [EmbeddedDestinationSettings](#channels-model-embeddeddestinationsettings) | False |  |
| embeddedPlusScte20DestinationSettings | [EmbeddedPlusScte20DestinationSettings](#channels-model-embeddedplusscte20destinationsettings) | False |  |
| rtmpCaptionInfoDestinationSettings | [RtmpCaptionInfoDestinationSettings](#channels-model-rtmpcaptioninfodestinationsettings) | False |  |
| scte20PlusEmbeddedDestinationSettings | [Scte20PlusEmbeddedDestinationSettings](#channels-model-scte20plusembeddeddestinationsettings) | False |  |
| scte27DestinationSettings | [Scte27DestinationSettings](#channels-model-scte27destinationsettings) | False |  |
| smpteTtDestinationSettings | [SmpteTtDestinationSettings](#channels-model-smptettdestinationsettings) | False |  |
| teletextDestinationSettings | [TeletextDestinationSettings](#channels-model-teletextdestinationsettings) | False |  |
| ttmlDestinationSettings | [TtmlDestinationSettings](#channels-model-ttmldestinationsettings) | False |  |
| webvttDestinationSettings | [WebvttDestinationSettings](#channels-model-webvttdestinationsettings) | False |  |

### CaptionLanguageMapping
<a name="channels-model-captionlanguagemapping"></a>

Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionChannel | integer<br />Minimum: 1<br />Maximum: 4 | True | The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4) |
| languageCode | string<br />MinLength: 3<br />MaxLength: 3 | True | Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2) |
| languageDescription | string<br />MinLength: 1 | True | Textual description of language |

### CaptionRectangle
<a name="channels-model-captionrectangle"></a>

Caption Rectangle

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For height, specify the entire height of the rectangle as a percentage of the underlying frame height. For example, \\"80\\" means the rectangle height is 80% of the underlying frame height. The topOffset and rectangleHeight must add up to 100% or less. This field corresponds to tts:extent - Y in the TTML standard. |
| leftOffset | number<br />Minimum: 0<br />Maximum: 100 | True | Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. (Make sure to leave the default if you don't have either of these formats in the output.) You can define a display rectangle for the captions that is smaller than the underlying video frame. You define the rectangle by specifying the position of the left edge, top edge, bottom edge, and right edge of the rectangle, all within the underlying video frame. The units for the measurements are percentages. If you specify a value for one of these fields, you must specify a value for all of them. For leftOffset, specify the position of the left edge of the rectangle, as a percentage of the underlying frame width, and relative to the left edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame width. The rectangle left edge starts at that position from the left edge of the frame. This field corresponds to tts:origin - X in the TTML standard. |
| topOffset | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For topOffset, specify the position of the top edge of the rectangle, as a percentage of the underlying frame height, and relative to the top edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame height. The rectangle top edge starts at that position from the top edge of the frame. This field corresponds to tts:origin - Y in the TTML standard. |
| width | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For width, specify the entire width of the rectangle as a percentage of the underlying frame width. For example, \\"80\\" means the rectangle width is 80% of the underlying frame width. The leftOffset and rectangleWidth must add up to 100% or less. This field corresponds to tts:extent - X in the TTML standard. |

### CaptionSelector
<a name="channels-model-captionselector"></a>

Output groups for this Live Event. Output groups contain information about where streams should be distributed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | False | When specified this field indicates the three letter language code of the caption track to extract from the source. |
| name | string<br />MinLength: 1 | True | Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event. |
| selectorSettings | [CaptionSelectorSettings](#channels-model-captionselectorsettings) | False | Caption selector settings. |

### CaptionSelectorSettings
<a name="channels-model-captionselectorsettings"></a>

Caption Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ancillarySourceSettings | [AncillarySourceSettings](#channels-model-ancillarysourcesettings) | False |  |
| aribSourceSettings | [AribSourceSettings](#channels-model-aribsourcesettings) | False |  |
| dvbSubSourceSettings | [DvbSubSourceSettings](#channels-model-dvbsubsourcesettings) | False |  |
| embeddedSourceSettings | [EmbeddedSourceSettings](#channels-model-embeddedsourcesettings) | False |  |
| scte20SourceSettings | [Scte20SourceSettings](#channels-model-scte20sourcesettings) | False |  |
| scte27SourceSettings | [Scte27SourceSettings](#channels-model-scte27sourcesettings) | False |  |
| smartSubtitleSourceSettings | [SmartSubtitleSourceSettings](#channels-model-smartsubtitlesourcesettings) | False | Settings for a caption selector that uses subtitles that AWS Elemental Inference generates from the channel audio (Smart Subtitles). The channel must include `InferenceSettings` that associate the channel with an Elemental Inference feed. |
| teletextSourceSettings | [TeletextSourceSettings](#channels-model-teletextsourcesettings) | False |  |

### CaptionSynchronizationMode
<a name="channels-model-captionsynchronizationmode"></a>

Controls how MediaLive synchronizes subtitles that AWS Elemental Inference generates with the video output. Valid values:
+ `VIDEO_ALIGNED_CAPTIONS` – MediaLive delays the video so that the captions appear at the same time as the speech they transcribe. This is the default.
+ `NO_VIDEO_DELAY` – MediaLive doesn't delay the video. It inserts the captions into the video as they become available from Elemental Inference, so captions appear later than the speech they transcribe.
+ `NO_VIDEO_DELAY`
+ `VIDEO_ALIGNED_CAPTIONS`

### CdiInputResolution
<a name="channels-model-cdiinputresolution"></a>

Maximum CDI input resolution; SD is 480i and 576i up to 30 frames-per-second (fps), HD is 720p up to 60 fps / 1080i up to 30 fps, FHD is 1080p up to 60 fps, UHD is 2160p up to 60 fps
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### CdiInputSpecification
<a name="channels-model-cdiinputspecification"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resolution | [CdiInputResolution](#channels-model-cdiinputresolution) | False | Maximum CDI input resolution |

### Channel
<a name="channels-model-channel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the channel. |
| cdiInputSpecification | [CdiInputSpecification](#channels-model-cdiinputspecification) | False | Specification of CDI inputs for this channel |
| channelClass | [ChannelClass](#channels-model-channelclass) | False | The class for this channel. STANDARD for a channel with two pipelines or SINGLE\_PIPELINE for a channel with one pipeline. |
| destinations | Array of type [OutputDestination](#channels-model-outputdestination) | False | A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.  |
| egressEndpoints | Array of type [ChannelEgressEndpoint](#channels-model-channelegressendpoint) | False | The endpoints where outgoing connections initiate from |
| encoderSettings | [EncoderSettings](#channels-model-encodersettings) | False |  |
| id | string | False | The unique ID of the channel. |
| inferenceSettings | [DescribeInferenceSettings](#channels-model-describeinferencesettings) | False | Contains the Elemental Inference configuration for a channel, as returned by DescribeChannel and related describe operations. |
| inputAttachments | Array of type [InputAttachment](#channels-model-inputattachment) | False | List of input attachments for channel. |
| inputSpecification | [InputSpecification](#channels-model-inputspecification) | False | Specification of network and file inputs for this channel |
| logLevel | [LogLevel](#channels-model-loglevel) | False | The log level being written to CloudWatch Logs. |
| maintenance | [MaintenanceStatus](#channels-model-maintenancestatus) | False | Maintenance settings for this channel. |
| name | string | False | The name of the channel. (user-mutable) |
| pipelineDetails | Array of type [PipelineDetail](#channels-model-pipelinedetail) | False | Runtime details for the pipelines of a running channel. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role assumed when running the Channel. |
| state | [ChannelState](#channels-model-channelstate) | False |  |
| tags | [Tags](#channels-model-tags) | False | A collection of key-value pairs. |
| vpc | [VpcOutputSettingsDescription](#channels-model-vpcoutputsettingsdescription) | False | Settings for VPC output |

### ChannelClass
<a name="channels-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### ChannelConfigurationValidationError
<a name="channels-model-channelconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |
| validationErrors | Array of type [ValidationError](#channels-model-validationerror) | False | A collection of validation error responses. |

### ChannelEgressEndpoint
<a name="channels-model-channelegressendpoint"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceIp | string | False | Public IP of where a channel's output comes from |

### ChannelEngineVersionRequest
<a name="channels-model-channelengineversionrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| version | string | False | The build identifier of the engine version to use for this channel. Specify 'DEFAULT' to reset to the default version. |

### ChannelState
<a name="channels-model-channelstate"></a>
+ `CREATING`
+ `CREATE_FAILED`
+ `IDLE`
+ `STARTING`
+ `RUNNING`
+ `RECOVERING`
+ `STOPPING`
+ `DELETING`
+ `DELETED`
+ `UPDATING`
+ `UPDATE_FAILED`

### ChannelSummary
<a name="channels-model-channelsummary"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the channel. |
| cdiInputSpecification | [CdiInputSpecification](#channels-model-cdiinputspecification) | False | Specification of CDI inputs for this channel |
| channelClass | [ChannelClass](#channels-model-channelclass) | False | The class for this channel. STANDARD for a channel with two pipelines or SINGLE\_PIPELINE for a channel with one pipeline. |
| destinations | Array of type [OutputDestination](#channels-model-outputdestination) | False | A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.  |
| egressEndpoints | Array of type [ChannelEgressEndpoint](#channels-model-channelegressendpoint) | False | The endpoints where outgoing connections initiate from |
| id | string | False | The unique id of the channel. |
| inputAttachments | Array of type [InputAttachment](#channels-model-inputattachment) | False | List of input attachments for channel. |
| inputSpecification | [InputSpecification](#channels-model-inputspecification) | False | Specification of network and file inputs for this channel |
| logLevel | [LogLevel](#channels-model-loglevel) | False | The log level being written to CloudWatch Logs. |
| maintenance | [MaintenanceStatus](#channels-model-maintenancestatus) | False | Maintenance settings for this channel. |
| name | string | False | The name of the channel. (user-mutable) |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role assumed when running the Channel. |
| state | [ChannelState](#channels-model-channelstate) | False |  |
| tags | [Tags](#channels-model-tags) | False | A collection of key-value pairs. |
| vpc | [VpcOutputSettingsDescription](#channels-model-vpcoutputsettingsdescription) | False | Settings for any VPC outputs. |

### CmafId3Behavior
<a name="channels-model-cmafid3behavior"></a>

Cmaf Id3 Behavior
+ `DISABLED`
+ `ENABLED`

### CmafIngestAbWatermarkerIrdetoSettings
<a name="channels-model-cmafingestabwatermarkerirdetosettings"></a>

A/B Watermarker settings for CMAF Ingest output groups.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalDestinationsAlternateDestinations | Array of type [OutputLocationRef](#channels-model-outputlocationref) | False | The "B" pipeline renditions for the additional destinations. |
| alternateDestination | [OutputLocationRef](#channels-model-outputlocationref) | True | The "B" pipeline renditions for the main destination. |
| customProfile | [AbWatermarkingCustomProfile](#channels-model-abwatermarkingcustomprofile) | False | The vendor-provided custom profile values. |
| license | string | False | The name of the Secrets Manager secret containing the license file. |
| operatorId | integer<br />Minimum: 1<br />Maximum: 511 | True | The vendor-provided Operator ID. |
| polyPeriod | integer<br />Minimum: 1<br />Maximum: 1000 | False | The number of segments per watermarking bit. The total duration of the watermarking bit should be the LCM (least common multiple) of all segments sizes emitted by the downstream packager. |
| profile | [AbWatermarkingProfile](#channels-model-abwatermarkingprofile) | True | The vendor-provided profile choice. |
| watermarkIdLength | [AbWatermarkerIdLength](#channels-model-abwatermarkeridlength) | False | The number of bits that compose the watermarking identifier to be embedded. |

### CmafIngestCaptionLanguageMapping
<a name="channels-model-cmafingestcaptionlanguagemapping"></a>

Add an array item for each language. Follow the order of the caption descriptions. For example, if the first caption description is for German, then the first array item must be for German, and its caption channel must be set to 1. The second array item must be 2, and so on.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionChannel | integer<br />Minimum: 1<br />Maximum: 4 | True | A number for the channel for this caption, 1 to 4. |
| languageCode | string<br />MinLength: 3<br />MaxLength: 3 | True | Language code for the language of the caption in this channel. For example, ger/deu. See http://www.loc.gov/standards/iso639-2 |

### CmafIngestGroupSettings
<a name="channels-model-cmafingestgroupsettings"></a>

Contains the settings for a Common Media Application Format (CMAF) Ingest output group, including SCTE-35 insertion behavior.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalDestinations | Array of type [AdditionalDestinations](#channels-model-additionaldestinations) | False | Optional an array of additional destinational HTTP destinations for the OutputGroup outputs |
| captionLanguageMappings | Array of type [CmafIngestCaptionLanguageMapping](#channels-model-cmafingestcaptionlanguagemapping) | False | An array that identifies the languages in the four caption channels in the embedded captions. |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | A HTTP destination for the tracks |
| id3Behavior | [CmafId3Behavior](#channels-model-cmafid3behavior) | False | Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule. |
| id3NameModifier | string<br />MaxLength: 100 | False | Change the modifier that MediaLive automatically adds to the Streams() name that identifies an ID3 track. The default is "id3", which means the default name will be Streams(id3.cmfm). Any string you enter here will replace the "id3" string. The modifier can only contain: numbers, letters, plus (\+), minus (-), underscore (\_) and period (.) and has a maximum length of 100 characters. |
| klvBehavior | [CmafKLVBehavior](#channels-model-cmafklvbehavior) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| klvNameModifier | string<br />MaxLength: 100 | False | Change the modifier that MediaLive automatically adds to the Streams() name that identifies a KLV track. The default is "klv", which means the default name will be Streams(klv.cmfm). Any string you enter here will replace the "klv" string. The modifier can only contain: numbers, letters, plus (\+), minus (-), underscore (\_) and period (.) and has a maximum length of 100 characters. |
| nielsenId3Behavior | [CmafNielsenId3Behavior](#channels-model-cmafnielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| nielsenId3NameModifier | string<br />MaxLength: 100 | False | Change the modifier that MediaLive automatically adds to the Streams() name that identifies a Nielsen ID3 track. The default is "nid3", which means the default name will be Streams(nid3.cmfm). Any string you enter here will replace the "nid3" string. The modifier can only contain: numbers, letters, plus (\+), minus (-), underscore (\_) and period (.) and has a maximum length of 100 characters. |
| scte35NameModifier | string<br />MaxLength: 100 | False | Change the modifier that MediaLive automatically adds to the Streams() name for a SCTE 35 track. The default is "scte", which means the default name will be Streams(scte.cmfm). Any string you enter here will replace the "scte" string. The modifier can only contain: numbers, letters, plus (\+), minus (-), underscore (\_) and period (.) and has a maximum length of 100 characters. |
| scte35Type | [Scte35Type](#channels-model-scte35type) | False | The SCTE-35 insertion behavior for this CMAF Ingest output group. Valid values:+ `NONE` – The channel does not insert SCTE-35 messages.<br />+ `SCTE_35_WITHOUT_IDR` – The channel inserts SCTE-35 messages without an Instantaneous Decoder Refresh (IDR) frame at the cue point.<br />+ `SCTE_35_WITHOUT_SEGMENTATION` – The channel inserts SCTE-35 messages with an IDR frame, but without a new segment boundary.<br />If you don't specify a value, the channel doesn't insert SCTE-35 messages (`NONE`). |
| segmentLength | integer<br />Minimum: 1 | False | The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units. |
| segmentLengthUnits | [CmafIngestSegmentLengthUnits](#channels-model-cmafingestsegmentlengthunits) | False | Time unit for segment length parameter. |
| sendDelayMs | integer<br />Minimum: 0<br />Maximum: 2000 | False | Number of milliseconds to delay the output from the second pipeline. |
| timedMetadataId3Frame | [CmafTimedMetadataId3Frame](#channels-model-cmaftimedmetadataid3frame) | False | Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0<br />Maximum: 10000 | False | If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds. |
| timedMetadataPassthrough | [CmafTimedMetadataPassthrough](#channels-model-cmaftimedmetadatapassthrough) | False | Set to enabled to pass through ID3 metadata from the input sources. |
| watermarkingSettings | [CmafIngestWatermarkingSettings](#channels-model-cmafingestwatermarkingsettings) | False | Specifies the type of watermarking technology to use. |

### CmafIngestOutputSettings
<a name="channels-model-cmafingestoutputsettings"></a>

Cmaf Ingest Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nameModifier | string | False | String concatenated to the end of the destination filename. Required for multiple outputs of the same type. |

### CmafIngestSegmentLengthUnits
<a name="channels-model-cmafingestsegmentlengthunits"></a>

Cmaf Ingest Segment Length Units
+ `MILLISECONDS`
+ `SECONDS`

### CmafIngestWatermarkingSettings
<a name="channels-model-cmafingestwatermarkingsettings"></a>

A/B Watermarker settings for CMAF Ingest output groups.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cmafIngestAbWatermarkerIrdetoSettings | [CmafIngestAbWatermarkerIrdetoSettings](#channels-model-cmafingestabwatermarkerirdetosettings) | False |  |

### CmafKLVBehavior
<a name="channels-model-cmafklvbehavior"></a>

Cmaf KLVBehavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### CmafNielsenId3Behavior
<a name="channels-model-cmafnielsenid3behavior"></a>

Cmaf Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### CmafTimedMetadataId3Frame
<a name="channels-model-cmaftimedmetadataid3frame"></a>

Cmaf Timed Metadata Id3 Frame
+ `NONE`
+ `PRIV`
+ `TDRL`

### CmafTimedMetadataPassthrough
<a name="channels-model-cmaftimedmetadatapassthrough"></a>

Cmaf Timed Metadata Passthrough
+ `DISABLED`
+ `ENABLED`

### ColorCorrection
<a name="channels-model-colorcorrection"></a>

Property of ColorCorrectionSettings. Used for custom color space conversion. The object identifies one 3D LUT file and specifies the input/output color space combination that the file will be used for.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputColorSpace | [ColorSpace](#channels-model-colorspace) | True | The color space of the input. |
| outputColorSpace | [ColorSpace](#channels-model-colorspace) | True | The color space of the output. |
| uri | string | True | The URI of the 3D LUT file. The protocol must be 's3:' or 's3ssl:':. |

### ColorCorrectionSettings
<a name="channels-model-colorcorrectionsettings"></a>

Property of encoderSettings. Controls color conversion when you are using 3D LUT files to perform color conversion on video.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| globalColorCorrections | Array of type [ColorCorrection](#channels-model-colorcorrection) | True | An array of colorCorrections that applies when you are using 3D LUT files to perform color conversion on video. Each colorCorrection contains one 3D LUT file (that defines the color mapping for converting an input color space to an output color space), and the input/output combination that this 3D LUT file applies to. MediaLive reads the color space in the input metadata, determines the color space that you have specified for the output, and finds and uses the LUT file that applies to this combination. |

### ColorSpace
<a name="channels-model-colorspace"></a>

Property of colorCorrections. When you are using 3D LUT files to perform color conversion on video, these are the supported color spaces.
+ `HDR10`
+ `HLG_2020`
+ `REC_601`
+ `REC_709`

### ColorSpacePassthroughSettings
<a name="channels-model-colorspacepassthroughsettings"></a>

Passthrough applies no color space conversion to the output

### ConnectionMode
<a name="channels-model-connectionmode"></a>
+ `CALLER`
+ `LISTENER`

### CreateChannel
<a name="channels-model-createchannel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anywhereSettings | [AnywhereSettings](#channels-model-anywheresettings) | False | The Elemental Anywhere settings for this channel. |
| cdiInputSpecification | [CdiInputSpecification](#channels-model-cdiinputspecification) | False | Specification of CDI inputs for this channel |
| channelClass | [ChannelClass](#channels-model-channelclass) | False | The class for this channel. STANDARD for a channel with two pipelines or SINGLE\_PIPELINE for a channel with one pipeline. |
| channelEngineVersion | [ChannelEngineVersionRequest](#channels-model-channelengineversionrequest) | False | The desired engine version for this channel. |
| channelSecurityGroups | Array of type string | False | A list of IDs for all the Input Security Groups attached to the channel. |
| destinations | Array of type [OutputDestination](#channels-model-outputdestination) | False |  |
| dryRun | boolean | False |  |
| encoderSettings | [EncoderSettings](#channels-model-encodersettings) | False |  |
| inferenceSettings | [InferenceSettings](#channels-model-inferencesettings) | False | Contains the Elemental Inference settings for a channel, including the feed Amazon Resource Name (ARN) and the enrichment methods that augment channel output with contextual metadata. |
| inputAttachments | Array of type [InputAttachment](#channels-model-inputattachment) | False | List of input attachments for channel. |
| inputSpecification | [InputSpecification](#channels-model-inputspecification) | False | Specification of network and file inputs for this channel |
| linkedChannelSettings | [LinkedChannelSettings](#channels-model-linkedchannelsettings) | False | The linked channel settings for the channel. |
| logLevel | [LogLevel](#channels-model-loglevel) | False | The log level to write to CloudWatch Logs. |
| maintenance | [MaintenanceCreateSettings](#channels-model-maintenancecreatesettings) | False | Maintenance settings for this channel. |
| name | string | False | Name of channel. |
| requestId | string | False | Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.  |
| reserved | string | False | Deprecated field that's only usable by whitelisted customers. |
| roleArn | string | False | An optional Amazon Resource Name (ARN) of the role to assume when running the Channel. |
| tags | [Tags](#channels-model-tags) | False | A collection of key-value pairs. |
| vpc | [VpcOutputSettings](#channels-model-vpcoutputsettings) | False | Settings for the VPC outputs |

### CreateChannelResultModel
<a name="channels-model-createchannelresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channel | [Channel](#channels-model-channel) | False |  |

### DashRoleAudio
<a name="channels-model-dashroleaudio"></a>

Dash Role Audio
+ `ALTERNATE`
+ `COMMENTARY`
+ `DESCRIPTION`
+ `DUB`
+ `EMERGENCY`
+ `ENHANCED-AUDIO-INTELLIGIBILITY`
+ `KARAOKE`
+ `MAIN`
+ `SUPPLEMENTARY`

### DashRoleCaption
<a name="channels-model-dashrolecaption"></a>

Dash Role Caption
+ `ALTERNATE`
+ `CAPTION`
+ `COMMENTARY`
+ `DESCRIPTION`
+ `DUB`
+ `EASYREADER`
+ `EMERGENCY`
+ `FORCED-SUBTITLE`
+ `KARAOKE`
+ `MAIN`
+ `METADATA`
+ `SUBTITLE`
+ `SUPPLEMENTARY`

### DescribeInferenceSettings
<a name="channels-model-describeinferencesettings"></a>

Contains the Elemental Inference configuration for a channel, as returned by DescribeChannel and related describe operations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioFeedInputs | Array of type [AudioFeedInput](#channels-model-audiofeedinput) | False | A list of audio feed inputs that map audio selectors in the channel to feed inputs on the associated AWS Elemental Inference feed. |
| enrichmentMethods | Array of type [EnrichmentMethod](#channels-model-enrichmentmethod) | False | The Contextual Metadata Enrichment methods enabled for this channel. Each method defines how the channel augments its output with contextual metadata from the Elemental Inference feed. Valid values:+ `SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS` – Enriches outbound SCTE-35 messages with query parameters that downstream systems can use to call the Elemental Inference GetMetadata API. |
| feedArn | string | False | The Amazon Resource Name (ARN) of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service. |

### DisabledLockingSettings
<a name="channels-model-disabledlockingsettings"></a>

Disabled Locking Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customEpoch | string | False | Optional. Only applies to CMAF Ingest Output Group and MediaPackage V2 Output Group. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00. |

### DolbyEProgramSelection
<a name="channels-model-dolbyeprogramselection"></a>

Dolby EProgram Selection
+ `ALL_CHANNELS`
+ `PROGRAM_1`
+ `PROGRAM_2`
+ `PROGRAM_3`
+ `PROGRAM_4`
+ `PROGRAM_5`
+ `PROGRAM_6`
+ `PROGRAM_7`
+ `PROGRAM_8`

### DolbyVision81Settings
<a name="channels-model-dolbyvision81settings"></a>

Dolby Vision81 Settings

### DvbDashAccessibility
<a name="channels-model-dvbdashaccessibility"></a>

Dvb Dash Accessibility
+ `DVBDASH_1_VISUALLY_IMPAIRED`
+ `DVBDASH_2_HARD_OF_HEARING`
+ `DVBDASH_3_SUPPLEMENTAL_COMMENTARY`
+ `DVBDASH_4_DIRECTORS_COMMENTARY`
+ `DVBDASH_5_EDUCATIONAL_NOTES`
+ `DVBDASH_6_MAIN_PROGRAM`
+ `DVBDASH_7_CLEAN_FEED`

### DvbNitSettings
<a name="channels-model-dvbnitsettings"></a>

DVB Network Information Table (NIT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkId | integer<br />Minimum: 0<br />Maximum: 65536 | True | The numeric value placed in the Network Information Table (NIT). |
| networkName | string<br />MinLength: 1<br />MaxLength: 256 | True | The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters. |
| repInterval | integer<br />Minimum: 25<br />Maximum: 10000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbSdtOutputSdt
<a name="channels-model-dvbsdtoutputsdt"></a>

Dvb Sdt Output Sdt
+ `SDT_FOLLOW`
+ `SDT_FOLLOW_IF_PRESENT`
+ `SDT_MANUAL`
+ `SDT_NONE`

### DvbSdtSettings
<a name="channels-model-dvbsdtsettings"></a>

DVB Service Description Table (SDT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputSdt | [DvbSdtOutputSdt](#channels-model-dvbsdtoutputsdt) | False | Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information. |
| repInterval | integer<br />Minimum: 25<br />Maximum: 2000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| serviceName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters. |
| serviceProviderName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters. |

### DvbSubDestinationAlignment
<a name="channels-model-dvbsubdestinationalignment"></a>

Dvb Sub Destination Alignment
+ `CENTERED`
+ `LEFT`
+ `SMART`

### DvbSubDestinationBackgroundColor
<a name="channels-model-dvbsubdestinationbackgroundcolor"></a>

Dvb Sub Destination Background Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### DvbSubDestinationFontColor
<a name="channels-model-dvbsubdestinationfontcolor"></a>

Dvb Sub Destination Font Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### DvbSubDestinationOutlineColor
<a name="channels-model-dvbsubdestinationoutlinecolor"></a>

Dvb Sub Destination Outline Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### DvbSubDestinationSettings
<a name="channels-model-dvbsubdestinationsettings"></a>

Dvb Sub Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [DvbSubDestinationAlignment](#channels-model-dvbsubdestinationalignment) | False | If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| backgroundColor | [DvbSubDestinationBackgroundColor](#channels-model-dvbsubdestinationbackgroundcolor) | False | Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| font | [InputLocation](#channels-model-inputlocation) | False | External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match. |
| fontColor | [DvbSubDestinationFontColor](#channels-model-dvbsubdestinationfontcolor) | False | Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match. |
| fontSize | string | False | When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match. |
| outlineColor | [DvbSubDestinationOutlineColor](#channels-model-dvbsubdestinationoutlinecolor) | False | Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| shadowColor | [DvbSubDestinationShadowColor](#channels-model-dvbsubdestinationshadowcolor) | False | Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| shadowXOffset | integer | False | Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match. |
| shadowYOffset | integer | False | Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match. |
| subtitleRows | [DvbSubDestinationSubtitleRows](#channels-model-dvbsubdestinationsubtitlerows) | False | Applies only when the input captions are Teletext and the output captions are DVB-Sub or Burn-In. Choose the number of lines for the captions bitmap. The captions bitmap is 700 wide × 576 high and will be laid over the video. For example, a value of 16 divides the bitmap into 16 lines, with each line 36 pixels high (16 × 36 = 576). The default is 24 (24 pixels high). Enter the same number in every encode in every output that converts the same Teletext source to DVB-Sub or Burn-in. |
| teletextGridControl | [DvbSubDestinationTeletextGridControl](#channels-model-dvbsubdestinationteletextgridcontrol) | False | Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs. |
| xPosition | integer<br />Minimum: 0 | False | Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| yPosition | integer<br />Minimum: 0 | False | Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |

### DvbSubDestinationShadowColor
<a name="channels-model-dvbsubdestinationshadowcolor"></a>

Dvb Sub Destination Shadow Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### DvbSubDestinationSubtitleRows
<a name="channels-model-dvbsubdestinationsubtitlerows"></a>

Dvb Sub Destination Subtitle Rows
+ `ROWS_16`
+ `ROWS_20`
+ `ROWS_24`

### DvbSubDestinationTeletextGridControl
<a name="channels-model-dvbsubdestinationteletextgridcontrol"></a>

Dvb Sub Destination Teletext Grid Control
+ `FIXED`
+ `SCALED`

### DvbSubOcrLanguage
<a name="channels-model-dvbsubocrlanguage"></a>

Dvb Sub Ocr Language
+ `DEU`
+ `ENG`
+ `FRA`
+ `NLD`
+ `POR`
+ `SPA`

### DvbSubSourceSettings
<a name="channels-model-dvbsubsourcesettings"></a>

Dvb Sub Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ocrLanguage | [DvbSubOcrLanguage](#channels-model-dvbsubocrlanguage) | False | If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text. |
| pid | integer<br />Minimum: 1 | False | When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors. |

### DvbTdtSettings
<a name="channels-model-dvbtdtsettings"></a>

DVB Time and Date Table (SDT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| repInterval | integer<br />Minimum: 1000<br />Maximum: 30000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### Eac3AtmosCodingMode
<a name="channels-model-eac3atmoscodingmode"></a>

Eac3 Atmos Coding Mode
+ `CODING_MODE_5_1_4`
+ `CODING_MODE_7_1_4`
+ `CODING_MODE_9_1_6`

### Eac3AtmosDrcLine
<a name="channels-model-eac3atmosdrcline"></a>

Eac3 Atmos Drc Line
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3AtmosDrcRf
<a name="channels-model-eac3atmosdrcrf"></a>

Eac3 Atmos Drc Rf
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3AtmosSettings
<a name="channels-model-eac3atmossettings"></a>

Eac3 Atmos Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. Valid bitrates depend on the coding mode. |
| codingMode | [Eac3AtmosCodingMode](#channels-model-eac3atmoscodingmode) | False | Dolby Digital Plus with Dolby Atmos coding mode. Determines number of channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. Default 23. |
| drcLine | [Eac3AtmosDrcLine](#channels-model-eac3atmosdrcline) | False | Sets the Dolby dynamic range compression profile. |
| drcRf | [Eac3AtmosDrcRf](#channels-model-eac3atmosdrcrf) | False | Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels. |
| heightTrim | number | False | Height dimensional trim. Sets the maximum amount to attenuate the height channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels. |
| surroundTrim | number | False | Surround dimensional trim. Sets the maximum amount to attenuate the surround channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels. |

### Eac3AttenuationControl
<a name="channels-model-eac3attenuationcontrol"></a>

Eac3 Attenuation Control
+ `ATTENUATE_3_DB`
+ `NONE`

### Eac3BitstreamMode
<a name="channels-model-eac3bitstreammode"></a>

Eac3 Bitstream Mode
+ `COMMENTARY`
+ `COMPLETE_MAIN`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `VISUALLY_IMPAIRED`

### Eac3CodingMode
<a name="channels-model-eac3codingmode"></a>

Eac3 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2`

### Eac3DcFilter
<a name="channels-model-eac3dcfilter"></a>

Eac3 Dc Filter
+ `DISABLED`
+ `ENABLED`

### Eac3DrcLine
<a name="channels-model-eac3drcline"></a>

Eac3 Drc Line
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3DrcRf
<a name="channels-model-eac3drcrf"></a>

Eac3 Drc Rf
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3LfeControl
<a name="channels-model-eac3lfecontrol"></a>

Eac3 Lfe Control
+ `LFE`
+ `NO_LFE`

### Eac3LfeFilter
<a name="channels-model-eac3lfefilter"></a>

Eac3 Lfe Filter
+ `DISABLED`
+ `ENABLED`

### Eac3MetadataControl
<a name="channels-model-eac3metadatacontrol"></a>

Eac3 Metadata Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Eac3PassthroughControl
<a name="channels-model-eac3passthroughcontrol"></a>

Eac3 Passthrough Control
+ `NO_PASSTHROUGH`
+ `WHEN_POSSIBLE`

### Eac3PhaseControl
<a name="channels-model-eac3phasecontrol"></a>

Eac3 Phase Control
+ `NO_SHIFT`
+ `SHIFT_90_DEGREES`

### Eac3Settings
<a name="channels-model-eac3settings"></a>

Eac3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attenuationControl | [Eac3AttenuationControl](#channels-model-eac3attenuationcontrol) | False | When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode. |
| bitrate | number | False | Average bitrate in bits/second. Valid bitrates depend on the coding mode. |
| bitstreamMode | [Eac3BitstreamMode](#channels-model-eac3bitstreammode) | False | Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values. |
| codingMode | [Eac3CodingMode](#channels-model-eac3codingmode) | False | Dolby Digital Plus coding mode. Determines number of channels. |
| dcFilter | [Eac3DcFilter](#channels-model-eac3dcfilter) | False | When set to enabled, activates a DC highpass filter for all input channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through. |
| drcLine | [Eac3DrcLine](#channels-model-eac3drcline) | False | Sets the Dolby dynamic range compression profile. |
| drcRf | [Eac3DrcRf](#channels-model-eac3drcrf) | False | Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels. |
| lfeControl | [Eac3LfeControl](#channels-model-eac3lfecontrol) | False | When encoding 3/2 audio, setting to lfe enables the LFE channel |
| lfeFilter | [Eac3LfeFilter](#channels-model-eac3lfefilter) | False | When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode. |
| loRoCenterMixLevel | number | False | Left only/Right only center mix level. Only used for 3/2 coding mode. |
| loRoSurroundMixLevel | number | False | Left only/Right only surround mix level. Only used for 3/2 coding mode. |
| ltRtCenterMixLevel | number | False | Left total/Right total center mix level. Only used for 3/2 coding mode. |
| ltRtSurroundMixLevel | number | False | Left total/Right total surround mix level. Only used for 3/2 coding mode. |
| metadataControl | [Eac3MetadataControl](#channels-model-eac3metadatacontrol) | False | When set to followInput, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| passthroughControl | [Eac3PassthroughControl](#channels-model-eac3passthroughcontrol) | False | When set to whenPossible, input DD\+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding. |
| phaseControl | [Eac3PhaseControl](#channels-model-eac3phasecontrol) | False | When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode. |
| stereoDownmix | [Eac3StereoDownmix](#channels-model-eac3stereodownmix) | False | Stereo downmix preference. Only used for 3/2 coding mode. |
| surroundExMode | [Eac3SurroundExMode](#channels-model-eac3surroundexmode) | False | When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels. |
| surroundMode | [Eac3SurroundMode](#channels-model-eac3surroundmode) | False | When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels. |

### Eac3StereoDownmix
<a name="channels-model-eac3stereodownmix"></a>

Eac3 Stereo Downmix
+ `DPL2`
+ `LO_RO`
+ `LT_RT`
+ `NOT_INDICATED`

### Eac3SurroundExMode
<a name="channels-model-eac3surroundexmode"></a>

Eac3 Surround Ex Mode
+ `DISABLED`
+ `ENABLED`
+ `NOT_INDICATED`

### Eac3SurroundMode
<a name="channels-model-eac3surroundmode"></a>

Eac3 Surround Mode
+ `DISABLED`
+ `ENABLED`
+ `NOT_INDICATED`

### EbuTtDDestinationSettings
<a name="channels-model-ebuttddestinationsettings"></a>

Ebu Tt DDestination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyrightHolder | string<br />MaxLength: 1000 | False | Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. Complete this field if you want to include the name of the copyright holder in the copyright metadata tag in the TTML |
| defaultFontSize | integer<br />Minimum: 1<br />Maximum: 800 | False | Specifies the default font size as a percentage of the computed cell size. Valid only if the defaultLineHeight is also set. If you leave this field empty, the default font size is 80% of the cell size. |
| defaultLineHeight | integer<br />Minimum: 80<br />Maximum: 800 | False |  |
| fillLineGap | [EbuTtDFillLineGapControl](#channels-model-ebuttdfilllinegapcontrol) | False | Specifies how to handle the gap between the lines (in multi-line captions). - enabled: Fill with the captions background color (as specified in the input captions). - disabled: Leave the gap unfilled. |
| fontFamily | string | False | Specifies the font family to include in the font data attached to the EBU-TT captions. Valid only if styleControl is set to include. If you leave this field empty, the font family is set to "monospaced". (If styleControl is set to exclude, the font family is always set to "monospaced".) You specify only the font family. All other style information (color, bold, position and so on) is copied from the input captions. The size is always set to 100% to allow the downstream player to choose the size. - Enter a list of font families, as a comma-separated list of font names, in order of preference. The name can be a font family (such as “Arial”), or a generic font family (such as “serif”), or “default” (to let the downstream player choose the font). - Leave blank to set the family to “monospace”. |
| styleControl | [EbuTtDDestinationStyleControl](#channels-model-ebuttddestinationstylecontrol) | False | Specifies the style information (font color, font position, and so on) to include in the font data that is attached to the EBU-TT captions. - include: Take the style information (font color, font position, and so on) from the source captions and include that information in the font data attached to the EBU-TT captions. This option is valid only if the source captions are Embedded or Teletext. - exclude: In the font data attached to the EBU-TT captions, set the font family to "monospaced". Do not include any other style information. |

### EbuTtDDestinationStyleControl
<a name="channels-model-ebuttddestinationstylecontrol"></a>

Ebu Tt DDestination Style Control
+ `EXCLUDE`
+ `INCLUDE`

### EbuTtDFillLineGapControl
<a name="channels-model-ebuttdfilllinegapcontrol"></a>

Ebu Tt DFill Line Gap Control
+ `DISABLED`
+ `ENABLED`

### EmbeddedCaptionPositionSettings
<a name="channels-model-embeddedcaptionpositionsettings"></a>

Specifies the position of embedded output captions when `styleControl` is set to `MANUAL`, as a row counted from the top of the output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| yPositionLine | integer<br />Minimum: 1<br />Maximum: 15 | False | Specifies the vertical position of the caption as a row counted from the top of the output. Row 1 is the topmost row. Acceptable values are 1 through 15. |

### EmbeddedConvert608To708
<a name="channels-model-embeddedconvert608to708"></a>

Embedded Convert608 To708
+ `DISABLED`
+ `UPCONVERT`

### EmbeddedDestinationSettings
<a name="channels-model-embeddeddestinationsettings"></a>

Embedded Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| position | [EmbeddedCaptionPositionSettings](#channels-model-embeddedcaptionpositionsettings) | False | Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`. |
| styleControl | [EmbeddedDestinationStyleControl](#channels-model-embeddeddestinationstylecontrol) | False | Controls the source of position and style information for the output captions. Valid values:+ `PASSTHROUGH` – Carry the caption position and style from the source captions. When the source captions are embedded, SCTE-20, or ancillary, the position and style are preserved exactly. When the source captions are another format, the position and any supported style are carried over.<br />+ `MANUAL` – Applies the specified styling and positioning. All other styling and positioning is given default values.<br />If you don't specify this field, the default is `PASSTHROUGH`. |

### EmbeddedDestinationStyleControl
<a name="channels-model-embeddeddestinationstylecontrol"></a>

Controls the source of position and style information for embedded output captions. For the valid values, see the `styleControl` field in `EmbeddedDestinationSettings`.
+ `MANUAL`
+ `PASSTHROUGH`

### EmbeddedPlusScte20DestinationSettings
<a name="channels-model-embeddedplusscte20destinationsettings"></a>

Embedded Plus Scte20 Destination Settings

### EmbeddedScte20Detection
<a name="channels-model-embeddedscte20detection"></a>

Embedded Scte20 Detection
+ `AUTO`
+ `OFF`

### EmbeddedSourceSettings
<a name="channels-model-embeddedsourcesettings"></a>

Embedded Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [EmbeddedConvert608To708](#channels-model-embeddedconvert608to708) | False | If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded. |
| scte20Detection | [EmbeddedScte20Detection](#channels-model-embeddedscte20detection) | False | Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions. |
| source608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough. |
| source608TrackNumber | integer<br />Minimum: 1<br />Maximum: 5 | False | This field is unused and deprecated. |

### EncoderSettings
<a name="channels-model-encodersettings"></a>

Encoder Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptions | Array of type [AudioDescription](#channels-model-audiodescription) | True |  |
| availBlanking | [AvailBlanking](#channels-model-availblanking) | False | Settings for ad avail blanking. |
| availConfiguration | [AvailConfiguration](#channels-model-availconfiguration) | False | Event-wide configuration settings for ad avail insertion. |
| blackoutSlate | [BlackoutSlate](#channels-model-blackoutslate) | False | Settings for blackout slate. |
| captionDescriptions | Array of type [CaptionDescription](#channels-model-captiondescription) | False | Settings for caption decriptions |
| colorCorrectionSettings | [ColorCorrectionSettings](#channels-model-colorcorrectionsettings) | False | Color Correction Settings |
| featureActivations | [FeatureActivations](#channels-model-featureactivations) | False | Feature Activations |
| globalConfiguration | [GlobalConfiguration](#channels-model-globalconfiguration) | False | Configuration settings that apply to the event as a whole. |
| motionGraphicsConfiguration | [MotionGraphicsConfiguration](#channels-model-motiongraphicsconfiguration) | False | Settings for motion graphics. |
| nielsenConfiguration | [NielsenConfiguration](#channels-model-nielsenconfiguration) | False | Nielsen configuration settings. |
| outputGroups | Array of type [OutputGroup](#channels-model-outputgroup) | True |  |
| thumbnailConfiguration | [ThumbnailConfiguration](#channels-model-thumbnailconfiguration) | False | Thumbnail configuration settings. |
| timecodeConfig | [TimecodeConfig](#channels-model-timecodeconfig) | True | Contains settings used to acquire and adjust timecode information from inputs. |
| videoDescriptions | Array of type [VideoDescription](#channels-model-videodescription) | True |  |

### EnrichmentMethod
<a name="channels-model-enrichmentmethod"></a>

A Contextual Metadata Enrichment method. For the valid values, see the `enrichmentMethods` field in `InferenceSettings`.
+ `SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS`

### EpochLockingSettings
<a name="channels-model-epochlockingsettings"></a>

Epoch Locking Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customEpoch | string | False | Optional. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00. |
| jamSyncTime | string | False | Optional. Enter a time for the jam sync. The default is midnight UTC. When epoch locking is enabled, MediaLive performs a daily jam sync on every output encode to ensure timecodes don’t diverge from the wall clock. The jam sync applies only to encodes with frame rate of 29.97 or 59.94 FPS. To override, enter a time in HH:MM:SS in UTC. Always set the MM:SS portion to 00:00. |

### Esam
<a name="channels-model-esam"></a>

Esam

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| acquisitionPointId | string<br />MaxLength: 256 | True | Sent as acquisitionPointIdentity to identify the MediaLive channel to the POIS. |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages. |
| passwordParam | string | False |  |
| poisEndpoint | string<br />MaxLength: 2048 | True | The URL of the signal conditioner endpoint on the Placement Opportunity Information System (POIS). MediaLive sends SignalProcessingEvents here when SCTE-35 messages are read. |
| username | string | False |  |
| zoneIdentity | string<br />MaxLength: 256 | False | Optional data sent as zoneIdentity to identify the MediaLive channel to the POIS. |

### FailoverCondition
<a name="channels-model-failovercondition"></a>

Failover Condition settings. There can be multiple failover conditions inside AutomaticInputFailoverSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| failoverConditionSettings | [FailoverConditionSettings](#channels-model-failoverconditionsettings) | False | Failover condition type-specific settings. |

### FailoverConditionSettings
<a name="channels-model-failoverconditionsettings"></a>

Settings for one failover condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSilenceSettings | [AudioSilenceFailoverSettings](#channels-model-audiosilencefailoversettings) | False | MediaLive will perform a failover if the specified audio selector is silent for the specified period. |
| inputLossSettings | [InputLossFailoverSettings](#channels-model-inputlossfailoversettings) | False | MediaLive will perform a failover if content is not detected in this input for the specified period. |
| videoBlackSettings | [VideoBlackFailoverSettings](#channels-model-videoblackfailoversettings) | False | MediaLive will perform a failover if content is considered black for the specified period. |

### FeatureActivations
<a name="channels-model-featureactivations"></a>

Feature Activations

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputPrepareScheduleActions | [FeatureActivationsInputPrepareScheduleActions](#channels-model-featureactivationsinputpreparescheduleactions) | False | Enables the Input Prepare feature. You can create Input Prepare actions in the schedule only if this feature is enabled. If you disable the feature on an existing schedule, make sure that you first delete all input prepare actions from the schedule. |
| outputStaticImageOverlayScheduleActions | [FeatureActivationsOutputStaticImageOverlayScheduleActions](#channels-model-featureactivationsoutputstaticimageoverlayscheduleactions) | False | Enables the output static image overlay feature. Enabling this feature allows you to send channel schedule updates to display/clear/modify image overlays on an output-by-output bases. |

### FeatureActivationsInputPrepareScheduleActions
<a name="channels-model-featureactivationsinputpreparescheduleactions"></a>

Feature Activations Input Prepare Schedule Actions
+ `DISABLED`
+ `ENABLED`

### FeatureActivationsOutputStaticImageOverlayScheduleActions
<a name="channels-model-featureactivationsoutputstaticimageoverlayscheduleactions"></a>

Feature Activations Output Static Image Overlay Schedule Actions
+ `DISABLED`
+ `ENABLED`

### FecOutputIncludeFec
<a name="channels-model-fecoutputincludefec"></a>

Fec Output Include Fec
+ `COLUMN`
+ `COLUMN_AND_ROW`

### FecOutputSettings
<a name="channels-model-fecoutputsettings"></a>

Fec Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| columnDepth | integer<br />Minimum: 4<br />Maximum: 20 | False | Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive. |
| includeFec | [FecOutputIncludeFec](#channels-model-fecoutputincludefec) | False | Enables column only or column and row based FEC |
| rowLength | integer<br />Minimum: 1<br />Maximum: 20 | False | Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive. |

### FixedAfd
<a name="channels-model-fixedafd"></a>

Fixed Afd
+ `AFD_0000`
+ `AFD_0010`
+ `AFD_0011`
+ `AFD_0100`
+ `AFD_1000`
+ `AFD_1001`
+ `AFD_1010`
+ `AFD_1011`
+ `AFD_1101`
+ `AFD_1110`
+ `AFD_1111`

### Fmp4HlsSettings
<a name="channels-model-fmp4hlssettings"></a>

Fmp4 Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioRenditionSets | string | False | List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','. |
| nielsenId3Behavior | [Fmp4NielsenId3Behavior](#channels-model-fmp4nielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| timedMetadataBehavior | [Fmp4TimedMetadataBehavior](#channels-model-fmp4timedmetadatabehavior) | False | When set to passthrough, timed metadata is passed through from input to output. |

### Fmp4NielsenId3Behavior
<a name="channels-model-fmp4nielsenid3behavior"></a>

Fmp4 Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### Fmp4TimedMetadataBehavior
<a name="channels-model-fmp4timedmetadatabehavior"></a>

Fmp4 Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### FollowerChannelSettings
<a name="channels-model-followerchannelsettings"></a>

Settings for a follower channel in a linked pair

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| linkedChannelType | [LinkedChannelType](#channels-model-linkedchanneltype) | False | Specifies this as a follower channel |
| primaryChannelArn | string | False | The ARN of the primary channel to follow |

### FrameCaptureCdnSettings
<a name="channels-model-framecapturecdnsettings"></a>

Frame Capture Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| frameCaptureS3Settings | [FrameCaptureS3Settings](#channels-model-framecaptures3settings) | False |  |

### FrameCaptureGroupSettings
<a name="channels-model-framecapturegroupsettings"></a>

Frame Capture Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | The destination for the frame capture files. Either the URI for an Amazon S3 bucket and object, plus a file name prefix (for example, s3ssl://sportsDelivery/highlights/20180820/curling-) or the URI for a MediaStore container, plus a file name prefix (for example, mediastoressl://sportsDelivery/20180820/curling-). The final file names consist of the prefix from the destination field (for example, "curling-") \+ name modifier \+ the counter (5 digits, starting from 00001) \+ extension (which is always .jpg). For example, curling-low.00001.jpg |
| frameCaptureCdnSettings | [FrameCaptureCdnSettings](#channels-model-framecapturecdnsettings) | False | Parameters that control interactions with the CDN. |

### FrameCaptureHlsSettings
<a name="channels-model-framecapturehlssettings"></a>

Frame Capture Hls Settings

### FrameCaptureIntervalUnit
<a name="channels-model-framecaptureintervalunit"></a>

Frame Capture Interval Unit
+ `MILLISECONDS`
+ `SECONDS`

### FrameCaptureOutputSettings
<a name="channels-model-framecaptureoutputsettings"></a>

Frame Capture Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nameModifier | string | False | Required if the output group contains more than one output. This modifier forms part of the output file name. |

### FrameCaptureS3LogUploads
<a name="channels-model-framecaptures3loguploads"></a>

Frame Capture S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### FrameCaptureS3Settings
<a name="channels-model-framecaptures3settings"></a>

Frame Capture S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [FrameCaptureS3LogUploads](#channels-model-framecaptures3loguploads) | False | When set to enabled, each upload to CDN or server will be logged. |

### FrameCaptureSettings
<a name="channels-model-framecapturesettings"></a>

Frame Capture Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captureInterval | integer<br />Minimum: 1<br />Maximum: 3600000 | False | The frequency at which to capture frames for inclusion in the output. May be specified in either seconds or milliseconds, as specified by captureIntervalUnits. |
| captureIntervalUnits | [FrameCaptureIntervalUnit](#channels-model-framecaptureintervalunit) | False | Unit for the frame capture interval. |
| timecodeBurninSettings | [TimecodeBurninSettings](#channels-model-timecodeburninsettings) | False | Timecode burn-in settings |

### GatewayTimeoutException
<a name="channels-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GlobalConfiguration
<a name="channels-model-globalconfiguration"></a>

Global Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| initialAudioGain | integer<br />Minimum: -60<br />Maximum: 60 | False | Value to set the initial audio gain for the Live Event. |
| inputEndAction | [GlobalConfigurationInputEndAction](#channels-model-globalconfigurationinputendaction) | False | Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When "none" is configured the encoder will transcode either black, a solid color, or a user specified slate images per the "Input Loss Behavior" configuration until the next input switch occurs (which is controlled through the Channel Schedule API). |
| inputLossBehavior | [InputLossBehavior](#channels-model-inputlossbehavior) | False | Settings for system actions when input is lost. |
| outputLockingMode | [GlobalConfigurationOutputLockingMode](#channels-model-globalconfigurationoutputlockingmode) | False | Indicates how MediaLive pipelines are synchronized. PIPELINE\_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the other. EPOCH\_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the Unix epoch. |
| outputLockingSettings | [OutputLockingSettings](#channels-model-outputlockingsettings) | False | Advanced output locking settings |
| outputTimingSource | [GlobalConfigurationOutputTimingSource](#channels-model-globalconfigurationoutputtimingsource) | False | Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream. |
| supportLowFramerateInputs | [GlobalConfigurationLowFramerateInputs](#channels-model-globalconfigurationlowframerateinputs) | False | Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second. |

### GlobalConfigurationInputEndAction
<a name="channels-model-globalconfigurationinputendaction"></a>

Global Configuration Input End Action
+ `NONE`
+ `SWITCH_AND_LOOP_INPUTS`

### GlobalConfigurationLowFramerateInputs
<a name="channels-model-globalconfigurationlowframerateinputs"></a>

Global Configuration Low Framerate Inputs
+ `DISABLED`
+ `ENABLED`

### GlobalConfigurationOutputLockingMode
<a name="channels-model-globalconfigurationoutputlockingmode"></a>

Global Configuration Output Locking Mode
+ `DISABLED`
+ `EPOCH_LOCKING`
+ `PIPELINE_LOCKING`

### GlobalConfigurationOutputTimingSource
<a name="channels-model-globalconfigurationoutputtimingsource"></a>

Global Configuration Output Timing Source
+ `INPUT_CLOCK`
+ `SYSTEM_CLOCK`

### H264AdaptiveQuantization
<a name="channels-model-h264adaptivequantization"></a>

H264 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `HIGHER`
+ `LOW`
+ `MAX`
+ `MEDIUM`
+ `OFF`

### H264AllowExplicitWeightedPrediction
<a name="channels-model-h264allowexplicitweightedprediction"></a>

Specifies whether the encoder may apply explicit weighted prediction (EWP).
+ `DISABLED`
+ `ENABLED`

### H264ColorMetadata
<a name="channels-model-h264colormetadata"></a>

H264 Color Metadata
+ `IGNORE`
+ `INSERT`

### H264ColorSpaceSettings
<a name="channels-model-h264colorspacesettings"></a>

H264 Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpacePassthroughSettings | [ColorSpacePassthroughSettings](#channels-model-colorspacepassthroughsettings) | False |  |
| rec601Settings | [Rec601Settings](#channels-model-rec601settings) | False |  |
| rec709Settings | [Rec709Settings](#channels-model-rec709settings) | False |  |

### H264EntropyEncoding
<a name="channels-model-h264entropyencoding"></a>

H264 Entropy Encoding
+ `CABAC`
+ `CAVLC`

### H264FilterSettings
<a name="channels-model-h264filtersettings"></a>

H264 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bandwidthReductionFilterSettings | [BandwidthReductionFilterSettings](#channels-model-bandwidthreductionfiltersettings) | False |  |
| temporalFilterSettings | [TemporalFilterSettings](#channels-model-temporalfiltersettings) | False |  |

### H264FlickerAq
<a name="channels-model-h264flickeraq"></a>

H264 Flicker Aq
+ `DISABLED`
+ `ENABLED`

### H264ForceFieldPictures
<a name="channels-model-h264forcefieldpictures"></a>

H264 Force Field Pictures
+ `DISABLED`
+ `ENABLED`

### H264FramerateControl
<a name="channels-model-h264frameratecontrol"></a>

H264 Framerate Control
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264GopBReference
<a name="channels-model-h264gopbreference"></a>

H264 Gop BReference
+ `DISABLED`
+ `ENABLED`

### H264GopSizeUnits
<a name="channels-model-h264gopsizeunits"></a>

H264 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### H264Level
<a name="channels-model-h264level"></a>

H264 Level
+ `H264_LEVEL_1`
+ `H264_LEVEL_1_1`
+ `H264_LEVEL_1_2`
+ `H264_LEVEL_1_3`
+ `H264_LEVEL_2`
+ `H264_LEVEL_2_1`
+ `H264_LEVEL_2_2`
+ `H264_LEVEL_3`
+ `H264_LEVEL_3_1`
+ `H264_LEVEL_3_2`
+ `H264_LEVEL_4`
+ `H264_LEVEL_4_1`
+ `H264_LEVEL_4_2`
+ `H264_LEVEL_5`
+ `H264_LEVEL_5_1`
+ `H264_LEVEL_5_2`
+ `H264_LEVEL_AUTO`

### H264LookAheadRateControl
<a name="channels-model-h264lookaheadratecontrol"></a>

H264 Look Ahead Rate Control
+ `HIGH`
+ `LOW`
+ `MEDIUM`

### H264ParControl
<a name="channels-model-h264parcontrol"></a>

H264 Par Control
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264Profile
<a name="channels-model-h264profile"></a>

H264 Profile
+ `BASELINE`
+ `HIGH`
+ `HIGH_10BIT`
+ `HIGH_422`
+ `HIGH_422_10BIT`
+ `MAIN`

### H264QualityLevel
<a name="channels-model-h264qualitylevel"></a>

H264 Quality Level
+ `ENHANCED_QUALITY`
+ `STANDARD_QUALITY`

### H264RateControlMode
<a name="channels-model-h264ratecontrolmode"></a>

H264 Rate Control Mode
+ `CBR`
+ `MULTIPLEX`
+ `QVBR`
+ `VBR`

### H264ScanType
<a name="channels-model-h264scantype"></a>

H264 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### H264SceneChangeDetect
<a name="channels-model-h264scenechangedetect"></a>

H264 Scene Change Detect
+ `DISABLED`
+ `ENABLED`

### H264Settings
<a name="channels-model-h264settings"></a>

H264 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H264AdaptiveQuantization](#channels-model-h264adaptivequantization) | False | Enables or disables adaptive quantization, which is a technique MediaLive can apply to video on a frame-by-frame basis to produce more compression without losing quality. There are three types of adaptive quantization: flicker, spatial, and temporal. Set the field in one of these ways: Set to Auto. Recommended. For each type of AQ, MediaLive will determine if AQ is needed, and if so, the appropriate strength. Set a strength (a value other than Auto or Disable). This strength will apply to any of the AQ fields that you choose to enable. Set to Disabled to disable all types of adaptive quantization. |
| afdSignaling | [AfdSignaling](#channels-model-afdsignaling) | False | Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter. |
| allowExplicitWeightedPrediction | [H264AllowExplicitWeightedPrediction](#channels-model-h264allowexplicitweightedprediction) | False | Specifies whether the encoder may apply explicit weighted prediction (EWP), an H.264 coding tool that can improve compression. EWP applies a scaling factor and offset to reference frames, which helps when brightness changes between frames, such as during a fade. When this setting is ENABLED, the encoder decides whether to apply EWP based on the output's other codec settings, such as profile and quality level. We recommend that you keep the default, ENABLED. When DISABLED, the encoder never applies EWP. |
| bitrate | integer<br />Minimum: 1000 | False | Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000. |
| bufFillPct | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| bufSize | integer<br />Minimum: 0 | False | Size of buffer (HRD buffer model) in bits. |
| colorMetadata | [H264ColorMetadata](#channels-model-h264colormetadata) | False | Includes colorspace metadata in the output. |
| colorSpaceSettings | [H264ColorSpaceSettings](#channels-model-h264colorspacesettings) | False | Color Space settings |
| entropyEncoding | [H264EntropyEncoding](#channels-model-h264entropyencoding) | False | Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc. |
| filterSettings | [H264FilterSettings](#channels-model-h264filtersettings) | False | Optional filters that you can apply to an encode. |
| fixedAfd | [FixedAfd](#channels-model-fixedafd) | False | Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'. |
| flickerAq | [H264FlickerAq](#channels-model-h264flickeraq) | False | Flicker AQ makes adjustments within each frame to reduce flicker or 'pop' on I-frames. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if flicker AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply flicker AQ using the specified strength. Disabled: MediaLive won't apply flicker AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply flicker AQ. |
| forceFieldPictures | [H264ForceFieldPictures](#channels-model-h264forcefieldpictures) | False | This setting applies only when scan type is "interlaced." It controls whether coding is performed on a field basis or on a frame basis. (When the video is progressive, the coding is always performed on a frame basis.) enabled: Force MediaLive to code on a field basis, so that odd and even sets of fields are coded separately. disabled: Code the two sets of fields separately (on a field basis) or together (on a frame basis using PAFF), depending on what is most appropriate for the content. |
| framerateControl | [H264FramerateControl](#channels-model-h264frameratecontrol) | False | This field indicates how the output video frame rate is specified. If "specified" is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if "initializeFromSource" is selected then the output video frame rate will be set equal to the input video frame rate of the first input. |
| framerateDenominator | integer<br />Minimum: 1 | False | Framerate denominator. |
| framerateNumerator | integer<br />Minimum: 1 | False | Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps. |
| gopBReference | [H264GopBReference](#channels-model-h264gopbreference) | False | If enabled, use reference B frames for GOP structures that have B frames > 1. |
| gopClosedCadence | integer<br />Minimum: 0 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| gopNumBFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Number of B-frames between reference frames. |
| gopSize | number | False | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer. |
| gopSizeUnits | [H264GopSizeUnits](#channels-model-h264gopsizeunits) | False | Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time. |
| level | [H264Level](#channels-model-h264level) | False | H.264 Level. |
| lookAheadRateControl | [H264LookAheadRateControl](#channels-model-h264lookaheadratecontrol) | False | Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content. |
| maxBitrate | integer<br />Minimum: 1000 | False | For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video. |
| minBitrate | integer<br />Minimum: 0 | False | Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size \+ Min-I-interval - 1 |
| minQp | integer<br />Minimum: 1<br />Maximum: 51 | False | Sets the minimum QP. If you aren't familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value. |
| numRefFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H264ParControl](#channels-model-h264parcontrol) | False | This field indicates how the output pixel aspect ratio is specified. If "specified" is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if "initializeFromSource" is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input. |
| parDenominator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio denominator. |
| parNumerator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio numerator. |
| profile | [H264Profile](#channels-model-h264profile) | False | H.264 Profile. |
| qualityLevel | [H264QualityLevel](#channels-model-h264qualitylevel) | False | Leave as STANDARD\_QUALITY or choose a different value (which might result in additional costs to run the channel). - ENHANCED\_QUALITY: Produces a slightly better video quality without an increase in the bitrate. Has an effect only when the Rate control mode is QVBR or CBR. If this channel is in a MediaLive multiplex, the value must be ENHANCED\_QUALITY. - STANDARD\_QUALITY: Valid for any Rate control mode. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. You can set a target quality or you can let MediaLive determine the best quality. To set a target quality, enter values in the QVBR quality level field and the Max bitrate field. Enter values that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M To let MediaLive decide, leave the QVBR quality level field empty, and in Max bitrate enter the maximum rate you want in the video. For more information, see the section called "Video - rate control mode" in the MediaLive user guide |
| rateControlMode | [H264RateControlMode](#channels-model-h264ratecontrolmode) | False | Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program. |
| scanType | [H264ScanType](#channels-model-h264scantype) | False | Sets the scan type of the output to progressive or top-field-first interlaced. |
| sceneChangeDetect | [H264SceneChangeDetect](#channels-model-h264scenechangedetect) | False | Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image. If not set to zero, must be greater than 15. |
| spatialAq | [H264SpatialAq](#channels-model-h264spatialaq) | False | Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if spatial AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply spatial AQ using the specified strength. Disabled: MediaLive won't apply spatial AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply spatial AQ. |
| subgopLength | [H264SubGopLength](#channels-model-h264subgoplength) | False | If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality. |
| syntax | [H264Syntax](#channels-model-h264syntax) | False | Produces a bitstream compliant with SMPTE RP-2027. |
| temporalAq | [H264TemporalAq](#channels-model-h264temporalaq) | False | Temporal makes adjustments within each frame based on temporal variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if temporal AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply temporal AQ using the specified strength. Disabled: MediaLive won't apply temporal AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply temporal AQ. |
| timecodeBurninSettings | [TimecodeBurninSettings](#channels-model-timecodeburninsettings) | False | Timecode burn-in settings |
| timecodeInsertion | [H264TimecodeInsertionBehavior](#channels-model-h264timecodeinsertionbehavior) | False | Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config |

### H264SpatialAq
<a name="channels-model-h264spatialaq"></a>

H264 Spatial Aq
+ `DISABLED`
+ `ENABLED`

### H264SubGopLength
<a name="channels-model-h264subgoplength"></a>

H264 Sub Gop Length
+ `DYNAMIC`
+ `FIXED`

### H264Syntax
<a name="channels-model-h264syntax"></a>

H264 Syntax
+ `DEFAULT`
+ `RP2027`

### H264TemporalAq
<a name="channels-model-h264temporalaq"></a>

H264 Temporal Aq
+ `DISABLED`
+ `ENABLED`

### H264TimecodeInsertionBehavior
<a name="channels-model-h264timecodeinsertionbehavior"></a>

H264 Timecode Insertion Behavior
+ `DISABLED`
+ `PIC_TIMING_SEI`

### H265AdaptiveQuantization
<a name="channels-model-h265adaptivequantization"></a>

H265 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `HIGHER`
+ `LOW`
+ `MAX`
+ `MEDIUM`
+ `OFF`

### H265AlternativeTransferFunction
<a name="channels-model-h265alternativetransferfunction"></a>

H265 Alternative Transfer Function
+ `INSERT`
+ `OMIT`

### H265ColorMetadata
<a name="channels-model-h265colormetadata"></a>

H265 Color Metadata
+ `IGNORE`
+ `INSERT`

### H265ColorSpaceSettings
<a name="channels-model-h265colorspacesettings"></a>

H265 Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpacePassthroughSettings | [ColorSpacePassthroughSettings](#channels-model-colorspacepassthroughsettings) | False |  |
| dolbyVision81Settings | [DolbyVision81Settings](#channels-model-dolbyvision81settings) | False |  |
| hdr10Settings | [Hdr10Settings](#channels-model-hdr10settings) | False |  |
| hlg2020Settings | [Hlg2020Settings](#channels-model-hlg2020settings) | False |  |
| rec601Settings | [Rec601Settings](#channels-model-rec601settings) | False |  |
| rec709Settings | [Rec709Settings](#channels-model-rec709settings) | False |  |

### H265Deblocking
<a name="channels-model-h265deblocking"></a>

H265 Deblocking
+ `DISABLED`
+ `ENABLED`

### H265FilterSettings
<a name="channels-model-h265filtersettings"></a>

H265 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bandwidthReductionFilterSettings | [BandwidthReductionFilterSettings](#channels-model-bandwidthreductionfiltersettings) | False |  |
| temporalFilterSettings | [TemporalFilterSettings](#channels-model-temporalfiltersettings) | False |  |

### H265FlickerAq
<a name="channels-model-h265flickeraq"></a>

H265 Flicker Aq
+ `DISABLED`
+ `ENABLED`

### H265GopBReference
<a name="channels-model-h265gopbreference"></a>

H265 Gop BReference
+ `DISABLED`
+ `ENABLED`

### H265GopSizeUnits
<a name="channels-model-h265gopsizeunits"></a>

H265 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### H265Level
<a name="channels-model-h265level"></a>

H265 Level
+ `H265_LEVEL_1`
+ `H265_LEVEL_2`
+ `H265_LEVEL_2_1`
+ `H265_LEVEL_3`
+ `H265_LEVEL_3_1`
+ `H265_LEVEL_4`
+ `H265_LEVEL_4_1`
+ `H265_LEVEL_5`
+ `H265_LEVEL_5_1`
+ `H265_LEVEL_5_2`
+ `H265_LEVEL_6`
+ `H265_LEVEL_6_1`
+ `H265_LEVEL_6_2`
+ `H265_LEVEL_AUTO`

### H265LookAheadRateControl
<a name="channels-model-h265lookaheadratecontrol"></a>

H265 Look Ahead Rate Control
+ `HIGH`
+ `LOW`
+ `MEDIUM`

### H265MvOverPictureBoundaries
<a name="channels-model-h265mvoverpictureboundaries"></a>

H265 Mv Over Picture Boundaries
+ `DISABLED`
+ `ENABLED`

### H265MvTemporalPredictor
<a name="channels-model-h265mvtemporalpredictor"></a>

H265 Mv Temporal Predictor
+ `DISABLED`
+ `ENABLED`

### H265Profile
<a name="channels-model-h265profile"></a>

H265 Profile
+ `MAIN`
+ `MAIN_10BIT`

### H265RateControlMode
<a name="channels-model-h265ratecontrolmode"></a>

H265 Rate Control Mode
+ `CBR`
+ `MULTIPLEX`
+ `QVBR`

### H265ScanType
<a name="channels-model-h265scantype"></a>

H265 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### H265SceneChangeDetect
<a name="channels-model-h265scenechangedetect"></a>

H265 Scene Change Detect
+ `DISABLED`
+ `ENABLED`

### H265Settings
<a name="channels-model-h265settings"></a>

H265 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H265AdaptiveQuantization](#channels-model-h265adaptivequantization) | False | Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality. |
| afdSignaling | [AfdSignaling](#channels-model-afdsignaling) | False | Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter. |
| alternativeTransferFunction | [H265AlternativeTransferFunction](#channels-model-h265alternativetransferfunction) | False | Whether or not EML should insert an Alternative Transfer Function SEI message to support backwards compatibility with non-HDR decoders and displays. |
| bitrate | integer<br />Minimum: 100000<br />Maximum: 40000000 | False | Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000. |
| bufSize | integer<br />Minimum: 100000<br />Maximum: 80000000 | False | Size of buffer (HRD buffer model) in bits. |
| colorMetadata | [H265ColorMetadata](#channels-model-h265colormetadata) | False | Includes colorspace metadata in the output. |
| colorSpaceSettings | [H265ColorSpaceSettings](#channels-model-h265colorspacesettings) | False | Color Space settings |
| deblocking | [H265Deblocking](#channels-model-h265deblocking) | False | Enable or disable the deblocking filter for this codec. The filter reduces blocking artifacts at block boundaries, which improves overall video quality. If the filter is disabled, visible block edges might appear in the output, especially at lower bitrates. |
| filterSettings | [H265FilterSettings](#channels-model-h265filtersettings) | False | Optional filters that you can apply to an encode. |
| fixedAfd | [FixedAfd](#channels-model-fixedafd) | False | Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'. |
| flickerAq | [H265FlickerAq](#channels-model-h265flickeraq) | False | If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 3003 | True | Framerate denominator. |
| framerateNumerator | integer<br />Minimum: 1 | True | Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps. |
| gopBReference | [H265GopBReference](#channels-model-h265gopbreference) | False | Allows the encoder to use a B-Frame as a reference frame as well. ENABLED: B-frames will also serve as reference frames. DISABLED: B-frames won't be reference frames. Must be DISABLED if resolution is greater than 1080p or when using tiled hevc encoding. |
| gopClosedCadence | integer<br />Minimum: 0 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| gopNumBFrames | integer<br />Minimum: 0<br />Maximum: 3 | False | Sets the number of B-frames between reference frames. Set to 2 if resolution is greater than 1080p or when using tiled hevc encoding. |
| gopSize | number | False | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer. |
| gopSizeUnits | [H265GopSizeUnits](#channels-model-h265gopsizeunits) | False | Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time. |
| level | [H265Level](#channels-model-h265level) | False | H.265 Level. |
| lookAheadRateControl | [H265LookAheadRateControl](#channels-model-h265lookaheadratecontrol) | False | Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content. |
| maxBitrate | integer<br />Minimum: 100000<br />Maximum: 40000000 | False | For QVBR: See the tooltip for Quality level |
| minBitrate | integer<br />Minimum: 0<br />Maximum: 40000000 | False | Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size \+ Min-I-interval - 1 |
| minQp | integer<br />Minimum: 1<br />Maximum: 51 | False | Sets the minimum QP. If you aren't familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value. |
| mvOverPictureBoundaries | [H265MvOverPictureBoundaries](#channels-model-h265mvoverpictureboundaries) | False | If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled". |
| mvTemporalPredictor | [H265MvTemporalPredictor](#channels-model-h265mvtemporalpredictor) | False | If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled". |
| parDenominator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio denominator. |
| parNumerator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio numerator. |
| profile | [H265Profile](#channels-model-h265profile) | False | H.265 Profile. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M |
| rateControlMode | [H265RateControlMode](#channels-model-h265ratecontrolmode) | False | Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program. |
| scanType | [H265ScanType](#channels-model-h265scantype) | False | Sets the scan type of the output to progressive or top-field-first interlaced. |
| sceneChangeDetect | [H265SceneChangeDetect](#channels-model-h265scenechangedetect) | False | Scene change detection. |
| slices | integer<br />Minimum: 1<br />Maximum: 16 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution. |
| subgopLength | [H265SubGopLength](#channels-model-h265subgoplength) | False | Sets the number of B-frames in each sub-GOP. FIXED: Use the value in Num B-frames. DYNAMIC: Optimizes the number of B-frames in each sub-GOP to improve visual quality. Must be FIXED if resolution is greater than 1080p or when using tiled hevc encoding. |
| tier | [H265Tier](#channels-model-h265tier) | False | H.265 Tier. |
| tileHeight | integer<br />Minimum: 64<br />Maximum: 2160 | False | Set this field to set up the picture as a tile. You must also set tileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 of less. If the tile width and height are specified, MediaLive will override the video codec slices field with a value that MediaLive calculates |
| tilePadding | [H265TilePadding](#channels-model-h265tilepadding) | False | Set to "padded" to force MediaLive to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none". |
| tileWidth | integer<br />Minimum: 256<br />Maximum: 3840 | False | Set this field to set up the picture as a tile. See tileHeight for more information. |
| timecodeBurninSettings | [TimecodeBurninSettings](#channels-model-timecodeburninsettings) | False | Timecode burn-in settings |
| timecodeInsertion | [H265TimecodeInsertionBehavior](#channels-model-h265timecodeinsertionbehavior) | False | Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config |
| treeblockSize | [H265TreeblockSize](#channels-model-h265treeblocksize) | False | Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto". |

### H265SubGopLength
<a name="channels-model-h265subgoplength"></a>

H265 Sub Gop Length
+ `DYNAMIC`
+ `FIXED`

### H265Tier
<a name="channels-model-h265tier"></a>

H265 Tier
+ `HIGH`
+ `MAIN`

### H265TilePadding
<a name="channels-model-h265tilepadding"></a>

H265 Tile Padding
+ `NONE`
+ `PADDED`

### H265TimecodeInsertionBehavior
<a name="channels-model-h265timecodeinsertionbehavior"></a>

H265 Timecode Insertion Behavior
+ `DISABLED`
+ `PIC_TIMING_SEI`

### H265TreeblockSize
<a name="channels-model-h265treeblocksize"></a>

H265 Treeblock Size
+ `AUTO`
+ `TREE_SIZE_32X32`

### Hdr10Settings
<a name="channels-model-hdr10settings"></a>

Hdr10 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxCll | integer<br />Minimum: 0<br />Maximum: 32768 | False | Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file. |
| maxFall | integer<br />Minimum: 0<br />Maximum: 32768 | False | Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file. |

### Hlg2020Settings
<a name="channels-model-hlg2020settings"></a>

Hlg2020 Settings

### HlsAdMarkers
<a name="channels-model-hlsadmarkers"></a>

Hls Ad Markers
+ `ADOBE`
+ `ELEMENTAL`
+ `ELEMENTAL_SCTE35`

### HlsAkamaiHttpTransferMode
<a name="channels-model-hlsakamaihttptransfermode"></a>

Hls Akamai Http Transfer Mode
+ `CHUNKED`
+ `NON_CHUNKED`

### HlsAkamaiSettings
<a name="channels-model-hlsakamaisettings"></a>

Hls Akamai Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| httpTransferMode | [HlsAkamaiHttpTransferMode](#channels-model-hlsakamaihttptransfermode) | False | Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |
| salt | string | False | Salt for authenticated Akamai. |
| token | string | False | Token parameter for authenticated akamai. If not specified, \_gda\_ is used. |

### HlsAutoSelect
<a name="channels-model-hlsautoselect"></a>

Hls Auto Select
+ `NO`
+ `OMIT`
+ `YES`

### HlsBasicPutSettings
<a name="channels-model-hlsbasicputsettings"></a>

Hls Basic Put Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HlsCaptionLanguageSetting
<a name="channels-model-hlscaptionlanguagesetting"></a>

Hls Caption Language Setting
+ `INSERT`
+ `NONE`
+ `OMIT`

### HlsCdnSettings
<a name="channels-model-hlscdnsettings"></a>

Hls Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsAkamaiSettings | [HlsAkamaiSettings](#channels-model-hlsakamaisettings) | False |  |
| hlsBasicPutSettings | [HlsBasicPutSettings](#channels-model-hlsbasicputsettings) | False |  |
| hlsMediaStoreSettings | [HlsMediaStoreSettings](#channels-model-hlsmediastoresettings) | False |  |
| hlsS3Settings | [HlsS3Settings](#channels-model-hlss3settings) | False |  |
| hlsWebdavSettings | [HlsWebdavSettings](#channels-model-hlswebdavsettings) | False |  |

### HlsClientCache
<a name="channels-model-hlsclientcache"></a>

Hls Client Cache
+ `DISABLED`
+ `ENABLED`

### HlsCodecSpecification
<a name="channels-model-hlscodecspecification"></a>

Hls Codec Specification
+ `RFC_4281`
+ `RFC_6381`

### HlsDefault
<a name="channels-model-hlsdefault"></a>

Hls Default
+ `NO`
+ `OMIT`
+ `YES`

### HlsDirectoryStructure
<a name="channels-model-hlsdirectorystructure"></a>

Hls Directory Structure
+ `SINGLE_DIRECTORY`
+ `SUBDIRECTORY_PER_STREAM`

### HlsDiscontinuityTags
<a name="channels-model-hlsdiscontinuitytags"></a>

Hls Discontinuity Tags
+ `INSERT`
+ `NEVER_INSERT`

### HlsEncryptionType
<a name="channels-model-hlsencryptiontype"></a>

Hls Encryption Type
+ `AES128`
+ `SAMPLE_AES`

### HlsGroupSettings
<a name="channels-model-hlsgroupsettings"></a>

Hls Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | Array of type [HlsAdMarkers](#channels-model-hlsadmarkers) | False | Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs. |
| baseUrlContent | string | False | A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file. |
| baseUrlContent1 | string | False | Optional. One value per output group. This field is required only if you are completing Base URL content A, and the downstream system has notified you that the media files for pipeline 1 of all outputs are in a location different from the media files for pipeline 0. |
| baseUrlManifest | string | False | A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file. |
| baseUrlManifest1 | string | False | Optional. One value per output group. Complete this field only if you are completing Base URL manifest A, and the downstream system has notified you that the child manifest files for pipeline 1 of all outputs are in a location different from the child manifest files for pipeline 0. |
| captionLanguageMappings | Array of type [CaptionLanguageMapping](#channels-model-captionlanguagemapping) | False | Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to "insert". |
| captionLanguageSetting | [HlsCaptionLanguageSetting](#channels-model-hlscaptionlanguagesetting) | False | Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest. |
| clientCache | [HlsClientCache](#channels-model-hlsclientcache) | False | When set to "disabled", sets the \#EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay. |
| codecSpecification | [HlsCodecSpecification](#channels-model-hlscodecspecification) | False | Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation. |
| constantIv | string<br />MinLength: 32<br />MaxLength: 32 | False | For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to "explicit" then this parameter is required and is used as the IV for encryption. |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled). |
| directoryStructure | [HlsDirectoryStructure](#channels-model-hlsdirectorystructure) | False | Place segments in subdirectories. |
| discontinuityTags | [HlsDiscontinuityTags](#channels-model-hlsdiscontinuitytags) | False | Specifies whether to insert EXT-X-DISCONTINUITY tags in the HLS child manifests for this output group. Typically, choose Insert because these tags are required in the manifest (according to the HLS specification) and serve an important purpose. Choose Never Insert only if the downstream system is doing real-time failover (without using the MediaLive automatic failover feature) and only if that downstream system has advised you to exclude the tags. |
| encryptionType | [HlsEncryptionType](#channels-model-hlsencryptiontype) | False | Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired. |
| hlsCdnSettings | [HlsCdnSettings](#channels-model-hlscdnsettings) | False | Parameters that control interactions with the CDN. |
| hlsId3SegmentTagging | [HlsId3SegmentTaggingState](#channels-model-hlsid3segmenttaggingstate) | False | State of HLS ID3 Segment Tagging |
| iFrameOnlyPlaylists | [IFrameOnlyPlaylistType](#channels-model-iframeonlyplaylisttype) | False | DISABLED: Do not create an I-frame-only manifest, but do create the master and media manifests (according to the Output Selection field). STANDARD: Create an I-frame-only manifest for each output that contains video, as well as the other manifests (according to the Output Selection field). The I-frame manifest contains a \#EXT-X-I-FRAMES-ONLY tag to indicate it is I-frame only, and one or more \#EXT-X-BYTERANGE entries identifying the I-frame position. For example, \#EXT-X-BYTERANGE:160364@1461888" |
| incompleteSegmentBehavior | [HlsIncompleteSegmentBehavior](#channels-model-hlsincompletesegmentbehavior) | False | Specifies whether to include the final (incomplete) segment in the media output when the pipeline stops producing output because of a channel stop, a channel pause or a loss of input to the pipeline. Auto means that MediaLive decides whether to include the final segment, depending on the channel class and the types of output groups. Suppress means to never include the incomplete segment. We recommend you choose Auto and let MediaLive control the behavior. |
| indexNSegments | integer<br />Minimum: 3 | False | Applies only if Mode field is LIVE. Specifies the maximum number of segments in the media manifest file. After this maximum, older segments are removed from the media manifest. This number must be smaller than the number in the Keep Segments field. |
| inputLossAction | [InputLossActionForHlsOut](#channels-model-inputlossactionforhlsout) | False | Parameter that control output group behavior on input loss. |
| ivInManifest | [HlsIvInManifest](#channels-model-hlsivinmanifest) | False | For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to "include", IV is listed in the manifest, otherwise the IV is not in the manifest. |
| ivSource | [HlsIvSource](#channels-model-hlsivsource) | False | For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is "followsSegmentNumber", it will cause the IV to change every segment (to match the segment number). If this is set to "explicit", you must enter a constantIv value. |
| keepSegments | integer<br />Minimum: 1 | False | Applies only if Mode field is LIVE. Specifies the number of media segments to retain in the destination directory. This number should be bigger than indexNSegments (Num segments). We recommend (value = (2 x indexNsegments) \+ 1). If this "keep segments" number is too low, the following might happen: the player is still reading a media manifest file that lists this segment, but that segment has been removed from the destination directory (as directed by indexNSegments). This situation would result in a 404 HTTP error on the player. |
| keyFormat | string | False | The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of "identity" is used. A reverse DNS string can also be given. |
| keyFormatVersions | string | False | Either a single positive integer version value or a slash delimited list of version values (1/2/3). |
| keyProviderSettings | [KeyProviderSettings](#channels-model-keyprovidersettings) | False | The key provider settings. |
| manifestCompression | [HlsManifestCompression](#channels-model-hlsmanifestcompression) | False | When set to gzip, compresses HLS playlist. |
| manifestDurationFormat | [HlsManifestDurationFormat](#channels-model-hlsmanifestdurationformat) | False | Indicates whether the output manifest should use floating point or integer values for segment duration. |
| minSegmentLength | integer<br />Minimum: 0 | False | When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed. |
| mode | [HlsMode](#channels-model-hlsmode) | False | If "vod", all segments are indexed and kept permanently in the destination and manifest. If "live", only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a "VOD" type manifest on completion of the stream. |
| outputSelection | [HlsOutputSelection](#channels-model-hlsoutputselection) | False | MANIFESTS\_AND\_SEGMENTS: Generates manifests (master manifest, if applicable, and media manifests) for this output group. VARIANT\_MANIFESTS\_AND\_SEGMENTS: Generates media manifests for this output group, but not a master manifest. SEGMENTS\_ONLY: Does not generate any manifests for this output group. |
| programDateTime | [HlsProgramDateTime](#channels-model-hlsprogramdatetime) | False | Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset. |
| programDateTimeClock | [HlsProgramDateTimeClock](#channels-model-hlsprogramdatetimeclock) | False | Specifies the algorithm used to drive the HLS EXT-X-PROGRAM-DATE-TIME clock. Options include: INITIALIZE\_FROM\_OUTPUT\_TIMECODE: The PDT clock is initialized as a function of the first output timecode, then incremented by the EXTINF duration of each encoded segment. SYSTEM\_CLOCK: The PDT clock is initialized as a function of the UTC wall clock, then incremented by the EXTINF duration of each encoded segment. If the PDT clock diverges from the wall clock by more than 500ms, it is resynchronized to the wall clock. |
| programDateTimePeriod | integer<br />Minimum: 0<br />Maximum: 3600 | False | Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds. |
| redundantManifest | [HlsRedundantManifest](#channels-model-hlsredundantmanifest) | False | ENABLED: The master manifest (.m3u8 file) for each pipeline includes information about both pipelines: first its own media files, then the media files of the other pipeline. This feature allows playout device that support stale manifest detection to switch from one manifest to the other, when the current manifest seems to be stale. There are still two destinations and two master manifests, but both master manifests reference the media files from both pipelines. DISABLED: The master manifest (.m3u8 file) for each pipeline includes information about its own pipeline only. For an HLS output group with MediaPackage as the destination, the DISABLED behavior is always followed. MediaPackage regenerates the manifests it serves to players so a redundant manifest from MediaLive is irrelevant. |
| segmentationMode | [HlsSegmentationMode](#channels-model-hlssegmentationmode) | False | useInputSegmentation has been deprecated. The configured segment size is always used. |
| segmentLength | integer<br />Minimum: 1 | False | Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer. |
| segmentsPerSubdirectory | integer<br />Minimum: 1 | False | Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect. |
| streamInfResolution | [HlsStreamInfResolution](#channels-model-hlsstreaminfresolution) | False | Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest. |
| timedMetadataId3Frame | [HlsTimedMetadataId3Frame](#channels-model-hlstimedmetadataid3frame) | False | Indicates ID3 frame that has the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0 | False | Timed Metadata interval in seconds. |
| timestampDeltaMilliseconds | integer<br />Minimum: 0 | False | Provides an extra millisecond delta offset to fine tune the timestamps. |
| tsFileMode | [HlsTsFileMode](#channels-model-hlstsfilemode) | False | SEGMENTED\_FILES: Emit the program as segments - multiple .ts media files. SINGLE\_FILE: Applies only if Mode field is VOD. Emit the program as a single .ts media file. The media manifest includes \#EXT-X-BYTERANGE tags to index segments for playback. A typical use for this value is when sending the output to AWS Elemental MediaConvert, which can accept only a single media file. Playback while the channel is running is not guaranteed due to HTTP server caching. |

### HlsH265PackagingType
<a name="channels-model-hlsh265packagingtype"></a>

Hls H265 Packaging Type
+ `HEV1`
+ `HVC1`

### HlsId3SegmentTaggingState
<a name="channels-model-hlsid3segmenttaggingstate"></a>

State of HLS ID3 Segment Tagging
+ `DISABLED`
+ `ENABLED`

### HlsIncompleteSegmentBehavior
<a name="channels-model-hlsincompletesegmentbehavior"></a>

Hls Incomplete Segment Behavior
+ `AUTO`
+ `SUPPRESS`

### HlsInputSettings
<a name="channels-model-hlsinputsettings"></a>

Hls Input Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bandwidth | integer<br />Minimum: 0 | False | When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest. |
| bufferSegments | integer<br />Minimum: 0 | False | When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8. |
| retries | integer<br />Minimum: 0 | False | The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable. |
| retryInterval | integer<br />Minimum: 0 | False | The number of seconds between retries when an attempt to read a manifest or segment fails. |
| scte35Source | [HlsScte35SourceType](#channels-model-hlsscte35sourcetype) | False | Identifies the source for the SCTE-35 messages that MediaLive will ingest. Messages can be ingested from the content segments (in the stream) or from tags in the playlist (the HLS manifest). MediaLive ignores SCTE-35 information in the source that is not selected. |

### HlsIvInManifest
<a name="channels-model-hlsivinmanifest"></a>

Hls Iv In Manifest
+ `EXCLUDE`
+ `INCLUDE`

### HlsIvSource
<a name="channels-model-hlsivsource"></a>

Hls Iv Source
+ `EXPLICIT`
+ `FOLLOWS_SEGMENT_NUMBER`

### HlsManifestCompression
<a name="channels-model-hlsmanifestcompression"></a>

Hls Manifest Compression
+ `GZIP`
+ `NONE`

### HlsManifestDurationFormat
<a name="channels-model-hlsmanifestdurationformat"></a>

Hls Manifest Duration Format
+ `FLOATING_POINT`
+ `INTEGER`

### HlsMediaStoreSettings
<a name="channels-model-hlsmediastoresettings"></a>

Hls Media Store Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| mediaStoreStorageClass | [HlsMediaStoreStorageClass](#channels-model-hlsmediastorestorageclass) | False | When set to temporal, output files are stored in non-persistent memory for faster reading and writing. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HlsMediaStoreStorageClass
<a name="channels-model-hlsmediastorestorageclass"></a>

Hls Media Store Storage Class
+ `TEMPORAL`

### HlsMode
<a name="channels-model-hlsmode"></a>

Hls Mode
+ `LIVE`
+ `VOD`

### HlsOutputSelection
<a name="channels-model-hlsoutputselection"></a>

Hls Output Selection
+ `MANIFESTS_AND_SEGMENTS`
+ `SEGMENTS_ONLY`
+ `VARIANT_MANIFESTS_AND_SEGMENTS`

### HlsOutputSettings
<a name="channels-model-hlsoutputsettings"></a>

Hls Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| h265PackagingType | [HlsH265PackagingType](#channels-model-hlsh265packagingtype) | False | Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1. |
| hlsSettings | [HlsSettings](#channels-model-hlssettings) | True | Settings regarding the underlying stream. These settings are different for audio-only outputs. |
| nameModifier | string<br />MinLength: 1 | False | String concatenated to the end of the destination filename. Accepts \\"Format Identifiers\\":\#formatIdentifierParameters. |
| segmentModifier | string | False | String concatenated to end of segment filenames. |

### HlsProgramDateTime
<a name="channels-model-hlsprogramdatetime"></a>

Hls Program Date Time
+ `EXCLUDE`
+ `INCLUDE`

### HlsProgramDateTimeClock
<a name="channels-model-hlsprogramdatetimeclock"></a>

Hls Program Date Time Clock
+ `INITIALIZE_FROM_OUTPUT_TIMECODE`
+ `SYSTEM_CLOCK`

### HlsRedundantManifest
<a name="channels-model-hlsredundantmanifest"></a>

Hls Redundant Manifest
+ `DISABLED`
+ `ENABLED`

### HlsS3LogUploads
<a name="channels-model-hlss3loguploads"></a>

Hls S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### HlsS3Settings
<a name="channels-model-hlss3settings"></a>

Hls S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [HlsS3LogUploads](#channels-model-hlss3loguploads) | False | When set to enabled, each fragment upload to CDN or server will be logged. |

### HlsScte35SourceType
<a name="channels-model-hlsscte35sourcetype"></a>

Hls Scte35 Source Type
+ `MANIFEST`
+ `SEGMENTS`

### HlsSegmentationMode
<a name="channels-model-hlssegmentationmode"></a>

Hls Segmentation Mode
+ `USE_INPUT_SEGMENTATION`
+ `USE_SEGMENT_DURATION`

### HlsSettings
<a name="channels-model-hlssettings"></a>

Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioOnlyHlsSettings | [AudioOnlyHlsSettings](#channels-model-audioonlyhlssettings) | False |  |
| fmp4HlsSettings | [Fmp4HlsSettings](#channels-model-fmp4hlssettings) | False |  |
| frameCaptureHlsSettings | [FrameCaptureHlsSettings](#channels-model-framecapturehlssettings) | False |  |
| standardHlsSettings | [StandardHlsSettings](#channels-model-standardhlssettings) | False |  |

### HlsStreamInfResolution
<a name="channels-model-hlsstreaminfresolution"></a>

Hls Stream Inf Resolution
+ `EXCLUDE`
+ `INCLUDE`

### HlsTimedMetadataId3Frame
<a name="channels-model-hlstimedmetadataid3frame"></a>

Hls Timed Metadata Id3 Frame
+ `NONE`
+ `PRIV`
+ `TDRL`

### HlsTsFileMode
<a name="channels-model-hlstsfilemode"></a>

Hls Ts File Mode
+ `SEGMENTED_FILES`
+ `SINGLE_FILE`

### HlsWebdavHttpTransferMode
<a name="channels-model-hlswebdavhttptransfermode"></a>

Hls Webdav Http Transfer Mode
+ `CHUNKED`
+ `NON_CHUNKED`

### HlsWebdavSettings
<a name="channels-model-hlswebdavsettings"></a>

Hls Webdav Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| httpTransferMode | [HlsWebdavHttpTransferMode](#channels-model-hlswebdavhttptransfermode) | False | Specify whether or not to use chunked transfer encoding to WebDAV. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HtmlMotionGraphicsSettings
<a name="channels-model-htmlmotiongraphicssettings"></a>

Html Motion Graphics Settings

### IFrameOnlyPlaylistType
<a name="channels-model-iframeonlyplaylisttype"></a>

When set to "standard", an I-Frame only playlist will be written out for each video output in the output group. This I-Frame only playlist will contain byte range offsets pointing to the I-frame(s) in each segment.
+ `DISABLED`
+ `STANDARD`

### IncludeFillerNalUnits
<a name="channels-model-includefillernalunits"></a>

Include Filler Nal Units
+ `AUTO`
+ `DROP`
+ `INCLUDE`

### InferenceSettings
<a name="channels-model-inferencesettings"></a>

Contains the AWS Elemental Inference settings for a channel: the Amazon Resource Name (ARN) of the associated feed, the audio feed inputs, and the enrichment methods that augment channel output with contextual metadata.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioFeedInputs | Array of type [AudioFeedInput](#channels-model-audiofeedinput) | False | A list of audio feed inputs that map audio selectors in the channel to feed inputs on the associated AWS Elemental Inference feed. |
| enrichmentMethods | Array of type [EnrichmentMethod](#channels-model-enrichmentmethod) | False | The Contextual Metadata Enrichment methods enabled for this channel. Each method defines how the channel augments its output with contextual metadata from the Elemental Inference feed. Valid values:+ `SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS` – Enriches outbound SCTE-35 messages with query parameters that downstream systems can use to call the Elemental Inference GetMetadata API. |
| feedArn | string | False | The Amazon Resource Name (ARN) of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service. |

### InputAttachment
<a name="channels-model-inputattachment"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| automaticInputFailoverSettings | [AutomaticInputFailoverSettings](#channels-model-automaticinputfailoversettings) | False | User-specified settings for defining what the conditions are for declaring the input unhealthy and failing over to a different input. |
| inputAttachmentName | string | False | User-specified name for the attachment. This is required if the user wants to use this input in an input switch action. |
| inputId | string | False | The ID of the input |
| inputSettings | [InputSettings](#channels-model-inputsettings) | False | Settings of an input (caption selector, etc.) |
| logicalInterfaceNames | Array of type string | False | Optional assignment of an input to a logical interface on the Node. Only applies to on premises channels. |

### InputChannelLevel
<a name="channels-model-inputchannellevel"></a>

Input Channel Level

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| gain | integer<br />Minimum: -60<br />Maximum: 6 | True | Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB. |
| inputChannel | integer<br />Minimum: 0<br />Maximum: 15 | True | The index of the input channel used as a source. |

### InputCodec
<a name="channels-model-inputcodec"></a>

codec in increasing order of complexity
+ `MPEG2`
+ `AVC`
+ `HEVC`

### InputDeblockFilter
<a name="channels-model-inputdeblockfilter"></a>

Input Deblock Filter
+ `DISABLED`
+ `ENABLED`

### InputDenoiseFilter
<a name="channels-model-inputdenoisefilter"></a>

Input Denoise Filter
+ `DISABLED`
+ `ENABLED`

### InputFilter
<a name="channels-model-inputfilter"></a>

Input Filter
+ `AUTO`
+ `DISABLED`
+ `FORCED`

### InputLocation
<a name="channels-model-inputlocation"></a>

Input Location

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | key used to extract the password from EC2 Parameter store |
| uri | string<br />MaxLength: 2048 | True | Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live". |
| username | string | False | Username if credentials are required to access a file or publishing point. This can be either a plaintext username, or a reference to an AWS parameter store name from which the username can be retrieved. AWS Parameter store format: "ssm://<parameter name>" |

### InputLossActionForHlsOut
<a name="channels-model-inputlossactionforhlsout"></a>

Input Loss Action For Hls Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForMsSmoothOut
<a name="channels-model-inputlossactionformssmoothout"></a>

Input Loss Action For Ms Smooth Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForRtmpOut
<a name="channels-model-inputlossactionforrtmpout"></a>

Input Loss Action For Rtmp Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForUdpOut
<a name="channels-model-inputlossactionforudpout"></a>

Input Loss Action For Udp Out
+ `DROP_PROGRAM`
+ `DROP_TS`
+ `EMIT_PROGRAM`

### InputLossBehavior
<a name="channels-model-inputlossbehavior"></a>

Input Loss Behavior

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackFrameMsec | integer<br />Minimum: 0<br />Maximum: 1000000 | False | On input loss, the number of milliseconds to substitute black into the output before switching to the frame specified by inputLossImageType. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000 will be interpreted as infinite. |
| inputLossImageColor | string<br />MinLength: 6<br />MaxLength: 6 | False | When input loss image type is "color" this field specifies the color to use. Value: 6 hex characters representing the values of RGB. |
| inputLossImageSlate | [InputLocation](#channels-model-inputlocation) | False | When input loss image type is "slate" these fields specify the parameters for accessing the slate. |
| inputLossImageType | [InputLossImageType](#channels-model-inputlossimagetype) | False | Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec. |
| repeatFrameMsec | integer<br />Minimum: 0<br />Maximum: 1000000 | False | On input loss, the number of milliseconds to repeat the previous picture before substituting black into the output. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000 will be interpreted as infinite. |

### InputLossFailoverSettings
<a name="channels-model-inputlossfailoversettings"></a>

MediaLive will perform a failover if content is not detected in this input for the specified period.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputLossThresholdMsec | integer<br />Minimum: 100 | False | The amount of time (in milliseconds) that no input is detected. After that time, an input failover will occur. |

### InputLossImageType
<a name="channels-model-inputlossimagetype"></a>

Input Loss Image Type
+ `COLOR`
+ `SLATE`

### InputMaximumBitrate
<a name="channels-model-inputmaximumbitrate"></a>

Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are supported currently.
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### InputPreference
<a name="channels-model-inputpreference"></a>

Input preference when deciding which input to make active when a previously failed input has recovered. If \\"EQUAL\_INPUT\_PREFERENCE\\", then the active input will stay active as long as it is healthy. If \\"PRIMARY\_INPUT\_PREFERRED\\", then always switch back to the primary input when it is healthy.
+ `EQUAL_INPUT_PREFERENCE`
+ `PRIMARY_INPUT_PREFERRED`

### InputResolution
<a name="channels-model-inputresolution"></a>

Input resolution based on lines of vertical resolution in the input; SD is less than 720 lines, HD is 720 to 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `UHD`

### InputSettings
<a name="channels-model-inputsettings"></a>

Live Event input parameters. There can be multiple inputs in a single Live Event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectors | Array of type [AudioSelector](#channels-model-audioselector) | False | Used to select the audio stream to decode for inputs that have multiple available. |
| captionSelectors | Array of type [CaptionSelector](#channels-model-captionselector) | False | Used to select the caption input to use for inputs that have multiple available. |
| deblockFilter | [InputDeblockFilter](#channels-model-inputdeblockfilter) | False | Enable or disable the deblock filter when filtering. |
| denoiseFilter | [InputDenoiseFilter](#channels-model-inputdenoisefilter) | False | Enable or disable the denoise filter when filtering. |
| filterStrength | integer<br />Minimum: 1<br />Maximum: 5 | False | Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest). |
| inputFilter | [InputFilter](#channels-model-inputfilter) | False | Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type |
| networkInputSettings | [NetworkInputSettings](#channels-model-networkinputsettings) | False | Input settings. |
| scte35Pid | integer<br />Minimum: 32<br />Maximum: 8191 | False | PID from which to read SCTE-35 messages. If left undefined, EML will select the first SCTE-35 PID found in the input. |
| smpte2038DataPreference | [Smpte2038DataPreference](#channels-model-smpte2038datapreference) | False | Specifies whether to extract applicable ancillary data from a SMPTE-2038 source in this input. Applicable data types are captions, timecode, AFD, and SCTE-104 messages. - PREFER: Extract from SMPTE-2038 if present in this input, otherwise extract from another source (if any). - IGNORE: Never extract any ancillary data from SMPTE-2038. |
| sourceEndBehavior | [InputSourceEndBehavior](#channels-model-inputsourceendbehavior) | False | Loop input if it is a file. This allows a file input to be streamed indefinitely. |
| videoSelector | [VideoSelector](#channels-model-videoselector) | False | Informs which video elementary stream to decode for input types that have multiple available. |

### InputSourceEndBehavior
<a name="channels-model-inputsourceendbehavior"></a>

Input Source End Behavior
+ `CONTINUE`
+ `LOOP`

### InputSpecification
<a name="channels-model-inputspecification"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| codec | [InputCodec](#channels-model-inputcodec) | False | Input codec |
| maximumBitrate | [InputMaximumBitrate](#channels-model-inputmaximumbitrate) | False | Maximum input bitrate, categorized coarsely |
| resolution | [InputResolution](#channels-model-inputresolution) | False | Input resolution, categorized coarsely |

### InternalServiceError
<a name="channels-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="channels-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### KeyProviderSettings
<a name="channels-model-keyprovidersettings"></a>

Key Provider Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| staticKeySettings | [StaticKeySettings](#channels-model-statickeysettings) | False |  |

### LimitExceeded
<a name="channels-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LinkedChannelSettings
<a name="channels-model-linkedchannelsettings"></a>

Configuration for linked channel relationships

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| followerChannelSettings | [FollowerChannelSettings](#channels-model-followerchannelsettings) | False |  |
| primaryChannelSettings | [PrimaryChannelSettings](#channels-model-primarychannelsettings) | False |  |

### LinkedChannelType
<a name="channels-model-linkedchanneltype"></a>

The values for the role for a linked channel.
+ `FOLLOWING_CHANNEL`
+ `PRIMARY_CHANNEL`

### ListChannelsResultModel
<a name="channels-model-listchannelsresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | Array of type [ChannelSummary](#channels-model-channelsummary) | False |  |
| nextToken | string | False |  |

### LogLevel
<a name="channels-model-loglevel"></a>

The log level the user wants for their channel.
+ `ERROR`
+ `WARNING`
+ `INFO`
+ `DEBUG`
+ `DISABLED`

### M2tsAbsentInputAudioBehavior
<a name="channels-model-m2tsabsentinputaudiobehavior"></a>

M2ts Absent Input Audio Behavior
+ `DROP`
+ `ENCODE_SILENCE`

### M2tsArib
<a name="channels-model-m2tsarib"></a>

M2ts Arib
+ `DISABLED`
+ `ENABLED`

### M2tsAribCaptionsPidControl
<a name="channels-model-m2tsaribcaptionspidcontrol"></a>

M2ts Arib Captions Pid Control
+ `AUTO`
+ `USE_CONFIGURED`

### M2tsAudioBufferModel
<a name="channels-model-m2tsaudiobuffermodel"></a>

M2ts Audio Buffer Model
+ `ATSC`
+ `DVB`

### M2tsAudioInterval
<a name="channels-model-m2tsaudiointerval"></a>

M2ts Audio Interval
+ `VIDEO_AND_FIXED_INTERVALS`
+ `VIDEO_INTERVAL`

### M2tsAudioStreamType
<a name="channels-model-m2tsaudiostreamtype"></a>

M2ts Audio Stream Type
+ `ATSC`
+ `DVB`

### M2tsBufferModel
<a name="channels-model-m2tsbuffermodel"></a>

M2ts Buffer Model
+ `MULTIPLEX`
+ `NONE`

### M2tsCcDescriptor
<a name="channels-model-m2tsccdescriptor"></a>

M2ts Cc Descriptor
+ `DISABLED`
+ `ENABLED`

### M2tsEbifControl
<a name="channels-model-m2tsebifcontrol"></a>

M2ts Ebif Control
+ `NONE`
+ `PASSTHROUGH`

### M2tsEbpPlacement
<a name="channels-model-m2tsebpplacement"></a>

M2ts Ebp Placement
+ `VIDEO_AND_AUDIO_PIDS`
+ `VIDEO_PID`

### M2tsEsRateInPes
<a name="channels-model-m2tsesrateinpes"></a>

M2ts Es Rate In Pes
+ `EXCLUDE`
+ `INCLUDE`

### M2tsKlv
<a name="channels-model-m2tsklv"></a>

M2ts Klv
+ `NONE`
+ `PASSTHROUGH`

### M2tsNielsenId3Behavior
<a name="channels-model-m2tsnielsenid3behavior"></a>

M2ts Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M2tsPcrControl
<a name="channels-model-m2tspcrcontrol"></a>

M2ts Pcr Control
+ `CONFIGURED_PCR_PERIOD`
+ `PCR_EVERY_PES_PACKET`

### M2tsRateMode
<a name="channels-model-m2tsratemode"></a>

M2ts Rate Mode
+ `CBR`
+ `VBR`

### M2tsScte35Control
<a name="channels-model-m2tsscte35control"></a>

M2ts Scte35 Control
+ `NONE`
+ `PASSTHROUGH`
+ `SCTE_35_WITHOUT_IDR`

### M2tsSegmentationMarkers
<a name="channels-model-m2tssegmentationmarkers"></a>

M2ts Segmentation Markers
+ `EBP`
+ `EBP_LEGACY`
+ `NONE`
+ `PSI_SEGSTART`
+ `RAI_ADAPT`
+ `RAI_SEGSTART`

### M2tsSegmentationStyle
<a name="channels-model-m2tssegmentationstyle"></a>

M2ts Segmentation Style
+ `MAINTAIN_CADENCE`
+ `RESET_CADENCE`

### M2tsSettings
<a name="channels-model-m2tssettings"></a>

M2ts Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| absentInputAudioBehavior | [M2tsAbsentInputAudioBehavior](#channels-model-m2tsabsentinputaudiobehavior) | False | When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream. |
| arib | [M2tsArib](#channels-model-m2tsarib) | False | When set to enabled, uses ARIB-compliant field muxing and removes video descriptor. |
| aribCaptionsPid | string | False | Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| aribCaptionsPidControl | [M2tsAribCaptionsPidControl](#channels-model-m2tsaribcaptionspidcontrol) | False | If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number. |
| audioBufferModel | [M2tsAudioBufferModel](#channels-model-m2tsaudiobuffermodel) | False | When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used. |
| audioFramesPerPes | integer<br />Minimum: 0 | False | The number of audio frames to insert for each PES packet. |
| audioPids | string | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| audioStreamType | [M2tsAudioStreamType](#channels-model-m2tsaudiostreamtype) | False | When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06. |
| bitrate | integer<br />Minimum: 0 | False | The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. |
| bufferModel | [M2tsBufferModel](#channels-model-m2tsbuffermodel) | False | Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices. |
| ccDescriptor | [M2tsCcDescriptor](#channels-model-m2tsccdescriptor) | False | When set to enabled, generates captionServiceDescriptor in PMT. |
| dvbNitSettings | [DvbNitSettings](#channels-model-dvbnitsettings) | False | Inserts DVB Network Information Table (NIT) at the specified table repetition interval. |
| dvbSdtSettings | [DvbSdtSettings](#channels-model-dvbsdtsettings) | False | Inserts DVB Service Description Table (SDT) at the specified table repetition interval. |
| dvbSubPids | string | False | Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| dvbTdtSettings | [DvbTdtSettings](#channels-model-dvbtdtsettings) | False | Inserts DVB Time and Date Table (TDT) at the specified table repetition interval. |
| dvbTeletextPid | string | False | Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| ebif | [M2tsEbifControl](#channels-model-m2tsebifcontrol) | False | If set to passthrough, passes any EBIF data from the input source to this output. |
| ebpAudioInterval | [M2tsAudioInterval](#channels-model-m2tsaudiointerval) | False | When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval. |
| ebpLookaheadMs | integer<br />Minimum: 0<br />Maximum: 10000 | False | When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate. |
| ebpPlacement | [M2tsEbpPlacement](#channels-model-m2tsebpplacement) | False | Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID. |
| ecmPid | string | False | This field is unused and deprecated. |
| esRateInPes | [M2tsEsRateInPes](#channels-model-m2tsesrateinpes) | False | Include or exclude the ES Rate field in the PES header. |
| etvPlatformPid | string | False | Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| etvSignalPid | string | False | Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| fragmentTime | number<br />Minimum: 0 | False | The length in seconds of each fragment. Only used with EBP markers. |
| klv | [M2tsKlv](#channels-model-m2tsklv) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| klvDataPids | string | False | Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| nielsenId3Behavior | [M2tsNielsenId3Behavior](#channels-model-m2tsnielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| nullPacketBitrate | number<br />Minimum: 0 | False | Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000. |
| pcrControl | [M2tsPcrControl](#channels-model-m2tspcrcontrol) | False | When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPeriod | integer<br />Minimum: 0<br />Maximum: 500 | False | Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream. |
| pcrPid | string | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000. |
| pmtPid | string | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| programNum | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| rateMode | [M2tsRateMode](#channels-model-m2tsratemode) | False | When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set. |
| scte27Pids | string | False | Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| scte35Control | [M2tsScte35Control](#channels-model-m2tsscte35control) | False | Optionally pass SCTE-35 signals from the input source to this output. |
| scte35Pid | string | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| scte35PrerollPullupMilliseconds | number<br />Minimum: 0<br />Maximum: 5000 | False | Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means don't add pullup (it doesn't mean set the preroll to zero). Negative pullup is not supported, which means that you can't make the preroll shorter. Be aware that latency in the output will increase by the pullup amount. |
| segmentationMarkers | [M2tsSegmentationMarkers](#channels-model-m2tssegmentationmarkers) | False | Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format. |
| segmentationStyle | [M2tsSegmentationStyle](#channels-model-m2tssegmentationstyle) | False | The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule. |
| segmentationTime | number<br />Minimum: 1 | False | The length in seconds of each segment. Required unless markers is set to \_none\_. |
| timedMetadataBehavior | [M2tsTimedMetadataBehavior](#channels-model-m2tstimedmetadatabehavior) | False | When set to passthrough, timed metadata will be passed through from input to output. |
| timedMetadataPid | string | False | Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | string | False | Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |

### M2tsTimedMetadataBehavior
<a name="channels-model-m2tstimedmetadatabehavior"></a>

M2ts Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8KlvBehavior
<a name="channels-model-m3u8klvbehavior"></a>

M3u8 Klv Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8NielsenId3Behavior
<a name="channels-model-m3u8nielsenid3behavior"></a>

M3u8 Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8PcrControl
<a name="channels-model-m3u8pcrcontrol"></a>

M3u8 Pcr Control
+ `CONFIGURED_PCR_PERIOD`
+ `PCR_EVERY_PES_PACKET`

### M3u8Scte35Behavior
<a name="channels-model-m3u8scte35behavior"></a>

M3u8 Scte35 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8Settings
<a name="channels-model-m3u8settings"></a>

Settings information for the .m3u8 container

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioFramesPerPes | integer<br />Minimum: 0 | False | The number of audio frames to insert for each PES packet. |
| audioPids | string | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. |
| ecmPid | string | False | This parameter is unused and deprecated. |
| klvBehavior | [M3u8KlvBehavior](#channels-model-m3u8klvbehavior) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| klvDataPids | string | False | Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| nielsenId3Behavior | [M3u8NielsenId3Behavior](#channels-model-m3u8nielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. A value of \\"0\\" writes out the PMT once per segment file. |
| pcrControl | [M3u8PcrControl](#channels-model-m3u8pcrcontrol) | False | When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPeriod | integer<br />Minimum: 0<br />Maximum: 500 | False | Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream. |
| pcrPid | string | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. A value of \\"0\\" writes out the PMT once per segment file. |
| pmtPid | string | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. |
| programNum | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| scte35Behavior | [M3u8Scte35Behavior](#channels-model-m3u8scte35behavior) | False | If set to passthrough, passes any SCTE-35 signals from the input source to this output. |
| scte35Pid | string | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. |
| timedMetadataBehavior | [M3u8TimedMetadataBehavior](#channels-model-m3u8timedmetadatabehavior) | False | When set to passthrough, timed metadata is passed through from input to output. |
| timedMetadataPid | string | False | Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | string | False | Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. |

### M3u8TimedMetadataBehavior
<a name="channels-model-m3u8timedmetadatabehavior"></a>

M3u8 Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### MaintenanceCreateSettings
<a name="channels-model-maintenancecreatesettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maintenanceDay | [MaintenanceDay](#channels-model-maintenanceday) | False | Choose one day of the week for maintenance. The chosen day is used for all future maintenance windows. |
| maintenanceStartTime | string<br />Pattern: `^([0,1]?[0-9]\|2[0-3]):00$` | False | Choose the hour that maintenance will start. The chosen time is used for all future maintenance windows. |

### MaintenanceDay
<a name="channels-model-maintenanceday"></a>

The currently selected maintenance day.
+ `MONDAY`
+ `TUESDAY`
+ `WEDNESDAY`
+ `THURSDAY`
+ `FRIDAY`
+ `SATURDAY`
+ `SUNDAY`

### MaintenanceStatus
<a name="channels-model-maintenancestatus"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maintenanceDay | [MaintenanceDay](#channels-model-maintenanceday) | False | The currently selected maintenance day. |
| maintenanceDeadline | string<br />Format: string | False | Maintenance is required by the displayed date and time. Date and time is in ISO. |
| maintenanceScheduledDate | string<br />Format: string | False | The currently scheduled maintenance date and time. Date and time is in ISO. |
| maintenanceStartTime | string | False | The currently selected maintenance start time. Time is in UTC. |

### MediaConnectRouterContainerSettings
<a name="channels-model-mediaconnectroutercontainersettings"></a>

Media Connect Router Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| m2tsSettings | [M2tsSettings](#channels-model-m2tssettings) | False |  |

### MediaConnectRouterGroupSettings
<a name="channels-model-mediaconnectroutergroupsettings"></a>

Media Connect Router Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZones | Array of type string | False | The names of the Availability Zones in which to write output to MediaConnect Router. |

### MediaConnectRouterOutputConnectionMap
<a name="channels-model-mediaconnectrouteroutputconnectionmap"></a>

Map of MediaLive pipeline IDs to the ARNs of the MediaConnect Router Inputs to which this Output is connected.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pipeline0 | string | False | The ARN of the MediaConnect Router Input connected to pipeline 0. |
| pipeline1 | string | False | The ARN of the MediaConnect Router Input connected to pipeline 1. |

### MediaConnectRouterOutputDestinationSettings
<a name="channels-model-mediaconnectrouteroutputdestinationsettings"></a>

MediaConnect Router Output Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionType | [MediaConnectRouterOutputEncryptionType](#channels-model-mediaconnectrouteroutputencryptiontype) | False | Encryption configuration for MediaConnect router. When using SECRETS\_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead. |
| secretArn | string | False | ARN of the secret used to encrypt this input. Used only with the SECRETS\_MANAGER encryption type. |

### MediaConnectRouterOutputEncryptionType
<a name="channels-model-mediaconnectrouteroutputencryptiontype"></a>

Encryption configuration for MediaConnect router. When using SECRETS\_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead.
+ `AUTOMATIC`
+ `SECRETS_MANAGER`

### MediaConnectRouterOutputSettings
<a name="channels-model-mediaconnectrouteroutputsettings"></a>

Media Connect Router Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectedRouterInputs | [MediaConnectRouterOutputConnectionMap](#channels-model-mediaconnectrouteroutputconnectionmap) | False | This parameter is deprecated and unused. |
| containerSettings | [MediaConnectRouterContainerSettings](#channels-model-mediaconnectroutercontainersettings) | True |  |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | Destination for this MediaConnect Router Output. The referenced OutputDestination must have MediaConnect Router settings configured. |

### MediaPackageAdditionalDestinations
<a name="channels-model-mediapackageadditionaldestinations"></a>

Additional output destinations for a CMAF Ingest output group

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | The destination location |

### MediaPackageGroupSettings
<a name="channels-model-mediapackagegroupsettings"></a>

Media Package Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | MediaPackage channel destination. |
| mediapackageV2GroupSettings | [MediaPackageV2GroupSettings](#channels-model-mediapackagev2groupsettings) | False | Parameters that apply only if the destination parameter for the output group specifies a channelGroup and channelName. Using those two parameters indicates that the output group is for MediaPackage V2 (CMAF Ingest). |

### MediaPackageOutputDestinationSettings
<a name="channels-model-mediapackageoutputdestinationsettings"></a>

MediaPackage Output Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelEndpointId | string<br />MinLength: 1 | False | Endpoint 1 or 2 of the channel in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2. |
| channelGroup | string<br />MinLength: 1 | False | Name of the channel group in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2. |
| channelId | string<br />MinLength: 1 | False | ID of the channel in MediaPackage that is the destination for this output group. You do not need to specify the individual inputs in MediaPackage; MediaLive will handle the connection of the two MediaLive pipelines to the two MediaPackage inputs. The MediaPackage channel and MediaLive channel must be in the same region. |
| channelName | string<br />MinLength: 1 | False | Name of the channel in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2. |
| mediaPackageRegionName | string<br />MinLength: 1 | False | Region the channel group and channel are located in for MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2. |

### MediaPackageOutputSettings
<a name="channels-model-mediapackageoutputsettings"></a>

Media Package Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaPackageV2DestinationSettings | [MediaPackageV2DestinationSettings](#channels-model-mediapackagev2destinationsettings) | False | Settings that apply only when the destination is a MediaPackage V2 channel. |

### MediaPackageV2AbWatermarkerIrdetoSettings
<a name="channels-model-mediapackagev2abwatermarkerirdetosettings"></a>

A/B Watermarker settings for MediaPackage V2 output groups.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalDestinationsAlternateDestinations | Array of type [OutputLocationRef](#channels-model-outputlocationref) | False | The "B" pipeline renditions for the additional destinations. |
| alternateDestination | [OutputLocationRef](#channels-model-outputlocationref) | True | The "B" pipeline renditions for the main destination. |
| customProfile | [AbWatermarkingCustomProfile](#channels-model-abwatermarkingcustomprofile) | False | The vendor-provided custom profile values. |
| license | string | False | The name of the Secrets Manager secret containing the license file. |
| operatorId | integer<br />Minimum: 1<br />Maximum: 511 | True | The vendor-provided Operator ID. |
| polyPeriod | integer<br />Minimum: 1<br />Maximum: 1000 | False | The number of segments per watermarking bit. The total duration of the watermarking bit should be the LCM (least common multiple) of all segments sizes emitted by the downstream packager. |
| profile | [AbWatermarkingProfile](#channels-model-abwatermarkingprofile) | True | The vendor-provided profile choice. |
| watermarkIdLength | [AbWatermarkerIdLength](#channels-model-abwatermarkeridlength) | False | The number of bits that compose the watermarking identifier to be embedded. |

### MediaPackageV2CaptionLanguageSetting
<a name="channels-model-mediapackagev2captionlanguagesetting"></a>

The CLOSED-CAPTIONS signaling that AWS Elemental MediaPackage V2 writes into the HLS manifest it delivers. For the valid values, see the `captionLanguageSetting` field in `MediaPackageV2GroupSettings`.
+ `AUTO`
+ `NONE`

### MediaPackageV2DestinationSettings
<a name="channels-model-mediapackagev2destinationsettings"></a>

Settings for an output that is delivered to a MediaPackage V2 channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioGroupId | string | False | Applies only to an output that contains audio. If you want to put several audio encodes into one audio rendition group, decide on a name (ID) for the group. Then in every audio output that you want to belong to that group, enter that ID in this field. This information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage includes it in the manifest that it creates for the video player. |
| audioRenditionSets | string | False | Applies only to an output that contains video, and only if you want to associate one or more audio groups with this video. In this field, assign the groups that you created (in the Group ID fields in the various audio outputs). Enter one group ID, or enter a comma-separated list of group IDs. This information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage includes it in the manifest that it creates for the video player. |
| hlsAutoSelect | [HlsAutoSelect](#channels-model-hlsautoselect) | False | Specifies whether MediaPackage should set this output as the auto-select rendition in the HLS manifest. YES means this must be the auto-select. NO means this should never be the auto-select. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, follow these guidelines. You can set zero or one renditions to YES. You can set zero or more renditions to NO, but you can't set all renditions to NO. You can set zero, some, or all to OMIT. |
| hlsDefault | [HlsDefault](#channels-model-hlsdefault) | False | Specifies whether MediaPackage should set this output as the default rendition in the HLS manifest. YES means this must be the default. NO means this should never be the default. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, follow these guidelines. You can set zero or one renditions to YES. You can set zero or more renditions to NO, but you can't set all renditions to NO. You can set zero, some, or all to OMIT. |
| outputUsage | Array of type [OutputUsage](#channels-model-outputusage) | False | A list of usage tags that declare how this MediaPackage V2 output participates in multiview. Valid values:+ `MULTIVIEW_EQUAL_SIZE_VIEW` – The output is one of several equally sized views in the multiview layout.<br />+ `MULTIVIEW_PRIMARY_VIEW` – The output is the primary view in the multiview layout.<br />+ `MULTIVIEW_SECONDARY_VIEW` – The output is a secondary view in the multiview layout.<br />Leave this field empty (the default) if the output has no multiview role.<br />If any video-carrying MediaPackage V2 output in an output group specifies a multiview value, then every video-carrying MediaPackage V2 output in that group must also specify a multiview value. Put standalone video outputs in a separate output group. |

### MediaPackageV2GroupSettings
<a name="channels-model-mediapackagev2groupsettings"></a>

Contains the settings for a MediaPackage V2 output group, including SCTE-35 insertion behavior.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalDestinations | Array of type [MediaPackageAdditionalDestinations](#channels-model-mediapackageadditionaldestinations) | False | Optional an array of additional destinational HTTP destinations for the OutputGroup outputs |
| captionLanguageMappings | Array of type [CaptionLanguageMapping](#channels-model-captionlanguagemapping) | False | Mapping of up to 4 caption channels to caption languages. |
| captionLanguageSetting | [MediaPackageV2CaptionLanguageSetting](#channels-model-mediapackagev2captionlanguagesetting) | False | Applies only to 608 Embedded output captions. Controls the CLOSED-CAPTIONS signaling that AWS Elemental MediaPackage V2 writes into the HLS manifest it delivers. Valid values:+ `AUTO` – The default. If `captionLanguageMappings` is non-empty, the HLS manifest includes a CLOSED-CAPTIONS line for each mapped caption channel. If `captionLanguageMappings` is empty, the manifest omits the CLOSED-CAPTIONS line.<br />+ `NONE` – The HLS manifest carries CLOSED-CAPTIONS=NONE on each EXT-X-STREAM-INF tag. This signals to players that the stream has no closed captions, so players stop offering a CC track. You cannot combine `NONE` with a non-empty `captionLanguageMappings`. |
| id3Behavior | [CmafId3Behavior](#channels-model-cmafid3behavior) | False | Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule. |
| klvBehavior | [CmafKLVBehavior](#channels-model-cmafklvbehavior) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| nielsenId3Behavior | [CmafNielsenId3Behavior](#channels-model-cmafnielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| scte35Type | [Scte35Type](#channels-model-scte35type) | False | The SCTE-35 insertion behavior for this MediaPackage V2 output group. Valid values:+ `NONE` – The channel does not insert SCTE-35 messages.<br />+ `SCTE_35_WITHOUT_IDR` – The channel inserts SCTE-35 messages without an Instantaneous Decoder Refresh (IDR) frame at the cue point.<br />+ `SCTE_35_WITHOUT_SEGMENTATION` – The channel inserts SCTE-35 messages with an IDR frame, but without a new segment boundary.<br />If you don't specify a value, the channel doesn't insert SCTE-35 messages (`NONE`). |
| segmentLength | integer<br />Minimum: 1 | False | The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units. |
| segmentLengthUnits | [CmafIngestSegmentLengthUnits](#channels-model-cmafingestsegmentlengthunits) | False | Time unit for segment length parameter. |
| timedMetadataId3Frame | [CmafTimedMetadataId3Frame](#channels-model-cmaftimedmetadataid3frame) | False | Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0<br />Maximum: 10000 | False | If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds. |
| timedMetadataPassthrough | [CmafTimedMetadataPassthrough](#channels-model-cmaftimedmetadatapassthrough) | False | Set to enabled to pass through ID3 metadata from the input sources. |
| watermarkingSettings | [MediaPackageV2WatermarkingSettings](#channels-model-mediapackagev2watermarkingsettings) | False | Specifies the type of watermarking technology to use. |

### MediaPackageV2WatermarkingSettings
<a name="channels-model-mediapackagev2watermarkingsettings"></a>

A/B Watermarker settings for MediaPackage V2 output groups.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaPackageV2AbWatermarkerIrdetoSettings | [MediaPackageV2AbWatermarkerIrdetoSettings](#channels-model-mediapackagev2abwatermarkerirdetosettings) | False |  |

### MotionGraphicsConfiguration
<a name="channels-model-motiongraphicsconfiguration"></a>

Motion Graphics Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| motionGraphicsInsertion | [MotionGraphicsInsertion](#channels-model-motiongraphicsinsertion) | False |  |
| motionGraphicsSettings | [MotionGraphicsSettings](#channels-model-motiongraphicssettings) | True | Motion Graphics Settings |

### MotionGraphicsInsertion
<a name="channels-model-motiongraphicsinsertion"></a>

Motion Graphics Insertion
+ `DISABLED`
+ `ENABLED`

### MotionGraphicsSettings
<a name="channels-model-motiongraphicssettings"></a>

Motion Graphics Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| htmlMotionGraphicsSettings | [HtmlMotionGraphicsSettings](#channels-model-htmlmotiongraphicssettings) | False |  |

### Mp2CodingMode
<a name="channels-model-mp2codingmode"></a>

Mp2 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`

### Mp2Settings
<a name="channels-model-mp2settings"></a>

Mp2 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. |
| codingMode | [Mp2CodingMode](#channels-model-mp2codingmode) | False | The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo). |
| sampleRate | number | False | Sample rate in Hz. |

### Mpeg2AdaptiveQuantization
<a name="channels-model-mpeg2adaptivequantization"></a>

Mpeg2 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `LOW`
+ `MEDIUM`
+ `OFF`

### Mpeg2ColorMetadata
<a name="channels-model-mpeg2colormetadata"></a>

Mpeg2 Color Metadata
+ `IGNORE`
+ `INSERT`

### Mpeg2ColorSpace
<a name="channels-model-mpeg2colorspace"></a>

Mpeg2 Color Space
+ `AUTO`
+ `PASSTHROUGH`

### Mpeg2DisplayRatio
<a name="channels-model-mpeg2displayratio"></a>

Mpeg2 Display Ratio
+ `DISPLAYRATIO16X9`
+ `DISPLAYRATIO4X3`

### Mpeg2FilterSettings
<a name="channels-model-mpeg2filtersettings"></a>

Mpeg2 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| temporalFilterSettings | [TemporalFilterSettings](#channels-model-temporalfiltersettings) | False |  |

### Mpeg2GopSizeUnits
<a name="channels-model-mpeg2gopsizeunits"></a>

Mpeg2 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### Mpeg2ScanType
<a name="channels-model-mpeg2scantype"></a>

Mpeg2 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### Mpeg2Settings
<a name="channels-model-mpeg2settings"></a>

Mpeg2 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Mpeg2AdaptiveQuantization](#channels-model-mpeg2adaptivequantization) | False | Choose Off to disable adaptive quantization. Or choose another value to enable the quantizer and set its strength. The strengths are: Auto, Off, Low, Medium, High. When you enable this field, MediaLive allows intra-frame quantizers to vary, which might improve visual quality. |
| afdSignaling | [AfdSignaling](#channels-model-afdsignaling) | False | Indicates the AFD values that MediaLive will write into the video encode. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose AUTO. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: MediaLive will use the value you specify in fixedAFD. |
| colorMetadata | [Mpeg2ColorMetadata](#channels-model-mpeg2colormetadata) | False | Specifies whether to include the color space metadata. The metadata describes the color space that applies to the video (the colorSpace field). We recommend that you insert the metadata. |
| colorSpace | [Mpeg2ColorSpace](#channels-model-mpeg2colorspace) | False | Choose the type of color space conversion to apply to the output. For detailed information on setting up both the input and the output to obtain the desired color space in the output, see the section on \\"MediaLive Features - Video - color space\\" in the MediaLive User Guide. PASSTHROUGH: Keep the color space of the input content - do not convert it. AUTO:Convert all content that is SD to rec 601, and convert all content that is HD to rec 709. |
| displayAspectRatio | [Mpeg2DisplayRatio](#channels-model-mpeg2displayratio) | False | Sets the pixel aspect ratio for the encode. |
| filterSettings | [Mpeg2FilterSettings](#channels-model-mpeg2filtersettings) | False | Optionally specify a noise reduction filter, which can improve quality of compressed content. If you do not choose a filter, no filter will be applied. TEMPORAL: This filter is useful for both source content that is noisy (when it has excessive digital artifacts) and source content that is clean. When the content is noisy, the filter cleans up the source content before the encoding phase, with these two effects: First, it improves the output video quality because the content has been cleaned up. Secondly, it decreases the bandwidth because MediaLive does not waste bits on encoding noise. When the content is reasonably clean, the filter tends to decrease the bitrate. |
| fixedAfd | [FixedAfd](#channels-model-fixedafd) | False | Complete this field only when afdSignaling is set to FIXED. Enter the AFD value (4 bits) to write on all frames of the video encode. |
| framerateDenominator | integer<br />Minimum: 1 | True | description": "The framerate denominator. For example, 1001. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS. |
| framerateNumerator | integer<br />Minimum: 1 | True | The framerate numerator. For example, 24000. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS. |
| gopClosedCadence | integer<br />Minimum: 0 | False | MPEG2: default is open GOP. |
| gopNumBFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Relates to the GOP structure. The number of B-frames between reference frames. If you do not know what a B-frame is, use the default. |
| gopSize | number | False | Relates to the GOP structure. The GOP size (keyframe interval) in the units specified in gopSizeUnits. If you do not know what GOP is, use the default. If gopSizeUnits is frames, then the gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, the gopSize must be greater than 0, but does not need to be an integer. |
| gopSizeUnits | [Mpeg2GopSizeUnits](#channels-model-mpeg2gopsizeunits) | False | Relates to the GOP structure. Specifies whether the gopSize is specified in frames or seconds. If you do not plan to change the default gopSize, leave the default. If you specify SECONDS, MediaLive will internally convert the gop size to a frame count. |
| scanType | [Mpeg2ScanType](#channels-model-mpeg2scantype) | False | Set the scan type of the output to PROGRESSIVE or INTERLACED (top field first). |
| subgopLength | [Mpeg2SubGopLength](#channels-model-mpeg2subgoplength) | False | Relates to the GOP structure. If you do not know what GOP is, use the default. FIXED: Set the number of B-frames in each sub-GOP to the value in gopNumBFrames. DYNAMIC: Let MediaLive optimize the number of B-frames in each sub-GOP, to improve visual quality. |
| timecodeBurninSettings | [TimecodeBurninSettings](#channels-model-timecodeburninsettings) | False | Timecode burn-in settings |
| timecodeInsertion | [Mpeg2TimecodeInsertionBehavior](#channels-model-mpeg2timecodeinsertionbehavior) | False | Determines how MediaLive inserts timecodes in the output video. For detailed information about setting up the input and the output for a timecode, see the section on \\"MediaLive Features - Timecode configuration\\" in the MediaLive User Guide. DISABLED: do not include timecodes. GOP\_TIMECODE: Include timecode metadata in the GOP header. |

### Mpeg2SubGopLength
<a name="channels-model-mpeg2subgoplength"></a>

Mpeg2 Sub Gop Length
+ `DYNAMIC`
+ `FIXED`

### Mpeg2TimecodeInsertionBehavior
<a name="channels-model-mpeg2timecodeinsertionbehavior"></a>

Mpeg2 Timecode Insertion Behavior
+ `DISABLED`
+ `GOP_TIMECODE`

### MsSmoothGroupSettings
<a name="channels-model-mssmoothgroupsettings"></a>

Ms Smooth Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| acquisitionPointId | string | False | The ID to include in each message in the sparse track. Ignored if sparseTrackType is NONE. |
| audioOnlyTimecodeControl | [SmoothGroupAudioOnlyTimecodeControl](#channels-model-smoothgroupaudioonlytimecodecontrol) | False | If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream. |
| certificateMode | [SmoothGroupCertificateMode](#channels-model-smoothgroupcertificatemode) | False | If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail. |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established. |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | Smooth Streaming publish point on an IIS server. Elemental Live acts as a "Push" encoder to IIS. |
| eventId | string | False | MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured. |
| eventIdMode | [SmoothGroupEventIdMode](#channels-model-smoothgroupeventidmode) | False | Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - "useConfigured" - use the value provided in eventId - "useTimestamp" - generate and send an event ID based on the current timestamp - "noEventId" - do not send an event ID to the IIS server. |
| eventStopBehavior | [SmoothGroupEventStopBehavior](#channels-model-smoothgroupeventstopbehavior) | False | When set to sendEos, send EOS signal to IIS server when stopping the event |
| filecacheDuration | integer<br />Minimum: 0 | False | Size in seconds of file cache for streaming outputs. |
| fragmentLength | integer<br />Minimum: 1 | False | Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate. |
| inputLossAction | [InputLossActionForMsSmoothOut](#channels-model-inputlossactionformssmoothout) | False | Parameter that control output group behavior on input loss. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts. |
| restartDelay | integer<br />Minimum: 0 | False | Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration. |
| segmentationMode | [SmoothGroupSegmentationMode](#channels-model-smoothgroupsegmentationmode) | False | useInputSegmentation has been deprecated. The configured segment size is always used. |
| sendDelayMs | integer<br />Minimum: 0<br />Maximum: 10000 | False | Number of milliseconds to delay the output from the second pipeline. |
| sparseTrackType | [SmoothGroupSparseTrackType](#channels-model-smoothgroupsparsetracktype) | False | Identifies the type of data to place in the sparse track: - SCTE35: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame to start a new segment. - SCTE35\_WITHOUT\_SEGMENTATION: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame but don't start a new segment. - NONE: Don't generate a sparse track for any outputs in this output group. |
| streamManifestBehavior | [SmoothGroupStreamManifestBehavior](#channels-model-smoothgroupstreammanifestbehavior) | False | When set to send, send stream manifest so publishing point doesn't start until all streams start. |
| timestampOffset | string | False | Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset. |
| timestampOffsetMode | [SmoothGroupTimestampOffsetMode](#channels-model-smoothgrouptimestampoffsetmode) | False | Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset |

### MsSmoothH265PackagingType
<a name="channels-model-mssmoothh265packagingtype"></a>

Ms Smooth H265 Packaging Type
+ `HEV1`
+ `HVC1`

### MsSmoothOutputSettings
<a name="channels-model-mssmoothoutputsettings"></a>

Ms Smooth Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| h265PackagingType | [MsSmoothH265PackagingType](#channels-model-mssmoothh265packagingtype) | False | Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1. |
| nameModifier | string | False | String concatenated to the end of the destination filename. Required for multiple outputs of the same type. |

### MulticastInputSettings
<a name="channels-model-multicastinputsettings"></a>

Multicast-specific input settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceIpAddress | string | False | Optionally, a source ip address to filter by for Source-specific Multicast (SSM) |

### MultiplexContainerSettings
<a name="channels-model-multiplexcontainersettings"></a>

Multiplex Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexM2tsSettings | [MultiplexM2tsSettings](#channels-model-multiplexm2tssettings) | False |  |

### MultiplexGroupSettings
<a name="channels-model-multiplexgroupsettings"></a>

Multiplex Group Settings

### MultiplexM2tsSettings
<a name="channels-model-multiplexm2tssettings"></a>

Multiplex M2ts Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| absentInputAudioBehavior | [M2tsAbsentInputAudioBehavior](#channels-model-m2tsabsentinputaudiobehavior) | False | When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream. |
| arib | [M2tsArib](#channels-model-m2tsarib) | False | When set to enabled, uses ARIB-compliant field muxing and removes video descriptor. |
| audioBufferModel | [M2tsAudioBufferModel](#channels-model-m2tsaudiobuffermodel) | False | When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used. |
| audioFramesPerPes | integer<br />Minimum: 0 | False | The number of audio frames to insert for each PES packet. |
| audioStreamType | [M2tsAudioStreamType](#channels-model-m2tsaudiostreamtype) | False | When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06. |
| ccDescriptor | [M2tsCcDescriptor](#channels-model-m2tsccdescriptor) | False | When set to enabled, generates captionServiceDescriptor in PMT. |
| ebif | [M2tsEbifControl](#channels-model-m2tsebifcontrol) | False | If set to passthrough, passes any EBIF data from the input source to this output. |
| esRateInPes | [M2tsEsRateInPes](#channels-model-m2tsesrateinpes) | False | Include or exclude the ES Rate field in the PES header. |
| klv | [M2tsKlv](#channels-model-m2tsklv) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| nielsenId3Behavior | [M2tsNielsenId3Behavior](#channels-model-m2tsnielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| pcrControl | [M2tsPcrControl](#channels-model-m2tspcrcontrol) | False | When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPeriod | integer<br />Minimum: 0<br />Maximum: 500 | False | Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream. |
| scte35Control | [M2tsScte35Control](#channels-model-m2tsscte35control) | False | SCTE-35 control. Option "none" indicates that a SCTE-35 marker will not be inserted, nor will an IDR be inserted at the SCTE-35 cue point, nor will the segment be segmented. Option "scte35WithoutIdr" indicates that a SCTE-35 marker will be inserted to indicate the cue point, but MediaLive will not insert an IDR on that frame nor will it introduce a new segment boundary there if it wasn't already going to be one (this option is required for use with downstream multiview bitstream stitching workflows). Option "passthrough" indicates that a SCTE-35 marker will be inserted to indicate the cue point, and an IDR will be inserted on that frame, and MediaLive itself will introduce a new segment boundary there. |
| scte35PrerollPullupMilliseconds | number<br />Minimum: 0<br />Maximum: 5000 | False | Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means don't add pullup (it doesn't mean set the preroll to zero). Negative pullup is not supported, which means that you can't make the preroll shorter. Be aware that latency in the output will increase by the pullup amount. |

### MultiplexOutputSettings
<a name="channels-model-multiplexoutputsettings"></a>

Multiplex Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| containerSettings | [MultiplexContainerSettings](#channels-model-multiplexcontainersettings) | False |  |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | Destination is a Multiplex. |

### MultiplexProgramChannelDestinationSettings
<a name="channels-model-multiplexprogramchanneldestinationsettings"></a>

Multiplex Program Input Destination Settings for outputting a Channel to a Multiplex

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexId | string<br />MinLength: 1 | False | The ID of the Multiplex that the encoder is providing output to. You do not need to specify the individual inputs to the Multiplex; MediaLive will handle the connection of the two MediaLive pipelines to the two Multiplex instances. The Multiplex must be in the same region as the Channel. |
| programName | string<br />MinLength: 1 | False | The program name of the Multiplex program that the encoder is providing output to. |

### NetworkInputServerValidation
<a name="channels-model-networkinputservervalidation"></a>

Network Input Server Validation
+ `CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME`
+ `CHECK_CRYPTOGRAPHY_ONLY`

### NetworkInputSettings
<a name="channels-model-networkinputsettings"></a>

Network source to transcode. Must be accessible to the Elemental Live node that is running the live event through a network connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsInputSettings | [HlsInputSettings](#channels-model-hlsinputsettings) | False | Specifies HLS input settings when the uri is for a HLS manifest. |
| multicastInputSettings | [MulticastInputSettings](#channels-model-multicastinputsettings) | False | Specifies multicast input settings when the uri is for a multicast event. |
| serverValidation | [NetworkInputServerValidation](#channels-model-networkinputservervalidation) | False | Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https. |

### NielsenCBET
<a name="channels-model-nielsencbet"></a>

Nielsen CBET

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cbetCheckDigitString | string<br />MinLength: 2<br />MaxLength: 2 | True | Enter the CBET check digits to use in the watermark. |
| cbetStepaside | [NielsenWatermarksCbetStepaside](#channels-model-nielsenwatermarkscbetstepaside) | True | Determines the method of CBET insertion mode when prior encoding is detected on the same layer. |
| csid | string<br />MinLength: 1<br />MaxLength: 7 | True | Enter the CBET Source ID (CSID) to use in the watermark |

### NielsenConfiguration
<a name="channels-model-nielsenconfiguration"></a>

Nielsen Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| distributorId | string | False | Enter the Distributor ID assigned to your organization by Nielsen. |
| nielsenPcmToId3Tagging | [NielsenPcmToId3TaggingState](#channels-model-nielsenpcmtoid3taggingstate) | False | Enables Nielsen PCM to ID3 tagging |

### NielsenNaesIiNw
<a name="channels-model-nielsennaesiinw"></a>

Nielsen Naes Ii Nw

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| checkDigitString | string<br />MinLength: 2<br />MaxLength: 2 | True | Enter the check digit string for the watermark |
| sid | number<br />Minimum: 1<br />Maximum: 65535 | True | Enter the Nielsen Source ID (SID) to include in the watermark |
| timezone | [NielsenWatermarkTimezones](#channels-model-nielsenwatermarktimezones) | False | Choose the timezone for the time stamps in the watermark. If not provided, the timestamps will be in Coordinated Universal Time (UTC) |

### NielsenNwOnly
<a name="channels-model-nielsennwonly"></a>

Nielsen Nw Only

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| checkDigitString | string<br />MinLength: 2<br />MaxLength: 2 | True | Enter the check digit string for the watermark |
| sid | number<br />Minimum: 1<br />Maximum: 65535 | True | Enter the Nielsen Source ID (SID) to include in the watermark |
| timezone | [NielsenWatermarkTimezones](#channels-model-nielsenwatermarktimezones) | False | Choose the timezone for the time stamps in the watermark. If not provided, the timestamps will be in Coordinated Universal Time (UTC) |

### NielsenPcmToId3TaggingState
<a name="channels-model-nielsenpcmtoid3taggingstate"></a>

State of Nielsen PCM to ID3 tagging
+ `DISABLED`
+ `ENABLED`

### NielsenWatermarkTimezones
<a name="channels-model-nielsenwatermarktimezones"></a>

Nielsen Watermark Timezones
+ `AMERICA_PUERTO_RICO`
+ `US_ALASKA`
+ `US_ARIZONA`
+ `US_CENTRAL`
+ `US_EASTERN`
+ `US_HAWAII`
+ `US_MOUNTAIN`
+ `US_PACIFIC`
+ `US_SAMOA`
+ `UTC`

### NielsenWatermarksCbetStepaside
<a name="channels-model-nielsenwatermarkscbetstepaside"></a>

Nielsen Watermarks Cbet Stepaside
+ `DISABLED`
+ `ENABLED`

### NielsenWatermarksDistributionTypes
<a name="channels-model-nielsenwatermarksdistributiontypes"></a>

Nielsen Watermarks Distribution Types
+ `FINAL_DISTRIBUTOR`
+ `PROGRAM_CONTENT`

### NielsenWatermarksSettings
<a name="channels-model-nielsenwatermarkssettings"></a>

Nielsen Watermarks Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nielsenCbetSettings | [NielsenCBET](#channels-model-nielsencbet) | False | Complete these fields only if you want to insert watermarks of type Nielsen CBET |
| nielsenDistributionType | [NielsenWatermarksDistributionTypes](#channels-model-nielsenwatermarksdistributiontypes) | False | Choose the distribution types that you want to assign to the watermarks: - PROGRAM\_CONTENT - FINAL\_DISTRIBUTOR |
| nielsenNaesIiNwSettings | [NielsenNaesIiNw](#channels-model-nielsennaesiinw) | False | Complete these fields only if you want to insert watermarks of type Nielsen NAES II (N2) and Nielsen NAES VI (NW). |
| nielsenNwOnlySettings | [NielsenNwOnly](#channels-model-nielsennwonly) | False | Complete these fields only if you want to insert watermarks of type Nielsen NAES VI (NW) only, without inserting NAES II (N2) watermarks. |

### Output
<a name="channels-model-output"></a>

Output settings. There can be multiple outputs within a group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionNames | Array of type string | False | The names of the AudioDescriptions used as audio sources for this output. |
| captionDescriptionNames | Array of type string | False | The names of the CaptionDescriptions used as caption sources for this output. |
| outputName | string<br />MinLength: 1<br />MaxLength: 255 | False | The name used to identify an output. |
| outputSettings | [OutputSettings](#channels-model-outputsettings) | True | Output type-specific settings. |
| videoDescriptionName | string | False | The name of the VideoDescription used as the source for this output. |

### OutputDestination
<a name="channels-model-outputdestination"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | User-specified id. This is used in an output group or an output. |
| logicalInterfaceNames | Array of type string | False | Optional assignment of an output to a logical interface on the Node. Only applies to on premises channels. |
| mediaConnectRouterSettings | Array of type [MediaConnectRouterOutputDestinationSettings](#channels-model-mediaconnectrouteroutputdestinationsettings) | False | Destination settings for a MediaConnect Router output; one destination for each redundant encoder. |
| mediaPackageSettings | Array of type [MediaPackageOutputDestinationSettings](#channels-model-mediapackageoutputdestinationsettings) | False | Destination settings for a MediaPackage output; one destination for both encoders. |
| multiplexSettings | [MultiplexProgramChannelDestinationSettings](#channels-model-multiplexprogramchanneldestinationsettings) | False | Destination settings for a Multiplex output; one destination for both encoders. |
| settings | Array of type [OutputDestinationSettings](#channels-model-outputdestinationsettings) | False | Destination settings for a standard output; one destination for each redundant encoder. |
| srtSettings | Array of type [SrtOutputDestinationSettings](#channels-model-srtoutputdestinationsettings) | False | SRT settings for an SRT output; one destination for each redundant encoder. |

### OutputDestinationSettings
<a name="channels-model-outputdestinationsettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | key used to extract the password from EC2 Parameter store |
| streamName | string | False | Stream name for RTMP destinations (URLs of type rtmp://) |
| url | string | False | A URL specifying a destination |
| username | string | False | username for destination |
| virtualSourceAddress | string | False | Specifies the source IP address for outbound multicast packets. |

### OutputGroup
<a name="channels-model-outputgroup"></a>

Output groups for this Live Event. Output groups contain information about where streams should be distributed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string<br />MaxLength: 32 | False | Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed. |
| outputGroupSettings | [OutputGroupSettings](#channels-model-outputgroupsettings) | True | Settings associated with the output group. |
| outputs | Array of type [Output](#channels-model-output) | True |  |

### OutputGroupSettings
<a name="channels-model-outputgroupsettings"></a>

Output Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveGroupSettings | [ArchiveGroupSettings](#channels-model-archivegroupsettings) | False |  |
| cmafIngestGroupSettings | [CmafIngestGroupSettings](#channels-model-cmafingestgroupsettings) | False |  |
| frameCaptureGroupSettings | [FrameCaptureGroupSettings](#channels-model-framecapturegroupsettings) | False |  |
| hlsGroupSettings | [HlsGroupSettings](#channels-model-hlsgroupsettings) | False |  |
| mediaConnectRouterGroupSettings | [MediaConnectRouterGroupSettings](#channels-model-mediaconnectroutergroupsettings) | False |  |
| mediaPackageGroupSettings | [MediaPackageGroupSettings](#channels-model-mediapackagegroupsettings) | False |  |
| msSmoothGroupSettings | [MsSmoothGroupSettings](#channels-model-mssmoothgroupsettings) | False |  |
| multiplexGroupSettings | [MultiplexGroupSettings](#channels-model-multiplexgroupsettings) | False |  |
| rtmpGroupSettings | [RtmpGroupSettings](#channels-model-rtmpgroupsettings) | False |  |
| srtGroupSettings | [SrtGroupSettings](#channels-model-srtgroupsettings) | False |  |
| udpGroupSettings | [UdpGroupSettings](#channels-model-udpgroupsettings) | False |  |

### OutputLocationRef
<a name="channels-model-outputlocationref"></a>

Reference to an OutputDestination ID defined in the channel

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationRefId | string | False |  |

### OutputLockingSettings
<a name="channels-model-outputlockingsettings"></a>

Output Locking Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| disabledLockingSettings | [DisabledLockingSettings](#channels-model-disabledlockingsettings) | False |  |
| epochLockingSettings | [EpochLockingSettings](#channels-model-epochlockingsettings) | False |  |
| pipelineLockingSettings | [PipelineLockingSettings](#channels-model-pipelinelockingsettings) | False |  |

### OutputSettings
<a name="channels-model-outputsettings"></a>

Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveOutputSettings | [ArchiveOutputSettings](#channels-model-archiveoutputsettings) | False |  |
| cmafIngestOutputSettings | [CmafIngestOutputSettings](#channels-model-cmafingestoutputsettings) | False |  |
| frameCaptureOutputSettings | [FrameCaptureOutputSettings](#channels-model-framecaptureoutputsettings) | False |  |
| hlsOutputSettings | [HlsOutputSettings](#channels-model-hlsoutputsettings) | False |  |
| mediaConnectRouterOutputSettings | [MediaConnectRouterOutputSettings](#channels-model-mediaconnectrouteroutputsettings) | False |  |
| mediaPackageOutputSettings | [MediaPackageOutputSettings](#channels-model-mediapackageoutputsettings) | False |  |
| msSmoothOutputSettings | [MsSmoothOutputSettings](#channels-model-mssmoothoutputsettings) | False |  |
| multiplexOutputSettings | [MultiplexOutputSettings](#channels-model-multiplexoutputsettings) | False |  |
| rtmpOutputSettings | [RtmpOutputSettings](#channels-model-rtmpoutputsettings) | False |  |
| srtOutputSettings | [SrtOutputSettings](#channels-model-srtoutputsettings) | False |  |
| udpOutputSettings | [UdpOutputSettings](#channels-model-udpoutputsettings) | False |  |

### OutputUsage
<a name="channels-model-outputusage"></a>

A usage tag that declares how a MediaPackage V2 output participates in multiview. For the valid values, see the `outputUsage` field in `MediaPackageV2DestinationSettings`.
+ `MULTIVIEW_EQUAL_SIZE_VIEW`
+ `MULTIVIEW_PRIMARY_VIEW`
+ `MULTIVIEW_SECONDARY_VIEW`

### PassThroughSettings
<a name="channels-model-passthroughsettings"></a>

Pass Through Settings

### PipelineDetail
<a name="channels-model-pipelinedetail"></a>

Runtime details of a pipeline when a channel is running.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInputAttachmentName | string | False | The name of the active input attachment currently being ingested by this pipeline. |
| activeInputSwitchActionName | string | False | The name of the input switch schedule action that occurred most recently and that resulted in the switch to the current input attachment for this pipeline. |
| activeMotionGraphicsActionName | string | False | The name of the motion graphics activate action that occurred most recently and that resulted in the current graphics URI for this pipeline. |
| activeMotionGraphicsUri | string | False | The current URI being used for HTML5 motion graphics for this pipeline. |
| pipelineId | string | False | Pipeline ID |

### PipelineLockingMethod
<a name="channels-model-pipelinelockingmethod"></a>

Pipeline Locking Method
+ `SOURCE_TIMECODE`
+ `VIDEO_ALIGNMENT`

### PipelineLockingSettings
<a name="channels-model-pipelinelockingsettings"></a>

Pipeline Locking Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customEpoch | string | False | Optional. Only applies to CMAF Ingest Output Group and MediaPackage V2 Output Group Only. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00. |
| pipelineLockingMethod | [PipelineLockingMethod](#channels-model-pipelinelockingmethod) | False | The method to use to lock the video frames in the pipelines. sourceTimecode (default): Use the timecode in the source. videoAlignment: Lock frames that the encoder identifies as having matching content. If videoAlignment is selected, existing timecodes will not be used for any locking decisions. |

### PrimaryChannelSettings
<a name="channels-model-primarychannelsettings"></a>

Settings for a primary (leader) channel in a linked pair

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| linkedChannelType | [LinkedChannelType](#channels-model-linkedchanneltype) | False | Specifies this as a primary channel |

### RawSettings
<a name="channels-model-rawsettings"></a>

Raw Settings

### Rec601Settings
<a name="channels-model-rec601settings"></a>

Rec601 Settings

### Rec709Settings
<a name="channels-model-rec709settings"></a>

Rec709 Settings

### RemixSettings
<a name="channels-model-remixsettings"></a>

Remix Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelMappings | Array of type [AudioChannelMapping](#channels-model-audiochannelmapping) | True | Mapping of input channels to output channels, with appropriate gain adjustments. |
| channelsIn | integer<br />Minimum: 1<br />Maximum: 16 | False | Number of input channels to be used. |
| channelsOut | integer<br />Minimum: 1<br />Maximum: 8 | False | Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8 |

### ResourceConflict
<a name="channels-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### RtmpAdMarkers
<a name="channels-model-rtmpadmarkers"></a>

Rtmp Ad Markers
+ `ON_CUE_POINT_SCTE35`

### RtmpCacheFullBehavior
<a name="channels-model-rtmpcachefullbehavior"></a>

Rtmp Cache Full Behavior
+ `DISCONNECT_IMMEDIATELY`
+ `WAIT_FOR_SERVER`

### RtmpCaptionData
<a name="channels-model-rtmpcaptiondata"></a>

Rtmp Caption Data
+ `ALL`
+ `FIELD1_608`
+ `FIELD1_AND_FIELD2_608`

### RtmpCaptionInfoDestinationSettings
<a name="channels-model-rtmpcaptioninfodestinationsettings"></a>

Rtmp Caption Info Destination Settings

### RtmpGroupSettings
<a name="channels-model-rtmpgroupsettings"></a>

Rtmp Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | Array of type [RtmpAdMarkers](#channels-model-rtmpadmarkers) | False | Choose the ad marker type for this output group. MediaLive will create a message based on the content of each SCTE-35 message, format it for that marker type, and insert it in the datastream. |
| authenticationScheme | [AuthenticationScheme](#channels-model-authenticationscheme) | False | Authentication scheme to use when connecting with CDN |
| cacheFullBehavior | [RtmpCacheFullBehavior](#channels-model-rtmpcachefullbehavior) | False | Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again. |
| cacheLength | integer<br />Minimum: 30 | False | Cache length, in seconds, is used to calculate buffer size. |
| captionData | [RtmpCaptionData](#channels-model-rtmpcaptiondata) | False | Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed. |
| includeFillerNalUnits | [IncludeFillerNalUnits](#channels-model-includefillernalunits) | False | Applies only when the rate control mode (in the codec settings) is CBR (constant bit rate). Controls whether the RTMP output stream is padded (with FILL NAL units) in order to achieve a constant bit rate that is truly constant. When there is no padding, the bandwidth varies (up to the bitrate value in the codec settings). We recommend that you choose Auto. |
| inputLossAction | [InputLossActionForRtmpOut](#channels-model-inputlossactionforrtmpout) | False | Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection. |
| restartDelay | integer<br />Minimum: 0 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### RtmpOutputCertificateMode
<a name="channels-model-rtmpoutputcertificatemode"></a>

Rtmp Output Certificate Mode
+ `SELF_SIGNED`
+ `VERIFY_AUTHENTICITY`

### RtmpOutputSettings
<a name="channels-model-rtmpoutputsettings"></a>

Rtmp Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateMode | [RtmpOutputCertificateMode](#channels-model-rtmpoutputcertificatemode) | False | If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail. |
| connectionRetryInterval | integer<br />Minimum: 1 | False | Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost. |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts. |

### S3CannedAcl
<a name="channels-model-s3cannedacl"></a>

S3 Canned Acl
+ `AUTHENTICATED_READ`
+ `BUCKET_OWNER_FULL_CONTROL`
+ `BUCKET_OWNER_READ`
+ `PUBLIC_READ`

### Scte20Convert608To708
<a name="channels-model-scte20convert608to708"></a>

Scte20 Convert608 To708
+ `DISABLED`
+ `UPCONVERT`

### Scte20PlusEmbeddedDestinationSettings
<a name="channels-model-scte20plusembeddeddestinationsettings"></a>

Scte20 Plus Embedded Destination Settings

### Scte20SourceSettings
<a name="channels-model-scte20sourcesettings"></a>

Scte20 Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [Scte20Convert608To708](#channels-model-scte20convert608to708) | False | If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded. |
| source608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough. |

### Scte27DestinationSettings
<a name="channels-model-scte27destinationsettings"></a>

Scte27 Destination Settings

### Scte27OcrLanguage
<a name="channels-model-scte27ocrlanguage"></a>

Scte27 Ocr Language
+ `DEU`
+ `ENG`
+ `FRA`
+ `NLD`
+ `POR`
+ `SPA`

### Scte27SourceSettings
<a name="channels-model-scte27sourcesettings"></a>

Scte27 Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ocrLanguage | [Scte27OcrLanguage](#channels-model-scte27ocrlanguage) | False | If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text. |
| pid | integer<br />Minimum: 1 | False | The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is "informational". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through. |

### Scte35AposNoRegionalBlackoutBehavior
<a name="channels-model-scte35aposnoregionalblackoutbehavior"></a>

Scte35 Apos No Regional Blackout Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35AposWebDeliveryAllowedBehavior
<a name="channels-model-scte35aposwebdeliveryallowedbehavior"></a>

Scte35 Apos Web Delivery Allowed Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35SegmentationScope
<a name="channels-model-scte35segmentationscope"></a>

Scte35 Segmentation Scope
+ `ALL_OUTPUT_GROUPS`
+ `SCTE35_ENABLED_OUTPUT_GROUPS`

### Scte35SpliceInsert
<a name="channels-model-scte35spliceinsert"></a>

Scte35 Splice Insert

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages. |
| noRegionalBlackoutFlag | [Scte35SpliceInsertNoRegionalBlackoutBehavior](#channels-model-scte35spliceinsertnoregionalblackoutbehavior) | False | When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates |
| webDeliveryAllowedFlag | [Scte35SpliceInsertWebDeliveryAllowedBehavior](#channels-model-scte35spliceinsertwebdeliveryallowedbehavior) | False | When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates |

### Scte35SpliceInsertNoRegionalBlackoutBehavior
<a name="channels-model-scte35spliceinsertnoregionalblackoutbehavior"></a>

Scte35 Splice Insert No Regional Blackout Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35SpliceInsertWebDeliveryAllowedBehavior
<a name="channels-model-scte35spliceinsertwebdeliveryallowedbehavior"></a>

Scte35 Splice Insert Web Delivery Allowed Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35TimeSignalApos
<a name="channels-model-scte35timesignalapos"></a>

Scte35 Time Signal Apos

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages. |
| noRegionalBlackoutFlag | [Scte35AposNoRegionalBlackoutBehavior](#channels-model-scte35aposnoregionalblackoutbehavior) | False | When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates |
| webDeliveryAllowedFlag | [Scte35AposWebDeliveryAllowedBehavior](#channels-model-scte35aposwebdeliveryallowedbehavior) | False | When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates |

### Scte35Type
<a name="channels-model-scte35type"></a>

The SCTE-35 insertion behavior for the output group. For the valid values, see the `scte35Type` field in `CmafIngestGroupSettings` or `MediaPackageV2GroupSettings`.
+ `NONE`
+ `SCTE_35_WITHOUT_IDR`
+ `SCTE_35_WITHOUT_SEGMENTATION`

### SmartSubtitleSourceSettings
<a name="channels-model-smartsubtitlesourcesettings"></a>

Contains the settings for a Smart Subtitles caption selector. The caption source is a subtitling output on the AWS Elemental Inference feed that `InferenceSettings` associates with the channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionSynchronizationMode | [CaptionSynchronizationMode](#channels-model-captionsynchronizationmode) | False | Controls whether MediaLive delays video to synchronize captions with audio and video output. Valid values:+ `VIDEO_ALIGNED_CAPTIONS` – MediaLive delays the video so that the captions appear at the same time as the speech they transcribe. This is the default.<br />+ `NO_VIDEO_DELAY` – MediaLive doesn't delay the video. It inserts the captions into the video as they become available from Elemental Inference, so captions appear later than the speech they transcribe. |
| inferenceFeedOutput | string | False | The name of the Elemental Inference feed output that supplies subtitle input into this caption selector. |

### SmoothGroupAudioOnlyTimecodeControl
<a name="channels-model-smoothgroupaudioonlytimecodecontrol"></a>

Smooth Group Audio Only Timecode Control
+ `PASSTHROUGH`
+ `USE_CONFIGURED_CLOCK`

### SmoothGroupCertificateMode
<a name="channels-model-smoothgroupcertificatemode"></a>

Smooth Group Certificate Mode
+ `SELF_SIGNED`
+ `VERIFY_AUTHENTICITY`

### SmoothGroupEventIdMode
<a name="channels-model-smoothgroupeventidmode"></a>

Smooth Group Event Id Mode
+ `NO_EVENT_ID`
+ `USE_CONFIGURED`
+ `USE_TIMESTAMP`

### SmoothGroupEventStopBehavior
<a name="channels-model-smoothgroupeventstopbehavior"></a>

Smooth Group Event Stop Behavior
+ `NONE`
+ `SEND_EOS`

### SmoothGroupSegmentationMode
<a name="channels-model-smoothgroupsegmentationmode"></a>

Smooth Group Segmentation Mode
+ `USE_INPUT_SEGMENTATION`
+ `USE_SEGMENT_DURATION`

### SmoothGroupSparseTrackType
<a name="channels-model-smoothgroupsparsetracktype"></a>

Smooth Group Sparse Track Type
+ `NONE`
+ `SCTE_35`
+ `SCTE_35_WITHOUT_SEGMENTATION`

### SmoothGroupStreamManifestBehavior
<a name="channels-model-smoothgroupstreammanifestbehavior"></a>

Smooth Group Stream Manifest Behavior
+ `DO_NOT_SEND`
+ `SEND`

### SmoothGroupTimestampOffsetMode
<a name="channels-model-smoothgrouptimestampoffsetmode"></a>

Smooth Group Timestamp Offset Mode
+ `USE_CONFIGURED_OFFSET`
+ `USE_EVENT_START_DATE`

### Smpte2038DataPreference
<a name="channels-model-smpte2038datapreference"></a>

Smpte2038 Data Preference
+ `IGNORE`
+ `PREFER`

### SmpteTtDestinationSettings
<a name="channels-model-smptettdestinationsettings"></a>

Smpte Tt Destination Settings

### SrtEncryptionType
<a name="channels-model-srtencryptiontype"></a>

Srt Encryption Type
+ `AES128`
+ `AES192`
+ `AES256`

### SrtGroupSettings
<a name="channels-model-srtgroupsettings"></a>

Srt Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputLossAction | [InputLossActionForUdpOut](#channels-model-inputlossactionforudpout) | False | Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video. |

### SrtOutputDestinationSettings
<a name="channels-model-srtoutputdestinationsettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionMode | [ConnectionMode](#channels-model-connectionmode) | False | Specifies the mode the output should use for connection establishment. CALLER mode requires URL, LISTENER mode requires port. |
| encryptionPassphraseSecretArn | string | False | Arn used to extract the password from Secrets Manager |
| listenerPort | integer<br />Minimum: 1<br />Maximum: 65535 | False | Port number for listener mode connections (required when connectionMode is LISTENER, must not be provided when connectionMode is CALLER). |
| streamId | string | False | Stream id for SRT destinations (URLs of type srt://) |
| url | string | False | A URL specifying a destination |

### SrtOutputSettings
<a name="channels-model-srtoutputsettings"></a>

Srt Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bufferMsec | integer<br />Minimum: 0<br />Maximum: 10000 | False | SRT output buffering in milliseconds. A higher value increases latency through the encoder. But the benefits are that it helps to maintain a constant, low-jitter SRT output, and it accommodates clock recovery, input switching, input disruptions, picture reordering, and so on. Range: 0-10000 milliseconds. |
| containerSettings | [UdpContainerSettings](#channels-model-udpcontainersettings) | True |  |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True |  |
| encryptionType | [SrtEncryptionType](#channels-model-srtencryptiontype) | False | The encryption level for the content. Valid values are AES128, AES192, AES256. You and the downstream system should plan how to set this field because the values must not conflict with each other. |
| latency | integer<br />Minimum: 40<br />Maximum: 16000 | False | The latency value, in milliseconds, that is proposed during the SRT connection handshake. SRT will choose the maximum of the values proposed by the sender and receiver. On the sender side, latency is the amount of time a packet is held to give it a chance to be delivered successfully. On the receiver side, latency is the amount of time the packet is held before delivering to the application, aiding in packet recovery and matching as closely as possible the packet timing of the sender. Range: 40-16000 milliseconds. |

### StandardHlsSettings
<a name="channels-model-standardhlssettings"></a>

Standard Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioRenditionSets | string | False | List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','. |
| m3u8Settings | [M3u8Settings](#channels-model-m3u8settings) | True |  |

### StaticKeySettings
<a name="channels-model-statickeysettings"></a>

Static Key Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| keyProviderServer | [InputLocation](#channels-model-inputlocation) | False | The URL of the license server used for protecting content. |
| staticKeyValue | string<br />MinLength: 32<br />MaxLength: 32 | True | Static key value as a 32 character hexadecimal string. |

### Tags
<a name="channels-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TeletextDestinationSettings
<a name="channels-model-teletextdestinationsettings"></a>

Teletext Destination Settings

### TeletextSourceSettings
<a name="channels-model-teletextsourcesettings"></a>

Teletext Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputRectangle | [CaptionRectangle](#channels-model-captionrectangle) | False | Optionally defines a region where TTML style captions will be displayed |
| pageNumber | string | False | Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix. |

### TemporalFilterPostFilterSharpening
<a name="channels-model-temporalfilterpostfiltersharpening"></a>

Temporal Filter Post Filter Sharpening
+ `AUTO`
+ `DISABLED`
+ `ENABLED`

### TemporalFilterSettings
<a name="channels-model-temporalfiltersettings"></a>

Temporal Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| postFilterSharpening | [TemporalFilterPostFilterSharpening](#channels-model-temporalfilterpostfiltersharpening) | False | If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR. |
| strength | [TemporalFilterStrength](#channels-model-temporalfilterstrength) | False | Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft. |

### TemporalFilterStrength
<a name="channels-model-temporalfilterstrength"></a>

Temporal Filter Strength
+ `AUTO`
+ `STRENGTH_1`
+ `STRENGTH_2`
+ `STRENGTH_3`
+ `STRENGTH_4`
+ `STRENGTH_5`
+ `STRENGTH_6`
+ `STRENGTH_7`
+ `STRENGTH_8`
+ `STRENGTH_9`
+ `STRENGTH_10`
+ `STRENGTH_11`
+ `STRENGTH_12`
+ `STRENGTH_13`
+ `STRENGTH_14`
+ `STRENGTH_15`
+ `STRENGTH_16`

### TextCaptionPositionSettings
<a name="channels-model-textcaptionpositionsettings"></a>

Specifies the position of TTML or WebVTT output captions when `styleControl` is set to `MANUAL`, as a percentage from the top of the output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| yPositionPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Specifies the vertical position of the top edge of the caption relative to the top of the output as a percentage. A value of 0 places the caption at the top of the output and 100 at the bottom. |

### ThumbnailConfiguration
<a name="channels-model-thumbnailconfiguration"></a>

Thumbnail Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| state | [ThumbnailState](#channels-model-thumbnailstate) | True | Enables the thumbnail feature. The feature generates thumbnails of the incoming video in each pipeline in the channel. AUTO turns the feature on, DISABLE turns the feature off. |

### ThumbnailState
<a name="channels-model-thumbnailstate"></a>

Thumbnail State
+ `AUTO`
+ `DISABLED`

### TimecodeBurninFontSize
<a name="channels-model-timecodeburninfontsize"></a>

Timecode Burnin Font Size
+ `EXTRA_SMALL_10`
+ `LARGE_48`
+ `MEDIUM_32`
+ `SMALL_16`

### TimecodeBurninPosition
<a name="channels-model-timecodeburninposition"></a>

Timecode Burnin Position
+ `BOTTOM_CENTER`
+ `BOTTOM_LEFT`
+ `BOTTOM_RIGHT`
+ `MIDDLE_CENTER`
+ `MIDDLE_LEFT`
+ `MIDDLE_RIGHT`
+ `TOP_CENTER`
+ `TOP_LEFT`
+ `TOP_RIGHT`

### TimecodeBurninSettings
<a name="channels-model-timecodeburninsettings"></a>

Timecode Burnin Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fontSize | [TimecodeBurninFontSize](#channels-model-timecodeburninfontsize) | True | Choose a timecode burn-in font size |
| position | [TimecodeBurninPosition](#channels-model-timecodeburninposition) | True | Choose a timecode burn-in output position |
| prefix | string<br />MaxLength: 255 | False | Create a timecode burn-in prefix (optional) |

### TimecodeConfig
<a name="channels-model-timecodeconfig"></a>

Timecode Config

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| source | [TimecodeConfigSource](#channels-model-timecodeconfigsource) | True | Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00. |
| syncThreshold | integer<br />Minimum: 1<br />Maximum: 1000000 | False | Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified. |

### TimecodeConfigSource
<a name="channels-model-timecodeconfigsource"></a>

Timecode Config Source
+ `EMBEDDED`
+ `SYSTEMCLOCK`
+ `ZEROBASED`

### TtmlDestinationSettings
<a name="channels-model-ttmldestinationsettings"></a>

Ttml Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| position | [TextCaptionPositionSettings](#channels-model-textcaptionpositionsettings) | False | Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`. |
| styleControl | [TtmlDestinationStyleControl](#channels-model-ttmldestinationstylecontrol) | False | Controls the source of style and position information for the output captions. Valid values:+ `PASSTHROUGH` – Preserve the style and position from the source captions.<br />+ `USE_CONFIGURED` – Don't pass through the style. The output captions will use the default styling.<br />+ `MANUAL` – Applies the specified styling and positioning. All other styling and positioning is given default values.<br />If you don't specify this field, the default is `PASSTHROUGH`. |

### TtmlDestinationStyleControl
<a name="channels-model-ttmldestinationstylecontrol"></a>

Ttml Destination Style Control
+ `MANUAL`
+ `PASSTHROUGH`
+ `USE_CONFIGURED`

### UdpContainerSettings
<a name="channels-model-udpcontainersettings"></a>

Udp Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| m2tsSettings | [M2tsSettings](#channels-model-m2tssettings) | False |  |

### UdpGroupSettings
<a name="channels-model-udpgroupsettings"></a>

Udp Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputLossAction | [InputLossActionForUdpOut](#channels-model-inputlossactionforudpout) | False | Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video. |
| timedMetadataId3Frame | [UdpTimedMetadataId3Frame](#channels-model-udptimedmetadataid3frame) | False | Indicates ID3 frame that has the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0 | False | Timed Metadata interval in seconds. |

### UdpOutputSettings
<a name="channels-model-udpoutputsettings"></a>

Udp Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bufferMsec | integer<br />Minimum: 0<br />Maximum: 10000 | False | UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc. |
| containerSettings | [UdpContainerSettings](#channels-model-udpcontainersettings) | True |  |
| destination | [OutputLocationRef](#channels-model-outputlocationref) | True | Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002). |
| fecOutputSettings | [FecOutputSettings](#channels-model-fecoutputsettings) | False | Settings for enabling and adjusting Forward Error Correction on UDP outputs. |

### UdpTimedMetadataId3Frame
<a name="channels-model-udptimedmetadataid3frame"></a>

Udp Timed Metadata Id3 Frame
+ `NONE`
+ `PRIV`
+ `TDRL`

### ValidationError
<a name="channels-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

### VideoBlackFailoverSettings
<a name="channels-model-videoblackfailoversettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackDetectThreshold | number<br />Minimum: 0<br />Maximum: 1 | False | A value used in calculating the threshold below which MediaLive considers a pixel to be 'black'. For the input to be considered black, every pixel in a frame must be below this threshold. The threshold is calculated as a percentage (expressed as a decimal) of white. Therefore .1 means 10% white (or 90% black). Note how the formula works for any color depth. For example, if you set this field to 0.1 in 10-bit color depth: (1023\*0.1=102.3), which means a pixel value of 102 or less is 'black'. If you set this field to .1 in an 8-bit color depth: (255\*0.1=25.5), which means a pixel value of 25 or less is 'black'. The range is 0.0 to 1.0, with any number of decimal places. |
| videoBlackThresholdMsec | integer<br />Minimum: 1000 | False | The amount of time (in milliseconds) that the active input must be black before automatic input failover occurs. |

### VideoCodecSettings
<a name="channels-model-videocodecsettings"></a>

Video Codec Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| av1Settings | [Av1Settings](#channels-model-av1settings) | False |  |
| frameCaptureSettings | [FrameCaptureSettings](#channels-model-framecapturesettings) | False |  |
| h264Settings | [H264Settings](#channels-model-h264settings) | False |  |
| h265Settings | [H265Settings](#channels-model-h265settings) | False |  |
| mpeg2Settings | [Mpeg2Settings](#channels-model-mpeg2settings) | False |  |

### VideoDescription
<a name="channels-model-videodescription"></a>

Video settings for this stream.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| border | integer<br />Minimum: 0<br />Maximum: 100 | False | The width, in pixels, of the black border to insert around each edge of the encoded picture. Must be an even integer from 0 (no border, which is the default) through 100. The border is applied to every side, so the width and height of this VideoDescription must each be greater than twice this value. You can't use this field together with outputPositionRectangle, because both fields govern the position of the encoded content within the output frame. |
| codecSettings | [VideoCodecSettings](#channels-model-videocodecsettings) | False | Video codec settings. |
| cropRectangle | [VideoPositionRectangle](#channels-model-videopositionrectangle) | False | Region of the input video to crop before scaling. If not specified, the entire input frame is used. Note: Unlike outputPositionRectangle, the bounds of cropRectangle are validated at ingest time by the encoder/scaler rather than at the API level, because the input resolution is not known until the source is probed. Field-level constraints on (x, y, width, height) defined on VideoPositionRectangle still apply. |
| height | integer | False | Output video height, in pixels. Must be an even number. For most codecs, you can leave this field and width blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required. |
| name | string | True | The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event. |
| outputPositionRectangle | [VideoPositionRectangle](#channels-model-videopositionrectangle) | False | The position of the encoded video within the output frame. The area outside the rectangle is filled with black. If you don't specify this field, the video fills the entire output frame. If you do specify it, you must also explicitly specify the width and height of this VideoDescription, so that MediaLive can validate the rectangle against the output frame. |
| respondToAfd | [VideoDescriptionRespondToAfd](#channels-model-videodescriptionrespondtoafd) | False | Indicates how MediaLive will respond to the AFD values that might be in the input video. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose PASSTHROUGH. RESPOND: MediaLive clips the input video using a formula that uses the AFD values (configured in afdSignaling ), the input display aspect ratio, and the output display aspect ratio. MediaLive also includes the AFD values in the output, unless the codec for this encode is FRAME\_CAPTURE. PASSTHROUGH: MediaLive ignores the AFD values and does not clip the video. But MediaLive does include the values in the output. NONE: MediaLive does not clip the input video and does not include the AFD values in the output |
| scalingBehavior | [VideoDescriptionScalingBehavior](#channels-model-videodescriptionscalingbehavior) | False | Configures how MediaLive transforms the video picture to match the output frame (height and width). Valid values:+ `DEFAULT` – MediaLive inserts pillar boxes or letter boxes around the video, as needed, to fill the output frame. The video isn't distorted.<br />+ `STRETCH_TO_OUTPUT` – MediaLive stretches the video to fill the output frame. This option overrides any position value. The video might be distorted.<br />+ `SMART_CROP` – MediaLive crops the video to the aspect ratio of the output frame. MediaLive keeps the region of interest that AWS Elemental Inference detects in the source. This value requires `InferenceSettings` with a `feedArn` that identifies an Elemental Inference feed that has a cropping output. For more information about smart cropping, see [Smart cropping video using Elemental Inference](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference-smart-crop.html) in the *MediaLive User Guide*. |
| sharpness | integer<br />Minimum: 0<br />Maximum: 100 | False | Changes the strength of the anti-alias filter used for scaling. 0 is the softest setting, 100 is the sharpest. A setting of 50 is recommended for most content. |
| width | integer | False | Output video width, in pixels. Must be an even number. For most codecs, you can leave this field and height blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required. |

### VideoDescriptionRespondToAfd
<a name="channels-model-videodescriptionrespondtoafd"></a>

Video Description Respond To Afd
+ `NONE`
+ `PASSTHROUGH`
+ `RESPOND`

### VideoDescriptionScalingBehavior
<a name="channels-model-videodescriptionscalingbehavior"></a>

Specifies how MediaLive transforms the video picture to match the output frame. Valid values:
+ `DEFAULT` – MediaLive inserts pillar boxes or letter boxes around the video, as needed, to fill the output frame.
+ `STRETCH_TO_OUTPUT` – MediaLive stretches the video to fill the output frame.
+ `SMART_CROP` – MediaLive crops the video to the aspect ratio of the output frame, keeping the region of interest that AWS Elemental Inference detects.

For details, see the `scalingBehavior` field in `VideoDescription`.
+ `DEFAULT`
+ `SMART_CROP`
+ `STRETCH_TO_OUTPUT`

### VideoPositionRectangle
<a name="channels-model-videopositionrectangle"></a>

A rectangle defined by a position (x, y) and dimensions (width, height), in pixels.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 2<br />Maximum: 8192 | True | The height of the rectangle, in pixels. Must be an even number. |
| width | integer<br />Minimum: 2<br />Maximum: 8192 | True | The width of the rectangle, in pixels. Must be an even number. |
| x | integer<br />Minimum: 0<br />Maximum: 8190 | True | The offset of the left edge of the rectangle, in pixels. Must be an even number. |
| y | integer<br />Minimum: 0<br />Maximum: 8190 | True | The offset of the top edge of the rectangle, in pixels. Must be an even number. |

### VideoSelector
<a name="channels-model-videoselector"></a>

Specifies a particular video stream within an input source. An input may have only a single video selector.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpace | [VideoSelectorColorSpace](#channels-model-videoselectorcolorspace) | False | Specifies the color space of an input. This setting works in tandem with colorSpaceUsage and a video description's colorSpaceSettingsChoice to determine if any conversion will be performed. |
| colorSpaceSettings | [VideoSelectorColorSpaceSettings](#channels-model-videoselectorcolorspacesettings) | False | Color space settings |
| colorSpaceUsage | [VideoSelectorColorSpaceUsage](#channels-model-videoselectorcolorspaceusage) | False | Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data. |
| selectorSettings | [VideoSelectorSettings](#channels-model-videoselectorsettings) | False | The video selector settings. |

### VideoSelectorColorSpace
<a name="channels-model-videoselectorcolorspace"></a>

Video Selector Color Space
+ `FOLLOW`
+ `HDR10`
+ `HLG_2020`
+ `REC_601`
+ `REC_709`

### VideoSelectorColorSpaceSettings
<a name="channels-model-videoselectorcolorspacesettings"></a>

Video Selector Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hdr10Settings | [Hdr10Settings](#channels-model-hdr10settings) | False |  |

### VideoSelectorColorSpaceUsage
<a name="channels-model-videoselectorcolorspaceusage"></a>

Video Selector Color Space Usage
+ `FALLBACK`
+ `FORCE`

### VideoSelectorPid
<a name="channels-model-videoselectorpid"></a>

Video Selector Pid

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | False | Selects a specific PID from within a video source. |

### VideoSelectorProgramId
<a name="channels-model-videoselectorprogramid"></a>

Video Selector Program Id

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| programId | integer<br />Minimum: 0<br />Maximum: 65536 | False | Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default. |

### VideoSelectorSettings
<a name="channels-model-videoselectorsettings"></a>

Video Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| videoSelectorPid | [VideoSelectorPid](#channels-model-videoselectorpid) | False |  |
| videoSelectorProgramId | [VideoSelectorProgramId](#channels-model-videoselectorprogramid) | False |  |

### VpcOutputSettings
<a name="channels-model-vpcoutputsettings"></a>

The properties for a private VPC Output When this property is specified, the output egress addresses will be created in a user specified VPC

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| publicAddressAllocationIds | Array of type string | False | List of public address allocation ids to associate with ENIs that will be created in Output VPC. Must specify one for SINGLE\_PIPELINE, two for STANDARD channels  |
| securityGroupIds | Array of type string | False | A list of up to 5 EC2 VPC security group IDs to attach to the Output VPC network interfaces. If none are specified then the VPC default security group will be used  |
| subnetIds | Array of type string | True | A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ).  |

### VpcOutputSettingsDescription
<a name="channels-model-vpcoutputsettingsdescription"></a>

The properties for a private VPC Output

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZones | Array of type string | False | The Availability Zones where the vpc subnets are located. The first Availability Zone applies to the first subnet in the list of subnets. The second Availability Zone applies to the second subnet.  |
| networkInterfaceIds | Array of type string | False | A list of Elastic Network Interfaces created by MediaLive in the customer's VPC  |
| securityGroupIds | Array of type string | False | A list of up EC2 VPC security group IDs attached to the Output VPC network interfaces.  |
| subnetIds | Array of type string | False | A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ).  |

### WavCodingMode
<a name="channels-model-wavcodingmode"></a>

Wav Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_4_0`
+ `CODING_MODE_8_0`

### WavSettings
<a name="channels-model-wavsettings"></a>

Wav Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | number | False | Bits per sample. |
| codingMode | [WavCodingMode](#channels-model-wavcodingmode) | False | The audio coding mode for the WAV audio. The mode determines the number of channels in the audio. |
| sampleRate | number | False | Sample rate in Hz. |

### WebvttDestinationSettings
<a name="channels-model-webvttdestinationsettings"></a>

Webvtt Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| position | [TextCaptionPositionSettings](#channels-model-textcaptionpositionsettings) | False | Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`. |
| styleControl | [WebvttDestinationStyleControl](#channels-model-webvttdestinationstylecontrol) | False | Controls whether the color and position of the source captions is passed through to the WebVTT output captions. Valid values:+ `PASSTHROUGH` – Valid only if the source captions are EMBEDDED, TELETEXT, or SMART SUBTITLES.<br />+ `NO_STYLE_DATA` – Don't pass through the style. The output captions will not contain any font styling information.<br />+ `MANUAL` – Applies the specified styling and positioning. All other styling and positioning is given default values.<br />If you don't specify this field, the default is `NO_STYLE_DATA`. |

### WebvttDestinationStyleControl
<a name="channels-model-webvttdestinationstylecontrol"></a>

Webvtt Destination Style Control
+ `MANUAL`
+ `NO_STYLE_DATA`
+ `PASSTHROUGH`

## See also
<a name="channels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListChannels
<a name="ListChannels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListChannels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListChannels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListChannels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListChannels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListChannels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListChannels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListChannels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListChannels)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/ListChannels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListChannels)

### CreateChannel
<a name="CreateChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/CreateChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateChannel)
