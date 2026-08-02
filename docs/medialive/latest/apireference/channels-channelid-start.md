---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/channels-channelid-start.html
---

# Channels: start
<a name="channels-channelid-start"></a>

## URI
<a name="channels-channelid-start-url"></a>

`/prod/channels/{{channelId}}/start`

## HTTP methods
<a name="channels-channelid-start-http-methods"></a>

### POST
<a name="channels-channelid-startpost"></a>

**Operation ID:** `StartChannel`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{channelId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Channel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="channels-channelid-start-schemas"></a>

### Response bodies
<a name="channels-channelid-start-response-examples"></a>

#### Channel schema
<a name="channels-channelid-start-response-body-channel-example"></a>

```
{
  "arn": "string",
  "cdiInputSpecification": {
    "resolution": enum
  },
  "channelClass": enum,
  "destinations": [
    {
      "id": "string",
      "mediaPackageSettings": [
        {
          "channelId": "string"
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
          "username": "string"
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
              "sid": number
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
            "bitrate": number,
            "bitstreamMode": enum,
            "codingMode": enum,
            "dialnorm": integer,
            "drcProfile": enum,
            "lfeFilter": enum,
            "metadataControl": enum
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
      }
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
            "teletextGridControl": enum,
            "xPosition": integer,
            "yPosition": integer
          },
          "ebuTtDDestinationSettings": {
            "copyrightHolder": "string",
            "fillLineGap": enum,
            "fontFamily": "string",
            "styleControl": enum
          },
          "embeddedDestinationSettings": {
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
            "styleControl": enum
          },
          "webvttDestinationSettings": {
            "styleControl": enum
          }
        },
        "languageCode": "string",
        "languageDescription": "string",
        "name": "string"
      }
    ],
    "featureActivations": {
      "inputPrepareScheduleActions": enum
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
          "mediaPackageGroupSettings": {
            "destination": {
              "destinationRefId": "string"
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
            "inputLossAction": enum,
            "restartDelay": integer
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
              "mediaPackageOutputSettings": {
              },
              "msSmoothOutputSettings": {
                "h265PackagingType": enum,
                "nameModifier": "string"
              },
              "multiplexOutputSettings": {
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
    "timecodeConfig": {
      "source": enum,
      "syncThreshold": integer
    },
    "videoDescriptions": [
      {
        "codecSettings": {
          "frameCaptureSettings": {
            "captureInterval": integer,
            "captureIntervalUnits": enum
          },
          "h264Settings": {
            "adaptiveQuantization": enum,
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
            "minIInterval": integer,
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
              "hdr10Settings": {
                "maxCll": integer,
                "maxFall": integer
              },
              "rec601Settings": {
              },
              "rec709Settings": {
              }
            },
            "filterSettings": {
              "temporalFilterSettings": {
                "postFilterSharpening": enum,
                "strength": enum
              }
            },
            "fixedAfd": enum,
            "flickerAq": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer,
            "gopClosedCadence": integer,
            "gopSize": number,
            "gopSizeUnits": enum,
            "level": enum,
            "lookAheadRateControl": enum,
            "maxBitrate": integer,
            "minIInterval": integer,
            "parDenominator": integer,
            "parNumerator": integer,
            "profile": enum,
            "qvbrQualityLevel": integer,
            "rateControlMode": enum,
            "scanType": enum,
            "sceneChangeDetect": enum,
            "slices": integer,
            "tier": enum,
            "timecodeInsertion": enum
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
            "timecodeInsertion": enum
          }
        },
        "height": integer,
        "name": "string",
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
          "serverValidation": enum
        },
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
      }
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
  }
}
```

#### InvalidRequest schema
<a name="channels-channelid-start-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="channels-channelid-start-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="channels-channelid-start-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="channels-channelid-start-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="channels-channelid-start-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="channels-channelid-start-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="channels-channelid-start-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="channels-channelid-start-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="channels-channelid-start-properties"></a>

### AacCodingMode
<a name="channels-channelid-start-model-aaccodingmode"></a>

Aac Coding Mode
+ `AD_RECEIVER_MIX`
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_5_1`

### AacInputType
<a name="channels-channelid-start-model-aacinputtype"></a>

Aac Input Type
+ `BROADCASTER_MIXED_AD`
+ `NORMAL`

### AacProfile
<a name="channels-channelid-start-model-aacprofile"></a>

Aac Profile
+ `HEV1`
+ `HEV2`
+ `LC`

### AacRateControlMode
<a name="channels-channelid-start-model-aacratecontrolmode"></a>

Aac Rate Control Mode
+ `CBR`
+ `VBR`

### AacRawFormat
<a name="channels-channelid-start-model-aacrawformat"></a>

Aac Raw Format
+ `LATM_LOAS`
+ `NONE`

### AacSettings
<a name="channels-channelid-start-model-aacsettings"></a>

Aac Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. Valid values depend on rate control mode and profile. |
| codingMode | [AacCodingMode](#channels-channelid-start-model-aaccodingmode) | False | Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E. |
| inputType | [AacInputType](#channels-channelid-start-model-aacinputtype) | False | Set to "broadcasterMixedAd" when input contains pre-mixed main audio \+ AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to "normal" when input does not contain pre-mixed audio \+ AD. |
| profile | [AacProfile](#channels-channelid-start-model-aacprofile) | False | AAC Profile. |
| rateControlMode | [AacRateControlMode](#channels-channelid-start-model-aacratecontrolmode) | False | Rate Control Mode. |
| rawFormat | [AacRawFormat](#channels-channelid-start-model-aacrawformat) | False | Sets LATM / LOAS AAC output for raw containers. |
| sampleRate | number | False | Sample rate in Hz. Valid values depend on rate control mode and profile. |
| spec | [AacSpec](#channels-channelid-start-model-aacspec) | False | Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers. |
| vbrQuality | [AacVbrQuality](#channels-channelid-start-model-aacvbrquality) | False | VBR Quality Level - Only used if rateControlMode is VBR. |

### AacSpec
<a name="channels-channelid-start-model-aacspec"></a>

Aac Spec
+ `MPEG2`
+ `MPEG4`

### AacVbrQuality
<a name="channels-channelid-start-model-aacvbrquality"></a>

Aac Vbr Quality
+ `HIGH`
+ `LOW`
+ `MEDIUM_HIGH`
+ `MEDIUM_LOW`

### Ac3BitstreamMode
<a name="channels-channelid-start-model-ac3bitstreammode"></a>

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
<a name="channels-channelid-start-model-ac3codingmode"></a>

Ac3 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`

### Ac3DrcProfile
<a name="channels-channelid-start-model-ac3drcprofile"></a>

Ac3 Drc Profile
+ `FILM_STANDARD`
+ `NONE`

### Ac3LfeFilter
<a name="channels-channelid-start-model-ac3lfefilter"></a>

Ac3 Lfe Filter
+ `DISABLED`
+ `ENABLED`

### Ac3MetadataControl
<a name="channels-channelid-start-model-ac3metadatacontrol"></a>

Ac3 Metadata Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Ac3Settings
<a name="channels-channelid-start-model-ac3settings"></a>

Ac3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. Valid bitrates depend on the coding mode. |
| bitstreamMode | [Ac3BitstreamMode](#channels-channelid-start-model-ac3bitstreammode) | False | Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values. |
| codingMode | [Ac3CodingMode](#channels-channelid-start-model-ac3codingmode) | False | Dolby Digital coding mode. Determines number of channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through. |
| drcProfile | [Ac3DrcProfile](#channels-channelid-start-model-ac3drcprofile) | False | If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification. |
| lfeFilter | [Ac3LfeFilter](#channels-channelid-start-model-ac3lfefilter) | False | When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode. |
| metadataControl | [Ac3MetadataControl](#channels-channelid-start-model-ac3metadatacontrol) | False | When set to "followInput", encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |

### AccessDenied
<a name="channels-channelid-start-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### AfdSignaling
<a name="channels-channelid-start-model-afdsignaling"></a>

Afd Signaling
+ `AUTO`
+ `FIXED`
+ `NONE`

### AncillarySourceSettings
<a name="channels-channelid-start-model-ancillarysourcesettings"></a>

Ancillary Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceAncillaryChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the number (1 to 4) of the captions channel you want to extract from the ancillary captions. If you plan to convert the ancillary captions to another format, complete this field. If you plan to choose Embedded as the captions destination in the output (to pass through all the channels in the ancillary captions), leave this field blank because MediaLive ignores the field. |

### ArchiveCdnSettings
<a name="channels-channelid-start-model-archivecdnsettings"></a>

Archive Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveS3Settings | [ArchiveS3Settings](#channels-channelid-start-model-archives3settings) | False |  |

### ArchiveContainerSettings
<a name="channels-channelid-start-model-archivecontainersettings"></a>

Archive Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| m2tsSettings | [M2tsSettings](#channels-channelid-start-model-m2tssettings) | False |  |
| rawSettings | [RawSettings](#channels-channelid-start-model-rawsettings) | False |  |

### ArchiveGroupSettings
<a name="channels-channelid-start-model-archivegroupsettings"></a>

Archive Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveCdnSettings | [ArchiveCdnSettings](#channels-channelid-start-model-archivecdnsettings) | False | Parameters that control interactions with the CDN. |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | A directory and base filename where archive files should be written. |
| rolloverInterval | integer<br />Minimum: 1 | False | Number of seconds to write to archive file before closing and starting a new one. |

### ArchiveOutputSettings
<a name="channels-channelid-start-model-archiveoutputsettings"></a>

Archive Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| containerSettings | [ArchiveContainerSettings](#channels-channelid-start-model-archivecontainersettings) | True | Settings specific to the container type of the file. |
| extension | string | False | Output file extension. If excluded, this will be auto-selected from the container type. |
| nameModifier | string | False | String concatenated to the end of the destination filename. Required for multiple outputs of the same type. |

### ArchiveS3LogUploads
<a name="channels-channelid-start-model-archives3loguploads"></a>

Archive S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### ArchiveS3Settings
<a name="channels-channelid-start-model-archives3settings"></a>

Archive S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-channelid-start-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [ArchiveS3LogUploads](#channels-channelid-start-model-archives3loguploads) | False | When set to enabled, each upload to CDN or server will be logged. |

### AribDestinationSettings
<a name="channels-channelid-start-model-aribdestinationsettings"></a>

Arib Destination Settings

### AribSourceSettings
<a name="channels-channelid-start-model-aribsourcesettings"></a>

Arib Source Settings

### AudioChannelMapping
<a name="channels-channelid-start-model-audiochannelmapping"></a>

Audio Channel Mapping

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputChannelLevels | Array of type [InputChannelLevel](#channels-channelid-start-model-inputchannellevel) | True | Indices and gain values for each input channel that should be remixed into this output channel. |
| outputChannel | integer<br />Minimum: 0<br />Maximum: 7 | True | The index of the output channel being produced. |

### AudioCodecSettings
<a name="channels-channelid-start-model-audiocodecsettings"></a>

Audio Codec Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aacSettings | [AacSettings](#channels-channelid-start-model-aacsettings) | False |  |
| ac3Settings | [Ac3Settings](#channels-channelid-start-model-ac3settings) | False |  |
| eac3Settings | [Eac3Settings](#channels-channelid-start-model-eac3settings) | False |  |
| mp2Settings | [Mp2Settings](#channels-channelid-start-model-mp2settings) | False |  |
| passThroughSettings | [PassThroughSettings](#channels-channelid-start-model-passthroughsettings) | False |  |
| wavSettings | [WavSettings](#channels-channelid-start-model-wavsettings) | False |  |

### AudioDescription
<a name="channels-channelid-start-model-audiodescription"></a>

Audio Description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioNormalizationSettings | [AudioNormalizationSettings](#channels-channelid-start-model-audionormalizationsettings) | False | Advanced audio normalization settings. |
| audioSelectorName | string | True | The name of the AudioSelector used as the source for this AudioDescription. |
| audioType | [AudioType](#channels-channelid-start-model-audiotype) | False | Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1. |
| audioTypeControl | [AudioDescriptionAudioTypeControl](#channels-channelid-start-model-audiodescriptionaudiotypecontrol) | False | Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd. |
| audioWatermarkingSettings | [AudioWatermarkSettings](#channels-channelid-start-model-audiowatermarksettings) | False | Settings to configure one or more solutions that insert audio watermarks in the audio encode |
| codecSettings | [AudioCodecSettings](#channels-channelid-start-model-audiocodecsettings) | False | Audio codec settings. |
| languageCode | string<br />MinLength: 1<br />MaxLength: 35 | False | RFC 5646 language code representing the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input. |
| languageCodeControl | [AudioDescriptionLanguageCodeControl](#channels-channelid-start-model-audiodescriptionlanguagecodecontrol) | False | Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input. |
| name | string | True | The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event. |
| remixSettings | [RemixSettings](#channels-channelid-start-model-remixsettings) | False | Settings that control how input audio channels are remixed into the output audio channels. |
| streamName | string | False | Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary). |

### AudioDescriptionAudioTypeControl
<a name="channels-channelid-start-model-audiodescriptionaudiotypecontrol"></a>

Audio Description Audio Type Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioDescriptionLanguageCodeControl
<a name="channels-channelid-start-model-audiodescriptionlanguagecodecontrol"></a>

Audio Description Language Code Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioHlsRenditionSelection
<a name="channels-channelid-start-model-audiohlsrenditionselection"></a>

Audio Hls Rendition Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| groupId | string<br />MinLength: 1 | True | Specifies the GROUP-ID in the \#EXT-X-MEDIA tag of the target HLS audio rendition. |
| name | string<br />MinLength: 1 | True | Specifies the NAME in the \#EXT-X-MEDIA tag of the target HLS audio rendition. |

### AudioLanguageSelection
<a name="channels-channelid-start-model-audiolanguageselection"></a>

Audio Language Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | True | Selects a specific three-letter language code from within an audio source. |
| languageSelectionPolicy | [AudioLanguageSelectionPolicy](#channels-channelid-start-model-audiolanguageselectionpolicy) | False | When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language. |

### AudioLanguageSelectionPolicy
<a name="channels-channelid-start-model-audiolanguageselectionpolicy"></a>

Audio Language Selection Policy
+ `LOOSE`
+ `STRICT`

### AudioNormalizationAlgorithm
<a name="channels-channelid-start-model-audionormalizationalgorithm"></a>

Audio Normalization Algorithm
+ `ITU_1770_1`
+ `ITU_1770_2`
+ `ITU_1770_3`
+ `ITU_1770_4`

### AudioNormalizationAlgorithmControl
<a name="channels-channelid-start-model-audionormalizationalgorithmcontrol"></a>

Audio Normalization Algorithm Control
+ `CORRECT_AUDIO`

### AudioNormalizationPeakCalculation
<a name="channels-channelid-start-model-audionormalizationpeakcalculation"></a>

Specifies the method for calculating peak loudness during audio normalization.
+ `NONE`
+ `TRUE_PEAK`

### AudioNormalizationSettings
<a name="channels-channelid-start-model-audionormalizationsettings"></a>

Audio Normalization Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [AudioNormalizationAlgorithm](#channels-channelid-start-model-audionormalizationalgorithm) | False | The audio normalization algorithm to use. Valid values: ITU\_1770\_1 – ITU-R BS.1770-1 (ungated loudness). Measures average loudness for an entire piece of content. Suitable for short-form content under ATSC A/85. Supports up to 5.1 audio channels. ITU\_1770\_2 – ITU-R BS.1770-2 (gated loudness). Measures gated average loudness compliant with EBU R128. Supports up to 5.1 audio channels. ITU\_1770\_3 – ITU-R BS.1770-3 (modified peak). Uses the ITU-R BS.1770-2 algorithm with an updated true peak measurement. ITU\_1770\_4 – ITU-R BS.1770-4 (higher channel count). Supports more audio channels, including 7.1 configurations.  |
| algorithmControl | [AudioNormalizationAlgorithmControl](#channels-channelid-start-model-audionormalizationalgorithmcontrol) | False | When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted. |
| peakCalculation | [AudioNormalizationPeakCalculation](#channels-channelid-start-model-audionormalizationpeakcalculation) | False | Specifies whether to calculate true peak loudness for each output audio track. When set to TRUE\_PEAK, the service calculates true peak values for every output. |
| peakLimiterThreshold | number<br />Minimum: -8<br />Maximum: 0 | False | The peak limiter threshold, in decibels relative to true peak (dBTP), when TRUE\_PEAK peak calculation is enabled. When TRUE\_PEAK is not enabled, the threshold applies as decibels relative to full scale (dBFS). |
| targetLkfs | number<br />Minimum: -59<br />Maximum: 0 | False | Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS. |

### AudioOnlyHlsSegmentType
<a name="channels-channelid-start-model-audioonlyhlssegmenttype"></a>

Audio Only Hls Segment Type
+ `AAC`
+ `FMP4`

### AudioOnlyHlsSettings
<a name="channels-channelid-start-model-audioonlyhlssettings"></a>

Audio Only Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioGroupId | string | False | Specifies the group to which the audio Rendition belongs. |
| audioOnlyImage | [InputLocation](#channels-channelid-start-model-inputlocation) | False | Optional. Specifies the .jpg or .png image to use as the cover art for an audio-only output. We recommend a low bit-size file because the image increases the output audio bandwidth. The image is attached to the audio as an ID3 tag, frame type APIC, picture type 0x10, as per the "ID3 tag version 2.4.0 - Native Frames" standard. |
| audioTrackType | [AudioOnlyHlsTrackType](#channels-channelid-start-model-audioonlyhlstracktype) | False | Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO |
| segmentType | [AudioOnlyHlsSegmentType](#channels-channelid-start-model-audioonlyhlssegmenttype) | False | Specifies the segment type. |

### AudioOnlyHlsTrackType
<a name="channels-channelid-start-model-audioonlyhlstracktype"></a>

Audio Only Hls Track Type
+ `ALTERNATE_AUDIO_AUTO_SELECT`
+ `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
+ `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
+ `AUDIO_ONLY_VARIANT_STREAM`

### AudioPid
<a name="channels-channelid-start-model-audiopid"></a>

Contains the packet identifier (PID) value and optional pre-mixer settings for a single audio stream within a source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | True | The packet identifier (PID) value from within the source. |
| premixSettings | [AudioPreMixerSettings](#channels-channelid-start-model-audiopremixersettings) | False | The optional audio pre-mixer settings for this PID. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this PID before interleaving. |

### AudioPidSelection
<a name="channels-channelid-start-model-audiopidselection"></a>

Audio Pid Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | True | Selects a specific PID from within a source. |
| pids | Array of type [AudioPid](#channels-channelid-start-model-audiopid) | False | Selects one or more unique packet identifiers (PIDs) from within a source. When using PIDs, you can specify per-PID audio pre-mixer settings. |

### AudioPreMixerSettings
<a name="channels-channelid-start-model-audiopremixersettings"></a>

Contains settings for preprocessing audio before interleaving, including loudness normalization, channel remixing, and gain adjustment. Apply these settings to individual PIDs or audio tracks to control audio output characteristics before the tracks are combined.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioNormalizationSettings | [AudioNormalizationSettings](#channels-channelid-start-model-audionormalizationsettings) | False | The audio normalization settings for loudness control. When specified, the service normalizes audio loudness according to the chosen algorithm. |
| channels | integer<br />Minimum: 1<br />Maximum: 16 | False | The number of audio channels to remix the audio to. If you don't specify a value, the service passes through the original channel count. The remixSettings setting overrides this value when specified. |
| gainDb | number<br />Minimum: -60<br />Maximum: 60 | False | The gain adjustment, in decibels (dB), to apply to this audio. |
| remixSettings | [RemixSettings](#channels-channelid-start-model-remixsettings) | False | The settings that control how the service remixes input audio channels. When specified, these settings provide fine-grained control over channel mapping and gain levels, and take precedence over the channels setting. |

### AudioSelector
<a name="channels-channelid-start-model-audioselector"></a>

Audio Selector

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string<br />MinLength: 1 | True | The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input. |
| selectorSettings | [AudioSelectorSettings](#channels-channelid-start-model-audioselectorsettings) | False | The audio selector settings. |

### AudioSelectorSettings
<a name="channels-channelid-start-model-audioselectorsettings"></a>

Audio Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioHlsRenditionSelection | [AudioHlsRenditionSelection](#channels-channelid-start-model-audiohlsrenditionselection) | False |  |
| audioLanguageSelection | [AudioLanguageSelection](#channels-channelid-start-model-audiolanguageselection) | False |  |
| audioPidSelection | [AudioPidSelection](#channels-channelid-start-model-audiopidselection) | False |  |
| audioTrackSelection | [AudioTrackSelection](#channels-channelid-start-model-audiotrackselection) | False |  |

### AudioSilenceFailoverSettings
<a name="channels-channelid-start-model-audiosilencefailoversettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectorName | string | True | The name of the audio selector in the input that MediaLive should monitor to detect silence. Select your most important rendition. If you didn't create an audio selector in this input, leave blank. |
| audioSilenceThresholdMsec | integer<br />Minimum: 1000 | False | The amount of time (in milliseconds) that the active input must be silent before automatic input failover occurs. Silence is defined as audio loss or audio quieter than -50 dBFS. |

### AudioTrack
<a name="channels-channelid-start-model-audiotrack"></a>

Audio Track

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| premixSettings | [AudioPreMixerSettings](#channels-channelid-start-model-audiopremixersettings) | False | The optional audio pre-mixer settings for this track. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this track before interleaving. |
| track | integer<br />Minimum: 1 | True | 1-based integer value that maps to a specific audio track |

### AudioTrackSelection
<a name="channels-channelid-start-model-audiotrackselection"></a>

Audio Track Selection

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tracks | Array of type [AudioTrack](#channels-channelid-start-model-audiotrack) | True | Selects one or more unique audio tracks from within a source. |

### AudioType
<a name="channels-channelid-start-model-audiotype"></a>

Audio Type
+ `CLEAN_EFFECTS`
+ `HEARING_IMPAIRED`
+ `UNDEFINED`
+ `VISUAL_IMPAIRED_COMMENTARY`

### AudioWatermarkSettings
<a name="channels-channelid-start-model-audiowatermarksettings"></a>

Audio Watermark Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nielsenWatermarksSettings | [NielsenWatermarksSettings](#channels-channelid-start-model-nielsenwatermarkssettings) | False | Settings to configure Nielsen Watermarks in the audio encode |

### AuthenticationScheme
<a name="channels-channelid-start-model-authenticationscheme"></a>

Authentication Scheme
+ `AKAMAI`
+ `COMMON`

### AutomaticInputFailoverSettings
<a name="channels-channelid-start-model-automaticinputfailoversettings"></a>

The settings for Automatic Input Failover.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorClearTimeMsec | integer<br />Minimum: 1 | False | This clear time defines the requirement a recovered input must meet to be considered healthy. The input must have no failover conditions for this length of time. Enter a time in milliseconds. This value is particularly important if the input\_preference for the failover pair is set to PRIMARY\_INPUT\_PREFERRED, because after this time, MediaLive will switch back to the primary input. |
| failoverConditions | Array of type [FailoverCondition](#channels-channelid-start-model-failovercondition) | False | A list of failover conditions. If any of these conditions occur, MediaLive will perform a failover to the other input. |
| inputPreference | [InputPreference](#channels-channelid-start-model-inputpreference) | False | Input preference when deciding which input to make active when a previously failed input has recovered. |
| secondaryInputId | string | True | The input ID of the secondary input in the automatic input failover pair. |

### AvailBlanking
<a name="channels-channelid-start-model-availblanking"></a>

Avail Blanking

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availBlankingImage | [InputLocation](#channels-channelid-start-model-inputlocation) | False | Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported. |
| state | [AvailBlankingState](#channels-channelid-start-model-availblankingstate) | False | When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added. |

### AvailBlankingState
<a name="channels-channelid-start-model-availblankingstate"></a>

Avail Blanking State
+ `DISABLED`
+ `ENABLED`

### AvailConfiguration
<a name="channels-channelid-start-model-availconfiguration"></a>

Avail Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availSettings | [AvailSettings](#channels-channelid-start-model-availsettings) | False | Ad avail settings. |

### AvailSettings
<a name="channels-channelid-start-model-availsettings"></a>

Avail Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scte35SpliceInsert | [Scte35SpliceInsert](#channels-channelid-start-model-scte35spliceinsert) | False |  |
| scte35TimeSignalApos | [Scte35TimeSignalApos](#channels-channelid-start-model-scte35timesignalapos) | False |  |

### BadGatewayException
<a name="channels-channelid-start-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BlackoutSlate
<a name="channels-channelid-start-model-blackoutslate"></a>

Blackout Slate

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackoutSlateImage | [InputLocation](#channels-channelid-start-model-inputlocation) | False | Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported. |
| networkEndBlackout | [BlackoutSlateNetworkEndBlackout](#channels-channelid-start-model-blackoutslatenetworkendblackout) | False | Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the "Network Blackout Image" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in "Network ID". |
| networkEndBlackoutImage | [InputLocation](#channels-channelid-start-model-inputlocation) | False | Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster. |
| networkId | string<br />MinLength: 34<br />MaxLength: 34 | False | Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C"). |
| state | [BlackoutSlateState](#channels-channelid-start-model-blackoutslatestate) | False | When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata. |

### BlackoutSlateNetworkEndBlackout
<a name="channels-channelid-start-model-blackoutslatenetworkendblackout"></a>

Blackout Slate Network End Blackout
+ `DISABLED`
+ `ENABLED`

### BlackoutSlateState
<a name="channels-channelid-start-model-blackoutslatestate"></a>

Blackout Slate State
+ `DISABLED`
+ `ENABLED`

### BurnInAlignment
<a name="channels-channelid-start-model-burninalignment"></a>

Burn In Alignment
+ `CENTERED`
+ `LEFT`
+ `SMART`

### BurnInBackgroundColor
<a name="channels-channelid-start-model-burninbackgroundcolor"></a>

Burn In Background Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### BurnInDestinationSettings
<a name="channels-channelid-start-model-burnindestinationsettings"></a>

Burn In Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [BurnInAlignment](#channels-channelid-start-model-burninalignment) | False | If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match. |
| backgroundColor | [BurnInBackgroundColor](#channels-channelid-start-model-burninbackgroundcolor) | False | Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| font | [InputLocation](#channels-channelid-start-model-inputlocation) | False | External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match. |
| fontColor | [BurnInFontColor](#channels-channelid-start-model-burninfontcolor) | False | Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match. |
| fontSize | string | False | When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match. |
| outlineColor | [BurnInOutlineColor](#channels-channelid-start-model-burninoutlinecolor) | False | Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| shadowColor | [BurnInShadowColor](#channels-channelid-start-model-burninshadowcolor) | False | Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| shadowXOffset | integer | False | Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match. |
| shadowYOffset | integer | False | Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match. |
| teletextGridControl | [BurnInTeletextGridControl](#channels-channelid-start-model-burninteletextgridcontrol) | False | Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs. |
| xPosition | integer<br />Minimum: 0 | False | Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match. |
| yPosition | integer<br />Minimum: 0 | False | Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match. |

### BurnInFontColor
<a name="channels-channelid-start-model-burninfontcolor"></a>

Burn In Font Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### BurnInOutlineColor
<a name="channels-channelid-start-model-burninoutlinecolor"></a>

Burn In Outline Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### BurnInShadowColor
<a name="channels-channelid-start-model-burninshadowcolor"></a>

Burn In Shadow Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### BurnInTeletextGridControl
<a name="channels-channelid-start-model-burninteletextgridcontrol"></a>

Burn In Teletext Grid Control
+ `FIXED`
+ `SCALED`

### CaptionDescription
<a name="channels-channelid-start-model-captiondescription"></a>

Caption Description

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionSelectorName | string | True | Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name. |
| destinationSettings | [CaptionDestinationSettings](#channels-channelid-start-model-captiondestinationsettings) | False | Additional settings for captions destination that depend on the destination type. |
| languageCode | string | False | ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/ |
| languageDescription | string | False | Human readable information to indicate captions available for players (eg. English, or Spanish). |
| name | string | True | Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event. |

### CaptionDestinationSettings
<a name="channels-channelid-start-model-captiondestinationsettings"></a>

Caption Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aribDestinationSettings | [AribDestinationSettings](#channels-channelid-start-model-aribdestinationsettings) | False |  |
| burnInDestinationSettings | [BurnInDestinationSettings](#channels-channelid-start-model-burnindestinationsettings) | False |  |
| dvbSubDestinationSettings | [DvbSubDestinationSettings](#channels-channelid-start-model-dvbsubdestinationsettings) | False |  |
| ebuTtDDestinationSettings | [EbuTtDDestinationSettings](#channels-channelid-start-model-ebuttddestinationsettings) | False |  |
| embeddedDestinationSettings | [EmbeddedDestinationSettings](#channels-channelid-start-model-embeddeddestinationsettings) | False |  |
| embeddedPlusScte20DestinationSettings | [EmbeddedPlusScte20DestinationSettings](#channels-channelid-start-model-embeddedplusscte20destinationsettings) | False |  |
| rtmpCaptionInfoDestinationSettings | [RtmpCaptionInfoDestinationSettings](#channels-channelid-start-model-rtmpcaptioninfodestinationsettings) | False |  |
| scte20PlusEmbeddedDestinationSettings | [Scte20PlusEmbeddedDestinationSettings](#channels-channelid-start-model-scte20plusembeddeddestinationsettings) | False |  |
| scte27DestinationSettings | [Scte27DestinationSettings](#channels-channelid-start-model-scte27destinationsettings) | False |  |
| smpteTtDestinationSettings | [SmpteTtDestinationSettings](#channels-channelid-start-model-smptettdestinationsettings) | False |  |
| teletextDestinationSettings | [TeletextDestinationSettings](#channels-channelid-start-model-teletextdestinationsettings) | False |  |
| ttmlDestinationSettings | [TtmlDestinationSettings](#channels-channelid-start-model-ttmldestinationsettings) | False |  |
| webvttDestinationSettings | [WebvttDestinationSettings](#channels-channelid-start-model-webvttdestinationsettings) | False |  |

### CaptionLanguageMapping
<a name="channels-channelid-start-model-captionlanguagemapping"></a>

Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionChannel | integer<br />Minimum: 1<br />Maximum: 4 | True | The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4) |
| languageCode | string<br />MinLength: 3<br />MaxLength: 3 | True | Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2) |
| languageDescription | string<br />MinLength: 1 | True | Textual description of language |

### CaptionRectangle
<a name="channels-channelid-start-model-captionrectangle"></a>

Caption Rectangle

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For height, specify the entire height of the rectangle as a percentage of the underlying frame height. For example, \\"80\\" means the rectangle height is 80% of the underlying frame height. The topOffset and rectangleHeight must add up to 100% or less. This field corresponds to tts:extent - Y in the TTML standard. |
| leftOffset | number<br />Minimum: 0<br />Maximum: 100 | True | Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. (Make sure to leave the default if you don't have either of these formats in the output.) You can define a display rectangle for the captions that is smaller than the underlying video frame. You define the rectangle by specifying the position of the left edge, top edge, bottom edge, and right edge of the rectangle, all within the underlying video frame. The units for the measurements are percentages. If you specify a value for one of these fields, you must specify a value for all of them. For leftOffset, specify the position of the left edge of the rectangle, as a percentage of the underlying frame width, and relative to the left edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame width. The rectangle left edge starts at that position from the left edge of the frame. This field corresponds to tts:origin - X in the TTML standard. |
| topOffset | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For topOffset, specify the position of the top edge of the rectangle, as a percentage of the underlying frame height, and relative to the top edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame height. The rectangle top edge starts at that position from the top edge of the frame. This field corresponds to tts:origin - Y in the TTML standard. |
| width | number<br />Minimum: 0<br />Maximum: 100 | True | See the description in leftOffset. For width, specify the entire width of the rectangle as a percentage of the underlying frame width. For example, \\"80\\" means the rectangle width is 80% of the underlying frame width. The leftOffset and rectangleWidth must add up to 100% or less. This field corresponds to tts:extent - X in the TTML standard. |

### CaptionSelector
<a name="channels-channelid-start-model-captionselector"></a>

Output groups for this Live Event. Output groups contain information about where streams should be distributed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | False | When specified this field indicates the three letter language code of the caption track to extract from the source. |
| name | string<br />MinLength: 1 | True | Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event. |
| selectorSettings | [CaptionSelectorSettings](#channels-channelid-start-model-captionselectorsettings) | False | Caption selector settings. |

### CaptionSelectorSettings
<a name="channels-channelid-start-model-captionselectorsettings"></a>

Caption Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ancillarySourceSettings | [AncillarySourceSettings](#channels-channelid-start-model-ancillarysourcesettings) | False |  |
| aribSourceSettings | [AribSourceSettings](#channels-channelid-start-model-aribsourcesettings) | False |  |
| dvbSubSourceSettings | [DvbSubSourceSettings](#channels-channelid-start-model-dvbsubsourcesettings) | False |  |
| embeddedSourceSettings | [EmbeddedSourceSettings](#channels-channelid-start-model-embeddedsourcesettings) | False |  |
| scte20SourceSettings | [Scte20SourceSettings](#channels-channelid-start-model-scte20sourcesettings) | False |  |
| scte27SourceSettings | [Scte27SourceSettings](#channels-channelid-start-model-scte27sourcesettings) | False |  |
| teletextSourceSettings | [TeletextSourceSettings](#channels-channelid-start-model-teletextsourcesettings) | False |  |

### CdiInputResolution
<a name="channels-channelid-start-model-cdiinputresolution"></a>

Maximum CDI input resolution; SD is 480i and 576i up to 30 frames-per-second (fps), HD is 720p up to 60 fps / 1080i up to 30 fps, FHD is 1080p up to 60 fps, UHD is 2160p up to 60 fps
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### CdiInputSpecification
<a name="channels-channelid-start-model-cdiinputspecification"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resolution | [CdiInputResolution](#channels-channelid-start-model-cdiinputresolution) | False | Maximum CDI input resolution |

### Channel
<a name="channels-channelid-start-model-channel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the channel. |
| cdiInputSpecification | [CdiInputSpecification](#channels-channelid-start-model-cdiinputspecification) | False | Specification of CDI inputs for this channel |
| channelClass | [ChannelClass](#channels-channelid-start-model-channelclass) | False | The class for this channel. STANDARD for a channel with two pipelines or SINGLE\_PIPELINE for a channel with one pipeline. |
| destinations | Array of type [OutputDestination](#channels-channelid-start-model-outputdestination) | False | A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.  |
| egressEndpoints | Array of type [ChannelEgressEndpoint](#channels-channelid-start-model-channelegressendpoint) | False | The endpoints where outgoing connections initiate from |
| encoderSettings | [EncoderSettings](#channels-channelid-start-model-encodersettings) | False |  |
| id | string | False | The unique ID of the channel. |
| inputAttachments | Array of type [InputAttachment](#channels-channelid-start-model-inputattachment) | False | List of input attachments for channel. |
| inputSpecification | [InputSpecification](#channels-channelid-start-model-inputspecification) | False | Specification of network and file inputs for this channel |
| logLevel | [LogLevel](#channels-channelid-start-model-loglevel) | False | The log level being written to CloudWatch Logs. |
| maintenance | [MaintenanceStatus](#channels-channelid-start-model-maintenancestatus) | False | Maintenance settings for this channel. |
| name | string | False | The name of the channel. (user-mutable) |
| pipelineDetails | Array of type [PipelineDetail](#channels-channelid-start-model-pipelinedetail) | False | Runtime details for the pipelines of a running channel. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role assumed when running the Channel. |
| state | [ChannelState](#channels-channelid-start-model-channelstate) | False |  |
| tags | [Tags](#channels-channelid-start-model-tags) | False | A collection of key-value pairs. |
| vpc | [VpcOutputSettingsDescription](#channels-channelid-start-model-vpcoutputsettingsdescription) | False | Settings for VPC output |

### ChannelClass
<a name="channels-channelid-start-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### ChannelEgressEndpoint
<a name="channels-channelid-start-model-channelegressendpoint"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceIp | string | False | Public IP of where a channel's output comes from |

### ChannelState
<a name="channels-channelid-start-model-channelstate"></a>
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

### ColorSpacePassthroughSettings
<a name="channels-channelid-start-model-colorspacepassthroughsettings"></a>

Passthrough applies no color space conversion to the output

### DvbNitSettings
<a name="channels-channelid-start-model-dvbnitsettings"></a>

DVB Network Information Table (NIT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkId | integer<br />Minimum: 0<br />Maximum: 65536 | True | The numeric value placed in the Network Information Table (NIT). |
| networkName | string<br />MinLength: 1<br />MaxLength: 256 | True | The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters. |
| repInterval | integer<br />Minimum: 25<br />Maximum: 10000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbSdtOutputSdt
<a name="channels-channelid-start-model-dvbsdtoutputsdt"></a>

Dvb Sdt Output Sdt
+ `SDT_FOLLOW`
+ `SDT_FOLLOW_IF_PRESENT`
+ `SDT_MANUAL`
+ `SDT_NONE`

### DvbSdtSettings
<a name="channels-channelid-start-model-dvbsdtsettings"></a>

DVB Service Description Table (SDT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputSdt | [DvbSdtOutputSdt](#channels-channelid-start-model-dvbsdtoutputsdt) | False | Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information. |
| repInterval | integer<br />Minimum: 25<br />Maximum: 2000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| serviceName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters. |
| serviceProviderName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters. |

### DvbSubDestinationAlignment
<a name="channels-channelid-start-model-dvbsubdestinationalignment"></a>

Dvb Sub Destination Alignment
+ `CENTERED`
+ `LEFT`
+ `SMART`

### DvbSubDestinationBackgroundColor
<a name="channels-channelid-start-model-dvbsubdestinationbackgroundcolor"></a>

Dvb Sub Destination Background Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### DvbSubDestinationFontColor
<a name="channels-channelid-start-model-dvbsubdestinationfontcolor"></a>

Dvb Sub Destination Font Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### DvbSubDestinationOutlineColor
<a name="channels-channelid-start-model-dvbsubdestinationoutlinecolor"></a>

Dvb Sub Destination Outline Color
+ `BLACK`
+ `BLUE`
+ `GREEN`
+ `RED`
+ `WHITE`
+ `YELLOW`

### DvbSubDestinationSettings
<a name="channels-channelid-start-model-dvbsubdestinationsettings"></a>

Dvb Sub Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [DvbSubDestinationAlignment](#channels-channelid-start-model-dvbsubdestinationalignment) | False | If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| backgroundColor | [DvbSubDestinationBackgroundColor](#channels-channelid-start-model-dvbsubdestinationbackgroundcolor) | False | Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| font | [InputLocation](#channels-channelid-start-model-inputlocation) | False | External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match. |
| fontColor | [DvbSubDestinationFontColor](#channels-channelid-start-model-dvbsubdestinationfontcolor) | False | Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match. |
| fontSize | string | False | When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match. |
| outlineColor | [DvbSubDestinationOutlineColor](#channels-channelid-start-model-dvbsubdestinationoutlinecolor) | False | Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| shadowColor | [DvbSubDestinationShadowColor](#channels-channelid-start-model-dvbsubdestinationshadowcolor) | False | Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match. |
| shadowXOffset | integer | False | Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match. |
| shadowYOffset | integer | False | Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match. |
| teletextGridControl | [DvbSubDestinationTeletextGridControl](#channels-channelid-start-model-dvbsubdestinationteletextgridcontrol) | False | Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs. |
| xPosition | integer<br />Minimum: 0 | False | Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |
| yPosition | integer<br />Minimum: 0 | False | Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match. |

### DvbSubDestinationShadowColor
<a name="channels-channelid-start-model-dvbsubdestinationshadowcolor"></a>

Dvb Sub Destination Shadow Color
+ `BLACK`
+ `NONE`
+ `WHITE`

### DvbSubDestinationTeletextGridControl
<a name="channels-channelid-start-model-dvbsubdestinationteletextgridcontrol"></a>

Dvb Sub Destination Teletext Grid Control
+ `FIXED`
+ `SCALED`

### DvbSubOcrLanguage
<a name="channels-channelid-start-model-dvbsubocrlanguage"></a>

Dvb Sub Ocr Language
+ `DEU`
+ `ENG`
+ `FRA`
+ `NLD`
+ `POR`
+ `SPA`

### DvbSubSourceSettings
<a name="channels-channelid-start-model-dvbsubsourcesettings"></a>

Dvb Sub Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ocrLanguage | [DvbSubOcrLanguage](#channels-channelid-start-model-dvbsubocrlanguage) | False | If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text. |
| pid | integer<br />Minimum: 1 | False | When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors. |

### DvbTdtSettings
<a name="channels-channelid-start-model-dvbtdtsettings"></a>

DVB Time and Date Table (SDT)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| repInterval | integer<br />Minimum: 1000<br />Maximum: 30000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### Eac3AttenuationControl
<a name="channels-channelid-start-model-eac3attenuationcontrol"></a>

Eac3 Attenuation Control
+ `ATTENUATE_3_DB`
+ `NONE`

### Eac3BitstreamMode
<a name="channels-channelid-start-model-eac3bitstreammode"></a>

Eac3 Bitstream Mode
+ `COMMENTARY`
+ `COMPLETE_MAIN`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `VISUALLY_IMPAIRED`

### Eac3CodingMode
<a name="channels-channelid-start-model-eac3codingmode"></a>

Eac3 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2`

### Eac3DcFilter
<a name="channels-channelid-start-model-eac3dcfilter"></a>

Eac3 Dc Filter
+ `DISABLED`
+ `ENABLED`

### Eac3DrcLine
<a name="channels-channelid-start-model-eac3drcline"></a>

Eac3 Drc Line
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3DrcRf
<a name="channels-channelid-start-model-eac3drcrf"></a>

Eac3 Drc Rf
+ `FILM_LIGHT`
+ `FILM_STANDARD`
+ `MUSIC_LIGHT`
+ `MUSIC_STANDARD`
+ `NONE`
+ `SPEECH`

### Eac3LfeControl
<a name="channels-channelid-start-model-eac3lfecontrol"></a>

Eac3 Lfe Control
+ `LFE`
+ `NO_LFE`

### Eac3LfeFilter
<a name="channels-channelid-start-model-eac3lfefilter"></a>

Eac3 Lfe Filter
+ `DISABLED`
+ `ENABLED`

### Eac3MetadataControl
<a name="channels-channelid-start-model-eac3metadatacontrol"></a>

Eac3 Metadata Control
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Eac3PassthroughControl
<a name="channels-channelid-start-model-eac3passthroughcontrol"></a>

Eac3 Passthrough Control
+ `NO_PASSTHROUGH`
+ `WHEN_POSSIBLE`

### Eac3PhaseControl
<a name="channels-channelid-start-model-eac3phasecontrol"></a>

Eac3 Phase Control
+ `NO_SHIFT`
+ `SHIFT_90_DEGREES`

### Eac3Settings
<a name="channels-channelid-start-model-eac3settings"></a>

Eac3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attenuationControl | [Eac3AttenuationControl](#channels-channelid-start-model-eac3attenuationcontrol) | False | When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode. |
| bitrate | number | False | Average bitrate in bits/second. Valid bitrates depend on the coding mode. |
| bitstreamMode | [Eac3BitstreamMode](#channels-channelid-start-model-eac3bitstreammode) | False | Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values. |
| codingMode | [Eac3CodingMode](#channels-channelid-start-model-eac3codingmode) | False | Dolby Digital Plus coding mode. Determines number of channels. |
| dcFilter | [Eac3DcFilter](#channels-channelid-start-model-eac3dcfilter) | False | When set to enabled, activates a DC highpass filter for all input channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through. |
| drcLine | [Eac3DrcLine](#channels-channelid-start-model-eac3drcline) | False | Sets the Dolby dynamic range compression profile. |
| drcRf | [Eac3DrcRf](#channels-channelid-start-model-eac3drcrf) | False | Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels. |
| lfeControl | [Eac3LfeControl](#channels-channelid-start-model-eac3lfecontrol) | False | When encoding 3/2 audio, setting to lfe enables the LFE channel |
| lfeFilter | [Eac3LfeFilter](#channels-channelid-start-model-eac3lfefilter) | False | When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode. |
| loRoCenterMixLevel | number | False | Left only/Right only center mix level. Only used for 3/2 coding mode. |
| loRoSurroundMixLevel | number | False | Left only/Right only surround mix level. Only used for 3/2 coding mode. |
| ltRtCenterMixLevel | number | False | Left total/Right total center mix level. Only used for 3/2 coding mode. |
| ltRtSurroundMixLevel | number | False | Left total/Right total surround mix level. Only used for 3/2 coding mode. |
| metadataControl | [Eac3MetadataControl](#channels-channelid-start-model-eac3metadatacontrol) | False | When set to followInput, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| passthroughControl | [Eac3PassthroughControl](#channels-channelid-start-model-eac3passthroughcontrol) | False | When set to whenPossible, input DD\+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding. |
| phaseControl | [Eac3PhaseControl](#channels-channelid-start-model-eac3phasecontrol) | False | When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode. |
| stereoDownmix | [Eac3StereoDownmix](#channels-channelid-start-model-eac3stereodownmix) | False | Stereo downmix preference. Only used for 3/2 coding mode. |
| surroundExMode | [Eac3SurroundExMode](#channels-channelid-start-model-eac3surroundexmode) | False | When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels. |
| surroundMode | [Eac3SurroundMode](#channels-channelid-start-model-eac3surroundmode) | False | When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels. |

### Eac3StereoDownmix
<a name="channels-channelid-start-model-eac3stereodownmix"></a>

Eac3 Stereo Downmix
+ `DPL2`
+ `LO_RO`
+ `LT_RT`
+ `NOT_INDICATED`

### Eac3SurroundExMode
<a name="channels-channelid-start-model-eac3surroundexmode"></a>

Eac3 Surround Ex Mode
+ `DISABLED`
+ `ENABLED`
+ `NOT_INDICATED`

### Eac3SurroundMode
<a name="channels-channelid-start-model-eac3surroundmode"></a>

Eac3 Surround Mode
+ `DISABLED`
+ `ENABLED`
+ `NOT_INDICATED`

### EbuTtDDestinationSettings
<a name="channels-channelid-start-model-ebuttddestinationsettings"></a>

Ebu Tt DDestination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyrightHolder | string<br />MaxLength: 1000 | False | Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. Complete this field if you want to include the name of the copyright holder in the copyright metadata tag in the TTML |
| fillLineGap | [EbuTtDFillLineGapControl](#channels-channelid-start-model-ebuttdfilllinegapcontrol) | False | Specifies how to handle the gap between the lines (in multi-line captions). - enabled: Fill with the captions background color (as specified in the input captions). - disabled: Leave the gap unfilled. |
| fontFamily | string | False | Specifies the font family to include in the font data attached to the EBU-TT captions. Valid only if styleControl is set to include. If you leave this field empty, the font family is set to "monospaced". (If styleControl is set to exclude, the font family is always set to "monospaced".) You specify only the font family. All other style information (color, bold, position and so on) is copied from the input captions. The size is always set to 100% to allow the downstream player to choose the size. - Enter a list of font families, as a comma-separated list of font names, in order of preference. The name can be a font family (such as “Arial”), or a generic font family (such as “serif”), or “default” (to let the downstream player choose the font). - Leave blank to set the family to “monospace”. |
| styleControl | [EbuTtDDestinationStyleControl](#channels-channelid-start-model-ebuttddestinationstylecontrol) | False | Specifies the style information (font color, font position, and so on) to include in the font data that is attached to the EBU-TT captions. - include: Take the style information (font color, font position, and so on) from the source captions and include that information in the font data attached to the EBU-TT captions. This option is valid only if the source captions are Embedded or Teletext. - exclude: In the font data attached to the EBU-TT captions, set the font family to "monospaced". Do not include any other style information. |

### EbuTtDDestinationStyleControl
<a name="channels-channelid-start-model-ebuttddestinationstylecontrol"></a>

Ebu Tt DDestination Style Control
+ `EXCLUDE`
+ `INCLUDE`

### EbuTtDFillLineGapControl
<a name="channels-channelid-start-model-ebuttdfilllinegapcontrol"></a>

Ebu Tt DFill Line Gap Control
+ `DISABLED`
+ `ENABLED`

### EmbeddedConvert608To708
<a name="channels-channelid-start-model-embeddedconvert608to708"></a>

Embedded Convert608 To708
+ `DISABLED`
+ `UPCONVERT`

### EmbeddedDestinationSettings
<a name="channels-channelid-start-model-embeddeddestinationsettings"></a>

Embedded Destination Settings

### EmbeddedPlusScte20DestinationSettings
<a name="channels-channelid-start-model-embeddedplusscte20destinationsettings"></a>

Embedded Plus Scte20 Destination Settings

### EmbeddedScte20Detection
<a name="channels-channelid-start-model-embeddedscte20detection"></a>

Embedded Scte20 Detection
+ `AUTO`
+ `OFF`

### EmbeddedSourceSettings
<a name="channels-channelid-start-model-embeddedsourcesettings"></a>

Embedded Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [EmbeddedConvert608To708](#channels-channelid-start-model-embeddedconvert608to708) | False | If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded. |
| scte20Detection | [EmbeddedScte20Detection](#channels-channelid-start-model-embeddedscte20detection) | False | Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions. |
| source608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough. |
| source608TrackNumber | integer<br />Minimum: 1<br />Maximum: 5 | False | This field is unused and deprecated. |

### EncoderSettings
<a name="channels-channelid-start-model-encodersettings"></a>

Encoder Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptions | Array of type [AudioDescription](#channels-channelid-start-model-audiodescription) | True |  |
| availBlanking | [AvailBlanking](#channels-channelid-start-model-availblanking) | False | Settings for ad avail blanking. |
| availConfiguration | [AvailConfiguration](#channels-channelid-start-model-availconfiguration) | False | Event-wide configuration settings for ad avail insertion. |
| blackoutSlate | [BlackoutSlate](#channels-channelid-start-model-blackoutslate) | False | Settings for blackout slate. |
| captionDescriptions | Array of type [CaptionDescription](#channels-channelid-start-model-captiondescription) | False | Settings for caption decriptions |
| featureActivations | [FeatureActivations](#channels-channelid-start-model-featureactivations) | False | Feature Activations |
| globalConfiguration | [GlobalConfiguration](#channels-channelid-start-model-globalconfiguration) | False | Configuration settings that apply to the event as a whole. |
| motionGraphicsConfiguration | [MotionGraphicsConfiguration](#channels-channelid-start-model-motiongraphicsconfiguration) | False | Settings for motion graphics. |
| nielsenConfiguration | [NielsenConfiguration](#channels-channelid-start-model-nielsenconfiguration) | False | Nielsen configuration settings. |
| outputGroups | Array of type [OutputGroup](#channels-channelid-start-model-outputgroup) | True |  |
| timecodeConfig | [TimecodeConfig](#channels-channelid-start-model-timecodeconfig) | True | Contains settings used to acquire and adjust timecode information from inputs. |
| videoDescriptions | Array of type [VideoDescription](#channels-channelid-start-model-videodescription) | True |  |

### FailoverCondition
<a name="channels-channelid-start-model-failovercondition"></a>

Failover Condition settings. There can be multiple failover conditions inside AutomaticInputFailoverSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| failoverConditionSettings | [FailoverConditionSettings](#channels-channelid-start-model-failoverconditionsettings) | False | Failover condition type-specific settings. |

### FailoverConditionSettings
<a name="channels-channelid-start-model-failoverconditionsettings"></a>

Settings for one failover condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSilenceSettings | [AudioSilenceFailoverSettings](#channels-channelid-start-model-audiosilencefailoversettings) | False | MediaLive will perform a failover if the specified audio selector is silent for the specified period. |
| inputLossSettings | [InputLossFailoverSettings](#channels-channelid-start-model-inputlossfailoversettings) | False | MediaLive will perform a failover if content is not detected in this input for the specified period. |
| videoBlackSettings | [VideoBlackFailoverSettings](#channels-channelid-start-model-videoblackfailoversettings) | False | MediaLive will perform a failover if content is considered black for the specified period. |

### FeatureActivations
<a name="channels-channelid-start-model-featureactivations"></a>

Feature Activations

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputPrepareScheduleActions | [FeatureActivationsInputPrepareScheduleActions](#channels-channelid-start-model-featureactivationsinputpreparescheduleactions) | False | Enables the Input Prepare feature. You can create Input Prepare actions in the schedule only if this feature is enabled. If you disable the feature on an existing schedule, make sure that you first delete all input prepare actions from the schedule. |

### FeatureActivationsInputPrepareScheduleActions
<a name="channels-channelid-start-model-featureactivationsinputpreparescheduleactions"></a>

Feature Activations Input Prepare Schedule Actions
+ `DISABLED`
+ `ENABLED`

### FecOutputIncludeFec
<a name="channels-channelid-start-model-fecoutputincludefec"></a>

Fec Output Include Fec
+ `COLUMN`
+ `COLUMN_AND_ROW`

### FecOutputSettings
<a name="channels-channelid-start-model-fecoutputsettings"></a>

Fec Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| columnDepth | integer<br />Minimum: 4<br />Maximum: 20 | False | Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive. |
| includeFec | [FecOutputIncludeFec](#channels-channelid-start-model-fecoutputincludefec) | False | Enables column only or column and row based FEC |
| rowLength | integer<br />Minimum: 1<br />Maximum: 20 | False | Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive. |

### FixedAfd
<a name="channels-channelid-start-model-fixedafd"></a>

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
<a name="channels-channelid-start-model-fmp4hlssettings"></a>

Fmp4 Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioRenditionSets | string | False | List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','. |
| nielsenId3Behavior | [Fmp4NielsenId3Behavior](#channels-channelid-start-model-fmp4nielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| timedMetadataBehavior | [Fmp4TimedMetadataBehavior](#channels-channelid-start-model-fmp4timedmetadatabehavior) | False | When set to passthrough, timed metadata is passed through from input to output. |

### Fmp4NielsenId3Behavior
<a name="channels-channelid-start-model-fmp4nielsenid3behavior"></a>

Fmp4 Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### Fmp4TimedMetadataBehavior
<a name="channels-channelid-start-model-fmp4timedmetadatabehavior"></a>

Fmp4 Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### FrameCaptureCdnSettings
<a name="channels-channelid-start-model-framecapturecdnsettings"></a>

Frame Capture Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| frameCaptureS3Settings | [FrameCaptureS3Settings](#channels-channelid-start-model-framecaptures3settings) | False |  |

### FrameCaptureGroupSettings
<a name="channels-channelid-start-model-framecapturegroupsettings"></a>

Frame Capture Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | The destination for the frame capture files. Either the URI for an Amazon S3 bucket and object, plus a file name prefix (for example, s3ssl://sportsDelivery/highlights/20180820/curling-) or the URI for a MediaStore container, plus a file name prefix (for example, mediastoressl://sportsDelivery/20180820/curling-). The final file names consist of the prefix from the destination field (for example, "curling-") \+ name modifier \+ the counter (5 digits, starting from 00001) \+ extension (which is always .jpg). For example, curling-low.00001.jpg |
| frameCaptureCdnSettings | [FrameCaptureCdnSettings](#channels-channelid-start-model-framecapturecdnsettings) | False | Parameters that control interactions with the CDN. |

### FrameCaptureHlsSettings
<a name="channels-channelid-start-model-framecapturehlssettings"></a>

Frame Capture Hls Settings

### FrameCaptureIntervalUnit
<a name="channels-channelid-start-model-framecaptureintervalunit"></a>

Frame Capture Interval Unit
+ `MILLISECONDS`
+ `SECONDS`

### FrameCaptureOutputSettings
<a name="channels-channelid-start-model-framecaptureoutputsettings"></a>

Frame Capture Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nameModifier | string | False | Required if the output group contains more than one output. This modifier forms part of the output file name. |

### FrameCaptureS3LogUploads
<a name="channels-channelid-start-model-framecaptures3loguploads"></a>

Frame Capture S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### FrameCaptureS3Settings
<a name="channels-channelid-start-model-framecaptures3settings"></a>

Frame Capture S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-channelid-start-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [FrameCaptureS3LogUploads](#channels-channelid-start-model-framecaptures3loguploads) | False | When set to enabled, each upload to CDN or server will be logged. |

### FrameCaptureSettings
<a name="channels-channelid-start-model-framecapturesettings"></a>

Frame Capture Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captureInterval | integer<br />Minimum: 1<br />Maximum: 3600000 | False | The frequency at which to capture frames for inclusion in the output. May be specified in either seconds or milliseconds, as specified by captureIntervalUnits. |
| captureIntervalUnits | [FrameCaptureIntervalUnit](#channels-channelid-start-model-framecaptureintervalunit) | False | Unit for the frame capture interval. |

### GatewayTimeoutException
<a name="channels-channelid-start-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GlobalConfiguration
<a name="channels-channelid-start-model-globalconfiguration"></a>

Global Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| initialAudioGain | integer<br />Minimum: -60<br />Maximum: 60 | False | Value to set the initial audio gain for the Live Event. |
| inputEndAction | [GlobalConfigurationInputEndAction](#channels-channelid-start-model-globalconfigurationinputendaction) | False | Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When "none" is configured the encoder will transcode either black, a solid color, or a user specified slate images per the "Input Loss Behavior" configuration until the next input switch occurs (which is controlled through the Channel Schedule API). |
| inputLossBehavior | [InputLossBehavior](#channels-channelid-start-model-inputlossbehavior) | False | Settings for system actions when input is lost. |
| outputLockingMode | [GlobalConfigurationOutputLockingMode](#channels-channelid-start-model-globalconfigurationoutputlockingmode) | False | Indicates how MediaLive pipelines are synchronized. PIPELINE\_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the other. EPOCH\_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the Unix epoch. |
| outputTimingSource | [GlobalConfigurationOutputTimingSource](#channels-channelid-start-model-globalconfigurationoutputtimingsource) | False | Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream. |
| supportLowFramerateInputs | [GlobalConfigurationLowFramerateInputs](#channels-channelid-start-model-globalconfigurationlowframerateinputs) | False | Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second. |

### GlobalConfigurationInputEndAction
<a name="channels-channelid-start-model-globalconfigurationinputendaction"></a>

Global Configuration Input End Action
+ `NONE`
+ `SWITCH_AND_LOOP_INPUTS`

### GlobalConfigurationLowFramerateInputs
<a name="channels-channelid-start-model-globalconfigurationlowframerateinputs"></a>

Global Configuration Low Framerate Inputs
+ `DISABLED`
+ `ENABLED`

### GlobalConfigurationOutputLockingMode
<a name="channels-channelid-start-model-globalconfigurationoutputlockingmode"></a>

Global Configuration Output Locking Mode
+ `EPOCH_LOCKING`
+ `PIPELINE_LOCKING`

### GlobalConfigurationOutputTimingSource
<a name="channels-channelid-start-model-globalconfigurationoutputtimingsource"></a>

Global Configuration Output Timing Source
+ `INPUT_CLOCK`
+ `SYSTEM_CLOCK`

### H264AdaptiveQuantization
<a name="channels-channelid-start-model-h264adaptivequantization"></a>

H264 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `HIGHER`
+ `LOW`
+ `MAX`
+ `MEDIUM`
+ `OFF`

### H264ColorMetadata
<a name="channels-channelid-start-model-h264colormetadata"></a>

H264 Color Metadata
+ `IGNORE`
+ `INSERT`

### H264ColorSpaceSettings
<a name="channels-channelid-start-model-h264colorspacesettings"></a>

H264 Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpacePassthroughSettings | [ColorSpacePassthroughSettings](#channels-channelid-start-model-colorspacepassthroughsettings) | False |  |
| rec601Settings | [Rec601Settings](#channels-channelid-start-model-rec601settings) | False |  |
| rec709Settings | [Rec709Settings](#channels-channelid-start-model-rec709settings) | False |  |

### H264EntropyEncoding
<a name="channels-channelid-start-model-h264entropyencoding"></a>

H264 Entropy Encoding
+ `CABAC`
+ `CAVLC`

### H264FilterSettings
<a name="channels-channelid-start-model-h264filtersettings"></a>

H264 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| temporalFilterSettings | [TemporalFilterSettings](#channels-channelid-start-model-temporalfiltersettings) | False |  |

### H264FlickerAq
<a name="channels-channelid-start-model-h264flickeraq"></a>

H264 Flicker Aq
+ `DISABLED`
+ `ENABLED`

### H264ForceFieldPictures
<a name="channels-channelid-start-model-h264forcefieldpictures"></a>

H264 Force Field Pictures
+ `DISABLED`
+ `ENABLED`

### H264FramerateControl
<a name="channels-channelid-start-model-h264frameratecontrol"></a>

H264 Framerate Control
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264GopBReference
<a name="channels-channelid-start-model-h264gopbreference"></a>

H264 Gop BReference
+ `DISABLED`
+ `ENABLED`

### H264GopSizeUnits
<a name="channels-channelid-start-model-h264gopsizeunits"></a>

H264 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### H264Level
<a name="channels-channelid-start-model-h264level"></a>

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
<a name="channels-channelid-start-model-h264lookaheadratecontrol"></a>

H264 Look Ahead Rate Control
+ `HIGH`
+ `LOW`
+ `MEDIUM`

### H264ParControl
<a name="channels-channelid-start-model-h264parcontrol"></a>

H264 Par Control
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264Profile
<a name="channels-channelid-start-model-h264profile"></a>

H264 Profile
+ `BASELINE`
+ `HIGH`
+ `HIGH_10BIT`
+ `HIGH_422`
+ `HIGH_422_10BIT`
+ `MAIN`

### H264QualityLevel
<a name="channels-channelid-start-model-h264qualitylevel"></a>

H264 Quality Level
+ `ENHANCED_QUALITY`
+ `STANDARD_QUALITY`

### H264RateControlMode
<a name="channels-channelid-start-model-h264ratecontrolmode"></a>

H264 Rate Control Mode
+ `CBR`
+ `MULTIPLEX`
+ `QVBR`
+ `VBR`

### H264ScanType
<a name="channels-channelid-start-model-h264scantype"></a>

H264 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### H264SceneChangeDetect
<a name="channels-channelid-start-model-h264scenechangedetect"></a>

H264 Scene Change Detect
+ `DISABLED`
+ `ENABLED`

### H264Settings
<a name="channels-channelid-start-model-h264settings"></a>

H264 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H264AdaptiveQuantization](#channels-channelid-start-model-h264adaptivequantization) | False | Enables or disables adaptive quantization, which is a technique MediaLive can apply to video on a frame-by-frame basis to produce more compression without losing quality. There are three types of adaptive quantization: flicker, spatial, and temporal. Set the field in one of these ways: Set to Auto. Recommended. For each type of AQ, MediaLive will determine if AQ is needed, and if so, the appropriate strength. Set a strength (a value other than Auto or Disable). This strength will apply to any of the AQ fields that you choose to enable. Set to Disabled to disable all types of adaptive quantization. |
| afdSignaling | [AfdSignaling](#channels-channelid-start-model-afdsignaling) | False | Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter. |
| bitrate | integer<br />Minimum: 1000 | False | Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000. |
| bufFillPct | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| bufSize | integer<br />Minimum: 0 | False | Size of buffer (HRD buffer model) in bits. |
| colorMetadata | [H264ColorMetadata](#channels-channelid-start-model-h264colormetadata) | False | Includes colorspace metadata in the output. |
| colorSpaceSettings | [H264ColorSpaceSettings](#channels-channelid-start-model-h264colorspacesettings) | False | Color Space settings |
| entropyEncoding | [H264EntropyEncoding](#channels-channelid-start-model-h264entropyencoding) | False | Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc. |
| filterSettings | [H264FilterSettings](#channels-channelid-start-model-h264filtersettings) | False | Optional filters that you can apply to an encode. |
| fixedAfd | [FixedAfd](#channels-channelid-start-model-fixedafd) | False | Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'. |
| flickerAq | [H264FlickerAq](#channels-channelid-start-model-h264flickeraq) | False | Flicker AQ makes adjustments within each frame to reduce flicker or 'pop' on I-frames. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if flicker AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply flicker AQ using the specified strength. Disabled: MediaLive won't apply flicker AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply flicker AQ. |
| forceFieldPictures | [H264ForceFieldPictures](#channels-channelid-start-model-h264forcefieldpictures) | False | This setting applies only when scan type is "interlaced." It controls whether coding is performed on a field basis or on a frame basis. (When the video is progressive, the coding is always performed on a frame basis.) enabled: Force MediaLive to code on a field basis, so that odd and even sets of fields are coded separately. disabled: Code the two sets of fields separately (on a field basis) or together (on a frame basis using PAFF), depending on what is most appropriate for the content. |
| framerateControl | [H264FramerateControl](#channels-channelid-start-model-h264frameratecontrol) | False | This field indicates how the output video frame rate is specified. If "specified" is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if "initializeFromSource" is selected then the output video frame rate will be set equal to the input video frame rate of the first input. |
| framerateDenominator | integer<br />Minimum: 1 | False | Framerate denominator. |
| framerateNumerator | integer<br />Minimum: 1 | False | Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps. |
| gopBReference | [H264GopBReference](#channels-channelid-start-model-h264gopbreference) | False | If enabled, use reference B frames for GOP structures that have B frames > 1. |
| gopClosedCadence | integer<br />Minimum: 0 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| gopNumBFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Number of B-frames between reference frames. |
| gopSize | number | False | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer. |
| gopSizeUnits | [H264GopSizeUnits](#channels-channelid-start-model-h264gopsizeunits) | False | Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time. |
| level | [H264Level](#channels-channelid-start-model-h264level) | False | H.264 Level. |
| lookAheadRateControl | [H264LookAheadRateControl](#channels-channelid-start-model-h264lookaheadratecontrol) | False | Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content. |
| maxBitrate | integer<br />Minimum: 1000 | False | For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size \+ Min-I-interval - 1 |
| numRefFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H264ParControl](#channels-channelid-start-model-h264parcontrol) | False | This field indicates how the output pixel aspect ratio is specified. If "specified" is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if "initializeFromSource" is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input. |
| parDenominator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio denominator. |
| parNumerator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio numerator. |
| profile | [H264Profile](#channels-channelid-start-model-h264profile) | False | H.264 Profile. |
| qualityLevel | [H264QualityLevel](#channels-channelid-start-model-h264qualitylevel) | False | Leave as STANDARD\_QUALITY or choose a different value (which might result in additional costs to run the channel). - ENHANCED\_QUALITY: Produces a slightly better video quality without an increase in the bitrate. Has an effect only when the Rate control mode is QVBR or CBR. If this channel is in a MediaLive multiplex, the value must be ENHANCED\_QUALITY. - STANDARD\_QUALITY: Valid for any Rate control mode. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. You can set a target quality or you can let MediaLive determine the best quality. To set a target quality, enter values in the QVBR quality level field and the Max bitrate field. Enter values that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M To let MediaLive decide, leave the QVBR quality level field empty, and in Max bitrate enter the maximum rate you want in the video. For more information, see the section called "Video - rate control mode" in the MediaLive user guide |
| rateControlMode | [H264RateControlMode](#channels-channelid-start-model-h264ratecontrolmode) | False | Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program. |
| scanType | [H264ScanType](#channels-channelid-start-model-h264scantype) | False | Sets the scan type of the output to progressive or top-field-first interlaced. |
| sceneChangeDetect | [H264SceneChangeDetect](#channels-channelid-start-model-h264scenechangedetect) | False | Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image. If not set to zero, must be greater than 15. |
| spatialAq | [H264SpatialAq](#channels-channelid-start-model-h264spatialaq) | False | Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if spatial AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply spatial AQ using the specified strength. Disabled: MediaLive won't apply spatial AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply spatial AQ. |
| subgopLength | [H264SubGopLength](#channels-channelid-start-model-h264subgoplength) | False | If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality. |
| syntax | [H264Syntax](#channels-channelid-start-model-h264syntax) | False | Produces a bitstream compliant with SMPTE RP-2027. |
| temporalAq | [H264TemporalAq](#channels-channelid-start-model-h264temporalaq) | False | Temporal makes adjustments within each frame based on temporal variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if temporal AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply temporal AQ using the specified strength. Disabled: MediaLive won't apply temporal AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesn't apply temporal AQ. |
| timecodeInsertion | [H264TimecodeInsertionBehavior](#channels-channelid-start-model-h264timecodeinsertionbehavior) | False | Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config |

### H264SpatialAq
<a name="channels-channelid-start-model-h264spatialaq"></a>

H264 Spatial Aq
+ `DISABLED`
+ `ENABLED`

### H264SubGopLength
<a name="channels-channelid-start-model-h264subgoplength"></a>

H264 Sub Gop Length
+ `DYNAMIC`
+ `FIXED`

### H264Syntax
<a name="channels-channelid-start-model-h264syntax"></a>

H264 Syntax
+ `DEFAULT`
+ `RP2027`

### H264TemporalAq
<a name="channels-channelid-start-model-h264temporalaq"></a>

H264 Temporal Aq
+ `DISABLED`
+ `ENABLED`

### H264TimecodeInsertionBehavior
<a name="channels-channelid-start-model-h264timecodeinsertionbehavior"></a>

H264 Timecode Insertion Behavior
+ `DISABLED`
+ `PIC_TIMING_SEI`

### H265AdaptiveQuantization
<a name="channels-channelid-start-model-h265adaptivequantization"></a>

H265 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `HIGHER`
+ `LOW`
+ `MAX`
+ `MEDIUM`
+ `OFF`

### H265AlternativeTransferFunction
<a name="channels-channelid-start-model-h265alternativetransferfunction"></a>

H265 Alternative Transfer Function
+ `INSERT`
+ `OMIT`

### H265ColorMetadata
<a name="channels-channelid-start-model-h265colormetadata"></a>

H265 Color Metadata
+ `IGNORE`
+ `INSERT`

### H265ColorSpaceSettings
<a name="channels-channelid-start-model-h265colorspacesettings"></a>

H265 Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpacePassthroughSettings | [ColorSpacePassthroughSettings](#channels-channelid-start-model-colorspacepassthroughsettings) | False |  |
| hdr10Settings | [Hdr10Settings](#channels-channelid-start-model-hdr10settings) | False |  |
| rec601Settings | [Rec601Settings](#channels-channelid-start-model-rec601settings) | False |  |
| rec709Settings | [Rec709Settings](#channels-channelid-start-model-rec709settings) | False |  |

### H265FilterSettings
<a name="channels-channelid-start-model-h265filtersettings"></a>

H265 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| temporalFilterSettings | [TemporalFilterSettings](#channels-channelid-start-model-temporalfiltersettings) | False |  |

### H265FlickerAq
<a name="channels-channelid-start-model-h265flickeraq"></a>

H265 Flicker Aq
+ `DISABLED`
+ `ENABLED`

### H265GopSizeUnits
<a name="channels-channelid-start-model-h265gopsizeunits"></a>

H265 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### H265Level
<a name="channels-channelid-start-model-h265level"></a>

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
<a name="channels-channelid-start-model-h265lookaheadratecontrol"></a>

H265 Look Ahead Rate Control
+ `HIGH`
+ `LOW`
+ `MEDIUM`

### H265Profile
<a name="channels-channelid-start-model-h265profile"></a>

H265 Profile
+ `MAIN`
+ `MAIN_10BIT`

### H265RateControlMode
<a name="channels-channelid-start-model-h265ratecontrolmode"></a>

H265 Rate Control Mode
+ `CBR`
+ `MULTIPLEX`
+ `QVBR`

### H265ScanType
<a name="channels-channelid-start-model-h265scantype"></a>

H265 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### H265SceneChangeDetect
<a name="channels-channelid-start-model-h265scenechangedetect"></a>

H265 Scene Change Detect
+ `DISABLED`
+ `ENABLED`

### H265Settings
<a name="channels-channelid-start-model-h265settings"></a>

H265 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H265AdaptiveQuantization](#channels-channelid-start-model-h265adaptivequantization) | False | Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality. |
| afdSignaling | [AfdSignaling](#channels-channelid-start-model-afdsignaling) | False | Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter. |
| alternativeTransferFunction | [H265AlternativeTransferFunction](#channels-channelid-start-model-h265alternativetransferfunction) | False | Whether or not EML should insert an Alternative Transfer Function SEI message to support backwards compatibility with non-HDR decoders and displays. |
| bitrate | integer<br />Minimum: 100000<br />Maximum: 40000000 | False | Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000. |
| bufSize | integer<br />Minimum: 100000<br />Maximum: 80000000 | False | Size of buffer (HRD buffer model) in bits. |
| colorMetadata | [H265ColorMetadata](#channels-channelid-start-model-h265colormetadata) | False | Includes colorspace metadata in the output. |
| colorSpaceSettings | [H265ColorSpaceSettings](#channels-channelid-start-model-h265colorspacesettings) | False | Color Space settings |
| filterSettings | [H265FilterSettings](#channels-channelid-start-model-h265filtersettings) | False | Optional filters that you can apply to an encode. |
| fixedAfd | [FixedAfd](#channels-channelid-start-model-fixedafd) | False | Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'. |
| flickerAq | [H265FlickerAq](#channels-channelid-start-model-h265flickeraq) | False | If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 3003 | True | Framerate denominator. |
| framerateNumerator | integer<br />Minimum: 1 | True | Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps. |
| gopClosedCadence | integer<br />Minimum: 0 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| gopSize | number | False | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer. |
| gopSizeUnits | [H265GopSizeUnits](#channels-channelid-start-model-h265gopsizeunits) | False | Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time. |
| level | [H265Level](#channels-channelid-start-model-h265level) | False | H.265 Level. |
| lookAheadRateControl | [H265LookAheadRateControl](#channels-channelid-start-model-h265lookaheadratecontrol) | False | Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content. |
| maxBitrate | integer<br />Minimum: 100000<br />Maximum: 40000000 | False | For QVBR: See the tooltip for Quality level |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size \+ Min-I-interval - 1 |
| parDenominator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio denominator. |
| parNumerator | integer<br />Minimum: 1 | False | Pixel Aspect Ratio numerator. |
| profile | [H265Profile](#channels-channelid-start-model-h265profile) | False | H.265 Profile. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M |
| rateControlMode | [H265RateControlMode](#channels-channelid-start-model-h265ratecontrolmode) | False | Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program. |
| scanType | [H265ScanType](#channels-channelid-start-model-h265scantype) | False | Sets the scan type of the output to progressive or top-field-first interlaced. |
| sceneChangeDetect | [H265SceneChangeDetect](#channels-channelid-start-model-h265scenechangedetect) | False | Scene change detection. |
| slices | integer<br />Minimum: 1<br />Maximum: 16 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution. |
| tier | [H265Tier](#channels-channelid-start-model-h265tier) | False | H.265 Tier. |
| timecodeInsertion | [H265TimecodeInsertionBehavior](#channels-channelid-start-model-h265timecodeinsertionbehavior) | False | Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config |

### H265Tier
<a name="channels-channelid-start-model-h265tier"></a>

H265 Tier
+ `HIGH`
+ `MAIN`

### H265TimecodeInsertionBehavior
<a name="channels-channelid-start-model-h265timecodeinsertionbehavior"></a>

H265 Timecode Insertion Behavior
+ `DISABLED`
+ `PIC_TIMING_SEI`

### Hdr10Settings
<a name="channels-channelid-start-model-hdr10settings"></a>

Hdr10 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxCll | integer<br />Minimum: 0<br />Maximum: 32768 | False | Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file. |
| maxFall | integer<br />Minimum: 0<br />Maximum: 32768 | False | Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file. |

### HlsAdMarkers
<a name="channels-channelid-start-model-hlsadmarkers"></a>

Hls Ad Markers
+ `ADOBE`
+ `ELEMENTAL`
+ `ELEMENTAL_SCTE35`

### HlsAkamaiHttpTransferMode
<a name="channels-channelid-start-model-hlsakamaihttptransfermode"></a>

Hls Akamai Http Transfer Mode
+ `CHUNKED`
+ `NON_CHUNKED`

### HlsAkamaiSettings
<a name="channels-channelid-start-model-hlsakamaisettings"></a>

Hls Akamai Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| httpTransferMode | [HlsAkamaiHttpTransferMode](#channels-channelid-start-model-hlsakamaihttptransfermode) | False | Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |
| salt | string | False | Salt for authenticated Akamai. |
| token | string | False | Token parameter for authenticated akamai. If not specified, \_gda\_ is used. |

### HlsBasicPutSettings
<a name="channels-channelid-start-model-hlsbasicputsettings"></a>

Hls Basic Put Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HlsCaptionLanguageSetting
<a name="channels-channelid-start-model-hlscaptionlanguagesetting"></a>

Hls Caption Language Setting
+ `INSERT`
+ `NONE`
+ `OMIT`

### HlsCdnSettings
<a name="channels-channelid-start-model-hlscdnsettings"></a>

Hls Cdn Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsAkamaiSettings | [HlsAkamaiSettings](#channels-channelid-start-model-hlsakamaisettings) | False |  |
| hlsBasicPutSettings | [HlsBasicPutSettings](#channels-channelid-start-model-hlsbasicputsettings) | False |  |
| hlsMediaStoreSettings | [HlsMediaStoreSettings](#channels-channelid-start-model-hlsmediastoresettings) | False |  |
| hlsS3Settings | [HlsS3Settings](#channels-channelid-start-model-hlss3settings) | False |  |
| hlsWebdavSettings | [HlsWebdavSettings](#channels-channelid-start-model-hlswebdavsettings) | False |  |

### HlsClientCache
<a name="channels-channelid-start-model-hlsclientcache"></a>

Hls Client Cache
+ `DISABLED`
+ `ENABLED`

### HlsCodecSpecification
<a name="channels-channelid-start-model-hlscodecspecification"></a>

Hls Codec Specification
+ `RFC_4281`
+ `RFC_6381`

### HlsDirectoryStructure
<a name="channels-channelid-start-model-hlsdirectorystructure"></a>

Hls Directory Structure
+ `SINGLE_DIRECTORY`
+ `SUBDIRECTORY_PER_STREAM`

### HlsDiscontinuityTags
<a name="channels-channelid-start-model-hlsdiscontinuitytags"></a>

Hls Discontinuity Tags
+ `INSERT`
+ `NEVER_INSERT`

### HlsEncryptionType
<a name="channels-channelid-start-model-hlsencryptiontype"></a>

Hls Encryption Type
+ `AES128`
+ `SAMPLE_AES`

### HlsGroupSettings
<a name="channels-channelid-start-model-hlsgroupsettings"></a>

Hls Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | Array of type [HlsAdMarkers](#channels-channelid-start-model-hlsadmarkers) | False | Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs. |
| baseUrlContent | string | False | A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file. |
| baseUrlContent1 | string | False | Optional. One value per output group. This field is required only if you are completing Base URL content A, and the downstream system has notified you that the media files for pipeline 1 of all outputs are in a location different from the media files for pipeline 0. |
| baseUrlManifest | string | False | A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file. |
| baseUrlManifest1 | string | False | Optional. One value per output group. Complete this field only if you are completing Base URL manifest A, and the downstream system has notified you that the child manifest files for pipeline 1 of all outputs are in a location different from the child manifest files for pipeline 0. |
| captionLanguageMappings | Array of type [CaptionLanguageMapping](#channels-channelid-start-model-captionlanguagemapping) | False | Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to "insert". |
| captionLanguageSetting | [HlsCaptionLanguageSetting](#channels-channelid-start-model-hlscaptionlanguagesetting) | False | Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest. |
| clientCache | [HlsClientCache](#channels-channelid-start-model-hlsclientcache) | False | When set to "disabled", sets the \#EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay. |
| codecSpecification | [HlsCodecSpecification](#channels-channelid-start-model-hlscodecspecification) | False | Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation. |
| constantIv | string<br />MinLength: 32<br />MaxLength: 32 | False | For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to "explicit" then this parameter is required and is used as the IV for encryption. |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled). |
| directoryStructure | [HlsDirectoryStructure](#channels-channelid-start-model-hlsdirectorystructure) | False | Place segments in subdirectories. |
| discontinuityTags | [HlsDiscontinuityTags](#channels-channelid-start-model-hlsdiscontinuitytags) | False | Specifies whether to insert EXT-X-DISCONTINUITY tags in the HLS child manifests for this output group. Typically, choose Insert because these tags are required in the manifest (according to the HLS specification) and serve an important purpose. Choose Never Insert only if the downstream system is doing real-time failover (without using the MediaLive automatic failover feature) and only if that downstream system has advised you to exclude the tags. |
| encryptionType | [HlsEncryptionType](#channels-channelid-start-model-hlsencryptiontype) | False | Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired. |
| hlsCdnSettings | [HlsCdnSettings](#channels-channelid-start-model-hlscdnsettings) | False | Parameters that control interactions with the CDN. |
| hlsId3SegmentTagging | [HlsId3SegmentTaggingState](#channels-channelid-start-model-hlsid3segmenttaggingstate) | False | State of HLS ID3 Segment Tagging |
| iFrameOnlyPlaylists | [IFrameOnlyPlaylistType](#channels-channelid-start-model-iframeonlyplaylisttype) | False | DISABLED: Do not create an I-frame-only manifest, but do create the master and media manifests (according to the Output Selection field). STANDARD: Create an I-frame-only manifest for each output that contains video, as well as the other manifests (according to the Output Selection field). The I-frame manifest contains a \#EXT-X-I-FRAMES-ONLY tag to indicate it is I-frame only, and one or more \#EXT-X-BYTERANGE entries identifying the I-frame position. For example, \#EXT-X-BYTERANGE:160364@1461888" |
| incompleteSegmentBehavior | [HlsIncompleteSegmentBehavior](#channels-channelid-start-model-hlsincompletesegmentbehavior) | False | Specifies whether to include the final (incomplete) segment in the media output when the pipeline stops producing output because of a channel stop, a channel pause or a loss of input to the pipeline. Auto means that MediaLive decides whether to include the final segment, depending on the channel class and the types of output groups. Suppress means to never include the incomplete segment. We recommend you choose Auto and let MediaLive control the behavior. |
| indexNSegments | integer<br />Minimum: 3 | False | Applies only if Mode field is LIVE. Specifies the maximum number of segments in the media manifest file. After this maximum, older segments are removed from the media manifest. This number must be smaller than the number in the Keep Segments field. |
| inputLossAction | [InputLossActionForHlsOut](#channels-channelid-start-model-inputlossactionforhlsout) | False | Parameter that control output group behavior on input loss. |
| ivInManifest | [HlsIvInManifest](#channels-channelid-start-model-hlsivinmanifest) | False | For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to "include", IV is listed in the manifest, otherwise the IV is not in the manifest. |
| ivSource | [HlsIvSource](#channels-channelid-start-model-hlsivsource) | False | For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is "followsSegmentNumber", it will cause the IV to change every segment (to match the segment number). If this is set to "explicit", you must enter a constantIv value. |
| keepSegments | integer<br />Minimum: 1 | False | Applies only if Mode field is LIVE. Specifies the number of media segments to retain in the destination directory. This number should be bigger than indexNSegments (Num segments). We recommend (value = (2 x indexNsegments) \+ 1). If this "keep segments" number is too low, the following might happen: the player is still reading a media manifest file that lists this segment, but that segment has been removed from the destination directory (as directed by indexNSegments). This situation would result in a 404 HTTP error on the player. |
| keyFormat | string | False | The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of "identity" is used. A reverse DNS string can also be given. |
| keyFormatVersions | string | False | Either a single positive integer version value or a slash delimited list of version values (1/2/3). |
| keyProviderSettings | [KeyProviderSettings](#channels-channelid-start-model-keyprovidersettings) | False | The key provider settings. |
| manifestCompression | [HlsManifestCompression](#channels-channelid-start-model-hlsmanifestcompression) | False | When set to gzip, compresses HLS playlist. |
| manifestDurationFormat | [HlsManifestDurationFormat](#channels-channelid-start-model-hlsmanifestdurationformat) | False | Indicates whether the output manifest should use floating point or integer values for segment duration. |
| minSegmentLength | integer<br />Minimum: 0 | False | When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed. |
| mode | [HlsMode](#channels-channelid-start-model-hlsmode) | False | If "vod", all segments are indexed and kept permanently in the destination and manifest. If "live", only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a "VOD" type manifest on completion of the stream. |
| outputSelection | [HlsOutputSelection](#channels-channelid-start-model-hlsoutputselection) | False | MANIFESTS\_AND\_SEGMENTS: Generates manifests (master manifest, if applicable, and media manifests) for this output group. VARIANT\_MANIFESTS\_AND\_SEGMENTS: Generates media manifests for this output group, but not a master manifest. SEGMENTS\_ONLY: Does not generate any manifests for this output group. |
| programDateTime | [HlsProgramDateTime](#channels-channelid-start-model-hlsprogramdatetime) | False | Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset. |
| programDateTimeClock | [HlsProgramDateTimeClock](#channels-channelid-start-model-hlsprogramdatetimeclock) | False | Specifies the algorithm used to drive the HLS EXT-X-PROGRAM-DATE-TIME clock. Options include: INITIALIZE\_FROM\_OUTPUT\_TIMECODE: The PDT clock is initialized as a function of the first output timecode, then incremented by the EXTINF duration of each encoded segment. SYSTEM\_CLOCK: The PDT clock is initialized as a function of the UTC wall clock, then incremented by the EXTINF duration of each encoded segment. If the PDT clock diverges from the wall clock by more than 500ms, it is resynchronized to the wall clock. |
| programDateTimePeriod | integer<br />Minimum: 0<br />Maximum: 3600 | False | Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds. |
| redundantManifest | [HlsRedundantManifest](#channels-channelid-start-model-hlsredundantmanifest) | False | ENABLED: The master manifest (.m3u8 file) for each pipeline includes information about both pipelines: first its own media files, then the media files of the other pipeline. This feature allows playout device that support stale manifest detection to switch from one manifest to the other, when the current manifest seems to be stale. There are still two destinations and two master manifests, but both master manifests reference the media files from both pipelines. DISABLED: The master manifest (.m3u8 file) for each pipeline includes information about its own pipeline only. For an HLS output group with MediaPackage as the destination, the DISABLED behavior is always followed. MediaPackage regenerates the manifests it serves to players so a redundant manifest from MediaLive is irrelevant. |
| segmentationMode | [HlsSegmentationMode](#channels-channelid-start-model-hlssegmentationmode) | False | useInputSegmentation has been deprecated. The configured segment size is always used. |
| segmentLength | integer<br />Minimum: 1 | False | Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer. |
| segmentsPerSubdirectory | integer<br />Minimum: 1 | False | Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect. |
| streamInfResolution | [HlsStreamInfResolution](#channels-channelid-start-model-hlsstreaminfresolution) | False | Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest. |
| timedMetadataId3Frame | [HlsTimedMetadataId3Frame](#channels-channelid-start-model-hlstimedmetadataid3frame) | False | Indicates ID3 frame that has the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0 | False | Timed Metadata interval in seconds. |
| timestampDeltaMilliseconds | integer<br />Minimum: 0 | False | Provides an extra millisecond delta offset to fine tune the timestamps. |
| tsFileMode | [HlsTsFileMode](#channels-channelid-start-model-hlstsfilemode) | False | SEGMENTED\_FILES: Emit the program as segments - multiple .ts media files. SINGLE\_FILE: Applies only if Mode field is VOD. Emit the program as a single .ts media file. The media manifest includes \#EXT-X-BYTERANGE tags to index segments for playback. A typical use for this value is when sending the output to AWS Elemental MediaConvert, which can accept only a single media file. Playback while the channel is running is not guaranteed due to HTTP server caching. |

### HlsH265PackagingType
<a name="channels-channelid-start-model-hlsh265packagingtype"></a>

Hls H265 Packaging Type
+ `HEV1`
+ `HVC1`

### HlsId3SegmentTaggingState
<a name="channels-channelid-start-model-hlsid3segmenttaggingstate"></a>

State of HLS ID3 Segment Tagging
+ `DISABLED`
+ `ENABLED`

### HlsIncompleteSegmentBehavior
<a name="channels-channelid-start-model-hlsincompletesegmentbehavior"></a>

Hls Incomplete Segment Behavior
+ `AUTO`
+ `SUPPRESS`

### HlsInputSettings
<a name="channels-channelid-start-model-hlsinputsettings"></a>

Hls Input Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bandwidth | integer<br />Minimum: 0 | False | When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest. |
| bufferSegments | integer<br />Minimum: 0 | False | When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8. |
| retries | integer<br />Minimum: 0 | False | The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable. |
| retryInterval | integer<br />Minimum: 0 | False | The number of seconds between retries when an attempt to read a manifest or segment fails. |
| scte35Source | [HlsScte35SourceType](#channels-channelid-start-model-hlsscte35sourcetype) | False | Identifies the source for the SCTE-35 messages that MediaLive will ingest. Messages can be ingested from the content segments (in the stream) or from tags in the playlist (the HLS manifest). MediaLive ignores SCTE-35 information in the source that is not selected. |

### HlsIvInManifest
<a name="channels-channelid-start-model-hlsivinmanifest"></a>

Hls Iv In Manifest
+ `EXCLUDE`
+ `INCLUDE`

### HlsIvSource
<a name="channels-channelid-start-model-hlsivsource"></a>

Hls Iv Source
+ `EXPLICIT`
+ `FOLLOWS_SEGMENT_NUMBER`

### HlsManifestCompression
<a name="channels-channelid-start-model-hlsmanifestcompression"></a>

Hls Manifest Compression
+ `GZIP`
+ `NONE`

### HlsManifestDurationFormat
<a name="channels-channelid-start-model-hlsmanifestdurationformat"></a>

Hls Manifest Duration Format
+ `FLOATING_POINT`
+ `INTEGER`

### HlsMediaStoreSettings
<a name="channels-channelid-start-model-hlsmediastoresettings"></a>

Hls Media Store Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| mediaStoreStorageClass | [HlsMediaStoreStorageClass](#channels-channelid-start-model-hlsmediastorestorageclass) | False | When set to temporal, output files are stored in non-persistent memory for faster reading and writing. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HlsMediaStoreStorageClass
<a name="channels-channelid-start-model-hlsmediastorestorageclass"></a>

Hls Media Store Storage Class
+ `TEMPORAL`

### HlsMode
<a name="channels-channelid-start-model-hlsmode"></a>

Hls Mode
+ `LIVE`
+ `VOD`

### HlsOutputSelection
<a name="channels-channelid-start-model-hlsoutputselection"></a>

Hls Output Selection
+ `MANIFESTS_AND_SEGMENTS`
+ `SEGMENTS_ONLY`
+ `VARIANT_MANIFESTS_AND_SEGMENTS`

### HlsOutputSettings
<a name="channels-channelid-start-model-hlsoutputsettings"></a>

Hls Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| h265PackagingType | [HlsH265PackagingType](#channels-channelid-start-model-hlsh265packagingtype) | False | Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1. |
| hlsSettings | [HlsSettings](#channels-channelid-start-model-hlssettings) | True | Settings regarding the underlying stream. These settings are different for audio-only outputs. |
| nameModifier | string<br />MinLength: 1 | False | String concatenated to the end of the destination filename. Accepts \\"Format Identifiers\\":\#formatIdentifierParameters. |
| segmentModifier | string | False | String concatenated to end of segment filenames. |

### HlsProgramDateTime
<a name="channels-channelid-start-model-hlsprogramdatetime"></a>

Hls Program Date Time
+ `EXCLUDE`
+ `INCLUDE`

### HlsProgramDateTimeClock
<a name="channels-channelid-start-model-hlsprogramdatetimeclock"></a>

Hls Program Date Time Clock
+ `INITIALIZE_FROM_OUTPUT_TIMECODE`
+ `SYSTEM_CLOCK`

### HlsRedundantManifest
<a name="channels-channelid-start-model-hlsredundantmanifest"></a>

Hls Redundant Manifest
+ `DISABLED`
+ `ENABLED`

### HlsS3LogUploads
<a name="channels-channelid-start-model-hlss3loguploads"></a>

Hls S3 Log Uploads
+ `DISABLED`
+ `ENABLED`

### HlsS3Settings
<a name="channels-channelid-start-model-hlss3settings"></a>

Hls S3 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3CannedAcl](#channels-channelid-start-model-s3cannedacl) | False | Specify the canned ACL to apply to each S3 request. Defaults to none. |
| logUploads | [HlsS3LogUploads](#channels-channelid-start-model-hlss3loguploads) | False | When set to enabled, each fragment upload to CDN or server will be logged. |

### HlsScte35SourceType
<a name="channels-channelid-start-model-hlsscte35sourcetype"></a>

Hls Scte35 Source Type
+ `MANIFEST`
+ `SEGMENTS`

### HlsSegmentationMode
<a name="channels-channelid-start-model-hlssegmentationmode"></a>

Hls Segmentation Mode
+ `USE_INPUT_SEGMENTATION`
+ `USE_SEGMENT_DURATION`

### HlsSettings
<a name="channels-channelid-start-model-hlssettings"></a>

Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioOnlyHlsSettings | [AudioOnlyHlsSettings](#channels-channelid-start-model-audioonlyhlssettings) | False |  |
| fmp4HlsSettings | [Fmp4HlsSettings](#channels-channelid-start-model-fmp4hlssettings) | False |  |
| frameCaptureHlsSettings | [FrameCaptureHlsSettings](#channels-channelid-start-model-framecapturehlssettings) | False |  |
| standardHlsSettings | [StandardHlsSettings](#channels-channelid-start-model-standardhlssettings) | False |  |

### HlsStreamInfResolution
<a name="channels-channelid-start-model-hlsstreaminfresolution"></a>

Hls Stream Inf Resolution
+ `EXCLUDE`
+ `INCLUDE`

### HlsTimedMetadataId3Frame
<a name="channels-channelid-start-model-hlstimedmetadataid3frame"></a>

Hls Timed Metadata Id3 Frame
+ `NONE`
+ `PRIV`
+ `TDRL`

### HlsTsFileMode
<a name="channels-channelid-start-model-hlstsfilemode"></a>

Hls Ts File Mode
+ `SEGMENTED_FILES`
+ `SINGLE_FILE`

### HlsWebdavHttpTransferMode
<a name="channels-channelid-start-model-hlswebdavhttptransfermode"></a>

Hls Webdav Http Transfer Mode
+ `CHUNKED`
+ `NON_CHUNKED`

### HlsWebdavSettings
<a name="channels-channelid-start-model-hlswebdavsettings"></a>

Hls Webdav Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the CDN if the connection is lost. |
| filecacheDuration | integer<br />Minimum: 0<br />Maximum: 600 | False | Size in seconds of file cache for streaming outputs. |
| httpTransferMode | [HlsWebdavHttpTransferMode](#channels-channelid-start-model-hlswebdavhttptransfermode) | False | Specify whether or not to use chunked transfer encoding to WebDAV. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts that will be made before the Live Event is put into an error state. |
| restartDelay | integer<br />Minimum: 0<br />Maximum: 15 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### HtmlMotionGraphicsSettings
<a name="channels-channelid-start-model-htmlmotiongraphicssettings"></a>

Html Motion Graphics Settings

### IFrameOnlyPlaylistType
<a name="channels-channelid-start-model-iframeonlyplaylisttype"></a>

When set to "standard", an I-Frame only playlist will be written out for each video output in the output group. This I-Frame only playlist will contain byte range offsets pointing to the I-frame(s) in each segment.
+ `DISABLED`
+ `STANDARD`

### InputAttachment
<a name="channels-channelid-start-model-inputattachment"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| automaticInputFailoverSettings | [AutomaticInputFailoverSettings](#channels-channelid-start-model-automaticinputfailoversettings) | False | User-specified settings for defining what the conditions are for declaring the input unhealthy and failing over to a different input. |
| inputAttachmentName | string | False | User-specified name for the attachment. This is required if the user wants to use this input in an input switch action. |
| inputId | string | False | The ID of the input |
| inputSettings | [InputSettings](#channels-channelid-start-model-inputsettings) | False | Settings of an input (caption selector, etc.) |

### InputChannelLevel
<a name="channels-channelid-start-model-inputchannellevel"></a>

Input Channel Level

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| gain | integer<br />Minimum: -60<br />Maximum: 6 | True | Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB. |
| inputChannel | integer<br />Minimum: 0<br />Maximum: 15 | True | The index of the input channel used as a source. |

### InputCodec
<a name="channels-channelid-start-model-inputcodec"></a>

codec in increasing order of complexity
+ `MPEG2`
+ `AVC`
+ `HEVC`

### InputDeblockFilter
<a name="channels-channelid-start-model-inputdeblockfilter"></a>

Input Deblock Filter
+ `DISABLED`
+ `ENABLED`

### InputDenoiseFilter
<a name="channels-channelid-start-model-inputdenoisefilter"></a>

Input Denoise Filter
+ `DISABLED`
+ `ENABLED`

### InputFilter
<a name="channels-channelid-start-model-inputfilter"></a>

Input Filter
+ `AUTO`
+ `DISABLED`
+ `FORCED`

### InputLocation
<a name="channels-channelid-start-model-inputlocation"></a>

Input Location

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | key used to extract the password from EC2 Parameter store |
| uri | string | True | Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live". |
| username | string | False | Username if credentials are required to access a file or publishing point. This can be either a plaintext username, or a reference to an AWS parameter store name from which the username can be retrieved. AWS Parameter store format: "ssm://<parameter name>" |

### InputLossActionForHlsOut
<a name="channels-channelid-start-model-inputlossactionforhlsout"></a>

Input Loss Action For Hls Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForMsSmoothOut
<a name="channels-channelid-start-model-inputlossactionformssmoothout"></a>

Input Loss Action For Ms Smooth Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForRtmpOut
<a name="channels-channelid-start-model-inputlossactionforrtmpout"></a>

Input Loss Action For Rtmp Out
+ `EMIT_OUTPUT`
+ `PAUSE_OUTPUT`

### InputLossActionForUdpOut
<a name="channels-channelid-start-model-inputlossactionforudpout"></a>

Input Loss Action For Udp Out
+ `DROP_PROGRAM`
+ `DROP_TS`
+ `EMIT_PROGRAM`

### InputLossBehavior
<a name="channels-channelid-start-model-inputlossbehavior"></a>

Input Loss Behavior

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackFrameMsec | integer<br />Minimum: 0<br />Maximum: 1000000 | False | On input loss, the number of milliseconds to substitute black into the output before switching to the frame specified by inputLossImageType. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000 will be interpreted as infinite. |
| inputLossImageColor | string<br />MinLength: 6<br />MaxLength: 6 | False | When input loss image type is "color" this field specifies the color to use. Value: 6 hex characters representing the values of RGB. |
| inputLossImageSlate | [InputLocation](#channels-channelid-start-model-inputlocation) | False | When input loss image type is "slate" these fields specify the parameters for accessing the slate. |
| inputLossImageType | [InputLossImageType](#channels-channelid-start-model-inputlossimagetype) | False | Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec. |
| repeatFrameMsec | integer<br />Minimum: 0<br />Maximum: 1000000 | False | On input loss, the number of milliseconds to repeat the previous picture before substituting black into the output. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000 will be interpreted as infinite. |

### InputLossFailoverSettings
<a name="channels-channelid-start-model-inputlossfailoversettings"></a>

MediaLive will perform a failover if content is not detected in this input for the specified period.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputLossThresholdMsec | integer<br />Minimum: 100 | False | The amount of time (in milliseconds) that no input is detected. After that time, an input failover will occur. |

### InputLossImageType
<a name="channels-channelid-start-model-inputlossimagetype"></a>

Input Loss Image Type
+ `COLOR`
+ `SLATE`

### InputMaximumBitrate
<a name="channels-channelid-start-model-inputmaximumbitrate"></a>

Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are supported currently.
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### InputPreference
<a name="channels-channelid-start-model-inputpreference"></a>

Input preference when deciding which input to make active when a previously failed input has recovered. If \\"EQUAL\_INPUT\_PREFERENCE\\", then the active input will stay active as long as it is healthy. If \\"PRIMARY\_INPUT\_PREFERRED\\", then always switch back to the primary input when it is healthy.
+ `EQUAL_INPUT_PREFERENCE`
+ `PRIMARY_INPUT_PREFERRED`

### InputResolution
<a name="channels-channelid-start-model-inputresolution"></a>

Input resolution based on lines of vertical resolution in the input; SD is less than 720 lines, HD is 720 to 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `UHD`

### InputSettings
<a name="channels-channelid-start-model-inputsettings"></a>

Live Event input parameters. There can be multiple inputs in a single Live Event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectors | Array of type [AudioSelector](#channels-channelid-start-model-audioselector) | False | Used to select the audio stream to decode for inputs that have multiple available. |
| captionSelectors | Array of type [CaptionSelector](#channels-channelid-start-model-captionselector) | False | Used to select the caption input to use for inputs that have multiple available. |
| deblockFilter | [InputDeblockFilter](#channels-channelid-start-model-inputdeblockfilter) | False | Enable or disable the deblock filter when filtering. |
| denoiseFilter | [InputDenoiseFilter](#channels-channelid-start-model-inputdenoisefilter) | False | Enable or disable the denoise filter when filtering. |
| filterStrength | integer<br />Minimum: 1<br />Maximum: 5 | False | Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest). |
| inputFilter | [InputFilter](#channels-channelid-start-model-inputfilter) | False | Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type |
| networkInputSettings | [NetworkInputSettings](#channels-channelid-start-model-networkinputsettings) | False | Input settings. |
| smpte2038DataPreference | [Smpte2038DataPreference](#channels-channelid-start-model-smpte2038datapreference) | False | Specifies whether to extract applicable ancillary data from a SMPTE-2038 source in this input. Applicable data types are captions, timecode, AFD, and SCTE-104 messages. - PREFER: Extract from SMPTE-2038 if present in this input, otherwise extract from another source (if any). - IGNORE: Never extract any ancillary data from SMPTE-2038. |
| sourceEndBehavior | [InputSourceEndBehavior](#channels-channelid-start-model-inputsourceendbehavior) | False | Loop input if it is a file. This allows a file input to be streamed indefinitely. |
| videoSelector | [VideoSelector](#channels-channelid-start-model-videoselector) | False | Informs which video elementary stream to decode for input types that have multiple available. |

### InputSourceEndBehavior
<a name="channels-channelid-start-model-inputsourceendbehavior"></a>

Input Source End Behavior
+ `CONTINUE`
+ `LOOP`

### InputSpecification
<a name="channels-channelid-start-model-inputspecification"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| codec | [InputCodec](#channels-channelid-start-model-inputcodec) | False | Input codec |
| maximumBitrate | [InputMaximumBitrate](#channels-channelid-start-model-inputmaximumbitrate) | False | Maximum input bitrate, categorized coarsely |
| resolution | [InputResolution](#channels-channelid-start-model-inputresolution) | False | Input resolution, categorized coarsely |

### InternalServiceError
<a name="channels-channelid-start-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="channels-channelid-start-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### KeyProviderSettings
<a name="channels-channelid-start-model-keyprovidersettings"></a>

Key Provider Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| staticKeySettings | [StaticKeySettings](#channels-channelid-start-model-statickeysettings) | False |  |

### LimitExceeded
<a name="channels-channelid-start-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LogLevel
<a name="channels-channelid-start-model-loglevel"></a>

The log level the user wants for their channel.
+ `ERROR`
+ `WARNING`
+ `INFO`
+ `DEBUG`
+ `DISABLED`

### M2tsAbsentInputAudioBehavior
<a name="channels-channelid-start-model-m2tsabsentinputaudiobehavior"></a>

M2ts Absent Input Audio Behavior
+ `DROP`
+ `ENCODE_SILENCE`

### M2tsArib
<a name="channels-channelid-start-model-m2tsarib"></a>

M2ts Arib
+ `DISABLED`
+ `ENABLED`

### M2tsAribCaptionsPidControl
<a name="channels-channelid-start-model-m2tsaribcaptionspidcontrol"></a>

M2ts Arib Captions Pid Control
+ `AUTO`
+ `USE_CONFIGURED`

### M2tsAudioBufferModel
<a name="channels-channelid-start-model-m2tsaudiobuffermodel"></a>

M2ts Audio Buffer Model
+ `ATSC`
+ `DVB`

### M2tsAudioInterval
<a name="channels-channelid-start-model-m2tsaudiointerval"></a>

M2ts Audio Interval
+ `VIDEO_AND_FIXED_INTERVALS`
+ `VIDEO_INTERVAL`

### M2tsAudioStreamType
<a name="channels-channelid-start-model-m2tsaudiostreamtype"></a>

M2ts Audio Stream Type
+ `ATSC`
+ `DVB`

### M2tsBufferModel
<a name="channels-channelid-start-model-m2tsbuffermodel"></a>

M2ts Buffer Model
+ `MULTIPLEX`
+ `NONE`

### M2tsCcDescriptor
<a name="channels-channelid-start-model-m2tsccdescriptor"></a>

M2ts Cc Descriptor
+ `DISABLED`
+ `ENABLED`

### M2tsEbifControl
<a name="channels-channelid-start-model-m2tsebifcontrol"></a>

M2ts Ebif Control
+ `NONE`
+ `PASSTHROUGH`

### M2tsEbpPlacement
<a name="channels-channelid-start-model-m2tsebpplacement"></a>

M2ts Ebp Placement
+ `VIDEO_AND_AUDIO_PIDS`
+ `VIDEO_PID`

### M2tsEsRateInPes
<a name="channels-channelid-start-model-m2tsesrateinpes"></a>

M2ts Es Rate In Pes
+ `EXCLUDE`
+ `INCLUDE`

### M2tsKlv
<a name="channels-channelid-start-model-m2tsklv"></a>

M2ts Klv
+ `NONE`
+ `PASSTHROUGH`

### M2tsNielsenId3Behavior
<a name="channels-channelid-start-model-m2tsnielsenid3behavior"></a>

M2ts Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M2tsPcrControl
<a name="channels-channelid-start-model-m2tspcrcontrol"></a>

M2ts Pcr Control
+ `CONFIGURED_PCR_PERIOD`
+ `PCR_EVERY_PES_PACKET`

### M2tsRateMode
<a name="channels-channelid-start-model-m2tsratemode"></a>

M2ts Rate Mode
+ `CBR`
+ `VBR`

### M2tsScte35Control
<a name="channels-channelid-start-model-m2tsscte35control"></a>

M2ts Scte35 Control
+ `NONE`
+ `PASSTHROUGH`

### M2tsSegmentationMarkers
<a name="channels-channelid-start-model-m2tssegmentationmarkers"></a>

M2ts Segmentation Markers
+ `EBP`
+ `EBP_LEGACY`
+ `NONE`
+ `PSI_SEGSTART`
+ `RAI_ADAPT`
+ `RAI_SEGSTART`

### M2tsSegmentationStyle
<a name="channels-channelid-start-model-m2tssegmentationstyle"></a>

M2ts Segmentation Style
+ `MAINTAIN_CADENCE`
+ `RESET_CADENCE`

### M2tsSettings
<a name="channels-channelid-start-model-m2tssettings"></a>

M2ts Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| absentInputAudioBehavior | [M2tsAbsentInputAudioBehavior](#channels-channelid-start-model-m2tsabsentinputaudiobehavior) | False | When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream. |
| arib | [M2tsArib](#channels-channelid-start-model-m2tsarib) | False | When set to enabled, uses ARIB-compliant field muxing and removes video descriptor. |
| aribCaptionsPid | string | False | Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| aribCaptionsPidControl | [M2tsAribCaptionsPidControl](#channels-channelid-start-model-m2tsaribcaptionspidcontrol) | False | If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number. |
| audioBufferModel | [M2tsAudioBufferModel](#channels-channelid-start-model-m2tsaudiobuffermodel) | False | When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used. |
| audioFramesPerPes | integer<br />Minimum: 0 | False | The number of audio frames to insert for each PES packet. |
| audioPids | string | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| audioStreamType | [M2tsAudioStreamType](#channels-channelid-start-model-m2tsaudiostreamtype) | False | When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06. |
| bitrate | integer<br />Minimum: 0 | False | The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. |
| bufferModel | [M2tsBufferModel](#channels-channelid-start-model-m2tsbuffermodel) | False | Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices. |
| ccDescriptor | [M2tsCcDescriptor](#channels-channelid-start-model-m2tsccdescriptor) | False | When set to enabled, generates captionServiceDescriptor in PMT. |
| dvbNitSettings | [DvbNitSettings](#channels-channelid-start-model-dvbnitsettings) | False | Inserts DVB Network Information Table (NIT) at the specified table repetition interval. |
| dvbSdtSettings | [DvbSdtSettings](#channels-channelid-start-model-dvbsdtsettings) | False | Inserts DVB Service Description Table (SDT) at the specified table repetition interval. |
| dvbSubPids | string | False | Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| dvbTdtSettings | [DvbTdtSettings](#channels-channelid-start-model-dvbtdtsettings) | False | Inserts DVB Time and Date Table (TDT) at the specified table repetition interval. |
| dvbTeletextPid | string | False | Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| ebif | [M2tsEbifControl](#channels-channelid-start-model-m2tsebifcontrol) | False | If set to passthrough, passes any EBIF data from the input source to this output. |
| ebpAudioInterval | [M2tsAudioInterval](#channels-channelid-start-model-m2tsaudiointerval) | False | When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval. |
| ebpLookaheadMs | integer<br />Minimum: 0<br />Maximum: 10000 | False | When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate. |
| ebpPlacement | [M2tsEbpPlacement](#channels-channelid-start-model-m2tsebpplacement) | False | Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID. |
| ecmPid | string | False | This field is unused and deprecated. |
| esRateInPes | [M2tsEsRateInPes](#channels-channelid-start-model-m2tsesrateinpes) | False | Include or exclude the ES Rate field in the PES header. |
| etvPlatformPid | string | False | Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| etvSignalPid | string | False | Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| fragmentTime | number<br />Minimum: 0 | False | The length in seconds of each fragment. Only used with EBP markers. |
| klv | [M2tsKlv](#channels-channelid-start-model-m2tsklv) | False | If set to passthrough, passes any KLV data from the input source to this output. |
| klvDataPids | string | False | Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| nielsenId3Behavior | [M2tsNielsenId3Behavior](#channels-channelid-start-model-m2tsnielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| nullPacketBitrate | number<br />Minimum: 0 | False | Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000. |
| pcrControl | [M2tsPcrControl](#channels-channelid-start-model-m2tspcrcontrol) | False | When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPeriod | integer<br />Minimum: 0<br />Maximum: 500 | False | Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream. |
| pcrPid | string | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000. |
| pmtPid | string | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| programNum | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| rateMode | [M2tsRateMode](#channels-channelid-start-model-m2tsratemode) | False | When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set. |
| scte27Pids | string | False | Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6). |
| scte35Control | [M2tsScte35Control](#channels-channelid-start-model-m2tsscte35control) | False | Optionally pass SCTE-35 signals from the input source to this output. |
| scte35Pid | string | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| segmentationMarkers | [M2tsSegmentationMarkers](#channels-channelid-start-model-m2tssegmentationmarkers) | False | Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format. |
| segmentationStyle | [M2tsSegmentationStyle](#channels-channelid-start-model-m2tssegmentationstyle) | False | The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule. |
| segmentationTime | number<br />Minimum: 1 | False | The length in seconds of each segment. Required unless markers is set to \_none\_. |
| timedMetadataBehavior | [M2tsTimedMetadataBehavior](#channels-channelid-start-model-m2tstimedmetadatabehavior) | False | When set to passthrough, timed metadata will be passed through from input to output. |
| timedMetadataPid | string | False | Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | string | False | Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |

### M2tsTimedMetadataBehavior
<a name="channels-channelid-start-model-m2tstimedmetadatabehavior"></a>

M2ts Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8NielsenId3Behavior
<a name="channels-channelid-start-model-m3u8nielsenid3behavior"></a>

M3u8 Nielsen Id3 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8PcrControl
<a name="channels-channelid-start-model-m3u8pcrcontrol"></a>

M3u8 Pcr Control
+ `CONFIGURED_PCR_PERIOD`
+ `PCR_EVERY_PES_PACKET`

### M3u8Scte35Behavior
<a name="channels-channelid-start-model-m3u8scte35behavior"></a>

M3u8 Scte35 Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### M3u8Settings
<a name="channels-channelid-start-model-m3u8settings"></a>

Settings information for the .m3u8 container

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioFramesPerPes | integer<br />Minimum: 0 | False | The number of audio frames to insert for each PES packet. |
| audioPids | string | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. |
| ecmPid | string | False | This parameter is unused and deprecated. |
| nielsenId3Behavior | [M3u8NielsenId3Behavior](#channels-channelid-start-model-m3u8nielsenid3behavior) | False | If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. A value of \\"0\\" writes out the PMT once per segment file. |
| pcrControl | [M3u8PcrControl](#channels-channelid-start-model-m3u8pcrcontrol) | False | When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPeriod | integer<br />Minimum: 0<br />Maximum: 500 | False | Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream. |
| pcrPid | string | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. A value of \\"0\\" writes out the PMT once per segment file. |
| pmtPid | string | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. |
| programNum | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| scte35Behavior | [M3u8Scte35Behavior](#channels-channelid-start-model-m3u8scte35behavior) | False | If set to passthrough, passes any SCTE-35 signals from the input source to this output. |
| scte35Pid | string | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. |
| timedMetadataBehavior | [M3u8TimedMetadataBehavior](#channels-channelid-start-model-m3u8timedmetadatabehavior) | False | When set to passthrough, timed metadata is passed through from input to output. |
| timedMetadataPid | string | False | Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6). |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | string | False | Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. |

### M3u8TimedMetadataBehavior
<a name="channels-channelid-start-model-m3u8timedmetadatabehavior"></a>

M3u8 Timed Metadata Behavior
+ `NO_PASSTHROUGH`
+ `PASSTHROUGH`

### MaintenanceDay
<a name="channels-channelid-start-model-maintenanceday"></a>

The currently selected maintenance day.
+ `MONDAY`
+ `TUESDAY`
+ `WEDNESDAY`
+ `THURSDAY`
+ `FRIDAY`
+ `SATURDAY`
+ `SUNDAY`

### MaintenanceStatus
<a name="channels-channelid-start-model-maintenancestatus"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maintenanceDay | [MaintenanceDay](#channels-channelid-start-model-maintenanceday) | False | The currently selected maintenance day. |
| maintenanceDeadline | string<br />Format: string | False | Maintenance is required by the displayed date and time. Date and time is in ISO. |
| maintenanceScheduledDate | string<br />Format: string | False | The currently scheduled maintenance date and time. Date and time is in ISO. |
| maintenanceStartTime | string | False | The currently selected maintenance start time. Time is in UTC. |

### MediaPackageGroupSettings
<a name="channels-channelid-start-model-mediapackagegroupsettings"></a>

Media Package Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | MediaPackage channel destination. |

### MediaPackageOutputDestinationSettings
<a name="channels-channelid-start-model-mediapackageoutputdestinationsettings"></a>

MediaPackage Output Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelId | string<br />MinLength: 1 | False | ID of the channel in MediaPackage that is the destination for this output group. You do not need to specify the individual inputs in MediaPackage; MediaLive will handle the connection of the two MediaLive pipelines to the two MediaPackage inputs. The MediaPackage channel and MediaLive channel must be in the same region. |

### MediaPackageOutputSettings
<a name="channels-channelid-start-model-mediapackageoutputsettings"></a>

Media Package Output Settings

### MotionGraphicsConfiguration
<a name="channels-channelid-start-model-motiongraphicsconfiguration"></a>

Motion Graphics Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| motionGraphicsInsertion | [MotionGraphicsInsertion](#channels-channelid-start-model-motiongraphicsinsertion) | False |  |
| motionGraphicsSettings | [MotionGraphicsSettings](#channels-channelid-start-model-motiongraphicssettings) | True | Motion Graphics Settings |

### MotionGraphicsInsertion
<a name="channels-channelid-start-model-motiongraphicsinsertion"></a>

Motion Graphics Insertion
+ `DISABLED`
+ `ENABLED`

### MotionGraphicsSettings
<a name="channels-channelid-start-model-motiongraphicssettings"></a>

Motion Graphics Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| htmlMotionGraphicsSettings | [HtmlMotionGraphicsSettings](#channels-channelid-start-model-htmlmotiongraphicssettings) | False |  |

### Mp2CodingMode
<a name="channels-channelid-start-model-mp2codingmode"></a>

Mp2 Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`

### Mp2Settings
<a name="channels-channelid-start-model-mp2settings"></a>

Mp2 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | number | False | Average bitrate in bits/second. |
| codingMode | [Mp2CodingMode](#channels-channelid-start-model-mp2codingmode) | False | The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo). |
| sampleRate | number | False | Sample rate in Hz. |

### Mpeg2AdaptiveQuantization
<a name="channels-channelid-start-model-mpeg2adaptivequantization"></a>

Mpeg2 Adaptive Quantization
+ `AUTO`
+ `HIGH`
+ `LOW`
+ `MEDIUM`
+ `OFF`

### Mpeg2ColorMetadata
<a name="channels-channelid-start-model-mpeg2colormetadata"></a>

Mpeg2 Color Metadata
+ `IGNORE`
+ `INSERT`

### Mpeg2ColorSpace
<a name="channels-channelid-start-model-mpeg2colorspace"></a>

Mpeg2 Color Space
+ `AUTO`
+ `PASSTHROUGH`

### Mpeg2DisplayRatio
<a name="channels-channelid-start-model-mpeg2displayratio"></a>

Mpeg2 Display Ratio
+ `DISPLAYRATIO16X9`
+ `DISPLAYRATIO4X3`

### Mpeg2FilterSettings
<a name="channels-channelid-start-model-mpeg2filtersettings"></a>

Mpeg2 Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| temporalFilterSettings | [TemporalFilterSettings](#channels-channelid-start-model-temporalfiltersettings) | False |  |

### Mpeg2GopSizeUnits
<a name="channels-channelid-start-model-mpeg2gopsizeunits"></a>

Mpeg2 Gop Size Units
+ `FRAMES`
+ `SECONDS`

### Mpeg2ScanType
<a name="channels-channelid-start-model-mpeg2scantype"></a>

Mpeg2 Scan Type
+ `INTERLACED`
+ `PROGRESSIVE`

### Mpeg2Settings
<a name="channels-channelid-start-model-mpeg2settings"></a>

Mpeg2 Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Mpeg2AdaptiveQuantization](#channels-channelid-start-model-mpeg2adaptivequantization) | False | Choose Off to disable adaptive quantization. Or choose another value to enable the quantizer and set its strength. The strengths are: Auto, Off, Low, Medium, High. When you enable this field, MediaLive allows intra-frame quantizers to vary, which might improve visual quality. |
| afdSignaling | [AfdSignaling](#channels-channelid-start-model-afdsignaling) | False | Indicates the AFD values that MediaLive will write into the video encode. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose AUTO. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: MediaLive will use the value you specify in fixedAFD. |
| colorMetadata | [Mpeg2ColorMetadata](#channels-channelid-start-model-mpeg2colormetadata) | False | Specifies whether to include the color space metadata. The metadata describes the color space that applies to the video (the colorSpace field). We recommend that you insert the metadata. |
| colorSpace | [Mpeg2ColorSpace](#channels-channelid-start-model-mpeg2colorspace) | False | Choose the type of color space conversion to apply to the output. For detailed information on setting up both the input and the output to obtain the desired color space in the output, see the section on \\"MediaLive Features - Video - color space\\" in the MediaLive User Guide. PASSTHROUGH: Keep the color space of the input content - do not convert it. AUTO:Convert all content that is SD to rec 601, and convert all content that is HD to rec 709. |
| displayAspectRatio | [Mpeg2DisplayRatio](#channels-channelid-start-model-mpeg2displayratio) | False | Sets the pixel aspect ratio for the encode. |
| filterSettings | [Mpeg2FilterSettings](#channels-channelid-start-model-mpeg2filtersettings) | False | Optionally specify a noise reduction filter, which can improve quality of compressed content. If you do not choose a filter, no filter will be applied. TEMPORAL: This filter is useful for both source content that is noisy (when it has excessive digital artifacts) and source content that is clean. When the content is noisy, the filter cleans up the source content before the encoding phase, with these two effects: First, it improves the output video quality because the content has been cleaned up. Secondly, it decreases the bandwidth because MediaLive does not waste bits on encoding noise. When the content is reasonably clean, the filter tends to decrease the bitrate. |
| fixedAfd | [FixedAfd](#channels-channelid-start-model-fixedafd) | False | Complete this field only when afdSignaling is set to FIXED. Enter the AFD value (4 bits) to write on all frames of the video encode. |
| framerateDenominator | integer<br />Minimum: 1 | True | description": "The framerate denominator. For example, 1001. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS. |
| framerateNumerator | integer<br />Minimum: 1 | True | The framerate numerator. For example, 24000. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS. |
| gopClosedCadence | integer<br />Minimum: 0 | False | MPEG2: default is open GOP. |
| gopNumBFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Relates to the GOP structure. The number of B-frames between reference frames. If you do not know what a B-frame is, use the default. |
| gopSize | number | False | Relates to the GOP structure. The GOP size (keyframe interval) in the units specified in gopSizeUnits. If you do not know what GOP is, use the default. If gopSizeUnits is frames, then the gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, the gopSize must be greater than 0, but does not need to be an integer. |
| gopSizeUnits | [Mpeg2GopSizeUnits](#channels-channelid-start-model-mpeg2gopsizeunits) | False | Relates to the GOP structure. Specifies whether the gopSize is specified in frames or seconds. If you do not plan to change the default gopSize, leave the default. If you specify SECONDS, MediaLive will internally convert the gop size to a frame count. |
| scanType | [Mpeg2ScanType](#channels-channelid-start-model-mpeg2scantype) | False | Set the scan type of the output to PROGRESSIVE or INTERLACED (top field first). |
| subgopLength | [Mpeg2SubGopLength](#channels-channelid-start-model-mpeg2subgoplength) | False | Relates to the GOP structure. If you do not know what GOP is, use the default. FIXED: Set the number of B-frames in each sub-GOP to the value in gopNumBFrames. DYNAMIC: Let MediaLive optimize the number of B-frames in each sub-GOP, to improve visual quality. |
| timecodeInsertion | [Mpeg2TimecodeInsertionBehavior](#channels-channelid-start-model-mpeg2timecodeinsertionbehavior) | False | Determines how MediaLive inserts timecodes in the output video. For detailed information about setting up the input and the output for a timecode, see the section on \\"MediaLive Features - Timecode configuration\\" in the MediaLive User Guide. DISABLED: do not include timecodes. GOP\_TIMECODE: Include timecode metadata in the GOP header. |

### Mpeg2SubGopLength
<a name="channels-channelid-start-model-mpeg2subgoplength"></a>

Mpeg2 Sub Gop Length
+ `DYNAMIC`
+ `FIXED`

### Mpeg2TimecodeInsertionBehavior
<a name="channels-channelid-start-model-mpeg2timecodeinsertionbehavior"></a>

Mpeg2 Timecode Insertion Behavior
+ `DISABLED`
+ `GOP_TIMECODE`

### MsSmoothGroupSettings
<a name="channels-channelid-start-model-mssmoothgroupsettings"></a>

Ms Smooth Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| acquisitionPointId | string | False | The ID to include in each message in the sparse track. Ignored if sparseTrackType is NONE. |
| audioOnlyTimecodeControl | [SmoothGroupAudioOnlyTimecodeControl](#channels-channelid-start-model-smoothgroupaudioonlytimecodecontrol) | False | If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream. |
| certificateMode | [SmoothGroupCertificateMode](#channels-channelid-start-model-smoothgroupcertificatemode) | False | If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail. |
| connectionRetryInterval | integer<br />Minimum: 0 | False | Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established. |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | Smooth Streaming publish point on an IIS server. Elemental Live acts as a "Push" encoder to IIS. |
| eventId | string | False | MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured. |
| eventIdMode | [SmoothGroupEventIdMode](#channels-channelid-start-model-smoothgroupeventidmode) | False | Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - "useConfigured" - use the value provided in eventId - "useTimestamp" - generate and send an event ID based on the current timestamp - "noEventId" - do not send an event ID to the IIS server. |
| eventStopBehavior | [SmoothGroupEventStopBehavior](#channels-channelid-start-model-smoothgroupeventstopbehavior) | False | When set to sendEos, send EOS signal to IIS server when stopping the event |
| filecacheDuration | integer<br />Minimum: 0 | False | Size in seconds of file cache for streaming outputs. |
| fragmentLength | integer<br />Minimum: 1 | False | Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate. |
| inputLossAction | [InputLossActionForMsSmoothOut](#channels-channelid-start-model-inputlossactionformssmoothout) | False | Parameter that control output group behavior on input loss. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts. |
| restartDelay | integer<br />Minimum: 0 | False | Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration. |
| segmentationMode | [SmoothGroupSegmentationMode](#channels-channelid-start-model-smoothgroupsegmentationmode) | False | useInputSegmentation has been deprecated. The configured segment size is always used. |
| sendDelayMs | integer<br />Minimum: 0<br />Maximum: 10000 | False | Number of milliseconds to delay the output from the second pipeline. |
| sparseTrackType | [SmoothGroupSparseTrackType](#channels-channelid-start-model-smoothgroupsparsetracktype) | False | Identifies the type of data to place in the sparse track: - SCTE35: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame to start a new segment. - SCTE35\_WITHOUT\_SEGMENTATION: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame but don't start a new segment. - NONE: Don't generate a sparse track for any outputs in this output group. |
| streamManifestBehavior | [SmoothGroupStreamManifestBehavior](#channels-channelid-start-model-smoothgroupstreammanifestbehavior) | False | When set to send, send stream manifest so publishing point doesn't start until all streams start. |
| timestampOffset | string | False | Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset. |
| timestampOffsetMode | [SmoothGroupTimestampOffsetMode](#channels-channelid-start-model-smoothgrouptimestampoffsetmode) | False | Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset |

### MsSmoothH265PackagingType
<a name="channels-channelid-start-model-mssmoothh265packagingtype"></a>

Ms Smooth H265 Packaging Type
+ `HEV1`
+ `HVC1`

### MsSmoothOutputSettings
<a name="channels-channelid-start-model-mssmoothoutputsettings"></a>

Ms Smooth Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| h265PackagingType | [MsSmoothH265PackagingType](#channels-channelid-start-model-mssmoothh265packagingtype) | False | Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1. |
| nameModifier | string | False | String concatenated to the end of the destination filename. Required for multiple outputs of the same type. |

### MultiplexGroupSettings
<a name="channels-channelid-start-model-multiplexgroupsettings"></a>

Multiplex Group Settings

### MultiplexOutputSettings
<a name="channels-channelid-start-model-multiplexoutputsettings"></a>

Multiplex Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | Destination is a Multiplex. |

### MultiplexProgramChannelDestinationSettings
<a name="channels-channelid-start-model-multiplexprogramchanneldestinationsettings"></a>

Multiplex Program Input Destination Settings for outputting a Channel to a Multiplex

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexId | string<br />MinLength: 1 | False | The ID of the Multiplex that the encoder is providing output to. You do not need to specify the individual inputs to the Multiplex; MediaLive will handle the connection of the two MediaLive pipelines to the two Multiplex instances. The Multiplex must be in the same region as the Channel. |
| programName | string<br />MinLength: 1 | False | The program name of the Multiplex program that the encoder is providing output to. |

### NetworkInputServerValidation
<a name="channels-channelid-start-model-networkinputservervalidation"></a>

Network Input Server Validation
+ `CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME`
+ `CHECK_CRYPTOGRAPHY_ONLY`

### NetworkInputSettings
<a name="channels-channelid-start-model-networkinputsettings"></a>

Network source to transcode. Must be accessible to the Elemental Live node that is running the live event through a network connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsInputSettings | [HlsInputSettings](#channels-channelid-start-model-hlsinputsettings) | False | Specifies HLS input settings when the uri is for a HLS manifest. |
| serverValidation | [NetworkInputServerValidation](#channels-channelid-start-model-networkinputservervalidation) | False | Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https. |

### NielsenCBET
<a name="channels-channelid-start-model-nielsencbet"></a>

Nielsen CBET

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cbetCheckDigitString | string<br />MinLength: 2<br />MaxLength: 2 | True | Enter the CBET check digits to use in the watermark. |
| cbetStepaside | [NielsenWatermarksCbetStepaside](#channels-channelid-start-model-nielsenwatermarkscbetstepaside) | True | Determines the method of CBET insertion mode when prior encoding is detected on the same layer. |
| csid | string<br />MinLength: 1<br />MaxLength: 7 | True | Enter the CBET Source ID (CSID) to use in the watermark |

### NielsenConfiguration
<a name="channels-channelid-start-model-nielsenconfiguration"></a>

Nielsen Configuration

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| distributorId | string | False | Enter the Distributor ID assigned to your organization by Nielsen. |
| nielsenPcmToId3Tagging | [NielsenPcmToId3TaggingState](#channels-channelid-start-model-nielsenpcmtoid3taggingstate) | False | Enables Nielsen PCM to ID3 tagging |

### NielsenNaesIiNw
<a name="channels-channelid-start-model-nielsennaesiinw"></a>

Nielsen Naes Ii Nw

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| checkDigitString | string<br />MinLength: 2<br />MaxLength: 2 | True | Enter the check digit string for the watermark |
| sid | number<br />Minimum: 1<br />Maximum: 65535 | True | Enter the Nielsen Source ID (SID) to include in the watermark |

### NielsenPcmToId3TaggingState
<a name="channels-channelid-start-model-nielsenpcmtoid3taggingstate"></a>

State of Nielsen PCM to ID3 tagging
+ `DISABLED`
+ `ENABLED`

### NielsenWatermarksCbetStepaside
<a name="channels-channelid-start-model-nielsenwatermarkscbetstepaside"></a>

Nielsen Watermarks Cbet Stepaside
+ `DISABLED`
+ `ENABLED`

### NielsenWatermarksDistributionTypes
<a name="channels-channelid-start-model-nielsenwatermarksdistributiontypes"></a>

Nielsen Watermarks Distribution Types
+ `FINAL_DISTRIBUTOR`
+ `PROGRAM_CONTENT`

### NielsenWatermarksSettings
<a name="channels-channelid-start-model-nielsenwatermarkssettings"></a>

Nielsen Watermarks Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nielsenCbetSettings | [NielsenCBET](#channels-channelid-start-model-nielsencbet) | False | Complete these fields only if you want to insert watermarks of type Nielsen CBET |
| nielsenDistributionType | [NielsenWatermarksDistributionTypes](#channels-channelid-start-model-nielsenwatermarksdistributiontypes) | False | Choose the distribution types that you want to assign to the watermarks: - PROGRAM\_CONTENT - FINAL\_DISTRIBUTOR |
| nielsenNaesIiNwSettings | [NielsenNaesIiNw](#channels-channelid-start-model-nielsennaesiinw) | False | Complete these fields only if you want to insert watermarks of type Nielsen NAES II (N2) and Nielsen NAES VI (NW). |

### Output
<a name="channels-channelid-start-model-output"></a>

Output settings. There can be multiple outputs within a group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionNames | Array of type string | False | The names of the AudioDescriptions used as audio sources for this output. |
| captionDescriptionNames | Array of type string | False | The names of the CaptionDescriptions used as caption sources for this output. |
| outputName | string<br />MinLength: 1<br />MaxLength: 255 | False | The name used to identify an output. |
| outputSettings | [OutputSettings](#channels-channelid-start-model-outputsettings) | True | Output type-specific settings. |
| videoDescriptionName | string | False | The name of the VideoDescription used as the source for this output. |

### OutputDestination
<a name="channels-channelid-start-model-outputdestination"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | User-specified id. This is used in an output group or an output. |
| mediaPackageSettings | Array of type [MediaPackageOutputDestinationSettings](#channels-channelid-start-model-mediapackageoutputdestinationsettings) | False | Destination settings for a MediaPackage output; one destination for both encoders. |
| multiplexSettings | [MultiplexProgramChannelDestinationSettings](#channels-channelid-start-model-multiplexprogramchanneldestinationsettings) | False | Destination settings for a Multiplex output; one destination for both encoders. |
| settings | Array of type [OutputDestinationSettings](#channels-channelid-start-model-outputdestinationsettings) | False | Destination settings for a standard output; one destination for each redundant encoder. |

### OutputDestinationSettings
<a name="channels-channelid-start-model-outputdestinationsettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | key used to extract the password from EC2 Parameter store |
| streamName | string | False | Stream name for RTMP destinations (URLs of type rtmp://) |
| url | string | False | A URL specifying a destination |
| username | string | False | username for destination |

### OutputGroup
<a name="channels-channelid-start-model-outputgroup"></a>

Output groups for this Live Event. Output groups contain information about where streams should be distributed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string<br />MaxLength: 32 | False | Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed. |
| outputGroupSettings | [OutputGroupSettings](#channels-channelid-start-model-outputgroupsettings) | True | Settings associated with the output group. |
| outputs | Array of type [Output](#channels-channelid-start-model-output) | True |  |

### OutputGroupSettings
<a name="channels-channelid-start-model-outputgroupsettings"></a>

Output Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveGroupSettings | [ArchiveGroupSettings](#channels-channelid-start-model-archivegroupsettings) | False |  |
| frameCaptureGroupSettings | [FrameCaptureGroupSettings](#channels-channelid-start-model-framecapturegroupsettings) | False |  |
| hlsGroupSettings | [HlsGroupSettings](#channels-channelid-start-model-hlsgroupsettings) | False |  |
| mediaPackageGroupSettings | [MediaPackageGroupSettings](#channels-channelid-start-model-mediapackagegroupsettings) | False |  |
| msSmoothGroupSettings | [MsSmoothGroupSettings](#channels-channelid-start-model-mssmoothgroupsettings) | False |  |
| multiplexGroupSettings | [MultiplexGroupSettings](#channels-channelid-start-model-multiplexgroupsettings) | False |  |
| rtmpGroupSettings | [RtmpGroupSettings](#channels-channelid-start-model-rtmpgroupsettings) | False |  |
| udpGroupSettings | [UdpGroupSettings](#channels-channelid-start-model-udpgroupsettings) | False |  |

### OutputLocationRef
<a name="channels-channelid-start-model-outputlocationref"></a>

Reference to an OutputDestination ID defined in the channel

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationRefId | string | False |  |

### OutputSettings
<a name="channels-channelid-start-model-outputsettings"></a>

Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveOutputSettings | [ArchiveOutputSettings](#channels-channelid-start-model-archiveoutputsettings) | False |  |
| frameCaptureOutputSettings | [FrameCaptureOutputSettings](#channels-channelid-start-model-framecaptureoutputsettings) | False |  |
| hlsOutputSettings | [HlsOutputSettings](#channels-channelid-start-model-hlsoutputsettings) | False |  |
| mediaPackageOutputSettings | [MediaPackageOutputSettings](#channels-channelid-start-model-mediapackageoutputsettings) | False |  |
| msSmoothOutputSettings | [MsSmoothOutputSettings](#channels-channelid-start-model-mssmoothoutputsettings) | False |  |
| multiplexOutputSettings | [MultiplexOutputSettings](#channels-channelid-start-model-multiplexoutputsettings) | False |  |
| rtmpOutputSettings | [RtmpOutputSettings](#channels-channelid-start-model-rtmpoutputsettings) | False |  |
| udpOutputSettings | [UdpOutputSettings](#channels-channelid-start-model-udpoutputsettings) | False |  |

### PassThroughSettings
<a name="channels-channelid-start-model-passthroughsettings"></a>

Pass Through Settings

### PipelineDetail
<a name="channels-channelid-start-model-pipelinedetail"></a>

Runtime details of a pipeline when a channel is running.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInputAttachmentName | string | False | The name of the active input attachment currently being ingested by this pipeline. |
| activeInputSwitchActionName | string | False | The name of the input switch schedule action that occurred most recently and that resulted in the switch to the current input attachment for this pipeline. |
| activeMotionGraphicsActionName | string | False | The name of the motion graphics activate action that occurred most recently and that resulted in the current graphics URI for this pipeline. |
| activeMotionGraphicsUri | string | False | The current URI being used for HTML5 motion graphics for this pipeline. |
| pipelineId | string | False | Pipeline ID |

### RawSettings
<a name="channels-channelid-start-model-rawsettings"></a>

Raw Settings

### Rec601Settings
<a name="channels-channelid-start-model-rec601settings"></a>

Rec601 Settings

### Rec709Settings
<a name="channels-channelid-start-model-rec709settings"></a>

Rec709 Settings

### RemixSettings
<a name="channels-channelid-start-model-remixsettings"></a>

Remix Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelMappings | Array of type [AudioChannelMapping](#channels-channelid-start-model-audiochannelmapping) | True | Mapping of input channels to output channels, with appropriate gain adjustments. |
| channelsIn | integer<br />Minimum: 1<br />Maximum: 16 | False | Number of input channels to be used. |
| channelsOut | integer<br />Minimum: 1<br />Maximum: 8 | False | Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8 |

### ResourceConflict
<a name="channels-channelid-start-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="channels-channelid-start-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### RtmpAdMarkers
<a name="channels-channelid-start-model-rtmpadmarkers"></a>

Rtmp Ad Markers
+ `ON_CUE_POINT_SCTE35`

### RtmpCacheFullBehavior
<a name="channels-channelid-start-model-rtmpcachefullbehavior"></a>

Rtmp Cache Full Behavior
+ `DISCONNECT_IMMEDIATELY`
+ `WAIT_FOR_SERVER`

### RtmpCaptionData
<a name="channels-channelid-start-model-rtmpcaptiondata"></a>

Rtmp Caption Data
+ `ALL`
+ `FIELD1_608`
+ `FIELD1_AND_FIELD2_608`

### RtmpCaptionInfoDestinationSettings
<a name="channels-channelid-start-model-rtmpcaptioninfodestinationsettings"></a>

Rtmp Caption Info Destination Settings

### RtmpGroupSettings
<a name="channels-channelid-start-model-rtmpgroupsettings"></a>

Rtmp Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adMarkers | Array of type [RtmpAdMarkers](#channels-channelid-start-model-rtmpadmarkers) | False | Choose the ad marker type for this output group. MediaLive will create a message based on the content of each SCTE-35 message, format it for that marker type, and insert it in the datastream. |
| authenticationScheme | [AuthenticationScheme](#channels-channelid-start-model-authenticationscheme) | False | Authentication scheme to use when connecting with CDN |
| cacheFullBehavior | [RtmpCacheFullBehavior](#channels-channelid-start-model-rtmpcachefullbehavior) | False | Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again. |
| cacheLength | integer<br />Minimum: 30 | False | Cache length, in seconds, is used to calculate buffer size. |
| captionData | [RtmpCaptionData](#channels-channelid-start-model-rtmpcaptiondata) | False | Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed. |
| inputLossAction | [InputLossActionForRtmpOut](#channels-channelid-start-model-inputlossactionforrtmpout) | False | Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection. |
| restartDelay | integer<br />Minimum: 0 | False | If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart. |

### RtmpOutputCertificateMode
<a name="channels-channelid-start-model-rtmpoutputcertificatemode"></a>

Rtmp Output Certificate Mode
+ `SELF_SIGNED`
+ `VERIFY_AUTHENTICITY`

### RtmpOutputSettings
<a name="channels-channelid-start-model-rtmpoutputsettings"></a>

Rtmp Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateMode | [RtmpOutputCertificateMode](#channels-channelid-start-model-rtmpoutputcertificatemode) | False | If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail. |
| connectionRetryInterval | integer<br />Minimum: 1 | False | Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost. |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers. |
| numRetries | integer<br />Minimum: 0 | False | Number of retry attempts. |

### S3CannedAcl
<a name="channels-channelid-start-model-s3cannedacl"></a>

S3 Canned Acl
+ `AUTHENTICATED_READ`
+ `BUCKET_OWNER_FULL_CONTROL`
+ `BUCKET_OWNER_READ`
+ `PUBLIC_READ`

### Scte20Convert608To708
<a name="channels-channelid-start-model-scte20convert608to708"></a>

Scte20 Convert608 To708
+ `DISABLED`
+ `UPCONVERT`

### Scte20PlusEmbeddedDestinationSettings
<a name="channels-channelid-start-model-scte20plusembeddeddestinationsettings"></a>

Scte20 Plus Embedded Destination Settings

### Scte20SourceSettings
<a name="channels-channelid-start-model-scte20sourcesettings"></a>

Scte20 Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [Scte20Convert608To708](#channels-channelid-start-model-scte20convert608to708) | False | If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded. |
| source608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough. |

### Scte27DestinationSettings
<a name="channels-channelid-start-model-scte27destinationsettings"></a>

Scte27 Destination Settings

### Scte27OcrLanguage
<a name="channels-channelid-start-model-scte27ocrlanguage"></a>

Scte27 Ocr Language
+ `DEU`
+ `ENG`
+ `FRA`
+ `NLD`
+ `POR`
+ `SPA`

### Scte27SourceSettings
<a name="channels-channelid-start-model-scte27sourcesettings"></a>

Scte27 Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ocrLanguage | [Scte27OcrLanguage](#channels-channelid-start-model-scte27ocrlanguage) | False | If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text. |
| pid | integer<br />Minimum: 1 | False | The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is "informational". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through. |

### Scte35AposNoRegionalBlackoutBehavior
<a name="channels-channelid-start-model-scte35aposnoregionalblackoutbehavior"></a>

Scte35 Apos No Regional Blackout Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35AposWebDeliveryAllowedBehavior
<a name="channels-channelid-start-model-scte35aposwebdeliveryallowedbehavior"></a>

Scte35 Apos Web Delivery Allowed Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35SpliceInsert
<a name="channels-channelid-start-model-scte35spliceinsert"></a>

Scte35 Splice Insert

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages. |
| noRegionalBlackoutFlag | [Scte35SpliceInsertNoRegionalBlackoutBehavior](#channels-channelid-start-model-scte35spliceinsertnoregionalblackoutbehavior) | False | When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates |
| webDeliveryAllowedFlag | [Scte35SpliceInsertWebDeliveryAllowedBehavior](#channels-channelid-start-model-scte35spliceinsertwebdeliveryallowedbehavior) | False | When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates |

### Scte35SpliceInsertNoRegionalBlackoutBehavior
<a name="channels-channelid-start-model-scte35spliceinsertnoregionalblackoutbehavior"></a>

Scte35 Splice Insert No Regional Blackout Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35SpliceInsertWebDeliveryAllowedBehavior
<a name="channels-channelid-start-model-scte35spliceinsertwebdeliveryallowedbehavior"></a>

Scte35 Splice Insert Web Delivery Allowed Behavior
+ `FOLLOW`
+ `IGNORE`

### Scte35TimeSignalApos
<a name="channels-channelid-start-model-scte35timesignalapos"></a>

Scte35 Time Signal Apos

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages. |
| noRegionalBlackoutFlag | [Scte35AposNoRegionalBlackoutBehavior](#channels-channelid-start-model-scte35aposnoregionalblackoutbehavior) | False | When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates |
| webDeliveryAllowedFlag | [Scte35AposWebDeliveryAllowedBehavior](#channels-channelid-start-model-scte35aposwebdeliveryallowedbehavior) | False | When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates |

### SmoothGroupAudioOnlyTimecodeControl
<a name="channels-channelid-start-model-smoothgroupaudioonlytimecodecontrol"></a>

Smooth Group Audio Only Timecode Control
+ `PASSTHROUGH`
+ `USE_CONFIGURED_CLOCK`

### SmoothGroupCertificateMode
<a name="channels-channelid-start-model-smoothgroupcertificatemode"></a>

Smooth Group Certificate Mode
+ `SELF_SIGNED`
+ `VERIFY_AUTHENTICITY`

### SmoothGroupEventIdMode
<a name="channels-channelid-start-model-smoothgroupeventidmode"></a>

Smooth Group Event Id Mode
+ `NO_EVENT_ID`
+ `USE_CONFIGURED`
+ `USE_TIMESTAMP`

### SmoothGroupEventStopBehavior
<a name="channels-channelid-start-model-smoothgroupeventstopbehavior"></a>

Smooth Group Event Stop Behavior
+ `NONE`
+ `SEND_EOS`

### SmoothGroupSegmentationMode
<a name="channels-channelid-start-model-smoothgroupsegmentationmode"></a>

Smooth Group Segmentation Mode
+ `USE_INPUT_SEGMENTATION`
+ `USE_SEGMENT_DURATION`

### SmoothGroupSparseTrackType
<a name="channels-channelid-start-model-smoothgroupsparsetracktype"></a>

Smooth Group Sparse Track Type
+ `NONE`
+ `SCTE_35`
+ `SCTE_35_WITHOUT_SEGMENTATION`

### SmoothGroupStreamManifestBehavior
<a name="channels-channelid-start-model-smoothgroupstreammanifestbehavior"></a>

Smooth Group Stream Manifest Behavior
+ `DO_NOT_SEND`
+ `SEND`

### SmoothGroupTimestampOffsetMode
<a name="channels-channelid-start-model-smoothgrouptimestampoffsetmode"></a>

Smooth Group Timestamp Offset Mode
+ `USE_CONFIGURED_OFFSET`
+ `USE_EVENT_START_DATE`

### Smpte2038DataPreference
<a name="channels-channelid-start-model-smpte2038datapreference"></a>

Smpte2038 Data Preference
+ `IGNORE`
+ `PREFER`

### SmpteTtDestinationSettings
<a name="channels-channelid-start-model-smptettdestinationsettings"></a>

Smpte Tt Destination Settings

### StandardHlsSettings
<a name="channels-channelid-start-model-standardhlssettings"></a>

Standard Hls Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioRenditionSets | string | False | List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','. |
| m3u8Settings | [M3u8Settings](#channels-channelid-start-model-m3u8settings) | True |  |

### StaticKeySettings
<a name="channels-channelid-start-model-statickeysettings"></a>

Static Key Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| keyProviderServer | [InputLocation](#channels-channelid-start-model-inputlocation) | False | The URL of the license server used for protecting content. |
| staticKeyValue | string<br />MinLength: 32<br />MaxLength: 32 | True | Static key value as a 32 character hexadecimal string. |

### Tags
<a name="channels-channelid-start-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TeletextDestinationSettings
<a name="channels-channelid-start-model-teletextdestinationsettings"></a>

Teletext Destination Settings

### TeletextSourceSettings
<a name="channels-channelid-start-model-teletextsourcesettings"></a>

Teletext Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputRectangle | [CaptionRectangle](#channels-channelid-start-model-captionrectangle) | False | Optionally defines a region where TTML style captions will be displayed |
| pageNumber | string | False | Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix. |

### TemporalFilterPostFilterSharpening
<a name="channels-channelid-start-model-temporalfilterpostfiltersharpening"></a>

Temporal Filter Post Filter Sharpening
+ `AUTO`
+ `DISABLED`
+ `ENABLED`

### TemporalFilterSettings
<a name="channels-channelid-start-model-temporalfiltersettings"></a>

Temporal Filter Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| postFilterSharpening | [TemporalFilterPostFilterSharpening](#channels-channelid-start-model-temporalfilterpostfiltersharpening) | False | If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR. |
| strength | [TemporalFilterStrength](#channels-channelid-start-model-temporalfilterstrength) | False | Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft. |

### TemporalFilterStrength
<a name="channels-channelid-start-model-temporalfilterstrength"></a>

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

### TimecodeConfig
<a name="channels-channelid-start-model-timecodeconfig"></a>

Timecode Config

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| source | [TimecodeConfigSource](#channels-channelid-start-model-timecodeconfigsource) | True | Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00. |
| syncThreshold | integer<br />Minimum: 1<br />Maximum: 1000000 | False | Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified. |

### TimecodeConfigSource
<a name="channels-channelid-start-model-timecodeconfigsource"></a>

Timecode Config Source
+ `EMBEDDED`
+ `SYSTEMCLOCK`
+ `ZEROBASED`

### TtmlDestinationSettings
<a name="channels-channelid-start-model-ttmldestinationsettings"></a>

Ttml Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| styleControl | [TtmlDestinationStyleControl](#channels-channelid-start-model-ttmldestinationstylecontrol) | False | When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output. |

### TtmlDestinationStyleControl
<a name="channels-channelid-start-model-ttmldestinationstylecontrol"></a>

Ttml Destination Style Control
+ `PASSTHROUGH`
+ `USE_CONFIGURED`

### UdpContainerSettings
<a name="channels-channelid-start-model-udpcontainersettings"></a>

Udp Container Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| m2tsSettings | [M2tsSettings](#channels-channelid-start-model-m2tssettings) | False |  |

### UdpGroupSettings
<a name="channels-channelid-start-model-udpgroupsettings"></a>

Udp Group Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputLossAction | [InputLossActionForUdpOut](#channels-channelid-start-model-inputlossactionforudpout) | False | Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video. |
| timedMetadataId3Frame | [UdpTimedMetadataId3Frame](#channels-channelid-start-model-udptimedmetadataid3frame) | False | Indicates ID3 frame that has the timecode. |
| timedMetadataId3Period | integer<br />Minimum: 0 | False | Timed Metadata interval in seconds. |

### UdpOutputSettings
<a name="channels-channelid-start-model-udpoutputsettings"></a>

Udp Output Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bufferMsec | integer<br />Minimum: 0<br />Maximum: 10000 | False | UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc. |
| containerSettings | [UdpContainerSettings](#channels-channelid-start-model-udpcontainersettings) | True |  |
| destination | [OutputLocationRef](#channels-channelid-start-model-outputlocationref) | True | Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002). |
| fecOutputSettings | [FecOutputSettings](#channels-channelid-start-model-fecoutputsettings) | False | Settings for enabling and adjusting Forward Error Correction on UDP outputs. |

### UdpTimedMetadataId3Frame
<a name="channels-channelid-start-model-udptimedmetadataid3frame"></a>

Udp Timed Metadata Id3 Frame
+ `NONE`
+ `PRIV`
+ `TDRL`

### VideoBlackFailoverSettings
<a name="channels-channelid-start-model-videoblackfailoversettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blackDetectThreshold | number<br />Minimum: 0<br />Maximum: 1 | False | A value used in calculating the threshold below which MediaLive considers a pixel to be 'black'. For the input to be considered black, every pixel in a frame must be below this threshold. The threshold is calculated as a percentage (expressed as a decimal) of white. Therefore .1 means 10% white (or 90% black). Note how the formula works for any color depth. For example, if you set this field to 0.1 in 10-bit color depth: (1023\*0.1=102.3), which means a pixel value of 102 or less is 'black'. If you set this field to .1 in an 8-bit color depth: (255\*0.1=25.5), which means a pixel value of 25 or less is 'black'. The range is 0.0 to 1.0, with any number of decimal places. |
| videoBlackThresholdMsec | integer<br />Minimum: 1000 | False | The amount of time (in milliseconds) that the active input must be black before automatic input failover occurs. |

### VideoCodecSettings
<a name="channels-channelid-start-model-videocodecsettings"></a>

Video Codec Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| frameCaptureSettings | [FrameCaptureSettings](#channels-channelid-start-model-framecapturesettings) | False |  |
| h264Settings | [H264Settings](#channels-channelid-start-model-h264settings) | False |  |
| h265Settings | [H265Settings](#channels-channelid-start-model-h265settings) | False |  |
| mpeg2Settings | [Mpeg2Settings](#channels-channelid-start-model-mpeg2settings) | False |  |

### VideoDescription
<a name="channels-channelid-start-model-videodescription"></a>

Video settings for this stream.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| codecSettings | [VideoCodecSettings](#channels-channelid-start-model-videocodecsettings) | False | Video codec settings. |
| height | integer | False | Output video height, in pixels. Must be an even number. For most codecs, you can leave this field and width blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required. |
| name | string | True | The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event. |
| respondToAfd | [VideoDescriptionRespondToAfd](#channels-channelid-start-model-videodescriptionrespondtoafd) | False | Indicates how MediaLive will respond to the AFD values that might be in the input video. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose PASSTHROUGH. RESPOND: MediaLive clips the input video using a formula that uses the AFD values (configured in afdSignaling ), the input display aspect ratio, and the output display aspect ratio. MediaLive also includes the AFD values in the output, unless the codec for this encode is FRAME\_CAPTURE. PASSTHROUGH: MediaLive ignores the AFD values and does not clip the video. But MediaLive does include the values in the output. NONE: MediaLive does not clip the input video and does not include the AFD values in the output |
| scalingBehavior | [VideoDescriptionScalingBehavior](#channels-channelid-start-model-videodescriptionscalingbehavior) | False | STRETCH\_TO\_OUTPUT configures the output position to stretch the video to the specified output resolution (height and width). This option will override any position value. DEFAULT may insert black boxes (pillar boxes or letter boxes) around the video to provide the specified output resolution. |
| sharpness | integer<br />Minimum: 0<br />Maximum: 100 | False | Changes the strength of the anti-alias filter used for scaling. 0 is the softest setting, 100 is the sharpest. A setting of 50 is recommended for most content. |
| width | integer | False | Output video width, in pixels. Must be an even number. For most codecs, you can leave this field and height blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required. |

### VideoDescriptionRespondToAfd
<a name="channels-channelid-start-model-videodescriptionrespondtoafd"></a>

Video Description Respond To Afd
+ `NONE`
+ `PASSTHROUGH`
+ `RESPOND`

### VideoDescriptionScalingBehavior
<a name="channels-channelid-start-model-videodescriptionscalingbehavior"></a>

Video Description Scaling Behavior
+ `DEFAULT`
+ `STRETCH_TO_OUTPUT`

### VideoSelector
<a name="channels-channelid-start-model-videoselector"></a>

Specifies a particular video stream within an input source. An input may have only a single video selector.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorSpace | [VideoSelectorColorSpace](#channels-channelid-start-model-videoselectorcolorspace) | False | Specifies the color space of an input. This setting works in tandem with colorSpaceUsage and a video description's colorSpaceSettingsChoice to determine if any conversion will be performed. |
| colorSpaceSettings | [VideoSelectorColorSpaceSettings](#channels-channelid-start-model-videoselectorcolorspacesettings) | False | Color space settings |
| colorSpaceUsage | [VideoSelectorColorSpaceUsage](#channels-channelid-start-model-videoselectorcolorspaceusage) | False | Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data. |
| selectorSettings | [VideoSelectorSettings](#channels-channelid-start-model-videoselectorsettings) | False | The video selector settings. |

### VideoSelectorColorSpace
<a name="channels-channelid-start-model-videoselectorcolorspace"></a>

Video Selector Color Space
+ `FOLLOW`
+ `HDR10`
+ `HLG_2020`
+ `REC_601`
+ `REC_709`

### VideoSelectorColorSpaceSettings
<a name="channels-channelid-start-model-videoselectorcolorspacesettings"></a>

Video Selector Color Space Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hdr10Settings | [Hdr10Settings](#channels-channelid-start-model-hdr10settings) | False |  |

### VideoSelectorColorSpaceUsage
<a name="channels-channelid-start-model-videoselectorcolorspaceusage"></a>

Video Selector Color Space Usage
+ `FALLBACK`
+ `FORCE`

### VideoSelectorPid
<a name="channels-channelid-start-model-videoselectorpid"></a>

Video Selector Pid

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 0<br />Maximum: 8191 | False | Selects a specific PID from within a video source. |

### VideoSelectorProgramId
<a name="channels-channelid-start-model-videoselectorprogramid"></a>

Video Selector Program Id

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| programId | integer<br />Minimum: 0<br />Maximum: 65536 | False | Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default. |

### VideoSelectorSettings
<a name="channels-channelid-start-model-videoselectorsettings"></a>

Video Selector Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| videoSelectorPid | [VideoSelectorPid](#channels-channelid-start-model-videoselectorpid) | False |  |
| videoSelectorProgramId | [VideoSelectorProgramId](#channels-channelid-start-model-videoselectorprogramid) | False |  |

### VpcOutputSettingsDescription
<a name="channels-channelid-start-model-vpcoutputsettingsdescription"></a>

The properties for a private VPC Output

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZones | Array of type string | False | The Availability Zones where the vpc subnets are located. The first Availability Zone applies to the first subnet in the list of subnets. The second Availability Zone applies to the second subnet.  |
| networkInterfaceIds | Array of type string | False | A list of Elastic Network Interfaces created by MediaLive in the customer's VPC  |
| securityGroupIds | Array of type string | False | A list of up EC2 VPC security group IDs attached to the Output VPC network interfaces.  |
| subnetIds | Array of type string | False | A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ).  |

### WavCodingMode
<a name="channels-channelid-start-model-wavcodingmode"></a>

Wav Coding Mode
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_4_0`
+ `CODING_MODE_8_0`

### WavSettings
<a name="channels-channelid-start-model-wavsettings"></a>

Wav Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | number | False | Bits per sample. |
| codingMode | [WavCodingMode](#channels-channelid-start-model-wavcodingmode) | False | The audio coding mode for the WAV audio. The mode determines the number of channels in the audio. |
| sampleRate | number | False | Sample rate in Hz. |

### WebvttDestinationSettings
<a name="channels-channelid-start-model-webvttdestinationsettings"></a>

Webvtt Destination Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| styleControl | [WebvttDestinationStyleControl](#channels-channelid-start-model-webvttdestinationstylecontrol) | False | Controls whether the color and position of the source captions is passed through to the WebVTT output captions. PASSTHROUGH - Valid only if the source captions are EMBEDDED or TELETEXT. NO\_STYLE\_DATA - Don't pass through the style. The output captions will not contain any font styling information. |

### WebvttDestinationStyleControl
<a name="channels-channelid-start-model-webvttdestinationstylecontrol"></a>

Webvtt Destination Style Control
+ `NO_STYLE_DATA`
+ `PASSTHROUGH`

## See also
<a name="channels-channelid-start-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StartChannel
<a name="StartChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/StartChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/StartChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/StartChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/StartChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/StartChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/StartChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/StartChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/StartChannel)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/StartChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/StartChannel)
