---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html
---

# Presets
<a name="presets"></a>

## URI
<a name="presets-url"></a>

`/2017-08-29/presets`

## HTTP methods
<a name="presets-http-methods"></a>

### GET
<a name="presetsget"></a>

**Operation ID:** `ListPresets`

Retrieve a JSON array of up to twenty of your presets. This will return the presets themselves, not just a list of them. To retrieve the next twenty presets, use the nextToken string returned with the array.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| category | String | False |  |
| listBy | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |
| order | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListPresetsResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### POST
<a name="presetspost"></a>

**Operation ID:** `CreatePreset`

Create a new preset. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreatePresetResponse | 201 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="presetsoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="presets-schemas"></a>

### Request bodies
<a name="presets-request-examples"></a>

#### GET schema
<a name="presets-request-body-get-example"></a>

```
{
  "listBy": enum,
  "category": "string",
  "order": enum,
  "nextToken": "string",
  "maxResults": integer
}
```

#### POST schema
<a name="presets-request-body-post-example"></a>

```
{
  "description": "string",
  "category": "string",
  "name": "string",
  "settings": {
    "videoDescription": {
      "fixedAfd": integer,
      "width": integer,
      "scalingBehavior": enum,
      "crop": {
        "height": integer,
        "width": integer,
        "x": integer,
        "y": integer
      },
      "height": integer,
      "videoPreprocessors": {
        "colorCorrector": {
          "brightness": integer,
          "colorSpaceConversion": enum,
          "sampleRangeConversion": enum,
          "clipLimits": {
            "minimumYUV": integer,
            "maximumYUV": integer,
            "minimumRGBTolerance": integer,
            "maximumRGBTolerance": integer
          },
          "sdrReferenceWhiteLevel": integer,
          "contrast": integer,
          "hue": integer,
          "saturation": integer,
          "maxLuminance": integer,
          "hdr10Metadata": {
            "redPrimaryX": integer,
            "redPrimaryY": integer,
            "greenPrimaryX": integer,
            "greenPrimaryY": integer,
            "bluePrimaryX": integer,
            "bluePrimaryY": integer,
            "whitePointX": integer,
            "whitePointY": integer,
            "maxFrameAverageLightLevel": integer,
            "maxContentLightLevel": integer,
            "maxLuminance": integer,
            "minLuminance": integer
          },
          "hdrToSdrToneMapper": enum
        },
        "deinterlacer": {
          "algorithm": enum,
          "mode": enum,
          "control": enum
        },
        "dolbyVision": {
          "profile": enum,
          "l6Mode": enum,
          "l6Metadata": {
            "maxCll": integer,
            "maxFall": integer
          },
          "mapping": enum,
          "compatibility": enum
        },
        "hdr10Plus": {
          "masteringMonitorNits": integer,
          "targetMonitorNits": integer
        },
        "imageInserter": {
          "insertableImages": [
            {
              "width": integer,
              "height": integer,
              "imageX": integer,
              "imageY": integer,
              "duration": integer,
              "fadeIn": integer,
              "layer": integer,
              "imageInserterInput": "string",
              "startTime": "string",
              "fadeOut": integer,
              "opacity": integer
            }
          ],
          "sdrReferenceWhiteLevel": integer
        },
        "noiseReducer": {
          "filter": enum,
          "filterSettings": {
            "strength": integer
          },
          "spatialFilterSettings": {
            "strength": integer,
            "speed": integer,
            "postFilterSharpenStrength": integer
          },
          "temporalFilterSettings": {
            "strength": integer,
            "speed": integer,
            "aggressiveMode": integer,
            "postTemporalSharpening": enum,
            "postTemporalSharpeningStrength": enum
          }
        },
        "timecodeBurnin": {
          "fontSize": integer,
          "position": enum,
          "prefix": "string"
        },
        "partnerWatermarking": {
          "nexguardFileMarkerSettings": {
            "license": "string",
            "preset": "string",
            "payload": integer,
            "strength": enum
          }
        }
      },
      "timecodeInsertion": enum,
      "timecodeTrack": enum,
      "antiAlias": enum,
      "position": {
        "height": integer,
        "width": integer,
        "x": integer,
        "y": integer
      },
      "sharpness": integer,
      "codecSettings": {
        "codec": enum,
        "av1Settings": {
          "gopSize": number,
          "numberBFramesBetweenReferenceFrames": integer,
          "slices": integer,
          "bitDepth": enum,
          "rateControlMode": enum,
          "qvbrSettings": {
            "qvbrQualityLevel": integer,
            "qvbrQualityLevelFineTune": number
          },
          "maxBitrate": integer,
          "adaptiveQuantization": enum,
          "spatialAdaptiveQuantization": enum,
          "framerateControl": enum,
          "framerateConversionAlgorithm": enum,
          "framerateNumerator": integer,
          "framerateDenominator": integer,
          "filmGrainSynthesis": enum,
          "perFrameMetrics": [
            enum
          ]
        },
        "avcIntraSettings": {
          "avcIntraClass": enum,
          "avcIntraUhdSettings": {
            "qualityTuningLevel": enum
          },
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "framerateDenominator": integer,
          "slowPal": enum,
          "framerateControl": enum,
          "telecine": enum,
          "framerateNumerator": integer,
          "framerateConversionAlgorithm": enum,
          "perFrameMetrics": [
            enum
          ]
        },
        "frameCaptureSettings": {
          "framerateNumerator": integer,
          "framerateDenominator": integer,
          "maxCaptures": integer,
          "quality": integer
        },
        "gifSettings": {
          "framerateControl": enum,
          "framerateConversionAlgorithm": enum,
          "framerateNumerator": integer,
          "framerateDenominator": integer
        },
        "h264Settings": {
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "parNumerator": integer,
          "numberReferenceFrames": integer,
          "syntax": enum,
          "softness": integer,
          "framerateDenominator": integer,
          "gopClosedCadence": integer,
          "hrdBufferInitialFillPercentage": integer,
          "gopSize": number,
          "slices": integer,
          "gopBReference": enum,
          "hrdBufferSize": integer,
          "maxBitrate": integer,
          "slowPal": enum,
          "parDenominator": integer,
          "spatialAdaptiveQuantization": enum,
          "temporalAdaptiveQuantization": enum,
          "flickerAdaptiveQuantization": enum,
          "entropyEncoding": enum,
          "bitrate": integer,
          "framerateControl": enum,
          "rateControlMode": enum,
          "qvbrSettings": {
            "qvbrQualityLevel": integer,
            "qvbrQualityLevelFineTune": number,
            "maxAverageBitrate": integer
          },
          "codecProfile": enum,
          "telecine": enum,
          "framerateNumerator": integer,
          "minIInterval": integer,
          "adaptiveQuantization": enum,
          "saliencyAwareEncoding": enum,
          "codecLevel": enum,
          "fieldEncoding": enum,
          "sceneChangeDetect": enum,
          "qualityTuningLevel": enum,
          "framerateConversionAlgorithm": enum,
          "unregisteredSeiTimecode": enum,
          "gopSizeUnits": enum,
          "parControl": enum,
          "numberBFramesBetweenReferenceFrames": integer,
          "repeatPps": enum,
          "writeMp4PackagingType": enum,
          "dynamicSubGop": enum,
          "hrdBufferFinalFillPercentage": integer,
          "bandwidthReductionFilter": {
            "strength": enum,
            "sharpening": enum
          },
          "endOfStreamMarkers": enum,
          "perFrameMetrics": [
            enum
          ]
        },
        "h265Settings": {
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "parNumerator": integer,
          "numberReferenceFrames": integer,
          "framerateDenominator": integer,
          "gopClosedCadence": integer,
          "alternateTransferFunctionSei": enum,
          "hrdBufferInitialFillPercentage": integer,
          "gopSize": number,
          "slices": integer,
          "gopBReference": enum,
          "hrdBufferSize": integer,
          "maxBitrate": integer,
          "slowPal": enum,
          "parDenominator": integer,
          "spatialAdaptiveQuantization": enum,
          "temporalAdaptiveQuantization": enum,
          "flickerAdaptiveQuantization": enum,
          "bitrate": integer,
          "framerateControl": enum,
          "rateControlMode": enum,
          "qvbrSettings": {
            "qvbrQualityLevel": integer,
            "qvbrQualityLevelFineTune": number,
            "maxAverageBitrate": integer
          },
          "codecProfile": enum,
          "tiles": enum,
          "telecine": enum,
          "framerateNumerator": integer,
          "minIInterval": integer,
          "adaptiveQuantization": enum,
          "codecLevel": enum,
          "sceneChangeDetect": enum,
          "qualityTuningLevel": enum,
          "framerateConversionAlgorithm": enum,
          "unregisteredSeiTimecode": enum,
          "gopSizeUnits": enum,
          "parControl": enum,
          "numberBFramesBetweenReferenceFrames": integer,
          "temporalIds": enum,
          "sampleAdaptiveOffsetFilterMode": enum,
          "writeMp4PackagingType": enum,
          "dynamicSubGop": enum,
          "hrdBufferFinalFillPercentage": integer,
          "endOfStreamMarkers": enum,
          "deblocking": enum,
          "tileWidth": integer,
          "tileHeight": integer,
          "tilePadding": enum,
          "mvTemporalPredictor": enum,
          "mvOverPictureBoundaries": enum,
          "treeBlockSize": enum,
          "bandwidthReductionFilter": {
            "strength": enum,
            "sharpening": enum
          },
          "perFrameMetrics": [
            enum
          ]
        },
        "mpeg2Settings": {
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "parNumerator": integer,
          "syntax": enum,
          "softness": integer,
          "framerateDenominator": integer,
          "gopClosedCadence": integer,
          "hrdBufferInitialFillPercentage": integer,
          "gopSize": number,
          "hrdBufferSize": integer,
          "maxBitrate": integer,
          "slowPal": enum,
          "parDenominator": integer,
          "spatialAdaptiveQuantization": enum,
          "temporalAdaptiveQuantization": enum,
          "bitrate": integer,
          "intraDcPrecision": enum,
          "framerateControl": enum,
          "rateControlMode": enum,
          "codecProfile": enum,
          "telecine": enum,
          "framerateNumerator": integer,
          "minIInterval": integer,
          "adaptiveQuantization": enum,
          "codecLevel": enum,
          "sceneChangeDetect": enum,
          "qualityTuningLevel": enum,
          "framerateConversionAlgorithm": enum,
          "gopSizeUnits": enum,
          "parControl": enum,
          "numberBFramesBetweenReferenceFrames": integer,
          "dynamicSubGop": enum,
          "hrdBufferFinalFillPercentage": integer,
          "perFrameMetrics": [
            enum
          ]
        },
        "proresSettings": {
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "parNumerator": integer,
          "framerateDenominator": integer,
          "codecProfile": enum,
          "slowPal": enum,
          "parDenominator": integer,
          "framerateControl": enum,
          "telecine": enum,
          "chromaSampling": enum,
          "framerateNumerator": integer,
          "framerateConversionAlgorithm": enum,
          "parControl": enum,
          "perFrameMetrics": [
            enum
          ]
        },
        "uncompressedSettings": {
          "framerateControl": enum,
          "framerateConversionAlgorithm": enum,
          "framerateNumerator": integer,
          "framerateDenominator": integer,
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "telecine": enum,
          "slowPal": enum,
          "fourcc": enum
        },
        "vc3Settings": {
          "vc3Class": enum,
          "interlaceMode": enum,
          "scanTypeConversionMode": enum,
          "framerateConversionAlgorithm": enum,
          "telecine": enum,
          "slowPal": enum,
          "framerateControl": enum,
          "framerateDenominator": integer,
          "framerateNumerator": integer
        },
        "vp8Settings": {
          "qualityTuningLevel": enum,
          "rateControlMode": enum,
          "gopSize": number,
          "maxBitrate": integer,
          "bitrate": integer,
          "hrdBufferSize": integer,
          "framerateControl": enum,
          "framerateConversionAlgorithm": enum,
          "framerateNumerator": integer,
          "framerateDenominator": integer,
          "parControl": enum,
          "parNumerator": integer,
          "parDenominator": integer
        },
        "vp9Settings": {
          "qualityTuningLevel": enum,
          "rateControlMode": enum,
          "gopSize": number,
          "maxBitrate": integer,
          "bitrate": integer,
          "hrdBufferSize": integer,
          "framerateControl": enum,
          "framerateConversionAlgorithm": enum,
          "framerateNumerator": integer,
          "framerateDenominator": integer,
          "parControl": enum,
          "parNumerator": integer,
          "parDenominator": integer
        },
        "xavcSettings": {
          "profile": enum,
          "xavcHdIntraCbgProfileSettings": {
            "xavcClass": enum
          },
          "xavc4kIntraCbgProfileSettings": {
            "xavcClass": enum
          },
          "xavc4kIntraVbrProfileSettings": {
            "xavcClass": enum
          },
          "xavcHdProfileSettings": {
            "bitrateClass": enum,
            "slices": integer,
            "hrdBufferSize": integer,
            "qualityTuningLevel": enum,
            "interlaceMode": enum,
            "telecine": enum,
            "gopClosedCadence": integer,
            "gopBReference": enum,
            "flickerAdaptiveQuantization": enum
          },
          "xavc4kProfileSettings": {
            "bitrateClass": enum,
            "slices": integer,
            "hrdBufferSize": integer,
            "codecProfile": enum,
            "qualityTuningLevel": enum,
            "gopClosedCadence": integer,
            "gopBReference": enum,
            "flickerAdaptiveQuantization": enum
          },
          "softness": integer,
          "framerateDenominator": integer,
          "slowPal": enum,
          "spatialAdaptiveQuantization": enum,
          "temporalAdaptiveQuantization": enum,
          "entropyEncoding": enum,
          "framerateControl": enum,
          "framerateNumerator": integer,
          "adaptiveQuantization": enum,
          "framerateConversionAlgorithm": enum,
          "perFrameMetrics": [
            enum
          ]
        },
        "passthroughSettings": {
          "videoSelectorMode": enum,
          "frameControl": enum
        }
      },
      "afdSignaling": enum,
      "dropFrameTimecode": enum,
      "respondToAfd": enum,
      "chromaPositionMode": enum,
      "colorMetadata": enum
    },
    "audioDescriptions": [
      {
        "audioTypeControl": enum,
        "audioSourceName": "string",
        "audioNormalizationSettings": {
          "algorithm": enum,
          "algorithmControl": enum,
          "correctionGateLevel": integer,
          "loudnessLogging": enum,
          "targetLkfs": number,
          "peakCalculation": enum,
          "truePeakLimiterThreshold": number
        },
        "audioPitchCorrectionSettings": {
          "slowPalPitchCorrection": enum
        },
        "audioChannelTaggingSettings": {
          "channelTag": enum,
          "channelTags": [
            enum
          ]
        },
        "codecSettings": {
          "codec": enum,
          "aacSettings": {
            "audioDescriptionBroadcasterMix": enum,
            "vbrQuality": enum,
            "bitrate": integer,
            "rateControlMode": enum,
            "codecProfile": enum,
            "codingMode": enum,
            "rawFormat": enum,
            "rapInterval": integer,
            "targetLoudnessRange": integer,
            "loudnessMeasurementMode": enum,
            "sampleRate": integer,
            "specification": enum
          },
          "ac3Settings": {
            "bitrate": integer,
            "bitstreamMode": enum,
            "codingMode": enum,
            "dialnorm": integer,
            "dynamicRangeCompressionProfile": enum,
            "dynamicRangeCompressionLine": enum,
            "dynamicRangeCompressionRf": enum,
            "metadataControl": enum,
            "lfeFilter": enum,
            "sampleRate": integer
          },
          "ac4Settings": {
            "bitrate": integer,
            "bitstreamMode": enum,
            "codingMode": enum,
            "dynamicRangeCompressionHomeTheater": enum,
            "dynamicRangeCompressionFlatPanelTv": enum,
            "dynamicRangeCompressionPortableSpeakers": enum,
            "dynamicRangeCompressionPortableHeadphones": enum,
            "stereoDownmix": enum,
            "ltRtCenterMixLevel": number,
            "ltRtSurroundMixLevel": number,
            "loRoCenterMixLevel": number,
            "loRoSurroundMixLevel": number,
            "sampleRate": integer
          },
          "aiffSettings": {
            "bitDepth": integer,
            "channels": integer,
            "sampleRate": integer
          },
          "eac3Settings": {
            "metadataControl": enum,
            "surroundExMode": enum,
            "loRoSurroundMixLevel": number,
            "phaseControl": enum,
            "dialnorm": integer,
            "ltRtSurroundMixLevel": number,
            "bitrate": integer,
            "ltRtCenterMixLevel": number,
            "passthroughControl": enum,
            "lfeControl": enum,
            "loRoCenterMixLevel": number,
            "attenuationControl": enum,
            "codingMode": enum,
            "surroundMode": enum,
            "bitstreamMode": enum,
            "lfeFilter": enum,
            "stereoDownmix": enum,
            "dynamicRangeCompressionRf": enum,
            "sampleRate": integer,
            "dynamicRangeCompressionLine": enum,
            "dcFilter": enum
          },
          "eac3AtmosSettings": {
            "surroundExMode": enum,
            "loRoSurroundMixLevel": number,
            "ltRtSurroundMixLevel": number,
            "bitrate": integer,
            "ltRtCenterMixLevel": number,
            "loRoCenterMixLevel": number,
            "codingMode": enum,
            "bitstreamMode": enum,
            "stereoDownmix": enum,
            "dynamicRangeCompressionRf": enum,
            "sampleRate": integer,
            "dynamicRangeCompressionLine": enum,
            "downmixControl": enum,
            "dynamicRangeControl": enum,
            "meteringMode": enum,
            "dialogueIntelligence": enum,
            "speechThreshold": integer
          },
          "flacSettings": {
            "bitDepth": integer,
            "channels": integer,
            "sampleRate": integer
          },
          "mp2Settings": {
            "audioDescriptionMix": enum,
            "bitrate": integer,
            "channels": integer,
            "sampleRate": integer
          },
          "mp3Settings": {
            "bitrate": integer,
            "channels": integer,
            "rateControlMode": enum,
            "sampleRate": integer,
            "vbrQuality": integer
          },
          "opusSettings": {
            "bitrate": integer,
            "channels": integer,
            "sampleRate": integer
          },
          "vorbisSettings": {
            "channels": integer,
            "sampleRate": integer,
            "vbrQuality": integer
          },
          "wavSettings": {
            "bitDepth": integer,
            "channels": integer,
            "sampleRate": integer,
            "format": enum
          }
        },
        "remixSettings": {
          "channelMapping": {
            "outputChannels": [
              {
                "inputChannels": [
                  integer
                ],
                "inputChannelsFineTune": [
                  number
                ]
              }
            ]
          },
          "channelsIn": integer,
          "channelsOut": integer,
          "audioDescriptionAudioChannel": integer,
          "audioDescriptionDataChannel": integer
        },
        "streamName": "string",
        "languageCodeControl": enum,
        "audioType": integer,
        "customLanguageCode": "string",
        "languageCode": enum
      }
    ],
    "containerSettings": {
      "container": enum,
      "m3u8Settings": {
        "audioFramesPerPes": integer,
        "pcrControl": enum,
        "dataPTSControl": enum,
        "maxPcrInterval": integer,
        "pcrPid": integer,
        "pmtPid": integer,
        "privateMetadataPid": integer,
        "programNumber": integer,
        "patInterval": integer,
        "pmtInterval": integer,
        "scte35Source": enum,
        "scte35Pid": integer,
        "nielsenId3": enum,
        "timedMetadata": enum,
        "timedMetadataPid": integer,
        "transportStreamId": integer,
        "videoPid": integer,
        "ptsOffsetMode": enum,
        "ptsOffset": integer,
        "audioPtsOffsetDelta": integer,
        "audioPids": [
          integer
        ],
        "audioDuration": enum
      },
      "f4vSettings": {
        "moovPlacement": enum
      },
      "m2tsSettings": {
        "audioBufferModel": enum,
        "minEbpInterval": integer,
        "esRateInPes": enum,
        "patInterval": integer,
        "dvbNitSettings": {
          "nitInterval": integer,
          "networkId": integer,
          "networkName": "string"
        },
        "dvbSdtSettings": {
          "outputSdt": enum,
          "sdtInterval": integer,
          "serviceName": "string",
          "serviceProviderName": "string"
        },
        "scte35Source": enum,
        "scte35Pid": integer,
        "scte35Esam": {
          "scte35EsamPid": integer
        },
        "klvMetadata": enum,
        "videoPid": integer,
        "dvbTdtSettings": {
          "tdtInterval": integer
        },
        "pmtInterval": integer,
        "segmentationStyle": enum,
        "segmentationTime": number,
        "pmtPid": integer,
        "bitrate": integer,
        "audioPids": [
          integer
        ],
        "privateMetadataPid": integer,
        "nielsenId3": enum,
        "timedMetadataPid": integer,
        "maxPcrInterval": integer,
        "transportStreamId": integer,
        "dvbSubPids": [
          integer
        ],
        "rateMode": enum,
        "audioFramesPerPes": integer,
        "pcrControl": enum,
        "dataPTSControl": enum,
        "segmentationMarkers": enum,
        "ebpAudioInterval": enum,
        "forceTsVideoEbpOrder": enum,
        "programNumber": integer,
        "pcrPid": integer,
        "bufferModel": enum,
        "dvbTeletextPid": integer,
        "fragmentTime": number,
        "ebpPlacement": enum,
        "nullPacketBitrate": number,
        "audioDuration": enum,
        "ptsOffsetMode": enum,
        "ptsOffset": integer,
        "audioPtsOffsetDelta": integer,
        "preventBufferUnderflow": enum
      },
      "movSettings": {
        "clapAtom": enum,
        "cslgAtom": enum,
        "paddingControl": enum,
        "reference": enum,
        "mpeg2FourCCControl": enum
      },
      "mp4Settings": {
        "cslgAtom": enum,
        "cttsVersion": integer,
        "freeSpaceBox": enum,
        "mp4MajorBrand": "string",
        "moovPlacement": enum,
        "audioDuration": enum,
        "c2paManifest": enum,
        "certificateSecret": "string",
        "signingKmsKey": "string"
      },
      "mpdSettings": {
        "accessibilityCaptionHints": enum,
        "captionContainerType": enum,
        "scte35Source": enum,
        "scte35Esam": enum,
        "audioDuration": enum,
        "timedMetadata": enum,
        "timedMetadataBoxVersion": enum,
        "timedMetadataSchemeIdUri": "string",
        "timedMetadataValue": "string",
        "manifestMetadataSignaling": enum,
        "klvMetadata": enum,
        "c2paManifest": enum,
        "certificateSecret": "string",
        "signingKmsKey": "string"
      },
      "cmfcSettings": {
        "scte35Source": enum,
        "scte35Esam": enum,
        "audioDuration": enum,
        "iFrameOnlyManifest": enum,
        "audioGroupId": "string",
        "audioRenditionSets": "string",
        "audioTrackType": enum,
        "descriptiveVideoServiceFlag": enum,
        "timedMetadata": enum,
        "timedMetadataBoxVersion": enum,
        "timedMetadataSchemeIdUri": "string",
        "timedMetadataValue": "string",
        "manifestMetadataSignaling": enum,
        "klvMetadata": enum,
        "c2paManifest": enum,
        "certificateSecret": "string",
        "signingKmsKey": "string"
      },
      "mxfSettings": {
        "afdSignaling": enum,
        "profile": enum,
        "uncompressedAudioWrapping": enum,
        "xavcProfileSettings": {
          "durationMode": enum,
          "maxAncDataSize": integer
        }
      }
    },
    "captionDescriptions": [
      {
        "destinationSettings": {
          "destinationType": enum,
          "burninDestinationSettings": {
            "backgroundOpacity": integer,
            "shadowXOffset": integer,
            "teletextSpacing": enum,
            "alignment": enum,
            "outlineSize": integer,
            "yPosition": integer,
            "shadowColor": enum,
            "fontOpacity": integer,
            "fontSize": integer,
            "fontScript": enum,
            "fallbackFont": enum,
            "fontFileRegular": "string",
            "fontFileBold": "string",
            "fontFileItalic": "string",
            "fontFileBoldItalic": "string",
            "fontColor": enum,
            "hexFontColor": "string",
            "applyFontColor": enum,
            "backgroundColor": enum,
            "fontResolution": integer,
            "outlineColor": enum,
            "shadowYOffset": integer,
            "xPosition": integer,
            "shadowOpacity": integer,
            "stylePassthrough": enum,
            "removeRubyReserveAttributes": enum
          },
          "dvbSubDestinationSettings": {
            "backgroundOpacity": integer,
            "shadowXOffset": integer,
            "teletextSpacing": enum,
            "alignment": enum,
            "outlineSize": integer,
            "yPosition": integer,
            "shadowColor": enum,
            "fontOpacity": integer,
            "fontSize": integer,
            "fontScript": enum,
            "fallbackFont": enum,
            "fontFileRegular": "string",
            "fontFileBold": "string",
            "fontFileItalic": "string",
            "fontFileBoldItalic": "string",
            "fontColor": enum,
            "hexFontColor": "string",
            "applyFontColor": enum,
            "backgroundColor": enum,
            "fontResolution": integer,
            "outlineColor": enum,
            "shadowYOffset": integer,
            "xPosition": integer,
            "shadowOpacity": integer,
            "subtitlingType": enum,
            "ddsHandling": enum,
            "ddsXCoordinate": integer,
            "ddsYCoordinate": integer,
            "width": integer,
            "height": integer,
            "stylePassthrough": enum
          },
          "sccDestinationSettings": {
            "framerate": enum
          },
          "teletextDestinationSettings": {
            "pageNumber": "string",
            "pageTypes": [
              enum
            ]
          },
          "ttmlDestinationSettings": {
            "stylePassthrough": enum
          },
          "imscDestinationSettings": {
            "stylePassthrough": enum,
            "accessibility": enum
          },
          "embeddedDestinationSettings": {
            "destination608ChannelNumber": integer,
            "destination708ServiceNumber": integer
          },
          "webvttDestinationSettings": {
            "stylePassthrough": enum,
            "accessibility": enum
          },
          "srtDestinationSettings": {
            "stylePassthrough": enum
          }
        },
        "customLanguageCode": "string",
        "languageCode": enum,
        "languageDescription": "string"
      }
    ]
  },
  "tags": {
  }
}
```

### Response bodies
<a name="presets-response-examples"></a>

#### ListPresetsResponse schema
<a name="presets-response-body-listpresetsresponse-example"></a>

```
{
  "presets": [
    {
      "arn": "string",
      "createdAt": "string",
      "lastUpdated": "string",
      "description": "string",
      "category": "string",
      "name": "string",
      "type": enum,
      "settings": {
        "videoDescription": {
          "fixedAfd": integer,
          "width": integer,
          "scalingBehavior": enum,
          "crop": {
            "height": integer,
            "width": integer,
            "x": integer,
            "y": integer
          },
          "height": integer,
          "videoPreprocessors": {
            "colorCorrector": {
              "brightness": integer,
              "colorSpaceConversion": enum,
              "sampleRangeConversion": enum,
              "clipLimits": {
                "minimumYUV": integer,
                "maximumYUV": integer,
                "minimumRGBTolerance": integer,
                "maximumRGBTolerance": integer
              },
              "sdrReferenceWhiteLevel": integer,
              "contrast": integer,
              "hue": integer,
              "saturation": integer,
              "maxLuminance": integer,
              "hdr10Metadata": {
                "redPrimaryX": integer,
                "redPrimaryY": integer,
                "greenPrimaryX": integer,
                "greenPrimaryY": integer,
                "bluePrimaryX": integer,
                "bluePrimaryY": integer,
                "whitePointX": integer,
                "whitePointY": integer,
                "maxFrameAverageLightLevel": integer,
                "maxContentLightLevel": integer,
                "maxLuminance": integer,
                "minLuminance": integer
              },
              "hdrToSdrToneMapper": enum
            },
            "deinterlacer": {
              "algorithm": enum,
              "mode": enum,
              "control": enum
            },
            "dolbyVision": {
              "profile": enum,
              "l6Mode": enum,
              "l6Metadata": {
                "maxCll": integer,
                "maxFall": integer
              },
              "mapping": enum,
              "compatibility": enum
            },
            "hdr10Plus": {
              "masteringMonitorNits": integer,
              "targetMonitorNits": integer
            },
            "imageInserter": {
              "insertableImages": [
                {
                  "width": integer,
                  "height": integer,
                  "imageX": integer,
                  "imageY": integer,
                  "duration": integer,
                  "fadeIn": integer,
                  "layer": integer,
                  "imageInserterInput": "string",
                  "startTime": "string",
                  "fadeOut": integer,
                  "opacity": integer
                }
              ],
              "sdrReferenceWhiteLevel": integer
            },
            "noiseReducer": {
              "filter": enum,
              "filterSettings": {
                "strength": integer
              },
              "spatialFilterSettings": {
                "strength": integer,
                "speed": integer,
                "postFilterSharpenStrength": integer
              },
              "temporalFilterSettings": {
                "strength": integer,
                "speed": integer,
                "aggressiveMode": integer,
                "postTemporalSharpening": enum,
                "postTemporalSharpeningStrength": enum
              }
            },
            "timecodeBurnin": {
              "fontSize": integer,
              "position": enum,
              "prefix": "string"
            },
            "partnerWatermarking": {
              "nexguardFileMarkerSettings": {
                "license": "string",
                "preset": "string",
                "payload": integer,
                "strength": enum
              }
            }
          },
          "timecodeInsertion": enum,
          "timecodeTrack": enum,
          "antiAlias": enum,
          "position": {
            "height": integer,
            "width": integer,
            "x": integer,
            "y": integer
          },
          "sharpness": integer,
          "codecSettings": {
            "codec": enum,
            "av1Settings": {
              "gopSize": number,
              "numberBFramesBetweenReferenceFrames": integer,
              "slices": integer,
              "bitDepth": enum,
              "rateControlMode": enum,
              "qvbrSettings": {
                "qvbrQualityLevel": integer,
                "qvbrQualityLevelFineTune": number
              },
              "maxBitrate": integer,
              "adaptiveQuantization": enum,
              "spatialAdaptiveQuantization": enum,
              "framerateControl": enum,
              "framerateConversionAlgorithm": enum,
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "filmGrainSynthesis": enum,
              "perFrameMetrics": [
                enum
              ]
            },
            "avcIntraSettings": {
              "avcIntraClass": enum,
              "avcIntraUhdSettings": {
                "qualityTuningLevel": enum
              },
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "framerateDenominator": integer,
              "slowPal": enum,
              "framerateControl": enum,
              "telecine": enum,
              "framerateNumerator": integer,
              "framerateConversionAlgorithm": enum,
              "perFrameMetrics": [
                enum
              ]
            },
            "frameCaptureSettings": {
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "maxCaptures": integer,
              "quality": integer
            },
            "gifSettings": {
              "framerateControl": enum,
              "framerateConversionAlgorithm": enum,
              "framerateNumerator": integer,
              "framerateDenominator": integer
            },
            "h264Settings": {
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "parNumerator": integer,
              "numberReferenceFrames": integer,
              "syntax": enum,
              "softness": integer,
              "framerateDenominator": integer,
              "gopClosedCadence": integer,
              "hrdBufferInitialFillPercentage": integer,
              "gopSize": number,
              "slices": integer,
              "gopBReference": enum,
              "hrdBufferSize": integer,
              "maxBitrate": integer,
              "slowPal": enum,
              "parDenominator": integer,
              "spatialAdaptiveQuantization": enum,
              "temporalAdaptiveQuantization": enum,
              "flickerAdaptiveQuantization": enum,
              "entropyEncoding": enum,
              "bitrate": integer,
              "framerateControl": enum,
              "rateControlMode": enum,
              "qvbrSettings": {
                "qvbrQualityLevel": integer,
                "qvbrQualityLevelFineTune": number,
                "maxAverageBitrate": integer
              },
              "codecProfile": enum,
              "telecine": enum,
              "framerateNumerator": integer,
              "minIInterval": integer,
              "adaptiveQuantization": enum,
              "saliencyAwareEncoding": enum,
              "codecLevel": enum,
              "fieldEncoding": enum,
              "sceneChangeDetect": enum,
              "qualityTuningLevel": enum,
              "framerateConversionAlgorithm": enum,
              "unregisteredSeiTimecode": enum,
              "gopSizeUnits": enum,
              "parControl": enum,
              "numberBFramesBetweenReferenceFrames": integer,
              "repeatPps": enum,
              "writeMp4PackagingType": enum,
              "dynamicSubGop": enum,
              "hrdBufferFinalFillPercentage": integer,
              "bandwidthReductionFilter": {
                "strength": enum,
                "sharpening": enum
              },
              "endOfStreamMarkers": enum,
              "perFrameMetrics": [
                enum
              ]
            },
            "h265Settings": {
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "parNumerator": integer,
              "numberReferenceFrames": integer,
              "framerateDenominator": integer,
              "gopClosedCadence": integer,
              "alternateTransferFunctionSei": enum,
              "hrdBufferInitialFillPercentage": integer,
              "gopSize": number,
              "slices": integer,
              "gopBReference": enum,
              "hrdBufferSize": integer,
              "maxBitrate": integer,
              "slowPal": enum,
              "parDenominator": integer,
              "spatialAdaptiveQuantization": enum,
              "temporalAdaptiveQuantization": enum,
              "flickerAdaptiveQuantization": enum,
              "bitrate": integer,
              "framerateControl": enum,
              "rateControlMode": enum,
              "qvbrSettings": {
                "qvbrQualityLevel": integer,
                "qvbrQualityLevelFineTune": number,
                "maxAverageBitrate": integer
              },
              "codecProfile": enum,
              "tiles": enum,
              "telecine": enum,
              "framerateNumerator": integer,
              "minIInterval": integer,
              "adaptiveQuantization": enum,
              "codecLevel": enum,
              "sceneChangeDetect": enum,
              "qualityTuningLevel": enum,
              "framerateConversionAlgorithm": enum,
              "unregisteredSeiTimecode": enum,
              "gopSizeUnits": enum,
              "parControl": enum,
              "numberBFramesBetweenReferenceFrames": integer,
              "temporalIds": enum,
              "sampleAdaptiveOffsetFilterMode": enum,
              "writeMp4PackagingType": enum,
              "dynamicSubGop": enum,
              "hrdBufferFinalFillPercentage": integer,
              "endOfStreamMarkers": enum,
              "deblocking": enum,
              "tileWidth": integer,
              "tileHeight": integer,
              "tilePadding": enum,
              "mvTemporalPredictor": enum,
              "mvOverPictureBoundaries": enum,
              "treeBlockSize": enum,
              "bandwidthReductionFilter": {
                "strength": enum,
                "sharpening": enum
              },
              "perFrameMetrics": [
                enum
              ]
            },
            "mpeg2Settings": {
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "parNumerator": integer,
              "syntax": enum,
              "softness": integer,
              "framerateDenominator": integer,
              "gopClosedCadence": integer,
              "hrdBufferInitialFillPercentage": integer,
              "gopSize": number,
              "hrdBufferSize": integer,
              "maxBitrate": integer,
              "slowPal": enum,
              "parDenominator": integer,
              "spatialAdaptiveQuantization": enum,
              "temporalAdaptiveQuantization": enum,
              "bitrate": integer,
              "intraDcPrecision": enum,
              "framerateControl": enum,
              "rateControlMode": enum,
              "codecProfile": enum,
              "telecine": enum,
              "framerateNumerator": integer,
              "minIInterval": integer,
              "adaptiveQuantization": enum,
              "codecLevel": enum,
              "sceneChangeDetect": enum,
              "qualityTuningLevel": enum,
              "framerateConversionAlgorithm": enum,
              "gopSizeUnits": enum,
              "parControl": enum,
              "numberBFramesBetweenReferenceFrames": integer,
              "dynamicSubGop": enum,
              "hrdBufferFinalFillPercentage": integer,
              "perFrameMetrics": [
                enum
              ]
            },
            "proresSettings": {
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "parNumerator": integer,
              "framerateDenominator": integer,
              "codecProfile": enum,
              "slowPal": enum,
              "parDenominator": integer,
              "framerateControl": enum,
              "telecine": enum,
              "chromaSampling": enum,
              "framerateNumerator": integer,
              "framerateConversionAlgorithm": enum,
              "parControl": enum,
              "perFrameMetrics": [
                enum
              ]
            },
            "uncompressedSettings": {
              "framerateControl": enum,
              "framerateConversionAlgorithm": enum,
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "telecine": enum,
              "slowPal": enum,
              "fourcc": enum
            },
            "vc3Settings": {
              "vc3Class": enum,
              "interlaceMode": enum,
              "scanTypeConversionMode": enum,
              "framerateConversionAlgorithm": enum,
              "telecine": enum,
              "slowPal": enum,
              "framerateControl": enum,
              "framerateDenominator": integer,
              "framerateNumerator": integer
            },
            "vp8Settings": {
              "qualityTuningLevel": enum,
              "rateControlMode": enum,
              "gopSize": number,
              "maxBitrate": integer,
              "bitrate": integer,
              "hrdBufferSize": integer,
              "framerateControl": enum,
              "framerateConversionAlgorithm": enum,
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "parControl": enum,
              "parNumerator": integer,
              "parDenominator": integer
            },
            "vp9Settings": {
              "qualityTuningLevel": enum,
              "rateControlMode": enum,
              "gopSize": number,
              "maxBitrate": integer,
              "bitrate": integer,
              "hrdBufferSize": integer,
              "framerateControl": enum,
              "framerateConversionAlgorithm": enum,
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "parControl": enum,
              "parNumerator": integer,
              "parDenominator": integer
            },
            "xavcSettings": {
              "profile": enum,
              "xavcHdIntraCbgProfileSettings": {
                "xavcClass": enum
              },
              "xavc4kIntraCbgProfileSettings": {
                "xavcClass": enum
              },
              "xavc4kIntraVbrProfileSettings": {
                "xavcClass": enum
              },
              "xavcHdProfileSettings": {
                "bitrateClass": enum,
                "slices": integer,
                "hrdBufferSize": integer,
                "qualityTuningLevel": enum,
                "interlaceMode": enum,
                "telecine": enum,
                "gopClosedCadence": integer,
                "gopBReference": enum,
                "flickerAdaptiveQuantization": enum
              },
              "xavc4kProfileSettings": {
                "bitrateClass": enum,
                "slices": integer,
                "hrdBufferSize": integer,
                "codecProfile": enum,
                "qualityTuningLevel": enum,
                "gopClosedCadence": integer,
                "gopBReference": enum,
                "flickerAdaptiveQuantization": enum
              },
              "softness": integer,
              "framerateDenominator": integer,
              "slowPal": enum,
              "spatialAdaptiveQuantization": enum,
              "temporalAdaptiveQuantization": enum,
              "entropyEncoding": enum,
              "framerateControl": enum,
              "framerateNumerator": integer,
              "adaptiveQuantization": enum,
              "framerateConversionAlgorithm": enum,
              "perFrameMetrics": [
                enum
              ]
            },
            "passthroughSettings": {
              "videoSelectorMode": enum,
              "frameControl": enum
            }
          },
          "afdSignaling": enum,
          "dropFrameTimecode": enum,
          "respondToAfd": enum,
          "chromaPositionMode": enum,
          "colorMetadata": enum
        },
        "audioDescriptions": [
          {
            "audioTypeControl": enum,
            "audioSourceName": "string",
            "audioNormalizationSettings": {
              "algorithm": enum,
              "algorithmControl": enum,
              "correctionGateLevel": integer,
              "loudnessLogging": enum,
              "targetLkfs": number,
              "peakCalculation": enum,
              "truePeakLimiterThreshold": number
            },
            "audioPitchCorrectionSettings": {
              "slowPalPitchCorrection": enum
            },
            "audioChannelTaggingSettings": {
              "channelTag": enum,
              "channelTags": [
                enum
              ]
            },
            "codecSettings": {
              "codec": enum,
              "aacSettings": {
                "audioDescriptionBroadcasterMix": enum,
                "vbrQuality": enum,
                "bitrate": integer,
                "rateControlMode": enum,
                "codecProfile": enum,
                "codingMode": enum,
                "rawFormat": enum,
                "rapInterval": integer,
                "targetLoudnessRange": integer,
                "loudnessMeasurementMode": enum,
                "sampleRate": integer,
                "specification": enum
              },
              "ac3Settings": {
                "bitrate": integer,
                "bitstreamMode": enum,
                "codingMode": enum,
                "dialnorm": integer,
                "dynamicRangeCompressionProfile": enum,
                "dynamicRangeCompressionLine": enum,
                "dynamicRangeCompressionRf": enum,
                "metadataControl": enum,
                "lfeFilter": enum,
                "sampleRate": integer
              },
              "ac4Settings": {
                "bitrate": integer,
                "bitstreamMode": enum,
                "codingMode": enum,
                "dynamicRangeCompressionHomeTheater": enum,
                "dynamicRangeCompressionFlatPanelTv": enum,
                "dynamicRangeCompressionPortableSpeakers": enum,
                "dynamicRangeCompressionPortableHeadphones": enum,
                "stereoDownmix": enum,
                "ltRtCenterMixLevel": number,
                "ltRtSurroundMixLevel": number,
                "loRoCenterMixLevel": number,
                "loRoSurroundMixLevel": number,
                "sampleRate": integer
              },
              "aiffSettings": {
                "bitDepth": integer,
                "channels": integer,
                "sampleRate": integer
              },
              "eac3Settings": {
                "metadataControl": enum,
                "surroundExMode": enum,
                "loRoSurroundMixLevel": number,
                "phaseControl": enum,
                "dialnorm": integer,
                "ltRtSurroundMixLevel": number,
                "bitrate": integer,
                "ltRtCenterMixLevel": number,
                "passthroughControl": enum,
                "lfeControl": enum,
                "loRoCenterMixLevel": number,
                "attenuationControl": enum,
                "codingMode": enum,
                "surroundMode": enum,
                "bitstreamMode": enum,
                "lfeFilter": enum,
                "stereoDownmix": enum,
                "dynamicRangeCompressionRf": enum,
                "sampleRate": integer,
                "dynamicRangeCompressionLine": enum,
                "dcFilter": enum
              },
              "eac3AtmosSettings": {
                "surroundExMode": enum,
                "loRoSurroundMixLevel": number,
                "ltRtSurroundMixLevel": number,
                "bitrate": integer,
                "ltRtCenterMixLevel": number,
                "loRoCenterMixLevel": number,
                "codingMode": enum,
                "bitstreamMode": enum,
                "stereoDownmix": enum,
                "dynamicRangeCompressionRf": enum,
                "sampleRate": integer,
                "dynamicRangeCompressionLine": enum,
                "downmixControl": enum,
                "dynamicRangeControl": enum,
                "meteringMode": enum,
                "dialogueIntelligence": enum,
                "speechThreshold": integer
              },
              "flacSettings": {
                "bitDepth": integer,
                "channels": integer,
                "sampleRate": integer
              },
              "mp2Settings": {
                "audioDescriptionMix": enum,
                "bitrate": integer,
                "channels": integer,
                "sampleRate": integer
              },
              "mp3Settings": {
                "bitrate": integer,
                "channels": integer,
                "rateControlMode": enum,
                "sampleRate": integer,
                "vbrQuality": integer
              },
              "opusSettings": {
                "bitrate": integer,
                "channels": integer,
                "sampleRate": integer
              },
              "vorbisSettings": {
                "channels": integer,
                "sampleRate": integer,
                "vbrQuality": integer
              },
              "wavSettings": {
                "bitDepth": integer,
                "channels": integer,
                "sampleRate": integer,
                "format": enum
              }
            },
            "remixSettings": {
              "channelMapping": {
                "outputChannels": [
                  {
                    "inputChannels": [
                      integer
                    ],
                    "inputChannelsFineTune": [
                      number
                    ]
                  }
                ]
              },
              "channelsIn": integer,
              "channelsOut": integer,
              "audioDescriptionAudioChannel": integer,
              "audioDescriptionDataChannel": integer
            },
            "streamName": "string",
            "languageCodeControl": enum,
            "audioType": integer,
            "customLanguageCode": "string",
            "languageCode": enum
          }
        ],
        "containerSettings": {
          "container": enum,
          "m3u8Settings": {
            "audioFramesPerPes": integer,
            "pcrControl": enum,
            "dataPTSControl": enum,
            "maxPcrInterval": integer,
            "pcrPid": integer,
            "pmtPid": integer,
            "privateMetadataPid": integer,
            "programNumber": integer,
            "patInterval": integer,
            "pmtInterval": integer,
            "scte35Source": enum,
            "scte35Pid": integer,
            "nielsenId3": enum,
            "timedMetadata": enum,
            "timedMetadataPid": integer,
            "transportStreamId": integer,
            "videoPid": integer,
            "ptsOffsetMode": enum,
            "ptsOffset": integer,
            "audioPtsOffsetDelta": integer,
            "audioPids": [
              integer
            ],
            "audioDuration": enum
          },
          "f4vSettings": {
            "moovPlacement": enum
          },
          "m2tsSettings": {
            "audioBufferModel": enum,
            "minEbpInterval": integer,
            "esRateInPes": enum,
            "patInterval": integer,
            "dvbNitSettings": {
              "nitInterval": integer,
              "networkId": integer,
              "networkName": "string"
            },
            "dvbSdtSettings": {
              "outputSdt": enum,
              "sdtInterval": integer,
              "serviceName": "string",
              "serviceProviderName": "string"
            },
            "scte35Source": enum,
            "scte35Pid": integer,
            "scte35Esam": {
              "scte35EsamPid": integer
            },
            "klvMetadata": enum,
            "videoPid": integer,
            "dvbTdtSettings": {
              "tdtInterval": integer
            },
            "pmtInterval": integer,
            "segmentationStyle": enum,
            "segmentationTime": number,
            "pmtPid": integer,
            "bitrate": integer,
            "audioPids": [
              integer
            ],
            "privateMetadataPid": integer,
            "nielsenId3": enum,
            "timedMetadataPid": integer,
            "maxPcrInterval": integer,
            "transportStreamId": integer,
            "dvbSubPids": [
              integer
            ],
            "rateMode": enum,
            "audioFramesPerPes": integer,
            "pcrControl": enum,
            "dataPTSControl": enum,
            "segmentationMarkers": enum,
            "ebpAudioInterval": enum,
            "forceTsVideoEbpOrder": enum,
            "programNumber": integer,
            "pcrPid": integer,
            "bufferModel": enum,
            "dvbTeletextPid": integer,
            "fragmentTime": number,
            "ebpPlacement": enum,
            "nullPacketBitrate": number,
            "audioDuration": enum,
            "ptsOffsetMode": enum,
            "ptsOffset": integer,
            "audioPtsOffsetDelta": integer,
            "preventBufferUnderflow": enum
          },
          "movSettings": {
            "clapAtom": enum,
            "cslgAtom": enum,
            "paddingControl": enum,
            "reference": enum,
            "mpeg2FourCCControl": enum
          },
          "mp4Settings": {
            "cslgAtom": enum,
            "cttsVersion": integer,
            "freeSpaceBox": enum,
            "mp4MajorBrand": "string",
            "moovPlacement": enum,
            "audioDuration": enum,
            "c2paManifest": enum,
            "certificateSecret": "string",
            "signingKmsKey": "string"
          },
          "mpdSettings": {
            "accessibilityCaptionHints": enum,
            "captionContainerType": enum,
            "scte35Source": enum,
            "scte35Esam": enum,
            "audioDuration": enum,
            "timedMetadata": enum,
            "timedMetadataBoxVersion": enum,
            "timedMetadataSchemeIdUri": "string",
            "timedMetadataValue": "string",
            "manifestMetadataSignaling": enum,
            "klvMetadata": enum,
            "c2paManifest": enum,
            "certificateSecret": "string",
            "signingKmsKey": "string"
          },
          "cmfcSettings": {
            "scte35Source": enum,
            "scte35Esam": enum,
            "audioDuration": enum,
            "iFrameOnlyManifest": enum,
            "audioGroupId": "string",
            "audioRenditionSets": "string",
            "audioTrackType": enum,
            "descriptiveVideoServiceFlag": enum,
            "timedMetadata": enum,
            "timedMetadataBoxVersion": enum,
            "timedMetadataSchemeIdUri": "string",
            "timedMetadataValue": "string",
            "manifestMetadataSignaling": enum,
            "klvMetadata": enum,
            "c2paManifest": enum,
            "certificateSecret": "string",
            "signingKmsKey": "string"
          },
          "mxfSettings": {
            "afdSignaling": enum,
            "profile": enum,
            "uncompressedAudioWrapping": enum,
            "xavcProfileSettings": {
              "durationMode": enum,
              "maxAncDataSize": integer
            }
          }
        },
        "captionDescriptions": [
          {
            "destinationSettings": {
              "destinationType": enum,
              "burninDestinationSettings": {
                "backgroundOpacity": integer,
                "shadowXOffset": integer,
                "teletextSpacing": enum,
                "alignment": enum,
                "outlineSize": integer,
                "yPosition": integer,
                "shadowColor": enum,
                "fontOpacity": integer,
                "fontSize": integer,
                "fontScript": enum,
                "fallbackFont": enum,
                "fontFileRegular": "string",
                "fontFileBold": "string",
                "fontFileItalic": "string",
                "fontFileBoldItalic": "string",
                "fontColor": enum,
                "hexFontColor": "string",
                "applyFontColor": enum,
                "backgroundColor": enum,
                "fontResolution": integer,
                "outlineColor": enum,
                "shadowYOffset": integer,
                "xPosition": integer,
                "shadowOpacity": integer,
                "stylePassthrough": enum,
                "removeRubyReserveAttributes": enum
              },
              "dvbSubDestinationSettings": {
                "backgroundOpacity": integer,
                "shadowXOffset": integer,
                "teletextSpacing": enum,
                "alignment": enum,
                "outlineSize": integer,
                "yPosition": integer,
                "shadowColor": enum,
                "fontOpacity": integer,
                "fontSize": integer,
                "fontScript": enum,
                "fallbackFont": enum,
                "fontFileRegular": "string",
                "fontFileBold": "string",
                "fontFileItalic": "string",
                "fontFileBoldItalic": "string",
                "fontColor": enum,
                "hexFontColor": "string",
                "applyFontColor": enum,
                "backgroundColor": enum,
                "fontResolution": integer,
                "outlineColor": enum,
                "shadowYOffset": integer,
                "xPosition": integer,
                "shadowOpacity": integer,
                "subtitlingType": enum,
                "ddsHandling": enum,
                "ddsXCoordinate": integer,
                "ddsYCoordinate": integer,
                "width": integer,
                "height": integer,
                "stylePassthrough": enum
              },
              "sccDestinationSettings": {
                "framerate": enum
              },
              "teletextDestinationSettings": {
                "pageNumber": "string",
                "pageTypes": [
                  enum
                ]
              },
              "ttmlDestinationSettings": {
                "stylePassthrough": enum
              },
              "imscDestinationSettings": {
                "stylePassthrough": enum,
                "accessibility": enum
              },
              "embeddedDestinationSettings": {
                "destination608ChannelNumber": integer,
                "destination708ServiceNumber": integer
              },
              "webvttDestinationSettings": {
                "stylePassthrough": enum,
                "accessibility": enum
              },
              "srtDestinationSettings": {
                "stylePassthrough": enum
              }
            },
            "customLanguageCode": "string",
            "languageCode": enum,
            "languageDescription": "string"
          }
        ]
      }
    }
  ],
  "nextToken": "string"
}
```

#### CreatePresetResponse schema
<a name="presets-response-body-createpresetresponse-example"></a>

```
{
  "preset": {
    "arn": "string",
    "createdAt": "string",
    "lastUpdated": "string",
    "description": "string",
    "category": "string",
    "name": "string",
    "type": enum,
    "settings": {
      "videoDescription": {
        "fixedAfd": integer,
        "width": integer,
        "scalingBehavior": enum,
        "crop": {
          "height": integer,
          "width": integer,
          "x": integer,
          "y": integer
        },
        "height": integer,
        "videoPreprocessors": {
          "colorCorrector": {
            "brightness": integer,
            "colorSpaceConversion": enum,
            "sampleRangeConversion": enum,
            "clipLimits": {
              "minimumYUV": integer,
              "maximumYUV": integer,
              "minimumRGBTolerance": integer,
              "maximumRGBTolerance": integer
            },
            "sdrReferenceWhiteLevel": integer,
            "contrast": integer,
            "hue": integer,
            "saturation": integer,
            "maxLuminance": integer,
            "hdr10Metadata": {
              "redPrimaryX": integer,
              "redPrimaryY": integer,
              "greenPrimaryX": integer,
              "greenPrimaryY": integer,
              "bluePrimaryX": integer,
              "bluePrimaryY": integer,
              "whitePointX": integer,
              "whitePointY": integer,
              "maxFrameAverageLightLevel": integer,
              "maxContentLightLevel": integer,
              "maxLuminance": integer,
              "minLuminance": integer
            },
            "hdrToSdrToneMapper": enum
          },
          "deinterlacer": {
            "algorithm": enum,
            "mode": enum,
            "control": enum
          },
          "dolbyVision": {
            "profile": enum,
            "l6Mode": enum,
            "l6Metadata": {
              "maxCll": integer,
              "maxFall": integer
            },
            "mapping": enum,
            "compatibility": enum
          },
          "hdr10Plus": {
            "masteringMonitorNits": integer,
            "targetMonitorNits": integer
          },
          "imageInserter": {
            "insertableImages": [
              {
                "width": integer,
                "height": integer,
                "imageX": integer,
                "imageY": integer,
                "duration": integer,
                "fadeIn": integer,
                "layer": integer,
                "imageInserterInput": "string",
                "startTime": "string",
                "fadeOut": integer,
                "opacity": integer
              }
            ],
            "sdrReferenceWhiteLevel": integer
          },
          "noiseReducer": {
            "filter": enum,
            "filterSettings": {
              "strength": integer
            },
            "spatialFilterSettings": {
              "strength": integer,
              "speed": integer,
              "postFilterSharpenStrength": integer
            },
            "temporalFilterSettings": {
              "strength": integer,
              "speed": integer,
              "aggressiveMode": integer,
              "postTemporalSharpening": enum,
              "postTemporalSharpeningStrength": enum
            }
          },
          "timecodeBurnin": {
            "fontSize": integer,
            "position": enum,
            "prefix": "string"
          },
          "partnerWatermarking": {
            "nexguardFileMarkerSettings": {
              "license": "string",
              "preset": "string",
              "payload": integer,
              "strength": enum
            }
          }
        },
        "timecodeInsertion": enum,
        "timecodeTrack": enum,
        "antiAlias": enum,
        "position": {
          "height": integer,
          "width": integer,
          "x": integer,
          "y": integer
        },
        "sharpness": integer,
        "codecSettings": {
          "codec": enum,
          "av1Settings": {
            "gopSize": number,
            "numberBFramesBetweenReferenceFrames": integer,
            "slices": integer,
            "bitDepth": enum,
            "rateControlMode": enum,
            "qvbrSettings": {
              "qvbrQualityLevel": integer,
              "qvbrQualityLevelFineTune": number
            },
            "maxBitrate": integer,
            "adaptiveQuantization": enum,
            "spatialAdaptiveQuantization": enum,
            "framerateControl": enum,
            "framerateConversionAlgorithm": enum,
            "framerateNumerator": integer,
            "framerateDenominator": integer,
            "filmGrainSynthesis": enum,
            "perFrameMetrics": [
              enum
            ]
          },
          "avcIntraSettings": {
            "avcIntraClass": enum,
            "avcIntraUhdSettings": {
              "qualityTuningLevel": enum
            },
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "framerateDenominator": integer,
            "slowPal": enum,
            "framerateControl": enum,
            "telecine": enum,
            "framerateNumerator": integer,
            "framerateConversionAlgorithm": enum,
            "perFrameMetrics": [
              enum
            ]
          },
          "frameCaptureSettings": {
            "framerateNumerator": integer,
            "framerateDenominator": integer,
            "maxCaptures": integer,
            "quality": integer
          },
          "gifSettings": {
            "framerateControl": enum,
            "framerateConversionAlgorithm": enum,
            "framerateNumerator": integer,
            "framerateDenominator": integer
          },
          "h264Settings": {
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "parNumerator": integer,
            "numberReferenceFrames": integer,
            "syntax": enum,
            "softness": integer,
            "framerateDenominator": integer,
            "gopClosedCadence": integer,
            "hrdBufferInitialFillPercentage": integer,
            "gopSize": number,
            "slices": integer,
            "gopBReference": enum,
            "hrdBufferSize": integer,
            "maxBitrate": integer,
            "slowPal": enum,
            "parDenominator": integer,
            "spatialAdaptiveQuantization": enum,
            "temporalAdaptiveQuantization": enum,
            "flickerAdaptiveQuantization": enum,
            "entropyEncoding": enum,
            "bitrate": integer,
            "framerateControl": enum,
            "rateControlMode": enum,
            "qvbrSettings": {
              "qvbrQualityLevel": integer,
              "qvbrQualityLevelFineTune": number,
              "maxAverageBitrate": integer
            },
            "codecProfile": enum,
            "telecine": enum,
            "framerateNumerator": integer,
            "minIInterval": integer,
            "adaptiveQuantization": enum,
            "saliencyAwareEncoding": enum,
            "codecLevel": enum,
            "fieldEncoding": enum,
            "sceneChangeDetect": enum,
            "qualityTuningLevel": enum,
            "framerateConversionAlgorithm": enum,
            "unregisteredSeiTimecode": enum,
            "gopSizeUnits": enum,
            "parControl": enum,
            "numberBFramesBetweenReferenceFrames": integer,
            "repeatPps": enum,
            "writeMp4PackagingType": enum,
            "dynamicSubGop": enum,
            "hrdBufferFinalFillPercentage": integer,
            "bandwidthReductionFilter": {
              "strength": enum,
              "sharpening": enum
            },
            "endOfStreamMarkers": enum,
            "perFrameMetrics": [
              enum
            ]
          },
          "h265Settings": {
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "parNumerator": integer,
            "numberReferenceFrames": integer,
            "framerateDenominator": integer,
            "gopClosedCadence": integer,
            "alternateTransferFunctionSei": enum,
            "hrdBufferInitialFillPercentage": integer,
            "gopSize": number,
            "slices": integer,
            "gopBReference": enum,
            "hrdBufferSize": integer,
            "maxBitrate": integer,
            "slowPal": enum,
            "parDenominator": integer,
            "spatialAdaptiveQuantization": enum,
            "temporalAdaptiveQuantization": enum,
            "flickerAdaptiveQuantization": enum,
            "bitrate": integer,
            "framerateControl": enum,
            "rateControlMode": enum,
            "qvbrSettings": {
              "qvbrQualityLevel": integer,
              "qvbrQualityLevelFineTune": number,
              "maxAverageBitrate": integer
            },
            "codecProfile": enum,
            "tiles": enum,
            "telecine": enum,
            "framerateNumerator": integer,
            "minIInterval": integer,
            "adaptiveQuantization": enum,
            "codecLevel": enum,
            "sceneChangeDetect": enum,
            "qualityTuningLevel": enum,
            "framerateConversionAlgorithm": enum,
            "unregisteredSeiTimecode": enum,
            "gopSizeUnits": enum,
            "parControl": enum,
            "numberBFramesBetweenReferenceFrames": integer,
            "temporalIds": enum,
            "sampleAdaptiveOffsetFilterMode": enum,
            "writeMp4PackagingType": enum,
            "dynamicSubGop": enum,
            "hrdBufferFinalFillPercentage": integer,
            "endOfStreamMarkers": enum,
            "deblocking": enum,
            "tileWidth": integer,
            "tileHeight": integer,
            "tilePadding": enum,
            "mvTemporalPredictor": enum,
            "mvOverPictureBoundaries": enum,
            "treeBlockSize": enum,
            "bandwidthReductionFilter": {
              "strength": enum,
              "sharpening": enum
            },
            "perFrameMetrics": [
              enum
            ]
          },
          "mpeg2Settings": {
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "parNumerator": integer,
            "syntax": enum,
            "softness": integer,
            "framerateDenominator": integer,
            "gopClosedCadence": integer,
            "hrdBufferInitialFillPercentage": integer,
            "gopSize": number,
            "hrdBufferSize": integer,
            "maxBitrate": integer,
            "slowPal": enum,
            "parDenominator": integer,
            "spatialAdaptiveQuantization": enum,
            "temporalAdaptiveQuantization": enum,
            "bitrate": integer,
            "intraDcPrecision": enum,
            "framerateControl": enum,
            "rateControlMode": enum,
            "codecProfile": enum,
            "telecine": enum,
            "framerateNumerator": integer,
            "minIInterval": integer,
            "adaptiveQuantization": enum,
            "codecLevel": enum,
            "sceneChangeDetect": enum,
            "qualityTuningLevel": enum,
            "framerateConversionAlgorithm": enum,
            "gopSizeUnits": enum,
            "parControl": enum,
            "numberBFramesBetweenReferenceFrames": integer,
            "dynamicSubGop": enum,
            "hrdBufferFinalFillPercentage": integer,
            "perFrameMetrics": [
              enum
            ]
          },
          "proresSettings": {
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "parNumerator": integer,
            "framerateDenominator": integer,
            "codecProfile": enum,
            "slowPal": enum,
            "parDenominator": integer,
            "framerateControl": enum,
            "telecine": enum,
            "chromaSampling": enum,
            "framerateNumerator": integer,
            "framerateConversionAlgorithm": enum,
            "parControl": enum,
            "perFrameMetrics": [
              enum
            ]
          },
          "uncompressedSettings": {
            "framerateControl": enum,
            "framerateConversionAlgorithm": enum,
            "framerateNumerator": integer,
            "framerateDenominator": integer,
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "telecine": enum,
            "slowPal": enum,
            "fourcc": enum
          },
          "vc3Settings": {
            "vc3Class": enum,
            "interlaceMode": enum,
            "scanTypeConversionMode": enum,
            "framerateConversionAlgorithm": enum,
            "telecine": enum,
            "slowPal": enum,
            "framerateControl": enum,
            "framerateDenominator": integer,
            "framerateNumerator": integer
          },
          "vp8Settings": {
            "qualityTuningLevel": enum,
            "rateControlMode": enum,
            "gopSize": number,
            "maxBitrate": integer,
            "bitrate": integer,
            "hrdBufferSize": integer,
            "framerateControl": enum,
            "framerateConversionAlgorithm": enum,
            "framerateNumerator": integer,
            "framerateDenominator": integer,
            "parControl": enum,
            "parNumerator": integer,
            "parDenominator": integer
          },
          "vp9Settings": {
            "qualityTuningLevel": enum,
            "rateControlMode": enum,
            "gopSize": number,
            "maxBitrate": integer,
            "bitrate": integer,
            "hrdBufferSize": integer,
            "framerateControl": enum,
            "framerateConversionAlgorithm": enum,
            "framerateNumerator": integer,
            "framerateDenominator": integer,
            "parControl": enum,
            "parNumerator": integer,
            "parDenominator": integer
          },
          "xavcSettings": {
            "profile": enum,
            "xavcHdIntraCbgProfileSettings": {
              "xavcClass": enum
            },
            "xavc4kIntraCbgProfileSettings": {
              "xavcClass": enum
            },
            "xavc4kIntraVbrProfileSettings": {
              "xavcClass": enum
            },
            "xavcHdProfileSettings": {
              "bitrateClass": enum,
              "slices": integer,
              "hrdBufferSize": integer,
              "qualityTuningLevel": enum,
              "interlaceMode": enum,
              "telecine": enum,
              "gopClosedCadence": integer,
              "gopBReference": enum,
              "flickerAdaptiveQuantization": enum
            },
            "xavc4kProfileSettings": {
              "bitrateClass": enum,
              "slices": integer,
              "hrdBufferSize": integer,
              "codecProfile": enum,
              "qualityTuningLevel": enum,
              "gopClosedCadence": integer,
              "gopBReference": enum,
              "flickerAdaptiveQuantization": enum
            },
            "softness": integer,
            "framerateDenominator": integer,
            "slowPal": enum,
            "spatialAdaptiveQuantization": enum,
            "temporalAdaptiveQuantization": enum,
            "entropyEncoding": enum,
            "framerateControl": enum,
            "framerateNumerator": integer,
            "adaptiveQuantization": enum,
            "framerateConversionAlgorithm": enum,
            "perFrameMetrics": [
              enum
            ]
          },
          "passthroughSettings": {
            "videoSelectorMode": enum,
            "frameControl": enum
          }
        },
        "afdSignaling": enum,
        "dropFrameTimecode": enum,
        "respondToAfd": enum,
        "chromaPositionMode": enum,
        "colorMetadata": enum
      },
      "audioDescriptions": [
        {
          "audioTypeControl": enum,
          "audioSourceName": "string",
          "audioNormalizationSettings": {
            "algorithm": enum,
            "algorithmControl": enum,
            "correctionGateLevel": integer,
            "loudnessLogging": enum,
            "targetLkfs": number,
            "peakCalculation": enum,
            "truePeakLimiterThreshold": number
          },
          "audioPitchCorrectionSettings": {
            "slowPalPitchCorrection": enum
          },
          "audioChannelTaggingSettings": {
            "channelTag": enum,
            "channelTags": [
              enum
            ]
          },
          "codecSettings": {
            "codec": enum,
            "aacSettings": {
              "audioDescriptionBroadcasterMix": enum,
              "vbrQuality": enum,
              "bitrate": integer,
              "rateControlMode": enum,
              "codecProfile": enum,
              "codingMode": enum,
              "rawFormat": enum,
              "rapInterval": integer,
              "targetLoudnessRange": integer,
              "loudnessMeasurementMode": enum,
              "sampleRate": integer,
              "specification": enum
            },
            "ac3Settings": {
              "bitrate": integer,
              "bitstreamMode": enum,
              "codingMode": enum,
              "dialnorm": integer,
              "dynamicRangeCompressionProfile": enum,
              "dynamicRangeCompressionLine": enum,
              "dynamicRangeCompressionRf": enum,
              "metadataControl": enum,
              "lfeFilter": enum,
              "sampleRate": integer
            },
            "ac4Settings": {
              "bitrate": integer,
              "bitstreamMode": enum,
              "codingMode": enum,
              "dynamicRangeCompressionHomeTheater": enum,
              "dynamicRangeCompressionFlatPanelTv": enum,
              "dynamicRangeCompressionPortableSpeakers": enum,
              "dynamicRangeCompressionPortableHeadphones": enum,
              "stereoDownmix": enum,
              "ltRtCenterMixLevel": number,
              "ltRtSurroundMixLevel": number,
              "loRoCenterMixLevel": number,
              "loRoSurroundMixLevel": number,
              "sampleRate": integer
            },
            "aiffSettings": {
              "bitDepth": integer,
              "channels": integer,
              "sampleRate": integer
            },
            "eac3Settings": {
              "metadataControl": enum,
              "surroundExMode": enum,
              "loRoSurroundMixLevel": number,
              "phaseControl": enum,
              "dialnorm": integer,
              "ltRtSurroundMixLevel": number,
              "bitrate": integer,
              "ltRtCenterMixLevel": number,
              "passthroughControl": enum,
              "lfeControl": enum,
              "loRoCenterMixLevel": number,
              "attenuationControl": enum,
              "codingMode": enum,
              "surroundMode": enum,
              "bitstreamMode": enum,
              "lfeFilter": enum,
              "stereoDownmix": enum,
              "dynamicRangeCompressionRf": enum,
              "sampleRate": integer,
              "dynamicRangeCompressionLine": enum,
              "dcFilter": enum
            },
            "eac3AtmosSettings": {
              "surroundExMode": enum,
              "loRoSurroundMixLevel": number,
              "ltRtSurroundMixLevel": number,
              "bitrate": integer,
              "ltRtCenterMixLevel": number,
              "loRoCenterMixLevel": number,
              "codingMode": enum,
              "bitstreamMode": enum,
              "stereoDownmix": enum,
              "dynamicRangeCompressionRf": enum,
              "sampleRate": integer,
              "dynamicRangeCompressionLine": enum,
              "downmixControl": enum,
              "dynamicRangeControl": enum,
              "meteringMode": enum,
              "dialogueIntelligence": enum,
              "speechThreshold": integer
            },
            "flacSettings": {
              "bitDepth": integer,
              "channels": integer,
              "sampleRate": integer
            },
            "mp2Settings": {
              "audioDescriptionMix": enum,
              "bitrate": integer,
              "channels": integer,
              "sampleRate": integer
            },
            "mp3Settings": {
              "bitrate": integer,
              "channels": integer,
              "rateControlMode": enum,
              "sampleRate": integer,
              "vbrQuality": integer
            },
            "opusSettings": {
              "bitrate": integer,
              "channels": integer,
              "sampleRate": integer
            },
            "vorbisSettings": {
              "channels": integer,
              "sampleRate": integer,
              "vbrQuality": integer
            },
            "wavSettings": {
              "bitDepth": integer,
              "channels": integer,
              "sampleRate": integer,
              "format": enum
            }
          },
          "remixSettings": {
            "channelMapping": {
              "outputChannels": [
                {
                  "inputChannels": [
                    integer
                  ],
                  "inputChannelsFineTune": [
                    number
                  ]
                }
              ]
            },
            "channelsIn": integer,
            "channelsOut": integer,
            "audioDescriptionAudioChannel": integer,
            "audioDescriptionDataChannel": integer
          },
          "streamName": "string",
          "languageCodeControl": enum,
          "audioType": integer,
          "customLanguageCode": "string",
          "languageCode": enum
        }
      ],
      "containerSettings": {
        "container": enum,
        "m3u8Settings": {
          "audioFramesPerPes": integer,
          "pcrControl": enum,
          "dataPTSControl": enum,
          "maxPcrInterval": integer,
          "pcrPid": integer,
          "pmtPid": integer,
          "privateMetadataPid": integer,
          "programNumber": integer,
          "patInterval": integer,
          "pmtInterval": integer,
          "scte35Source": enum,
          "scte35Pid": integer,
          "nielsenId3": enum,
          "timedMetadata": enum,
          "timedMetadataPid": integer,
          "transportStreamId": integer,
          "videoPid": integer,
          "ptsOffsetMode": enum,
          "ptsOffset": integer,
          "audioPtsOffsetDelta": integer,
          "audioPids": [
            integer
          ],
          "audioDuration": enum
        },
        "f4vSettings": {
          "moovPlacement": enum
        },
        "m2tsSettings": {
          "audioBufferModel": enum,
          "minEbpInterval": integer,
          "esRateInPes": enum,
          "patInterval": integer,
          "dvbNitSettings": {
            "nitInterval": integer,
            "networkId": integer,
            "networkName": "string"
          },
          "dvbSdtSettings": {
            "outputSdt": enum,
            "sdtInterval": integer,
            "serviceName": "string",
            "serviceProviderName": "string"
          },
          "scte35Source": enum,
          "scte35Pid": integer,
          "scte35Esam": {
            "scte35EsamPid": integer
          },
          "klvMetadata": enum,
          "videoPid": integer,
          "dvbTdtSettings": {
            "tdtInterval": integer
          },
          "pmtInterval": integer,
          "segmentationStyle": enum,
          "segmentationTime": number,
          "pmtPid": integer,
          "bitrate": integer,
          "audioPids": [
            integer
          ],
          "privateMetadataPid": integer,
          "nielsenId3": enum,
          "timedMetadataPid": integer,
          "maxPcrInterval": integer,
          "transportStreamId": integer,
          "dvbSubPids": [
            integer
          ],
          "rateMode": enum,
          "audioFramesPerPes": integer,
          "pcrControl": enum,
          "dataPTSControl": enum,
          "segmentationMarkers": enum,
          "ebpAudioInterval": enum,
          "forceTsVideoEbpOrder": enum,
          "programNumber": integer,
          "pcrPid": integer,
          "bufferModel": enum,
          "dvbTeletextPid": integer,
          "fragmentTime": number,
          "ebpPlacement": enum,
          "nullPacketBitrate": number,
          "audioDuration": enum,
          "ptsOffsetMode": enum,
          "ptsOffset": integer,
          "audioPtsOffsetDelta": integer,
          "preventBufferUnderflow": enum
        },
        "movSettings": {
          "clapAtom": enum,
          "cslgAtom": enum,
          "paddingControl": enum,
          "reference": enum,
          "mpeg2FourCCControl": enum
        },
        "mp4Settings": {
          "cslgAtom": enum,
          "cttsVersion": integer,
          "freeSpaceBox": enum,
          "mp4MajorBrand": "string",
          "moovPlacement": enum,
          "audioDuration": enum,
          "c2paManifest": enum,
          "certificateSecret": "string",
          "signingKmsKey": "string"
        },
        "mpdSettings": {
          "accessibilityCaptionHints": enum,
          "captionContainerType": enum,
          "scte35Source": enum,
          "scte35Esam": enum,
          "audioDuration": enum,
          "timedMetadata": enum,
          "timedMetadataBoxVersion": enum,
          "timedMetadataSchemeIdUri": "string",
          "timedMetadataValue": "string",
          "manifestMetadataSignaling": enum,
          "klvMetadata": enum,
          "c2paManifest": enum,
          "certificateSecret": "string",
          "signingKmsKey": "string"
        },
        "cmfcSettings": {
          "scte35Source": enum,
          "scte35Esam": enum,
          "audioDuration": enum,
          "iFrameOnlyManifest": enum,
          "audioGroupId": "string",
          "audioRenditionSets": "string",
          "audioTrackType": enum,
          "descriptiveVideoServiceFlag": enum,
          "timedMetadata": enum,
          "timedMetadataBoxVersion": enum,
          "timedMetadataSchemeIdUri": "string",
          "timedMetadataValue": "string",
          "manifestMetadataSignaling": enum,
          "klvMetadata": enum,
          "c2paManifest": enum,
          "certificateSecret": "string",
          "signingKmsKey": "string"
        },
        "mxfSettings": {
          "afdSignaling": enum,
          "profile": enum,
          "uncompressedAudioWrapping": enum,
          "xavcProfileSettings": {
            "durationMode": enum,
            "maxAncDataSize": integer
          }
        }
      },
      "captionDescriptions": [
        {
          "destinationSettings": {
            "destinationType": enum,
            "burninDestinationSettings": {
              "backgroundOpacity": integer,
              "shadowXOffset": integer,
              "teletextSpacing": enum,
              "alignment": enum,
              "outlineSize": integer,
              "yPosition": integer,
              "shadowColor": enum,
              "fontOpacity": integer,
              "fontSize": integer,
              "fontScript": enum,
              "fallbackFont": enum,
              "fontFileRegular": "string",
              "fontFileBold": "string",
              "fontFileItalic": "string",
              "fontFileBoldItalic": "string",
              "fontColor": enum,
              "hexFontColor": "string",
              "applyFontColor": enum,
              "backgroundColor": enum,
              "fontResolution": integer,
              "outlineColor": enum,
              "shadowYOffset": integer,
              "xPosition": integer,
              "shadowOpacity": integer,
              "stylePassthrough": enum,
              "removeRubyReserveAttributes": enum
            },
            "dvbSubDestinationSettings": {
              "backgroundOpacity": integer,
              "shadowXOffset": integer,
              "teletextSpacing": enum,
              "alignment": enum,
              "outlineSize": integer,
              "yPosition": integer,
              "shadowColor": enum,
              "fontOpacity": integer,
              "fontSize": integer,
              "fontScript": enum,
              "fallbackFont": enum,
              "fontFileRegular": "string",
              "fontFileBold": "string",
              "fontFileItalic": "string",
              "fontFileBoldItalic": "string",
              "fontColor": enum,
              "hexFontColor": "string",
              "applyFontColor": enum,
              "backgroundColor": enum,
              "fontResolution": integer,
              "outlineColor": enum,
              "shadowYOffset": integer,
              "xPosition": integer,
              "shadowOpacity": integer,
              "subtitlingType": enum,
              "ddsHandling": enum,
              "ddsXCoordinate": integer,
              "ddsYCoordinate": integer,
              "width": integer,
              "height": integer,
              "stylePassthrough": enum
            },
            "sccDestinationSettings": {
              "framerate": enum
            },
            "teletextDestinationSettings": {
              "pageNumber": "string",
              "pageTypes": [
                enum
              ]
            },
            "ttmlDestinationSettings": {
              "stylePassthrough": enum
            },
            "imscDestinationSettings": {
              "stylePassthrough": enum,
              "accessibility": enum
            },
            "embeddedDestinationSettings": {
              "destination608ChannelNumber": integer,
              "destination708ServiceNumber": integer
            },
            "webvttDestinationSettings": {
              "stylePassthrough": enum,
              "accessibility": enum
            },
            "srtDestinationSettings": {
              "stylePassthrough": enum
            }
          },
          "customLanguageCode": "string",
          "languageCode": enum,
          "languageDescription": "string"
        }
      ]
    }
  }
}
```

#### ExceptionBody schema
<a name="presets-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="presets-properties"></a>

### AacAudioDescriptionBroadcasterMix
<a name="presets-model-aacaudiodescriptionbroadcastermix"></a>

Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
+ `BROADCASTER_MIXED_AD`
+ `NORMAL`

### AacCodecProfile
<a name="presets-model-aaccodecprofile"></a>

Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE.
+ `LC`
+ `HEV1`
+ `HEV2`
+ `XHE`

### AacCodingMode
<a name="presets-model-aaccodingmode"></a>

The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. \* 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. \* 1.0 Mono: One channel, C. \* 2.0 Stereo: Two channels, L, R. \* 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING\_MODE\_AUTO, and the service will automatically choose from one of the coding modes above.
+ `AD_RECEIVER_MIX`
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_5_1`
+ `CODING_MODE_AUTO`

### AacLoudnessMeasurementMode
<a name="presets-model-aacloudnessmeasurementmode"></a>

Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates.
+ `PROGRAM`
+ `ANCHOR`

### AacRateControlMode
<a name="presets-model-aacratecontrolmode"></a>

Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality.
+ `CBR`
+ `VBR`

### AacRawFormat
<a name="presets-model-aacrawformat"></a>

Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container.
+ `LATM_LOAS`
+ `NONE`

### AacSettings
<a name="presets-model-aacsettings"></a>

Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionBroadcasterMix | [AacAudioDescriptionBroadcasterMix](#presets-model-aacaudiodescriptionbroadcastermix) | False | Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType. |
| bitrate | integer<br />Minimum: 6000<br />Maximum: 1024000 | False | Specify the average bitrate in bits per second. The set of valid values for this setting is: 6000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000. The value you set is also constrained by the values that you choose for Profile, Bitrate control mode, and Sample rate. Default values depend on Bitrate control mode and Profile. |
| codecProfile | [AacCodecProfile](#presets-model-aaccodecprofile) | False | Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE. |
| codingMode | [AacCodingMode](#presets-model-aaccodingmode) | False | The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. \* 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. \* 1.0 Mono: One channel, C. \* 2.0 Stereo: Two channels, L, R. \* 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING\_MODE\_AUTO, and the service will automatically choose from one of the coding modes above. |
| loudnessMeasurementMode | [AacLoudnessMeasurementMode](#presets-model-aacloudnessmeasurementmode) | False | Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates. |
| rapInterval | integer<br />Minimum: 2000<br />Maximum: 30000 | False | Specify the RAP (Random Access Point) interval for your xHE-AAC audio output. A RAP allows a decoder to decode audio data mid-stream, without the need to reference previous audio frames, and perform adaptive audio bitrate switching. To specify the RAP interval: Enter an integer from 2000 to 30000, in milliseconds. Smaller values allow for better seeking and more frequent stream switching, while large values improve compression efficiency. To have MediaConvert automatically determine the RAP interval: Leave blank. |
| rateControlMode | [AacRateControlMode](#presets-model-aacratecontrolmode) | False | Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality. |
| rawFormat | [AacRawFormat](#presets-model-aacrawformat) | False | Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 96000 | False | Specify the AAC sample rate in samples per second (Hz). Valid sample rates depend on the AAC profile and Coding mode that you select. For a list of supported sample rates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html |
| specification | [AacSpecification](#presets-model-aacspecification) | False | Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers. |
| targetLoudnessRange | integer<br />Minimum: 6<br />Maximum: 16 | False | Specify the xHE-AAC loudness target. Enter an integer from 6 to 16, representing "loudness units". For more information, see the following specification: Supplementary information for R 128 EBU Tech 3342-2023. |
| vbrQuality | [AacVbrQuality](#presets-model-aacvbrquality) | False | Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html\#aac\_vbr |

### AacSpecification
<a name="presets-model-aacspecification"></a>

Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
+ `MPEG2`
+ `MPEG4`

### AacVbrQuality
<a name="presets-model-aacvbrquality"></a>

Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html\#aac\_vbr
+ `LOW`
+ `MEDIUM_LOW`
+ `MEDIUM_HIGH`
+ `HIGH`

### Ac3BitstreamMode
<a name="presets-model-ac3bitstreammode"></a>

Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E).
+ `COMPLETE_MAIN`
+ `COMMENTARY`
+ `DIALOGUE`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `MUSIC_AND_EFFECTS`
+ `VISUALLY_IMPAIRED`
+ `VOICE_OVER`

### Ac3CodingMode
<a name="presets-model-ac3codingmode"></a>

Dolby Digital coding mode. Determines number of channels.
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`
+ `CODING_MODE_AUTO`

### Ac3DynamicRangeCompressionLine
<a name="presets-model-ac3dynamicrangecompressionline"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`
+ `NONE`

### Ac3DynamicRangeCompressionProfile
<a name="presets-model-ac3dynamicrangecompressionprofile"></a>

When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes.
+ `FILM_STANDARD`
+ `NONE`

### Ac3DynamicRangeCompressionRf
<a name="presets-model-ac3dynamicrangecompressionrf"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`
+ `NONE`

### Ac3LfeFilter
<a name="presets-model-ac3lfefilter"></a>

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode.
+ `ENABLED`
+ `DISABLED`

### Ac3MetadataControl
<a name="presets-model-ac3metadatacontrol"></a>

When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Ac3Settings
<a name="presets-model-ac3settings"></a>

Required when you set Codec to the value AC3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 64000<br />Maximum: 640000 | False | Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 64000. Maximum: 128000. Valid bitrates for coding mode 1/1: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 3/2 with FLE: Default: 384000. Minimum: 384000. Maximum: 640000. |
| bitstreamMode | [Ac3BitstreamMode](#presets-model-ac3bitstreammode) | False | Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Ac3CodingMode](#presets-model-ac3codingmode) | False | Dolby Digital coding mode. Determines number of channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through. |
| dynamicRangeCompressionLine | [Ac3DynamicRangeCompressionLine](#presets-model-ac3dynamicrangecompressionline) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionProfile | [Ac3DynamicRangeCompressionProfile](#presets-model-ac3dynamicrangecompressionprofile) | False | When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes. |
| dynamicRangeCompressionRf | [Ac3DynamicRangeCompressionRf](#presets-model-ac3dynamicrangecompressionrf) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| lfeFilter | [Ac3LfeFilter](#presets-model-ac3lfefilter) | False | Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode. |
| metadataControl | [Ac3MetadataControl](#presets-model-ac3metadatacontrol) | False | When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |

### Ac4BitstreamMode
<a name="presets-model-ac4bitstreammode"></a>

Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb\_paec\_ac4\_bed\_classifier in the encoder implementation. - COMPLETE\_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content
+ `COMPLETE_MAIN`
+ `EMERGENCY`

### Ac4CodingMode
<a name="presets-model-ac4codingmode"></a>

Dolby AC-4 coding mode. Determines number of channels. Maps to dlb\_paec\_ac4\_bed\_channel\_config in the encoder implementation. - CODING\_MODE\_2\_0: 2.0 (stereo) - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_20 - CODING\_MODE\_3\_2\_LFE: 5.1 surround - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_51 - CODING\_MODE\_5\_1\_4: 5.1.4 immersive - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_514
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`
+ `CODING_MODE_5_1_4`

### Ac4DynamicRangeCompressionDrcProfile
<a name="presets-model-ac4dynamicrangecompressiondrcprofile"></a>

Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Ac4Settings
<a name="presets-model-ac4settings"></a>

Required when you set Codec to the value AC4.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 48000<br />Maximum: 768000 | False | Specify the average bitrate in bits per second. Leave blank to use the default bitrate for the coding mode you select according to ETSI TS 103 190. Valid bitrates for coding mode 2.0 (stereo): 48000, 64000, 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1 (3/2 with LFE): 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1.4 (immersive): 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. |
| bitstreamMode | [Ac4BitstreamMode](#presets-model-ac4bitstreammode) | False | Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb\_paec\_ac4\_bed\_classifier in the encoder implementation. - COMPLETE\_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content |
| codingMode | [Ac4CodingMode](#presets-model-ac4codingmode) | False | Dolby AC-4 coding mode. Determines number of channels. Maps to dlb\_paec\_ac4\_bed\_channel\_config in the encoder implementation. - CODING\_MODE\_2\_0: 2.0 (stereo) - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_20 - CODING\_MODE\_3\_2\_LFE: 5.1 surround - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_51 - CODING\_MODE\_5\_1\_4: 5.1.4 immersive - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_514 |
| dynamicRangeCompressionFlatPanelTv | [Ac4DynamicRangeCompressionDrcProfile](#presets-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionHomeTheater | [Ac4DynamicRangeCompressionDrcProfile](#presets-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionPortableHeadphones | [Ac4DynamicRangeCompressionDrcProfile](#presets-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionPortableSpeakers | [Ac4DynamicRangeCompressionDrcProfile](#presets-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby AC-4 setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby AC-4 setting: Left only/Right only surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby AC-4 setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby AC-4 setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| stereoDownmix | [Ac4StereoDownmix](#presets-model-ac4stereodownmix) | False | Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback. |

### Ac4StereoDownmix
<a name="presets-model-ac4stereodownmix"></a>

Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback.
+ `NOT_INDICATED`
+ `LO_RO`
+ `LT_RT`
+ `DPL2`

### AfdSignaling
<a name="presets-model-afdsignaling"></a>

This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. \* Choose None to remove all AFD values from this output. \* Choose Fixed to ignore input AFD values and instead encode the value specified in the job. \* Choose Auto to calculate output AFD values based on the input AFD scaler data.
+ `NONE`
+ `AUTO`
+ `FIXED`

### AiffSettings
<a name="presets-model-aiffsettings"></a>

Required when you set Codec to the value AIFF.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 64 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 64. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and so on, up to 64. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 192000 | False | Sample rate in Hz. |

### AntiAlias
<a name="presets-model-antialias"></a>

The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting.
+ `DISABLED`
+ `ENABLED`

### AudioChannelTag
<a name="presets-model-audiochanneltag"></a>

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track.
+ `L`
+ `R`
+ `C`
+ `LFE`
+ `LS`
+ `RS`
+ `LC`
+ `RC`
+ `CS`
+ `LSD`
+ `RSD`
+ `TCS`
+ `VHL`
+ `VHC`
+ `VHR`
+ `TBL`
+ `TBC`
+ `TBR`
+ `RSL`
+ `RSR`
+ `LW`
+ `RW`
+ `LFE2`
+ `LT`
+ `RT`
+ `HI`
+ `NAR`
+ `M`

### AudioChannelTaggingSettings
<a name="presets-model-audiochanneltaggingsettings"></a>

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelTag | [AudioChannelTag](#presets-model-audiochanneltag) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track. |
| channelTags | Array of type [AudioChannelTag](#presets-model-audiochanneltag) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track. |

### AudioCodec
<a name="presets-model-audiocodec"></a>

Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html\#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#audio-only-output
+ `AAC`
+ `MP2`
+ `MP3`
+ `WAV`
+ `AIFF`
+ `AC3`
+ `AC4`
+ `EAC3`
+ `EAC3_ATMOS`
+ `VORBIS`
+ `OPUS`
+ `PASSTHROUGH`
+ `FLAC`

### AudioCodecSettings
<a name="presets-model-audiocodecsettings"></a>

Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aacSettings | [AacSettings](#presets-model-aacsettings) | False | Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode. |
| ac3Settings | [Ac3Settings](#presets-model-ac3settings) | False | Required when you set Codec to the value AC3. |
| ac4Settings | [Ac4Settings](#presets-model-ac4settings) | False | Required when you set Codec to the value AC4. |
| aiffSettings | [AiffSettings](#presets-model-aiffsettings) | False | Required when you set Codec to the value AIFF. |
| codec | [AudioCodec](#presets-model-audiocodec) | False | Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html\#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#audio-only-output |
| eac3AtmosSettings | [Eac3AtmosSettings](#presets-model-eac3atmossettings) | False | Required when you set Codec to the value EAC3\_ATMOS. |
| eac3Settings | [Eac3Settings](#presets-model-eac3settings) | False | Required when you set Codec to the value EAC3. |
| flacSettings | [FlacSettings](#presets-model-flacsettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC. |
| mp2Settings | [Mp2Settings](#presets-model-mp2settings) | False | Required when you set Codec to the value MP2. |
| mp3Settings | [Mp3Settings](#presets-model-mp3settings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3. |
| opusSettings | [OpusSettings](#presets-model-opussettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS. |
| vorbisSettings | [VorbisSettings](#presets-model-vorbissettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis. |
| wavSettings | [WavSettings](#presets-model-wavsettings) | False | Required when you set Codec to the value WAV. |

### AudioDescription
<a name="presets-model-audiodescription"></a>

Settings related to one audio tab on the MediaConvert console. In your job JSON, an instance of AudioDescription is equivalent to one audio tab in the console. Usually, one audio tab corresponds to one output audio track. Depending on how you set up your input audio selectors and whether you use audio selector groups, one audio tab can correspond to a group of output audio tracks.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioChannelTaggingSettings | [AudioChannelTaggingSettings](#presets-model-audiochanneltaggingsettings) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF. |
| audioNormalizationSettings | [AudioNormalizationSettings](#presets-model-audionormalizationsettings) | False | Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard. |
| audioPitchCorrectionSettings | [AudioPitchCorrectionSettings](#presets-model-audiopitchcorrectionsettings) | False | Settings for audio pitch correction during framerate conversion. |
| audioSourceName | string<br />MaxLength: 2048 | False | Specifies which audio data to use from each input. In the simplest case, specify an "Audio Selector":\#inputs-audio\_selector by name based on its order within each input. For example if you specify "Audio Selector 3", then the third audio selector will be used from each input. If an input does not have an "Audio Selector 3", then the audio selector marked as "default" in that input will be used. If there is no audio selector marked as "default", silence will be inserted for the duration of that input. Alternatively, an "Audio Selector Group":\#inputs-audio\_selector\_group name may be specified, with similar default/silence behavior. If no audio\_source\_name is specified, then "Audio Selector 1" will be chosen automatically. |
| audioType | integer<br />Minimum: 0<br />Maximum: 255 | False | Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved. |
| audioTypeControl | [AudioTypeControl](#presets-model-audiotypecontrol) | False | When set to FOLLOW\_INPUT, if the input contains an ISO 639 audio\_type, then that value is passed through to the output. If the input contains no ISO 639 audio\_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER\_MIXED\_AD. |
| codecSettings | [AudioCodecSettings](#presets-model-audiocodecsettings) | False | Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec. |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{2,3}(-[A-Za-z0-9-]+)?$` | False | Specify the language for this audio output track. The service puts this language code into your output audio track when you set Language code control to Use configured. The service also uses your specified custom language code when you set Language code control to Follow input, but your input file doesn't specify a language code. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming. |
| languageCode | [LanguageCode](#presets-model-languagecode) | False | Specify the language for your output audio track. To follow the input language: Leave blank. When you do, also set Language code control to Follow input. If no input language is detected MediaConvert will not write an output language code. To follow the input langauge, but fall back to a specified language code if there is no input language to follow: Enter an ISO 639-2 three-letter language code in all capital letters. When you do, also set Language code control to Follow input. To specify the language code: Enter an ISO 639 three-letter language code in all capital letters. When you do, also set Language code control to Use configured. |
| languageCodeControl | [AudioLanguageCodeControl](#presets-model-audiolanguagecodecontrol) | False | Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify. |
| remixSettings | [RemixSettings](#presets-model-remixsettings) | False | Advanced audio remixing settings. |
| streamName | string<br />Pattern: `^[\w\s]*$` | False | Specify a label for this output audio stream. For example, "English", "Director commentary", or "track\_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting. |

### AudioLanguageCodeControl
<a name="presets-model-audiolanguagecodecontrol"></a>

Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioNormalizationAlgorithm
<a name="presets-model-audionormalizationalgorithm"></a>

Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1.
+ `ITU_BS_1770_1`
+ `ITU_BS_1770_2`
+ `ITU_BS_1770_3`
+ `ITU_BS_1770_4`

### AudioNormalizationAlgorithmControl
<a name="presets-model-audionormalizationalgorithmcontrol"></a>

When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.
+ `CORRECT_AUDIO`
+ `MEASURE_ONLY`

### AudioNormalizationLoudnessLogging
<a name="presets-model-audionormalizationloudnesslogging"></a>

If set to LOG, log each output's audio track loudness to a CSV file.
+ `LOG`
+ `DONT_LOG`

### AudioNormalizationPeakCalculation
<a name="presets-model-audionormalizationpeakcalculation"></a>

If set to TRUE\_PEAK, calculate and log the TruePeak for each output's audio track loudness.
+ `TRUE_PEAK`
+ `NONE`

### AudioNormalizationSettings
<a name="presets-model-audionormalizationsettings"></a>

Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [AudioNormalizationAlgorithm](#presets-model-audionormalizationalgorithm) | False | Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1. |
| algorithmControl | [AudioNormalizationAlgorithmControl](#presets-model-audionormalizationalgorithmcontrol) | False | When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted. |
| correctionGateLevel | integer<br />Minimum: -70<br />Maximum: 0 | False | Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected. |
| loudnessLogging | [AudioNormalizationLoudnessLogging](#presets-model-audionormalizationloudnesslogging) | False | If set to LOG, log each output's audio track loudness to a CSV file. |
| peakCalculation | [AudioNormalizationPeakCalculation](#presets-model-audionormalizationpeakcalculation) | False | If set to TRUE\_PEAK, calculate and log the TruePeak for each output's audio track loudness. |
| targetLkfs | number<br />Format: float<br />Minimum: -59.0<br />Maximum: 0.0 | False | When you use Audio normalization, optionally use this setting to specify a target loudness. If you don't specify a value here, the encoder chooses a value for you, based on the algorithm that you choose for Algorithm. If you choose algorithm 1770-1, the encoder will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS. |
| truePeakLimiterThreshold | number<br />Format: float<br />Minimum: -8.0<br />Maximum: 0.0 | False | Specify the True-peak limiter threshold in decibels relative to full scale (dBFS). The peak inter-audio sample loudness in your output will be limited to the value that you specify, without affecting the overall target LKFS. Enter a value from 0 to -8. Leave blank to use the default value 0. |

### AudioPitchCorrectionSettings
<a name="presets-model-audiopitchcorrectionsettings"></a>

Settings for audio pitch correction during framerate conversion.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| slowPalPitchCorrection | [SlowPalPitchCorrection](#presets-model-slowpalpitchcorrection) | False | Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled. |

### AudioTypeControl
<a name="presets-model-audiotypecontrol"></a>

When set to FOLLOW\_INPUT, if the input contains an ISO 639 audio\_type, then that value is passed through to the output. If the input contains no ISO 639 audio\_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER\_MIXED\_AD.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Av1AdaptiveQuantization
<a name="presets-model-av1adaptivequantization"></a>

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### Av1BitDepth
<a name="presets-model-av1bitdepth"></a>

Specify the Bit depth. You can choose 8-bit or 10-bit.
+ `BIT_8`
+ `BIT_10`

### Av1FilmGrainSynthesis
<a name="presets-model-av1filmgrainsynthesis"></a>

Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor.
+ `DISABLED`
+ `ENABLED`

### Av1FramerateControl
<a name="presets-model-av1frameratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Av1FramerateConversionAlgorithm
<a name="presets-model-av1framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Av1QvbrSettings
<a name="presets-model-av1qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the AV1 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### Av1RateControlMode
<a name="presets-model-av1ratecontrolmode"></a>

'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.'
+ `QVBR`

### Av1Settings
<a name="presets-model-av1settings"></a>

Required when you set Codec, under VideoDescription>CodecSettings to the value AV1.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Av1AdaptiveQuantization](#presets-model-av1adaptivequantization) | False | Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization. |
| bitDepth | [Av1BitDepth](#presets-model-av1bitdepth) | False | Specify the Bit depth. You can choose 8-bit or 10-bit. |
| filmGrainSynthesis | [Av1FilmGrainSynthesis](#presets-model-av1filmgrainsynthesis) | False | Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor. |
| framerateControl | [Av1FramerateControl](#presets-model-av1frameratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Av1FramerateConversionAlgorithm](#presets-model-av1framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Specify the GOP length (keyframe interval) in frames. With AV1, MediaConvert doesn't support GOP length in seconds. This value must be greater than zero and preferably equal to 1 \+ ((numberBFrames \+ 1) \* x), where x is an integer value. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 15 | False | Specify from the number of B-frames, in the range of 0-15. For AV1 encoding, we recommend using 7 or 15. Choose a larger number for a lower bitrate and smaller file size; choose a smaller number for better video quality. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qvbrSettings | [Av1QvbrSettings](#presets-model-av1qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [Av1RateControlMode](#presets-model-av1ratecontrolmode) | False | 'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.' |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Specify the number of slices per picture. This value must be 1, 2, 4, 8, 16, or 32. For progressive pictures, this value must be less than or equal to the number of macroblock rows. For interlaced pictures, this value must be less than or equal to half the number of macroblock rows. |
| spatialAdaptiveQuantization | [Av1SpatialAdaptiveQuantization](#presets-model-av1spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |

### Av1SpatialAdaptiveQuantization
<a name="presets-model-av1spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### AvcIntraClass
<a name="presets-model-avcintraclass"></a>

Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling.
+ `CLASS_50`
+ `CLASS_100`
+ `CLASS_200`
+ `CLASS_4K_2K`

### AvcIntraFramerateControl
<a name="presets-model-avcintraframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### AvcIntraFramerateConversionAlgorithm
<a name="presets-model-avcintraframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### AvcIntraInterlaceMode
<a name="presets-model-avcintrainterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### AvcIntraScanTypeConversionMode
<a name="presets-model-avcintrascantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### AvcIntraSettings
<a name="presets-model-avcintrasettings"></a>

Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| avcIntraClass | [AvcIntraClass](#presets-model-avcintraclass) | False | Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling. |
| avcIntraUhdSettings | [AvcIntraUhdSettings](#presets-model-avcintrauhdsettings) | False | Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isn't allowed. |
| framerateControl | [AvcIntraFramerateControl](#presets-model-avcintraframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [AvcIntraFramerateConversionAlgorithm](#presets-model-avcintraframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [AvcIntraInterlaceMode](#presets-model-avcintrainterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| scanTypeConversionMode | [AvcIntraScanTypeConversionMode](#presets-model-avcintrascantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [AvcIntraSlowPal](#presets-model-avcintraslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| telecine | [AvcIntraTelecine](#presets-model-avcintratelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### AvcIntraSlowPal
<a name="presets-model-avcintraslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### AvcIntraTelecine
<a name="presets-model-avcintratelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### AvcIntraUhdQualityTuningLevel
<a name="presets-model-avcintrauhdqualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass.
+ `SINGLE_PASS`
+ `MULTI_PASS`

### AvcIntraUhdSettings
<a name="presets-model-avcintrauhdsettings"></a>

Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isn't allowed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| qualityTuningLevel | [AvcIntraUhdQualityTuningLevel](#presets-model-avcintrauhdqualitytuninglevel) | False | Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass. |

### BandwidthReductionFilter
<a name="presets-model-bandwidthreductionfilter"></a>

The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sharpening | [BandwidthReductionFilterSharpening](#presets-model-bandwidthreductionfiltersharpening) | False | Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening. |
| strength | [BandwidthReductionFilterStrength](#presets-model-bandwidthreductionfilterstrength) | False | Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output. |

### BandwidthReductionFilterSharpening
<a name="presets-model-bandwidthreductionfiltersharpening"></a>

Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening.
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `OFF`

### BandwidthReductionFilterStrength
<a name="presets-model-bandwidthreductionfilterstrength"></a>

Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output.
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `AUTO`
+ `OFF`

### BurnInSubtitleStylePassthrough
<a name="presets-model-burninsubtitlestylepassthrough"></a>

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.
+ `ENABLED`
+ `DISABLED`

### BurninDestinationSettings
<a name="presets-model-burnindestinationsettings"></a>

Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [BurninSubtitleAlignment](#presets-model-burninsubtitlealignment) | False | Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. |
| applyFontColor | [BurninSubtitleApplyFontColor](#presets-model-burninsubtitleapplyfontcolor) | False | Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text. |
| backgroundColor | [BurninSubtitleBackgroundColor](#presets-model-burninsubtitlebackgroundcolor) | False | Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions. |
| fallbackFont | [BurninSubtitleFallbackFont](#presets-model-burninsubtitlefallbackfont) | False | Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input. |
| fontColor | [BurninSubtitleFontColor](#presets-model-burninsubtitlefontcolor) | False | Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. |
| fontFileBold | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file. |
| fontFileBoldItalic | string | False | Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file. |
| fontFileItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file. |
| fontFileRegular | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Specify the Font resolution in DPI (dots per inch). |
| fontScript | [FontScript](#presets-model-fontscript) | False | Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese. |
| fontSize | integer<br />Minimum: 0<br />Maximum: 96 | False | Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size. |
| hexFontColor | string<br />Pattern: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`<br />MinLength: 6<br />MaxLength: 8 | False | Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB. |
| outlineColor | [BurninSubtitleOutlineColor](#presets-model-burninsubtitleoutlinecolor) | False | Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present. |
| removeRubyReserveAttributes | [RemoveRubyReserveAttributes](#presets-model-removerubyreserveattributes) | False | Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled. |
| shadowColor | [BurninSubtitleShadowColor](#presets-model-burninsubtitleshadowcolor) | False | Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions. |
| shadowXOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. |
| shadowYOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present. |
| stylePassthrough | [BurnInSubtitleStylePassthrough](#presets-model-burninsubtitlestylepassthrough) | False | To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files. |
| teletextSpacing | [BurninSubtitleTeletextSpacing](#presets-model-burninsubtitleteletextspacing) | False | Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. |
| xPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x\_position is provided, the horizontal caption position will be determined by the alignment parameter. |
| yPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y\_position is provided, the caption will be positioned towards the bottom of the output. |

### BurninSubtitleAlignment
<a name="presets-model-burninsubtitlealignment"></a>

Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates.
+ `CENTERED`
+ `LEFT`
+ `AUTO`

### BurninSubtitleApplyFontColor
<a name="presets-model-burninsubtitleapplyfontcolor"></a>

Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text.
+ `WHITE_TEXT_ONLY`
+ `ALL_TEXT`

### BurninSubtitleBackgroundColor
<a name="presets-model-burninsubtitlebackgroundcolor"></a>

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### BurninSubtitleFallbackFont
<a name="presets-model-burninsubtitlefallbackfont"></a>

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.
+ `BEST_MATCH`
+ `MONOSPACED_SANSSERIF`
+ `MONOSPACED_SERIF`
+ `PROPORTIONAL_SANSSERIF`
+ `PROPORTIONAL_SERIF`

### BurninSubtitleFontColor
<a name="presets-model-burninsubtitlefontcolor"></a>

Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present.
+ `WHITE`
+ `BLACK`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `HEX`
+ `AUTO`

### BurninSubtitleOutlineColor
<a name="presets-model-burninsubtitleoutlinecolor"></a>

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present.
+ `BLACK`
+ `WHITE`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `AUTO`

### BurninSubtitleShadowColor
<a name="presets-model-burninsubtitleshadowcolor"></a>

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### BurninSubtitleTeletextSpacing
<a name="presets-model-burninsubtitleteletextspacing"></a>

Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions.
+ `FIXED_GRID`
+ `PROPORTIONAL`
+ `AUTO`

### CaptionDescriptionPreset
<a name="presets-model-captiondescriptionpreset"></a>

Caption Description for preset

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{2,3}(-[A-Za-z-]+)?$` | False | Specify the language for this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information when automatically selecting the font script for rendering the captions text. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming. |
| destinationSettings | [CaptionDestinationSettings](#presets-model-captiondestinationsettings) | False | Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html. |
| languageCode | [LanguageCode](#presets-model-languagecode) | False | Specify the language of this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information to choose the font language for rendering the captions text. |
| languageDescription | string | False | Specify a label for this set of output captions. For example, "English", "Director commentary", or "track\_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting. |

### CaptionDestinationSettings
<a name="presets-model-captiondestinationsettings"></a>

Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| burninDestinationSettings | [BurninDestinationSettings](#presets-model-burnindestinationsettings) | False | Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html. |
| destinationType | [CaptionDestinationType](#presets-model-captiondestinationtype) | False | Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html. If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20. |
| dvbSubDestinationSettings | [DvbSubDestinationSettings](#presets-model-dvbsubdestinationsettings) | False | Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html. |
| embeddedDestinationSettings | [EmbeddedDestinationSettings](#presets-model-embeddeddestinationsettings) | False | Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html. |
| imscDestinationSettings | [ImscDestinationSettings](#presets-model-imscdestinationsettings) | False | Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |
| sccDestinationSettings | [SccDestinationSettings](#presets-model-sccdestinationsettings) | False | Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html. |
| srtDestinationSettings | [SrtDestinationSettings](#presets-model-srtdestinationsettings) | False | Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. |
| teletextDestinationSettings | [TeletextDestinationSettings](#presets-model-teletextdestinationsettings) | False | Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html. |
| ttmlDestinationSettings | [TtmlDestinationSettings](#presets-model-ttmldestinationsettings) | False | Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |
| webvttDestinationSettings | [WebvttDestinationSettings](#presets-model-webvttdestinationsettings) | False | Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |

### CaptionDestinationType
<a name="presets-model-captiondestinationtype"></a>

Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html. If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20.
+ `BURN_IN`
+ `DVB_SUB`
+ `EMBEDDED`
+ `EMBEDDED_PLUS_SCTE20`
+ `IMSC`
+ `SCTE20_PLUS_EMBEDDED`
+ `SCC`
+ `SRT`
+ `SMI`
+ `TELETEXT`
+ `TTML`
+ `WEBVTT`

### ChannelMapping
<a name="presets-model-channelmapping"></a>

Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Don't use both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputChannels | Array of type [OutputChannelMapping](#presets-model-outputchannelmapping) | False | In your JSON job specification, include one child of OutputChannels for each audio channel that you want in your output. Each child should contain one instance of InputChannels or InputChannelsFineTune. |

### ChromaPositionMode
<a name="presets-model-chromapositionmode"></a>

Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left.
+ `AUTO`
+ `FORCE_CENTER`
+ `FORCE_TOP_LEFT`

### ClipLimits
<a name="presets-model-cliplimits"></a>

Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumRGBTolerance | integer<br />Minimum: 90<br />Maximum: 105 | False | Specify the Maximum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the upper tolerance that you specify. Enter an integer from 90 to 105 as an offset percentage to the maximum possible value. Leave blank to use the default value 100. When you specify a value for Maximum RGB tolerance, you must set Sample range conversion to Limited range clip. |
| maximumYUV | integer<br />Minimum: 920<br />Maximum: 1023 | False | Specify the Maximum YUV color sample limit. MediaConvert conforms any pixels in your input above the value that you specify to typical limited range bounds. Enter an integer from 920 to 1023. Leave blank to use the default value 940. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Maximum YUV, you must set Sample range conversion to Limited range clip. |
| minimumRGBTolerance | integer<br />Minimum: -5<br />Maximum: 10 | False | Specify the Minimum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the lower tolerance that you specify. Enter an integer from -5 to 10 as an offset percentage to the minimum possible value. Leave blank to use the default value 0. When you specify a value for Minimum RGB tolerance, you must set Sample range conversion to Limited range clip. |
| minimumYUV | integer<br />Minimum: 0<br />Maximum: 128 | False | Specify the Minimum YUV color sample limit. MediaConvert conforms any pixels in your input below the value that you specify to typical limited range bounds. Enter an integer from 0 to 128. Leave blank to use the default value 64. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Minumum YUV, you must set Sample range conversion to Limited range clip. |

### CmfcAudioDuration
<a name="presets-model-cmfcaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### CmfcAudioTrackType
<a name="presets-model-cmfcaudiotracktype"></a>

Use this setting to control the values that MediaConvert puts in your HLS parent playlist to control how the client player selects which audio track to play. Choose Audio-only variant stream (AUDIO\_ONLY\_VARIANT\_STREAM) for any variant that you want to prohibit the client from playing with video. This causes MediaConvert to represent the variant as an EXT-X-STREAM-INF in the HLS manifest. The other options for this setting determine the values that MediaConvert writes for the DEFAULT and AUTOSELECT attributes of the EXT-X-MEDIA entry for the audio variant. For more information about these attributes, see the Apple documentation article https://developer.apple.com/documentation/http\_live\_streaming/example\_playlists\_for\_http\_live\_streaming/adding\_alternate\_media\_to\_a\_playlist. Choose Alternate audio, auto select, default to set DEFAULT=YES and AUTOSELECT=YES. Choose this value for only one variant in your output group. Choose Alternate audio, auto select, not default to set DEFAULT=NO and AUTOSELECT=YES. Choose Alternate Audio, Not Auto Select to set DEFAULT=NO and AUTOSELECT=NO. When you don't specify a value for this setting, MediaConvert defaults to Alternate audio, auto select, default. When there is more than one variant in your output group, you must explicitly choose a value for this setting.
+ `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
+ `ALTERNATE_AUDIO_AUTO_SELECT`
+ `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
+ `AUDIO_ONLY_VARIANT_STREAM`

### CmfcC2paManifest
<a name="presets-model-cmfcc2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### CmfcDescriptiveVideoServiceFlag
<a name="presets-model-cmfcdescriptivevideoserviceflag"></a>

Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.
+ `DONT_FLAG`
+ `FLAG`

### CmfcIFrameOnlyManifest
<a name="presets-model-cmfciframeonlymanifest"></a>

Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you don't need the I-frame only child manifest, keep the default value Exclude.
+ `INCLUDE`
+ `EXCLUDE`

### CmfcKlvMetadata
<a name="presets-model-cmfcklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### CmfcManifestMetadataSignaling
<a name="presets-model-cmfcmanifestmetadatasignaling"></a>

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.
+ `ENABLED`
+ `DISABLED`

### CmfcScte35Esam
<a name="presets-model-cmfcscte35esam"></a>

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.
+ `INSERT`
+ `NONE`

### CmfcScte35Source
<a name="presets-model-cmfcscte35source"></a>

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output.
+ `PASSTHROUGH`
+ `NONE`

### CmfcSettings
<a name="presets-model-cmfcsettings"></a>

These settings relate to the fragmented MP4 container for the segments in your CMAF outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [CmfcAudioDuration](#presets-model-cmfcaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioGroupId | string | False | Specify the audio rendition group for this audio rendition. Specify up to one value for each audio output in your output group. This value appears in your HLS parent manifest in the EXT-X-MEDIA tag of TYPE=AUDIO, as the value for the GROUP-ID attribute. For example, if you specify "audio\_aac\_1" for Audio group ID, it appears in your manifest like this: \#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio\_aac\_1". Related setting: To associate the rendition group that this audio track belongs to with a video rendition, include the same value that you provide here for that video output's setting Audio rendition sets. |
| audioRenditionSets | string | False | List the audio rendition groups that you want included with this video rendition. Use a comma-separated list. For example, say you want to include the audio rendition groups that have the audio group IDs "audio\_aac\_1" and "audio\_dolby". Then you would specify this value: "audio\_aac\_1,audio\_dolby". Related setting: The rendition groups that you include in your comma-separated list should all match values that you specify in the setting Audio group ID for audio renditions in the same output group as this video rendition. Default behavior: If you don't specify anything here and for Audio group ID, MediaConvert puts each audio variant in its own audio rendition group and associates it with every video variant. Each value in your list appears in your HLS parent manifest in the EXT-X-STREAM-INF tag as the value for the AUDIO attribute. To continue the previous example, say that the file name for the child manifest for your video rendition is "amazing\_video\_1.m3u8". Then, in your parent manifest, each value will appear on separate lines, like this: \#EXT-X-STREAM-INF:AUDIO="audio\_aac\_1"... amazing\_video\_1.m3u8 \#EXT-X-STREAM-INF:AUDIO="audio\_dolby"... amazing\_video\_1.m3u8 |
| audioTrackType | [CmfcAudioTrackType](#presets-model-cmfcaudiotracktype) | False | Use this setting to control the values that MediaConvert puts in your HLS parent playlist to control how the client player selects which audio track to play. Choose Audio-only variant stream (AUDIO\_ONLY\_VARIANT\_STREAM) for any variant that you want to prohibit the client from playing with video. This causes MediaConvert to represent the variant as an EXT-X-STREAM-INF in the HLS manifest. The other options for this setting determine the values that MediaConvert writes for the DEFAULT and AUTOSELECT attributes of the EXT-X-MEDIA entry for the audio variant. For more information about these attributes, see the Apple documentation article https://developer.apple.com/documentation/http\_live\_streaming/example\_playlists\_for\_http\_live\_streaming/adding\_alternate\_media\_to\_a\_playlist. Choose Alternate audio, auto select, default to set DEFAULT=YES and AUTOSELECT=YES. Choose this value for only one variant in your output group. Choose Alternate audio, auto select, not default to set DEFAULT=NO and AUTOSELECT=YES. Choose Alternate Audio, Not Auto Select to set DEFAULT=NO and AUTOSELECT=NO. When you don't specify a value for this setting, MediaConvert defaults to Alternate audio, auto select, default. When there is more than one variant in your output group, you must explicitly choose a value for this setting. |
| c2paManifest | [CmfcC2paManifest](#presets-model-cmfcc2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| descriptiveVideoServiceFlag | [CmfcDescriptiveVideoServiceFlag](#presets-model-cmfcdescriptivevideoserviceflag) | False | Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation. |
| iFrameOnlyManifest | [CmfcIFrameOnlyManifest](#presets-model-cmfciframeonlymanifest) | False | Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you don't need the I-frame only child manifest, keep the default value Exclude. |
| klvMetadata | [CmfcKlvMetadata](#presets-model-cmfcklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| manifestMetadataSignaling | [CmfcManifestMetadataSignaling](#presets-model-cmfcmanifestmetadatasignaling) | False | To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough. |
| scte35Esam | [CmfcScte35Esam](#presets-model-cmfcscte35esam) | False | Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Source | [CmfcScte35Source](#presets-model-cmfcscte35source) | False | Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |
| timedMetadata | [CmfcTimedMetadata](#presets-model-cmfctimedmetadata) | False | To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank. |
| timedMetadataBoxVersion | [CmfcTimedMetadataBoxVersion](#presets-model-cmfctimedmetadataboxversion) | False | Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough. |
| timedMetadataSchemeIdUri | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: https://aomedia.org/emsg/ID3 When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough. |
| timedMetadataValue | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough. |

### CmfcTimedMetadata
<a name="presets-model-cmfctimedmetadata"></a>

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### CmfcTimedMetadataBoxVersion
<a name="presets-model-cmfctimedmetadataboxversion"></a>

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.
+ `VERSION_0`
+ `VERSION_1`

### ColorCorrector
<a name="presets-model-colorcorrector"></a>

Settings for color correction.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brightness | integer<br />Minimum: 1<br />Maximum: 100 | False | Brightness level. |
| clipLimits | [ClipLimits](#presets-model-cliplimits) | False | Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip. |
| colorSpaceConversion | [ColorSpaceConversion](#presets-model-colorspaceconversion) | False | Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesn't upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709 |
| contrast | integer<br />Minimum: 1<br />Maximum: 100 | False | Contrast level. |
| hdr10Metadata | [Hdr10Metadata](#presets-model-hdr10metadata) | False | Use these settings when you convert to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering Display Color Volume static metadata that you want signaled in the output. These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator. When you set Color space conversion to HDR 10, these settings are required. You must set values for Max frame average light level and Max content light level; these settings don't have a default value. The default values for the other HDR 10 metadata settings are defined by the P3D65 color space. For more information about MediaConvert HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. |
| hdrToSdrToneMapper | [HDRToSDRToneMapper](#presets-model-hdrtosdrtonemapper) | False | Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR. |
| hue | integer<br />Minimum: -180<br />Maximum: 180 | False | Hue in degrees. |
| maxLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits. |
| sampleRangeConversion | [SampleRangeConversion](#presets-model-samplerangeconversion) | False | Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output. |
| saturation | integer<br />Minimum: 1<br />Maximum: 100 | False | Saturation level. |
| sdrReferenceWhiteLevel | integer<br />Minimum: 100<br />Maximum: 1000 | False | Specify the reference white level, in nits, for all of your SDR inputs. Use to correct brightness levels within HDR10 outputs. The following color metadata must be present in your SDR input: color primaries, transfer characteristics, and matrix coefficients. If your SDR input has missing color metadata, or if you want to correct input color metadata, manually specify a color space in the input video selector. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000. |

### ColorMetadata
<a name="presets-model-colormetadata"></a>

Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default.
+ `IGNORE`
+ `INSERT`

### ColorSpaceConversion
<a name="presets-model-colorspaceconversion"></a>

Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesn't upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709
+ `NONE`
+ `FORCE_601`
+ `FORCE_709`
+ `FORCE_HDR10`
+ `FORCE_HLG_2020`
+ `FORCE_P3DCI`
+ `FORCE_P3D65_SDR`
+ `FORCE_P3D65_HDR`

### ContainerSettings
<a name="presets-model-containersettings"></a>

Container specific settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cmfcSettings | [CmfcSettings](#presets-model-cmfcsettings) | False | These settings relate to the fragmented MP4 container for the segments in your CMAF outputs. |
| container | [ContainerType](#presets-model-containertype) | False | Container for this output. Some containers require a container settings object. If not specified, the default object will be created. |
| f4vSettings | [F4vSettings](#presets-model-f4vsettings) | False | Settings for F4v container |
| m2tsSettings | [M2tsSettings](#presets-model-m2tssettings) | False | MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset. |
| m3u8Settings | [M3u8Settings](#presets-model-m3u8settings) | False | These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs. |
| movSettings | [MovSettings](#presets-model-movsettings) | False | These settings relate to your QuickTime MOV output container. |
| mp4Settings | [Mp4Settings](#presets-model-mp4settings) | False | These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html\#output-codecs-and-containers-supported-for-audio-only. |
| mpdSettings | [MpdSettings](#presets-model-mpdsettings) | False | These settings relate to the fragmented MP4 container for the segments in your DASH outputs. |
| mxfSettings | [MxfSettings](#presets-model-mxfsettings) | False | These settings relate to your MXF output container. |

### ContainerType
<a name="presets-model-containertype"></a>

Container for this output. Some containers require a container settings object. If not specified, the default object will be created.
+ `F4V`
+ `GIF`
+ `ISMV`
+ `M2TS`
+ `M3U8`
+ `CMFC`
+ `MOV`
+ `MP4`
+ `MPD`
+ `MXF`
+ `OGG`
+ `WEBM`
+ `RAW`
+ `Y4M`

### CreatePresetRequest
<a name="presets-model-createpresetrequest"></a>

Send your create preset request with the name of the preset and the JSON for the output settings specified by the preset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| category | string | False | Optional. A category for the preset you are creating. |
| description | string | False | Optional. A description of the preset you are creating. |
| name | string | True | The name of the preset you are creating. |
| settings | [PresetSettings](#presets-model-presetsettings) | True | Settings for preset |
| tags | object | False | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. |

### CreatePresetResponse
<a name="presets-model-createpresetresponse"></a>

Successful create preset requests will return the preset JSON.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| preset | [Preset](#presets-model-preset) | False | A preset is a collection of preconfigured media conversion settings that you want MediaConvert to apply to the output during the conversion process. |

### DeinterlaceAlgorithm
<a name="presets-model-deinterlacealgorithm"></a>

Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output.
+ `INTERPOLATE`
+ `INTERPOLATE_TICKER`
+ `BLEND`
+ `BLEND_TICKER`
+ `LINEAR_INTERPOLATION`

### Deinterlacer
<a name="presets-model-deinterlacer"></a>

Settings for deinterlacer

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [DeinterlaceAlgorithm](#presets-model-deinterlacealgorithm) | False | Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output. |
| control | [DeinterlacerControl](#presets-model-deinterlacercontrol) | False | - When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE\_ALL\_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video. |
| mode | [DeinterlacerMode](#presets-model-deinterlacermode) | False | Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive. |

### DeinterlacerControl
<a name="presets-model-deinterlacercontrol"></a>

- When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE\_ALL\_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.
+ `FORCE_ALL_FRAMES`
+ `NORMAL`

### DeinterlacerMode
<a name="presets-model-deinterlacermode"></a>

Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.
+ `DEINTERLACE`
+ `INVERSE_TELECINE`
+ `ADAPTIVE`

### DolbyVision
<a name="presets-model-dolbyvision"></a>

Create Dolby Vision Profile 5 or Profile 8.1 compatible video output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| compatibility | [DolbyVisionCompatibility](#presets-model-dolbyvisioncompatibility) | False | When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL\_CODECS property. |
| l6Metadata | [DolbyVisionLevel6Metadata](#presets-model-dolbyvisionlevel6metadata) | False | Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values. |
| l6Mode | [DolbyVisionLevel6Mode](#presets-model-dolbyvisionlevel6mode) | False | Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies. |
| mapping | [DolbyVisionMapping](#presets-model-dolbyvisionmapping) | False | Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims. |
| profile | [DolbyVisionProfile](#presets-model-dolbyvisionprofile) | False | Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata. |

### DolbyVisionCompatibility
<a name="presets-model-dolbyvisioncompatibility"></a>

When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL\_CODECS property.
+ `DUPLICATE_STREAM`
+ `SUPPLEMENTAL_CODECS`

### DolbyVisionLevel6Metadata
<a name="presets-model-dolbyvisionlevel6metadata"></a>

Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxCll | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum Content Light Level. Static HDR metadata that corresponds to the brightest pixel in the entire stream. Measured in nits. |
| maxFall | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum Frame-Average Light Level. Static HDR metadata that corresponds to the highest frame-average brightness in the entire stream. Measured in nits. |

### DolbyVisionLevel6Mode
<a name="presets-model-dolbyvisionlevel6mode"></a>

Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies.
+ `PASSTHROUGH`
+ `RECALCULATE`
+ `SPECIFY`

### DolbyVisionMapping
<a name="presets-model-dolbyvisionmapping"></a>

Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims.
+ `HDR10_NOMAP`
+ `HDR10_1000`

### DolbyVisionProfile
<a name="presets-model-dolbyvisionprofile"></a>

Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata.
+ `PROFILE_5`
+ `PROFILE_8_1`

### DropFrameTimecode
<a name="presets-model-dropframetimecode"></a>

Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled.
+ `DISABLED`
+ `ENABLED`

### DvbNitSettings
<a name="presets-model-dvbnitsettings"></a>

Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The numeric value placed in the Network Information Table (NIT). |
| networkName | string<br />MinLength: 1<br />MaxLength: 256 | False | The network name text placed in the network\_name\_descriptor inside the Network Information Table. Maximum length is 256 characters. |
| nitInterval | integer<br />Minimum: 25<br />Maximum: 10000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbSdtSettings
<a name="presets-model-dvbsdtsettings"></a>

Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputSdt | [OutputSdt](#presets-model-outputsdt) | False | Selects method of inserting SDT information into output stream. "Follow input SDT" copies SDT information from input stream to output stream. "Follow input SDT if present" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter "SDT Manually" means user will enter the SDT information. "No SDT" means output stream will not contain SDT information. |
| sdtInterval | integer<br />Minimum: 25<br />Maximum: 2000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| serviceName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service name placed in the service\_descriptor in the Service Description Table. Maximum length is 256 characters. |
| serviceProviderName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service provider name placed in the service\_descriptor in the Service Description Table. Maximum length is 256 characters. |

### DvbSubDestinationSettings
<a name="presets-model-dvbsubdestinationsettings"></a>

Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [DvbSubtitleAlignment](#presets-model-dvbsubtitlealignment) | False | Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical. |
| applyFontColor | [DvbSubtitleApplyFontColor](#presets-model-dvbsubtitleapplyfontcolor) | False | Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text. |
| backgroundColor | [DvbSubtitleBackgroundColor](#presets-model-dvbsubtitlebackgroundcolor) | False | Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| ddsHandling | [DvbddsHandling](#presets-model-dvbddshandling) | False | Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn't include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match. To include the DDS, with optimized subtitle placement and reduced data overhead: We recommend that you choose Specified (optimal). This option provides the same visual positioning as Specified while using less bandwidth. This also supports resolutions higher than 1080p while maintaining full DVB-Sub compatibility. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. |
| ddsXCoordinate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Use this setting, along with DDS y-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the left side of the frame and the left side of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment. All burn-in and DVB-Sub font settings must match. |
| ddsYCoordinate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Use this setting, along with DDS x-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the top of the frame and the top of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment (PCS). All burn-in and DVB-Sub font settings must match. |
| fallbackFont | [DvbSubSubtitleFallbackFont](#presets-model-dvbsubsubtitlefallbackfont) | False | Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input. |
| fontColor | [DvbSubtitleFontColor](#presets-model-dvbsubtitlefontcolor) | False | Specify the color of the captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontFileBold | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file. |
| fontFileBoldItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file. |
| fontFileItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file. |
| fontFileRegular | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Specify the Font resolution in DPI (dots per inch). Within your job settings, all of your DVB-Sub settings must be identical. |
| fontScript | [FontScript](#presets-model-fontscript) | False | Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontSize | integer<br />Minimum: 0<br />Maximum: 96 | False | Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size. Within your job settings, all of your DVB-Sub settings must be identical. |
| height | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the height, in pixels, of this set of DVB-Sub captions. The default value is 576 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match. |
| hexFontColor | string<br />Pattern: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`<br />MinLength: 6<br />MaxLength: 8 | False | Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB. |
| outlineColor | [DvbSubtitleOutlineColor](#presets-model-dvbsubtitleoutlinecolor) | False | Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowColor | [DvbSubtitleShadowColor](#presets-model-dvbsubtitleshadowcolor) | False | Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowXOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowYOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| stylePassthrough | [DvbSubtitleStylePassthrough](#presets-model-dvbsubtitlestylepassthrough) | False | To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files. |
| subtitlingType | [DvbSubtitlingType](#presets-model-dvbsubtitlingtype) | False | Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue. |
| teletextSpacing | [DvbSubtitleTeletextSpacing](#presets-model-dvbsubtitleteletextspacing) | False | Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| width | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the width, in pixels, of this set of DVB-Sub captions. The default value is 720 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match. |
| xPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x\_position is provided, the horizontal caption position will be determined by the alignment parameter. Within your job settings, all of your DVB-Sub settings must be identical. |
| yPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y\_position is provided, the caption will be positioned towards the bottom of the output. Within your job settings, all of your DVB-Sub settings must be identical. |

### DvbSubSubtitleFallbackFont
<a name="presets-model-dvbsubsubtitlefallbackfont"></a>

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.
+ `BEST_MATCH`
+ `MONOSPACED_SANSSERIF`
+ `MONOSPACED_SERIF`
+ `PROPORTIONAL_SANSSERIF`
+ `PROPORTIONAL_SERIF`

### DvbSubtitleAlignment
<a name="presets-model-dvbsubtitlealignment"></a>

Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical.
+ `CENTERED`
+ `LEFT`
+ `AUTO`

### DvbSubtitleApplyFontColor
<a name="presets-model-dvbsubtitleapplyfontcolor"></a>

Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text.
+ `WHITE_TEXT_ONLY`
+ `ALL_TEXT`

### DvbSubtitleBackgroundColor
<a name="presets-model-dvbsubtitlebackgroundcolor"></a>

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### DvbSubtitleFontColor
<a name="presets-model-dvbsubtitlefontcolor"></a>

Specify the color of the captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.
+ `WHITE`
+ `BLACK`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `HEX`
+ `AUTO`

### DvbSubtitleOutlineColor
<a name="presets-model-dvbsubtitleoutlinecolor"></a>

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.
+ `BLACK`
+ `WHITE`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `AUTO`

### DvbSubtitleShadowColor
<a name="presets-model-dvbsubtitleshadowcolor"></a>

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### DvbSubtitleStylePassthrough
<a name="presets-model-dvbsubtitlestylepassthrough"></a>

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.
+ `ENABLED`
+ `DISABLED`

### DvbSubtitleTeletextSpacing
<a name="presets-model-dvbsubtitleteletextspacing"></a>

Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical.
+ `FIXED_GRID`
+ `PROPORTIONAL`
+ `AUTO`

### DvbSubtitlingType
<a name="presets-model-dvbsubtitlingtype"></a>

Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue.
+ `HEARING_IMPAIRED`
+ `STANDARD`

### DvbTdtSettings
<a name="presets-model-dvbtdtsettings"></a>

Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tdtInterval | integer<br />Minimum: 1000<br />Maximum: 30000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbddsHandling
<a name="presets-model-dvbddshandling"></a>

Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn't include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match. To include the DDS, with optimized subtitle placement and reduced data overhead: We recommend that you choose Specified (optimal). This option provides the same visual positioning as Specified while using less bandwidth. This also supports resolutions higher than 1080p while maintaining full DVB-Sub compatibility. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate.
+ `NONE`
+ `SPECIFIED`
+ `NO_DISPLAY_WINDOW`
+ `SPECIFIED_OPTIMAL`

### Eac3AtmosBitstreamMode
<a name="presets-model-eac3atmosbitstreammode"></a>

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).
+ `COMPLETE_MAIN`

### Eac3AtmosCodingMode
<a name="presets-model-eac3atmoscodingmode"></a>

The coding mode for Dolby Digital Plus JOC (Atmos).
+ `CODING_MODE_AUTO`
+ `CODING_MODE_5_1_4`
+ `CODING_MODE_7_1_4`
+ `CODING_MODE_9_1_6`

### Eac3AtmosDialogueIntelligence
<a name="presets-model-eac3atmosdialogueintelligence"></a>

Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis.
+ `ENABLED`
+ `DISABLED`

### Eac3AtmosDownmixControl
<a name="presets-model-eac3atmosdownmixcontrol"></a>

Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings.
+ `SPECIFIED`
+ `INITIALIZE_FROM_SOURCE`

### Eac3AtmosDynamicRangeCompressionLine
<a name="presets-model-eac3atmosdynamicrangecompressionline"></a>

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3AtmosDynamicRangeCompressionRf
<a name="presets-model-eac3atmosdynamicrangecompressionrf"></a>

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3AtmosDynamicRangeControl
<a name="presets-model-eac3atmosdynamicrangecontrol"></a>

Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings.
+ `SPECIFIED`
+ `INITIALIZE_FROM_SOURCE`

### Eac3AtmosMeteringMode
<a name="presets-model-eac3atmosmeteringmode"></a>

Choose how the service meters the loudness of your audio.
+ `LEQ_A`
+ `ITU_BS_1770_1`
+ `ITU_BS_1770_2`
+ `ITU_BS_1770_3`
+ `ITU_BS_1770_4`

### Eac3AtmosSettings
<a name="presets-model-eac3atmossettings"></a>

Required when you set Codec to the value EAC3\_ATMOS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 384000<br />Maximum: 1024000 | False | Specify the average bitrate for this output in bits per second. Valid values: 384k, 448k, 576k, 640k, 768k, 1024k Default value: 448k Note that MediaConvert supports 384k only with channel-based immersive (CBI) 7.1.4 and 5.1.4 inputs. For CBI 9.1.6 and other input types, MediaConvert automatically increases your output bitrate to 448k. |
| bitstreamMode | [Eac3AtmosBitstreamMode](#presets-model-eac3atmosbitstreammode) | False | Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Eac3AtmosCodingMode](#presets-model-eac3atmoscodingmode) | False | The coding mode for Dolby Digital Plus JOC (Atmos). |
| dialogueIntelligence | [Eac3AtmosDialogueIntelligence](#presets-model-eac3atmosdialogueintelligence) | False | Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis. |
| downmixControl | [Eac3AtmosDownmixControl](#presets-model-eac3atmosdownmixcontrol) | False | Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings. |
| dynamicRangeCompressionLine | [Eac3AtmosDynamicRangeCompressionLine](#presets-model-eac3atmosdynamicrangecompressionline) | False | Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionRf | [Eac3AtmosDynamicRangeCompressionRf](#presets-model-eac3atmosdynamicrangecompressionrf) | False | Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeControl | [Eac3AtmosDynamicRangeControl](#presets-model-eac3atmosdynamicrangecontrol) | False | Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -6.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Atmos setting: Left only/Right only center mix (Lo/Ro center). MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Atmos setting: Left only/Right only. MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -6.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Atmos setting: Left total/Right total center mix (Lt/Rt center). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Atmos setting: Left total/Right total surround mix (Lt/Rt surround). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, the service ignores Left total/Right total surround. |
| meteringMode | [Eac3AtmosMeteringMode](#presets-model-eac3atmosmeteringmode) | False | Choose how the service meters the loudness of your audio. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| speechThreshold | integer<br />Minimum: 0<br />Maximum: 100 | False | Specify the percentage of audio content, from 0% to 100%, that must be speech in order for the encoder to use the measured speech loudness as the overall program loudness. Default value: 15% |
| stereoDownmix | [Eac3AtmosStereoDownmix](#presets-model-eac3atmosstereodownmix) | False | Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix. |
| surroundExMode | [Eac3AtmosSurroundExMode](#presets-model-eac3atmossurroundexmode) | False | Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels. |

### Eac3AtmosStereoDownmix
<a name="presets-model-eac3atmosstereodownmix"></a>

Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix.
+ `NOT_INDICATED`
+ `STEREO`
+ `SURROUND`
+ `DPL2`

### Eac3AtmosSurroundExMode
<a name="presets-model-eac3atmossurroundexmode"></a>

Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### Eac3AttenuationControl
<a name="presets-model-eac3attenuationcontrol"></a>

If set to ATTENUATE\_3\_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
+ `ATTENUATE_3_DB`
+ `NONE`

### Eac3BitstreamMode
<a name="presets-model-eac3bitstreammode"></a>

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).
+ `COMPLETE_MAIN`
+ `COMMENTARY`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `VISUALLY_IMPAIRED`

### Eac3CodingMode
<a name="presets-model-eac3codingmode"></a>

Dolby Digital Plus coding mode. Determines number of channels.
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2`
+ `CODING_MODE_AUTO`

### Eac3DcFilter
<a name="presets-model-eac3dcfilter"></a>

Activates a DC highpass filter for all input channels.
+ `ENABLED`
+ `DISABLED`

### Eac3DynamicRangeCompressionLine
<a name="presets-model-eac3dynamicrangecompressionline"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3DynamicRangeCompressionRf
<a name="presets-model-eac3dynamicrangecompressionrf"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3LfeControl
<a name="presets-model-eac3lfecontrol"></a>

When encoding 3/2 audio, controls whether the LFE channel is enabled
+ `LFE`
+ `NO_LFE`

### Eac3LfeFilter
<a name="presets-model-eac3lfefilter"></a>

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode.
+ `ENABLED`
+ `DISABLED`

### Eac3MetadataControl
<a name="presets-model-eac3metadatacontrol"></a>

When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Eac3PassthroughControl
<a name="presets-model-eac3passthroughcontrol"></a>

When set to WHEN\_POSSIBLE, input DD\+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding.
+ `WHEN_POSSIBLE`
+ `NO_PASSTHROUGH`

### Eac3PhaseControl
<a name="presets-model-eac3phasecontrol"></a>

Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.
+ `SHIFT_90_DEGREES`
+ `NO_SHIFT`

### Eac3Settings
<a name="presets-model-eac3settings"></a>

Required when you set Codec to the value EAC3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attenuationControl | [Eac3AttenuationControl](#presets-model-eac3attenuationcontrol) | False | If set to ATTENUATE\_3\_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode. |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 3024000 | False | Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 32000. Maximum: 3024000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 96000. Maximum: 3024000. Valid bitrates for coding mode 3/2: Default: 384000. Minimum: 192000. Maximum: 3024000. |
| bitstreamMode | [Eac3BitstreamMode](#presets-model-eac3bitstreammode) | False | Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Eac3CodingMode](#presets-model-eac3codingmode) | False | Dolby Digital Plus coding mode. Determines number of channels. |
| dcFilter | [Eac3DcFilter](#presets-model-eac3dcfilter) | False | Activates a DC highpass filter for all input channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through. |
| dynamicRangeCompressionLine | [Eac3DynamicRangeCompressionLine](#presets-model-eac3dynamicrangecompressionline) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionRf | [Eac3DynamicRangeCompressionRf](#presets-model-eac3dynamicrangecompressionrf) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| lfeControl | [Eac3LfeControl](#presets-model-eac3lfecontrol) | False | When encoding 3/2 audio, controls whether the LFE channel is enabled |
| lfeFilter | [Eac3LfeFilter](#presets-model-eac3lfefilter) | False | Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Digital Plus setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Digital Plus setting: Left only/Right only. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Digital Plus setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Digital Plus setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround. |
| metadataControl | [Eac3MetadataControl](#presets-model-eac3metadatacontrol) | False | When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| passthroughControl | [Eac3PassthroughControl](#presets-model-eac3passthroughcontrol) | False | When set to WHEN\_POSSIBLE, input DD\+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding. |
| phaseControl | [Eac3PhaseControl](#presets-model-eac3phasecontrol) | False | Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| stereoDownmix | [Eac3StereoDownmix](#presets-model-eac3stereodownmix) | False | Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix. |
| surroundExMode | [Eac3SurroundExMode](#presets-model-eac3surroundexmode) | False | When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels. |
| surroundMode | [Eac3SurroundMode](#presets-model-eac3surroundmode) | False | When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels. |

### Eac3StereoDownmix
<a name="presets-model-eac3stereodownmix"></a>

Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix.
+ `NOT_INDICATED`
+ `LO_RO`
+ `LT_RT`
+ `DPL2`

### Eac3SurroundExMode
<a name="presets-model-eac3surroundexmode"></a>

When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### Eac3SurroundMode
<a name="presets-model-eac3surroundmode"></a>

When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### EmbeddedDestinationSettings
<a name="presets-model-embeddeddestinationsettings"></a>

Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Ignore this setting unless your input captions are SCC format and your output captions are embedded in the video stream. Specify a CC number for each captions channel in this output. If you have two channels, choose CC numbers that aren't in the same field. For example, choose 1 and 3. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded. |
| destination708ServiceNumber | integer<br />Minimum: 1<br />Maximum: 6 | False | Ignore this setting unless your input captions are SCC format and you want both 608 and 708 captions embedded in your output stream. Optionally, specify the 708 service number for each output captions channel. Choose a different number for each channel. To use this setting, also set Force 608 to 708 upconvert to Upconvert in your input captions selector settings. If you choose to upconvert but don't specify a 708 service number, MediaConvert uses the number that you specify for CC channel number for the 708 service number. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded. |

### ExceptionBody
<a name="presets-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### F4vMoovPlacement
<a name="presets-model-f4vmoovplacement"></a>

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.
+ `PROGRESSIVE_DOWNLOAD`
+ `NORMAL`

### F4vSettings
<a name="presets-model-f4vsettings"></a>

Settings for F4v container

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| moovPlacement | [F4vMoovPlacement](#presets-model-f4vmoovplacement) | False | To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal. |

### FlacSettings
<a name="presets-model-flacsettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 8 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 8. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and 8. |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 192000 | False | Sample rate in Hz. |

### FontScript
<a name="presets-model-fontscript"></a>

Provide the font script, using an ISO 15924 script code, if the LanguageCode is not sufficient for determining the script type. Where LanguageCode or CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
+ `AUTOMATIC`
+ `HANS`
+ `HANT`

### FrameCaptureSettings
<a name="presets-model-framecapturesettings"></a>

Required when you set Codec to the value FRAME\_CAPTURE.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places. |
| maxCaptures | integer<br />Minimum: 1<br />Maximum: 10000000 | False | Maximum number of captures (encoded jpg output files). |
| quality | integer<br />Minimum: 1<br />Maximum: 100 | False | JPEG Quality - a higher value equals higher quality. |

### FrameControl
<a name="presets-model-framecontrol"></a>

Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players.
+ `NEAREST_IDRFRAME`
+ `NEAREST_IFRAME`

### GifFramerateControl
<a name="presets-model-gifframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE\_FROM\_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### GifFramerateConversionAlgorithm
<a name="presets-model-gifframerateconversionalgorithm"></a>

Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE\_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`

### GifSettings
<a name="presets-model-gifsettings"></a>

Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateControl | [GifFramerateControl](#presets-model-gifframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE\_FROM\_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator. |
| framerateConversionAlgorithm | [GifFramerateConversionAlgorithm](#presets-model-gifframerateconversionalgorithm) | False | Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE\_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |

### H264AdaptiveQuantization
<a name="presets-model-h264adaptivequantization"></a>

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization.
+ `OFF`
+ `AUTO`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### H264CodecLevel
<a name="presets-model-h264codeclevel"></a>

Specify an H.264 level that is consistent with your output video settings. If you aren't sure what level to specify, choose Auto.
+ `AUTO`
+ `LEVEL_1`
+ `LEVEL_1_1`
+ `LEVEL_1_2`
+ `LEVEL_1_3`
+ `LEVEL_2`
+ `LEVEL_2_1`
+ `LEVEL_2_2`
+ `LEVEL_3`
+ `LEVEL_3_1`
+ `LEVEL_3_2`
+ `LEVEL_4`
+ `LEVEL_4_1`
+ `LEVEL_4_2`
+ `LEVEL_5`
+ `LEVEL_5_1`
+ `LEVEL_5_2`

### H264CodecProfile
<a name="presets-model-h264codecprofile"></a>

H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.
+ `BASELINE`
+ `HIGH`
+ `HIGH_10BIT`
+ `HIGH_422`
+ `HIGH_422_10BIT`
+ `MAIN`

### H264DynamicSubGop
<a name="presets-model-h264dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### H264EndOfStreamMarkers
<a name="presets-model-h264endofstreammarkers"></a>

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.
+ `INCLUDE`
+ `SUPPRESS`

### H264EntropyEncoding
<a name="presets-model-h264entropyencoding"></a>

Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
+ `CABAC`
+ `CAVLC`

### H264FieldEncoding
<a name="presets-model-h264fieldencoding"></a>

The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs.
+ `PAFF`
+ `FORCE_FIELD`
+ `MBAFF`

### H264FlickerAdaptiveQuantization
<a name="presets-model-h264flickeradaptivequantization"></a>

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264FramerateControl
<a name="presets-model-h264frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264FramerateConversionAlgorithm
<a name="presets-model-h264framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### H264GopBReference
<a name="presets-model-h264gopbreference"></a>

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.
+ `DISABLED`
+ `ENABLED`

### H264GopSizeUnits
<a name="presets-model-h264gopsizeunits"></a>

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.
+ `FRAMES`
+ `SECONDS`
+ `AUTO`

### H264InterlaceMode
<a name="presets-model-h264interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### H264ParControl
<a name="presets-model-h264parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264QualityTuningLevel
<a name="presets-model-h264qualitytuninglevel"></a>

The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### H264QvbrSettings
<a name="presets-model-h264qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the H.264 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxAverageBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### H264RateControlMode
<a name="presets-model-h264ratecontrolmode"></a>

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
+ `VBR`
+ `CBR`
+ `QVBR`

### H264RepeatPps
<a name="presets-model-h264repeatpps"></a>

Places a PPS header on each encoded picture, even if repeated.
+ `DISABLED`
+ `ENABLED`

### H264SaliencyAwareEncoding
<a name="presets-model-h264saliencyawareencoding"></a>

Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled.
+ `DISABLED`
+ `PREFERRED`

### H264ScanTypeConversionMode
<a name="presets-model-h264scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### H264SceneChangeDetect
<a name="presets-model-h264scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.
+ `DISABLED`
+ `ENABLED`
+ `TRANSITION_DETECTION`

### H264Settings
<a name="presets-model-h264settings"></a>

Required when you set Codec to the value H\_264.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H264AdaptiveQuantization](#presets-model-h264adaptivequantization) | False | Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization. |
| bandwidthReductionFilter | [BandwidthReductionFilter](#presets-model-bandwidthreductionfilter) | False | The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [H264CodecLevel](#presets-model-h264codeclevel) | False | Specify an H.264 level that is consistent with your output video settings. If you aren't sure what level to specify, choose Auto. |
| codecProfile | [H264CodecProfile](#presets-model-h264codecprofile) | False | H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License. |
| dynamicSubGop | [H264DynamicSubGop](#presets-model-h264dynamicsubgop) | False | Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static. |
| endOfStreamMarkers | [H264EndOfStreamMarkers](#presets-model-h264endofstreammarkers) | False | Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream. |
| entropyEncoding | [H264EntropyEncoding](#presets-model-h264entropyencoding) | False | Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC. |
| fieldEncoding | [H264FieldEncoding](#presets-model-h264fieldencoding) | False | The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs. |
| flickerAdaptiveQuantization | [H264FlickerAdaptiveQuantization](#presets-model-h264flickeradaptivequantization) | False | Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| framerateControl | [H264FramerateControl](#presets-model-h264frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [H264FramerateConversionAlgorithm](#presets-model-h264framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopBReference | [H264GopBReference](#presets-model-h264gopbreference) | False | Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. In the console, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group. |
| gopSizeUnits | [H264GopSizeUnits](#presets-model-h264gopsizeunits) | False | Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [H264InterlaceMode](#presets-model-h264interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7. |
| numberReferenceFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H264ParControl](#presets-model-h264parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [H264QualityTuningLevel](#presets-model-h264qualitytuninglevel) | False | The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing. |
| qvbrSettings | [H264QvbrSettings](#presets-model-h264qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [H264RateControlMode](#presets-model-h264ratecontrolmode) | False | Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR). |
| repeatPps | [H264RepeatPps](#presets-model-h264repeatpps) | False | Places a PPS header on each encoded picture, even if repeated. |
| saliencyAwareEncoding | [H264SaliencyAwareEncoding](#presets-model-h264saliencyawareencoding) | False | Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled. |
| scanTypeConversionMode | [H264ScanTypeConversionMode](#presets-model-h264scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [H264SceneChangeDetect](#presets-model-h264scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| slowPal | [H264SlowPal](#presets-model-h264slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless you need to comply with a specification that requires a specific value. If you don't have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [H264SpatialAdaptiveQuantization](#presets-model-h264spatialadaptivequantization) | False | Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| syntax | [H264Syntax](#presets-model-h264syntax) | False | Produces a bitstream compliant with SMPTE RP-2027. |
| telecine | [H264Telecine](#presets-model-h264telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| temporalAdaptiveQuantization | [H264TemporalAdaptiveQuantization](#presets-model-h264temporaladaptivequantization) | False | Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| unregisteredSeiTimecode | [H264UnregisteredSeiTimecode](#presets-model-h264unregisteredseitimecode) | False | Inserts timecode for each frame as 4 bytes of an unregistered SEI message. |
| writeMp4PackagingType | [H264WriteMp4PackagingType](#presets-model-h264writemp4packagingtype) | False | Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players. |

### H264SlowPal
<a name="presets-model-h264slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### H264SpatialAdaptiveQuantization
<a name="presets-model-h264spatialadaptivequantization"></a>

Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264Syntax
<a name="presets-model-h264syntax"></a>

Produces a bitstream compliant with SMPTE RP-2027.
+ `DEFAULT`
+ `RP2027`

### H264Telecine
<a name="presets-model-h264telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `SOFT`
+ `HARD`

### H264TemporalAdaptiveQuantization
<a name="presets-model-h264temporaladaptivequantization"></a>

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264UnregisteredSeiTimecode
<a name="presets-model-h264unregisteredseitimecode"></a>

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
+ `DISABLED`
+ `ENABLED`

### H264WriteMp4PackagingType
<a name="presets-model-h264writemp4packagingtype"></a>

Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players.
+ `AVC1`
+ `AVC3`

### H265AdaptiveQuantization
<a name="presets-model-h265adaptivequantization"></a>

When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`
+ `AUTO`

### H265AlternateTransferFunctionSei
<a name="presets-model-h265alternatetransferfunctionsei"></a>

Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
+ `DISABLED`
+ `ENABLED`

### H265CodecLevel
<a name="presets-model-h265codeclevel"></a>

H.265 Level.
+ `AUTO`
+ `LEVEL_1`
+ `LEVEL_2`
+ `LEVEL_2_1`
+ `LEVEL_3`
+ `LEVEL_3_1`
+ `LEVEL_4`
+ `LEVEL_4_1`
+ `LEVEL_5`
+ `LEVEL_5_1`
+ `LEVEL_5_2`
+ `LEVEL_6`
+ `LEVEL_6_1`
+ `LEVEL_6_2`

### H265CodecProfile
<a name="presets-model-h265codecprofile"></a>

Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.
+ `MAIN_MAIN`
+ `MAIN_HIGH`
+ `MAIN10_MAIN`
+ `MAIN10_HIGH`
+ `MAIN_422_8BIT_MAIN`
+ `MAIN_422_8BIT_HIGH`
+ `MAIN_422_10BIT_MAIN`
+ `MAIN_422_10BIT_HIGH`

### H265Deblocking
<a name="presets-model-h265deblocking"></a>

Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates.
+ `ENABLED`
+ `DISABLED`

### H265DynamicSubGop
<a name="presets-model-h265dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### H265EndOfStreamMarkers
<a name="presets-model-h265endofstreammarkers"></a>

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.
+ `INCLUDE`
+ `SUPPRESS`

### H265FlickerAdaptiveQuantization
<a name="presets-model-h265flickeradaptivequantization"></a>

Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off.
+ `DISABLED`
+ `ENABLED`

### H265FramerateControl
<a name="presets-model-h265frameratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H265FramerateConversionAlgorithm
<a name="presets-model-h265framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### H265GopBReference
<a name="presets-model-h265gopbreference"></a>

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.
+ `DISABLED`
+ `ENABLED`

### H265GopSizeUnits
<a name="presets-model-h265gopsizeunits"></a>

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.
+ `FRAMES`
+ `SECONDS`
+ `AUTO`

### H265InterlaceMode
<a name="presets-model-h265interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### H265MvOverPictureBoundaries
<a name="presets-model-h265mvoverpictureboundaries"></a>

If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled".
+ `ENABLED`
+ `DISABLED`

### H265MvTemporalPredictor
<a name="presets-model-h265mvtemporalpredictor"></a>

If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled".
+ `ENABLED`
+ `DISABLED`

### H265ParControl
<a name="presets-model-h265parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H265QualityTuningLevel
<a name="presets-model-h265qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### H265QvbrSettings
<a name="presets-model-h265qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxAverageBitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### H265RateControlMode
<a name="presets-model-h265ratecontrolmode"></a>

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
+ `VBR`
+ `CBR`
+ `QVBR`

### H265SampleAdaptiveOffsetFilterMode
<a name="presets-model-h265sampleadaptiveoffsetfiltermode"></a>

Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content
+ `DEFAULT`
+ `ADAPTIVE`
+ `OFF`

### H265ScanTypeConversionMode
<a name="presets-model-h265scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### H265SceneChangeDetect
<a name="presets-model-h265scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.
+ `DISABLED`
+ `ENABLED`
+ `TRANSITION_DETECTION`

### H265Settings
<a name="presets-model-h265settings"></a>

Settings for H265 codec

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H265AdaptiveQuantization](#presets-model-h265adaptivequantization) | False | When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output. |
| alternateTransferFunctionSei | [H265AlternateTransferFunctionSei](#presets-model-h265alternatetransferfunctionsei) | False | Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF). |
| bandwidthReductionFilter | [BandwidthReductionFilter](#presets-model-bandwidthreductionfilter) | False | The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [H265CodecLevel](#presets-model-h265codeclevel) | False | H.265 Level. |
| codecProfile | [H265CodecProfile](#presets-model-h265codecprofile) | False | Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License. |
| deblocking | [H265Deblocking](#presets-model-h265deblocking) | False | Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates. |
| dynamicSubGop | [H265DynamicSubGop](#presets-model-h265dynamicsubgop) | False | Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static. |
| endOfStreamMarkers | [H265EndOfStreamMarkers](#presets-model-h265endofstreammarkers) | False | Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream. |
| flickerAdaptiveQuantization | [H265FlickerAdaptiveQuantization](#presets-model-h265flickeradaptivequantization) | False | Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off. |
| framerateControl | [H265FramerateControl](#presets-model-h265frameratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [H265FramerateConversionAlgorithm](#presets-model-h265framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopBReference | [H265GopBReference](#presets-model-h265gopbreference) | False | Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group. |
| gopSizeUnits | [H265GopSizeUnits](#presets-model-h265gopsizeunits) | False | Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1466400000 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [H265InterlaceMode](#presets-model-h265interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| mvOverPictureBoundaries | [H265MvOverPictureBoundaries](#presets-model-h265mvoverpictureboundaries) | False | If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled". |
| mvTemporalPredictor | [H265MvTemporalPredictor](#presets-model-h265mvtemporalpredictor) | False | If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled". |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7. |
| numberReferenceFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H265ParControl](#presets-model-h265parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [H265QualityTuningLevel](#presets-model-h265qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| qvbrSettings | [H265QvbrSettings](#presets-model-h265qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [H265RateControlMode](#presets-model-h265ratecontrolmode) | False | Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR). |
| sampleAdaptiveOffsetFilterMode | [H265SampleAdaptiveOffsetFilterMode](#presets-model-h265sampleadaptiveoffsetfiltermode) | False | Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content |
| scanTypeConversionMode | [H265ScanTypeConversionMode](#presets-model-h265scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [H265SceneChangeDetect](#presets-model-h265scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| slowPal | [H265SlowPal](#presets-model-h265slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| spatialAdaptiveQuantization | [H265SpatialAdaptiveQuantization](#presets-model-h265spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| telecine | [H265Telecine](#presets-model-h265telecine) | False | This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i. |
| temporalAdaptiveQuantization | [H265TemporalAdaptiveQuantization](#presets-model-h265temporaladaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. |
| temporalIds | [H265TemporalIds](#presets-model-h265temporalids) | False | Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output. |
| tileHeight | integer<br />Minimum: 64<br />Maximum: 2160 | False | Set this field to set up the picture as a tile. You must also set TileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 or less. If the tile width and height are specified, MediaConvert will override the video codec slices field with a value that MediaConvert calculates. |
| tilePadding | [H265TilePadding](#presets-model-h265tilepadding) | False | Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none". |
| tiles | [H265Tiles](#presets-model-h265tiles) | False | Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures. |
| tileWidth | integer<br />Minimum: 256<br />Maximum: 3840 | False | Set this field to set up the picture as a tile. See TileHeight for more information. |
| treeBlockSize | [H265TreeBlockSize](#presets-model-h265treeblocksize) | False | Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto". |
| unregisteredSeiTimecode | [H265UnregisteredSeiTimecode](#presets-model-h265unregisteredseitimecode) | False | Inserts timecode for each frame as 4 bytes of an unregistered SEI message. |
| writeMp4PackagingType | [H265WriteMp4PackagingType](#presets-model-h265writemp4packagingtype) | False | If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples. |

### H265SlowPal
<a name="presets-model-h265slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### H265SpatialAdaptiveQuantization
<a name="presets-model-h265spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### H265Telecine
<a name="presets-model-h265telecine"></a>

This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
+ `NONE`
+ `SOFT`
+ `HARD`

### H265TemporalAdaptiveQuantization
<a name="presets-model-h265temporaladaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### H265TemporalIds
<a name="presets-model-h265temporalids"></a>

Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.
+ `DISABLED`
+ `ENABLED`

### H265TilePadding
<a name="presets-model-h265tilepadding"></a>

Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none".
+ `NONE`
+ `PADDED`

### H265Tiles
<a name="presets-model-h265tiles"></a>

Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.
+ `DISABLED`
+ `ENABLED`

### H265TreeBlockSize
<a name="presets-model-h265treeblocksize"></a>

Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto".
+ `AUTO`
+ `TREE_SIZE_32X32`

### H265UnregisteredSeiTimecode
<a name="presets-model-h265unregisteredseitimecode"></a>

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
+ `DISABLED`
+ `ENABLED`

### H265WriteMp4PackagingType
<a name="presets-model-h265writemp4packagingtype"></a>

If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples.
+ `HVC1`
+ `HEV1`

### HDRToSDRToneMapper
<a name="presets-model-hdrtosdrtonemapper"></a>

Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR.
+ `PRESERVE_DETAILS`
+ `VIBRANT`

### Hdr10Metadata
<a name="presets-model-hdr10metadata"></a>

Use these settings to specify static color calibration metadata, as defined by SMPTE ST 2086. These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bluePrimaryX | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| bluePrimaryY | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| greenPrimaryX | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| greenPrimaryY | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| maxContentLightLevel | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum light level among all samples in the coded video sequence, in units of candelas per square meter. This setting doesn't have a default value; you must specify a value that is suitable for the content. |
| maxFrameAverageLightLevel | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter. This setting doesn't have a default value; you must specify a value that is suitable for the content. |
| maxLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter. |
| minLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter |
| redPrimaryX | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| redPrimaryY | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| whitePointX | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |
| whitePointY | integer<br />Minimum: 0<br />Maximum: 50000 | False | HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction. |

### Hdr10Plus
<a name="presets-model-hdr10plus"></a>

Setting for HDR10\+ metadata insertion

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| masteringMonitorNits | integer<br />Minimum: 0<br />Maximum: 4000 | False | Specify the HDR10\+ mastering display normalized peak luminance, in nits. This is the normalized actual peak luminance of the mastering display, as defined by ST 2094-40. |
| targetMonitorNits | integer<br />Minimum: 0<br />Maximum: 4000 | False | Specify the HDR10\+ target display nominal peak luminance, in nits. This is the nominal maximum luminance of the target display as defined by ST 2094-40. |

### ImageInserter
<a name="presets-model-imageinserter"></a>

Use the image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each input or output individually. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/graphic-overlay.html. This setting is disabled by default.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| insertableImages | Array of type [InsertableImage](#presets-model-insertableimage) | False | Specify the images that you want to overlay on your video. The images must be PNG or TGA files. |
| sdrReferenceWhiteLevel | integer<br />Minimum: 100<br />Maximum: 1000 | False | Specify the reference white level, in nits, for all of your image inserter images. Use to correct brightness levels within HDR10 outputs. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000. |

### ImscAccessibilitySubs
<a name="presets-model-imscaccessibilitysubs"></a>

If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>.
+ `DISABLED`
+ `ENABLED`

### ImscDestinationSettings
<a name="presets-model-imscdestinationsettings"></a>

Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibility | [ImscAccessibilitySubs](#presets-model-imscaccessibilitysubs) | False | If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>. |
| stylePassthrough | [ImscStylePassthrough](#presets-model-imscstylepassthrough) | False | Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions. |

### ImscStylePassthrough
<a name="presets-model-imscstylepassthrough"></a>

Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions.
+ `ENABLED`
+ `DISABLED`

### InsertableImage
<a name="presets-model-insertableimage"></a>

These settings apply to a specific graphic overlay. You can include multiple overlays in your job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| duration | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the time, in milliseconds, for the image to remain on the output video. This duration includes fade-in time but not fade-out time. |
| fadeIn | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the length of time, in milliseconds, between the Start time that you specify for the image insertion and the time that the image appears at full opacity. Full opacity is the level that you specify for the opacity setting. If you don't specify a value for Fade-in, the image will appear abruptly at the overlay start time. |
| fadeOut | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the length of time, in milliseconds, between the end of the time that you have specified for the image overlay Duration and when the overlaid image has faded to total transparency. If you don't specify a value for Fade-out, the image will disappear abruptly at the end of the inserted image duration. |
| height | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the height of the inserted image in pixels. If you specify a value that's larger than the video resolution height, the service will crop your overlaid image to fit. To use the native height of the image, keep this setting blank. |
| imageInserterInput | string<br />Pattern: `^((s3://(.*?)\.(bmp\|BMP\|png\|PNG\|tga\|TGA))\|(https?://(.*?)\.(bmp\|BMP\|png\|PNG\|tga\|TGA)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file. |
| imageX | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the distance, in pixels, between the inserted image and the left edge of the video frame. Required for any image overlay that you specify. |
| imageY | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the distance, in pixels, between the overlaid image and the top edge of the video frame. Required for any image overlay that you specify. |
| layer | integer<br />Minimum: 0<br />Maximum: 99 | False | Specify how overlapping inserted images appear. Images with higher values for Layer appear on top of images with lower values for Layer. |
| opacity | integer<br />Minimum: 0<br />Maximum: 100 | False | Use Opacity to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50. |
| startTime | string<br />Pattern: `^((([0-1]\d)\|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$` | False | Specify the timecode of the frame that you want the overlay to first appear on. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your timecode source settings. |
| width | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the width of the inserted image in pixels. If you specify a value that's larger than the video resolution width, the service will crop your overlaid image to fit. To use the native width of the image, keep this setting blank. |

### LanguageCode
<a name="presets-model-languagecode"></a>

Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php
+ `ENG`
+ `SPA`
+ `FRA`
+ `DEU`
+ `GER`
+ `ZHO`
+ `ARA`
+ `HIN`
+ `JPN`
+ `RUS`
+ `POR`
+ `ITA`
+ `URD`
+ `VIE`
+ `KOR`
+ `PAN`
+ `ABK`
+ `AAR`
+ `AFR`
+ `AKA`
+ `SQI`
+ `AMH`
+ `ARG`
+ `HYE`
+ `ASM`
+ `AVA`
+ `AVE`
+ `AYM`
+ `AZE`
+ `BAM`
+ `BAK`
+ `EUS`
+ `BEL`
+ `BEN`
+ `BIH`
+ `BIS`
+ `BOS`
+ `BRE`
+ `BUL`
+ `MYA`
+ `CAT`
+ `KHM`
+ `CHA`
+ `CHE`
+ `NYA`
+ `CHU`
+ `CHV`
+ `COR`
+ `COS`
+ `CRE`
+ `HRV`
+ `CES`
+ `DAN`
+ `DIV`
+ `NLD`
+ `DZO`
+ `ENM`
+ `EPO`
+ `EST`
+ `EWE`
+ `FAO`
+ `FIJ`
+ `FIN`
+ `FRM`
+ `FUL`
+ `GLA`
+ `GLG`
+ `LUG`
+ `KAT`
+ `ELL`
+ `GRN`
+ `GUJ`
+ `HAT`
+ `HAU`
+ `HEB`
+ `HER`
+ `HMO`
+ `HUN`
+ `ISL`
+ `IDO`
+ `IBO`
+ `IND`
+ `INA`
+ `ILE`
+ `IKU`
+ `IPK`
+ `GLE`
+ `JAV`
+ `KAL`
+ `KAN`
+ `KAU`
+ `KAS`
+ `KAZ`
+ `KIK`
+ `KIN`
+ `KIR`
+ `KOM`
+ `KON`
+ `KUA`
+ `KUR`
+ `LAO`
+ `LAT`
+ `LAV`
+ `LIM`
+ `LIN`
+ `LIT`
+ `LUB`
+ `LTZ`
+ `MKD`
+ `MLG`
+ `MSA`
+ `MAL`
+ `MLT`
+ `GLV`
+ `MRI`
+ `MAR`
+ `MAH`
+ `MON`
+ `NAU`
+ `NAV`
+ `NDE`
+ `NBL`
+ `NDO`
+ `NEP`
+ `SME`
+ `NOR`
+ `NOB`
+ `NNO`
+ `OCI`
+ `OJI`
+ `ORI`
+ `ORM`
+ `OSS`
+ `PLI`
+ `FAS`
+ `POL`
+ `PUS`
+ `QUE`
+ `QAA`
+ `RON`
+ `ROH`
+ `RUN`
+ `SMO`
+ `SAG`
+ `SAN`
+ `SRD`
+ `SRB`
+ `SNA`
+ `III`
+ `SND`
+ `SIN`
+ `SLK`
+ `SLV`
+ `SOM`
+ `SOT`
+ `SUN`
+ `SWA`
+ `SSW`
+ `SWE`
+ `TGL`
+ `TAH`
+ `TGK`
+ `TAM`
+ `TAT`
+ `TEL`
+ `THA`
+ `BOD`
+ `TIR`
+ `TON`
+ `TSO`
+ `TSN`
+ `TUR`
+ `TUK`
+ `TWI`
+ `UIG`
+ `UKR`
+ `UZB`
+ `VEN`
+ `VOL`
+ `WLN`
+ `CYM`
+ `FRY`
+ `WOL`
+ `XHO`
+ `YID`
+ `YOR`
+ `ZHA`
+ `ZUL`
+ `ORJ`
+ `QPC`
+ `TNG`
+ `SRP`

### ListPresetsRequest
<a name="presets-model-listpresetsrequest"></a>

You can send list presets requests with an empty body. Optionally, you can filter the response by category by specifying it in your request body. You can also optionally specify the maximum number, up to twenty, of queues to be returned.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| category | string | False | Optionally, specify a preset category to limit responses to only presets from that category. |
| listBy | [PresetListBy](#presets-model-presetlistby) | False | Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION\_DATE. If you don't specify, the service will list them by name. |
| maxResults | integer<br />Format: int32<br />Minimum: 1<br />Maximum: 20 | False | Optional. Number of presets, up to twenty, that will be returned at one time |
| nextToken | string | False | Use this string, provided with the response to a previous request, to request the next batch of presets. |
| order | [Order](#presets-model-order) | False | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. |

### ListPresetsResponse
<a name="presets-model-listpresetsresponse"></a>

Successful list presets requests return a JSON array of presets. If you don't specify how they are ordered, you will receive them alphabetically by name.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Use this string to request the next batch of presets. |
| presets | Array of type [Preset](#presets-model-preset) | False | List of presets |

### M2tsAudioBufferModel
<a name="presets-model-m2tsaudiobuffermodel"></a>

Selects between the DVB and ATSC buffer models for Dolby Digital audio.
+ `DVB`
+ `ATSC`

### M2tsAudioDuration
<a name="presets-model-m2tsaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### M2tsBufferModel
<a name="presets-model-m2tsbuffermodel"></a>

Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
+ `MULTIPLEX`
+ `NONE`

### M2tsDataPtsControl
<a name="presets-model-m2tsdataptscontrol"></a>

If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values.
+ `AUTO`
+ `ALIGN_TO_VIDEO`

### M2tsEbpAudioInterval
<a name="presets-model-m2tsebpaudiointerval"></a>

When set to VIDEO\_AND\_FIXED\_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO\_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY).
+ `VIDEO_AND_FIXED_INTERVALS`
+ `VIDEO_INTERVAL`

### M2tsEbpPlacement
<a name="presets-model-m2tsebpplacement"></a>

Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY).
+ `VIDEO_AND_AUDIO_PIDS`
+ `VIDEO_PID`

### M2tsEsRateInPes
<a name="presets-model-m2tsesrateinpes"></a>

Controls whether to include the ES Rate field in the PES header.
+ `INCLUDE`
+ `EXCLUDE`

### M2tsForceTsVideoEbpOrder
<a name="presets-model-m2tsforcetsvideoebporder"></a>

Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force.
+ `FORCE`
+ `DEFAULT`

### M2tsKlvMetadata
<a name="presets-model-m2tsklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### M2tsNielsenId3
<a name="presets-model-m2tsnielsenid3"></a>

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
+ `INSERT`
+ `NONE`

### M2tsPcrControl
<a name="presets-model-m2tspcrcontrol"></a>

When set to PCR\_EVERY\_PES\_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.
+ `PCR_EVERY_PES_PACKET`
+ `CONFIGURED_PCR_PERIOD`

### M2tsPreventBufferUnderflow
<a name="presets-model-m2tspreventbufferunderflow"></a>

Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete.
+ `DISABLED`
+ `ENABLED`

### M2tsRateMode
<a name="presets-model-m2tsratemode"></a>

When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.
+ `VBR`
+ `CBR`

### M2tsScte35Esam
<a name="presets-model-m2tsscte35esam"></a>

Settings for SCTE-35 signals from ESAM. Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scte35EsamPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream generated by ESAM. |

### M2tsScte35Source
<a name="presets-model-m2tsscte35source"></a>

For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam).
+ `PASSTHROUGH`
+ `NONE`

### M2tsSegmentationMarkers
<a name="presets-model-m2tssegmentationmarkers"></a>

Inserts segmentation markers at each segmentation\_time period. rai\_segstart sets the Random Access Indicator bit in the adaptation field. rai\_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi\_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp\_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
+ `NONE`
+ `RAI_SEGSTART`
+ `RAI_ADAPT`
+ `PSI_SEGSTART`
+ `EBP`
+ `EBP_LEGACY`

### M2tsSegmentationStyle
<a name="presets-model-m2tssegmentationstyle"></a>

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset\_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation\_time seconds. When a segmentation style of "maintain\_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation\_time seconds. Note that EBP lookahead is a slight exception to this rule.
+ `MAINTAIN_CADENCE`
+ `RESET_CADENCE`

### M2tsSettings
<a name="presets-model-m2tssettings"></a>

MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioBufferModel | [M2tsAudioBufferModel](#presets-model-m2tsaudiobuffermodel) | False | Selects between the DVB and ATSC buffer models for Dolby Digital audio. |
| audioDuration | [M2tsAudioDuration](#presets-model-m2tsaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioFramesPerPes | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The number of audio frames to insert for each PES packet. |
| audioPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifiers (PIDs) for any elementary audio streams you include in this output. Specify multiple PIDs as a JSON array. Default is the range 482-492. |
| audioPtsOffsetDelta | integer<br />Minimum: -10000<br />Maximum: 10000 | False | Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0. |
| bitrate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000. |
| bufferModel | [M2tsBufferModel](#presets-model-m2tsbuffermodel) | False | Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions. |
| dataPTSControl | [M2tsDataPtsControl](#presets-model-m2tsdataptscontrol) | False | If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values. |
| dvbNitSettings | [DvbNitSettings](#presets-model-dvbnitsettings) | False | Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output. |
| dvbSdtSettings | [DvbSdtSettings](#presets-model-dvbsdtsettings) | False | Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output. |
| dvbSubPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifiers (PIDs) for DVB subtitle data included in this output. Specify multiple PIDs as a JSON array. Default is the range 460-479. |
| dvbTdtSettings | [DvbTdtSettings](#presets-model-dvbtdtsettings) | False | Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output. |
| dvbTeletextPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for DVB teletext data you include in this output. Default is 499. |
| ebpAudioInterval | [M2tsEbpAudioInterval](#presets-model-m2tsebpaudiointerval) | False | When set to VIDEO\_AND\_FIXED\_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO\_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY). |
| ebpPlacement | [M2tsEbpPlacement](#presets-model-m2tsebpplacement) | False | Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY). |
| esRateInPes | [M2tsEsRateInPes](#presets-model-m2tsesrateinpes) | False | Controls whether to include the ES Rate field in the PES header. |
| forceTsVideoEbpOrder | [M2tsForceTsVideoEbpOrder](#presets-model-m2tsforcetsvideoebporder) | False | Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force. |
| fragmentTime | number<br />Format: float<br />Minimum: 0.0 | False | The length, in seconds, of each fragment. Only used with EBP markers. |
| klvMetadata | [M2tsKlvMetadata](#presets-model-m2tsklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| maxPcrInterval | integer<br />Minimum: 0<br />Maximum: 500 | False | Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream. |
| minEbpInterval | integer<br />Minimum: 0<br />Maximum: 10000 | False | When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate. |
| nielsenId3 | [M2tsNielsenId3](#presets-model-m2tsnielsenid3) | False | If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| nullPacketBitrate | number<br />Format: float<br />Minimum: 0.0 | False | Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pcrControl | [M2tsPcrControl](#presets-model-m2tspcrcontrol) | False | When set to PCR\_EVERY\_PES\_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for the program clock reference (PCR) in this output. If you do not specify a value, the service will use the value for Video PID. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | Specify the number of milliseconds between instances of the program map table (PMT) in the output transport stream. |
| pmtPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for the program map table (PMT) itself. Default is 480. |
| preventBufferUnderflow | [M2tsPreventBufferUnderflow](#presets-model-m2tspreventbufferunderflow) | False | Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete. |
| privateMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the private metadata stream. Default is 503. |
| programNumber | integer<br />Minimum: 0<br />Maximum: 65535 | False | Use Program number to specify the program number used in the program map table (PMT) for this output. Default is 1. Program numbers and program map tables are parts of MPEG-2 transport stream containers, used for organizing data. |
| ptsOffset | integer<br />Minimum: 0<br />Maximum: 3600 | False | Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2. |
| ptsOffsetMode | [TsPtsOffset](#presets-model-tsptsoffset) | False | Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset. |
| rateMode | [M2tsRateMode](#presets-model-m2tsratemode) | False | When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate. |
| scte35Esam | [M2tsScte35Esam](#presets-model-m2tsscte35esam) | False | Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Pid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the SCTE-35 stream in the transport stream. |
| scte35Source | [M2tsScte35Source](#presets-model-m2tsscte35source) | False | For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam). |
| segmentationMarkers | [M2tsSegmentationMarkers](#presets-model-m2tssegmentationmarkers) | False | Inserts segmentation markers at each segmentation\_time period. rai\_segstart sets the Random Access Indicator bit in the adaptation field. rai\_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi\_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp\_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format. |
| segmentationStyle | [M2tsSegmentationStyle](#presets-model-m2tssegmentationstyle) | False | The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset\_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation\_time seconds. When a segmentation style of "maintain\_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation\_time seconds. Note that EBP lookahead is a slight exception to this rule. |
| segmentationTime | number<br />Format: float<br />Minimum: 0.0 | False | Specify the length, in seconds, of each segment. Required unless markers is set to \_none\_. |
| timedMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the ID3 metadata stream in the transport stream. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | Specify the ID for the transport stream itself in the program map table for this output. Transport stream IDs and program map tables are parts of MPEG-2 transport stream containers, used for organizing data. |
| videoPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the elementary video stream in the transport stream. |

### M3u8AudioDuration
<a name="presets-model-m3u8audioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### M3u8DataPtsControl
<a name="presets-model-m3u8dataptscontrol"></a>

If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values.
+ `AUTO`
+ `ALIGN_TO_VIDEO`

### M3u8NielsenId3
<a name="presets-model-m3u8nielsenid3"></a>

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
+ `INSERT`
+ `NONE`

### M3u8PcrControl
<a name="presets-model-m3u8pcrcontrol"></a>

When set to PCR\_EVERY\_PES\_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
+ `PCR_EVERY_PES_PACKET`
+ `CONFIGURED_PCR_PERIOD`

### M3u8Scte35Source
<a name="presets-model-m3u8scte35source"></a>

For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML.
+ `PASSTHROUGH`
+ `NONE`

### M3u8Settings
<a name="presets-model-m3u8settings"></a>

These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [M3u8AudioDuration](#presets-model-m3u8audioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioFramesPerPes | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The number of audio frames to insert for each PES packet. |
| audioPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. |
| audioPtsOffsetDelta | integer<br />Minimum: -10000<br />Maximum: 10000 | False | Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0. |
| dataPTSControl | [M3u8DataPtsControl](#presets-model-m3u8dataptscontrol) | False | If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values. |
| maxPcrInterval | integer<br />Minimum: 0<br />Maximum: 500 | False | Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream. |
| nielsenId3 | [M3u8NielsenId3](#presets-model-m3u8nielsenid3) | False | If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pcrControl | [M3u8PcrControl](#presets-model-m3u8pcrcontrol) | False | When set to PCR\_EVERY\_PES\_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pmtPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. |
| privateMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the private metadata stream in the transport stream. |
| programNumber | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| ptsOffset | integer<br />Minimum: 0<br />Maximum: 3600 | False | Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2. |
| ptsOffsetMode | [TsPtsOffset](#presets-model-tsptsoffset) | False | Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset. |
| scte35Pid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. |
| scte35Source | [M3u8Scte35Source](#presets-model-m3u8scte35source) | False | For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML. |
| timedMetadata | [TimedMetadata](#presets-model-timedmetadata) | False | Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank. |
| timedMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the ID3 metadata stream in the transport stream. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the elementary video stream in the transport stream. |

### MovClapAtom
<a name="presets-model-movclapatom"></a>

When enabled, include 'clap' atom if appropriate for the video output settings.
+ `INCLUDE`
+ `EXCLUDE`

### MovCslgAtom
<a name="presets-model-movcslgatom"></a>

When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
+ `INCLUDE`
+ `EXCLUDE`

### MovMpeg2FourCCControl
<a name="presets-model-movmpeg2fourcccontrol"></a>

When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.
+ `XDCAM`
+ `MPEG`

### MovPaddingControl
<a name="presets-model-movpaddingcontrol"></a>

Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding.
+ `OMNEON`
+ `NONE`

### MovReference
<a name="presets-model-movreference"></a>

Always keep the default value (SELF\_CONTAINED) for this setting.
+ `SELF_CONTAINED`
+ `EXTERNAL`

### MovSettings
<a name="presets-model-movsettings"></a>

These settings relate to your QuickTime MOV output container.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clapAtom | [MovClapAtom](#presets-model-movclapatom) | False | When enabled, include 'clap' atom if appropriate for the video output settings. |
| cslgAtom | [MovCslgAtom](#presets-model-movcslgatom) | False | When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools. |
| mpeg2FourCCControl | [MovMpeg2FourCCControl](#presets-model-movmpeg2fourcccontrol) | False | When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2. |
| paddingControl | [MovPaddingControl](#presets-model-movpaddingcontrol) | False | Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding. |
| reference | [MovReference](#presets-model-movreference) | False | Always keep the default value (SELF\_CONTAINED) for this setting. |

### Mp2AudioDescriptionMix
<a name="presets-model-mp2audiodescriptionmix"></a>

Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
+ `BROADCASTER_MIXED_AD`
+ `NONE`

### Mp2Settings
<a name="presets-model-mp2settings"></a>

Required when you set Codec to the value MP2.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionMix | [Mp2AudioDescriptionMix](#presets-model-mp2audiodescriptionmix) | False | Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType. |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 384000 | False | Specify the average bitrate in bits per second. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Set Channels to specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 0, 1, and 2. |
| sampleRate | integer<br />Minimum: 32000<br />Maximum: 48000 | False | Sample rate in Hz. |

### Mp3RateControlMode
<a name="presets-model-mp3ratecontrolmode"></a>

Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR).
+ `CBR`
+ `VBR`

### Mp3Settings
<a name="presets-model-mp3settings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 16000<br />Maximum: 320000 | False | Specify the average bitrate in bits per second. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. |
| rateControlMode | [Mp3RateControlMode](#presets-model-mp3ratecontrolmode) | False | Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR). |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 48000 | False | Sample rate in Hz. |
| vbrQuality | integer<br />Minimum: 0<br />Maximum: 9 | False | Required when you set Bitrate control mode to VBR. Specify the audio quality of this MP3 output from 0 (highest quality) to 9 (lowest quality). |

### Mp4C2paManifest
<a name="presets-model-mp4c2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### Mp4CslgAtom
<a name="presets-model-mp4cslgatom"></a>

When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
+ `INCLUDE`
+ `EXCLUDE`

### Mp4FreeSpaceBox
<a name="presets-model-mp4freespacebox"></a>

Inserts a free-space box immediately after the moov box.
+ `INCLUDE`
+ `EXCLUDE`

### Mp4MoovPlacement
<a name="presets-model-mp4moovplacement"></a>

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.
+ `PROGRESSIVE_DOWNLOAD`
+ `NORMAL`

### Mp4Settings
<a name="presets-model-mp4settings"></a>

These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html\#output-codecs-and-containers-supported-for-audio-only.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [CmfcAudioDuration](#presets-model-cmfcaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| c2paManifest | [Mp4C2paManifest](#presets-model-mp4c2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| cslgAtom | [Mp4CslgAtom](#presets-model-mp4cslgatom) | False | When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools. |
| cttsVersion | integer<br />Minimum: 0<br />Maximum: 1 | False | Ignore this setting unless compliance to the CTTS box version specification matters in your workflow. Specify a value of 1 to set your CTTS box version to 1 and make your output compliant with the specification. When you specify a value of 1, you must also set CSLG atom to the value INCLUDE. Keep the default value 0 to set your CTTS box version to 0. This can provide backward compatibility for some players and packagers. |
| freeSpaceBox | [Mp4FreeSpaceBox](#presets-model-mp4freespacebox) | False | Inserts a free-space box immediately after the moov box. |
| moovPlacement | [Mp4MoovPlacement](#presets-model-mp4moovplacement) | False | To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal. |
| mp4MajorBrand | string | False | Overrides the "Major Brand" field in the output file. Usually not necessary to specify. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |

### MpdAccessibilityCaptionHints
<a name="presets-model-mpdaccessibilitycaptionhints"></a>

Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/>
+ `INCLUDE`
+ `EXCLUDE`

### MpdAudioDuration
<a name="presets-model-mpdaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### MpdC2paManifest
<a name="presets-model-mpdc2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### MpdCaptionContainerType
<a name="presets-model-mpdcaptioncontainertype"></a>

Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files.
+ `RAW`
+ `FRAGMENTED_MP4`

### MpdKlvMetadata
<a name="presets-model-mpdklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `NONE`
+ `PASSTHROUGH`

### MpdManifestMetadataSignaling
<a name="presets-model-mpdmanifestmetadatasignaling"></a>

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.
+ `ENABLED`
+ `DISABLED`

### MpdScte35Esam
<a name="presets-model-mpdscte35esam"></a>

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.
+ `INSERT`
+ `NONE`

### MpdScte35Source
<a name="presets-model-mpdscte35source"></a>

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output.
+ `PASSTHROUGH`
+ `NONE`

### MpdSettings
<a name="presets-model-mpdsettings"></a>

These settings relate to the fragmented MP4 container for the segments in your DASH outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibilityCaptionHints | [MpdAccessibilityCaptionHints](#presets-model-mpdaccessibilitycaptionhints) | False | Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/> |
| audioDuration | [MpdAudioDuration](#presets-model-mpdaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| c2paManifest | [MpdC2paManifest](#presets-model-mpdc2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| captionContainerType | [MpdCaptionContainerType](#presets-model-mpdcaptioncontainertype) | False | Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files. |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| klvMetadata | [MpdKlvMetadata](#presets-model-mpdklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| manifestMetadataSignaling | [MpdManifestMetadataSignaling](#presets-model-mpdmanifestmetadatasignaling) | False | To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough. |
| scte35Esam | [MpdScte35Esam](#presets-model-mpdscte35esam) | False | Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Source | [MpdScte35Source](#presets-model-mpdscte35source) | False | Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |
| timedMetadata | [MpdTimedMetadata](#presets-model-mpdtimedmetadata) | False | To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank. |
| timedMetadataBoxVersion | [MpdTimedMetadataBoxVersion](#presets-model-mpdtimedmetadataboxversion) | False | Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough. |
| timedMetadataSchemeIdUri | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: https://aomedia.org/emsg/ID3 When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough. |
| timedMetadataValue | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough. |

### MpdTimedMetadata
<a name="presets-model-mpdtimedmetadata"></a>

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### MpdTimedMetadataBoxVersion
<a name="presets-model-mpdtimedmetadataboxversion"></a>

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.
+ `VERSION_0`
+ `VERSION_1`

### Mpeg2AdaptiveQuantization
<a name="presets-model-mpeg2adaptivequantization"></a>

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### Mpeg2CodecLevel
<a name="presets-model-mpeg2codeclevel"></a>

Use Level to set the MPEG-2 level for the video output.
+ `AUTO`
+ `LOW`
+ `MAIN`
+ `HIGH1440`
+ `HIGH`

### Mpeg2CodecProfile
<a name="presets-model-mpeg2codecprofile"></a>

Use Profile to set the MPEG-2 profile for the video output.
+ `MAIN`
+ `PROFILE_422`

### Mpeg2DynamicSubGop
<a name="presets-model-mpeg2dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### Mpeg2FramerateControl
<a name="presets-model-mpeg2frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Mpeg2FramerateConversionAlgorithm
<a name="presets-model-mpeg2framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Mpeg2GopSizeUnits
<a name="presets-model-mpeg2gopsizeunits"></a>

Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames.
+ `FRAMES`
+ `SECONDS`

### Mpeg2InterlaceMode
<a name="presets-model-mpeg2interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### Mpeg2IntraDcPrecision
<a name="presets-model-mpeg2intradcprecision"></a>

Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.
+ `AUTO`
+ `INTRA_DC_PRECISION_8`
+ `INTRA_DC_PRECISION_9`
+ `INTRA_DC_PRECISION_10`
+ `INTRA_DC_PRECISION_11`

### Mpeg2ParControl
<a name="presets-model-mpeg2parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Mpeg2QualityTuningLevel
<a name="presets-model-mpeg2qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `MULTI_PASS`

### Mpeg2RateControlMode
<a name="presets-model-mpeg2ratecontrolmode"></a>

Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr).
+ `VBR`
+ `CBR`

### Mpeg2ScanTypeConversionMode
<a name="presets-model-mpeg2scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### Mpeg2SceneChangeDetect
<a name="presets-model-mpeg2scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default.
+ `DISABLED`
+ `ENABLED`

### Mpeg2Settings
<a name="presets-model-mpeg2settings"></a>

Required when you set Codec to the value MPEG2.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Mpeg2AdaptiveQuantization](#presets-model-mpeg2adaptivequantization) | False | Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 288000000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [Mpeg2CodecLevel](#presets-model-mpeg2codeclevel) | False | Use Level to set the MPEG-2 level for the video output. |
| codecProfile | [Mpeg2CodecProfile](#presets-model-mpeg2codecprofile) | False | Use Profile to set the MPEG-2 profile for the video output. |
| dynamicSubGop | [Mpeg2DynamicSubGop](#presets-model-mpeg2dynamicsubgop) | False | Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames. |
| framerateControl | [Mpeg2FramerateControl](#presets-model-mpeg2frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Mpeg2FramerateConversionAlgorithm](#presets-model-mpeg2framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. When you create a streaming output, we recommend that you keep the default value, 1, so that players starting mid-stream receive an IDR frame as quickly as possible. Don't set this value to 0; that would break output segmenting. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Specify the interval between keyframes, in seconds or frames, for this output. Default: 12 Related settings: When you specify the GOP size in seconds, set GOP mode control to Specified, seconds. The default value for GOP mode control is Frames. |
| gopSizeUnits | [Mpeg2GopSizeUnits](#presets-model-mpeg2gopsizeunits) | False | Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [Mpeg2InterlaceMode](#presets-model-mpeg2interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| intraDcPrecision | [Mpeg2IntraDcPrecision](#presets-model-mpeg2intradcprecision) | False | Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 300000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames that MediaConvert puts between reference frames in this output. Valid values are whole numbers from 0 through 7. When you don't specify a value, MediaConvert defaults to 2. |
| parControl | [Mpeg2ParControl](#presets-model-mpeg2parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [Mpeg2QualityTuningLevel](#presets-model-mpeg2qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| rateControlMode | [Mpeg2RateControlMode](#presets-model-mpeg2ratecontrolmode) | False | Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr). |
| scanTypeConversionMode | [Mpeg2ScanTypeConversionMode](#presets-model-mpeg2scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [Mpeg2SceneChangeDetect](#presets-model-mpeg2scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. |
| slowPal | [Mpeg2SlowPal](#presets-model-mpeg2slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless you need to comply with a specification that requires a specific value. If you don't have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, to use the AWS Elemental default matrices. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [Mpeg2SpatialAdaptiveQuantization](#presets-model-mpeg2spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| syntax | [Mpeg2Syntax](#presets-model-mpeg2syntax) | False | Specify whether this output's video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10. |
| telecine | [Mpeg2Telecine](#presets-model-mpeg2telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| temporalAdaptiveQuantization | [Mpeg2TemporalAdaptiveQuantization](#presets-model-mpeg2temporaladaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. |

### Mpeg2SlowPal
<a name="presets-model-mpeg2slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### Mpeg2SpatialAdaptiveQuantization
<a name="presets-model-mpeg2spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### Mpeg2Syntax
<a name="presets-model-mpeg2syntax"></a>

Specify whether this output's video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10.
+ `DEFAULT`
+ `D_10`

### Mpeg2Telecine
<a name="presets-model-mpeg2telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `SOFT`
+ `HARD`

### Mpeg2TemporalAdaptiveQuantization
<a name="presets-model-mpeg2temporaladaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### MxfAfdSignaling
<a name="presets-model-mxfafdsignaling"></a>

Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings.
+ `NO_COPY`
+ `COPY_FROM_VIDEO`

### MxfProfile
<a name="presets-model-mxfprofile"></a>

Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html.
+ `D_10`
+ `XDCAM`
+ `OP1A`
+ `XAVC`
+ `XDCAM_RDD9`

### MxfSettings
<a name="presets-model-mxfsettings"></a>

These settings relate to your MXF output container.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| afdSignaling | [MxfAfdSignaling](#presets-model-mxfafdsignaling) | False | Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings. |
| profile | [MxfProfile](#presets-model-mxfprofile) | False | Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html. |
| uncompressedAudioWrapping | [MxfUncompressedAudioWrapping](#presets-model-mxfuncompressedaudiowrapping) | False | Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a. |
| xavcProfileSettings | [MxfXavcProfileSettings](#presets-model-mxfxavcprofilesettings) | False | Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC. |

### MxfUncompressedAudioWrapping
<a name="presets-model-mxfuncompressedaudiowrapping"></a>

Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a.
+ `AUTO`
+ `AES3`

### MxfXavcDurationMode
<a name="presets-model-mxfxavcdurationmode"></a>

To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration.
+ `ALLOW_ANY_DURATION`
+ `DROP_FRAMES_FOR_COMPLIANCE`

### MxfXavcProfileSettings
<a name="presets-model-mxfxavcprofilesettings"></a>

Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| durationMode | [MxfXavcDurationMode](#presets-model-mxfxavcdurationmode) | False | To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration. |
| maxAncDataSize | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify a value for this setting only for outputs that you set up with one of these two XAVC profiles: XAVC HD Intra CBG or XAVC 4K Intra CBG. Specify the amount of space in each frame that the service reserves for ancillary data, such as teletext captions. The default value for this setting is 1492 bytes per frame. This should be sufficient to prevent overflow unless you have multiple pages of teletext captions data. If you have a large amount of teletext data, specify a larger number. |

### NexGuardFileMarkerSettings
<a name="presets-model-nexguardfilemarkersettings"></a>

For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| license | string<br />MinLength: 1<br />MaxLength: 100000 | False | Use the base64 license string that Nagra provides you. Enter it directly in your JSON job specification or in the console. Required when you include Nagra NexGuard File Marker watermarking in your job. |
| payload | integer<br />Minimum: 0<br />Maximum: 4194303 | False | Specify the payload ID that you want associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. Required when you include Nagra NexGuard File Marker watermarking in your job. For PreRelease Content (NGPR/G2), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of which ID you have assigned to each asset. Neither Nagra nor MediaConvert keep track of the relationship between output files and your IDs. For OTT Streaming, create two adaptive bitrate (ABR) stacks for each asset. Do this by setting up two output groups. For one output group, set the value of Payload ID to 0 in every output. For the other output group, set Payload ID to 1 in every output. |
| preset | string<br />MinLength: 1<br />MaxLength: 256 | False | Enter one of the watermarking preset strings that Nagra provides you. Required when you include Nagra NexGuard File Marker watermarking in your job. |
| strength | [WatermarkingStrength](#presets-model-watermarkingstrength) | False | Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value. |

### NoiseFilterPostTemporalSharpening
<a name="presets-model-noisefilterposttemporalsharpening"></a>

When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening.
+ `DISABLED`
+ `ENABLED`
+ `AUTO`

### NoiseFilterPostTemporalSharpeningStrength
<a name="presets-model-noisefilterposttemporalsharpeningstrength"></a>

Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening.
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### NoiseReducer
<a name="presets-model-noisereducer"></a>

Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| filter | [NoiseReducerFilter](#presets-model-noisereducerfilter) | False | Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. \* Bilateral preserves edges while reducing noise. \* Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. \* Conserve does min/max noise reduction. \* Spatial does frequency-domain filtering based on JND principles. \* Temporal optimizes video quality for complex motion. |
| filterSettings | [NoiseReducerFilterSettings](#presets-model-noisereducerfiltersettings) | False | Settings for a noise reducer filter |
| spatialFilterSettings | [NoiseReducerSpatialFilterSettings](#presets-model-noisereducerspatialfiltersettings) | False | Noise reducer filter settings for spatial filter. |
| temporalFilterSettings | [NoiseReducerTemporalFilterSettings](#presets-model-noisereducertemporalfiltersettings) | False | Noise reducer filter settings for temporal filter. |

### NoiseReducerFilter
<a name="presets-model-noisereducerfilter"></a>

Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. \* Bilateral preserves edges while reducing noise. \* Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. \* Conserve does min/max noise reduction. \* Spatial does frequency-domain filtering based on JND principles. \* Temporal optimizes video quality for complex motion.
+ `BILATERAL`
+ `MEAN`
+ `GAUSSIAN`
+ `LANCZOS`
+ `SHARPEN`
+ `CONSERVE`
+ `SPATIAL`
+ `TEMPORAL`

### NoiseReducerFilterSettings
<a name="presets-model-noisereducerfiltersettings"></a>

Settings for a noise reducer filter

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| strength | integer<br />Minimum: 0<br />Maximum: 3 | False | Relative strength of noise reducing filter. Higher values produce stronger filtering. |

### NoiseReducerSpatialFilterSettings
<a name="presets-model-noisereducerspatialfiltersettings"></a>

Noise reducer filter settings for spatial filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| postFilterSharpenStrength | integer<br />Minimum: 0<br />Maximum: 3 | False | Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength. |
| speed | integer<br />Minimum: -2<br />Maximum: 3 | False | The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value. |
| strength | integer<br />Minimum: 0<br />Maximum: 16 | False | Relative strength of noise reducing filter. Higher values produce stronger filtering. |

### NoiseReducerTemporalFilterSettings
<a name="presets-model-noisereducertemporalfiltersettings"></a>

Noise reducer filter settings for temporal filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aggressiveMode | integer<br />Minimum: 0<br />Maximum: 4 | False | Use Aggressive mode for content that has complex motion. Higher values produce stronger temporal filtering. This filters highly complex scenes more aggressively and creates better VQ for low bitrate outputs. |
| postTemporalSharpening | [NoiseFilterPostTemporalSharpening](#presets-model-noisefilterposttemporalsharpening) | False | When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening. |
| postTemporalSharpeningStrength | [NoiseFilterPostTemporalSharpeningStrength](#presets-model-noisefilterposttemporalsharpeningstrength) | False | Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening. |
| speed | integer<br />Minimum: -1<br />Maximum: 3 | False | The speed of the filter (higher number is faster). Low setting reduces bit rate at the cost of transcode time, high setting improves transcode time at the cost of bit rate. |
| strength | integer<br />Minimum: 0<br />Maximum: 16 | False | Specify the strength of the noise reducing filter on this output. Higher values produce stronger filtering. We recommend the following value ranges, depending on the result that you want: \* 0-2 for complexity reduction with minimal sharpness loss \* 2-8 for complexity reduction with image preservation \* 8-16 for a high level of complexity reduction |

### OpusSettings
<a name="presets-model-opussettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 192000 | False | Optional. Specify the average bitrate in bits per second. Valid values are multiples of 8000, from 32000 through 192000. The default value is 96000, which we recommend for quality and bandwidth. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. |
| sampleRate | integer<br />Minimum: 16000<br />Maximum: 48000 | False | Optional. Sample rate in Hz. Valid values are 16000, 24000, and 48000. The default value is 48000. |

### Order
<a name="presets-model-order"></a>

Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
+ `ASCENDING`
+ `DESCENDING`

### OutputChannelMapping
<a name="presets-model-outputchannelmapping"></a>

OutputChannel mapping settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputChannels | Array of type integer<br />Minimum: -60<br />Maximum: 6 | False | Use this setting to specify your remix values when they are integers, such as -10, 0, or 4. |
| inputChannelsFineTune | Array of type number<br />Format: float<br />Minimum: -60.0<br />Maximum: 6.0 | False | Use this setting to specify your remix values when they have a decimal component, such as -10.312, 0.08, or 4.9. MediaConvert rounds your remixing values to the nearest thousandth. |

### OutputSdt
<a name="presets-model-outputsdt"></a>

Selects method of inserting SDT information into output stream. "Follow input SDT" copies SDT information from input stream to output stream. "Follow input SDT if present" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter "SDT Manually" means user will enter the SDT information. "No SDT" means output stream will not contain SDT information.
+ `SDT_FOLLOW`
+ `SDT_FOLLOW_IF_PRESENT`
+ `SDT_MANUAL`
+ `SDT_NONE`

### PartnerWatermarking
<a name="presets-model-partnerwatermarking"></a>

If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nexguardFileMarkerSettings | [NexGuardFileMarkerSettings](#presets-model-nexguardfilemarkersettings) | False | For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows. |

### PassthroughSettings
<a name="presets-model-passthroughsettings"></a>

Optional settings when you set Codec to the value Passthrough.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| frameControl | [FrameControl](#presets-model-framecontrol) | False | Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players. |
| videoSelectorMode | [VideoSelectorMode](#presets-model-videoselectormode) | False | AUTO will select the highest bitrate input in the video selector source. REMUX\_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX\_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source. |

### Preset
<a name="presets-model-preset"></a>

A preset is a collection of preconfigured media conversion settings that you want MediaConvert to apply to the output during the conversion process.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | An identifier for this resource that is unique within all of AWS. |
| category | string | False | An optional category you create to organize your presets. |
| createdAt | string<br />Format: date-time | False | The timestamp in epoch seconds for preset creation. |
| description | string | False | An optional description you create for each preset. |
| lastUpdated | string<br />Format: date-time | False | The timestamp in epoch seconds when the preset was last updated. |
| name | string | True | A name you create for each preset. Each name must be unique within your account. |
| settings | [PresetSettings](#presets-model-presetsettings) | True | Settings for preset |
| type | [Type](#presets-model-type) | False | A preset can be of two types: system or custom. System or built-in preset can't be modified or deleted by the user. |

### PresetListBy
<a name="presets-model-presetlistby"></a>

Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION\_DATE. If you don't specify, the service will list them by name.
+ `NAME`
+ `CREATION_DATE`
+ `SYSTEM`

### PresetSettings
<a name="presets-model-presetsettings"></a>

Settings for preset

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptions | Array of type [AudioDescription](#presets-model-audiodescription) | False | Contains groups of audio encoding settings organized by audio codec. Include one instance of per output. Can contain multiple groups of encoding settings. |
| captionDescriptions | Array of type [CaptionDescriptionPreset](#presets-model-captiondescriptionpreset) | False | This object holds groups of settings related to captions for one output. For each output that has captions, include one instance of CaptionDescriptions. |
| containerSettings | [ContainerSettings](#presets-model-containersettings) | False | Container specific settings. |
| videoDescription | [VideoDescription](#presets-model-videodescription) | False | VideoDescription contains a group of video encoding settings. The specific video settings depend on the video codec that you choose for the property codec. Include one instance of VideoDescription per output. |

### ProresChromaSampling
<a name="presets-model-proreschromasampling"></a>

This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10\+, or Noise reducer.
+ `PRESERVE_444_SAMPLING`
+ `SUBSAMPLE_TO_422`

### ProresCodecProfile
<a name="presets-model-prorescodecprofile"></a>

Use Profile to specify the type of Apple ProRes codec to use for this output.
+ `APPLE_PRORES_422`
+ `APPLE_PRORES_422_HQ`
+ `APPLE_PRORES_422_LT`
+ `APPLE_PRORES_422_PROXY`
+ `APPLE_PRORES_4444`
+ `APPLE_PRORES_4444_XQ`

### ProresFramerateControl
<a name="presets-model-proresframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### ProresFramerateConversionAlgorithm
<a name="presets-model-proresframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### ProresInterlaceMode
<a name="presets-model-proresinterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### ProresParControl
<a name="presets-model-proresparcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### ProresScanTypeConversionMode
<a name="presets-model-proresscantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### ProresSettings
<a name="presets-model-proressettings"></a>

Required when you set Codec to the value PRORES.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| chromaSampling | [ProresChromaSampling](#presets-model-proreschromasampling) | False | This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10\+, or Noise reducer. |
| codecProfile | [ProresCodecProfile](#presets-model-prorescodecprofile) | False | Use Profile to specify the type of Apple ProRes codec to use for this output. |
| framerateControl | [ProresFramerateControl](#presets-model-proresframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [ProresFramerateConversionAlgorithm](#presets-model-proresframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [ProresInterlaceMode](#presets-model-proresinterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| parControl | [ProresParControl](#presets-model-proresparcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| scanTypeConversionMode | [ProresScanTypeConversionMode](#presets-model-proresscantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [ProresSlowPal](#presets-model-proresslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| telecine | [ProresTelecine](#presets-model-prorestelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### ProresSlowPal
<a name="presets-model-proresslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### ProresTelecine
<a name="presets-model-prorestelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### Rectangle
<a name="presets-model-rectangle"></a>

Use Rectangle to identify a specific area of the video frame.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 2<br />Maximum: 2147483647 | False | Height of rectangle in pixels. Specify only even numbers. |
| width | integer<br />Minimum: 2<br />Maximum: 2147483647 | False | Width of rectangle in pixels. Specify only even numbers. |
| x | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers. |
| y | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers. |

### RemixSettings
<a name="presets-model-remixsettings"></a>

Use Manual audio remixing to adjust audio levels for each audio channel in each output of your job. With audio remixing, you can output more or fewer audio channels than your input audio source provides.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionAudioChannel | integer<br />Minimum: 1<br />Maximum: 64 | False | Optionally specify the channel in your input that contains your audio description audio signal. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description audio channel, you must also specify an audio description data channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers. |
| audioDescriptionDataChannel | integer<br />Minimum: 1<br />Maximum: 64 | False | Optionally specify the channel in your input that contains your audio description data stream. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description data channel, you must also specify an audio description audio channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers. |
| channelMapping | [ChannelMapping](#presets-model-channelmapping) | False | Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Don't use both. |
| channelsIn | integer<br />Minimum: 1<br />Maximum: 64 | False | Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different. If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping. |
| channelsOut | integer<br />Minimum: 1<br />Maximum: 64 | False | Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and even numbers to 64.) If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping. |

### RemoveRubyReserveAttributes
<a name="presets-model-removerubyreserveattributes"></a>

Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### RespondToAfd
<a name="presets-model-respondtoafd"></a>

Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. \* Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. \* Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. \* Choose None to remove all input AFD values from this output.
+ `NONE`
+ `RESPOND`
+ `PASSTHROUGH`

### SampleRangeConversion
<a name="presets-model-samplerangeconversion"></a>

Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output.
+ `LIMITED_RANGE_SQUEEZE`
+ `NONE`
+ `LIMITED_RANGE_CLIP`

### ScalingBehavior
<a name="presets-model-scalingbehavior"></a>

Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported).
+ `DEFAULT`
+ `STRETCH_TO_OUTPUT`
+ `FIT`
+ `FIT_NO_UPSCALE`
+ `FILL`
+ `SMART_CROP`

### SccDestinationFramerate
<a name="presets-model-sccdestinationframerate"></a>

Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video\_insertion=true and drop\_frame\_timecode=true; otherwise, choose 29.97 non-dropframe.
+ `FRAMERATE_23_97`
+ `FRAMERATE_24`
+ `FRAMERATE_25`
+ `FRAMERATE_29_97_DROPFRAME`
+ `FRAMERATE_29_97_NON_DROPFRAME`

### SccDestinationSettings
<a name="presets-model-sccdestinationsettings"></a>

Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerate | [SccDestinationFramerate](#presets-model-sccdestinationframerate) | False | Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video\_insertion=true and drop\_frame\_timecode=true; otherwise, choose 29.97 non-dropframe. |

### SlowPalPitchCorrection
<a name="presets-model-slowpalpitchcorrection"></a>

Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### SrtDestinationSettings
<a name="presets-model-srtdestinationsettings"></a>

Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stylePassthrough | [SrtStylePassthrough](#presets-model-srtstylepassthrough) | False | Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions. |

### SrtStylePassthrough
<a name="presets-model-srtstylepassthrough"></a>

Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions.
+ `ENABLED`
+ `DISABLED`

### TeletextDestinationSettings
<a name="presets-model-teletextdestinationsettings"></a>

Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pageNumber | string<br />Pattern: `^[1-8][0-9a-fA-F][0-9a-eA-E]$`<br />MinLength: 3<br />MaxLength: 3 | False | Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field. |
| pageTypes | Array of type [TeletextPageType](#presets-model-teletextpagetype) | False | Specify the page types for this Teletext page. If you don't specify a value here, the service sets the page type to the default value Subtitle. If you pass through the entire set of Teletext data, don't use this field. When you pass through a set of Teletext pages, your output has the same page types as your input. |

### TeletextPageType
<a name="presets-model-teletextpagetype"></a>

A page type as defined in the standard ETSI EN 300 468, Table 94
+ `PAGE_TYPE_INITIAL`
+ `PAGE_TYPE_SUBTITLE`
+ `PAGE_TYPE_ADDL_INFO`
+ `PAGE_TYPE_PROGRAM_SCHEDULE`
+ `PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE`

### TimecodeBurnin
<a name="presets-model-timecodeburnin"></a>

Settings for burning the output timecode and specified prefix into the output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fontSize | integer<br />Minimum: 10<br />Maximum: 48 | False | Use Font size to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48. |
| position | [TimecodeBurninPosition](#presets-model-timecodeburninposition) | False | Use Position under Timecode burn-in to specify the location the burned-in timecode on output video. |
| prefix | string<br />Pattern: `^[ -~]+$` | False | Use Prefix to place ASCII characters before any burned-in timecode. For example, a prefix of "EZ-" will result in the timecode "EZ-00:00:00:00". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard. |

### TimecodeBurninPosition
<a name="presets-model-timecodeburninposition"></a>

Use Position under Timecode burn-in to specify the location the burned-in timecode on output video.
+ `TOP_CENTER`
+ `TOP_LEFT`
+ `TOP_RIGHT`
+ `MIDDLE_LEFT`
+ `MIDDLE_CENTER`
+ `MIDDLE_RIGHT`
+ `BOTTOM_LEFT`
+ `BOTTOM_CENTER`
+ `BOTTOM_RIGHT`

### TimecodeTrack
<a name="presets-model-timecodetrack"></a>

To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### TimedMetadata
<a name="presets-model-timedmetadata"></a>

Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### TsPtsOffset
<a name="presets-model-tsptsoffset"></a>

Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset.
+ `AUTO`
+ `SECONDS`
+ `MILLISECONDS`

### TtmlDestinationSettings
<a name="presets-model-ttmldestinationsettings"></a>

Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stylePassthrough | [TtmlStylePassthrough](#presets-model-ttmlstylepassthrough) | False | Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output. |

### TtmlStylePassthrough
<a name="presets-model-ttmlstylepassthrough"></a>

Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output.
+ `ENABLED`
+ `DISABLED`

### Type
<a name="presets-model-type"></a>
+ `SYSTEM`
+ `CUSTOM`

### UncompressedFourcc
<a name="presets-model-uncompressedfourcc"></a>

The four character code for the uncompressed video.
+ `I420`
+ `I422`
+ `I444`

### UncompressedFramerateControl
<a name="presets-model-uncompressedframeratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### UncompressedFramerateConversionAlgorithm
<a name="presets-model-uncompressedframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### UncompressedInterlaceMode
<a name="presets-model-uncompressedinterlacemode"></a>

Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output.
+ `INTERLACED`
+ `PROGRESSIVE`

### UncompressedScanTypeConversionMode
<a name="presets-model-uncompressedscantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### UncompressedSettings
<a name="presets-model-uncompressedsettings"></a>

Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fourcc | [UncompressedFourcc](#presets-model-uncompressedfourcc) | False | The four character code for the uncompressed video. |
| framerateControl | [UncompressedFramerateControl](#presets-model-uncompressedframeratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [UncompressedFramerateConversionAlgorithm](#presets-model-uncompressedframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [UncompressedInterlaceMode](#presets-model-uncompressedinterlacemode) | False | Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output. |
| scanTypeConversionMode | [UncompressedScanTypeConversionMode](#presets-model-uncompressedscantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [UncompressedSlowPal](#presets-model-uncompressedslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25. |
| telecine | [UncompressedTelecine](#presets-model-uncompressedtelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### UncompressedSlowPal
<a name="presets-model-uncompressedslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### UncompressedTelecine
<a name="presets-model-uncompressedtelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### Vc3Class
<a name="presets-model-vc3class"></a>

Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output.
+ `CLASS_145_8BIT`
+ `CLASS_220_8BIT`
+ `CLASS_220_10BIT`

### Vc3FramerateControl
<a name="presets-model-vc3frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vc3FramerateConversionAlgorithm
<a name="presets-model-vc3framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vc3InterlaceMode
<a name="presets-model-vc3interlacemode"></a>

Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output.
+ `INTERLACED`
+ `PROGRESSIVE`

### Vc3ScanTypeConversionMode
<a name="presets-model-vc3scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### Vc3Settings
<a name="presets-model-vc3settings"></a>

Required when you set Codec to the value VC3

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateControl | [Vc3FramerateControl](#presets-model-vc3frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vc3FramerateConversionAlgorithm](#presets-model-vc3framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [Vc3InterlaceMode](#presets-model-vc3interlacemode) | False | Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output. |
| scanTypeConversionMode | [Vc3ScanTypeConversionMode](#presets-model-vc3scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [Vc3SlowPal](#presets-model-vc3slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25. |
| telecine | [Vc3Telecine](#presets-model-vc3telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| vc3Class | [Vc3Class](#presets-model-vc3class) | False | Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output. |

### Vc3SlowPal
<a name="presets-model-vc3slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### Vc3Telecine
<a name="presets-model-vc3telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### VideoCodec
<a name="presets-model-videocodec"></a>

Type of video codec
+ `AV1`
+ `AVC_INTRA`
+ `FRAME_CAPTURE`
+ `GIF`
+ `H_264`
+ `H_265`
+ `MPEG2`
+ `PASSTHROUGH`
+ `PRORES`
+ `UNCOMPRESSED`
+ `VC3`
+ `VP8`
+ `VP9`
+ `XAVC`

### VideoCodecSettings
<a name="presets-model-videocodecsettings"></a>

Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. \* AV1, Av1Settings \* AVC\_INTRA, AvcIntraSettings \* FRAME\_CAPTURE, FrameCaptureSettings \* GIF, GifSettings \* H\_264, H264Settings \* H\_265, H265Settings \* MPEG2, Mpeg2Settings \* PRORES, ProresSettings \* UNCOMPRESSED, UncompressedSettings \* VC3, Vc3Settings \* VP8, Vp8Settings \* VP9, Vp9Settings \* XAVC, XavcSettings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| av1Settings | [Av1Settings](#presets-model-av1settings) | False | Required when you set Codec, under VideoDescription>CodecSettings to the value AV1. |
| avcIntraSettings | [AvcIntraSettings](#presets-model-avcintrasettings) | False | Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf. |
| codec | [VideoCodec](#presets-model-videocodec) | False | Specifies the video codec. This must be equal to one of the enum values defined by the object VideoCodec. To passthrough the video stream of your input without any video encoding: Choose Passthrough. More information about passthrough codec support and job settings requirements, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/video-passthrough-feature-restrictions.html |
| frameCaptureSettings | [FrameCaptureSettings](#presets-model-framecapturesettings) | False | Required when you set Codec to the value FRAME\_CAPTURE. |
| gifSettings | [GifSettings](#presets-model-gifsettings) | False | Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF |
| h264Settings | [H264Settings](#presets-model-h264settings) | False | Required when you set Codec to the value H\_264. |
| h265Settings | [H265Settings](#presets-model-h265settings) | False | Settings for H265 codec |
| mpeg2Settings | [Mpeg2Settings](#presets-model-mpeg2settings) | False | Required when you set Codec to the value MPEG2. |
| passthroughSettings | [PassthroughSettings](#presets-model-passthroughsettings) | False | Optional settings when you set Codec to the value Passthrough. |
| proresSettings | [ProresSettings](#presets-model-proressettings) | False | Required when you set Codec to the value PRORES. |
| uncompressedSettings | [UncompressedSettings](#presets-model-uncompressedsettings) | False | Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED. |
| vc3Settings | [Vc3Settings](#presets-model-vc3settings) | False | Required when you set Codec to the value VC3 |
| vp8Settings | [Vp8Settings](#presets-model-vp8settings) | False | Required when you set Codec to the value VP8. |
| vp9Settings | [Vp9Settings](#presets-model-vp9settings) | False | Required when you set Codec to the value VP9. |
| xavcSettings | [XavcSettings](#presets-model-xavcsettings) | False | Required when you set Codec to the value XAVC. |

### VideoDescription
<a name="presets-model-videodescription"></a>

Settings related to video encoding of your output. The specific video settings depend on the video codec that you choose.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| afdSignaling | [AfdSignaling](#presets-model-afdsignaling) | False | This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. \* Choose None to remove all AFD values from this output. \* Choose Fixed to ignore input AFD values and instead encode the value specified in the job. \* Choose Auto to calculate output AFD values based on the input AFD scaler data. |
| antiAlias | [AntiAlias](#presets-model-antialias) | False | The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting. |
| chromaPositionMode | [ChromaPositionMode](#presets-model-chromapositionmode) | False | Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left. |
| codecSettings | [VideoCodecSettings](#presets-model-videocodecsettings) | False | Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. \* AV1, Av1Settings \* AVC\_INTRA, AvcIntraSettings \* FRAME\_CAPTURE, FrameCaptureSettings \* GIF, GifSettings \* H\_264, H264Settings \* H\_265, H265Settings \* MPEG2, Mpeg2Settings \* PRORES, ProresSettings \* UNCOMPRESSED, UncompressedSettings \* VC3, Vc3Settings \* VP8, Vp8Settings \* VP9, Vp9Settings \* XAVC, XavcSettings |
| colorMetadata | [ColorMetadata](#presets-model-colormetadata) | False | Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default. |
| crop | [Rectangle](#presets-model-rectangle) | False | Use Cropping selection to specify the video area that the service will include in the output video frame. |
| dropFrameTimecode | [DropFrameTimecode](#presets-model-dropframetimecode) | False | Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled. |
| fixedAfd | integer<br />Minimum: 0<br />Maximum: 15 | False | Applies only if you set AFD Signaling to Fixed. Use Fixed to specify a four-bit AFD value which the service will write on all frames of this video output. |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Height blank and enter a value for Width. For example, if your input is 1920x1080 and you set Width to 1280, your output will be 1280x720. |
| position | [Rectangle](#presets-model-rectangle) | False | Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black. |
| respondToAfd | [RespondToAfd](#presets-model-respondtoafd) | False | Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. \* Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. \* Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. \* Choose None to remove all input AFD values from this output. |
| scalingBehavior | [ScalingBehavior](#presets-model-scalingbehavior) | False | Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported). |
| sharpness | integer<br />Minimum: 0<br />Maximum: 100 | False | Use Sharpness setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content. |
| timecodeInsertion | [VideoTimecodeInsertion](#presets-model-videotimecodeinsertion) | False | Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC\_TIMING\_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does. |
| timecodeTrack | [TimecodeTrack](#presets-model-timecodetrack) | False | To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled. |
| videoPreprocessors | [VideoPreprocessor](#presets-model-videopreprocessor) | False | Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Width blank and enter a value for Height. For example, if your input is 1920x1080 and you set Height to 720, your output will be 1280x720. |

### VideoPreprocessor
<a name="presets-model-videopreprocessor"></a>

Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorCorrector | [ColorCorrector](#presets-model-colorcorrector) | False | Use these settings to convert the color space or to modify properties such as hue and contrast for this output. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html. |
| deinterlacer | [Deinterlacer](#presets-model-deinterlacer) | False | Use the deinterlacer to produce smoother motion and a clearer picture. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html. |
| dolbyVision | [DolbyVision](#presets-model-dolbyvision) | False | Enable Dolby Vision feature to produce Dolby Vision compatible video output. |
| hdr10Plus | [Hdr10Plus](#presets-model-hdr10plus) | False | Enable HDR10\+ analysis and metadata injection. Compatible with HEVC only. |
| imageInserter | [ImageInserter](#presets-model-imageinserter) | False | Enable the Image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default. |
| noiseReducer | [NoiseReducer](#presets-model-noisereducer) | False | Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter. |
| partnerWatermarking | [PartnerWatermarking](#presets-model-partnerwatermarking) | False | If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output. |
| timecodeBurnin | [TimecodeBurnin](#presets-model-timecodeburnin) | False | Settings for burning the output timecode and specified prefix into the output. |

### VideoSelectorMode
<a name="presets-model-videoselectormode"></a>

AUTO will select the highest bitrate input in the video selector source. REMUX\_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX\_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source.
+ `AUTO`
+ `REMUX_ALL`

### VideoTimecodeInsertion
<a name="presets-model-videotimecodeinsertion"></a>

Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC\_TIMING\_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does.
+ `DISABLED`
+ `PIC_TIMING_SEI`

### VorbisSettings
<a name="presets-model-vorbissettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Optional. Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono on the console gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. The default value is 2. |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 48000 | False | Optional. Specify the audio sample rate in Hz. Valid values are 22050, 32000, 44100, and 48000. The default value is 48000. |
| vbrQuality | integer<br />Minimum: -1<br />Maximum: 10 | False | Optional. Specify the variable audio quality of this Vorbis output from -1 (lowest quality, \~45 kbit/s) to 10 (highest quality, \~500 kbit/s). The default value is 4 (\~128 kbit/s). Values 5 and 6 are approximately 160 and 192 kbit/s, respectively. |

### Vp8FramerateControl
<a name="presets-model-vp8frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp8FramerateConversionAlgorithm
<a name="presets-model-vp8framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vp8ParControl
<a name="presets-model-vp8parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp8QualityTuningLevel
<a name="presets-model-vp8qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.
+ `MULTI_PASS`
+ `MULTI_PASS_HQ`

### Vp8RateControlMode
<a name="presets-model-vp8ratecontrolmode"></a>

With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode.
+ `VBR`

### Vp8Settings
<a name="presets-model-vp8settings"></a>

Required when you set Codec to the value VP8.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Target bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| framerateControl | [Vp8FramerateControl](#presets-model-vp8frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vp8FramerateConversionAlgorithm](#presets-model-vp8framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | GOP Length (keyframe interval) in frames. Must be greater than zero. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Optional. Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Ignore this setting unless you set qualityTuningLevel to MULTI\_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate. |
| parControl | [Vp8ParControl](#presets-model-vp8parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| qualityTuningLevel | [Vp8QualityTuningLevel](#presets-model-vp8qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding. |
| rateControlMode | [Vp8RateControlMode](#presets-model-vp8ratecontrolmode) | False | With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode. |

### Vp9FramerateControl
<a name="presets-model-vp9frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp9FramerateConversionAlgorithm
<a name="presets-model-vp9framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vp9ParControl
<a name="presets-model-vp9parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp9QualityTuningLevel
<a name="presets-model-vp9qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.
+ `MULTI_PASS`
+ `MULTI_PASS_HQ`

### Vp9RateControlMode
<a name="presets-model-vp9ratecontrolmode"></a>

With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode.
+ `VBR`

### Vp9Settings
<a name="presets-model-vp9settings"></a>

Required when you set Codec to the value VP9.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 480000000 | False | Target bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| framerateControl | [Vp9FramerateControl](#presets-model-vp9frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vp9FramerateConversionAlgorithm](#presets-model-vp9framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | GOP Length (keyframe interval) in frames. Must be greater than zero. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 480000000 | False | Ignore this setting unless you set qualityTuningLevel to MULTI\_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate. |
| parControl | [Vp9ParControl](#presets-model-vp9parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio for this output. The default behavior is to use the same pixel aspect ratio as your input video. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| qualityTuningLevel | [Vp9QualityTuningLevel](#presets-model-vp9qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding. |
| rateControlMode | [Vp9RateControlMode](#presets-model-vp9ratecontrolmode) | False | With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode. |

### WatermarkingStrength
<a name="presets-model-watermarkingstrength"></a>

Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value.
+ `LIGHTEST`
+ `LIGHTER`
+ `DEFAULT`
+ `STRONGER`
+ `STRONGEST`

### WavFormat
<a name="presets-model-wavformat"></a>

Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible.
+ `RIFF`
+ `RF64`
+ `EXTENSIBLE`

### WavSettings
<a name="presets-model-wavsettings"></a>

Required when you set Codec to the value WAV.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 64 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 64. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and so on, up to 64. |
| format | [WavFormat](#presets-model-wavformat) | False | Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 192000 | False | Sample rate in Hz. |

### WebvttAccessibilitySubs
<a name="presets-model-webvttaccessibilitysubs"></a>

If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>.
+ `DISABLED`
+ `ENABLED`

### WebvttDestinationSettings
<a name="presets-model-webvttdestinationsettings"></a>

Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibility | [WebvttAccessibilitySubs](#presets-model-webvttaccessibilitysubs) | False | If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>. |
| stylePassthrough | [WebvttStylePassthrough](#presets-model-webvttstylepassthrough) | False | Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range. |

### WebvttStylePassthrough
<a name="presets-model-webvttstylepassthrough"></a>

Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range.
+ `ENABLED`
+ `DISABLED`
+ `STRICT`
+ `MERGE`

### Xavc4kIntraCbgProfileClass
<a name="presets-model-xavc4kintracbgprofileclass"></a>

Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_100`
+ `CLASS_300`
+ `CLASS_480`

### Xavc4kIntraCbgProfileSettings
<a name="presets-model-xavc4kintracbgprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K\_INTRA\_CBG.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [Xavc4kIntraCbgProfileClass](#presets-model-xavc4kintracbgprofileclass) | False | Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### Xavc4kIntraVbrProfileClass
<a name="presets-model-xavc4kintravbrprofileclass"></a>

Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_100`
+ `CLASS_300`
+ `CLASS_480`

### Xavc4kIntraVbrProfileSettings
<a name="presets-model-xavc4kintravbrprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K\_INTRA\_VBR.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [Xavc4kIntraVbrProfileClass](#presets-model-xavc4kintravbrprofileclass) | False | Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### Xavc4kProfileBitrateClass
<a name="presets-model-xavc4kprofilebitrateclass"></a>

Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `BITRATE_CLASS_100`
+ `BITRATE_CLASS_140`
+ `BITRATE_CLASS_200`

### Xavc4kProfileCodecProfile
<a name="presets-model-xavc4kprofilecodecprofile"></a>

Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH\_422). These profiles are specified in ITU-T H.264.
+ `HIGH`
+ `HIGH_422`

### Xavc4kProfileQualityTuningLevel
<a name="presets-model-xavc4kprofilequalitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### Xavc4kProfileSettings
<a name="presets-model-xavc4kprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrateClass | [Xavc4kProfileBitrateClass](#presets-model-xavc4kprofilebitrateclass) | False | Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |
| codecProfile | [Xavc4kProfileCodecProfile](#presets-model-xavc4kprofilecodecprofile) | False | Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH\_422). These profiles are specified in ITU-T H.264. |
| flickerAdaptiveQuantization | [XavcFlickerAdaptiveQuantization](#presets-model-xavcflickeradaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides. |
| gopBReference | [XavcGopBReference](#presets-model-xavcgopbreference) | False | Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point. |
| qualityTuningLevel | [Xavc4kProfileQualityTuningLevel](#presets-model-xavc4kprofilequalitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| slices | integer<br />Minimum: 8<br />Maximum: 12 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |

### XavcAdaptiveQuantization
<a name="presets-model-xavcadaptivequantization"></a>

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization.
+ `OFF`
+ `AUTO`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### XavcEntropyEncoding
<a name="presets-model-xavcentropyencoding"></a>

Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point.
+ `AUTO`
+ `CABAC`
+ `CAVLC`

### XavcFlickerAdaptiveQuantization
<a name="presets-model-xavcflickeradaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides.
+ `DISABLED`
+ `ENABLED`

### XavcFramerateControl
<a name="presets-model-xavcframeratecontrol"></a>

If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### XavcFramerateConversionAlgorithm
<a name="presets-model-xavcframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### XavcGopBReference
<a name="presets-model-xavcgopbreference"></a>

Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames.
+ `DISABLED`
+ `ENABLED`

### XavcHdIntraCbgProfileClass
<a name="presets-model-xavchdintracbgprofileclass"></a>

Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_50`
+ `CLASS_100`
+ `CLASS_200`

### XavcHdIntraCbgProfileSettings
<a name="presets-model-xavchdintracbgprofilesettings"></a>

Required when you set Profile to the value XAVC\_HD\_INTRA\_CBG.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [XavcHdIntraCbgProfileClass](#presets-model-xavchdintracbgprofileclass) | False | Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### XavcHdProfileBitrateClass
<a name="presets-model-xavchdprofilebitrateclass"></a>

Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `BITRATE_CLASS_25`
+ `BITRATE_CLASS_35`
+ `BITRATE_CLASS_50`

### XavcHdProfileQualityTuningLevel
<a name="presets-model-xavchdprofilequalitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### XavcHdProfileSettings
<a name="presets-model-xavchdprofilesettings"></a>

Required when you set Profile to the value XAVC\_HD.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrateClass | [XavcHdProfileBitrateClass](#presets-model-xavchdprofilebitrateclass) | False | Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |
| flickerAdaptiveQuantization | [XavcFlickerAdaptiveQuantization](#presets-model-xavcflickeradaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides. |
| gopBReference | [XavcGopBReference](#presets-model-xavcgopbreference) | False | Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point. |
| interlaceMode | [XavcInterlaceMode](#presets-model-xavcinterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| qualityTuningLevel | [XavcHdProfileQualityTuningLevel](#presets-model-xavchdprofilequalitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| slices | integer<br />Minimum: 4<br />Maximum: 12 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| telecine | [XavcHdProfileTelecine](#presets-model-xavchdprofiletelecine) | False | Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html. |

### XavcHdProfileTelecine
<a name="presets-model-xavchdprofiletelecine"></a>

Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html.
+ `NONE`
+ `HARD`

### XavcInterlaceMode
<a name="presets-model-xavcinterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### XavcProfile
<a name="presets-model-xavcprofile"></a>

Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC\_HD\_INTRA\_CBG. To create an interlaced XAVC output, choose the profile XAVC\_HD.
+ `XAVC_HD_INTRA_CBG`
+ `XAVC_4K_INTRA_CBG`
+ `XAVC_4K_INTRA_VBR`
+ `XAVC_HD`
+ `XAVC_4K`

### XavcSettings
<a name="presets-model-xavcsettings"></a>

Required when you set Codec to the value XAVC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [XavcAdaptiveQuantization](#presets-model-xavcadaptivequantization) | False | Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization. |
| entropyEncoding | [XavcEntropyEncoding](#presets-model-xavcentropyencoding) | False | Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point. |
| framerateControl | [XavcFramerateControl](#presets-model-xavcframeratecontrol) | False | If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions. |
| framerateConversionAlgorithm | [XavcFramerateConversionAlgorithm](#presets-model-xavcframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Frame rate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| perFrameMetrics | Array of type [frameMetricType](#presets-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| profile | [XavcProfile](#presets-model-xavcprofile) | False | Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC\_HD\_INTRA\_CBG. To create an interlaced XAVC output, choose the profile XAVC\_HD. |
| slowPal | [XavcSlowPal](#presets-model-xavcslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless your downstream workflow requires that you specify it explicitly. Otherwise, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [XavcSpatialAdaptiveQuantization](#presets-model-xavcspatialadaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| temporalAdaptiveQuantization | [XavcTemporalAdaptiveQuantization](#presets-model-xavctemporaladaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization. |
| xavc4kIntraCbgProfileSettings | [Xavc4kIntraCbgProfileSettings](#presets-model-xavc4kintracbgprofilesettings) | False | Required when you set Profile to the value XAVC\_4K\_INTRA\_CBG. |
| xavc4kIntraVbrProfileSettings | [Xavc4kIntraVbrProfileSettings](#presets-model-xavc4kintravbrprofilesettings) | False | Required when you set Profile to the value XAVC\_4K\_INTRA\_VBR. |
| xavc4kProfileSettings | [Xavc4kProfileSettings](#presets-model-xavc4kprofilesettings) | False | Required when you set Profile to the value XAVC\_4K. |
| xavcHdIntraCbgProfileSettings | [XavcHdIntraCbgProfileSettings](#presets-model-xavchdintracbgprofilesettings) | False | Required when you set Profile to the value XAVC\_HD\_INTRA\_CBG. |
| xavcHdProfileSettings | [XavcHdProfileSettings](#presets-model-xavchdprofilesettings) | False | Required when you set Profile to the value XAVC\_HD. |

### XavcSlowPal
<a name="presets-model-xavcslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25.
+ `DISABLED`
+ `ENABLED`

### XavcSpatialAdaptiveQuantization
<a name="presets-model-xavcspatialadaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### XavcTemporalAdaptiveQuantization
<a name="presets-model-xavctemporaladaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### frameMetricType
<a name="presets-model-framemetrictype"></a>

\* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes
+ `PSNR`
+ `SSIM`
+ `MS_SSIM`
+ `PSNR_HVS`
+ `VMAF`
+ `QVBR`
+ `SHOT_CHANGE`

## See also
<a name="presets-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListPresets
<a name="ListPresets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/ListPresets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/ListPresets)

### CreatePreset
<a name="CreatePreset-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/CreatePreset)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/CreatePreset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
