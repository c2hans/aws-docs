---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobsqueries-id.html
---

# JobsQueries id
<a name="jobsqueries-id"></a>

## URI
<a name="jobsqueries-id-url"></a>

`/2017-08-29/jobsQueries/{{id}}`

## HTTP methods
<a name="jobsqueries-id-http-methods"></a>

### GET
<a name="jobsqueries-idget"></a>

**Operation ID:** `GetJobsQueryResults`

Retrieve a JSON array of up to twenty of your most recent jobs matched by a jobs query.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetJobsQueryResultsResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="jobsqueries-idoptions"></a>

Supports CORS preflight requests.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="jobsqueries-id-schemas"></a>

### Request bodies
<a name="jobsqueries-id-request-examples"></a>

#### GET schema
<a name="jobsqueries-id-request-body-get-example"></a>

```
{
  "id": "string"
}
```

### Response bodies
<a name="jobsqueries-id-response-examples"></a>

#### GetJobsQueryResultsResponse schema
<a name="jobsqueries-id-response-body-getjobsqueryresultsresponse-example"></a>

```
{
  "jobs": [
    {
      "arn": "string",
      "id": "string",
      "createdAt": "string",
      "jobTemplate": "string",
      "jobEngineVersionRequested": "string",
      "jobEngineVersionUsed": "string",
      "queue": "string",
      "userMetadata": {
      },
      "role": "string",
      "settings": {
        "timecodeConfig": {
          "anchor": "string",
          "source": enum,
          "start": "string",
          "timestampOffset": "string"
        },
        "outputGroups": [
          {
            "customName": "string",
            "name": "string",
            "outputs": [
              {
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
                "preset": "string",
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
                "outputSettings": {
                  "hlsSettings": {
                    "audioGroupId": "string",
                    "audioRenditionSets": "string",
                    "audioTrackType": enum,
                    "descriptiveVideoServiceFlag": enum,
                    "iFrameOnlyManifest": enum,
                    "segmentModifier": "string",
                    "audioOnlyContainer": enum
                  }
                },
                "extension": "string",
                "nameModifier": "string",
                "captionDescriptions": [
                  {
                    "captionSelectorName": "string",
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
            ],
            "outputGroupSettings": {
              "type": enum,
              "hlsGroupSettings": {
                "targetDurationCompatibilityMode": enum,
                "manifestDurationFormat": enum,
                "segmentLength": integer,
                "segmentLengthControl": enum,
                "timedMetadataId3Period": integer,
                "captionLanguageSetting": enum,
                "captionLanguageMappings": [
                  {
                    "captionChannel": integer,
                    "customLanguageCode": "string",
                    "languageCode": enum,
                    "languageDescription": "string"
                  }
                ],
                "destination": "string",
                "destinationSettings": {
                  "s3Settings": {
                    "encryption": {
                      "encryptionType": enum,
                      "kmsKeyArn": "string",
                      "kmsEncryptionContext": "string"
                    },
                    "accessControl": {
                      "cannedAcl": enum
                    },
                    "storageClass": enum
                  }
                },
                "additionalManifests": [
                  {
                    "manifestNameModifier": "string",
                    "selectedOutputs": [
                      "string"
                    ]
                  }
                ],
                "encryption": {
                  "encryptionMethod": enum,
                  "constantInitializationVector": "string",
                  "initializationVectorInManifest": enum,
                  "offlineEncrypted": enum,
                  "spekeKeyProvider": {
                    "resourceId": "string",
                    "systemIds": [
                      "string"
                    ],
                    "url": "string",
                    "certificateArn": "string",
                    "encryptionContractConfiguration": {
                      "spekeVideoPreset": enum,
                      "spekeAudioPreset": enum
                    }
                  },
                  "staticKeyProvider": {
                    "staticKeyValue": "string",
                    "keyFormat": "string",
                    "keyFormatVersions": "string",
                    "url": "string"
                  },
                  "type": enum
                },
                "timedMetadataId3Frame": enum,
                "baseUrl": "string",
                "codecSpecification": enum,
                "outputSelection": enum,
                "programDateTimePeriod": integer,
                "segmentsPerSubdirectory": integer,
                "minSegmentLength": integer,
                "minFinalSegmentLength": number,
                "directoryStructure": enum,
                "programDateTime": enum,
                "adMarkers": [
                  enum
                ],
                "segmentControl": enum,
                "timestampDeltaMilliseconds": integer,
                "manifestCompression": enum,
                "clientCache": enum,
                "audioOnlyHeader": enum,
                "streamInfResolution": enum,
                "imageBasedTrickPlay": enum,
                "progressiveWriteHlsManifest": enum,
                "imageBasedTrickPlaySettings": {
                  "thumbnailHeight": integer,
                  "thumbnailWidth": integer,
                  "tileHeight": integer,
                  "tileWidth": integer,
                  "intervalCadence": enum,
                  "thumbnailInterval": number
                },
                "captionSegmentLengthControl": enum
              },
              "dashIsoGroupSettings": {
                "audioChannelConfigSchemeIdUri": enum,
                "segmentLength": integer,
                "minFinalSegmentLength": number,
                "segmentLengthControl": enum,
                "destination": "string",
                "destinationSettings": {
                  "s3Settings": {
                    "encryption": {
                      "encryptionType": enum,
                      "kmsKeyArn": "string",
                      "kmsEncryptionContext": "string"
                    },
                    "accessControl": {
                      "cannedAcl": enum
                    },
                    "storageClass": enum
                  }
                },
                "additionalManifests": [
                  {
                    "manifestNameModifier": "string",
                    "selectedOutputs": [
                      "string"
                    ]
                  }
                ],
                "encryption": {
                  "playbackDeviceCompatibility": enum,
                  "spekeKeyProvider": {
                    "resourceId": "string",
                    "systemIds": [
                      "string"
                    ],
                    "url": "string",
                    "certificateArn": "string",
                    "encryptionContractConfiguration": {
                      "spekeVideoPreset": enum,
                      "spekeAudioPreset": enum
                    }
                  }
                },
                "minBufferTime": integer,
                "fragmentLength": integer,
                "baseUrl": "string",
                "segmentControl": enum,
                "ptsOffsetHandlingForBFrames": enum,
                "mpdManifestBandwidthType": enum,
                "mpdProfile": enum,
                "hbbtvCompliance": enum,
                "writeSegmentTimelineInRepresentation": enum,
                "imageBasedTrickPlay": enum,
                "dashIFrameTrickPlayNameModifier": "string",
                "imageBasedTrickPlaySettings": {
                  "thumbnailHeight": integer,
                  "thumbnailWidth": integer,
                  "tileHeight": integer,
                  "tileWidth": integer,
                  "intervalCadence": enum,
                  "thumbnailInterval": number
                },
                "videoCompositionOffsets": enum,
                "dashManifestStyle": enum
              },
              "fileGroupSettings": {
                "destination": "string",
                "destinationSettings": {
                  "s3Settings": {
                    "encryption": {
                      "encryptionType": enum,
                      "kmsKeyArn": "string",
                      "kmsEncryptionContext": "string"
                    },
                    "accessControl": {
                      "cannedAcl": enum
                    },
                    "storageClass": enum
                  }
                }
              },
              "msSmoothGroupSettings": {
                "destination": "string",
                "destinationSettings": {
                  "s3Settings": {
                    "encryption": {
                      "encryptionType": enum,
                      "kmsKeyArn": "string",
                      "kmsEncryptionContext": "string"
                    },
                    "accessControl": {
                      "cannedAcl": enum
                    },
                    "storageClass": enum
                  }
                },
                "additionalManifests": [
                  {
                    "manifestNameModifier": "string",
                    "selectedOutputs": [
                      "string"
                    ]
                  }
                ],
                "fragmentLength": integer,
                "fragmentLengthControl": enum,
                "encryption": {
                  "spekeKeyProvider": {
                    "resourceId": "string",
                    "systemIds": [
                      "string"
                    ],
                    "url": "string",
                    "certificateArn": "string",
                    "encryptionContractConfiguration": {
                      "spekeVideoPreset": enum,
                      "spekeAudioPreset": enum
                    }
                  }
                },
                "manifestEncoding": enum,
                "audioDeduplication": enum
              },
              "cmafGroupSettings": {
                "targetDurationCompatibilityMode": enum,
                "writeHlsManifest": enum,
                "writeDashManifest": enum,
                "segmentLength": integer,
                "segmentLengthControl": enum,
                "minFinalSegmentLength": number,
                "destination": "string",
                "destinationSettings": {
                  "s3Settings": {
                    "encryption": {
                      "encryptionType": enum,
                      "kmsKeyArn": "string",
                      "kmsEncryptionContext": "string"
                    },
                    "accessControl": {
                      "cannedAcl": enum
                    },
                    "storageClass": enum
                  }
                },
                "additionalManifests": [
                  {
                    "manifestNameModifier": "string",
                    "selectedOutputs": [
                      "string"
                    ]
                  }
                ],
                "encryption": {
                  "encryptionMethod": enum,
                  "constantInitializationVector": "string",
                  "initializationVectorInManifest": enum,
                  "spekeKeyProvider": {
                    "resourceId": "string",
                    "hlsSignaledSystemIds": [
                      "string"
                    ],
                    "dashSignaledSystemIds": [
                      "string"
                    ],
                    "url": "string",
                    "certificateArn": "string",
                    "encryptionContractConfiguration": {
                      "spekeVideoPreset": enum,
                      "spekeAudioPreset": enum
                    }
                  },
                  "staticKeyProvider": {
                    "staticKeyValue": "string",
                    "keyFormat": "string",
                    "keyFormatVersions": "string",
                    "url": "string"
                  },
                  "type": enum,
                  "clearLead": enum
                },
                "minBufferTime": integer,
                "fragmentLength": integer,
                "baseUrl": "string",
                "segmentControl": enum,
                "ptsOffsetHandlingForBFrames": enum,
                "mpdManifestBandwidthType": enum,
                "mpdProfile": enum,
                "writeSegmentTimelineInRepresentation": enum,
                "manifestDurationFormat": enum,
                "streamInfResolution": enum,
                "clientCache": enum,
                "manifestCompression": enum,
                "codecSpecification": enum,
                "imageBasedTrickPlay": enum,
                "dashIFrameTrickPlayNameModifier": "string",
                "imageBasedTrickPlaySettings": {
                  "thumbnailHeight": integer,
                  "thumbnailWidth": integer,
                  "tileHeight": integer,
                  "tileWidth": integer,
                  "intervalCadence": enum,
                  "thumbnailInterval": number
                },
                "videoCompositionOffsets": enum,
                "dashManifestStyle": enum
              },
              "perFrameMetrics": [
                enum
              ]
            },
            "automatedEncodingSettings": {
              "abrSettings": {
                "maxQualityLevel": number,
                "maxRenditions": integer,
                "maxAbrBitrate": integer,
                "minAbrBitrate": integer,
                "rules": [
                  {
                    "type": enum,
                    "minTopRenditionSize": {
                      "width": integer,
                      "height": integer
                    },
                    "minBottomRenditionSize": {
                      "width": integer,
                      "height": integer
                    },
                    "forceIncludeRenditions": [
                      {
                        "width": integer,
                        "height": integer
                      }
                    ],
                    "allowedRenditions": [
                      {
                        "width": integer,
                        "height": integer,
                        "required": enum
                      }
                    ]
                  }
                ]
              }
            }
          }
        ],
        "adAvailOffset": integer,
        "availBlanking": {
          "availBlankingImage": "string"
        },
        "followSource": integer,
        "timedMetadataInsertion": {
          "id3Insertions": [
            {
              "timecode": "string",
              "id3": "string"
            }
          ]
        },
        "nielsenConfiguration": {
          "breakoutCode": integer,
          "distributorId": "string"
        },
        "motionImageInserter": {
          "insertionMode": enum,
          "input": "string",
          "offset": {
            "imageX": integer,
            "imageY": integer
          },
          "startTime": "string",
          "playback": enum,
          "framerate": {
            "framerateNumerator": integer,
            "framerateDenominator": integer
          }
        },
        "esam": {
          "signalProcessingNotification": {
            "sccXml": "string"
          },
          "manifestConfirmConditionNotification": {
            "mccXml": "string"
          },
          "responseSignalPreroll": integer
        },
        "nielsenNonLinearWatermark": {
          "sourceId": integer,
          "cbetSourceId": "string",
          "activeWatermarkProcess": enum,
          "assetId": "string",
          "assetName": "string",
          "episodeId": "string",
          "ticServerUrl": "string",
          "metadataDestination": "string",
          "uniqueTicPerAudioTrack": enum,
          "adiFilename": "string",
          "sourceWatermarkStatus": enum
        },
        "kantarWatermark": {
          "credentialsSecretName": "string",
          "channelName": "string",
          "contentReference": "string",
          "kantarServerUrl": "string",
          "kantarLicenseId": integer,
          "logDestination": "string",
          "fileOffset": number,
          "metadata3": "string",
          "metadata4": "string",
          "metadata5": "string",
          "metadata6": "string",
          "metadata7": "string",
          "metadata8": "string"
        },
        "extendedDataServices": {
          "vchipAction": enum,
          "copyProtectionAction": enum
        },
        "colorConversion3DLUTSettings": [
          {
            "inputMasteringLuminance": integer,
            "inputColorSpace": enum,
            "outputMasteringLuminance": integer,
            "outputColorSpace": enum,
            "fileInput": "string"
          }
        ],
        "inputs": [
          {
            "inputClippings": [
              {
                "endTimecode": "string",
                "startTimecode": "string"
              }
            ],
            "audioSelectors": {
            },
            "dynamicAudioSelectors": {
            },
            "audioSelectorGroups": {
            },
            "programNumber": integer,
            "videoSelector": {
              "colorSpace": enum,
              "sampleRange": enum,
              "rotate": enum,
              "pid": integer,
              "programNumber": integer,
              "embeddedTimecodeOverride": enum,
              "alphaBehavior": enum,
              "colorSpaceUsage": enum,
              "padVideo": enum,
              "selectorType": enum,
              "streams": [
                integer
              ],
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
              }
            },
            "filterEnable": enum,
            "psiControl": enum,
            "filterStrength": integer,
            "deblockFilter": enum,
            "denoiseFilter": enum,
            "inputScanType": enum,
            "timecodeSource": enum,
            "timecodeStart": "string",
            "captionSelectors": {
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
            "dolbyVisionMetadataXml": "string",
            "crop": {
              "height": integer,
              "width": integer,
              "x": integer,
              "y": integer
            },
            "position": {
              "height": integer,
              "width": integer,
              "x": integer,
              "y": integer
            },
            "advancedInputFilter": enum,
            "advancedInputFilterSettings": {
              "sharpening": enum,
              "addTexture": enum
            },
            "videoOverlays": [
              {
                "input": {
                  "fileInput": "string",
                  "inputClippings": [
                    {
                      "endTimecode": "string",
                      "startTimecode": "string"
                    }
                  ],
                  "timecodeSource": enum,
                  "timecodeStart": "string",
                  "audioSelectors": {
                  }
                },
                "endTimecode": "string",
                "startTimecode": "string",
                "crop": {
                  "x": integer,
                  "y": integer,
                  "width": integer,
                  "height": integer,
                  "unit": enum
                },
                "initialPosition": {
                  "opacity": integer,
                  "xPosition": integer,
                  "yPosition": integer,
                  "width": integer,
                  "height": integer,
                  "unit": enum
                },
                "playback": enum,
                "transitions": [
                  {
                    "endTimecode": "string",
                    "startTimecode": "string",
                    "endPosition": {
                      "opacity": integer,
                      "xPosition": integer,
                      "yPosition": integer,
                      "width": integer,
                      "height": integer,
                      "unit": enum
                    }
                  }
                ]
              }
            ],
            "multiViewSettings": [
              {
                "input": {
                  "fileInput": "string"
                }
              }
            ],
            "fileInput": "string",
            "videoGenerator": {
              "duration": integer,
              "width": integer,
              "height": integer,
              "framerateNumerator": integer,
              "framerateDenominator": integer,
              "sampleRate": integer,
              "channels": integer,
              "imageInput": "string"
            },
            "decryptionSettings": {
              "decryptionMode": enum,
              "encryptedDecryptionKey": "string",
              "initializationVector": "string",
              "kmsKeyRegion": "string"
            },
            "supplementalImps": [
              "string"
            ],
            "tamsSettings": {
              "sourceId": "string",
              "timerange": "string",
              "gapHandling": enum,
              "authConnectionArn": "string"
            }
          }
        ]
      },
      "status": enum,
      "errorCode": integer,
      "errorMessage": "string",
      "timing": {
        "submitTime": "string",
        "startTime": "string",
        "finishTime": "string"
      },
      "outputGroupDetails": [
        {
          "outputDetails": [
            {
              "durationInMs": integer,
              "videoDetails": {
                "widthInPx": integer,
                "heightInPx": integer
              }
            }
          ]
        }
      ],
      "billingTagsSource": enum,
      "accelerationSettings": {
        "mode": enum
      },
      "statusUpdateInterval": enum,
      "jobPercentComplete": integer,
      "currentPhase": enum,
      "retryCount": integer,
      "priority": integer,
      "simulateReservedQueue": enum,
      "accelerationStatus": enum,
      "messages": {
        "info": [
          "string"
        ],
        "warning": [
          "string"
        ]
      },
      "hopDestinations": [
        {
          "waitMinutes": integer,
          "queue": "string",
          "priority": integer
        }
      ],
      "queueTransitions": [
        {
          "timestamp": "string",
          "sourceQueue": "string",
          "destinationQueue": "string"
        }
      ],
      "clientRequestToken": "string",
      "warnings": [
        {
          "code": integer,
          "count": integer
        }
      ],
      "shareStatus": enum,
      "lastShareDetails": "string",
      "elementalInferenceConfiguration": {
        "features": [
          enum
        ],
        "feeds": [
          {
            "arn": "string",
            "feedManagementState": enum
          }
        ]
      }
    }
  ],
  "status": enum,
  "nextToken": "string"
}
```

#### ExceptionBody schema
<a name="jobsqueries-id-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="jobsqueries-id-properties"></a>

### AacAudioDescriptionBroadcasterMix
<a name="jobsqueries-id-model-aacaudiodescriptionbroadcastermix"></a>

Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
+ `BROADCASTER_MIXED_AD`
+ `NORMAL`

### AacCodecProfile
<a name="jobsqueries-id-model-aaccodecprofile"></a>

Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE.
+ `LC`
+ `HEV1`
+ `HEV2`
+ `XHE`

### AacCodingMode
<a name="jobsqueries-id-model-aaccodingmode"></a>

The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. \* 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. \* 1.0 Mono: One channel, C. \* 2.0 Stereo: Two channels, L, R. \* 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING\_MODE\_AUTO, and the service will automatically choose from one of the coding modes above.
+ `AD_RECEIVER_MIX`
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_5_1`
+ `CODING_MODE_AUTO`

### AacLoudnessMeasurementMode
<a name="jobsqueries-id-model-aacloudnessmeasurementmode"></a>

Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates.
+ `PROGRAM`
+ `ANCHOR`

### AacRateControlMode
<a name="jobsqueries-id-model-aacratecontrolmode"></a>

Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality.
+ `CBR`
+ `VBR`

### AacRawFormat
<a name="jobsqueries-id-model-aacrawformat"></a>

Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container.
+ `LATM_LOAS`
+ `NONE`

### AacSettings
<a name="jobsqueries-id-model-aacsettings"></a>

Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionBroadcasterMix | [AacAudioDescriptionBroadcasterMix](#jobsqueries-id-model-aacaudiodescriptionbroadcastermix) | False | Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType. |
| bitrate | integer<br />Minimum: 6000<br />Maximum: 1024000 | False | Specify the average bitrate in bits per second. The set of valid values for this setting is: 6000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000. The value you set is also constrained by the values that you choose for Profile, Bitrate control mode, and Sample rate. Default values depend on Bitrate control mode and Profile. |
| codecProfile | [AacCodecProfile](#jobsqueries-id-model-aaccodecprofile) | False | Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE. |
| codingMode | [AacCodingMode](#jobsqueries-id-model-aaccodingmode) | False | The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. \* 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. \* 1.0 Mono: One channel, C. \* 2.0 Stereo: Two channels, L, R. \* 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING\_MODE\_AUTO, and the service will automatically choose from one of the coding modes above. |
| loudnessMeasurementMode | [AacLoudnessMeasurementMode](#jobsqueries-id-model-aacloudnessmeasurementmode) | False | Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates. |
| rapInterval | integer<br />Minimum: 2000<br />Maximum: 30000 | False | Specify the RAP (Random Access Point) interval for your xHE-AAC audio output. A RAP allows a decoder to decode audio data mid-stream, without the need to reference previous audio frames, and perform adaptive audio bitrate switching. To specify the RAP interval: Enter an integer from 2000 to 30000, in milliseconds. Smaller values allow for better seeking and more frequent stream switching, while large values improve compression efficiency. To have MediaConvert automatically determine the RAP interval: Leave blank. |
| rateControlMode | [AacRateControlMode](#jobsqueries-id-model-aacratecontrolmode) | False | Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality. |
| rawFormat | [AacRawFormat](#jobsqueries-id-model-aacrawformat) | False | Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 96000 | False | Specify the AAC sample rate in samples per second (Hz). Valid sample rates depend on the AAC profile and Coding mode that you select. For a list of supported sample rates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html |
| specification | [AacSpecification](#jobsqueries-id-model-aacspecification) | False | Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers. |
| targetLoudnessRange | integer<br />Minimum: 6<br />Maximum: 16 | False | Specify the xHE-AAC loudness target. Enter an integer from 6 to 16, representing "loudness units". For more information, see the following specification: Supplementary information for R 128 EBU Tech 3342-2023. |
| vbrQuality | [AacVbrQuality](#jobsqueries-id-model-aacvbrquality) | False | Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html\#aac\_vbr |

### AacSpecification
<a name="jobsqueries-id-model-aacspecification"></a>

Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
+ `MPEG2`
+ `MPEG4`

### AacVbrQuality
<a name="jobsqueries-id-model-aacvbrquality"></a>

Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html\#aac\_vbr
+ `LOW`
+ `MEDIUM_LOW`
+ `MEDIUM_HIGH`
+ `HIGH`

### Ac3BitstreamMode
<a name="jobsqueries-id-model-ac3bitstreammode"></a>

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
<a name="jobsqueries-id-model-ac3codingmode"></a>

Dolby Digital coding mode. Determines number of channels.
+ `CODING_MODE_1_0`
+ `CODING_MODE_1_1`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`
+ `CODING_MODE_AUTO`

### Ac3DynamicRangeCompressionLine
<a name="jobsqueries-id-model-ac3dynamicrangecompressionline"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`
+ `NONE`

### Ac3DynamicRangeCompressionProfile
<a name="jobsqueries-id-model-ac3dynamicrangecompressionprofile"></a>

When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes.
+ `FILM_STANDARD`
+ `NONE`

### Ac3DynamicRangeCompressionRf
<a name="jobsqueries-id-model-ac3dynamicrangecompressionrf"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`
+ `NONE`

### Ac3LfeFilter
<a name="jobsqueries-id-model-ac3lfefilter"></a>

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode.
+ `ENABLED`
+ `DISABLED`

### Ac3MetadataControl
<a name="jobsqueries-id-model-ac3metadatacontrol"></a>

When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Ac3Settings
<a name="jobsqueries-id-model-ac3settings"></a>

Required when you set Codec to the value AC3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 64000<br />Maximum: 640000 | False | Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 64000. Maximum: 128000. Valid bitrates for coding mode 1/1: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 3/2 with FLE: Default: 384000. Minimum: 384000. Maximum: 640000. |
| bitstreamMode | [Ac3BitstreamMode](#jobsqueries-id-model-ac3bitstreammode) | False | Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Ac3CodingMode](#jobsqueries-id-model-ac3codingmode) | False | Dolby Digital coding mode. Determines number of channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through. |
| dynamicRangeCompressionLine | [Ac3DynamicRangeCompressionLine](#jobsqueries-id-model-ac3dynamicrangecompressionline) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionProfile | [Ac3DynamicRangeCompressionProfile](#jobsqueries-id-model-ac3dynamicrangecompressionprofile) | False | When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes. |
| dynamicRangeCompressionRf | [Ac3DynamicRangeCompressionRf](#jobsqueries-id-model-ac3dynamicrangecompressionrf) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| lfeFilter | [Ac3LfeFilter](#jobsqueries-id-model-ac3lfefilter) | False | Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode. |
| metadataControl | [Ac3MetadataControl](#jobsqueries-id-model-ac3metadatacontrol) | False | When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |

### Ac4BitstreamMode
<a name="jobsqueries-id-model-ac4bitstreammode"></a>

Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb\_paec\_ac4\_bed\_classifier in the encoder implementation. - COMPLETE\_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content
+ `COMPLETE_MAIN`
+ `EMERGENCY`

### Ac4CodingMode
<a name="jobsqueries-id-model-ac4codingmode"></a>

Dolby AC-4 coding mode. Determines number of channels. Maps to dlb\_paec\_ac4\_bed\_channel\_config in the encoder implementation. - CODING\_MODE\_2\_0: 2.0 (stereo) - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_20 - CODING\_MODE\_3\_2\_LFE: 5.1 surround - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_51 - CODING\_MODE\_5\_1\_4: 5.1.4 immersive - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_514
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2_LFE`
+ `CODING_MODE_5_1_4`

### Ac4DynamicRangeCompressionDrcProfile
<a name="jobsqueries-id-model-ac4dynamicrangecompressiondrcprofile"></a>

Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Ac4Settings
<a name="jobsqueries-id-model-ac4settings"></a>

Required when you set Codec to the value AC4.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 48000<br />Maximum: 768000 | False | Specify the average bitrate in bits per second. Leave blank to use the default bitrate for the coding mode you select according to ETSI TS 103 190. Valid bitrates for coding mode 2.0 (stereo): 48000, 64000, 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1 (3/2 with LFE): 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1.4 (immersive): 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. |
| bitstreamMode | [Ac4BitstreamMode](#jobsqueries-id-model-ac4bitstreammode) | False | Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb\_paec\_ac4\_bed\_classifier in the encoder implementation. - COMPLETE\_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content |
| codingMode | [Ac4CodingMode](#jobsqueries-id-model-ac4codingmode) | False | Dolby AC-4 coding mode. Determines number of channels. Maps to dlb\_paec\_ac4\_bed\_channel\_config in the encoder implementation. - CODING\_MODE\_2\_0: 2.0 (stereo) - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_20 - CODING\_MODE\_3\_2\_LFE: 5.1 surround - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_51 - CODING\_MODE\_5\_1\_4: 5.1.4 immersive - maps to DLB\_PAEC\_AC4\_BED\_CHANNEL\_CONFIG\_514 |
| dynamicRangeCompressionFlatPanelTv | [Ac4DynamicRangeCompressionDrcProfile](#jobsqueries-id-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionHomeTheater | [Ac4DynamicRangeCompressionDrcProfile](#jobsqueries-id-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionPortableHeadphones | [Ac4DynamicRangeCompressionDrcProfile](#jobsqueries-id-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| dynamicRangeCompressionPortableSpeakers | [Ac4DynamicRangeCompressionDrcProfile](#jobsqueries-id-model-ac4dynamicrangecompressiondrcprofile) | False | Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby AC-4 setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby AC-4 setting: Left only/Right only surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby AC-4 setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -1000.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby AC-4 setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| stereoDownmix | [Ac4StereoDownmix](#jobsqueries-id-model-ac4stereodownmix) | False | Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback. |

### Ac4StereoDownmix
<a name="jobsqueries-id-model-ac4stereodownmix"></a>

Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback.
+ `NOT_INDICATED`
+ `LO_RO`
+ `LT_RT`
+ `DPL2`

### AccelerationMode
<a name="jobsqueries-id-model-accelerationmode"></a>

Specify whether the service runs your job with accelerated transcoding. Choose DISABLED if you don't want accelerated transcoding. Choose ENABLED if you want your job to run with accelerated transcoding and to fail if your input files or your job settings aren't compatible with accelerated transcoding. Choose PREFERRED if you want your job to run with accelerated transcoding if the job is compatible with the feature and to run at standard speed if it's not.
+ `DISABLED`
+ `ENABLED`
+ `PREFERRED`

### AccelerationSettings
<a name="jobsqueries-id-model-accelerationsettings"></a>

Accelerated transcoding can significantly speed up jobs with long, visually complex content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mode | [AccelerationMode](#jobsqueries-id-model-accelerationmode) | True | Specify the conditions when the service will run your job with accelerated transcoding. |

### AccelerationStatus
<a name="jobsqueries-id-model-accelerationstatus"></a>

Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT\_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN\_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings aren't compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT\_ACCELERATED.
+ `NOT_APPLICABLE`
+ `IN_PROGRESS`
+ `ACCELERATED`
+ `NOT_ACCELERATED`

### AdvancedInputFilter
<a name="jobsqueries-id-model-advancedinputfilter"></a>

Use to remove noise, blocking, blurriness, or ringing from your input as a pre-filter step before encoding. The Advanced input filter removes more types of compression artifacts and is an improvement when compared to basic Deblock and Denoise filters. To remove video compression artifacts from your input and improve the video quality: Choose Enabled. Additionally, this filter can help increase the video quality of your output relative to its bitrate, since noisy inputs are more complex and require more bits to encode. To help restore loss of detail after applying the filter, you can optionally add texture or sharpening as an additional step. Jobs that use this feature incur pro-tier pricing. To not apply advanced input filtering: Choose Disabled. Note that you can still apply basic filtering with Deblock and Denoise.
+ `ENABLED`
+ `DISABLED`

### AdvancedInputFilterAddTexture
<a name="jobsqueries-id-model-advancedinputfilteraddtexture"></a>

Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesn't have texture, including screen recordings, computer graphics, or cartoons.
+ `ENABLED`
+ `DISABLED`

### AdvancedInputFilterSettings
<a name="jobsqueries-id-model-advancedinputfiltersettings"></a>

Optional settings for Advanced input filter when you set Advanced input filter to Enabled.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| addTexture | [AdvancedInputFilterAddTexture](#jobsqueries-id-model-advancedinputfilteraddtexture) | False | Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesn't have texture, including screen recordings, computer graphics, or cartoons. |
| sharpening | [AdvancedInputFilterSharpen](#jobsqueries-id-model-advancedinputfiltersharpen) | False | Optionally specify the amount of sharpening to apply when you use the Advanced input filter. Sharpening adds contrast to the edges of your video content and can reduce softness. To apply no sharpening: Keep the default value, Off. To apply a minimal amount of sharpening choose Low, or for the maximum choose High. |

### AdvancedInputFilterSharpen
<a name="jobsqueries-id-model-advancedinputfiltersharpen"></a>

Optionally specify the amount of sharpening to apply when you use the Advanced input filter. Sharpening adds contrast to the edges of your video content and can reduce softness. To apply no sharpening: Keep the default value, Off. To apply a minimal amount of sharpening choose Low, or for the maximum choose High.
+ `OFF`
+ `LOW`
+ `HIGH`

### AfdSignaling
<a name="jobsqueries-id-model-afdsignaling"></a>

This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. \* Choose None to remove all AFD values from this output. \* Choose Fixed to ignore input AFD values and instead encode the value specified in the job. \* Choose Auto to calculate output AFD values based on the input AFD scaler data.
+ `NONE`
+ `AUTO`
+ `FIXED`

### AiffSettings
<a name="jobsqueries-id-model-aiffsettings"></a>

Required when you set Codec to the value AIFF.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 64 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 64. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and so on, up to 64. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 192000 | False | Sample rate in Hz. |

### AllowedRenditionSize
<a name="jobsqueries-id-model-allowedrenditionsize"></a>

Use Allowed renditions to specify a list of possible resolutions in your ABR stack. \* MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. \* Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. \* You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. \* If you specify Allowed renditions, you must not specify a separate rule for Force include renditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this rule. |
| required | [RequiredFlag](#jobsqueries-id-model-requiredflag) | False | Set to ENABLED to force a rendition to be included. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this rule. |

### AlphaBehavior
<a name="jobsqueries-id-model-alphabehavior"></a>

Ignore this setting unless this input is a QuickTime animation with an alpha channel. Use this setting to create separate Key and Fill outputs. In each output, specify which part of the input MediaConvert uses. Leave this setting at the default value DISCARD to delete the alpha channel and preserve the video. Set it to REMAP\_TO\_LUMA to delete the video and map the alpha channel to the luma channel of your outputs.
+ `DISCARD`
+ `REMAP_TO_LUMA`

### AncillaryConvert608To708
<a name="jobsqueries-id-model-ancillaryconvert608to708"></a>

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.
+ `UPCONVERT`
+ `DISABLED`

### AncillarySourceSettings
<a name="jobsqueries-id-model-ancillarysourcesettings"></a>

Settings for ancillary captions source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [AncillaryConvert608To708](#jobsqueries-id-model-ancillaryconvert608to708) | False | Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708. |
| sourceAncillaryChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608 channel number in the ancillary data track from which to extract captions. Unused for passthrough. |
| terminateCaptions | [AncillaryTerminateCaptions](#jobsqueries-id-model-ancillaryterminatecaptions) | False | By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting. |

### AncillaryTerminateCaptions
<a name="jobsqueries-id-model-ancillaryterminatecaptions"></a>

By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting.
+ `END_OF_INPUT`
+ `DISABLED`

### AntiAlias
<a name="jobsqueries-id-model-antialias"></a>

The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting.
+ `DISABLED`
+ `ENABLED`

### AudioChannelTag
<a name="jobsqueries-id-model-audiochanneltag"></a>

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
<a name="jobsqueries-id-model-audiochanneltaggingsettings"></a>

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelTag | [AudioChannelTag](#jobsqueries-id-model-audiochanneltag) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track. |
| channelTags | Array of type [AudioChannelTag](#jobsqueries-id-model-audiochanneltag) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track. |

### AudioCodec
<a name="jobsqueries-id-model-audiocodec"></a>

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
<a name="jobsqueries-id-model-audiocodecsettings"></a>

Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aacSettings | [AacSettings](#jobsqueries-id-model-aacsettings) | False | Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode. |
| ac3Settings | [Ac3Settings](#jobsqueries-id-model-ac3settings) | False | Required when you set Codec to the value AC3. |
| ac4Settings | [Ac4Settings](#jobsqueries-id-model-ac4settings) | False | Required when you set Codec to the value AC4. |
| aiffSettings | [AiffSettings](#jobsqueries-id-model-aiffsettings) | False | Required when you set Codec to the value AIFF. |
| codec | [AudioCodec](#jobsqueries-id-model-audiocodec) | False | Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html\#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html\#audio-only-output |
| eac3AtmosSettings | [Eac3AtmosSettings](#jobsqueries-id-model-eac3atmossettings) | False | Required when you set Codec to the value EAC3\_ATMOS. |
| eac3Settings | [Eac3Settings](#jobsqueries-id-model-eac3settings) | False | Required when you set Codec to the value EAC3. |
| flacSettings | [FlacSettings](#jobsqueries-id-model-flacsettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC. |
| mp2Settings | [Mp2Settings](#jobsqueries-id-model-mp2settings) | False | Required when you set Codec to the value MP2. |
| mp3Settings | [Mp3Settings](#jobsqueries-id-model-mp3settings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3. |
| opusSettings | [OpusSettings](#jobsqueries-id-model-opussettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS. |
| vorbisSettings | [VorbisSettings](#jobsqueries-id-model-vorbissettings) | False | Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis. |
| wavSettings | [WavSettings](#jobsqueries-id-model-wavsettings) | False | Required when you set Codec to the value WAV. |

### AudioDefaultSelection
<a name="jobsqueries-id-model-audiodefaultselection"></a>

Specify a fallback audio selector for this input. Use to ensure outputs have audio even when the audio selector you specify in your output is missing from the source. DEFAULT (Checked in the MediaConvert console): If your output settings specify an audio selector that does not exist in this input, MediaConvert uses this audio selector instead. This is useful when you have multiple inputs with a different number of audio tracks. NOT\_DEFAULT (Unchecked in the MediaConvert console): MediaConvert will not fallback from any missing audio selector. Any output specifying a missing audio selector will be silent.
+ `DEFAULT`
+ `NOT_DEFAULT`

### AudioDescription
<a name="jobsqueries-id-model-audiodescription"></a>

Settings related to one audio tab on the MediaConvert console. In your job JSON, an instance of AudioDescription is equivalent to one audio tab in the console. Usually, one audio tab corresponds to one output audio track. Depending on how you set up your input audio selectors and whether you use audio selector groups, one audio tab can correspond to a group of output audio tracks.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioChannelTaggingSettings | [AudioChannelTaggingSettings](#jobsqueries-id-model-audiochanneltaggingsettings) | False | Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF. |
| audioNormalizationSettings | [AudioNormalizationSettings](#jobsqueries-id-model-audionormalizationsettings) | False | Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard. |
| audioPitchCorrectionSettings | [AudioPitchCorrectionSettings](#jobsqueries-id-model-audiopitchcorrectionsettings) | False | Settings for audio pitch correction during framerate conversion. |
| audioSourceName | string<br />MaxLength: 2048 | False | Specifies which audio data to use from each input. In the simplest case, specify an "Audio Selector":\#inputs-audio\_selector by name based on its order within each input. For example if you specify "Audio Selector 3", then the third audio selector will be used from each input. If an input does not have an "Audio Selector 3", then the audio selector marked as "default" in that input will be used. If there is no audio selector marked as "default", silence will be inserted for the duration of that input. Alternatively, an "Audio Selector Group":\#inputs-audio\_selector\_group name may be specified, with similar default/silence behavior. If no audio\_source\_name is specified, then "Audio Selector 1" will be chosen automatically. |
| audioType | integer<br />Minimum: 0<br />Maximum: 255 | False | Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved. |
| audioTypeControl | [AudioTypeControl](#jobsqueries-id-model-audiotypecontrol) | False | When set to FOLLOW\_INPUT, if the input contains an ISO 639 audio\_type, then that value is passed through to the output. If the input contains no ISO 639 audio\_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER\_MIXED\_AD. |
| codecSettings | [AudioCodecSettings](#jobsqueries-id-model-audiocodecsettings) | False | Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec. |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{2,3}(-[A-Za-z0-9-]+)?$` | False | Specify the language for this audio output track. The service puts this language code into your output audio track when you set Language code control to Use configured. The service also uses your specified custom language code when you set Language code control to Follow input, but your input file doesn't specify a language code. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming. |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Specify the language for your output audio track. To follow the input language: Leave blank. When you do, also set Language code control to Follow input. If no input language is detected MediaConvert will not write an output language code. To follow the input langauge, but fall back to a specified language code if there is no input language to follow: Enter an ISO 639-2 three-letter language code in all capital letters. When you do, also set Language code control to Follow input. To specify the language code: Enter an ISO 639 three-letter language code in all capital letters. When you do, also set Language code control to Use configured. |
| languageCodeControl | [AudioLanguageCodeControl](#jobsqueries-id-model-audiolanguagecodecontrol) | False | Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify. |
| remixSettings | [RemixSettings](#jobsqueries-id-model-remixsettings) | False | Advanced audio remixing settings. |
| streamName | string<br />Pattern: `^[\w\s]*$` | False | Specify a label for this output audio stream. For example, "English", "Director commentary", or "track\_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting. |

### AudioDurationCorrection
<a name="jobsqueries-id-model-audiodurationcorrection"></a>

Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: \* Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. \* Audio track: AAC. Choose from the following audio timing correction settings: \* Disabled (Default): Apply no correction. \* Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. \* Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. \* Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. \* Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your input's STTS table. Your output audio and video may not be aligned or it may contain audio artifacts.
+ `DISABLED`
+ `AUTO`
+ `TRACK`
+ `FRAME`
+ `FORCE`

### AudioLanguageCodeControl
<a name="jobsqueries-id-model-audiolanguagecodecontrol"></a>

Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AudioNormalizationAlgorithm
<a name="jobsqueries-id-model-audionormalizationalgorithm"></a>

Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1.
+ `ITU_BS_1770_1`
+ `ITU_BS_1770_2`
+ `ITU_BS_1770_3`
+ `ITU_BS_1770_4`

### AudioNormalizationAlgorithmControl
<a name="jobsqueries-id-model-audionormalizationalgorithmcontrol"></a>

When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.
+ `CORRECT_AUDIO`
+ `MEASURE_ONLY`

### AudioNormalizationLoudnessLogging
<a name="jobsqueries-id-model-audionormalizationloudnesslogging"></a>

If set to LOG, log each output's audio track loudness to a CSV file.
+ `LOG`
+ `DONT_LOG`

### AudioNormalizationPeakCalculation
<a name="jobsqueries-id-model-audionormalizationpeakcalculation"></a>

If set to TRUE\_PEAK, calculate and log the TruePeak for each output's audio track loudness.
+ `TRUE_PEAK`
+ `NONE`

### AudioNormalizationSettings
<a name="jobsqueries-id-model-audionormalizationsettings"></a>

Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [AudioNormalizationAlgorithm](#jobsqueries-id-model-audionormalizationalgorithm) | False | Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1. |
| algorithmControl | [AudioNormalizationAlgorithmControl](#jobsqueries-id-model-audionormalizationalgorithmcontrol) | False | When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted. |
| correctionGateLevel | integer<br />Minimum: -70<br />Maximum: 0 | False | Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected. |
| loudnessLogging | [AudioNormalizationLoudnessLogging](#jobsqueries-id-model-audionormalizationloudnesslogging) | False | If set to LOG, log each output's audio track loudness to a CSV file. |
| peakCalculation | [AudioNormalizationPeakCalculation](#jobsqueries-id-model-audionormalizationpeakcalculation) | False | If set to TRUE\_PEAK, calculate and log the TruePeak for each output's audio track loudness. |
| targetLkfs | number<br />Format: float<br />Minimum: -59.0<br />Maximum: 0.0 | False | When you use Audio normalization, optionally use this setting to specify a target loudness. If you don't specify a value here, the encoder chooses a value for you, based on the algorithm that you choose for Algorithm. If you choose algorithm 1770-1, the encoder will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS. |
| truePeakLimiterThreshold | number<br />Format: float<br />Minimum: -8.0<br />Maximum: 0.0 | False | Specify the True-peak limiter threshold in decibels relative to full scale (dBFS). The peak inter-audio sample loudness in your output will be limited to the value that you specify, without affecting the overall target LKFS. Enter a value from 0 to -8. Leave blank to use the default value 0. |

### AudioPitchCorrectionSettings
<a name="jobsqueries-id-model-audiopitchcorrectionsettings"></a>

Settings for audio pitch correction during framerate conversion.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| slowPalPitchCorrection | [SlowPalPitchCorrection](#jobsqueries-id-model-slowpalpitchcorrection) | False | Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled. |

### AudioSelector
<a name="jobsqueries-id-model-audioselector"></a>

Use Audio selectors to specify a track or set of tracks from the input that you will use in your outputs. You can use multiple Audio selectors per input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDurationCorrection | [AudioDurationCorrection](#jobsqueries-id-model-audiodurationcorrection) | False | Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: \* Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. \* Audio track: AAC. Choose from the following audio timing correction settings: \* Disabled (Default): Apply no correction. \* Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. \* Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. \* Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. \* Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your input's STTS table. Your output audio and video may not be aligned or it may contain audio artifacts. |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{3}$`<br />MinLength: 3<br />MaxLength: 3 | False | Selects a specific language code from within an audio source, using the ISO 639-2 or ISO 639-3 three-letter language code |
| defaultSelection | [AudioDefaultSelection](#jobsqueries-id-model-audiodefaultselection) | False | Specify a fallback audio selector for this input. Use to ensure outputs have audio even when the audio selector you specify in your output is missing from the source. DEFAULT (Checked in the MediaConvert console): If your output settings specify an audio selector that does not exist in this input, MediaConvert uses this audio selector instead. This is useful when you have multiple inputs with a different number of audio tracks. NOT\_DEFAULT (Unchecked in the MediaConvert console): MediaConvert will not fallback from any missing audio selector. Any output specifying a missing audio selector will be silent. |
| externalAudioFileInput | string<br />Pattern: `^s3://([^\/]+\/+)+((([^\/]*)))\|^https?://[^\/].*[^&]$` | False | Specify the S3, HTTP, or HTTPS URL for your external audio file input. |
| hlsRenditionGroupSettings | [HlsRenditionGroupSettings](#jobsqueries-id-model-hlsrenditiongroupsettings) | False | Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead. |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| offset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647 |
| pids | Array of type integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Selects a specific PID from within an audio source (e.g. 257 selects PID 0x101). |
| programSelection | integer<br />Minimum: 0<br />Maximum: 8 | False | Use this setting for input streams that contain Dolby E, to have the service extract specific program data from the track. To select multiple programs, create multiple selectors with the same Track and different Program numbers. In the console, this setting is visible when you set Selector type to Track. Choose the program number from the dropdown list. If your input file has incorrect metadata, you can choose All channels instead of a program number to have the service ignore the program IDs and include all the programs in the track. |
| remixSettings | [RemixSettings](#jobsqueries-id-model-remixsettings) | False | Use these settings to reorder the audio channels of one input to match those of another input. This allows you to combine the two files into a single output, one after the other. |
| selectorType | [AudioSelectorType](#jobsqueries-id-model-audioselectortype) | False | Specify how MediaConvert selects audio content within your input. The default is Track. PID: Select audio by specifying the Packet Identifier (PID) values for MPEG Transport Stream inputs. Use this when you know the exact PID values of your audio streams. Track: Default. Select audio by track number. This is the most common option and works with most input container formats. If more types of audio data get recognized in the future, these numberings may shift, but the numberings used for Stream mode will not. Language code: Select audio by language using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. Use this when your source has embedded language metadata and you want to select tracks based on their language. HLS rendition group: Select audio from an HLS rendition group. Use this when your input is an HLS package with multiple audio renditions and you want to select specific rendition groups. All PCM: Select all uncompressed PCM audio tracks from your input automatically. This is useful when you want to include all PCM audio tracks without specifying individual track numbers. Stream: Select audio by stream number. Stream numbers include all tracks in the source file, regardless of type, and correspond to either the order of tracks in the file, or if applicable, the stream number metadata of the track. Although all tracks count toward these stream numbers, in this audio selector context, only the stream number of a track containing audio data may be used. If your source file contains a track which is not recognized by the service, then the corresponding stream number will still be reserved for future use. If more types of audio data get recognized in the future, these numberings will not shift. |
| streams | Array of type integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Identify a track from the input audio to include in this selector by entering the stream index number. These numberings count all tracks in the input file, but only a track containing audio data may be used here. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For example, type "1,2,3" to include tracks 1 through 3. |
| tracks | Array of type integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Identify a track from the input audio to include in this selector by entering the track index number. These numberings include only tracks recognized as audio. If the service recognizes more types of audio tracks in the future, these numberings may shift. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For example, type "1,2,3" to include tracks 1 through 3. |

### AudioSelectorGroup
<a name="jobsqueries-id-model-audioselectorgroup"></a>

Use audio selector groups to combine multiple sidecar audio inputs so that you can assign them to a single output audio tab. Note that, if you're working with embedded audio, it's simpler to assign multiple input tracks into a single audio selector rather than use an audio selector group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectorNames | Array of type string<br />MinLength: 1 | False | Name of an Audio Selector within the same input to include in the group. Audio selector names are standardized, based on their order within the input (e.g., "Audio Selector 1"). The audio selector name parameter can be repeated to add any number of audio selectors to the group. |

### AudioSelectorType
<a name="jobsqueries-id-model-audioselectortype"></a>

Specify how MediaConvert selects audio content within your input. The default is Track. PID: Select audio by specifying the Packet Identifier (PID) values for MPEG Transport Stream inputs. Use this when you know the exact PID values of your audio streams. Track: Default. Select audio by track number. This is the most common option and works with most input container formats. If more types of audio data get recognized in the future, these numberings may shift, but the numberings used for Stream mode will not. Language code: Select audio by language using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. Use this when your source has embedded language metadata and you want to select tracks based on their language. HLS rendition group: Select audio from an HLS rendition group. Use this when your input is an HLS package with multiple audio renditions and you want to select specific rendition groups. All PCM: Select all uncompressed PCM audio tracks from your input automatically. This is useful when you want to include all PCM audio tracks without specifying individual track numbers. Stream: Select audio by stream number. Stream numbers include all tracks in the source file, regardless of type, and correspond to either the order of tracks in the file, or if applicable, the stream number metadata of the track. Although all tracks count toward these stream numbers, in this audio selector context, only the stream number of a track containing audio data may be used. If your source file contains a track which is not recognized by the service, then the corresponding stream number will still be reserved for future use. If more types of audio data get recognized in the future, these numberings will not shift.
+ `PID`
+ `TRACK`
+ `LANGUAGE_CODE`
+ `HLS_RENDITION_GROUP`
+ `ALL_PCM`
+ `STREAM`

### AudioTypeControl
<a name="jobsqueries-id-model-audiotypecontrol"></a>

When set to FOLLOW\_INPUT, if the input contains an ISO 639 audio\_type, then that value is passed through to the output. If the input contains no ISO 639 audio\_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER\_MIXED\_AD.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### AutomatedAbrRule
<a name="jobsqueries-id-model-automatedabrrule"></a>

Specify one or more Automated ABR rule types. Note: Force include and Allowed renditions are mutually exclusive.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowedRenditions | Array of type [AllowedRenditionSize](#jobsqueries-id-model-allowedrenditionsize) | False | When customer adds the allowed renditions rule for auto ABR ladder, they are required to add at leat one rendition to allowedRenditions list |
| forceIncludeRenditions | Array of type [ForceIncludeRenditionSize](#jobsqueries-id-model-forceincluderenditionsize) | False | When customer adds the force include renditions rule for auto ABR ladder, they are required to add at leat one rendition to forceIncludeRenditions list |
| minBottomRenditionSize | [MinBottomRenditionSize](#jobsqueries-id-model-minbottomrenditionsize) | False | Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. \* The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. \* If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size. |
| minTopRenditionSize | [MinTopRenditionSize](#jobsqueries-id-model-mintoprenditionsize) | False | Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. \* The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. \* If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution. |
| type | [RuleType](#jobsqueries-id-model-ruletype) | False | Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. \* The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. \* If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution. Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. \* The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. \* If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size. Use Force include renditions to specify one or more resolutions to include your ABR stack. \* (Recommended) To optimize automated ABR, specify as few resolutions as possible. \* (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. \* If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. \* If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. \* If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. \* Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting. Use Allowed renditions to specify a list of possible resolutions in your ABR stack. \* (Required) The number of resolutions that you specify must be equal to, or greater than, the Max renditions setting. \* MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. \* Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. \* You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. \* If you specify Allowed renditions, you must not specify a separate rule for Force include renditions. |

### AutomatedAbrSettings
<a name="jobsqueries-id-model-automatedabrsettings"></a>

Use automated ABR to have MediaConvert set up the renditions in your ABR package for you automatically, based on characteristics of your input video. This feature optimizes video quality while minimizing the overall size of your ABR package.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxAbrBitrate | integer<br />Minimum: 100000<br />Maximum: 100000000 | False | Specify the maximum average bitrate for MediaConvert to use in your automated ABR stack. If you don't specify a value, MediaConvert uses 8,000,000 (8 mb/s) by default. The average bitrate of your highest-quality rendition will be equal to or below this value, depending on the quality, complexity, and resolution of your content. Note that the instantaneous maximum bitrate may vary above the value that you specify. |
| maxQualityLevel | number<br />Format: float<br />Minimum: 1.0<br />Maximum: 10.0 | False | Optional. Specify the QVBR quality level to use for all renditions in your automated ABR stack. To have MediaConvert automatically determine the quality level: Leave blank. To manually specify a quality level: Enter a value from 1 to 10. MediaConvert will use a quality level up to the value that you specify, depending on your source. For more information about QVBR quality levels, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/qvbr-guidelines.html |
| maxRenditions | integer<br />Minimum: 3<br />Maximum: 15 | False | Optional. The maximum number of renditions that MediaConvert will create in your automated ABR stack. The number of renditions is determined automatically, based on analysis of each job, but will never exceed this limit. When you set this to Auto in the console, which is equivalent to excluding it from your JSON job specification, MediaConvert defaults to a limit of 15. |
| minAbrBitrate | integer<br />Minimum: 100000<br />Maximum: 100000000 | False | Specify the minimum average bitrate for MediaConvert to use in your automated ABR stack. If you don't specify a value, MediaConvert uses 600,000 (600 kb/s) by default. The average bitrate of your lowest-quality rendition will be near this value. Note that the instantaneous minimum bitrate may vary below the value that you specify. |
| rules | Array of type [AutomatedAbrRule](#jobsqueries-id-model-automatedabrrule) | False | Optional. Use Automated ABR rules to specify restrictions for the rendition sizes MediaConvert will create in your ABR stack. You can use these rules if your ABR workflow has specific rendition size requirements, but you still want MediaConvert to optimize for video quality and overall file size. |

### AutomatedEncodingSettings
<a name="jobsqueries-id-model-automatedencodingsettings"></a>

Use automated encoding to have MediaConvert choose your encoding settings for you, based on characteristics of your input video.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| abrSettings | [AutomatedAbrSettings](#jobsqueries-id-model-automatedabrsettings) | False | Use automated ABR to have MediaConvert set up the renditions in your ABR package for you automatically, based on characteristics of your input video. This feature optimizes video quality while minimizing the overall size of your ABR package. |

### Av1AdaptiveQuantization
<a name="jobsqueries-id-model-av1adaptivequantization"></a>

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### Av1BitDepth
<a name="jobsqueries-id-model-av1bitdepth"></a>

Specify the Bit depth. You can choose 8-bit or 10-bit.
+ `BIT_8`
+ `BIT_10`

### Av1FilmGrainSynthesis
<a name="jobsqueries-id-model-av1filmgrainsynthesis"></a>

Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor.
+ `DISABLED`
+ `ENABLED`

### Av1FramerateControl
<a name="jobsqueries-id-model-av1frameratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Av1FramerateConversionAlgorithm
<a name="jobsqueries-id-model-av1framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Av1QvbrSettings
<a name="jobsqueries-id-model-av1qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the AV1 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### Av1RateControlMode
<a name="jobsqueries-id-model-av1ratecontrolmode"></a>

'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.'
+ `QVBR`

### Av1Settings
<a name="jobsqueries-id-model-av1settings"></a>

Required when you set Codec, under VideoDescription>CodecSettings to the value AV1.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Av1AdaptiveQuantization](#jobsqueries-id-model-av1adaptivequantization) | False | Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization. |
| bitDepth | [Av1BitDepth](#jobsqueries-id-model-av1bitdepth) | False | Specify the Bit depth. You can choose 8-bit or 10-bit. |
| filmGrainSynthesis | [Av1FilmGrainSynthesis](#jobsqueries-id-model-av1filmgrainsynthesis) | False | Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor. |
| framerateControl | [Av1FramerateControl](#jobsqueries-id-model-av1frameratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Av1FramerateConversionAlgorithm](#jobsqueries-id-model-av1framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Specify the GOP length (keyframe interval) in frames. With AV1, MediaConvert doesn't support GOP length in seconds. This value must be greater than zero and preferably equal to 1 \+ ((numberBFrames \+ 1) \* x), where x is an integer value. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 15 | False | Specify from the number of B-frames, in the range of 0-15. For AV1 encoding, we recommend using 7 or 15. Choose a larger number for a lower bitrate and smaller file size; choose a smaller number for better video quality. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qvbrSettings | [Av1QvbrSettings](#jobsqueries-id-model-av1qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [Av1RateControlMode](#jobsqueries-id-model-av1ratecontrolmode) | False | 'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.' |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Specify the number of slices per picture. This value must be 1, 2, 4, 8, 16, or 32. For progressive pictures, this value must be less than or equal to the number of macroblock rows. For interlaced pictures, this value must be less than or equal to half the number of macroblock rows. |
| spatialAdaptiveQuantization | [Av1SpatialAdaptiveQuantization](#jobsqueries-id-model-av1spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |

### Av1SpatialAdaptiveQuantization
<a name="jobsqueries-id-model-av1spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### AvailBlanking
<a name="jobsqueries-id-model-availblanking"></a>

Use ad avail blanking settings to specify your output content during SCTE-35 triggered ad avails. You can blank your video or overlay it with an image. MediaConvert also removes any audio and embedded captions during the ad avail. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ad-avail-blanking.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availBlankingImage | string<br />Pattern: `^((s3://(.*?)\.(bmp\|BMP\|png\|PNG))\|(https?://(.*?)\.(bmp\|BMP\|png\|PNG)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported. |

### AvcIntraClass
<a name="jobsqueries-id-model-avcintraclass"></a>

Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling.
+ `CLASS_50`
+ `CLASS_100`
+ `CLASS_200`
+ `CLASS_4K_2K`

### AvcIntraFramerateControl
<a name="jobsqueries-id-model-avcintraframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### AvcIntraFramerateConversionAlgorithm
<a name="jobsqueries-id-model-avcintraframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### AvcIntraInterlaceMode
<a name="jobsqueries-id-model-avcintrainterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### AvcIntraScanTypeConversionMode
<a name="jobsqueries-id-model-avcintrascantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### AvcIntraSettings
<a name="jobsqueries-id-model-avcintrasettings"></a>

Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| avcIntraClass | [AvcIntraClass](#jobsqueries-id-model-avcintraclass) | False | Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling. |
| avcIntraUhdSettings | [AvcIntraUhdSettings](#jobsqueries-id-model-avcintrauhdsettings) | False | Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isn't allowed. |
| framerateControl | [AvcIntraFramerateControl](#jobsqueries-id-model-avcintraframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [AvcIntraFramerateConversionAlgorithm](#jobsqueries-id-model-avcintraframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [AvcIntraInterlaceMode](#jobsqueries-id-model-avcintrainterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| scanTypeConversionMode | [AvcIntraScanTypeConversionMode](#jobsqueries-id-model-avcintrascantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [AvcIntraSlowPal](#jobsqueries-id-model-avcintraslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| telecine | [AvcIntraTelecine](#jobsqueries-id-model-avcintratelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### AvcIntraSlowPal
<a name="jobsqueries-id-model-avcintraslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### AvcIntraTelecine
<a name="jobsqueries-id-model-avcintratelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### AvcIntraUhdQualityTuningLevel
<a name="jobsqueries-id-model-avcintrauhdqualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass.
+ `SINGLE_PASS`
+ `MULTI_PASS`

### AvcIntraUhdSettings
<a name="jobsqueries-id-model-avcintrauhdsettings"></a>

Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isn't allowed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| qualityTuningLevel | [AvcIntraUhdQualityTuningLevel](#jobsqueries-id-model-avcintrauhdqualitytuninglevel) | False | Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass. |

### BandwidthReductionFilter
<a name="jobsqueries-id-model-bandwidthreductionfilter"></a>

The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sharpening | [BandwidthReductionFilterSharpening](#jobsqueries-id-model-bandwidthreductionfiltersharpening) | False | Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening. |
| strength | [BandwidthReductionFilterStrength](#jobsqueries-id-model-bandwidthreductionfilterstrength) | False | Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output. |

### BandwidthReductionFilterSharpening
<a name="jobsqueries-id-model-bandwidthreductionfiltersharpening"></a>

Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening.
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `OFF`

### BandwidthReductionFilterStrength
<a name="jobsqueries-id-model-bandwidthreductionfilterstrength"></a>

Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output.
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `AUTO`
+ `OFF`

### BillingTagsSource
<a name="jobsqueries-id-model-billingtagssource"></a>

The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up.
+ `QUEUE`
+ `PRESET`
+ `JOB_TEMPLATE`
+ `JOB`

### BurnInSubtitleStylePassthrough
<a name="jobsqueries-id-model-burninsubtitlestylepassthrough"></a>

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.
+ `ENABLED`
+ `DISABLED`

### BurninDestinationSettings
<a name="jobsqueries-id-model-burnindestinationsettings"></a>

Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [BurninSubtitleAlignment](#jobsqueries-id-model-burninsubtitlealignment) | False | Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. |
| applyFontColor | [BurninSubtitleApplyFontColor](#jobsqueries-id-model-burninsubtitleapplyfontcolor) | False | Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text. |
| backgroundColor | [BurninSubtitleBackgroundColor](#jobsqueries-id-model-burninsubtitlebackgroundcolor) | False | Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions. |
| fallbackFont | [BurninSubtitleFallbackFont](#jobsqueries-id-model-burninsubtitlefallbackfont) | False | Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input. |
| fontColor | [BurninSubtitleFontColor](#jobsqueries-id-model-burninsubtitlefontcolor) | False | Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. |
| fontFileBold | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file. |
| fontFileBoldItalic | string | False | Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file. |
| fontFileItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file. |
| fontFileRegular | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Specify the Font resolution in DPI (dots per inch). |
| fontScript | [FontScript](#jobsqueries-id-model-fontscript) | False | Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese. |
| fontSize | integer<br />Minimum: 0<br />Maximum: 96 | False | Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size. |
| hexFontColor | string<br />Pattern: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`<br />MinLength: 6<br />MaxLength: 8 | False | Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB. |
| outlineColor | [BurninSubtitleOutlineColor](#jobsqueries-id-model-burninsubtitleoutlinecolor) | False | Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present. |
| removeRubyReserveAttributes | [RemoveRubyReserveAttributes](#jobsqueries-id-model-removerubyreserveattributes) | False | Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled. |
| shadowColor | [BurninSubtitleShadowColor](#jobsqueries-id-model-burninsubtitleshadowcolor) | False | Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions. |
| shadowXOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. |
| shadowYOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present. |
| stylePassthrough | [BurnInSubtitleStylePassthrough](#jobsqueries-id-model-burninsubtitlestylepassthrough) | False | To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files. |
| teletextSpacing | [BurninSubtitleTeletextSpacing](#jobsqueries-id-model-burninsubtitleteletextspacing) | False | Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. |
| xPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x\_position is provided, the horizontal caption position will be determined by the alignment parameter. |
| yPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y\_position is provided, the caption will be positioned towards the bottom of the output. |

### BurninSubtitleAlignment
<a name="jobsqueries-id-model-burninsubtitlealignment"></a>

Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates.
+ `CENTERED`
+ `LEFT`
+ `AUTO`

### BurninSubtitleApplyFontColor
<a name="jobsqueries-id-model-burninsubtitleapplyfontcolor"></a>

Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text.
+ `WHITE_TEXT_ONLY`
+ `ALL_TEXT`

### BurninSubtitleBackgroundColor
<a name="jobsqueries-id-model-burninsubtitlebackgroundcolor"></a>

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### BurninSubtitleFallbackFont
<a name="jobsqueries-id-model-burninsubtitlefallbackfont"></a>

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.
+ `BEST_MATCH`
+ `MONOSPACED_SANSSERIF`
+ `MONOSPACED_SERIF`
+ `PROPORTIONAL_SANSSERIF`
+ `PROPORTIONAL_SERIF`

### BurninSubtitleFontColor
<a name="jobsqueries-id-model-burninsubtitlefontcolor"></a>

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
<a name="jobsqueries-id-model-burninsubtitleoutlinecolor"></a>

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present.
+ `BLACK`
+ `WHITE`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `AUTO`

### BurninSubtitleShadowColor
<a name="jobsqueries-id-model-burninsubtitleshadowcolor"></a>

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### BurninSubtitleTeletextSpacing
<a name="jobsqueries-id-model-burninsubtitleteletextspacing"></a>

Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions.
+ `FIXED_GRID`
+ `PROPORTIONAL`
+ `AUTO`

### CaptionDescription
<a name="jobsqueries-id-model-captiondescription"></a>

This object holds groups of settings related to captions for one output. For each output that has captions, include one instance of CaptionDescriptions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionSelectorName | string<br />MinLength: 1 | False | Specifies which "Caption Selector":\#inputs-caption\_selector to use from each input when generating captions. The name should be of the format "Caption Selector <N>", which denotes that the Nth Caption Selector will be used from each input. |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{2,3}(-[A-Za-z-]+)?$` | False | Specify the language for this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information when automatically selecting the font script for rendering the captions text. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming. |
| destinationSettings | [CaptionDestinationSettings](#jobsqueries-id-model-captiondestinationsettings) | False | Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html. |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Specify the language of this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information to choose the font language for rendering the captions text. |
| languageDescription | string | False | Specify a label for this set of output captions. For example, "English", "Director commentary", or "track\_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting. |

### CaptionDestinationSettings
<a name="jobsqueries-id-model-captiondestinationsettings"></a>

Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| burninDestinationSettings | [BurninDestinationSettings](#jobsqueries-id-model-burnindestinationsettings) | False | Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html. |
| destinationType | [CaptionDestinationType](#jobsqueries-id-model-captiondestinationtype) | False | Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html. If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20. |
| dvbSubDestinationSettings | [DvbSubDestinationSettings](#jobsqueries-id-model-dvbsubdestinationsettings) | False | Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html. |
| embeddedDestinationSettings | [EmbeddedDestinationSettings](#jobsqueries-id-model-embeddeddestinationsettings) | False | Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html. |
| imscDestinationSettings | [ImscDestinationSettings](#jobsqueries-id-model-imscdestinationsettings) | False | Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |
| sccDestinationSettings | [SccDestinationSettings](#jobsqueries-id-model-sccdestinationsettings) | False | Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html. |
| srtDestinationSettings | [SrtDestinationSettings](#jobsqueries-id-model-srtdestinationsettings) | False | Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. |
| teletextDestinationSettings | [TeletextDestinationSettings](#jobsqueries-id-model-teletextdestinationsettings) | False | Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html. |
| ttmlDestinationSettings | [TtmlDestinationSettings](#jobsqueries-id-model-ttmldestinationsettings) | False | Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |
| webvttDestinationSettings | [WebvttDestinationSettings](#jobsqueries-id-model-webvttdestinationsettings) | False | Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. |

### CaptionDestinationType
<a name="jobsqueries-id-model-captiondestinationtype"></a>

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

### CaptionSelector
<a name="jobsqueries-id-model-captionselector"></a>

Use captions selectors to specify the captions data from your input that you use in your outputs. You can use up to 100 captions selectors per input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{3}$`<br />MinLength: 3<br />MaxLength: 3 | False | The specific language to extract from source, using the ISO 639-2 or ISO 639-3 three-letter language code. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions. |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | The specific language to extract from source. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions. |
| sourceSettings | [CaptionSourceSettings](#jobsqueries-id-model-captionsourcesettings) | False | If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input captions source file. If your input captions are IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings. |

### CaptionSourceByteRateLimit
<a name="jobsqueries-id-model-captionsourcebyteratelimit"></a>

Choose whether to limit the byte rate at which your SCC input captions are inserted into your output. To not limit the caption rate: We recommend that you keep the default value, Disabled. MediaConvert inserts captions in your output according to the byte rates listed in the EIA-608 specification, typically 2 or 3 caption bytes per frame depending on your output frame rate. To limit your output caption rate: Choose Enabled. Choose this option if your downstream systems require a maximum of 2 caption bytes per frame. Note that this setting has no effect when your output frame rate is 30 or 60.
+ `ENABLED`
+ `DISABLED`

### CaptionSourceConvertPaintOnToPopOn
<a name="jobsqueries-id-model-captionsourceconvertpaintontopopon"></a>

Choose the presentation style of your input SCC captions. To use the same presentation style as your input: Keep the default value, Disabled. To convert paint-on captions to pop-on: Choose Enabled. We also recommend that you choose Enabled if you notice additional repeated lines in your output captions.
+ `ENABLED`
+ `DISABLED`

### CaptionSourceFramerate
<a name="jobsqueries-id-model-captionsourceframerate"></a>

Ignore this setting unless your input captions format is SCC. To have the service compensate for differing frame rates between your input captions and input video, specify the frame rate of the captions file. Specify this value as a fraction. For example, you might specify 24 / 1 for 24 fps, 25 / 1 for 25 fps, 24000 / 1001 for 23.976 fps, or 30000 / 1001 for 29.97 fps.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | Specify the denominator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate numerator. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 60000 | False | Specify the numerator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate denominator. |

### CaptionSourceSettings
<a name="jobsqueries-id-model-captionsourcesettings"></a>

If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input captions source file. If your input captions are IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ancillarySourceSettings | [AncillarySourceSettings](#jobsqueries-id-model-ancillarysourcesettings) | False | Settings for ancillary captions source. |
| dvbSubSourceSettings | [DvbSubSourceSettings](#jobsqueries-id-model-dvbsubsourcesettings) | False | DVB Sub Source Settings |
| embeddedSourceSettings | [EmbeddedSourceSettings](#jobsqueries-id-model-embeddedsourcesettings) | False | Settings for embedded captions Source |
| fileSourceSettings | [FileSourceSettings](#jobsqueries-id-model-filesourcesettings) | False | If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1 in an xml file, specify the URI of the input caption source file. If your caption source is IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings. |
| sourceType | [CaptionSourceType](#jobsqueries-id-model-captionsourcetype) | False | Use Source to identify the format of your input captions. The service cannot auto-detect caption format. |
| teletextSourceSettings | [TeletextSourceSettings](#jobsqueries-id-model-teletextsourcesettings) | False | Settings specific to Teletext caption sources, including Page number. |
| trackSourceSettings | [TrackSourceSettings](#jobsqueries-id-model-tracksourcesettings) | False | Settings specific to caption sources that are specified by track number. Currently, this is only IMSC captions in an IMF package. If your caption source is IMSC 1.1 in a separate xml file, use FileSourceSettings instead of TrackSourceSettings. |
| webvttHlsSourceSettings | [WebvttHlsSourceSettings](#jobsqueries-id-model-webvtthlssourcesettings) | False | Settings specific to WebVTT sources in HLS alternative rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique subtitle track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the specified properties, the job fails. If there is only one subtitle track in the rendition group, the settings can be left empty and the default subtitle track will be chosen. If your caption source is a sidecar file, use FileSourceSettings instead of WebvttHlsSourceSettings. |

### CaptionSourceType
<a name="jobsqueries-id-model-captionsourcetype"></a>

Use Source to identify the format of your input captions. The service cannot auto-detect caption format.
+ `ANCILLARY`
+ `DVB_SUB`
+ `EMBEDDED`
+ `SCTE20`
+ `SCC`
+ `TTML`
+ `STL`
+ `SRT`
+ `SMI`
+ `SMPTE_TT`
+ `TELETEXT`
+ `NULL_SOURCE`
+ `IMSC`
+ `WEBVTT`
+ `TT_3GPP`

### CaptionSourceUpconvertSTLToTeletext
<a name="jobsqueries-id-model-captionsourceupconvertstltoteletext"></a>

Specify whether this set of input captions appears in your outputs in both STL and Teletext format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the STL data through using the Teletext compatibility bytes fields of the Teletext wrapper, and it also translates the STL data into Teletext.
+ `UPCONVERT`
+ `DISABLED`

### ChannelMapping
<a name="jobsqueries-id-model-channelmapping"></a>

Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Don't use both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputChannels | Array of type [OutputChannelMapping](#jobsqueries-id-model-outputchannelmapping) | False | In your JSON job specification, include one child of OutputChannels for each audio channel that you want in your output. Each child should contain one instance of InputChannels or InputChannelsFineTune. |

### ChromaPositionMode
<a name="jobsqueries-id-model-chromapositionmode"></a>

Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left.
+ `AUTO`
+ `FORCE_CENTER`
+ `FORCE_TOP_LEFT`

### ClipLimits
<a name="jobsqueries-id-model-cliplimits"></a>

Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumRGBTolerance | integer<br />Minimum: 90<br />Maximum: 105 | False | Specify the Maximum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the upper tolerance that you specify. Enter an integer from 90 to 105 as an offset percentage to the maximum possible value. Leave blank to use the default value 100. When you specify a value for Maximum RGB tolerance, you must set Sample range conversion to Limited range clip. |
| maximumYUV | integer<br />Minimum: 920<br />Maximum: 1023 | False | Specify the Maximum YUV color sample limit. MediaConvert conforms any pixels in your input above the value that you specify to typical limited range bounds. Enter an integer from 920 to 1023. Leave blank to use the default value 940. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Maximum YUV, you must set Sample range conversion to Limited range clip. |
| minimumRGBTolerance | integer<br />Minimum: -5<br />Maximum: 10 | False | Specify the Minimum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the lower tolerance that you specify. Enter an integer from -5 to 10 as an offset percentage to the minimum possible value. Leave blank to use the default value 0. When you specify a value for Minimum RGB tolerance, you must set Sample range conversion to Limited range clip. |
| minimumYUV | integer<br />Minimum: 0<br />Maximum: 128 | False | Specify the Minimum YUV color sample limit. MediaConvert conforms any pixels in your input below the value that you specify to typical limited range bounds. Enter an integer from 0 to 128. Leave blank to use the default value 64. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Minumum YUV, you must set Sample range conversion to Limited range clip. |

### CmafAdditionalManifest
<a name="jobsqueries-id-model-cmafadditionalmanifest"></a>

Specify the details for each pair of HLS and DASH additional manifests that you want the service to generate for this CMAF output group. Each pair of manifests can reference a different subset of outputs in the group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestNameModifier | string<br />MinLength: 1 | False | Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your HLS group is film-name.m3u8. If you enter "-no-premium" for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.m3u8. For HLS output groups, specify a manifestNameModifier that is different from the nameModifier of the output. The service uses the output name modifier to create unique names for the individual variant manifests. |
| selectedOutputs | Array of type string<br />MinLength: 1 | False | Specify the outputs that you want this additional top-level manifest to reference. |

### CmafClientCache
<a name="jobsqueries-id-model-cmafclientcache"></a>

Disable this setting only when your workflow requires the \#EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header.
+ `DISABLED`
+ `ENABLED`

### CmafCodecSpecification
<a name="jobsqueries-id-model-cmafcodecspecification"></a>

Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
+ `RFC_6381`
+ `RFC_4281`

### CmafEncryptionSettings
<a name="jobsqueries-id-model-cmafencryptionsettings"></a>

Settings for CMAF encryption

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clearLead | [HlsClearLead](#jobsqueries-id-model-hlsclearlead) | False | Enable Clear Lead DRM to reduce video startup latency by leaving the first segment unencrypted while DRM license retrieval occurs in parallel. This optimization allows immediate playback startup while maintaining content protection for the remainder of the stream. When enabled, the first output segment remains fully unencrypted, and encryption begins at the start of the second segment. The HLS manifest will omit \#EXT-X-KEY tags during the clear segment and insert the first \#EXT-X-KEY immediately before the first encrypted fragment. This feature is supported exclusively for CMAF HLS (fMP4) outputs and is compatible with all existing key provider integrations (SPEKE v1, SPEKE v2, and Static Key encryption). Supported codecs: H.264, H.265, and AV1 video codecs, and AAC audio codec. Choose Enabled to activate Clear Lead DRM optimization. Choose Disabled to use standard encryption where all segments are encrypted from the beginning. |
| constantInitializationVector | string<br />Pattern: `^[0-9a-fA-F]{32}$`<br />MinLength: 32<br />MaxLength: 32 | False | This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default. |
| encryptionMethod | [CmafEncryptionType](#jobsqueries-id-model-cmafencryptiontype) | False | Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES\_CTR. |
| initializationVectorInManifest | [CmafInitializationVectorInManifest](#jobsqueries-id-model-cmafinitializationvectorinmanifest) | False | When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests. |
| spekeKeyProvider | [SpekeKeyProviderCmaf](#jobsqueries-id-model-spekekeyprovidercmaf) | False | If your output group type is CMAF, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider settings instead. |
| staticKeyProvider | [StaticKeyProvider](#jobsqueries-id-model-statickeyprovider) | False | Use these settings to set up encryption with a static key provider. |
| type | [CmafKeyProviderType](#jobsqueries-id-model-cmafkeyprovidertype) | False | Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html. |

### CmafEncryptionType
<a name="jobsqueries-id-model-cmafencryptiontype"></a>

Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES\_CTR.
+ `SAMPLE_AES`
+ `AES_CTR`

### CmafGroupSettings
<a name="jobsqueries-id-model-cmafgroupsettings"></a>

Settings related to your CMAF output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalManifests | Array of type [CmafAdditionalManifest](#jobsqueries-id-model-cmafadditionalmanifest) | False | By default, the service creates one top-level .m3u8 HLS manifest and one top -level .mpd DASH manifest for each CMAF output group in your job. These default manifests reference every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here. For each additional manifest that you specify, the service creates one HLS manifest and one DASH manifest. |
| baseUrl | string | False | A partial URI prefix that will be put in the manifest file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file. |
| clientCache | [CmafClientCache](#jobsqueries-id-model-cmafclientcache) | False | Disable this setting only when your workflow requires the \#EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header. |
| codecSpecification | [CmafCodecSpecification](#jobsqueries-id-model-cmafcodecspecification) | False | Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation. |
| dashIFrameTrickPlayNameModifier | string<br />MinLength: 1<br />MaxLength: 256 | False | Specify whether MediaConvert generates I-frame only video segments for DASH trick play, also known as trick mode. When specified, the I-frame only video segments are included within an additional AdaptationSet in your DASH output manifest. To generate I-frame only video segments: Enter a name as a text string, up to 256 character long. This name is appended to the end of this output group's base filename, that you specify as part of your destination URI, and used for the I-frame only video segment files. You may also include format identifiers. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html\#using-settings-variables-with-streaming-outputs To not generate I-frame only video segments: Leave blank. |
| dashManifestStyle | [DashManifestStyle](#jobsqueries-id-model-dashmanifeststyle) | False | Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline for outputs that you also specify a Name modifier for: Keep the default value, Basic. Note that if you do not specify a name modifier for an output, MediaConvert will not write a SegmentTimeline for it. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct. To write a SegmentTimeline in each AdaptationSet: Choose Full. |
| destination | string<br />Pattern: `^s3:\/\/.*$` | False | Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file. |
| destinationSettings | [DestinationSettings](#jobsqueries-id-model-destinationsettings) | False | Settings associated with the destination. Will vary based on the type of destination |
| encryption | [CmafEncryptionSettings](#jobsqueries-id-model-cmafencryptionsettings) | False | DRM settings. |
| fragmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the length, in whole seconds, of the mp4 fragments. When you don't specify a value, MediaConvert defaults to 2. Related setting: Use Fragment length control to specify whether the encoder enforces this value strictly. |
| imageBasedTrickPlay | [CmafImageBasedTrickPlay](#jobsqueries-id-model-cmafimagebasedtrickplay) | False | Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. When you enable Write HLS manifest, MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. When you enable Write DASH manifest, MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md |
| imageBasedTrickPlaySettings | [CmafImageBasedTrickPlaySettings](#jobsqueries-id-model-cmafimagebasedtrickplaysettings) | False | Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED |
| manifestCompression | [CmafManifestCompression](#jobsqueries-id-model-cmafmanifestcompression) | False | When set to GZIP, compresses HLS playlist. |
| manifestDurationFormat | [CmafManifestDurationFormat](#jobsqueries-id-model-cmafmanifestdurationformat) | False | Indicates whether the output manifest should use floating point values for segment duration. |
| minBufferTime | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Minimum time of initially buffered media that is needed to ensure smooth playout. |
| minFinalSegmentLength | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds. |
| mpdManifestBandwidthType | [CmafMpdManifestBandwidthType](#jobsqueries-id-model-cmafmpdmanifestbandwidthtype) | False | Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second. |
| mpdProfile | [CmafMpdProfile](#jobsqueries-id-model-cmafmpdprofile) | False | Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file. |
| ptsOffsetHandlingForBFrames | [CmafPtsOffsetHandlingForBFrames](#jobsqueries-id-model-cmafptsoffsethandlingforbframes) | False | Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here. |
| segmentControl | [CmafSegmentControl](#jobsqueries-id-model-cmafsegmentcontrol) | False | When set to SINGLE\_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED\_FILES, separate segment files will be created. |
| segmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the length, in whole seconds, of each segment. When you don't specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries. |
| segmentLengthControl | [CmafSegmentLengthControl](#jobsqueries-id-model-cmafsegmentlengthcontrol) | False | Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz. |
| streamInfResolution | [CmafStreamInfResolution](#jobsqueries-id-model-cmafstreaminfresolution) | False | Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest. |
| targetDurationCompatibilityMode | [CmafTargetDurationCompatibilityMode](#jobsqueries-id-model-cmaftargetdurationcompatibilitymode) | False | When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\\\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration. |
| videoCompositionOffsets | [CmafVideoCompositionOffsets](#jobsqueries-id-model-cmafvideocompositionoffsets) | False | Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers. |
| writeDashManifest | [CmafWriteDASHManifest](#jobsqueries-id-model-cmafwritedashmanifest) | False | When set to ENABLED, a DASH MPD manifest will be generated for this output. |
| writeHlsManifest | [CmafWriteHLSManifest](#jobsqueries-id-model-cmafwritehlsmanifest) | False | When set to ENABLED, an Apple HLS manifest will be generated for this output. |
| writeSegmentTimelineInRepresentation | [CmafWriteSegmentTimelineInRepresentation](#jobsqueries-id-model-cmafwritesegmenttimelineinrepresentation) | False | When you enable Precise segment duration in DASH manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isn't enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element. |

### CmafImageBasedTrickPlay
<a name="jobsqueries-id-model-cmafimagebasedtrickplay"></a>

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. When you enable Write HLS manifest, MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. When you enable Write DASH manifest, MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md
+ `NONE`
+ `THUMBNAIL`
+ `THUMBNAIL_AND_FULLFRAME`
+ `ADVANCED`

### CmafImageBasedTrickPlaySettings
<a name="jobsqueries-id-model-cmafimagebasedtrickplaysettings"></a>

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| intervalCadence | [CmafIntervalCadence](#jobsqueries-id-model-cmafintervalcadence) | False | The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling. |
| thumbnailHeight | integer<br />Minimum: 2<br />Maximum: 4096 | False | Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2. |
| thumbnailInterval | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesn't align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails. |
| thumbnailWidth | integer<br />Minimum: 8<br />Maximum: 4096 | False | Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8. |
| tileHeight | integer<br />Minimum: 1<br />Maximum: 2048 | False | Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2. |
| tileWidth | integer<br />Minimum: 1<br />Maximum: 512 | False | Number of thumbnails in each row of a tile image. Set a value between 1 and 512. |

### CmafInitializationVectorInManifest
<a name="jobsqueries-id-model-cmafinitializationvectorinmanifest"></a>

When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests.
+ `INCLUDE`
+ `EXCLUDE`

### CmafIntervalCadence
<a name="jobsqueries-id-model-cmafintervalcadence"></a>

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling.
+ `FOLLOW_IFRAME`
+ `FOLLOW_CUSTOM`
+ `FOLLOW_SEGMENTATION`

### CmafKeyProviderType
<a name="jobsqueries-id-model-cmafkeyprovidertype"></a>

Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.
+ `SPEKE`
+ `STATIC_KEY`

### CmafManifestCompression
<a name="jobsqueries-id-model-cmafmanifestcompression"></a>

When set to GZIP, compresses HLS playlist.
+ `GZIP`
+ `NONE`

### CmafManifestDurationFormat
<a name="jobsqueries-id-model-cmafmanifestdurationformat"></a>

Indicates whether the output manifest should use floating point values for segment duration.
+ `FLOATING_POINT`
+ `INTEGER`

### CmafMpdManifestBandwidthType
<a name="jobsqueries-id-model-cmafmpdmanifestbandwidthtype"></a>

Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second.
+ `AVERAGE`
+ `MAX`

### CmafMpdProfile
<a name="jobsqueries-id-model-cmafmpdprofile"></a>

Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file.
+ `MAIN_PROFILE`
+ `ON_DEMAND_PROFILE`

### CmafPtsOffsetHandlingForBFrames
<a name="jobsqueries-id-model-cmafptsoffsethandlingforbframes"></a>

Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here.
+ `ZERO_BASED`
+ `MATCH_INITIAL_PTS`

### CmafSegmentControl
<a name="jobsqueries-id-model-cmafsegmentcontrol"></a>

When set to SINGLE\_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED\_FILES, separate segment files will be created.
+ `SINGLE_FILE`
+ `SEGMENTED_FILES`

### CmafSegmentLengthControl
<a name="jobsqueries-id-model-cmafsegmentlengthcontrol"></a>

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.
+ `EXACT`
+ `GOP_MULTIPLE`
+ `MATCH`

### CmafStreamInfResolution
<a name="jobsqueries-id-model-cmafstreaminfresolution"></a>

Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
+ `INCLUDE`
+ `EXCLUDE`

### CmafTargetDurationCompatibilityMode
<a name="jobsqueries-id-model-cmaftargetdurationcompatibilitymode"></a>

When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\\\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration.
+ `LEGACY`
+ `SPEC_COMPLIANT`

### CmafVideoCompositionOffsets
<a name="jobsqueries-id-model-cmafvideocompositionoffsets"></a>

Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers.
+ `SIGNED`
+ `UNSIGNED`

### CmafWriteDASHManifest
<a name="jobsqueries-id-model-cmafwritedashmanifest"></a>

When set to ENABLED, a DASH MPD manifest will be generated for this output.
+ `DISABLED`
+ `ENABLED`

### CmafWriteHLSManifest
<a name="jobsqueries-id-model-cmafwritehlsmanifest"></a>

When set to ENABLED, an Apple HLS manifest will be generated for this output.
+ `DISABLED`
+ `ENABLED`

### CmafWriteSegmentTimelineInRepresentation
<a name="jobsqueries-id-model-cmafwritesegmenttimelineinrepresentation"></a>

When you enable Precise segment duration in DASH manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isn't enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element.
+ `ENABLED`
+ `DISABLED`

### CmfcAudioDuration
<a name="jobsqueries-id-model-cmfcaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### CmfcAudioTrackType
<a name="jobsqueries-id-model-cmfcaudiotracktype"></a>

Use this setting to control the values that MediaConvert puts in your HLS parent playlist to control how the client player selects which audio track to play. Choose Audio-only variant stream (AUDIO\_ONLY\_VARIANT\_STREAM) for any variant that you want to prohibit the client from playing with video. This causes MediaConvert to represent the variant as an EXT-X-STREAM-INF in the HLS manifest. The other options for this setting determine the values that MediaConvert writes for the DEFAULT and AUTOSELECT attributes of the EXT-X-MEDIA entry for the audio variant. For more information about these attributes, see the Apple documentation article https://developer.apple.com/documentation/http\_live\_streaming/example\_playlists\_for\_http\_live\_streaming/adding\_alternate\_media\_to\_a\_playlist. Choose Alternate audio, auto select, default to set DEFAULT=YES and AUTOSELECT=YES. Choose this value for only one variant in your output group. Choose Alternate audio, auto select, not default to set DEFAULT=NO and AUTOSELECT=YES. Choose Alternate Audio, Not Auto Select to set DEFAULT=NO and AUTOSELECT=NO. When you don't specify a value for this setting, MediaConvert defaults to Alternate audio, auto select, default. When there is more than one variant in your output group, you must explicitly choose a value for this setting.
+ `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
+ `ALTERNATE_AUDIO_AUTO_SELECT`
+ `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
+ `AUDIO_ONLY_VARIANT_STREAM`

### CmfcC2paManifest
<a name="jobsqueries-id-model-cmfcc2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### CmfcDescriptiveVideoServiceFlag
<a name="jobsqueries-id-model-cmfcdescriptivevideoserviceflag"></a>

Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.
+ `DONT_FLAG`
+ `FLAG`

### CmfcIFrameOnlyManifest
<a name="jobsqueries-id-model-cmfciframeonlymanifest"></a>

Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you don't need the I-frame only child manifest, keep the default value Exclude.
+ `INCLUDE`
+ `EXCLUDE`

### CmfcKlvMetadata
<a name="jobsqueries-id-model-cmfcklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### CmfcManifestMetadataSignaling
<a name="jobsqueries-id-model-cmfcmanifestmetadatasignaling"></a>

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.
+ `ENABLED`
+ `DISABLED`

### CmfcScte35Esam
<a name="jobsqueries-id-model-cmfcscte35esam"></a>

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.
+ `INSERT`
+ `NONE`

### CmfcScte35Source
<a name="jobsqueries-id-model-cmfcscte35source"></a>

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output.
+ `PASSTHROUGH`
+ `NONE`

### CmfcSettings
<a name="jobsqueries-id-model-cmfcsettings"></a>

These settings relate to the fragmented MP4 container for the segments in your CMAF outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [CmfcAudioDuration](#jobsqueries-id-model-cmfcaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioGroupId | string | False | Specify the audio rendition group for this audio rendition. Specify up to one value for each audio output in your output group. This value appears in your HLS parent manifest in the EXT-X-MEDIA tag of TYPE=AUDIO, as the value for the GROUP-ID attribute. For example, if you specify "audio\_aac\_1" for Audio group ID, it appears in your manifest like this: \#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio\_aac\_1". Related setting: To associate the rendition group that this audio track belongs to with a video rendition, include the same value that you provide here for that video output's setting Audio rendition sets. |
| audioRenditionSets | string | False | List the audio rendition groups that you want included with this video rendition. Use a comma-separated list. For example, say you want to include the audio rendition groups that have the audio group IDs "audio\_aac\_1" and "audio\_dolby". Then you would specify this value: "audio\_aac\_1,audio\_dolby". Related setting: The rendition groups that you include in your comma-separated list should all match values that you specify in the setting Audio group ID for audio renditions in the same output group as this video rendition. Default behavior: If you don't specify anything here and for Audio group ID, MediaConvert puts each audio variant in its own audio rendition group and associates it with every video variant. Each value in your list appears in your HLS parent manifest in the EXT-X-STREAM-INF tag as the value for the AUDIO attribute. To continue the previous example, say that the file name for the child manifest for your video rendition is "amazing\_video\_1.m3u8". Then, in your parent manifest, each value will appear on separate lines, like this: \#EXT-X-STREAM-INF:AUDIO="audio\_aac\_1"... amazing\_video\_1.m3u8 \#EXT-X-STREAM-INF:AUDIO="audio\_dolby"... amazing\_video\_1.m3u8 |
| audioTrackType | [CmfcAudioTrackType](#jobsqueries-id-model-cmfcaudiotracktype) | False | Use this setting to control the values that MediaConvert puts in your HLS parent playlist to control how the client player selects which audio track to play. Choose Audio-only variant stream (AUDIO\_ONLY\_VARIANT\_STREAM) for any variant that you want to prohibit the client from playing with video. This causes MediaConvert to represent the variant as an EXT-X-STREAM-INF in the HLS manifest. The other options for this setting determine the values that MediaConvert writes for the DEFAULT and AUTOSELECT attributes of the EXT-X-MEDIA entry for the audio variant. For more information about these attributes, see the Apple documentation article https://developer.apple.com/documentation/http\_live\_streaming/example\_playlists\_for\_http\_live\_streaming/adding\_alternate\_media\_to\_a\_playlist. Choose Alternate audio, auto select, default to set DEFAULT=YES and AUTOSELECT=YES. Choose this value for only one variant in your output group. Choose Alternate audio, auto select, not default to set DEFAULT=NO and AUTOSELECT=YES. Choose Alternate Audio, Not Auto Select to set DEFAULT=NO and AUTOSELECT=NO. When you don't specify a value for this setting, MediaConvert defaults to Alternate audio, auto select, default. When there is more than one variant in your output group, you must explicitly choose a value for this setting. |
| c2paManifest | [CmfcC2paManifest](#jobsqueries-id-model-cmfcc2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| descriptiveVideoServiceFlag | [CmfcDescriptiveVideoServiceFlag](#jobsqueries-id-model-cmfcdescriptivevideoserviceflag) | False | Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation. |
| iFrameOnlyManifest | [CmfcIFrameOnlyManifest](#jobsqueries-id-model-cmfciframeonlymanifest) | False | Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you don't need the I-frame only child manifest, keep the default value Exclude. |
| klvMetadata | [CmfcKlvMetadata](#jobsqueries-id-model-cmfcklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| manifestMetadataSignaling | [CmfcManifestMetadataSignaling](#jobsqueries-id-model-cmfcmanifestmetadatasignaling) | False | To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough. |
| scte35Esam | [CmfcScte35Esam](#jobsqueries-id-model-cmfcscte35esam) | False | Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Source | [CmfcScte35Source](#jobsqueries-id-model-cmfcscte35source) | False | Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |
| timedMetadata | [CmfcTimedMetadata](#jobsqueries-id-model-cmfctimedmetadata) | False | To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank. |
| timedMetadataBoxVersion | [CmfcTimedMetadataBoxVersion](#jobsqueries-id-model-cmfctimedmetadataboxversion) | False | Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough. |
| timedMetadataSchemeIdUri | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: https://aomedia.org/emsg/ID3 When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough. |
| timedMetadataValue | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough. |

### CmfcTimedMetadata
<a name="jobsqueries-id-model-cmfctimedmetadata"></a>

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### CmfcTimedMetadataBoxVersion
<a name="jobsqueries-id-model-cmfctimedmetadataboxversion"></a>

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.
+ `VERSION_0`
+ `VERSION_1`

### ColorConversion3DLUTSetting
<a name="jobsqueries-id-model-colorconversion3dlutsetting"></a>

Custom 3D lut settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileInput | string<br />Pattern: `^((s3://(.*?)\.(cube\|CUBE))\|(https?://(.*?)\.(cube\|CUBE)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Specify the input file S3, HTTP, or HTTPS URL for your 3D LUT .cube file. Note that MediaConvert accepts 3D LUT files up to 8MB in size. |
| inputColorSpace | [ColorSpace](#jobsqueries-id-model-colorspace) | False | Specify which inputs use this 3D LUT, according to their color space. |
| inputMasteringLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify which inputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) inputs with a specific mastering luminance: Enter an integer from 0 to 2147483647, corresponding to the input's Maximum luminance value. To apply this 3D LUT to any input regardless of its luminance: Leave blank, or enter 0. |
| outputColorSpace | [ColorSpace](#jobsqueries-id-model-colorspace) | False | Specify which outputs use this 3D LUT, according to their color space. |
| outputMasteringLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify which outputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) outputs with a specific luminance: Enter an integer from 0 to 2147483647, corresponding to the output's luminance. To apply this 3D LUT to any output regardless of its luminance: Leave blank, or enter 0. |

### ColorCorrector
<a name="jobsqueries-id-model-colorcorrector"></a>

Settings for color correction.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brightness | integer<br />Minimum: 1<br />Maximum: 100 | False | Brightness level. |
| clipLimits | [ClipLimits](#jobsqueries-id-model-cliplimits) | False | Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip. |
| colorSpaceConversion | [ColorSpaceConversion](#jobsqueries-id-model-colorspaceconversion) | False | Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesn't upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709 |
| contrast | integer<br />Minimum: 1<br />Maximum: 100 | False | Contrast level. |
| hdr10Metadata | [Hdr10Metadata](#jobsqueries-id-model-hdr10metadata) | False | Use these settings when you convert to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering Display Color Volume static metadata that you want signaled in the output. These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator. When you set Color space conversion to HDR 10, these settings are required. You must set values for Max frame average light level and Max content light level; these settings don't have a default value. The default values for the other HDR 10 metadata settings are defined by the P3D65 color space. For more information about MediaConvert HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. |
| hdrToSdrToneMapper | [HDRToSDRToneMapper](#jobsqueries-id-model-hdrtosdrtonemapper) | False | Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR. |
| hue | integer<br />Minimum: -180<br />Maximum: 180 | False | Hue in degrees. |
| maxLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits. |
| sampleRangeConversion | [SampleRangeConversion](#jobsqueries-id-model-samplerangeconversion) | False | Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output. |
| saturation | integer<br />Minimum: 1<br />Maximum: 100 | False | Saturation level. |
| sdrReferenceWhiteLevel | integer<br />Minimum: 100<br />Maximum: 1000 | False | Specify the reference white level, in nits, for all of your SDR inputs. Use to correct brightness levels within HDR10 outputs. The following color metadata must be present in your SDR input: color primaries, transfer characteristics, and matrix coefficients. If your SDR input has missing color metadata, or if you want to correct input color metadata, manually specify a color space in the input video selector. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000. |

### ColorMetadata
<a name="jobsqueries-id-model-colormetadata"></a>

Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default.
+ `IGNORE`
+ `INSERT`

### ColorSpace
<a name="jobsqueries-id-model-colorspace"></a>

If your input video has accurate color space metadata, or if you don't know about color space: Keep the default value, Follow. MediaConvert will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or has missing metadata: Specify the accurate color space here. If your input video is HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata isn't present in your video stream, or if that metadata is present but not accurate: Choose Force HDR 10. Specify correct values in the input HDR 10 metadata settings. For more information about HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. When you specify an input color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709
+ `FOLLOW`
+ `REC_601`
+ `REC_709`
+ `HDR10`
+ `HLG_2020`
+ `P3DCI`
+ `P3D65_SDR`
+ `P3D65_HDR`

### ColorSpaceConversion
<a name="jobsqueries-id-model-colorspaceconversion"></a>

Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesn't upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709
+ `NONE`
+ `FORCE_601`
+ `FORCE_709`
+ `FORCE_HDR10`
+ `FORCE_HLG_2020`
+ `FORCE_P3DCI`
+ `FORCE_P3D65_SDR`
+ `FORCE_P3D65_HDR`

### ColorSpaceUsage
<a name="jobsqueries-id-model-colorspaceusage"></a>

There are two sources for color metadata, the input file and the job input settings Color space and HDR master display information settings. The Color space usage setting determines which takes precedence. Choose Force to use color metadata from the input job settings. If you don't specify values for those settings, the service defaults to using metadata from your input. FALLBACK - Choose Fallback to use color metadata from the source when it is present. If there's no color metadata in your input file, the service defaults to using values you specify in the input settings.
+ `FORCE`
+ `FALLBACK`

### ContainerSettings
<a name="jobsqueries-id-model-containersettings"></a>

Container specific settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cmfcSettings | [CmfcSettings](#jobsqueries-id-model-cmfcsettings) | False | These settings relate to the fragmented MP4 container for the segments in your CMAF outputs. |
| container | [ContainerType](#jobsqueries-id-model-containertype) | False | Container for this output. Some containers require a container settings object. If not specified, the default object will be created. |
| f4vSettings | [F4vSettings](#jobsqueries-id-model-f4vsettings) | False | Settings for F4v container |
| m2tsSettings | [M2tsSettings](#jobsqueries-id-model-m2tssettings) | False | MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset. |
| m3u8Settings | [M3u8Settings](#jobsqueries-id-model-m3u8settings) | False | These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs. |
| movSettings | [MovSettings](#jobsqueries-id-model-movsettings) | False | These settings relate to your QuickTime MOV output container. |
| mp4Settings | [Mp4Settings](#jobsqueries-id-model-mp4settings) | False | These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html\#output-codecs-and-containers-supported-for-audio-only. |
| mpdSettings | [MpdSettings](#jobsqueries-id-model-mpdsettings) | False | These settings relate to the fragmented MP4 container for the segments in your DASH outputs. |
| mxfSettings | [MxfSettings](#jobsqueries-id-model-mxfsettings) | False | These settings relate to your MXF output container. |

### ContainerType
<a name="jobsqueries-id-model-containertype"></a>

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

### CopyProtectionAction
<a name="jobsqueries-id-model-copyprotectionaction"></a>

The action to take on copy and redistribution control XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions.
+ `PASSTHROUGH`
+ `STRIP`

### DashAdditionalManifest
<a name="jobsqueries-id-model-dashadditionalmanifest"></a>

Specify the details for each additional DASH manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestNameModifier | string<br />MinLength: 1 | False | Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your DASH group is film-name.mpd. If you enter "-no-premium" for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.mpd. |
| selectedOutputs | Array of type string<br />MinLength: 1 | False | Specify the outputs that you want this additional top-level manifest to reference. |

### DashIsoEncryptionSettings
<a name="jobsqueries-id-model-dashisoencryptionsettings"></a>

Specifies DRM settings for DASH outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| playbackDeviceCompatibility | [DashIsoPlaybackDeviceCompatibility](#jobsqueries-id-model-dashisoplaybackdevicecompatibility) | False | This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1. If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted. |
| spekeKeyProvider | [SpekeKeyProvider](#jobsqueries-id-model-spekekeyprovider) | False | If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead. |

### DashIsoGroupAudioChannelConfigSchemeIdUri
<a name="jobsqueries-id-model-dashisogroupaudiochannelconfigschemeiduri"></a>

Use this setting only when your audio codec is a Dolby one (AC3, EAC3, or Atmos) and your downstream workflow requires that your DASH manifest use the Dolby channel configuration tag, rather than the MPEG one. For example, you might need to use this to make dynamic ad insertion work. Specify which audio channel configuration scheme ID URI MediaConvert writes in your DASH manifest. Keep the default value, MPEG channel configuration, to have MediaConvert write this: urn:mpeg:mpegB:cicp:ChannelConfiguration. Choose Dolby channel configuration to have MediaConvert write this instead: tag:dolby.com,2014:dash:audio\_channel\_configuration:2011.
+ `MPEG_CHANNEL_CONFIGURATION`
+ `DOLBY_CHANNEL_CONFIGURATION`

### DashIsoGroupSettings
<a name="jobsqueries-id-model-dashisogroupsettings"></a>

Settings related to your DASH output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalManifests | Array of type [DashAdditionalManifest](#jobsqueries-id-model-dashadditionalmanifest) | False | By default, the service creates one .mpd DASH manifest for each DASH ISO output group in your job. This default manifest references every output in the output group. To create additional DASH manifests that reference a subset of the outputs in the output group, specify a list of them here. |
| audioChannelConfigSchemeIdUri | [DashIsoGroupAudioChannelConfigSchemeIdUri](#jobsqueries-id-model-dashisogroupaudiochannelconfigschemeiduri) | False | Use this setting only when your audio codec is a Dolby one (AC3, EAC3, or Atmos) and your downstream workflow requires that your DASH manifest use the Dolby channel configuration tag, rather than the MPEG one. For example, you might need to use this to make dynamic ad insertion work. Specify which audio channel configuration scheme ID URI MediaConvert writes in your DASH manifest. Keep the default value, MPEG channel configuration, to have MediaConvert write this: urn:mpeg:mpegB:cicp:ChannelConfiguration. Choose Dolby channel configuration to have MediaConvert write this instead: tag:dolby.com,2014:dash:audio\_channel\_configuration:2011. |
| baseUrl | string | False | A partial URI prefix that will be put in the manifest (.mpd) file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file. |
| dashIFrameTrickPlayNameModifier | string<br />MinLength: 1<br />MaxLength: 256 | False | Specify whether MediaConvert generates I-frame only video segments for DASH trick play, also known as trick mode. When specified, the I-frame only video segments are included within an additional AdaptationSet in your DASH output manifest. To generate I-frame only video segments: Enter a name as a text string, up to 256 character long. This name is appended to the end of this output group's base filename, that you specify as part of your destination URI, and used for the I-frame only video segment files. You may also include format identifiers. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html\#using-settings-variables-with-streaming-outputs To not generate I-frame only video segments: Leave blank. |
| dashManifestStyle | [DashManifestStyle](#jobsqueries-id-model-dashmanifeststyle) | False | Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline for outputs that you also specify a Name modifier for: Keep the default value, Basic. Note that if you do not specify a name modifier for an output, MediaConvert will not write a SegmentTimeline for it. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct. To write a SegmentTimeline in each AdaptationSet: Choose Full. |
| destination | string<br />Pattern: `^s3:\/\/.*$` | False | Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file. |
| destinationSettings | [DestinationSettings](#jobsqueries-id-model-destinationsettings) | False | Settings associated with the destination. Will vary based on the type of destination |
| encryption | [DashIsoEncryptionSettings](#jobsqueries-id-model-dashisoencryptionsettings) | False | DRM settings. |
| fragmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types. |
| hbbtvCompliance | [DashIsoHbbtvCompliance](#jobsqueries-id-model-dashisohbbtvcompliance) | False | Supports HbbTV specification as indicated |
| imageBasedTrickPlay | [DashIsoImageBasedTrickPlay](#jobsqueries-id-model-dashisoimagebasedtrickplay) | False | Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md |
| imageBasedTrickPlaySettings | [DashIsoImageBasedTrickPlaySettings](#jobsqueries-id-model-dashisoimagebasedtrickplaysettings) | False | Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED |
| minBufferTime | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Minimum time of initially buffered media that is needed to ensure smooth playout. |
| minFinalSegmentLength | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds. |
| mpdManifestBandwidthType | [DashIsoMpdManifestBandwidthType](#jobsqueries-id-model-dashisompdmanifestbandwidthtype) | False | Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second. |
| mpdProfile | [DashIsoMpdProfile](#jobsqueries-id-model-dashisompdprofile) | False | Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file. |
| ptsOffsetHandlingForBFrames | [DashIsoPtsOffsetHandlingForBFrames](#jobsqueries-id-model-dashisoptsoffsethandlingforbframes) | False | Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here. |
| segmentControl | [DashIsoSegmentControl](#jobsqueries-id-model-dashisosegmentcontrol) | False | When set to SINGLE\_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED\_FILES, separate segment files will be created. |
| segmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the length, in whole seconds, of each segment. When you don't specify a value, MediaConvert defaults to 30. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries. |
| segmentLengthControl | [DashIsoSegmentLengthControl](#jobsqueries-id-model-dashisosegmentlengthcontrol) | False | Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz. |
| videoCompositionOffsets | [DashIsoVideoCompositionOffsets](#jobsqueries-id-model-dashisovideocompositionoffsets) | False | Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers. |
| writeSegmentTimelineInRepresentation | [DashIsoWriteSegmentTimelineInRepresentation](#jobsqueries-id-model-dashisowritesegmenttimelineinrepresentation) | False | If you get an HTTP error in the 400 range when you play back your DASH output, enable this setting and run your transcoding job again. When you enable this setting, the service writes precise segment durations in the DASH manifest. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When you don't enable this setting, the service writes approximate segment durations in your DASH manifest. |

### DashIsoHbbtvCompliance
<a name="jobsqueries-id-model-dashisohbbtvcompliance"></a>

Supports HbbTV specification as indicated
+ `HBBTV_1_5`
+ `NONE`

### DashIsoImageBasedTrickPlay
<a name="jobsqueries-id-model-dashisoimagebasedtrickplay"></a>

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md
+ `NONE`
+ `THUMBNAIL`
+ `THUMBNAIL_AND_FULLFRAME`
+ `ADVANCED`

### DashIsoImageBasedTrickPlaySettings
<a name="jobsqueries-id-model-dashisoimagebasedtrickplaysettings"></a>

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| intervalCadence | [DashIsoIntervalCadence](#jobsqueries-id-model-dashisointervalcadence) | False | The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling. |
| thumbnailHeight | integer<br />Minimum: 1<br />Maximum: 4096 | False | Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2. |
| thumbnailInterval | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesn't align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails. |
| thumbnailWidth | integer<br />Minimum: 8<br />Maximum: 4096 | False | Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8. |
| tileHeight | integer<br />Minimum: 1<br />Maximum: 2048 | False | Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2. |
| tileWidth | integer<br />Minimum: 1<br />Maximum: 512 | False | Number of thumbnails in each row of a tile image. Set a value between 1 and 512. |

### DashIsoIntervalCadence
<a name="jobsqueries-id-model-dashisointervalcadence"></a>

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling.
+ `FOLLOW_IFRAME`
+ `FOLLOW_CUSTOM`
+ `FOLLOW_SEGMENTATION`

### DashIsoMpdManifestBandwidthType
<a name="jobsqueries-id-model-dashisompdmanifestbandwidthtype"></a>

Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second.
+ `AVERAGE`
+ `MAX`

### DashIsoMpdProfile
<a name="jobsqueries-id-model-dashisompdprofile"></a>

Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH manifest. When you choose On-demand, the service signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file.
+ `MAIN_PROFILE`
+ `ON_DEMAND_PROFILE`

### DashIsoPlaybackDeviceCompatibility
<a name="jobsqueries-id-model-dashisoplaybackdevicecompatibility"></a>

This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1. If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted.
+ `CENC_V1`
+ `UNENCRYPTED_SEI`

### DashIsoPtsOffsetHandlingForBFrames
<a name="jobsqueries-id-model-dashisoptsoffsethandlingforbframes"></a>

Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here.
+ `ZERO_BASED`
+ `MATCH_INITIAL_PTS`

### DashIsoSegmentControl
<a name="jobsqueries-id-model-dashisosegmentcontrol"></a>

When set to SINGLE\_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED\_FILES, separate segment files will be created.
+ `SINGLE_FILE`
+ `SEGMENTED_FILES`

### DashIsoSegmentLengthControl
<a name="jobsqueries-id-model-dashisosegmentlengthcontrol"></a>

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.
+ `EXACT`
+ `GOP_MULTIPLE`
+ `MATCH`

### DashIsoVideoCompositionOffsets
<a name="jobsqueries-id-model-dashisovideocompositionoffsets"></a>

Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers.
+ `SIGNED`
+ `UNSIGNED`

### DashIsoWriteSegmentTimelineInRepresentation
<a name="jobsqueries-id-model-dashisowritesegmenttimelineinrepresentation"></a>

When you enable Precise segment duration in manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isn't enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element.
+ `ENABLED`
+ `DISABLED`

### DashManifestStyle
<a name="jobsqueries-id-model-dashmanifeststyle"></a>

Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline for outputs that you also specify a Name modifier for: Keep the default value, Basic. Note that if you do not specify a name modifier for an output, MediaConvert will not write a SegmentTimeline for it. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct. To write a SegmentTimeline in each AdaptationSet: Choose Full.
+ `BASIC`
+ `COMPACT`
+ `DISTINCT`
+ `FULL`

### DecryptionMode
<a name="jobsqueries-id-model-decryptionmode"></a>

Specify the encryption mode that you used to encrypt your input files.
+ `AES_CTR`
+ `AES_CBC`
+ `AES_GCM`

### DeinterlaceAlgorithm
<a name="jobsqueries-id-model-deinterlacealgorithm"></a>

Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output.
+ `INTERPOLATE`
+ `INTERPOLATE_TICKER`
+ `BLEND`
+ `BLEND_TICKER`
+ `LINEAR_INTERPOLATION`

### Deinterlacer
<a name="jobsqueries-id-model-deinterlacer"></a>

Settings for deinterlacer

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [DeinterlaceAlgorithm](#jobsqueries-id-model-deinterlacealgorithm) | False | Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output. |
| control | [DeinterlacerControl](#jobsqueries-id-model-deinterlacercontrol) | False | - When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE\_ALL\_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video. |
| mode | [DeinterlacerMode](#jobsqueries-id-model-deinterlacermode) | False | Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive. |

### DeinterlacerControl
<a name="jobsqueries-id-model-deinterlacercontrol"></a>

- When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE\_ALL\_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.
+ `FORCE_ALL_FRAMES`
+ `NORMAL`

### DeinterlacerMode
<a name="jobsqueries-id-model-deinterlacermode"></a>

Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.
+ `DEINTERLACE`
+ `INVERSE_TELECINE`
+ `ADAPTIVE`

### DestinationSettings
<a name="jobsqueries-id-model-destinationsettings"></a>

Settings associated with the destination. Will vary based on the type of destination

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| s3Settings | [S3DestinationSettings](#jobsqueries-id-model-s3destinationsettings) | False | Settings associated with S3 destination |

### DolbyVision
<a name="jobsqueries-id-model-dolbyvision"></a>

Create Dolby Vision Profile 5 or Profile 8.1 compatible video output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| compatibility | [DolbyVisionCompatibility](#jobsqueries-id-model-dolbyvisioncompatibility) | False | When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL\_CODECS property. |
| l6Metadata | [DolbyVisionLevel6Metadata](#jobsqueries-id-model-dolbyvisionlevel6metadata) | False | Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values. |
| l6Mode | [DolbyVisionLevel6Mode](#jobsqueries-id-model-dolbyvisionlevel6mode) | False | Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies. |
| mapping | [DolbyVisionMapping](#jobsqueries-id-model-dolbyvisionmapping) | False | Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims. |
| profile | [DolbyVisionProfile](#jobsqueries-id-model-dolbyvisionprofile) | False | Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata. |

### DolbyVisionCompatibility
<a name="jobsqueries-id-model-dolbyvisioncompatibility"></a>

When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL\_CODECS property.
+ `DUPLICATE_STREAM`
+ `SUPPLEMENTAL_CODECS`

### DolbyVisionLevel6Metadata
<a name="jobsqueries-id-model-dolbyvisionlevel6metadata"></a>

Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxCll | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum Content Light Level. Static HDR metadata that corresponds to the brightest pixel in the entire stream. Measured in nits. |
| maxFall | integer<br />Minimum: 0<br />Maximum: 65535 | False | Maximum Frame-Average Light Level. Static HDR metadata that corresponds to the highest frame-average brightness in the entire stream. Measured in nits. |

### DolbyVisionLevel6Mode
<a name="jobsqueries-id-model-dolbyvisionlevel6mode"></a>

Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies.
+ `PASSTHROUGH`
+ `RECALCULATE`
+ `SPECIFY`

### DolbyVisionMapping
<a name="jobsqueries-id-model-dolbyvisionmapping"></a>

Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims.
+ `HDR10_NOMAP`
+ `HDR10_1000`

### DolbyVisionProfile
<a name="jobsqueries-id-model-dolbyvisionprofile"></a>

Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata.
+ `PROFILE_5`
+ `PROFILE_8_1`

### DropFrameTimecode
<a name="jobsqueries-id-model-dropframetimecode"></a>

Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled.
+ `DISABLED`
+ `ENABLED`

### DvbNitSettings
<a name="jobsqueries-id-model-dvbnitsettings"></a>

Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The numeric value placed in the Network Information Table (NIT). |
| networkName | string<br />MinLength: 1<br />MaxLength: 256 | False | The network name text placed in the network\_name\_descriptor inside the Network Information Table. Maximum length is 256 characters. |
| nitInterval | integer<br />Minimum: 25<br />Maximum: 10000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbSdtSettings
<a name="jobsqueries-id-model-dvbsdtsettings"></a>

Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputSdt | [OutputSdt](#jobsqueries-id-model-outputsdt) | False | Selects method of inserting SDT information into output stream. "Follow input SDT" copies SDT information from input stream to output stream. "Follow input SDT if present" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter "SDT Manually" means user will enter the SDT information. "No SDT" means output stream will not contain SDT information. |
| sdtInterval | integer<br />Minimum: 25<br />Maximum: 2000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| serviceName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service name placed in the service\_descriptor in the Service Description Table. Maximum length is 256 characters. |
| serviceProviderName | string<br />MinLength: 1<br />MaxLength: 256 | False | The service provider name placed in the service\_descriptor in the Service Description Table. Maximum length is 256 characters. |

### DvbSubDestinationSettings
<a name="jobsqueries-id-model-dvbsubdestinationsettings"></a>

Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alignment | [DvbSubtitleAlignment](#jobsqueries-id-model-dvbsubtitlealignment) | False | Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical. |
| applyFontColor | [DvbSubtitleApplyFontColor](#jobsqueries-id-model-dvbsubtitleapplyfontcolor) | False | Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text. |
| backgroundColor | [DvbSubtitleBackgroundColor](#jobsqueries-id-model-dvbsubtitlebackgroundcolor) | False | Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present. |
| backgroundOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| ddsHandling | [DvbddsHandling](#jobsqueries-id-model-dvbddshandling) | False | Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn't include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match. To include the DDS, with optimized subtitle placement and reduced data overhead: We recommend that you choose Specified (optimal). This option provides the same visual positioning as Specified while using less bandwidth. This also supports resolutions higher than 1080p while maintaining full DVB-Sub compatibility. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. |
| ddsXCoordinate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Use this setting, along with DDS y-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the left side of the frame and the left side of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment. All burn-in and DVB-Sub font settings must match. |
| ddsYCoordinate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Use this setting, along with DDS x-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the top of the frame and the top of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment (PCS). All burn-in and DVB-Sub font settings must match. |
| fallbackFont | [DvbSubSubtitleFallbackFont](#jobsqueries-id-model-dvbsubsubtitlefallbackfont) | False | Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input. |
| fontColor | [DvbSubtitleFontColor](#jobsqueries-id-model-dvbsubtitlefontcolor) | False | Specify the color of the captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontFileBold | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file. |
| fontFileBoldItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file. |
| fontFileItalic | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file. |
| fontFileRegular | string<br />Pattern: `^((s3://(.*?)\.(ttf))\|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$` | False | Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file. |
| fontOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontResolution | integer<br />Minimum: 96<br />Maximum: 600 | False | Specify the Font resolution in DPI (dots per inch). Within your job settings, all of your DVB-Sub settings must be identical. |
| fontScript | [FontScript](#jobsqueries-id-model-fontscript) | False | Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese. Within your job settings, all of your DVB-Sub settings must be identical. |
| fontSize | integer<br />Minimum: 0<br />Maximum: 96 | False | Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size. Within your job settings, all of your DVB-Sub settings must be identical. |
| height | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the height, in pixels, of this set of DVB-Sub captions. The default value is 576 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match. |
| hexFontColor | string<br />Pattern: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`<br />MinLength: 6<br />MaxLength: 8 | False | Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB. |
| outlineColor | [DvbSubtitleOutlineColor](#jobsqueries-id-model-dvbsubtitleoutlinecolor) | False | Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| outlineSize | integer<br />Minimum: 0<br />Maximum: 10 | False | Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowColor | [DvbSubtitleShadowColor](#jobsqueries-id-model-dvbsubtitleshadowcolor) | False | Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowOpacity | integer<br />Minimum: 0<br />Maximum: 255 | False | Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowXOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. Within your job settings, all of your DVB-Sub settings must be identical. |
| shadowYOffset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical. |
| stylePassthrough | [DvbSubtitleStylePassthrough](#jobsqueries-id-model-dvbsubtitlestylepassthrough) | False | To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files. |
| subtitlingType | [DvbSubtitlingType](#jobsqueries-id-model-dvbsubtitlingtype) | False | Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue. |
| teletextSpacing | [DvbSubtitleTeletextSpacing](#jobsqueries-id-model-dvbsubtitleteletextspacing) | False | Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical. |
| width | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the width, in pixels, of this set of DVB-Sub captions. The default value is 720 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match. |
| xPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x\_position is provided, the horizontal caption position will be determined by the alignment parameter. Within your job settings, all of your DVB-Sub settings must be identical. |
| yPosition | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y\_position is provided, the caption will be positioned towards the bottom of the output. Within your job settings, all of your DVB-Sub settings must be identical. |

### DvbSubSourceSettings
<a name="jobsqueries-id-model-dvbsubsourcesettings"></a>

DVB Sub Source Settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pid | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When using DVB-Sub with Burn-in, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors. |

### DvbSubSubtitleFallbackFont
<a name="jobsqueries-id-model-dvbsubsubtitlefallbackfont"></a>

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.
+ `BEST_MATCH`
+ `MONOSPACED_SANSSERIF`
+ `MONOSPACED_SERIF`
+ `PROPORTIONAL_SANSSERIF`
+ `PROPORTIONAL_SERIF`

### DvbSubtitleAlignment
<a name="jobsqueries-id-model-dvbsubtitlealignment"></a>

Specify the alignment of your captions. If no explicit x\_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical.
+ `CENTERED`
+ `LEFT`
+ `AUTO`

### DvbSubtitleApplyFontColor
<a name="jobsqueries-id-model-dvbsubtitleapplyfontcolor"></a>

Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL\_TEXT, your font color setting applies to all of your output captions text.
+ `WHITE_TEXT_ONLY`
+ `ALL_TEXT`

### DvbSubtitleBackgroundColor
<a name="jobsqueries-id-model-dvbsubtitlebackgroundcolor"></a>

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### DvbSubtitleFontColor
<a name="jobsqueries-id-model-dvbsubtitlefontcolor"></a>

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
<a name="jobsqueries-id-model-dvbsubtitleoutlinecolor"></a>

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.
+ `BLACK`
+ `WHITE`
+ `YELLOW`
+ `RED`
+ `GREEN`
+ `BLUE`
+ `AUTO`

### DvbSubtitleShadowColor
<a name="jobsqueries-id-model-dvbsubtitleshadowcolor"></a>

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.
+ `NONE`
+ `BLACK`
+ `WHITE`
+ `AUTO`

### DvbSubtitleStylePassthrough
<a name="jobsqueries-id-model-dvbsubtitlestylepassthrough"></a>

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.
+ `ENABLED`
+ `DISABLED`

### DvbSubtitleTeletextSpacing
<a name="jobsqueries-id-model-dvbsubtitleteletextspacing"></a>

Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical.
+ `FIXED_GRID`
+ `PROPORTIONAL`
+ `AUTO`

### DvbSubtitlingType
<a name="jobsqueries-id-model-dvbsubtitlingtype"></a>

Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue.
+ `HEARING_IMPAIRED`
+ `STANDARD`

### DvbTdtSettings
<a name="jobsqueries-id-model-dvbtdtsettings"></a>

Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tdtInterval | integer<br />Minimum: 1000<br />Maximum: 30000 | False | The number of milliseconds between instances of this table in the output transport stream. |

### DvbddsHandling
<a name="jobsqueries-id-model-dvbddshandling"></a>

Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn't include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match. To include the DDS, with optimized subtitle placement and reduced data overhead: We recommend that you choose Specified (optimal). This option provides the same visual positioning as Specified while using less bandwidth. This also supports resolutions higher than 1080p while maintaining full DVB-Sub compatibility. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate.
+ `NONE`
+ `SPECIFIED`
+ `NO_DISPLAY_WINDOW`
+ `SPECIFIED_OPTIMAL`

### DynamicAudioSelector
<a name="jobsqueries-id-model-dynamicaudioselector"></a>

Use Dynamic audio selectors when you do not know the track layout of your source when you submit your job, but want to select multiple audio tracks. When you include an audio track in your output and specify this Dynamic audio selector as the Audio source, MediaConvert creates an audio track within that output for each dynamically selected track. Note that when you include a Dynamic audio selector for two or more inputs, each input must have the same number of audio tracks and audio channels.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDurationCorrection | [AudioDurationCorrection](#jobsqueries-id-model-audiodurationcorrection) | False | Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: \* Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. \* Audio track: AAC. Choose from the following audio timing correction settings: \* Disabled (Default): Apply no correction. \* Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. \* Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. \* Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. \* Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your input's STTS table. Your output audio and video may not be aligned or it may contain audio artifacts. |
| externalAudioFileInput | string<br />Pattern: `^s3://([^\/]+\/+)+((([^\/]*)))\|^https?://[^\/].*[^&]$` | False | Specify the S3, HTTP, or HTTPS URL for your external audio file input. |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| offset | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647 |
| selectorType | [DynamicAudioSelectorType](#jobsqueries-id-model-dynamicaudioselectortype) | False | Specify which audio tracks to dynamically select from your source. To select all audio tracks: Keep the default value, All tracks. To select all audio tracks with a specific language code: Choose Language code. When you do, you must also specify a language code under the Language code setting. If there is no matching Language code in your source, then no track will be selected. |

### DynamicAudioSelectorType
<a name="jobsqueries-id-model-dynamicaudioselectortype"></a>

Specify which audio tracks to dynamically select from your source. To select all audio tracks: Keep the default value, All tracks. To select all audio tracks with a specific language code: Choose Language code. When you do, you must also specify a language code under the Language code setting. If there is no matching Language code in your source, then no track will be selected.
+ `ALL_TRACKS`
+ `LANGUAGE_CODE`

### Eac3AtmosBitstreamMode
<a name="jobsqueries-id-model-eac3atmosbitstreammode"></a>

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).
+ `COMPLETE_MAIN`

### Eac3AtmosCodingMode
<a name="jobsqueries-id-model-eac3atmoscodingmode"></a>

The coding mode for Dolby Digital Plus JOC (Atmos).
+ `CODING_MODE_AUTO`
+ `CODING_MODE_5_1_4`
+ `CODING_MODE_7_1_4`
+ `CODING_MODE_9_1_6`

### Eac3AtmosDialogueIntelligence
<a name="jobsqueries-id-model-eac3atmosdialogueintelligence"></a>

Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis.
+ `ENABLED`
+ `DISABLED`

### Eac3AtmosDownmixControl
<a name="jobsqueries-id-model-eac3atmosdownmixcontrol"></a>

Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings.
+ `SPECIFIED`
+ `INITIALIZE_FROM_SOURCE`

### Eac3AtmosDynamicRangeCompressionLine
<a name="jobsqueries-id-model-eac3atmosdynamicrangecompressionline"></a>

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3AtmosDynamicRangeCompressionRf
<a name="jobsqueries-id-model-eac3atmosdynamicrangecompressionrf"></a>

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3AtmosDynamicRangeControl
<a name="jobsqueries-id-model-eac3atmosdynamicrangecontrol"></a>

Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings.
+ `SPECIFIED`
+ `INITIALIZE_FROM_SOURCE`

### Eac3AtmosMeteringMode
<a name="jobsqueries-id-model-eac3atmosmeteringmode"></a>

Choose how the service meters the loudness of your audio.
+ `LEQ_A`
+ `ITU_BS_1770_1`
+ `ITU_BS_1770_2`
+ `ITU_BS_1770_3`
+ `ITU_BS_1770_4`

### Eac3AtmosSettings
<a name="jobsqueries-id-model-eac3atmossettings"></a>

Required when you set Codec to the value EAC3\_ATMOS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 384000<br />Maximum: 1024000 | False | Specify the average bitrate for this output in bits per second. Valid values: 384k, 448k, 576k, 640k, 768k, 1024k Default value: 448k Note that MediaConvert supports 384k only with channel-based immersive (CBI) 7.1.4 and 5.1.4 inputs. For CBI 9.1.6 and other input types, MediaConvert automatically increases your output bitrate to 448k. |
| bitstreamMode | [Eac3AtmosBitstreamMode](#jobsqueries-id-model-eac3atmosbitstreammode) | False | Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Eac3AtmosCodingMode](#jobsqueries-id-model-eac3atmoscodingmode) | False | The coding mode for Dolby Digital Plus JOC (Atmos). |
| dialogueIntelligence | [Eac3AtmosDialogueIntelligence](#jobsqueries-id-model-eac3atmosdialogueintelligence) | False | Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis. |
| downmixControl | [Eac3AtmosDownmixControl](#jobsqueries-id-model-eac3atmosdownmixcontrol) | False | Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings. |
| dynamicRangeCompressionLine | [Eac3AtmosDynamicRangeCompressionLine](#jobsqueries-id-model-eac3atmosdynamicrangecompressionline) | False | Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionRf | [Eac3AtmosDynamicRangeCompressionRf](#jobsqueries-id-model-eac3atmosdynamicrangecompressionrf) | False | Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeControl | [Eac3AtmosDynamicRangeControl](#jobsqueries-id-model-eac3atmosdynamicrangecontrol) | False | Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -6.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Atmos setting: Left only/Right only center mix (Lo/Ro center). MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Atmos setting: Left only/Right only. MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -6.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Atmos setting: Left total/Right total center mix (Lt/Rt center). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Atmos setting: Left total/Right total surround mix (Lt/Rt surround). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, the service ignores Left total/Right total surround. |
| meteringMode | [Eac3AtmosMeteringMode](#jobsqueries-id-model-eac3atmosmeteringmode) | False | Choose how the service meters the loudness of your audio. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| speechThreshold | integer<br />Minimum: 0<br />Maximum: 100 | False | Specify the percentage of audio content, from 0% to 100%, that must be speech in order for the encoder to use the measured speech loudness as the overall program loudness. Default value: 15% |
| stereoDownmix | [Eac3AtmosStereoDownmix](#jobsqueries-id-model-eac3atmosstereodownmix) | False | Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix. |
| surroundExMode | [Eac3AtmosSurroundExMode](#jobsqueries-id-model-eac3atmossurroundexmode) | False | Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels. |

### Eac3AtmosStereoDownmix
<a name="jobsqueries-id-model-eac3atmosstereodownmix"></a>

Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix.
+ `NOT_INDICATED`
+ `STEREO`
+ `SURROUND`
+ `DPL2`

### Eac3AtmosSurroundExMode
<a name="jobsqueries-id-model-eac3atmossurroundexmode"></a>

Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### Eac3AttenuationControl
<a name="jobsqueries-id-model-eac3attenuationcontrol"></a>

If set to ATTENUATE\_3\_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
+ `ATTENUATE_3_DB`
+ `NONE`

### Eac3BitstreamMode
<a name="jobsqueries-id-model-eac3bitstreammode"></a>

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).
+ `COMPLETE_MAIN`
+ `COMMENTARY`
+ `EMERGENCY`
+ `HEARING_IMPAIRED`
+ `VISUALLY_IMPAIRED`

### Eac3CodingMode
<a name="jobsqueries-id-model-eac3codingmode"></a>

Dolby Digital Plus coding mode. Determines number of channels.
+ `CODING_MODE_1_0`
+ `CODING_MODE_2_0`
+ `CODING_MODE_3_2`
+ `CODING_MODE_AUTO`

### Eac3DcFilter
<a name="jobsqueries-id-model-eac3dcfilter"></a>

Activates a DC highpass filter for all input channels.
+ `ENABLED`
+ `DISABLED`

### Eac3DynamicRangeCompressionLine
<a name="jobsqueries-id-model-eac3dynamicrangecompressionline"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3DynamicRangeCompressionRf
<a name="jobsqueries-id-model-eac3dynamicrangecompressionrf"></a>

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf.
+ `NONE`
+ `FILM_STANDARD`
+ `FILM_LIGHT`
+ `MUSIC_STANDARD`
+ `MUSIC_LIGHT`
+ `SPEECH`

### Eac3LfeControl
<a name="jobsqueries-id-model-eac3lfecontrol"></a>

When encoding 3/2 audio, controls whether the LFE channel is enabled
+ `LFE`
+ `NO_LFE`

### Eac3LfeFilter
<a name="jobsqueries-id-model-eac3lfefilter"></a>

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode.
+ `ENABLED`
+ `DISABLED`

### Eac3MetadataControl
<a name="jobsqueries-id-model-eac3metadatacontrol"></a>

When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
+ `FOLLOW_INPUT`
+ `USE_CONFIGURED`

### Eac3PassthroughControl
<a name="jobsqueries-id-model-eac3passthroughcontrol"></a>

When set to WHEN\_POSSIBLE, input DD\+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding.
+ `WHEN_POSSIBLE`
+ `NO_PASSTHROUGH`

### Eac3PhaseControl
<a name="jobsqueries-id-model-eac3phasecontrol"></a>

Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.
+ `SHIFT_90_DEGREES`
+ `NO_SHIFT`

### Eac3Settings
<a name="jobsqueries-id-model-eac3settings"></a>

Required when you set Codec to the value EAC3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attenuationControl | [Eac3AttenuationControl](#jobsqueries-id-model-eac3attenuationcontrol) | False | If set to ATTENUATE\_3\_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode. |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 3024000 | False | Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 32000. Maximum: 3024000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 96000. Maximum: 3024000. Valid bitrates for coding mode 3/2: Default: 384000. Minimum: 192000. Maximum: 3024000. |
| bitstreamMode | [Eac3BitstreamMode](#jobsqueries-id-model-eac3bitstreammode) | False | Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E). |
| codingMode | [Eac3CodingMode](#jobsqueries-id-model-eac3codingmode) | False | Dolby Digital Plus coding mode. Determines number of channels. |
| dcFilter | [Eac3DcFilter](#jobsqueries-id-model-eac3dcfilter) | False | Activates a DC highpass filter for all input channels. |
| dialnorm | integer<br />Minimum: 1<br />Maximum: 31 | False | Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through. |
| dynamicRangeCompressionLine | [Eac3DynamicRangeCompressionLine](#jobsqueries-id-model-eac3dynamicrangecompressionline) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| dynamicRangeCompressionRf | [Eac3DynamicRangeCompressionRf](#jobsqueries-id-model-eac3dynamicrangecompressionrf) | False | Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf. |
| lfeControl | [Eac3LfeControl](#jobsqueries-id-model-eac3lfecontrol) | False | When encoding 3/2 audio, controls whether the LFE channel is enabled |
| lfeFilter | [Eac3LfeFilter](#jobsqueries-id-model-eac3lfefilter) | False | Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3\_2\_LFE coding mode. |
| loRoCenterMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Digital Plus setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center. |
| loRoSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Digital Plus setting: Left only/Right only. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround. |
| ltRtCenterMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: 3.0 | False | Specify a value for the following Dolby Digital Plus setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center. |
| ltRtSurroundMixLevel | number<br />Format: float<br />Minimum: -60.0<br />Maximum: -1.5 | False | Specify a value for the following Dolby Digital Plus setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround. |
| metadataControl | [Eac3MetadataControl](#jobsqueries-id-model-eac3metadatacontrol) | False | When set to FOLLOW\_INPUT, encoder metadata will be sourced from the DD, DD\+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used. |
| passthroughControl | [Eac3PassthroughControl](#jobsqueries-id-model-eac3passthroughcontrol) | False | When set to WHEN\_POSSIBLE, input DD\+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD\+ and non-DD\+ content will have a consistent DD\+ output as the system alternates between passthrough and encoding. |
| phaseControl | [Eac3PhaseControl](#jobsqueries-id-model-eac3phasecontrol) | False | Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode. |
| sampleRate | integer<br />Minimum: 48000<br />Maximum: 48000 | False | This value is always 48000. It represents the sample rate in Hz. |
| stereoDownmix | [Eac3StereoDownmix](#jobsqueries-id-model-eac3stereodownmix) | False | Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix. |
| surroundExMode | [Eac3SurroundExMode](#jobsqueries-id-model-eac3surroundexmode) | False | When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels. |
| surroundMode | [Eac3SurroundMode](#jobsqueries-id-model-eac3surroundmode) | False | When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels. |

### Eac3StereoDownmix
<a name="jobsqueries-id-model-eac3stereodownmix"></a>

Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix.
+ `NOT_INDICATED`
+ `LO_RO`
+ `LT_RT`
+ `DPL2`

### Eac3SurroundExMode
<a name="jobsqueries-id-model-eac3surroundexmode"></a>

When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### Eac3SurroundMode
<a name="jobsqueries-id-model-eac3surroundmode"></a>

When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
+ `NOT_INDICATED`
+ `ENABLED`
+ `DISABLED`

### ElementalInferenceConfiguration
<a name="jobsqueries-id-model-elementalinferenceconfiguration"></a>

Elemental Inference features used in this job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| features | Array of type [ElementalInferenceFeature](#jobsqueries-id-model-elementalinferencefeature) | False | A list of Elemental Inference features used in this job. |
| feeds | Array of type [ElementalInferenceFeed](#jobsqueries-id-model-elementalinferencefeed) | False | A list of Elemental Inference feeds used by this job. |

### ElementalInferenceFeature
<a name="jobsqueries-id-model-elementalinferencefeature"></a>

Elemental Inference feature.
+ `SMART_CROP`

### ElementalInferenceFeed
<a name="jobsqueries-id-model-elementalinferencefeed"></a>

Elemental Inference Feed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Feed ARN. |
| feedManagementState | [ElementalInferenceFeedManagementState](#jobsqueries-id-model-elementalinferencefeedmanagementstate) | False | Elemental Inference Feed management state. |

### ElementalInferenceFeedManagementState
<a name="jobsqueries-id-model-elementalinferencefeedmanagementstate"></a>

Elemental Inference Feed management state.
+ `CREATED`
+ `ASSOCIATED`
+ `PENDING_DELETION`
+ `DELETED`

### EmbeddedConvert608To708
<a name="jobsqueries-id-model-embeddedconvert608to708"></a>

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.
+ `UPCONVERT`
+ `DISABLED`

### EmbeddedDestinationSettings
<a name="jobsqueries-id-model-embeddeddestinationsettings"></a>

Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Ignore this setting unless your input captions are SCC format and your output captions are embedded in the video stream. Specify a CC number for each captions channel in this output. If you have two channels, choose CC numbers that aren't in the same field. For example, choose 1 and 3. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded. |
| destination708ServiceNumber | integer<br />Minimum: 1<br />Maximum: 6 | False | Ignore this setting unless your input captions are SCC format and you want both 608 and 708 captions embedded in your output stream. Optionally, specify the 708 service number for each output captions channel. Choose a different number for each channel. To use this setting, also set Force 608 to 708 upconvert to Upconvert in your input captions selector settings. If you choose to upconvert but don't specify a 708 service number, MediaConvert uses the number that you specify for CC channel number for the 708 service number. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded. |

### EmbeddedSourceSettings
<a name="jobsqueries-id-model-embeddedsourcesettings"></a>

Settings for embedded captions Source

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| convert608To708 | [EmbeddedConvert608To708](#jobsqueries-id-model-embeddedconvert608to708) | False | Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708. |
| source608ChannelNumber | integer<br />Minimum: 1<br />Maximum: 4 | False | Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough. |
| source608TrackNumber | integer<br />Minimum: 1<br />Maximum: 1 | False | Specifies the video track index used for extracting captions. The system only supports one input video track, so this should always be set to '1'. |
| terminateCaptions | [EmbeddedTerminateCaptions](#jobsqueries-id-model-embeddedterminatecaptions) | False | By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting. |

### EmbeddedTerminateCaptions
<a name="jobsqueries-id-model-embeddedterminatecaptions"></a>

By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting.
+ `END_OF_INPUT`
+ `DISABLED`

### EmbeddedTimecodeOverride
<a name="jobsqueries-id-model-embeddedtimecodeoverride"></a>

Set Embedded timecode override to Use MDPM when your AVCHD input contains timecode tag data in the Modified Digital Video Pack Metadata. When you do, we recommend you also set Timecode source to Embedded. Leave Embedded timecode override blank, or set to None, when your input does not contain MDPM timecode.
+ `NONE`
+ `USE_MDPM`

### EncryptionContractConfiguration
<a name="jobsqueries-id-model-encryptioncontractconfiguration"></a>

Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spekeAudioPreset | [PresetSpeke20Audio](#jobsqueries-id-model-presetspeke20audio) | False | Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted). |
| spekeVideoPreset | [PresetSpeke20Video](#jobsqueries-id-model-presetspeke20video) | False | Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted). |

### EsamManifestConfirmConditionNotification
<a name="jobsqueries-id-model-esammanifestconfirmconditionnotification"></a>

ESAM ManifestConfirmConditionNotification defined by OC-SP-ESAM-API-I03-131025.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mccXml | string<br />Pattern: `^\s*<(.\|\n)*ManifestConfirmConditionNotification(.\|\n)*>\s*$` | False | Provide your ESAM ManifestConfirmConditionNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the Manifest Conditioning instructions in the message that you supply. |

### EsamSettings
<a name="jobsqueries-id-model-esamsettings"></a>

Settings for Event Signaling And Messaging (ESAM). If you don't do ad insertion, you can ignore these settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestConfirmConditionNotification | [EsamManifestConfirmConditionNotification](#jobsqueries-id-model-esammanifestconfirmconditionnotification) | False | Specifies an ESAM ManifestConfirmConditionNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the manifest conditioning instructions that you provide in the setting MCC XML. |
| responseSignalPreroll | integer<br />Minimum: 0<br />Maximum: 30000 | False | Specifies the stream distance, in milliseconds, between the SCTE 35 messages that the transcoder places and the splice points that they refer to. If the time between the start of the asset and the SCTE-35 message is less than this value, then the transcoder places the SCTE-35 marker at the beginning of the stream. |
| signalProcessingNotification | [EsamSignalProcessingNotification](#jobsqueries-id-model-esamsignalprocessingnotification) | False | Specifies an ESAM SignalProcessingNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the signal processing instructions that you provide in the setting SCC XML. |

### EsamSignalProcessingNotification
<a name="jobsqueries-id-model-esamsignalprocessingnotification"></a>

ESAM SignalProcessingNotification data defined by OC-SP-ESAM-API-I03-131025.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sccXml | string<br />Pattern: `^\s*<(.\|\n)*SignalProcessingNotification(.\|\n)*>\s*$` | False | Provide your ESAM SignalProcessingNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the signal processing instructions in the message that you supply. For your MPEG2-TS file outputs, if you want the service to place SCTE-35 markers at the insertion points you specify in the XML document, you must also enable SCTE-35 ESAM. Note that you can either specify an ESAM XML document or enable SCTE-35 passthrough. You can't do both. |

### ExceptionBody
<a name="jobsqueries-id-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ExtendedDataServices
<a name="jobsqueries-id-model-extendeddataservices"></a>

If your source content has EIA-608 Line 21 Data Services, enable this feature to specify what MediaConvert does with the Extended Data Services (XDS) packets. You can choose to pass through XDS packets, or remove them from the output. For more information about XDS, see EIA-608 Line Data Services, section 9.5.1.5 05h Content Advisory.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| copyProtectionAction | [CopyProtectionAction](#jobsqueries-id-model-copyprotectionaction) | False | The action to take on copy and redistribution control XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions. |
| vchipAction | [VchipAction](#jobsqueries-id-model-vchipaction) | False | The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions. |

### F4vMoovPlacement
<a name="jobsqueries-id-model-f4vmoovplacement"></a>

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.
+ `PROGRESSIVE_DOWNLOAD`
+ `NORMAL`

### F4vSettings
<a name="jobsqueries-id-model-f4vsettings"></a>

Settings for F4v container

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| moovPlacement | [F4vMoovPlacement](#jobsqueries-id-model-f4vmoovplacement) | False | To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal. |

### FileGroupSettings
<a name="jobsqueries-id-model-filegroupsettings"></a>

Settings related to your File output group. MediaConvert uses this group of settings to generate a single standalone file, rather than a streaming package.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destination | string<br />Pattern: `^s3:\/\/.*$` | False | Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file. |
| destinationSettings | [DestinationSettings](#jobsqueries-id-model-destinationsettings) | False | Settings associated with the destination. Will vary based on the type of destination |

### FileSourceConvert608To708
<a name="jobsqueries-id-model-filesourceconvert608to708"></a>

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.
+ `UPCONVERT`
+ `DISABLED`

### FileSourceSettings
<a name="jobsqueries-id-model-filesourcesettings"></a>

If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1 in an xml file, specify the URI of the input caption source file. If your caption source is IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| byteRateLimit | [CaptionSourceByteRateLimit](#jobsqueries-id-model-captionsourcebyteratelimit) | False | Choose whether to limit the byte rate at which your SCC input captions are inserted into your output. To not limit the caption rate: We recommend that you keep the default value, Disabled. MediaConvert inserts captions in your output according to the byte rates listed in the EIA-608 specification, typically 2 or 3 caption bytes per frame depending on your output frame rate. To limit your output caption rate: Choose Enabled. Choose this option if your downstream systems require a maximum of 2 caption bytes per frame. Note that this setting has no effect when your output frame rate is 30 or 60. |
| convert608To708 | [FileSourceConvert608To708](#jobsqueries-id-model-filesourceconvert608to708) | False | Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708. |
| convertPaintToPop | [CaptionSourceConvertPaintOnToPopOn](#jobsqueries-id-model-captionsourceconvertpaintontopopon) | False | Choose the presentation style of your input SCC captions. To use the same presentation style as your input: Keep the default value, Disabled. To convert paint-on captions to pop-on: Choose Enabled. We also recommend that you choose Enabled if you notice additional repeated lines in your output captions. |
| framerate | [CaptionSourceFramerate](#jobsqueries-id-model-captionsourceframerate) | False | Ignore this setting unless your input captions format is SCC. To have the service compensate for differing frame rates between your input captions and input video, specify the frame rate of the captions file. Specify this value as a fraction. For example, you might specify 24 / 1 for 24 fps, 25 / 1 for 25 fps, 24000 / 1001 for 23.976 fps, or 30000 / 1001 for 29.97 fps. |
| sourceFile | string<br />Pattern: `^((s3://(.*?)\.(scc\|SCC\|ttml\|TTML\|dfxp\|DFXP\|stl\|STL\|srt\|SRT\|xml\|XML\|smi\|SMI\|vtt\|VTT\|webvtt\|WEBVTT))\|(https?://(.*?)\.(scc\|SCC\|ttml\|TTML\|dfxp\|DFXP\|stl\|STL\|srt\|SRT\|xml\|XML\|smi\|SMI\|vtt\|VTT\|webvtt\|WEBVTT)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | External caption file used for loading captions. Accepted file extensions are 'scc', 'ttml', 'dfxp', 'stl', 'srt', 'xml', 'smi', 'webvtt', and 'vtt'. |
| timeDelta | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Optional. Use this setting when you need to adjust the sync between your sidecar captions and your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/time-delta-use-cases.html. Enter a positive or negative number to modify the times in the captions file. For example, type 15 to add 15 seconds to all the times in the captions file. Type -5 to subtract 5 seconds from the times in the captions file. You can optionally specify your time delta in milliseconds instead of seconds. When you do so, set the related setting, Time delta units to Milliseconds. Note that, when you specify a time delta for timecode-based caption sources, such as SCC and STL, and your time delta isn't a multiple of the input frame rate, MediaConvert snaps the captions to the nearest frame. For example, when your input video frame rate is 25 fps and you specify 1010ms for time delta, MediaConvert delays your captions by 1000 ms. |
| timeDeltaUnits | [FileSourceTimeDeltaUnits](#jobsqueries-id-model-filesourcetimedeltaunits) | False | When you use the setting Time delta to adjust the sync between your sidecar captions and your video, use this setting to specify the units for the delta that you specify. When you don't specify a value for Time delta units, MediaConvert uses seconds by default. |
| upconvertSTLToTeletext | [CaptionSourceUpconvertSTLToTeletext](#jobsqueries-id-model-captionsourceupconvertstltoteletext) | False | Specify whether this set of input captions appears in your outputs in both STL and Teletext format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the STL data through using the Teletext compatibility bytes fields of the Teletext wrapper, and it also translates the STL data into Teletext. |

### FileSourceTimeDeltaUnits
<a name="jobsqueries-id-model-filesourcetimedeltaunits"></a>

When you use the setting Time delta to adjust the sync between your sidecar captions and your video, use this setting to specify the units for the delta that you specify. When you don't specify a value for Time delta units, MediaConvert uses seconds by default.
+ `SECONDS`
+ `MILLISECONDS`

### FlacSettings
<a name="jobsqueries-id-model-flacsettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 8 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 8. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and 8. |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 192000 | False | Sample rate in Hz. |

### FontScript
<a name="jobsqueries-id-model-fontscript"></a>

Provide the font script, using an ISO 15924 script code, if the LanguageCode is not sufficient for determining the script type. Where LanguageCode or CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
+ `AUTOMATIC`
+ `HANS`
+ `HANT`

### ForceIncludeRenditionSize
<a name="jobsqueries-id-model-forceincluderenditionsize"></a>

Use Force include renditions to specify one or more resolutions to include your ABR stack. \* (Recommended) To optimize automated ABR, specify as few resolutions as possible. \* (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. \* If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. \* If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. \* If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. \* Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this rule. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this rule. |

### FrameCaptureSettings
<a name="jobsqueries-id-model-framecapturesettings"></a>

Required when you set Codec to the value FRAME\_CAPTURE.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places. |
| maxCaptures | integer<br />Minimum: 1<br />Maximum: 10000000 | False | Maximum number of captures (encoded jpg output files). |
| quality | integer<br />Minimum: 1<br />Maximum: 100 | False | JPEG Quality - a higher value equals higher quality. |

### FrameControl
<a name="jobsqueries-id-model-framecontrol"></a>

Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players.
+ `NEAREST_IDRFRAME`
+ `NEAREST_IFRAME`

### GetJobsQueryResultsRequest
<a name="jobsqueries-id-model-getjobsqueryresultsrequest"></a>

Retrieve a JSON array of up to twenty of your most recent jobs matched by a jobs query.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The ID of the jobs query. |

### GetJobsQueryResultsResponse
<a name="jobsqueries-id-model-getjobsqueryresultsresponse"></a>

If the jobs query completed successfully, then a JSON array of jobs will be included in this response. To retrieve the twenty next most recent jobs matched by your jobs query, call the StartJobsQuery using the nextToken string returned in this response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobs | Array of type [Job](#jobsqueries-id-model-job) | False | List of jobs. |
| nextToken | string | False | Use this string to request the next batch of jobs via the StartJobsQuery API. |
| status | [JobsQueryStatus](#jobsqueries-id-model-jobsquerystatus) | False | The status of the jobs query. |

### GifFramerateControl
<a name="jobsqueries-id-model-gifframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE\_FROM\_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### GifFramerateConversionAlgorithm
<a name="jobsqueries-id-model-gifframerateconversionalgorithm"></a>

Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE\_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`

### GifSettings
<a name="jobsqueries-id-model-gifsettings"></a>

Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateControl | [GifFramerateControl](#jobsqueries-id-model-gifframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE\_FROM\_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator. |
| framerateConversionAlgorithm | [GifFramerateConversionAlgorithm](#jobsqueries-id-model-gifframerateconversionalgorithm) | False | Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE\_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |

### H264AdaptiveQuantization
<a name="jobsqueries-id-model-h264adaptivequantization"></a>

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization.
+ `OFF`
+ `AUTO`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### H264CodecLevel
<a name="jobsqueries-id-model-h264codeclevel"></a>

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
<a name="jobsqueries-id-model-h264codecprofile"></a>

H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.
+ `BASELINE`
+ `HIGH`
+ `HIGH_10BIT`
+ `HIGH_422`
+ `HIGH_422_10BIT`
+ `MAIN`

### H264DynamicSubGop
<a name="jobsqueries-id-model-h264dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### H264EndOfStreamMarkers
<a name="jobsqueries-id-model-h264endofstreammarkers"></a>

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.
+ `INCLUDE`
+ `SUPPRESS`

### H264EntropyEncoding
<a name="jobsqueries-id-model-h264entropyencoding"></a>

Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
+ `CABAC`
+ `CAVLC`

### H264FieldEncoding
<a name="jobsqueries-id-model-h264fieldencoding"></a>

The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs.
+ `PAFF`
+ `FORCE_FIELD`
+ `MBAFF`

### H264FlickerAdaptiveQuantization
<a name="jobsqueries-id-model-h264flickeradaptivequantization"></a>

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264FramerateControl
<a name="jobsqueries-id-model-h264frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264FramerateConversionAlgorithm
<a name="jobsqueries-id-model-h264framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### H264GopBReference
<a name="jobsqueries-id-model-h264gopbreference"></a>

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.
+ `DISABLED`
+ `ENABLED`

### H264GopSizeUnits
<a name="jobsqueries-id-model-h264gopsizeunits"></a>

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.
+ `FRAMES`
+ `SECONDS`
+ `AUTO`

### H264InterlaceMode
<a name="jobsqueries-id-model-h264interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### H264ParControl
<a name="jobsqueries-id-model-h264parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H264QualityTuningLevel
<a name="jobsqueries-id-model-h264qualitytuninglevel"></a>

The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### H264QvbrSettings
<a name="jobsqueries-id-model-h264qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the H.264 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxAverageBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### H264RateControlMode
<a name="jobsqueries-id-model-h264ratecontrolmode"></a>

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
+ `VBR`
+ `CBR`
+ `QVBR`

### H264RepeatPps
<a name="jobsqueries-id-model-h264repeatpps"></a>

Places a PPS header on each encoded picture, even if repeated.
+ `DISABLED`
+ `ENABLED`

### H264SaliencyAwareEncoding
<a name="jobsqueries-id-model-h264saliencyawareencoding"></a>

Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled.
+ `DISABLED`
+ `PREFERRED`

### H264ScanTypeConversionMode
<a name="jobsqueries-id-model-h264scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### H264SceneChangeDetect
<a name="jobsqueries-id-model-h264scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.
+ `DISABLED`
+ `ENABLED`
+ `TRANSITION_DETECTION`

### H264Settings
<a name="jobsqueries-id-model-h264settings"></a>

Required when you set Codec to the value H\_264.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H264AdaptiveQuantization](#jobsqueries-id-model-h264adaptivequantization) | False | Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization. |
| bandwidthReductionFilter | [BandwidthReductionFilter](#jobsqueries-id-model-bandwidthreductionfilter) | False | The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [H264CodecLevel](#jobsqueries-id-model-h264codeclevel) | False | Specify an H.264 level that is consistent with your output video settings. If you aren't sure what level to specify, choose Auto. |
| codecProfile | [H264CodecProfile](#jobsqueries-id-model-h264codecprofile) | False | H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License. |
| dynamicSubGop | [H264DynamicSubGop](#jobsqueries-id-model-h264dynamicsubgop) | False | Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static. |
| endOfStreamMarkers | [H264EndOfStreamMarkers](#jobsqueries-id-model-h264endofstreammarkers) | False | Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream. |
| entropyEncoding | [H264EntropyEncoding](#jobsqueries-id-model-h264entropyencoding) | False | Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC. |
| fieldEncoding | [H264FieldEncoding](#jobsqueries-id-model-h264fieldencoding) | False | The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs. |
| flickerAdaptiveQuantization | [H264FlickerAdaptiveQuantization](#jobsqueries-id-model-h264flickeradaptivequantization) | False | Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| framerateControl | [H264FramerateControl](#jobsqueries-id-model-h264frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [H264FramerateConversionAlgorithm](#jobsqueries-id-model-h264framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopBReference | [H264GopBReference](#jobsqueries-id-model-h264gopbreference) | False | Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. In the console, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group. |
| gopSizeUnits | [H264GopSizeUnits](#jobsqueries-id-model-h264gopsizeunits) | False | Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [H264InterlaceMode](#jobsqueries-id-model-h264interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7. |
| numberReferenceFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H264ParControl](#jobsqueries-id-model-h264parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [H264QualityTuningLevel](#jobsqueries-id-model-h264qualitytuninglevel) | False | The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing. |
| qvbrSettings | [H264QvbrSettings](#jobsqueries-id-model-h264qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [H264RateControlMode](#jobsqueries-id-model-h264ratecontrolmode) | False | Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR). |
| repeatPps | [H264RepeatPps](#jobsqueries-id-model-h264repeatpps) | False | Places a PPS header on each encoded picture, even if repeated. |
| saliencyAwareEncoding | [H264SaliencyAwareEncoding](#jobsqueries-id-model-h264saliencyawareencoding) | False | Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled. |
| scanTypeConversionMode | [H264ScanTypeConversionMode](#jobsqueries-id-model-h264scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [H264SceneChangeDetect](#jobsqueries-id-model-h264scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| slowPal | [H264SlowPal](#jobsqueries-id-model-h264slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless you need to comply with a specification that requires a specific value. If you don't have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [H264SpatialAdaptiveQuantization](#jobsqueries-id-model-h264spatialadaptivequantization) | False | Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| syntax | [H264Syntax](#jobsqueries-id-model-h264syntax) | False | Produces a bitstream compliant with SMPTE RP-2027. |
| telecine | [H264Telecine](#jobsqueries-id-model-h264telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| temporalAdaptiveQuantization | [H264TemporalAdaptiveQuantization](#jobsqueries-id-model-h264temporaladaptivequantization) | False | Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO. |
| unregisteredSeiTimecode | [H264UnregisteredSeiTimecode](#jobsqueries-id-model-h264unregisteredseitimecode) | False | Inserts timecode for each frame as 4 bytes of an unregistered SEI message. |
| writeMp4PackagingType | [H264WriteMp4PackagingType](#jobsqueries-id-model-h264writemp4packagingtype) | False | Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players. |

### H264SlowPal
<a name="jobsqueries-id-model-h264slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### H264SpatialAdaptiveQuantization
<a name="jobsqueries-id-model-h264spatialadaptivequantization"></a>

Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264Syntax
<a name="jobsqueries-id-model-h264syntax"></a>

Produces a bitstream compliant with SMPTE RP-2027.
+ `DEFAULT`
+ `RP2027`

### H264Telecine
<a name="jobsqueries-id-model-h264telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `SOFT`
+ `HARD`

### H264TemporalAdaptiveQuantization
<a name="jobsqueries-id-model-h264temporaladaptivequantization"></a>

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.
+ `DISABLED`
+ `ENABLED`

### H264UnregisteredSeiTimecode
<a name="jobsqueries-id-model-h264unregisteredseitimecode"></a>

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
+ `DISABLED`
+ `ENABLED`

### H264WriteMp4PackagingType
<a name="jobsqueries-id-model-h264writemp4packagingtype"></a>

Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players.
+ `AVC1`
+ `AVC3`

### H265AdaptiveQuantization
<a name="jobsqueries-id-model-h265adaptivequantization"></a>

When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`
+ `AUTO`

### H265AlternateTransferFunctionSei
<a name="jobsqueries-id-model-h265alternatetransferfunctionsei"></a>

Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
+ `DISABLED`
+ `ENABLED`

### H265CodecLevel
<a name="jobsqueries-id-model-h265codeclevel"></a>

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
<a name="jobsqueries-id-model-h265codecprofile"></a>

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
<a name="jobsqueries-id-model-h265deblocking"></a>

Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates.
+ `ENABLED`
+ `DISABLED`

### H265DynamicSubGop
<a name="jobsqueries-id-model-h265dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### H265EndOfStreamMarkers
<a name="jobsqueries-id-model-h265endofstreammarkers"></a>

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.
+ `INCLUDE`
+ `SUPPRESS`

### H265FlickerAdaptiveQuantization
<a name="jobsqueries-id-model-h265flickeradaptivequantization"></a>

Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off.
+ `DISABLED`
+ `ENABLED`

### H265FramerateControl
<a name="jobsqueries-id-model-h265frameratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H265FramerateConversionAlgorithm
<a name="jobsqueries-id-model-h265framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### H265GopBReference
<a name="jobsqueries-id-model-h265gopbreference"></a>

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.
+ `DISABLED`
+ `ENABLED`

### H265GopSizeUnits
<a name="jobsqueries-id-model-h265gopsizeunits"></a>

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.
+ `FRAMES`
+ `SECONDS`
+ `AUTO`

### H265InterlaceMode
<a name="jobsqueries-id-model-h265interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### H265MvOverPictureBoundaries
<a name="jobsqueries-id-model-h265mvoverpictureboundaries"></a>

If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled".
+ `ENABLED`
+ `DISABLED`

### H265MvTemporalPredictor
<a name="jobsqueries-id-model-h265mvtemporalpredictor"></a>

If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled".
+ `ENABLED`
+ `DISABLED`

### H265ParControl
<a name="jobsqueries-id-model-h265parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### H265QualityTuningLevel
<a name="jobsqueries-id-model-h265qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### H265QvbrSettings
<a name="jobsqueries-id-model-h265qvbrsettings"></a>

Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxAverageBitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output. |
| qvbrQualityLevel | integer<br />Minimum: 1<br />Maximum: 10 | False | Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. |
| qvbrQualityLevelFineTune | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 1.0 | False | Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33. |

### H265RateControlMode
<a name="jobsqueries-id-model-h265ratecontrolmode"></a>

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
+ `VBR`
+ `CBR`
+ `QVBR`

### H265SampleAdaptiveOffsetFilterMode
<a name="jobsqueries-id-model-h265sampleadaptiveoffsetfiltermode"></a>

Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content
+ `DEFAULT`
+ `ADAPTIVE`
+ `OFF`

### H265ScanTypeConversionMode
<a name="jobsqueries-id-model-h265scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### H265SceneChangeDetect
<a name="jobsqueries-id-model-h265scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.
+ `DISABLED`
+ `ENABLED`
+ `TRANSITION_DETECTION`

### H265Settings
<a name="jobsqueries-id-model-h265settings"></a>

Settings for H265 codec

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [H265AdaptiveQuantization](#jobsqueries-id-model-h265adaptivequantization) | False | When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output. |
| alternateTransferFunctionSei | [H265AlternateTransferFunctionSei](#jobsqueries-id-model-h265alternatetransferfunctionsei) | False | Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF). |
| bandwidthReductionFilter | [BandwidthReductionFilter](#jobsqueries-id-model-bandwidthreductionfilter) | False | The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [H265CodecLevel](#jobsqueries-id-model-h265codeclevel) | False | H.265 Level. |
| codecProfile | [H265CodecProfile](#jobsqueries-id-model-h265codecprofile) | False | Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License. |
| deblocking | [H265Deblocking](#jobsqueries-id-model-h265deblocking) | False | Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates. |
| dynamicSubGop | [H265DynamicSubGop](#jobsqueries-id-model-h265dynamicsubgop) | False | Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static. |
| endOfStreamMarkers | [H265EndOfStreamMarkers](#jobsqueries-id-model-h265endofstreammarkers) | False | Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream. |
| flickerAdaptiveQuantization | [H265FlickerAdaptiveQuantization](#jobsqueries-id-model-h265flickeradaptivequantization) | False | Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off. |
| framerateControl | [H265FramerateControl](#jobsqueries-id-model-h265frameratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [H265FramerateConversionAlgorithm](#jobsqueries-id-model-h265framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopBReference | [H265GopBReference](#jobsqueries-id-model-h265gopbreference) | False | Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group. |
| gopSizeUnits | [H265GopSizeUnits](#jobsqueries-id-model-h265gopsizeunits) | False | Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1466400000 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [H265InterlaceMode](#jobsqueries-id-model-h265interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1466400000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| mvOverPictureBoundaries | [H265MvOverPictureBoundaries](#jobsqueries-id-model-h265mvoverpictureboundaries) | False | If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled". |
| mvTemporalPredictor | [H265MvTemporalPredictor](#jobsqueries-id-model-h265mvtemporalpredictor) | False | If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled". |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7. |
| numberReferenceFrames | integer<br />Minimum: 1<br />Maximum: 6 | False | Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding. |
| parControl | [H265ParControl](#jobsqueries-id-model-h265parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [H265QualityTuningLevel](#jobsqueries-id-model-h265qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| qvbrSettings | [H265QvbrSettings](#jobsqueries-id-model-h265qvbrsettings) | False | Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode. |
| rateControlMode | [H265RateControlMode](#jobsqueries-id-model-h265ratecontrolmode) | False | Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR). |
| sampleAdaptiveOffsetFilterMode | [H265SampleAdaptiveOffsetFilterMode](#jobsqueries-id-model-h265sampleadaptiveoffsetfiltermode) | False | Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content |
| scanTypeConversionMode | [H265ScanTypeConversionMode](#jobsqueries-id-model-h265scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [H265SceneChangeDetect](#jobsqueries-id-model-h265scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr. |
| slices | integer<br />Minimum: 1<br />Maximum: 32 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| slowPal | [H265SlowPal](#jobsqueries-id-model-h265slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| spatialAdaptiveQuantization | [H265SpatialAdaptiveQuantization](#jobsqueries-id-model-h265spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| telecine | [H265Telecine](#jobsqueries-id-model-h265telecine) | False | This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i. |
| temporalAdaptiveQuantization | [H265TemporalAdaptiveQuantization](#jobsqueries-id-model-h265temporaladaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. |
| temporalIds | [H265TemporalIds](#jobsqueries-id-model-h265temporalids) | False | Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output. |
| tileHeight | integer<br />Minimum: 64<br />Maximum: 2160 | False | Set this field to set up the picture as a tile. You must also set TileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 or less. If the tile width and height are specified, MediaConvert will override the video codec slices field with a value that MediaConvert calculates. |
| tilePadding | [H265TilePadding](#jobsqueries-id-model-h265tilepadding) | False | Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none". |
| tiles | [H265Tiles](#jobsqueries-id-model-h265tiles) | False | Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures. |
| tileWidth | integer<br />Minimum: 256<br />Maximum: 3840 | False | Set this field to set up the picture as a tile. See TileHeight for more information. |
| treeBlockSize | [H265TreeBlockSize](#jobsqueries-id-model-h265treeblocksize) | False | Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto". |
| unregisteredSeiTimecode | [H265UnregisteredSeiTimecode](#jobsqueries-id-model-h265unregisteredseitimecode) | False | Inserts timecode for each frame as 4 bytes of an unregistered SEI message. |
| writeMp4PackagingType | [H265WriteMp4PackagingType](#jobsqueries-id-model-h265writemp4packagingtype) | False | If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples. |

### H265SlowPal
<a name="jobsqueries-id-model-h265slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### H265SpatialAdaptiveQuantization
<a name="jobsqueries-id-model-h265spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### H265Telecine
<a name="jobsqueries-id-model-h265telecine"></a>

This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
+ `NONE`
+ `SOFT`
+ `HARD`

### H265TemporalAdaptiveQuantization
<a name="jobsqueries-id-model-h265temporaladaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### H265TemporalIds
<a name="jobsqueries-id-model-h265temporalids"></a>

Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.
+ `DISABLED`
+ `ENABLED`

### H265TilePadding
<a name="jobsqueries-id-model-h265tilepadding"></a>

Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none".
+ `NONE`
+ `PADDED`

### H265Tiles
<a name="jobsqueries-id-model-h265tiles"></a>

Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.
+ `DISABLED`
+ `ENABLED`

### H265TreeBlockSize
<a name="jobsqueries-id-model-h265treeblocksize"></a>

Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto".
+ `AUTO`
+ `TREE_SIZE_32X32`

### H265UnregisteredSeiTimecode
<a name="jobsqueries-id-model-h265unregisteredseitimecode"></a>

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
+ `DISABLED`
+ `ENABLED`

### H265WriteMp4PackagingType
<a name="jobsqueries-id-model-h265writemp4packagingtype"></a>

If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples.
+ `HVC1`
+ `HEV1`

### HDRToSDRToneMapper
<a name="jobsqueries-id-model-hdrtosdrtonemapper"></a>

Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR.
+ `PRESERVE_DETAILS`
+ `VIBRANT`

### Hdr10Metadata
<a name="jobsqueries-id-model-hdr10metadata"></a>

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
<a name="jobsqueries-id-model-hdr10plus"></a>

Setting for HDR10\+ metadata insertion

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| masteringMonitorNits | integer<br />Minimum: 0<br />Maximum: 4000 | False | Specify the HDR10\+ mastering display normalized peak luminance, in nits. This is the normalized actual peak luminance of the mastering display, as defined by ST 2094-40. |
| targetMonitorNits | integer<br />Minimum: 0<br />Maximum: 4000 | False | Specify the HDR10\+ target display nominal peak luminance, in nits. This is the nominal maximum luminance of the target display as defined by ST 2094-40. |

### HlsAdMarkers
<a name="jobsqueries-id-model-hlsadmarkers"></a>

Ad marker for Apple HLS manifest.
+ `ELEMENTAL`
+ `ELEMENTAL_SCTE35`

### HlsAdditionalManifest
<a name="jobsqueries-id-model-hlsadditionalmanifest"></a>

Specify the details for each additional HLS manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestNameModifier | string<br />MinLength: 1 | False | Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your HLS group is film-name.m3u8. If you enter "-no-premium" for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.m3u8. For HLS output groups, specify a manifestNameModifier that is different from the nameModifier of the output. The service uses the output name modifier to create unique names for the individual variant manifests. |
| selectedOutputs | Array of type string<br />MinLength: 1 | False | Specify the outputs that you want this additional top-level manifest to reference. |

### HlsAudioOnlyContainer
<a name="jobsqueries-id-model-hlsaudioonlycontainer"></a>

Use this setting only in audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a file in an MPEG2-TS container. Keep the default value Automatic to create a raw audio-only file with no container. Regardless of the value that you specify here, if this output has video, the service will place outputs into an MPEG2-TS container.
+ `AUTOMATIC`
+ `M2TS`

### HlsAudioOnlyHeader
<a name="jobsqueries-id-model-hlsaudioonlyheader"></a>

Ignore this setting unless you are using FairPlay DRM with Verimatrix and you encounter playback issues. Keep the default value, Include, to output audio-only headers. Choose Exclude to remove the audio-only headers from your audio segments.
+ `INCLUDE`
+ `EXCLUDE`

### HlsAudioTrackType
<a name="jobsqueries-id-model-hlsaudiotracktype"></a>

Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
+ `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
+ `ALTERNATE_AUDIO_AUTO_SELECT`
+ `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
+ `AUDIO_ONLY_VARIANT_STREAM`

### HlsCaptionLanguageMapping
<a name="jobsqueries-id-model-hlscaptionlanguagemapping"></a>

Caption Language Mapping

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| captionChannel | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Caption channel. |
| customLanguageCode | string<br />Pattern: `^[A-Za-z]{3}$`<br />MinLength: 3<br />MaxLength: 3 | False | Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| languageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| languageDescription | string | False | Caption language description. |

### HlsCaptionLanguageSetting
<a name="jobsqueries-id-model-hlscaptionlanguagesetting"></a>

Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest.
+ `INSERT`
+ `OMIT`
+ `NONE`

### HlsCaptionSegmentLengthControl
<a name="jobsqueries-id-model-hlscaptionsegmentlengthcontrol"></a>

Set Caption segment length control to Match video to create caption segments that align with the video segments from the first video output in this output group. For example, if the video segments are 2 seconds long, your WebVTT segments will also be 2 seconds long. Keep the default setting, Large segments to create caption segments that are 300 seconds long.
+ `LARGE_SEGMENTS`
+ `MATCH_VIDEO`

### HlsClearLead
<a name="jobsqueries-id-model-hlsclearlead"></a>

Enable Clear Lead DRM to reduce video startup latency by leaving the first segment unencrypted while DRM license retrieval occurs in parallel. This optimization allows immediate playback startup while maintaining content protection for the remainder of the stream. When enabled, the first output segment remains fully unencrypted, and encryption begins at the start of the second segment. The HLS manifest will omit \#EXT-X-KEY tags during the clear segment and insert the first \#EXT-X-KEY immediately before the first encrypted fragment. This feature is supported exclusively for CMAF HLS (fMP4) outputs and is compatible with all existing key provider integrations (SPEKE v1, SPEKE v2, and Static Key encryption). Supported codecs: H.264, H.265, and AV1 video codecs, and AAC audio codec. Choose Enabled to activate Clear Lead DRM optimization. Choose Disabled to use standard encryption where all segments are encrypted from the beginning.
+ `ENABLED`
+ `DISABLED`

### HlsClientCache
<a name="jobsqueries-id-model-hlsclientcache"></a>

Disable this setting only when your workflow requires the \#EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header.
+ `DISABLED`
+ `ENABLED`

### HlsCodecSpecification
<a name="jobsqueries-id-model-hlscodecspecification"></a>

Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
+ `RFC_6381`
+ `RFC_4281`

### HlsDescriptiveVideoServiceFlag
<a name="jobsqueries-id-model-hlsdescriptivevideoserviceflag"></a>

Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.
+ `DONT_FLAG`
+ `FLAG`

### HlsDirectoryStructure
<a name="jobsqueries-id-model-hlsdirectorystructure"></a>

Indicates whether segments should be placed in subdirectories.
+ `SINGLE_DIRECTORY`
+ `SUBDIRECTORY_PER_STREAM`

### HlsEncryptionSettings
<a name="jobsqueries-id-model-hlsencryptionsettings"></a>

Settings for HLS encryption

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantInitializationVector | string<br />Pattern: `^[0-9a-fA-F]{32}$`<br />MinLength: 32<br />MaxLength: 32 | False | This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default. |
| encryptionMethod | [HlsEncryptionType](#jobsqueries-id-model-hlsencryptiontype) | False | Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting 'Disabled' in the web interface also disables encryption. |
| initializationVectorInManifest | [HlsInitializationVectorInManifest](#jobsqueries-id-model-hlsinitializationvectorinmanifest) | False | The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest. |
| offlineEncrypted | [HlsOfflineEncrypted](#jobsqueries-id-model-hlsofflineencrypted) | False | Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection. |
| spekeKeyProvider | [SpekeKeyProvider](#jobsqueries-id-model-spekekeyprovider) | False | If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead. |
| staticKeyProvider | [StaticKeyProvider](#jobsqueries-id-model-statickeyprovider) | False | Use these settings to set up encryption with a static key provider. |
| type | [HlsKeyProviderType](#jobsqueries-id-model-hlskeyprovidertype) | False | Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html. |

### HlsEncryptionType
<a name="jobsqueries-id-model-hlsencryptiontype"></a>

Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting 'Disabled' in the web interface also disables encryption.
+ `AES128`
+ `SAMPLE_AES`

### HlsGroupSettings
<a name="jobsqueries-id-model-hlsgroupsettings"></a>

Settings related to your HLS output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalManifests | Array of type [HlsAdditionalManifest](#jobsqueries-id-model-hlsadditionalmanifest) | False | By default, the service creates one top-level .m3u8 HLS manifest for each HLS output group in your job. This default manifest references every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here. |
| adMarkers | Array of type [HlsAdMarkers](#jobsqueries-id-model-hlsadmarkers) | False | Choose one or more ad marker types to decorate your Apple HLS manifest. This setting does not determine whether SCTE-35 markers appear in the outputs themselves. |
| audioOnlyHeader | [HlsAudioOnlyHeader](#jobsqueries-id-model-hlsaudioonlyheader) | False | Ignore this setting unless you are using FairPlay DRM with Verimatrix and you encounter playback issues. Keep the default value, Include, to output audio-only headers. Choose Exclude to remove the audio-only headers from your audio segments. |
| baseUrl | string | False | A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file. |
| captionLanguageMappings | Array of type [HlsCaptionLanguageMapping](#jobsqueries-id-model-hlscaptionlanguagemapping) | False | Language to be used on Caption outputs |
| captionLanguageSetting | [HlsCaptionLanguageSetting](#jobsqueries-id-model-hlscaptionlanguagesetting) | False | Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest. |
| captionSegmentLengthControl | [HlsCaptionSegmentLengthControl](#jobsqueries-id-model-hlscaptionsegmentlengthcontrol) | False | Set Caption segment length control to Match video to create caption segments that align with the video segments from the first video output in this output group. For example, if the video segments are 2 seconds long, your WebVTT segments will also be 2 seconds long. Keep the default setting, Large segments to create caption segments that are 300 seconds long. |
| clientCache | [HlsClientCache](#jobsqueries-id-model-hlsclientcache) | False | Disable this setting only when your workflow requires the \#EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header. |
| codecSpecification | [HlsCodecSpecification](#jobsqueries-id-model-hlscodecspecification) | False | Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation. |
| destination | string<br />Pattern: `^s3:\/\/.*$` | False | Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file. |
| destinationSettings | [DestinationSettings](#jobsqueries-id-model-destinationsettings) | False | Settings associated with the destination. Will vary based on the type of destination |
| directoryStructure | [HlsDirectoryStructure](#jobsqueries-id-model-hlsdirectorystructure) | False | Indicates whether segments should be placed in subdirectories. |
| encryption | [HlsEncryptionSettings](#jobsqueries-id-model-hlsencryptionsettings) | False | DRM settings. |
| imageBasedTrickPlay | [HlsImageBasedTrickPlay](#jobsqueries-id-model-hlsimagebasedtrickplay) | False | Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md |
| imageBasedTrickPlaySettings | [HlsImageBasedTrickPlaySettings](#jobsqueries-id-model-hlsimagebasedtrickplaysettings) | False | Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED |
| manifestCompression | [HlsManifestCompression](#jobsqueries-id-model-hlsmanifestcompression) | False | When set to GZIP, compresses HLS playlist. |
| manifestDurationFormat | [HlsManifestDurationFormat](#jobsqueries-id-model-hlsmanifestdurationformat) | False | Indicates whether the output manifest should use floating point values for segment duration. |
| minFinalSegmentLength | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds. |
| minSegmentLength | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | When set, Minimum Segment Size is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed. |
| outputSelection | [HlsOutputSelection](#jobsqueries-id-model-hlsoutputselection) | False | Indicates whether the .m3u8 manifest file should be generated for this HLS output group. |
| programDateTime | [HlsProgramDateTime](#jobsqueries-id-model-hlsprogramdatetime) | False | Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp\_offset. |
| programDateTimePeriod | integer<br />Minimum: 0<br />Maximum: 3600 | False | Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds. |
| progressiveWriteHlsManifest | [HlsProgressiveWriteHlsManifest](#jobsqueries-id-model-hlsprogressivewritehlsmanifest) | False | Specify whether MediaConvert generates HLS manifests while your job is running or when your job is complete. To generate HLS manifests while your job is running: Choose Enabled. Use if you want to play back your content as soon as it's available. MediaConvert writes the parent and child manifests after the first three media segments are written to your destination S3 bucket. It then writes new updated manifests after each additional segment is written. The parent manifest includes the latest BANDWIDTH and AVERAGE-BANDWIDTH attributes, and child manifests include the latest available media segment. When your job completes, the final child playlists include an EXT-X-ENDLIST tag. To generate HLS manifests only when your job completes: Choose Disabled. |
| segmentControl | [HlsSegmentControl](#jobsqueries-id-model-hlssegmentcontrol) | False | When set to SINGLE\_FILE, emits program as a single media resource (.ts) file, uses \#EXT-X-BYTERANGE tags to index segment for playback. |
| segmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the length, in whole seconds, of each segment. When you don't specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries. |
| segmentLengthControl | [HlsSegmentLengthControl](#jobsqueries-id-model-hlssegmentlengthcontrol) | False | Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz. |
| segmentsPerSubdirectory | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify the number of segments to write to a subdirectory before starting a new one. You must also set Directory structure to Subdirectory per stream for this setting to have an effect. |
| streamInfResolution | [HlsStreamInfResolution](#jobsqueries-id-model-hlsstreaminfresolution) | False | Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest. |
| targetDurationCompatibilityMode | [HlsTargetDurationCompatibilityMode](#jobsqueries-id-model-hlstargetdurationcompatibilitymode) | False | When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\\\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration. |
| timedMetadataId3Frame | [HlsTimedMetadataId3Frame](#jobsqueries-id-model-hlstimedmetadataid3frame) | False | Specify the type of the ID3 frame to use for ID3 timestamps in your output. To include ID3 timestamps: Specify PRIV or TDRL and set ID3 metadata to Passthrough. To exclude ID3 timestamps: Set ID3 timestamp frame type to None. |
| timedMetadataId3Period | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Specify the interval in seconds to write ID3 timestamps in your output. The first timestamp starts at the output timecode and date, and increases incrementally with each ID3 timestamp. To use the default interval of 10 seconds: Leave blank. To include this metadata in your output: Set ID3 timestamp frame type to PRIV or TDRL, and set ID3 metadata to Passthrough. |
| timestampDeltaMilliseconds | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Provides an extra millisecond delta offset to fine tune the timestamps. |

### HlsIFrameOnlyManifest
<a name="jobsqueries-id-model-hlsiframeonlymanifest"></a>

Generate a variant manifest that lists only the I-frames for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only variant manifest and the regular variant manifest to the multivariant manifest. To have MediaConvert write a variant manifest that references I-frames from your output content using EXT-X-BYTERANGE tags: Choose Include. To have MediaConvert output I-frames as single frame TS files and a corresponding variant manifest that references them: Choose Include as TS. When you don't need the I-frame only variant manifest: Keep the default value, Exclude.
+ `INCLUDE`
+ `INCLUDE_AS_TS`
+ `EXCLUDE`

### HlsImageBasedTrickPlay
<a name="jobsqueries-id-model-hlsimagebasedtrickplay"></a>

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md
+ `NONE`
+ `THUMBNAIL`
+ `THUMBNAIL_AND_FULLFRAME`
+ `ADVANCED`

### HlsImageBasedTrickPlaySettings
<a name="jobsqueries-id-model-hlsimagebasedtrickplaysettings"></a>

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| intervalCadence | [HlsIntervalCadence](#jobsqueries-id-model-hlsintervalcadence) | False | The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling. |
| thumbnailHeight | integer<br />Minimum: 2<br />Maximum: 4096 | False | Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2. |
| thumbnailInterval | number<br />Format: float<br />Minimum: 0.0<br />Maximum: 2.147483647E9 | False | Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesn't align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails. |
| thumbnailWidth | integer<br />Minimum: 8<br />Maximum: 4096 | False | Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8. |
| tileHeight | integer<br />Minimum: 1<br />Maximum: 2048 | False | Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2. |
| tileWidth | integer<br />Minimum: 1<br />Maximum: 512 | False | Number of thumbnails in each row of a tile image. Set a value between 1 and 512. |

### HlsInitializationVectorInManifest
<a name="jobsqueries-id-model-hlsinitializationvectorinmanifest"></a>

The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.
+ `INCLUDE`
+ `EXCLUDE`

### HlsIntervalCadence
<a name="jobsqueries-id-model-hlsintervalcadence"></a>

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW\_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW\_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW\_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW\_SEGMENTATION requires 1x1 tiling.
+ `FOLLOW_IFRAME`
+ `FOLLOW_CUSTOM`
+ `FOLLOW_SEGMENTATION`

### HlsKeyProviderType
<a name="jobsqueries-id-model-hlskeyprovidertype"></a>

Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.
+ `SPEKE`
+ `STATIC_KEY`

### HlsManifestCompression
<a name="jobsqueries-id-model-hlsmanifestcompression"></a>

When set to GZIP, compresses HLS playlist.
+ `GZIP`
+ `NONE`

### HlsManifestDurationFormat
<a name="jobsqueries-id-model-hlsmanifestdurationformat"></a>

Indicates whether the output manifest should use floating point values for segment duration.
+ `FLOATING_POINT`
+ `INTEGER`

### HlsOfflineEncrypted
<a name="jobsqueries-id-model-hlsofflineencrypted"></a>

Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection.
+ `ENABLED`
+ `DISABLED`

### HlsOutputSelection
<a name="jobsqueries-id-model-hlsoutputselection"></a>

Indicates whether the .m3u8 manifest file should be generated for this HLS output group.
+ `MANIFESTS_AND_SEGMENTS`
+ `SEGMENTS_ONLY`

### HlsProgramDateTime
<a name="jobsqueries-id-model-hlsprogramdatetime"></a>

Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp\_offset.
+ `INCLUDE`
+ `EXCLUDE`

### HlsProgressiveWriteHlsManifest
<a name="jobsqueries-id-model-hlsprogressivewritehlsmanifest"></a>

Specify whether MediaConvert generates HLS manifests while your job is running or when your job is complete. To generate HLS manifests while your job is running: Choose Enabled. Use if you want to play back your content as soon as it's available. MediaConvert writes the parent and child manifests after the first three media segments are written to your destination S3 bucket. It then writes new updated manifests after each additional segment is written. The parent manifest includes the latest BANDWIDTH and AVERAGE-BANDWIDTH attributes, and child manifests include the latest available media segment. When your job completes, the final child playlists include an EXT-X-ENDLIST tag. To generate HLS manifests only when your job completes: Choose Disabled.
+ `ENABLED`
+ `DISABLED`

### HlsRenditionGroupSettings
<a name="jobsqueries-id-model-hlsrenditiongroupsettings"></a>

Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| renditionGroupId | string | False | Optional. Specify alternative group ID |
| renditionLanguageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Optionally specify the language, using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| renditionName | string | False | Optional. Specify media name |

### HlsSegmentControl
<a name="jobsqueries-id-model-hlssegmentcontrol"></a>

When set to SINGLE\_FILE, emits program as a single media resource (.ts) file, uses \#EXT-X-BYTERANGE tags to index segment for playback.
+ `SINGLE_FILE`
+ `SEGMENTED_FILES`

### HlsSegmentLengthControl
<a name="jobsqueries-id-model-hlssegmentlengthcontrol"></a>

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.
+ `EXACT`
+ `GOP_MULTIPLE`
+ `MATCH`

### HlsSettings
<a name="jobsqueries-id-model-hlssettings"></a>

Settings for HLS output groups

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioGroupId | string | False | Specifies the group to which the audio rendition belongs. |
| audioOnlyContainer | [HlsAudioOnlyContainer](#jobsqueries-id-model-hlsaudioonlycontainer) | False | Use this setting only in audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a file in an MPEG2-TS container. Keep the default value Automatic to create an audio-only file in a raw container. Regardless of the value that you specify here, if this output has video, the service will place the output into an MPEG2-TS container. |
| audioRenditionSets | string | False | List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','. |
| audioTrackType | [HlsAudioTrackType](#jobsqueries-id-model-hlsaudiotracktype) | False | Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO |
| descriptiveVideoServiceFlag | [HlsDescriptiveVideoServiceFlag](#jobsqueries-id-model-hlsdescriptivevideoserviceflag) | False | Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation. |
| iFrameOnlyManifest | [HlsIFrameOnlyManifest](#jobsqueries-id-model-hlsiframeonlymanifest) | False | Generate a variant manifest that lists only the I-frames for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only variant manifest and the regular variant manifest to the multivariant manifest. To have MediaConvert write a variant manifest that references I-frames from your output content using EXT-X-BYTERANGE tags: Choose Include. To have MediaConvert output I-frames as single frame TS files and a corresponding variant manifest that references them: Choose Include as TS. When you don't need the I-frame only variant manifest: Keep the default value, Exclude. |
| segmentModifier | string | False | Use this setting to add an identifying string to the filename of each segment. The service adds this string between the name modifier and segment index number. You can use format identifiers in the string. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html |

### HlsStreamInfResolution
<a name="jobsqueries-id-model-hlsstreaminfresolution"></a>

Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
+ `INCLUDE`
+ `EXCLUDE`

### HlsTargetDurationCompatibilityMode
<a name="jobsqueries-id-model-hlstargetdurationcompatibilitymode"></a>

When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\\\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration.
+ `LEGACY`
+ `SPEC_COMPLIANT`

### HlsTimedMetadataId3Frame
<a name="jobsqueries-id-model-hlstimedmetadataid3frame"></a>

Specify the type of the ID3 frame to use for ID3 timestamps in your output. To include ID3 timestamps: Specify PRIV or TDRL and set ID3 metadata to Passthrough. To exclude ID3 timestamps: Set ID3 timestamp frame type to None.
+ `NONE`
+ `PRIV`
+ `TDRL`

### HopDestination
<a name="jobsqueries-id-model-hopdestination"></a>

Optional. Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| priority | integer<br />Format: int32<br />Minimum: -50<br />Maximum: 50 | False | Optional. When you set up a job to use queue hopping, you can specify a different relative priority for the job in the destination queue. If you don't specify, the relative priority will remain the same as in the previous queue. |
| queue | string | False | Optional unless the job is submitted on the default queue. When you set up a job to use queue hopping, you can specify a destination queue. This queue cannot be the original queue to which the job is submitted. If the original queue isn't the default queue and you don't specify the destination queue, the job will move to the default queue. |
| waitMinutes | integer | False | Required for setting up a job to use queue hopping. Minimum wait time in minutes until the job can hop to the destination queue. Valid range is 1 to 4320 minutes, inclusive. |

### Id3Insertion
<a name="jobsqueries-id-model-id3insertion"></a>

To insert ID3 tags in your output, specify two values. Use ID3 tag to specify the base 64 encoded string and use Timecode to specify the time when the tag should be inserted. To insert multiple ID3 tags in your output, create multiple instances of ID3 insertion.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id3 | string<br />Pattern: `^[A-Za-z0-9+\/]+={0,2}$` | False | Use ID3 tag to provide a fully formed ID3 tag in base64-encode format. |
| timecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Provide a Timecode in HH:MM:SS:FF or HH:MM:SS;FF format. |

### ImageInserter
<a name="jobsqueries-id-model-imageinserter"></a>

Use the image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each input or output individually. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/graphic-overlay.html. This setting is disabled by default.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| insertableImages | Array of type [InsertableImage](#jobsqueries-id-model-insertableimage) | False | Specify the images that you want to overlay on your video. The images must be PNG or TGA files. |
| sdrReferenceWhiteLevel | integer<br />Minimum: 100<br />Maximum: 1000 | False | Specify the reference white level, in nits, for all of your image inserter images. Use to correct brightness levels within HDR10 outputs. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000. |

### ImscAccessibilitySubs
<a name="jobsqueries-id-model-imscaccessibilitysubs"></a>

If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>.
+ `DISABLED`
+ `ENABLED`

### ImscDestinationSettings
<a name="jobsqueries-id-model-imscdestinationsettings"></a>

Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibility | [ImscAccessibilitySubs](#jobsqueries-id-model-imscaccessibilitysubs) | False | If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>. |
| stylePassthrough | [ImscStylePassthrough](#jobsqueries-id-model-imscstylepassthrough) | False | Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions. |

### ImscStylePassthrough
<a name="jobsqueries-id-model-imscstylepassthrough"></a>

Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions.
+ `ENABLED`
+ `DISABLED`

### Input
<a name="jobsqueries-id-model-input"></a>

Use inputs to define the source files used in your transcoding job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html. You can use multiple video inputs to do input stitching. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| advancedInputFilter | [AdvancedInputFilter](#jobsqueries-id-model-advancedinputfilter) | False | Use to remove noise, blocking, blurriness, or ringing from your input as a pre-filter step before encoding. The Advanced input filter removes more types of compression artifacts and is an improvement when compared to basic Deblock and Denoise filters. To remove video compression artifacts from your input and improve the video quality: Choose Enabled. Additionally, this filter can help increase the video quality of your output relative to its bitrate, since noisy inputs are more complex and require more bits to encode. To help restore loss of detail after applying the filter, you can optionally add texture or sharpening as an additional step. Jobs that use this feature incur pro-tier pricing. To not apply advanced input filtering: Choose Disabled. Note that you can still apply basic filtering with Deblock and Denoise. |
| advancedInputFilterSettings | [AdvancedInputFilterSettings](#jobsqueries-id-model-advancedinputfiltersettings) | False | Optional settings for Advanced input filter when you set Advanced input filter to Enabled. |
| audioSelectorGroups | object | False | Use audio selector groups to combine multiple sidecar audio inputs so that you can assign them to a single output audio tab. Note that, if you're working with embedded audio, it's simpler to assign multiple input tracks into a single audio selector rather than use an audio selector group. |
| audioSelectors | object | False | Use Audio selectors to specify a track or set of tracks from the input that you will use in your outputs. You can use multiple Audio selectors per input. |
| captionSelectors | object | False | Use captions selectors to specify the captions data from your input that you use in your outputs. You can use up to 100 captions selectors per input. |
| crop | [Rectangle](#jobsqueries-id-model-rectangle) | False | Use Cropping selection to specify the video area that the service will include in the output video frame. If you specify a value here, it will override any value that you specify in the output setting Cropping selection. |
| deblockFilter | [InputDeblockFilter](#jobsqueries-id-model-inputdeblockfilter) | False | Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs. |
| decryptionSettings | [InputDecryptionSettings](#jobsqueries-id-model-inputdecryptionsettings) | False | Settings for decrypting any input files that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt files only when you use AWS Key Management Service (KMS) to encrypt the data key that you use to encrypt your content. |
| denoiseFilter | [InputDenoiseFilter](#jobsqueries-id-model-inputdenoisefilter) | False | Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs. |
| dolbyVisionMetadataXml | string<br />Pattern: `^((s3://(.*?)\.(xml\|XML))\|(https?://(.*?)\.(xml\|XML)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Use this setting only when your video source has Dolby Vision studio mastering metadata that is carried in a separate XML file. Specify the Amazon S3 location for the metadata XML file. MediaConvert uses this file to provide global and frame-level metadata for Dolby Vision preprocessing. When you specify a file here and your input also has interleaved global and frame level metadata, MediaConvert ignores the interleaved metadata and uses only the the metadata from this external XML file. Note that your IAM service role must grant MediaConvert read permissions to this file. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html. |
| dynamicAudioSelectors | object | False | Use Dynamic audio selectors when you do not know the track layout of your source when you submit your job, but want to select multiple audio tracks. When you include an audio track in your output and specify this Dynamic audio selector as the Audio source, MediaConvert creates an output audio track for each dynamically selected track. Note that when you include a Dynamic audio selector for two or more inputs, each input must have the same number of audio tracks and audio channels. |
| fileInput | string<br />Pattern: `^s3://([^\/]+\/+)+((([^\/]*)))\|^https?://[^\/].*[^&]$`<br />MaxLength: 2048 | False | Specify the source file for your transcoding job. You can use multiple inputs in a single job. The service concatenates these inputs, in the order that you specify them in the job, to create the outputs. For standard inputs, provide the path to your S3, HTTP, or HTTPS source file. For example, s3://amzn-s3-demo-bucket/input.mp4 for an Amazon S3 input or https://example.com/input.mp4 for an HTTPS input. For TAMS inputs, specify the HTTPS endpoint of your TAMS server. For example, https://tams-server.example.com . When you do, also specify Source ID, Timerange, GAP handling, and the Authorization connection ARN under TAMS settings. (Don't include these parameters in the Input file URL.) For IMF inputs, specify your input by providing the path to your CPL. For example, s3://amzn-s3-demo-bucket/vf/cpl.xml . If the CPL is in an incomplete IMP, make sure to use Supplemental IMPsto specify any supplemental IMPs that contain assets referenced by the CPL. |
| filterEnable | [InputFilterEnable](#jobsqueries-id-model-inputfilterenable) | False | Specify whether to apply input filtering to improve the video quality of your input. To apply filtering depending on your input type and quality: Choose Auto. To apply no filtering: Choose Disable. To apply filtering regardless of your input type and quality: Choose Force. When you do, you must also specify a value for Filter strength. |
| filterStrength | integer<br />Minimum: 0<br />Maximum: 5 | False | Specify the strength of the input filter. To apply an automatic amount of filtering based the compression artifacts measured in your input: We recommend that you leave Filter strength blank and set Filter enable to Auto. To manually apply filtering: Enter a value from 1 to 5, where 1 is the least amount of filtering and 5 is the most. The value that you enter applies to the strength of the Deblock or Denoise filters, or to the strength of the Advanced input filter. |
| imageInserter | [ImageInserter](#jobsqueries-id-model-imageinserter) | False | Enable the image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each input individually. This setting is disabled by default. |
| inputClippings | Array of type [InputClipping](#jobsqueries-id-model-inputclipping) | False | Contains sets of start and end times that together specify a portion of the input to be used in the outputs. If you provide only a start time, the clip will be the entire input from that point to the end. If you provide only an end time, it will be the entire input up to that point. When you specify more than one input clip, the transcoding service creates the job outputs by stringing the clips together in the order you specify them. |
| inputScanType | [InputScanType](#jobsqueries-id-model-inputscantype) | False | When you have a progressive segmented frame (PsF) input, use this setting to flag the input as PsF. MediaConvert doesn't automatically detect PsF. Therefore, flagging your input as PsF results in better preservation of video quality when you do deinterlacing and frame rate conversion. If you don't specify, the default value is Auto. Auto is the correct setting for all inputs that are not PsF. Don't set this value to PsF when your input is interlaced. Doing so creates horizontal interlacing artifacts. |
| multiViewSettings | Array of type [MultiViewSettings](#jobsqueries-id-model-multiviewsettings) | False | Specify the enhancement layer input video file path for Multi View outputs. The base layer input is treated as the left eye and this Multi View input is treated as the right eye. Only one Multi View input is currently supported. MediaConvert encodes both views into a single MV-HEVC output codec. When you add MultiViewSettings to your job, you can only produce Multi View outputs. Adding any other codec output to the same job is not supported. |
| position | [Rectangle](#jobsqueries-id-model-rectangle) | False | Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black. If you specify a value here, it will override any value that you specify in the output setting Selection placement. If you specify a value here, this will override any AFD values in your input, even if you set Respond to AFD to Respond. If you specify a value here, this will ignore anything that you specify for the setting Scaling Behavior. |
| programNumber | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Use Program to select a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. Default is the first program within the transport stream. If the program you specify doesn't exist, the transcoding service will use this default. |
| psiControl | [InputPsiControl](#jobsqueries-id-model-inputpsicontrol) | False | Set PSI control for transport stream inputs to specify which data the demux process to scans. \* Ignore PSI - Scan all PIDs for audio and video. \* Use PSI - Scan only PSI data. |
| supplementalImps | Array of type string<br />Pattern: `^s3:\/\/.*\/(ASSETMAP.xml)?$` | False | Provide a list of any necessary supplemental IMPs. You need supplemental IMPs if the CPL that you're using for your input is in an incomplete IMP. Specify either the supplemental IMP directories with a trailing slash or the ASSETMAP.xml files. For example ["s3://bucket/ov/", "s3://bucket/vf2/ASSETMAP.xml"]. You don't need to specify the IMP that contains your input CPL, because the service automatically detects it. |
| tamsSettings | [InputTamsSettings](#jobsqueries-id-model-inputtamssettings) | False | Specify a Time Addressable Media Store (TAMS) server as an input source. TAMS is an open-source API specification that provides access to time-segmented media content. Use TAMS to retrieve specific time ranges from live or archived media streams. When you specify TAMS settings, MediaConvert connects to your TAMS server, retrieves the media segments for your specified time range, and processes them as a single input. This enables workflows like extracting clips from live streams or processing specific portions of archived content. To use TAMS, you must: 1. Have access to a TAMS-compliant server 2. Specify the server URL in the Input file URL field 3. Provide the required SourceId and Timerange parameters 4. Configure authentication, if your TAMS server requires it |
| timecodeSource | [InputTimecodeSource](#jobsqueries-id-model-inputtimecodesource) | False | Use this Timecode source setting, located under the input settings, to specify how the service counts input video frames. This input frame count affects only the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Choose Embedded to use the timecodes in your input video. Choose Start at zero to start the first frame at zero. Choose Specified start to start the first frame at the timecode that you specify in the setting Start timecode. If you don't specify a value for Timecode source, the service will use Embedded by default. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode. |
| timecodeStart | string<br />Pattern: `^((([0-1]\d)\|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`<br />MinLength: 11<br />MaxLength: 11 | False | Specify the timecode that you want the service to use for this input's initial frame. To use this setting, you must set the Timecode source setting, located under the input settings, to Specified start. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode. |
| videoGenerator | [InputVideoGenerator](#jobsqueries-id-model-inputvideogenerator) | False | When you include Video generator, MediaConvert creates a video input with black frames. Use this setting if you do not have a video input or if you want to add black video frames before, or after, other inputs. You can specify Video generator, or you can specify an Input file, but you cannot specify both. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html |
| videoOverlays | Array of type [VideoOverlay](#jobsqueries-id-model-videooverlay) | False | Contains an array of video overlays. |
| videoSelector | [VideoSelector](#jobsqueries-id-model-videoselector) | False | Input video selectors contain the video settings for the input. Each of your inputs can have up to one video selector. |

### InputClipping
<a name="jobsqueries-id-model-inputclipping"></a>

To transcode only portions of your input, include one input clip for each part of your input that you want in your output. All input clips that you specify will be included in every output of the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}(@[0-9]+(\.[0-9]+)?(:[0-9]+)?)?$` | False | Set End timecode to the end of the portion of the input you are clipping. The frame corresponding to the End timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for timecode source under input settings. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to end six minutes into the video, use 01:06:00:00. |
| startTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}(@[0-9]+(\.[0-9]+)?(:[0-9]+)?)?$` | False | Set Start timecode to the beginning of the portion of the input you are clipping. The frame corresponding to the Start timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for Input timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to begin five minutes into the video, use 01:05:00:00. |

### InputDeblockFilter
<a name="jobsqueries-id-model-inputdeblockfilter"></a>

Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs.
+ `ENABLED`
+ `DISABLED`

### InputDecryptionSettings
<a name="jobsqueries-id-model-inputdecryptionsettings"></a>

Settings for decrypting any input files that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt files only when you use AWS Key Management Service (KMS) to encrypt the data key that you use to encrypt your content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| decryptionMode | [DecryptionMode](#jobsqueries-id-model-decryptionmode) | False | Specify the encryption mode that you used to encrypt your input files. |
| encryptedDecryptionKey | string<br />Pattern: `^[A-Za-z0-9+\/]+={0,2}$`<br />MinLength: 24<br />MaxLength: 512 | False | Warning\! Don't provide your encryption key in plaintext. Your job settings could be intercepted, making your encrypted content vulnerable. Specify the encrypted version of the data key that you used to encrypt your content. The data key must be encrypted by AWS Key Management Service (KMS). The key can be 128, 192, or 256 bits. |
| initializationVector | string<br />Pattern: `^[A-Za-z0-9+\/]{22}==$\|^[A-Za-z0-9+\/]{16}$`<br />MinLength: 16<br />MaxLength: 24 | False | Specify the initialization vector that you used when you encrypted your content before uploading it to Amazon S3. You can use a 16-byte initialization vector with any encryption mode. Or, you can use a 12-byte initialization vector with GCM or CTR. MediaConvert accepts only initialization vectors that are base64-encoded. |
| kmsKeyRegion | string<br />Pattern: `^[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}$`<br />MinLength: 9<br />MaxLength: 19 | False | Specify the AWS Region for AWS Key Management Service (KMS) that you used to encrypt your data key, if that Region is different from the one you are using for AWS Elemental MediaConvert. |

### InputDenoiseFilter
<a name="jobsqueries-id-model-inputdenoisefilter"></a>

Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs.
+ `ENABLED`
+ `DISABLED`

### InputFilterEnable
<a name="jobsqueries-id-model-inputfilterenable"></a>

Specify whether to apply input filtering to improve the video quality of your input. To apply filtering depending on your input type and quality: Choose Auto. To apply no filtering: Choose Disable. To apply filtering regardless of your input type and quality: Choose Force. When you do, you must also specify a value for Filter strength.
+ `AUTO`
+ `DISABLE`
+ `FORCE`

### InputPsiControl
<a name="jobsqueries-id-model-inputpsicontrol"></a>

Set PSI control for transport stream inputs to specify which data the demux process to scans. \* Ignore PSI - Scan all PIDs for audio and video. \* Use PSI - Scan only PSI data.
+ `IGNORE_PSI`
+ `USE_PSI`

### InputRotate
<a name="jobsqueries-id-model-inputrotate"></a>

Use Rotate to specify how the service rotates your video. You can choose automatic rotation or specify a rotation. You can specify a clockwise rotation of 0, 90, 180, or 270 degrees. If your input video container is .mov or .mp4 and your input has rotation metadata, you can choose Automatic to have the service rotate your video according to the rotation specified in the metadata. The rotation must be within one degree of 90, 180, or 270 degrees. If the rotation metadata specifies any other rotation, the service will default to no rotation. By default, the service does no rotation, even if your input video has rotation metadata. The service doesn't pass through rotation metadata.
+ `DEGREE_0`
+ `DEGREES_90`
+ `DEGREES_180`
+ `DEGREES_270`
+ `AUTO`

### InputSampleRange
<a name="jobsqueries-id-model-inputsamplerange"></a>

If the sample range metadata in your input video is accurate, or if you don't know about sample range, keep the default value, Follow, for this setting. When you do, the service automatically detects your input sample range. If your input video has metadata indicating the wrong sample range, specify the accurate sample range here. When you do, MediaConvert ignores any sample range information in the input metadata. Regardless of whether MediaConvert uses the input sample range or the sample range that you specify, MediaConvert uses the sample range for transcoding and also writes it to the output metadata.
+ `FOLLOW`
+ `FULL_RANGE`
+ `LIMITED_RANGE`

### InputScanType
<a name="jobsqueries-id-model-inputscantype"></a>

When you have a progressive segmented frame (PsF) input, use this setting to flag the input as PsF. MediaConvert doesn't automatically detect PsF. Therefore, flagging your input as PsF results in better preservation of video quality when you do deinterlacing and frame rate conversion. If you don't specify, the default value is Auto. Auto is the correct setting for all inputs that are not PsF. Don't set this value to PsF when your input is interlaced. Doing so creates horizontal interlacing artifacts.
+ `AUTO`
+ `PSF`

### InputTamsSettings
<a name="jobsqueries-id-model-inputtamssettings"></a>

Specify a Time Addressable Media Store (TAMS) server as an input source. TAMS is an open-source API specification that provides access to time-segmented media content. Use TAMS to retrieve specific time ranges from live or archived media streams. When you specify TAMS settings, MediaConvert connects to your TAMS server, retrieves the media segments for your specified time range, and processes them as a single input. This enables workflows like extracting clips from live streams or processing specific portions of archived content. To use TAMS, you must: 1. Have access to a TAMS-compliant server 2. Specify the server URL in the Input file URL field 3. Provide the required SourceId and Timerange parameters 4. Configure authentication, if your TAMS server requires it

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authConnectionArn | string<br />Pattern: `^arn:aws[a-z0-9-]*:events:[a-z0-9-]+:[0-9]{12}:connection/[a-zA-Z0-9-]+/[a-f0-9-]{36}$` | False | Specify the ARN (Amazon Resource Name) of an EventBridge Connection to authenticate with your TAMS server. The EventBridge Connection stores your authentication credentials securely. MediaConvert assumes your job's IAM role to access this connection, so ensure the role has the events:RetrieveConnectionCredentials, secretsmanager:DescribeSecret, and secretsmanager:GetSecretValue permissions. Format: arn:aws:events:region:account-id:connection/connection-name/unique-id This setting is required when you include TAMS settings in your job. |
| gapHandling | [TamsGapHandling](#jobsqueries-id-model-tamsgaphandling) | False | Specify how MediaConvert handles gaps between media segments in your TAMS source. Gaps can occur in live streams due to network issues or other interruptions. Choose from the following options: \* Skip gaps - Default. Skip over gaps and join segments together. This creates a continuous output with no blank frames, but may cause timeline discontinuities. \* Fill with black - Insert black frames to fill gaps between segments. This maintains timeline continuity but adds black frames where content is missing. \* Hold last frame - Repeat the last frame before a gap until the next segment begins. This maintains visual continuity during gaps. |
| sourceId | string | False | Specify the unique identifier for the media source in your TAMS server. MediaConvert uses this source ID to locate the appropriate flows containing the media segments you want to process. The source ID corresponds to a specific media source registered in your TAMS server. This source must be of type urn:x-nmos:format:multi, and can can reference multiple flows for audio, video, or combined audio/video content. MediaConvert automatically selects the highest quality flows available for your job. This setting is required when you include TAMS settings in your job. |
| timerange | string<br />Pattern: `^(\[\|\()?(-?(0\|[1-9][0-9]*):(0\|[1-9][0-9]{0,8}))?(_(-?(0\|[1-9][0-9]*):(0\|[1-9][0-9]{0,8}))?)?(\]\|\))?$` | False | Specify the time range of media segments to retrieve from your TAMS server. MediaConvert fetches only the segments that fall within this range. Use the format specified by your TAMS server implementation. This must be two timestamp values with the format {sign?}{seconds}:{nanoseconds}, separated by an underscore, surrounded by either parentheses or square brackets. Example: [15:0\_35:0) This setting is required when you include TAMS settings in your job. |

### InputTimecodeSource
<a name="jobsqueries-id-model-inputtimecodesource"></a>

Use this Timecode source setting, located under the input settings, to specify how the service counts input video frames. This input frame count affects only the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Choose Embedded to use the timecodes in your input video. Choose Start at zero to start the first frame at zero. Choose Specified start to start the first frame at the timecode that you specify in the setting Start timecode. If you don't specify a value for Timecode source, the service will use Embedded by default. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode.
+ `EMBEDDED`
+ `ZEROBASED`
+ `SPECIFIEDSTART`

### InputVideoGenerator
<a name="jobsqueries-id-model-inputvideogenerator"></a>

When you include Video generator, MediaConvert creates a video input with black frames. Use this setting if you do not have a video input or if you want to add black video frames before, or after, other inputs. You can specify Video generator, or you can specify an Input file, but you cannot specify both. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | integer<br />Minimum: 1<br />Maximum: 32 | False | Specify the number of audio channels to include in your video generator input. MediaConvert creates these audio channels as silent audio within a single audio track. Enter an integer from 1 to 32. |
| duration | integer<br />Minimum: 1<br />Maximum: 86400000 | False | Specify the duration, in milliseconds, for your video generator input. Enter an integer from 1 to 86400000. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | Specify the denominator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate numerator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 60000 | False | Specify the numerator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate denominator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank. |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Specify the height, in pixels, for your video generator input. This is useful for positioning when you include one or more video overlays for this input. To use the default resolution 540x360: Leave both width and height blank. To specify a height: Enter an even integer from 32 to 8192. When you do, you must also specify a value for width. |
| imageInput | string<br />Pattern: `^((s3://(.*?)\.(bmp\|BMP\|png\|PNG\|tga\|TGA))\|(https?://(.*?)\.(bmp\|BMP\|png\|PNG\|tga\|TGA)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file. |
| sampleRate | integer<br />Minimum: 32000<br />Maximum: 48000 | False | Specify the audio sample rate, in Hz, for the silent audio in your video generator input. Enter an integer from 32000 to 48000. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Specify the width, in pixels, for your video generator input. This is useful for positioning when you include one or more video overlays for this input. To use the default resolution 540x360: Leave both width and height blank. To specify a width: Enter an even integer from 32 to 8192. When you do, you must also specify a value for height. |

### InsertableImage
<a name="jobsqueries-id-model-insertableimage"></a>

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

### Job
<a name="jobsqueries-id-model-job"></a>

Each job converts an input file into an output file or files. For more information, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accelerationSettings | [AccelerationSettings](#jobsqueries-id-model-accelerationsettings) | False | Accelerated transcoding can significantly speed up jobs with long, visually complex content. |
| accelerationStatus | [AccelerationStatus](#jobsqueries-id-model-accelerationstatus) | False | Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT\_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN\_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings aren't compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT\_ACCELERATED. |
| arn | string | False | An identifier for this resource that is unique within all of AWS. |
| billingTagsSource | [BillingTagsSource](#jobsqueries-id-model-billingtagssource) | False | The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up. |
| clientRequestToken | string | False | Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html. |
| createdAt | string<br />Format: date-time | False | The time, in Unix epoch format in seconds, when the job got created. |
| currentPhase | [JobPhase](#jobsqueries-id-model-jobphase) | False | A job's phase can be PROBING, TRANSCODING OR UPLOADING |
| elementalInferenceConfiguration | [ElementalInferenceConfiguration](#jobsqueries-id-model-elementalinferenceconfiguration) | False | Elemental Inference features used in this job. |
| errorCode | integer<br />Format: int32 | False | Error code for the job |
| errorMessage | string | False | Error message of Job |
| hopDestinations | Array of type [HopDestination](#jobsqueries-id-model-hopdestination) | False | Optional list of hop destinations. |
| id | string | False | A portion of the job's ARN, unique within your AWS Elemental MediaConvert resources |
| jobEngineVersionRequested | string | False | The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format. |
| jobEngineVersionUsed | string | False | The Job engine version that your job used. Job engine versions are in a YYYY-MM-DD format. When you request an expired version, the response for this property will be empty. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested. When you request an invalid version, the response for this property will be empty. Requests to create jobs with an invalid version result in a 400 error message, and no job is created. |
| jobPercentComplete | integer | False | An estimate of how far your job has progressed. This estimate is shown as a percentage of the total time from when your job leaves its queue to when your output files appear in your output Amazon S3 bucket. AWS Elemental MediaConvert provides jobPercentComplete in CloudWatch STATUS\_UPDATE events and in the response to GetJob and ListJobs requests. The jobPercentComplete estimate is reliable for the following input containers: Quicktime, Transport Stream, MP4, and MXF. For some jobs, the service can't provide information about job progress. In those cases, jobPercentComplete returns a null value. |
| jobTemplate | string | False | The job template that the job is created from, if it is created from a job template. |
| lastShareDetails | string | False | Contains information about the most recent share attempt for the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-resource-share.html |
| messages | [JobMessages](#jobsqueries-id-model-jobmessages) | False | Provides messages from the service about jobs that you have already successfully submitted. |
| outputGroupDetails | Array of type [OutputGroupDetail](#jobsqueries-id-model-outputgroupdetail) | False | List of output group details |
| priority | integer<br />Format: int32<br />Minimum: -50<br />Maximum: 50 | False | Relative priority on the job. |
| queue | string | False | When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html |
| queueTransitions | Array of type [QueueTransition](#jobsqueries-id-model-queuetransition) | False | The job's queue hopping history. |
| retryCount | integer | False | The number of times that the service automatically attempted to process your job after encountering an error. |
| role | string | True | The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html |
| settings | [JobSettings](#jobsqueries-id-model-jobsettings) | True | JobSettings contains all the transcode settings for a job. |
| shareStatus | string<br />Values: `NOT_SHARED \| INITIATED \| SHARED` | False | A job's share status can be NOT\_SHARED, INITIATED, or SHARED |
| simulateReservedQueue | [SimulateReservedQueue](#jobsqueries-id-model-simulatereservedqueue) | False | Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default. |
| status | [JobStatus](#jobsqueries-id-model-jobstatus) | False | A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR. |
| statusUpdateInterval | [StatusUpdateInterval](#jobsqueries-id-model-statusupdateinterval) | False | Specify how often MediaConvert sends STATUS\_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. |
| timing | [Timing](#jobsqueries-id-model-timing) | False | Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds. |
| userMetadata | object | False | User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs. |
| warnings | Array of type [WarningGroup](#jobsqueries-id-model-warninggroup) | False | Contains any warning messages for the job. Use to help identify potential issues with your input, output, or job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/warning\_codes.html |

### JobMessages
<a name="jobsqueries-id-model-jobmessages"></a>

Provides messages from the service about jobs that you have already successfully submitted.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| info | Array of type string | False | List of messages that are informational only and don't indicate a problem with your job. |
| warning | Array of type string | False | List of messages that warn about conditions that might cause your job not to run or to fail. |

### JobPhase
<a name="jobsqueries-id-model-jobphase"></a>

A job's phase can be PROBING, TRANSCODING OR UPLOADING
+ `PROBING`
+ `TRANSCODING`
+ `UPLOADING`

### JobSettings
<a name="jobsqueries-id-model-jobsettings"></a>

JobSettings contains all the transcode settings for a job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adAvailOffset | integer<br />Minimum: -1000<br />Maximum: 1000 | False | When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. |
| availBlanking | [AvailBlanking](#jobsqueries-id-model-availblanking) | False | Settings for ad avail blanking. Video can be blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad avails. |
| colorConversion3DLUTSettings | Array of type [ColorConversion3DLUTSetting](#jobsqueries-id-model-colorconversion3dlutsetting) | False | Use 3D LUTs to specify custom color mapping behavior when you convert from one color space into another. You can include up to 8 different 3D LUTs. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/3d-luts.html |
| esam | [EsamSettings](#jobsqueries-id-model-esamsettings) | False | Settings for Event Signaling And Messaging (ESAM). If you don't do ad insertion, you can ignore these settings. |
| extendedDataServices | [ExtendedDataServices](#jobsqueries-id-model-extendeddataservices) | False | If your source content has EIA-608 Line 21 Data Services, enable this feature to specify what MediaConvert does with the Extended Data Services (XDS) packets. You can choose to pass through XDS packets, or remove them from the output. For more information about XDS, see EIA-608 Line Data Services, section 9.5.1.5 05h Content Advisory. |
| followSource | integer<br />Minimum: 1<br />Maximum: 150 | False | Specify the input that MediaConvert references for your default output settings. MediaConvert uses this input's Resolution, Frame rate, and Pixel aspect ratio for all outputs that you don't manually specify different output settings for. Enabling this setting will disable "Follow source" for all other inputs. If MediaConvert cannot follow your source, for example if you specify an audio-only input, MediaConvert uses the first followable input instead. In your JSON job specification, enter an integer from 1 to 150 corresponding to the order of your inputs. |
| inputs | Array of type [Input](#jobsqueries-id-model-input) | False | Use Inputs to define source file used in the transcode job. There can be multiple inputs add in a job. These inputs will be concantenated together to create the output. |
| kantarWatermark | [KantarWatermarkSettings](#jobsqueries-id-model-kantarwatermarksettings) | False | Use these settings only when you use Kantar watermarking. Specify the values that MediaConvert uses to generate and place Kantar watermarks in your output audio. These settings apply to every output in your job. In addition to specifying these values, you also need to store your Kantar credentials in AWS Secrets Manager. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html. |
| motionImageInserter | [MotionImageInserter](#jobsqueries-id-model-motionimageinserter) | False | Overlay motion graphics on top of your video. The motion graphics that you specify here appear on all outputs in all output groups. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html. |
| nielsenConfiguration | [NielsenConfiguration](#jobsqueries-id-model-nielsenconfiguration) | False | Settings for your Nielsen configuration. If you don't do Nielsen measurement and analytics, ignore these settings. When you enable Nielsen configuration, MediaConvert enables PCM to ID3 tagging for all outputs in the job. |
| nielsenNonLinearWatermark | [NielsenNonLinearWatermarkSettings](#jobsqueries-id-model-nielsennonlinearwatermarksettings) | False | Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 6.0.13 Nielsen NLM Watermark Engine Version 1.3.3 Nielsen Watermark Authenticator [SID\_TIC] Version [7.0.0] |
| outputGroups | Array of type [OutputGroup](#jobsqueries-id-model-outputgroup) | False | Contains one group of settings for each set of outputs that share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single output group as well. Required in is a group of settings that apply to the whole group. This required object depends on the value you set for Type. Type, settings object pairs are as follows. \* FILE\_GROUP\_SETTINGS, FileGroupSettings \* HLS\_GROUP\_SETTINGS, HlsGroupSettings \* DASH\_ISO\_GROUP\_SETTINGS, DashIsoGroupSettings \* MS\_SMOOTH\_GROUP\_SETTINGS, MsSmoothGroupSettings \* CMAF\_GROUP\_SETTINGS, CmafGroupSettings |
| timecodeConfig | [TimecodeConfig](#jobsqueries-id-model-timecodeconfig) | False | These settings control how the service handles timecodes throughout the job. These settings don't affect input clipping. |
| timedMetadataInsertion | [TimedMetadataInsertion](#jobsqueries-id-model-timedmetadatainsertion) | False | Insert user-defined custom ID3 metadata at timecodes that you specify. In each output that you want to include this metadata, you must set ID3 metadata to Passthrough. |

### JobStatus
<a name="jobsqueries-id-model-jobstatus"></a>

A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
+ `SUBMITTED`
+ `PROGRESSING`
+ `COMPLETE`
+ `CANCELED`
+ `ERROR`

### JobsQueryStatus
<a name="jobsqueries-id-model-jobsquerystatus"></a>

A job query's status can be SUBMITTED, PROGRESSING, COMPLETE, or ERROR.
+ `SUBMITTED`
+ `PROGRESSING`
+ `COMPLETE`
+ `ERROR`

### KantarWatermarkSettings
<a name="jobsqueries-id-model-kantarwatermarksettings"></a>

Use these settings only when you use Kantar watermarking. Specify the values that MediaConvert uses to generate and place Kantar watermarks in your output audio. These settings apply to every output in your job. In addition to specifying these values, you also need to store your Kantar credentials in AWS Secrets Manager. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelName | string<br />MinLength: 1<br />MaxLength: 20 | False | Provide an audio channel name from your Kantar audio license. |
| contentReference | string<br />Pattern: `^[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 50 | False | Specify a unique identifier for Kantar to use for this piece of content. |
| credentialsSecretName | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Provide the name of the AWS Secrets Manager secret where your Kantar credentials are stored. Note that your MediaConvert service role must provide access to this secret. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-permissions-for-mediaconvert-to-access-secrets-manager-secret.html. For instructions on creating a secret, see https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials\_basic.html, in the AWS Secrets Manager User Guide. |
| fileOffset | number<br />Format: float<br />Minimum: 0.0 | False | Optional. Specify an offset, in whole seconds, from the start of your output and the beginning of the watermarking. When you don't specify an offset, Kantar defaults to zero. |
| kantarLicenseId | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Provide your Kantar license ID number. You should get this number from Kantar. |
| kantarServerUrl | string<br />Format: uri<br />Pattern: `^https:\/\/.*.kantarmedia.*$` | False | Provide the HTTPS endpoint to the Kantar server. You should get this endpoint from Kantar. |
| logDestination | string<br />Format: uri<br />Pattern: `^s3:\/\/.*$` | False | Optional. Specify the Amazon S3 bucket where you want MediaConvert to store your Kantar watermark XML logs. When you don't specify a bucket, MediaConvert doesn't save these logs. Note that your MediaConvert service role must provide access to this location. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html |
| metadata3 | string<br />MinLength: 1<br />MaxLength: 50 | False | You can optionally use this field to specify the first timestamp that Kantar embeds during watermarking. Kantar suggests that you be very cautious when using this Kantar feature, and that you use it only on channels that are managed specifically for use with this feature by your Audience Measurement Operator. For more information about this feature, contact Kantar technical support. |
| metadata4 | string<br />MinLength: 1<br />MaxLength: 50 | False | Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters. |
| metadata5 | string<br />MinLength: 1<br />MaxLength: 50 | False | Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters. |
| metadata6 | string<br />MinLength: 1<br />MaxLength: 50 | False | Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters. |
| metadata7 | string<br />MinLength: 1<br />MaxLength: 50 | False | Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters. |
| metadata8 | string<br />MinLength: 1<br />MaxLength: 50 | False | Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters. |

### LanguageCode
<a name="jobsqueries-id-model-languagecode"></a>

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

### M2tsAudioBufferModel
<a name="jobsqueries-id-model-m2tsaudiobuffermodel"></a>

Selects between the DVB and ATSC buffer models for Dolby Digital audio.
+ `DVB`
+ `ATSC`

### M2tsAudioDuration
<a name="jobsqueries-id-model-m2tsaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### M2tsBufferModel
<a name="jobsqueries-id-model-m2tsbuffermodel"></a>

Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
+ `MULTIPLEX`
+ `NONE`

### M2tsDataPtsControl
<a name="jobsqueries-id-model-m2tsdataptscontrol"></a>

If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values.
+ `AUTO`
+ `ALIGN_TO_VIDEO`

### M2tsEbpAudioInterval
<a name="jobsqueries-id-model-m2tsebpaudiointerval"></a>

When set to VIDEO\_AND\_FIXED\_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO\_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY).
+ `VIDEO_AND_FIXED_INTERVALS`
+ `VIDEO_INTERVAL`

### M2tsEbpPlacement
<a name="jobsqueries-id-model-m2tsebpplacement"></a>

Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY).
+ `VIDEO_AND_AUDIO_PIDS`
+ `VIDEO_PID`

### M2tsEsRateInPes
<a name="jobsqueries-id-model-m2tsesrateinpes"></a>

Controls whether to include the ES Rate field in the PES header.
+ `INCLUDE`
+ `EXCLUDE`

### M2tsForceTsVideoEbpOrder
<a name="jobsqueries-id-model-m2tsforcetsvideoebporder"></a>

Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force.
+ `FORCE`
+ `DEFAULT`

### M2tsKlvMetadata
<a name="jobsqueries-id-model-m2tsklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### M2tsNielsenId3
<a name="jobsqueries-id-model-m2tsnielsenid3"></a>

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
+ `INSERT`
+ `NONE`

### M2tsPcrControl
<a name="jobsqueries-id-model-m2tspcrcontrol"></a>

When set to PCR\_EVERY\_PES\_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.
+ `PCR_EVERY_PES_PACKET`
+ `CONFIGURED_PCR_PERIOD`

### M2tsPreventBufferUnderflow
<a name="jobsqueries-id-model-m2tspreventbufferunderflow"></a>

Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete.
+ `DISABLED`
+ `ENABLED`

### M2tsRateMode
<a name="jobsqueries-id-model-m2tsratemode"></a>

When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.
+ `VBR`
+ `CBR`

### M2tsScte35Esam
<a name="jobsqueries-id-model-m2tsscte35esam"></a>

Settings for SCTE-35 signals from ESAM. Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scte35EsamPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream generated by ESAM. |

### M2tsScte35Source
<a name="jobsqueries-id-model-m2tsscte35source"></a>

For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam).
+ `PASSTHROUGH`
+ `NONE`

### M2tsSegmentationMarkers
<a name="jobsqueries-id-model-m2tssegmentationmarkers"></a>

Inserts segmentation markers at each segmentation\_time period. rai\_segstart sets the Random Access Indicator bit in the adaptation field. rai\_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi\_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp\_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
+ `NONE`
+ `RAI_SEGSTART`
+ `RAI_ADAPT`
+ `PSI_SEGSTART`
+ `EBP`
+ `EBP_LEGACY`

### M2tsSegmentationStyle
<a name="jobsqueries-id-model-m2tssegmentationstyle"></a>

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset\_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation\_time seconds. When a segmentation style of "maintain\_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation\_time seconds. Note that EBP lookahead is a slight exception to this rule.
+ `MAINTAIN_CADENCE`
+ `RESET_CADENCE`

### M2tsSettings
<a name="jobsqueries-id-model-m2tssettings"></a>

MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioBufferModel | [M2tsAudioBufferModel](#jobsqueries-id-model-m2tsaudiobuffermodel) | False | Selects between the DVB and ATSC buffer models for Dolby Digital audio. |
| audioDuration | [M2tsAudioDuration](#jobsqueries-id-model-m2tsaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioFramesPerPes | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The number of audio frames to insert for each PES packet. |
| audioPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifiers (PIDs) for any elementary audio streams you include in this output. Specify multiple PIDs as a JSON array. Default is the range 482-492. |
| audioPtsOffsetDelta | integer<br />Minimum: -10000<br />Maximum: 10000 | False | Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0. |
| bitrate | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000. |
| bufferModel | [M2tsBufferModel](#jobsqueries-id-model-m2tsbuffermodel) | False | Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions. |
| dataPTSControl | [M2tsDataPtsControl](#jobsqueries-id-model-m2tsdataptscontrol) | False | If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values. |
| dvbNitSettings | [DvbNitSettings](#jobsqueries-id-model-dvbnitsettings) | False | Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output. |
| dvbSdtSettings | [DvbSdtSettings](#jobsqueries-id-model-dvbsdtsettings) | False | Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output. |
| dvbSubPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifiers (PIDs) for DVB subtitle data included in this output. Specify multiple PIDs as a JSON array. Default is the range 460-479. |
| dvbTdtSettings | [DvbTdtSettings](#jobsqueries-id-model-dvbtdtsettings) | False | Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output. |
| dvbTeletextPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for DVB teletext data you include in this output. Default is 499. |
| ebpAudioInterval | [M2tsEbpAudioInterval](#jobsqueries-id-model-m2tsebpaudiointerval) | False | When set to VIDEO\_AND\_FIXED\_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO\_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY). |
| ebpPlacement | [M2tsEbpPlacement](#jobsqueries-id-model-m2tsebpplacement) | False | Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP\_LEGACY). |
| esRateInPes | [M2tsEsRateInPes](#jobsqueries-id-model-m2tsesrateinpes) | False | Controls whether to include the ES Rate field in the PES header. |
| forceTsVideoEbpOrder | [M2tsForceTsVideoEbpOrder](#jobsqueries-id-model-m2tsforcetsvideoebporder) | False | Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force. |
| fragmentTime | number<br />Format: float<br />Minimum: 0.0 | False | The length, in seconds, of each fragment. Only used with EBP markers. |
| klvMetadata | [M2tsKlvMetadata](#jobsqueries-id-model-m2tsklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| maxPcrInterval | integer<br />Minimum: 0<br />Maximum: 500 | False | Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream. |
| minEbpInterval | integer<br />Minimum: 0<br />Maximum: 10000 | False | When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate. |
| nielsenId3 | [M2tsNielsenId3](#jobsqueries-id-model-m2tsnielsenid3) | False | If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| nullPacketBitrate | number<br />Format: float<br />Minimum: 0.0 | False | Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pcrControl | [M2tsPcrControl](#jobsqueries-id-model-m2tspcrcontrol) | False | When set to PCR\_EVERY\_PES\_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for the program clock reference (PCR) in this output. If you do not specify a value, the service will use the value for Video PID. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | Specify the number of milliseconds between instances of the program map table (PMT) in the output transport stream. |
| pmtPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) for the program map table (PMT) itself. Default is 480. |
| preventBufferUnderflow | [M2tsPreventBufferUnderflow](#jobsqueries-id-model-m2tspreventbufferunderflow) | False | Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete. |
| privateMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the private metadata stream. Default is 503. |
| programNumber | integer<br />Minimum: 0<br />Maximum: 65535 | False | Use Program number to specify the program number used in the program map table (PMT) for this output. Default is 1. Program numbers and program map tables are parts of MPEG-2 transport stream containers, used for organizing data. |
| ptsOffset | integer<br />Minimum: 0<br />Maximum: 3600 | False | Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2. |
| ptsOffsetMode | [TsPtsOffset](#jobsqueries-id-model-tsptsoffset) | False | Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset. |
| rateMode | [M2tsRateMode](#jobsqueries-id-model-m2tsratemode) | False | When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate. |
| scte35Esam | [M2tsScte35Esam](#jobsqueries-id-model-m2tsscte35esam) | False | Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Pid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the SCTE-35 stream in the transport stream. |
| scte35Source | [M2tsScte35Source](#jobsqueries-id-model-m2tsscte35source) | False | For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam). |
| segmentationMarkers | [M2tsSegmentationMarkers](#jobsqueries-id-model-m2tssegmentationmarkers) | False | Inserts segmentation markers at each segmentation\_time period. rai\_segstart sets the Random Access Indicator bit in the adaptation field. rai\_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi\_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp\_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format. |
| segmentationStyle | [M2tsSegmentationStyle](#jobsqueries-id-model-m2tssegmentationstyle) | False | The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset\_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation\_time seconds. When a segmentation style of "maintain\_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation\_time seconds. Note that EBP lookahead is a slight exception to this rule. |
| segmentationTime | number<br />Format: float<br />Minimum: 0.0 | False | Specify the length, in seconds, of each segment. Required unless markers is set to \_none\_. |
| timedMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the ID3 metadata stream in the transport stream. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | Specify the ID for the transport stream itself in the program map table for this output. Transport stream IDs and program map tables are parts of MPEG-2 transport stream containers, used for organizing data. |
| videoPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Specify the packet identifier (PID) of the elementary video stream in the transport stream. |

### M3u8AudioDuration
<a name="jobsqueries-id-model-m3u8audioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### M3u8DataPtsControl
<a name="jobsqueries-id-model-m3u8dataptscontrol"></a>

If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values.
+ `AUTO`
+ `ALIGN_TO_VIDEO`

### M3u8NielsenId3
<a name="jobsqueries-id-model-m3u8nielsenid3"></a>

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
+ `INSERT`
+ `NONE`

### M3u8PcrControl
<a name="jobsqueries-id-model-m3u8pcrcontrol"></a>

When set to PCR\_EVERY\_PES\_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
+ `PCR_EVERY_PES_PACKET`
+ `CONFIGURED_PCR_PERIOD`

### M3u8Scte35Source
<a name="jobsqueries-id-model-m3u8scte35source"></a>

For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML.
+ `PASSTHROUGH`
+ `NONE`

### M3u8Settings
<a name="jobsqueries-id-model-m3u8settings"></a>

These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [M3u8AudioDuration](#jobsqueries-id-model-m3u8audioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| audioFramesPerPes | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The number of audio frames to insert for each PES packet. |
| audioPids | Array of type integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. |
| audioPtsOffsetDelta | integer<br />Minimum: -10000<br />Maximum: 10000 | False | Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0. |
| dataPTSControl | [M3u8DataPtsControl](#jobsqueries-id-model-m3u8dataptscontrol) | False | If you select ALIGN\_TO\_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values. |
| maxPcrInterval | integer<br />Minimum: 0<br />Maximum: 500 | False | Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream. |
| nielsenId3 | [M3u8NielsenId3](#jobsqueries-id-model-m3u8nielsenid3) | False | If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output. |
| patInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pcrControl | [M3u8PcrControl](#jobsqueries-id-model-m3u8pcrcontrol) | False | When set to PCR\_EVERY\_PES\_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream. |
| pcrPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. |
| pmtInterval | integer<br />Minimum: 0<br />Maximum: 1000 | False | The number of milliseconds between instances of this table in the output transport stream. |
| pmtPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. |
| privateMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the private metadata stream in the transport stream. |
| programNumber | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the program number field in the Program Map Table. |
| ptsOffset | integer<br />Minimum: 0<br />Maximum: 3600 | False | Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2. |
| ptsOffsetMode | [TsPtsOffset](#jobsqueries-id-model-tsptsoffset) | False | Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset. |
| scte35Pid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the SCTE-35 stream in the transport stream. |
| scte35Source | [M3u8Scte35Source](#jobsqueries-id-model-m3u8scte35source) | False | For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML. |
| timedMetadata | [TimedMetadata](#jobsqueries-id-model-timedmetadata) | False | Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank. |
| timedMetadataPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the ID3 metadata stream in the transport stream. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | False | The value of the transport stream ID field in the Program Map Table. |
| videoPid | integer<br />Minimum: 32<br />Maximum: 8182 | False | Packet Identifier (PID) of the elementary video stream in the transport stream. |

### MinBottomRenditionSize
<a name="jobsqueries-id-model-minbottomrenditionsize"></a>

Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. \* The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. \* If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this rule. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this rule. |

### MinTopRenditionSize
<a name="jobsqueries-id-model-mintoprenditionsize"></a>

Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. \* The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. \* If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this rule. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this rule. |

### MotionImageInserter
<a name="jobsqueries-id-model-motionimageinserter"></a>

Overlay motion graphics on top of your video. The motion graphics that you specify here appear on all outputs in all output groups. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerate | [MotionImageInsertionFramerate](#jobsqueries-id-model-motionimageinsertionframerate) | False | If your motion graphic asset is a .mov file, keep this setting unspecified. If your motion graphic asset is a series of .png files, specify the frame rate of the overlay in frames per second, as a fraction. For example, specify 24 fps as 24/1. Make sure that the number of images in your series matches the frame rate and your intended overlay duration. For example, if you want a 30-second overlay at 30 fps, you should have 900 .png images. This overlay frame rate doesn't need to match the frame rate of the underlying video. |
| input | string<br />Pattern: `^((s3://(.*)(\.mov\|[0-9]+\.png))\|(https?://(.*)(\.mov\|[0-9]+\.png)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`<br />MinLength: 14 | False | Specify the .mov file or series of .png files that you want to overlay on your video. For .png files, provide the file name of the first file in the series. Make sure that the names of the .png files end with sequential numbers that specify the order that they are played in. For example, overlay\_000.png, overlay\_001.png, overlay\_002.png, and so on. The sequence must start at zero, and each image file name must have the same number of digits. Pad your initial file names with enough zeros to complete the sequence. For example, if the first image is overlay\_0.png, there can be only 10 images in the sequence, with the last image being overlay\_9.png. But if the first image is overlay\_00.png, there can be 100 images in the sequence. |
| insertionMode | [MotionImageInsertionMode](#jobsqueries-id-model-motionimageinsertionmode) | False | Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files. |
| offset | [MotionImageInsertionOffset](#jobsqueries-id-model-motionimageinsertionoffset) | False | Use Offset to specify the placement of your motion graphic overlay on the video frame. Specify in pixels, from the upper-left corner of the frame. If you don't specify an offset, the service scales your overlay to the full size of the frame. Otherwise, the service inserts the overlay at its native resolution and scales the size up or down with any video scaling. |
| playback | [MotionImagePlayback](#jobsqueries-id-model-motionimageplayback) | False | Specify whether your motion graphic overlay repeats on a loop or plays only once. |
| startTime | string<br />Pattern: `^((([0-1]\d)\|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`<br />MinLength: 11<br />MaxLength: 11 | False | Specify when the motion overlay begins. Use timecode format (HH:MM:SS:FF or HH:MM:SS;FF). Make sure that the timecode you provide here takes into account how you have set up your timecode configuration under both job settings and input settings. The simplest way to do that is to set both to start at 0. If you need to set up your job to follow timecodes embedded in your source that don't start at zero, make sure that you specify a start time that is after the first embedded timecode. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-timecode.html |

### MotionImageInsertionFramerate
<a name="jobsqueries-id-model-motionimageinsertionframerate"></a>

For motion overlays that don't have a built-in frame rate, specify the frame rate of the overlay in frames per second, as a fraction. For example, specify 24 fps as 24/1. The overlay frame rate doesn't need to match the frame rate of the underlying video.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 17895697 | False | The bottom of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 1. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483640 | False | The top of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 24. |

### MotionImageInsertionMode
<a name="jobsqueries-id-model-motionimageinsertionmode"></a>

Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files.
+ `MOV`
+ `PNG`

### MotionImageInsertionOffset
<a name="jobsqueries-id-model-motionimageinsertionoffset"></a>

Specify the offset between the upper-left corner of the video frame and the top left corner of the overlay.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| imageX | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Set the distance, in pixels, between the overlay and the left edge of the video frame. |
| imageY | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Set the distance, in pixels, between the overlay and the top edge of the video frame. |

### MotionImagePlayback
<a name="jobsqueries-id-model-motionimageplayback"></a>

Specify whether your motion graphic overlay repeats on a loop or plays only once.
+ `ONCE`
+ `REPEAT`

### MovClapAtom
<a name="jobsqueries-id-model-movclapatom"></a>

When enabled, include 'clap' atom if appropriate for the video output settings.
+ `INCLUDE`
+ `EXCLUDE`

### MovCslgAtom
<a name="jobsqueries-id-model-movcslgatom"></a>

When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
+ `INCLUDE`
+ `EXCLUDE`

### MovMpeg2FourCCControl
<a name="jobsqueries-id-model-movmpeg2fourcccontrol"></a>

When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.
+ `XDCAM`
+ `MPEG`

### MovPaddingControl
<a name="jobsqueries-id-model-movpaddingcontrol"></a>

Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding.
+ `OMNEON`
+ `NONE`

### MovReference
<a name="jobsqueries-id-model-movreference"></a>

Always keep the default value (SELF\_CONTAINED) for this setting.
+ `SELF_CONTAINED`
+ `EXTERNAL`

### MovSettings
<a name="jobsqueries-id-model-movsettings"></a>

These settings relate to your QuickTime MOV output container.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clapAtom | [MovClapAtom](#jobsqueries-id-model-movclapatom) | False | When enabled, include 'clap' atom if appropriate for the video output settings. |
| cslgAtom | [MovCslgAtom](#jobsqueries-id-model-movcslgatom) | False | When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools. |
| mpeg2FourCCControl | [MovMpeg2FourCCControl](#jobsqueries-id-model-movmpeg2fourcccontrol) | False | When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2. |
| paddingControl | [MovPaddingControl](#jobsqueries-id-model-movpaddingcontrol) | False | Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding. |
| reference | [MovReference](#jobsqueries-id-model-movreference) | False | Always keep the default value (SELF\_CONTAINED) for this setting. |

### Mp2AudioDescriptionMix
<a name="jobsqueries-id-model-mp2audiodescriptionmix"></a>

Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
+ `BROADCASTER_MIXED_AD`
+ `NONE`

### Mp2Settings
<a name="jobsqueries-id-model-mp2settings"></a>

Required when you set Codec to the value MP2.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionMix | [Mp2AudioDescriptionMix](#jobsqueries-id-model-mp2audiodescriptionmix) | False | Choose BROADCASTER\_MIXED\_AD when the input contains pre-mixed main audio \+ audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER\_MIXED\_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio \+ audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType. |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 384000 | False | Specify the average bitrate in bits per second. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Set Channels to specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 0, 1, and 2. |
| sampleRate | integer<br />Minimum: 32000<br />Maximum: 48000 | False | Sample rate in Hz. |

### Mp3RateControlMode
<a name="jobsqueries-id-model-mp3ratecontrolmode"></a>

Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR).
+ `CBR`
+ `VBR`

### Mp3Settings
<a name="jobsqueries-id-model-mp3settings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 16000<br />Maximum: 320000 | False | Specify the average bitrate in bits per second. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. |
| rateControlMode | [Mp3RateControlMode](#jobsqueries-id-model-mp3ratecontrolmode) | False | Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR). |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 48000 | False | Sample rate in Hz. |
| vbrQuality | integer<br />Minimum: 0<br />Maximum: 9 | False | Required when you set Bitrate control mode to VBR. Specify the audio quality of this MP3 output from 0 (highest quality) to 9 (lowest quality). |

### Mp4C2paManifest
<a name="jobsqueries-id-model-mp4c2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### Mp4CslgAtom
<a name="jobsqueries-id-model-mp4cslgatom"></a>

When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
+ `INCLUDE`
+ `EXCLUDE`

### Mp4FreeSpaceBox
<a name="jobsqueries-id-model-mp4freespacebox"></a>

Inserts a free-space box immediately after the moov box.
+ `INCLUDE`
+ `EXCLUDE`

### Mp4MoovPlacement
<a name="jobsqueries-id-model-mp4moovplacement"></a>

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.
+ `PROGRESSIVE_DOWNLOAD`
+ `NORMAL`

### Mp4Settings
<a name="jobsqueries-id-model-mp4settings"></a>

These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html\#output-codecs-and-containers-supported-for-audio-only.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDuration | [CmfcAudioDuration](#jobsqueries-id-model-cmfcaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| c2paManifest | [Mp4C2paManifest](#jobsqueries-id-model-mp4c2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| cslgAtom | [Mp4CslgAtom](#jobsqueries-id-model-mp4cslgatom) | False | When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools. |
| cttsVersion | integer<br />Minimum: 0<br />Maximum: 1 | False | Ignore this setting unless compliance to the CTTS box version specification matters in your workflow. Specify a value of 1 to set your CTTS box version to 1 and make your output compliant with the specification. When you specify a value of 1, you must also set CSLG atom to the value INCLUDE. Keep the default value 0 to set your CTTS box version to 0. This can provide backward compatibility for some players and packagers. |
| freeSpaceBox | [Mp4FreeSpaceBox](#jobsqueries-id-model-mp4freespacebox) | False | Inserts a free-space box immediately after the moov box. |
| moovPlacement | [Mp4MoovPlacement](#jobsqueries-id-model-mp4moovplacement) | False | To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal. |
| mp4MajorBrand | string | False | Overrides the "Major Brand" field in the output file. Usually not necessary to specify. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |

### MpdAccessibilityCaptionHints
<a name="jobsqueries-id-model-mpdaccessibilitycaptionhints"></a>

Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/>
+ `INCLUDE`
+ `EXCLUDE`

### MpdAudioDuration
<a name="jobsqueries-id-model-mpdaudioduration"></a>

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.
+ `DEFAULT_CODEC_DURATION`
+ `MATCH_VIDEO_DURATION`

### MpdC2paManifest
<a name="jobsqueries-id-model-mpdc2pamanifest"></a>

When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html
+ `INCLUDE`
+ `EXCLUDE`

### MpdCaptionContainerType
<a name="jobsqueries-id-model-mpdcaptioncontainertype"></a>

Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files.
+ `RAW`
+ `FRAGMENTED_MP4`

### MpdKlvMetadata
<a name="jobsqueries-id-model-mpdklvmetadata"></a>

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.
+ `NONE`
+ `PASSTHROUGH`

### MpdManifestMetadataSignaling
<a name="jobsqueries-id-model-mpdmanifestmetadatasignaling"></a>

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.
+ `ENABLED`
+ `DISABLED`

### MpdScte35Esam
<a name="jobsqueries-id-model-mpdscte35esam"></a>

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.
+ `INSERT`
+ `NONE`

### MpdScte35Source
<a name="jobsqueries-id-model-mpdscte35source"></a>

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output.
+ `PASSTHROUGH`
+ `NONE`

### MpdSettings
<a name="jobsqueries-id-model-mpdsettings"></a>

These settings relate to the fragmented MP4 container for the segments in your DASH outputs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibilityCaptionHints | [MpdAccessibilityCaptionHints](#jobsqueries-id-model-mpdaccessibilitycaptionhints) | False | Optional. Choose Include to have MediaConvert mark up your DASH manifest with <Accessibility> elements for embedded 608 captions. This markup isn't generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest: <Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng"/> |
| audioDuration | [MpdAudioDuration](#jobsqueries-id-model-mpdaudioduration) | False | Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec. |
| c2paManifest | [MpdC2paManifest](#jobsqueries-id-model-mpdc2pamanifest) | False | When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html |
| captionContainerType | [MpdCaptionContainerType](#jobsqueries-id-model-mpdcaptioncontainertype) | False | Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files. |
| certificateSecret | string<br />Pattern: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`<br />MinLength: 1<br />MaxLength: 2048 | False | Specify the name or ARN of the AWS Secrets Manager secret that contains your C2PA public certificate chain in PEM format. Provide a valid secret name or ARN. Note that your MediaConvert service role must allow access to this secret. The public certificate chain is added to the COSE header (x5chain) for signature validation. Include the signer's certificate and all intermediate certificates. Do not include the root certificate. For details on COSE, see: https://opensource.contentauthenticity.org/docs/manifest/signing-manifests |
| klvMetadata | [MpdKlvMetadata](#jobsqueries-id-model-mpdklvmetadata) | False | To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank. |
| manifestMetadataSignaling | [MpdManifestMetadataSignaling](#jobsqueries-id-model-mpdmanifestmetadatasignaling) | False | To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be "urn:scte:scte35:2013:bin". To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough. |
| scte35Esam | [MpdScte35Esam](#jobsqueries-id-model-mpdscte35esam) | False | Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML. |
| scte35Source | [MpdScte35Source](#jobsqueries-id-model-mpdscte35source) | False | Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. |
| signingKmsKey | string<br />Pattern: `^(arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/)?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32}$`<br />MinLength: 1 | False | Specify the ID or ARN of the AWS KMS key used to sign the C2PA manifest in your MP4 output. Provide a valid KMS key ARN. Note that your MediaConvert service role must allow access to this key. |
| timedMetadata | [MpdTimedMetadata](#jobsqueries-id-model-mpdtimedmetadata) | False | To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank. |
| timedMetadataBoxVersion | [MpdTimedMetadataBoxVersion](#jobsqueries-id-model-mpdtimedmetadataboxversion) | False | Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough. |
| timedMetadataSchemeIdUri | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: https://aomedia.org/emsg/ID3 When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough. |
| timedMetadataValue | string<br />MaxLength: 1000 | False | Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough. |

### MpdTimedMetadata
<a name="jobsqueries-id-model-mpdtimedmetadata"></a>

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### MpdTimedMetadataBoxVersion
<a name="jobsqueries-id-model-mpdtimedmetadataboxversion"></a>

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.
+ `VERSION_0`
+ `VERSION_1`

### Mpeg2AdaptiveQuantization
<a name="jobsqueries-id-model-mpeg2adaptivequantization"></a>

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization.
+ `OFF`
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### Mpeg2CodecLevel
<a name="jobsqueries-id-model-mpeg2codeclevel"></a>

Use Level to set the MPEG-2 level for the video output.
+ `AUTO`
+ `LOW`
+ `MAIN`
+ `HIGH1440`
+ `HIGH`

### Mpeg2CodecProfile
<a name="jobsqueries-id-model-mpeg2codecprofile"></a>

Use Profile to set the MPEG-2 profile for the video output.
+ `MAIN`
+ `PROFILE_422`

### Mpeg2DynamicSubGop
<a name="jobsqueries-id-model-mpeg2dynamicsubgop"></a>

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.
+ `ADAPTIVE`
+ `STATIC`

### Mpeg2FramerateControl
<a name="jobsqueries-id-model-mpeg2frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Mpeg2FramerateConversionAlgorithm
<a name="jobsqueries-id-model-mpeg2framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Mpeg2GopSizeUnits
<a name="jobsqueries-id-model-mpeg2gopsizeunits"></a>

Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames.
+ `FRAMES`
+ `SECONDS`

### Mpeg2InterlaceMode
<a name="jobsqueries-id-model-mpeg2interlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### Mpeg2IntraDcPrecision
<a name="jobsqueries-id-model-mpeg2intradcprecision"></a>

Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.
+ `AUTO`
+ `INTRA_DC_PRECISION_8`
+ `INTRA_DC_PRECISION_9`
+ `INTRA_DC_PRECISION_10`
+ `INTRA_DC_PRECISION_11`

### Mpeg2ParControl
<a name="jobsqueries-id-model-mpeg2parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Mpeg2QualityTuningLevel
<a name="jobsqueries-id-model-mpeg2qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `MULTI_PASS`

### Mpeg2RateControlMode
<a name="jobsqueries-id-model-mpeg2ratecontrolmode"></a>

Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr).
+ `VBR`
+ `CBR`

### Mpeg2ScanTypeConversionMode
<a name="jobsqueries-id-model-mpeg2scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### Mpeg2SceneChangeDetect
<a name="jobsqueries-id-model-mpeg2scenechangedetect"></a>

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default.
+ `DISABLED`
+ `ENABLED`

### Mpeg2Settings
<a name="jobsqueries-id-model-mpeg2settings"></a>

Required when you set Codec to the value MPEG2.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [Mpeg2AdaptiveQuantization](#jobsqueries-id-model-mpeg2adaptivequantization) | False | Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization. |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 288000000 | False | Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000. |
| codecLevel | [Mpeg2CodecLevel](#jobsqueries-id-model-mpeg2codeclevel) | False | Use Level to set the MPEG-2 level for the video output. |
| codecProfile | [Mpeg2CodecProfile](#jobsqueries-id-model-mpeg2codecprofile) | False | Use Profile to set the MPEG-2 profile for the video output. |
| dynamicSubGop | [Mpeg2DynamicSubGop](#jobsqueries-id-model-mpeg2dynamicsubgop) | False | Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames. |
| framerateControl | [Mpeg2FramerateControl](#jobsqueries-id-model-mpeg2frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Mpeg2FramerateConversionAlgorithm](#jobsqueries-id-model-mpeg2framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. When you create a streaming output, we recommend that you keep the default value, 1, so that players starting mid-stream receive an IDR frame as quickly as possible. Don't set this value to 0; that would break output segmenting. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | Specify the interval between keyframes, in seconds or frames, for this output. Default: 12 Related settings: When you specify the GOP size in seconds, set GOP mode control to Specified, seconds. The default value for GOP mode control is Frames. |
| gopSizeUnits | [Mpeg2GopSizeUnits](#jobsqueries-id-model-mpeg2gopsizeunits) | False | Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames. |
| hrdBufferFinalFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage. |
| hrdBufferInitialFillPercentage | integer<br />Minimum: 0<br />Maximum: 100 | False | Percentage of the buffer that should initially be filled (HRD buffer model). |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| interlaceMode | [Mpeg2InterlaceMode](#jobsqueries-id-model-mpeg2interlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| intraDcPrecision | [Mpeg2IntraDcPrecision](#jobsqueries-id-model-mpeg2intradcprecision) | False | Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 300000000 | False | Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| minIInterval | integer<br />Minimum: 0<br />Maximum: 30 | False | Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size. |
| numberBFramesBetweenReferenceFrames | integer<br />Minimum: 0<br />Maximum: 7 | False | Specify the number of B-frames that MediaConvert puts between reference frames in this output. Valid values are whole numbers from 0 through 7. When you don't specify a value, MediaConvert defaults to 2. |
| parControl | [Mpeg2ParControl](#jobsqueries-id-model-mpeg2parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| qualityTuningLevel | [Mpeg2QualityTuningLevel](#jobsqueries-id-model-mpeg2qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| rateControlMode | [Mpeg2RateControlMode](#jobsqueries-id-model-mpeg2ratecontrolmode) | False | Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr). |
| scanTypeConversionMode | [Mpeg2ScanTypeConversionMode](#jobsqueries-id-model-mpeg2scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| sceneChangeDetect | [Mpeg2SceneChangeDetect](#jobsqueries-id-model-mpeg2scenechangedetect) | False | Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. |
| slowPal | [Mpeg2SlowPal](#jobsqueries-id-model-mpeg2slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless you need to comply with a specification that requires a specific value. If you don't have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, to use the AWS Elemental default matrices. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [Mpeg2SpatialAdaptiveQuantization](#jobsqueries-id-model-mpeg2spatialadaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| syntax | [Mpeg2Syntax](#jobsqueries-id-model-mpeg2syntax) | False | Specify whether this output's video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10. |
| telecine | [Mpeg2Telecine](#jobsqueries-id-model-mpeg2telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| temporalAdaptiveQuantization | [Mpeg2TemporalAdaptiveQuantization](#jobsqueries-id-model-mpeg2temporaladaptivequantization) | False | Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. |

### Mpeg2SlowPal
<a name="jobsqueries-id-model-mpeg2slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### Mpeg2SpatialAdaptiveQuantization
<a name="jobsqueries-id-model-mpeg2spatialadaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### Mpeg2Syntax
<a name="jobsqueries-id-model-mpeg2syntax"></a>

Specify whether this output's video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10.
+ `DEFAULT`
+ `D_10`

### Mpeg2Telecine
<a name="jobsqueries-id-model-mpeg2telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `SOFT`
+ `HARD`

### Mpeg2TemporalAdaptiveQuantization
<a name="jobsqueries-id-model-mpeg2temporaladaptivequantization"></a>

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### MsSmoothAdditionalManifest
<a name="jobsqueries-id-model-mssmoothadditionalmanifest"></a>

Specify the details for each additional Microsoft Smooth Streaming manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| manifestNameModifier | string<br />MinLength: 1 | False | Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your Microsoft Smooth group is film-name.ismv. If you enter "-no-premium" for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.ismv. |
| selectedOutputs | Array of type string<br />MinLength: 1 | False | Specify the outputs that you want this additional top-level manifest to reference. |

### MsSmoothAudioDeduplication
<a name="jobsqueries-id-model-mssmoothaudiodeduplication"></a>

COMBINE\_DUPLICATE\_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream.
+ `COMBINE_DUPLICATE_STREAMS`
+ `NONE`

### MsSmoothEncryptionSettings
<a name="jobsqueries-id-model-mssmoothencryptionsettings"></a>

If you are using DRM, set DRM System to specify the value SpekeKeyProvider.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spekeKeyProvider | [SpekeKeyProvider](#jobsqueries-id-model-spekekeyprovider) | False | If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead. |

### MsSmoothFragmentLengthControl
<a name="jobsqueries-id-model-mssmoothfragmentlengthcontrol"></a>

Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary.
+ `EXACT`
+ `GOP_MULTIPLE`

### MsSmoothGroupSettings
<a name="jobsqueries-id-model-mssmoothgroupsettings"></a>

Settings related to your Microsoft Smooth Streaming output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalManifests | Array of type [MsSmoothAdditionalManifest](#jobsqueries-id-model-mssmoothadditionalmanifest) | False | By default, the service creates one .ism Microsoft Smooth Streaming manifest for each Microsoft Smooth Streaming output group in your job. This default manifest references every output in the output group. To create additional manifests that reference a subset of the outputs in the output group, specify a list of them here. |
| audioDeduplication | [MsSmoothAudioDeduplication](#jobsqueries-id-model-mssmoothaudiodeduplication) | False | COMBINE\_DUPLICATE\_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream. |
| destination | string<br />Pattern: `^s3:\/\/.*$` | False | Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file. |
| destinationSettings | [DestinationSettings](#jobsqueries-id-model-destinationsettings) | False | Settings associated with the destination. Will vary based on the type of destination |
| encryption | [MsSmoothEncryptionSettings](#jobsqueries-id-model-mssmoothencryptionsettings) | False | If you are using DRM, set DRM System to specify the value SpekeKeyProvider. |
| fragmentLength | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary. |
| fragmentLengthControl | [MsSmoothFragmentLengthControl](#jobsqueries-id-model-mssmoothfragmentlengthcontrol) | False | Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary. |
| manifestEncoding | [MsSmoothManifestEncoding](#jobsqueries-id-model-mssmoothmanifestencoding) | False | Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16. |

### MsSmoothManifestEncoding
<a name="jobsqueries-id-model-mssmoothmanifestencoding"></a>

Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16.
+ `UTF8`
+ `UTF16`

### MultiViewInput
<a name="jobsqueries-id-model-multiviewinput"></a>

Input settings for MultiView Settings. You can include exactly one input as enhancement layer.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileInput | string<br />Pattern: `^s3://([^\/]+\/+)+((([^\/]*)))\|^https?://[^\/].*[^&]$` | False | Specify the input file S3, HTTP, or HTTPS URL for your right eye view video. |

### MultiViewSettings
<a name="jobsqueries-id-model-multiviewsettings"></a>

Specify the enhancement layer input video file path for Multi View outputs. The base layer input is treated as the left eye and this Multi View input is treated as the right eye. Only one Multi View input is currently supported. MediaConvert encodes both views into a single MV-HEVC output codec. When you add MultiViewSettings to your job, you can only produce Multi View outputs. Adding any other codec output to the same job is not supported.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| input | [MultiViewInput](#jobsqueries-id-model-multiviewinput) | False | Input settings for MultiView Settings. You can include exactly one input as enhancement layer. |

### MxfAfdSignaling
<a name="jobsqueries-id-model-mxfafdsignaling"></a>

Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings.
+ `NO_COPY`
+ `COPY_FROM_VIDEO`

### MxfProfile
<a name="jobsqueries-id-model-mxfprofile"></a>

Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html.
+ `D_10`
+ `XDCAM`
+ `OP1A`
+ `XAVC`
+ `XDCAM_RDD9`

### MxfSettings
<a name="jobsqueries-id-model-mxfsettings"></a>

These settings relate to your MXF output container.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| afdSignaling | [MxfAfdSignaling](#jobsqueries-id-model-mxfafdsignaling) | False | Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings. |
| profile | [MxfProfile](#jobsqueries-id-model-mxfprofile) | False | Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html. |
| uncompressedAudioWrapping | [MxfUncompressedAudioWrapping](#jobsqueries-id-model-mxfuncompressedaudiowrapping) | False | Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a. |
| xavcProfileSettings | [MxfXavcProfileSettings](#jobsqueries-id-model-mxfxavcprofilesettings) | False | Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC. |

### MxfUncompressedAudioWrapping
<a name="jobsqueries-id-model-mxfuncompressedaudiowrapping"></a>

Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a.
+ `AUTO`
+ `AES3`

### MxfXavcDurationMode
<a name="jobsqueries-id-model-mxfxavcdurationmode"></a>

To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration.
+ `ALLOW_ANY_DURATION`
+ `DROP_FRAMES_FOR_COMPLIANCE`

### MxfXavcProfileSettings
<a name="jobsqueries-id-model-mxfxavcprofilesettings"></a>

Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| durationMode | [MxfXavcDurationMode](#jobsqueries-id-model-mxfxavcdurationmode) | False | To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration. |
| maxAncDataSize | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify a value for this setting only for outputs that you set up with one of these two XAVC profiles: XAVC HD Intra CBG or XAVC 4K Intra CBG. Specify the amount of space in each frame that the service reserves for ancillary data, such as teletext captions. The default value for this setting is 1492 bytes per frame. This should be sufficient to prevent overflow unless you have multiple pages of teletext captions data. If you have a large amount of teletext data, specify a larger number. |

### NexGuardFileMarkerSettings
<a name="jobsqueries-id-model-nexguardfilemarkersettings"></a>

For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| license | string<br />MinLength: 1<br />MaxLength: 100000 | False | Use the base64 license string that Nagra provides you. Enter it directly in your JSON job specification or in the console. Required when you include Nagra NexGuard File Marker watermarking in your job. |
| payload | integer<br />Minimum: 0<br />Maximum: 4194303 | False | Specify the payload ID that you want associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. Required when you include Nagra NexGuard File Marker watermarking in your job. For PreRelease Content (NGPR/G2), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of which ID you have assigned to each asset. Neither Nagra nor MediaConvert keep track of the relationship between output files and your IDs. For OTT Streaming, create two adaptive bitrate (ABR) stacks for each asset. Do this by setting up two output groups. For one output group, set the value of Payload ID to 0 in every output. For the other output group, set Payload ID to 1 in every output. |
| preset | string<br />MinLength: 1<br />MaxLength: 256 | False | Enter one of the watermarking preset strings that Nagra provides you. Required when you include Nagra NexGuard File Marker watermarking in your job. |
| strength | [WatermarkingStrength](#jobsqueries-id-model-watermarkingstrength) | False | Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value. |

### NielsenActiveWatermarkProcessType
<a name="jobsqueries-id-model-nielsenactivewatermarkprocesstype"></a>

Choose the type of Nielsen watermarks that you want in your outputs. When you choose NAES 2 and NW, you must provide a value for the setting SID. When you choose CBET, you must provide a value for the setting CSID. When you choose NAES 2, NW, and CBET, you must provide values for both of these settings.
+ `NAES2_AND_NW`
+ `CBET`
+ `NAES2_AND_NW_AND_CBET`

### NielsenConfiguration
<a name="jobsqueries-id-model-nielsenconfiguration"></a>

Settings for your Nielsen configuration. If you don't do Nielsen measurement and analytics, ignore these settings. When you enable Nielsen configuration, MediaConvert enables PCM to ID3 tagging for all outputs in the job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| breakoutCode | integer<br />Minimum: 0<br />Maximum: 0 | False | Nielsen has discontinued the use of breakout code functionality. If you must include this property, set the value to zero. |
| distributorId | string | False | Use Distributor ID to specify the distributor ID that is assigned to your organization by Nielsen. |

### NielsenNonLinearWatermarkSettings
<a name="jobsqueries-id-model-nielsennonlinearwatermarksettings"></a>

Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 6.0.13 Nielsen NLM Watermark Engine Version 1.3.3 Nielsen Watermark Authenticator [SID\_TIC] Version [7.0.0]

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeWatermarkProcess | [NielsenActiveWatermarkProcessType](#jobsqueries-id-model-nielsenactivewatermarkprocesstype) | False | Choose the type of Nielsen watermarks that you want in your outputs. When you choose NAES 2 and NW, you must provide a value for the setting SID. When you choose CBET, you must provide a value for the setting CSID. When you choose NAES 2, NW, and CBET, you must provide values for both of these settings. |
| adiFilename | string<br />Pattern: `^s3:\/\/.*$` | False | Optional. Use this setting when you want the service to include an ADI file in the Nielsen metadata .zip file. To provide an ADI file, store it in Amazon S3 and provide a URL to it here. The URL should be in the following format: S3://bucket/path/ADI-file. For more information about the metadata .zip file, see the setting Metadata destination. |
| assetId | string<br />MinLength: 1<br />MaxLength: 20 | False | Use the asset ID that you provide to Nielsen to uniquely identify this asset. Required for all Nielsen non-linear watermarking. |
| assetName | string<br />MinLength: 1<br />MaxLength: 50 | False | Use the asset name that you provide to Nielsen for this asset. Required for all Nielsen non-linear watermarking. |
| cbetSourceId | string<br />Pattern: `(^0x[A-Fa-f0-9]{0,8}$\|^[1-9][0-9]{0,8}$)` | False | Use the CSID that Nielsen provides to you. This CBET source ID should be unique to your Nielsen account but common to all of your output assets that have CBET watermarking. Required when you choose a value for the setting Watermark types that includes CBET. |
| episodeId | string<br />MinLength: 1<br />MaxLength: 20 | False | Optional. If this asset uses an episode ID with Nielsen, provide it here. |
| metadataDestination | string<br />Pattern: `^s3:\/\/.*$` | False | Specify the Amazon S3 location where you want MediaConvert to save your Nielsen non-linear metadata .zip file. This Amazon S3 bucket must be in the same Region as the one where you do your MediaConvert transcoding. If you want to include an ADI file in this .zip file, use the setting ADI file to specify it. MediaConvert delivers the Nielsen metadata .zip files only to your metadata destination Amazon S3 bucket. It doesn't deliver the .zip files to Nielsen. You are responsible for delivering the metadata .zip files to Nielsen. |
| sourceId | integer<br />Minimum: 0<br />Maximum: 65534 | False | Use the SID that Nielsen provides to you. This source ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking. This ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking. |
| sourceWatermarkStatus | [NielsenSourceWatermarkStatusType](#jobsqueries-id-model-nielsensourcewatermarkstatustype) | False | Required. Specify whether your source content already contains Nielsen non-linear watermarks. When you set this value to Watermarked, the service fails the job. Nielsen requires that you add non-linear watermarking to only clean content that doesn't already have non-linear Nielsen watermarks. |
| ticServerUrl | string<br />Format: uri<br />Pattern: `^https:\/\/.*$` | False | Specify the endpoint for the TIC server that you have deployed and configured in the AWS Cloud. Required for all Nielsen non-linear watermarking. MediaConvert can't connect directly to a TIC server. Instead, you must use API Gateway to provide a RESTful interface between MediaConvert and a TIC server that you deploy in your AWS account. For more information on deploying a TIC server in your AWS account and the required API Gateway, contact Nielsen support. |
| uniqueTicPerAudioTrack | [NielsenUniqueTicPerAudioTrackType](#jobsqueries-id-model-nielsenuniqueticperaudiotracktype) | False | To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs. |

### NielsenSourceWatermarkStatusType
<a name="jobsqueries-id-model-nielsensourcewatermarkstatustype"></a>

Required. Specify whether your source content already contains Nielsen non-linear watermarks. When you set this value to Watermarked, the service fails the job. Nielsen requires that you add non-linear watermarking to only clean content that doesn't already have non-linear Nielsen watermarks.
+ `CLEAN`
+ `WATERMARKED`

### NielsenUniqueTicPerAudioTrackType
<a name="jobsqueries-id-model-nielsenuniqueticperaudiotracktype"></a>

To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs.
+ `RESERVE_UNIQUE_TICS_PER_TRACK`
+ `SAME_TICS_PER_TRACK`

### NoiseFilterPostTemporalSharpening
<a name="jobsqueries-id-model-noisefilterposttemporalsharpening"></a>

When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening.
+ `DISABLED`
+ `ENABLED`
+ `AUTO`

### NoiseFilterPostTemporalSharpeningStrength
<a name="jobsqueries-id-model-noisefilterposttemporalsharpeningstrength"></a>

Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening.
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### NoiseReducer
<a name="jobsqueries-id-model-noisereducer"></a>

Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| filter | [NoiseReducerFilter](#jobsqueries-id-model-noisereducerfilter) | False | Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. \* Bilateral preserves edges while reducing noise. \* Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. \* Conserve does min/max noise reduction. \* Spatial does frequency-domain filtering based on JND principles. \* Temporal optimizes video quality for complex motion. |
| filterSettings | [NoiseReducerFilterSettings](#jobsqueries-id-model-noisereducerfiltersettings) | False | Settings for a noise reducer filter |
| spatialFilterSettings | [NoiseReducerSpatialFilterSettings](#jobsqueries-id-model-noisereducerspatialfiltersettings) | False | Noise reducer filter settings for spatial filter. |
| temporalFilterSettings | [NoiseReducerTemporalFilterSettings](#jobsqueries-id-model-noisereducertemporalfiltersettings) | False | Noise reducer filter settings for temporal filter. |

### NoiseReducerFilter
<a name="jobsqueries-id-model-noisereducerfilter"></a>

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
<a name="jobsqueries-id-model-noisereducerfiltersettings"></a>

Settings for a noise reducer filter

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| strength | integer<br />Minimum: 0<br />Maximum: 3 | False | Relative strength of noise reducing filter. Higher values produce stronger filtering. |

### NoiseReducerSpatialFilterSettings
<a name="jobsqueries-id-model-noisereducerspatialfiltersettings"></a>

Noise reducer filter settings for spatial filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| postFilterSharpenStrength | integer<br />Minimum: 0<br />Maximum: 3 | False | Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength. |
| speed | integer<br />Minimum: -2<br />Maximum: 3 | False | The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value. |
| strength | integer<br />Minimum: 0<br />Maximum: 16 | False | Relative strength of noise reducing filter. Higher values produce stronger filtering. |

### NoiseReducerTemporalFilterSettings
<a name="jobsqueries-id-model-noisereducertemporalfiltersettings"></a>

Noise reducer filter settings for temporal filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aggressiveMode | integer<br />Minimum: 0<br />Maximum: 4 | False | Use Aggressive mode for content that has complex motion. Higher values produce stronger temporal filtering. This filters highly complex scenes more aggressively and creates better VQ for low bitrate outputs. |
| postTemporalSharpening | [NoiseFilterPostTemporalSharpening](#jobsqueries-id-model-noisefilterposttemporalsharpening) | False | When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening. |
| postTemporalSharpeningStrength | [NoiseFilterPostTemporalSharpeningStrength](#jobsqueries-id-model-noisefilterposttemporalsharpeningstrength) | False | Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening. |
| speed | integer<br />Minimum: -1<br />Maximum: 3 | False | The speed of the filter (higher number is faster). Low setting reduces bit rate at the cost of transcode time, high setting improves transcode time at the cost of bit rate. |
| strength | integer<br />Minimum: 0<br />Maximum: 16 | False | Specify the strength of the noise reducing filter on this output. Higher values produce stronger filtering. We recommend the following value ranges, depending on the result that you want: \* 0-2 for complexity reduction with minimal sharpness loss \* 2-8 for complexity reduction with image preservation \* 8-16 for a high level of complexity reduction |

### OpusSettings
<a name="jobsqueries-id-model-opussettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 32000<br />Maximum: 192000 | False | Optional. Specify the average bitrate in bits per second. Valid values are multiples of 8000, from 32000 through 192000. The default value is 96000, which we recommend for quality and bandwidth. |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. |
| sampleRate | integer<br />Minimum: 16000<br />Maximum: 48000 | False | Optional. Sample rate in Hz. Valid values are 16000, 24000, and 48000. The default value is 48000. |

### Output
<a name="jobsqueries-id-model-output"></a>

Each output in your job is a collection of settings that describes how you want MediaConvert to encode a single output file or stream. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/create-outputs.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptions | Array of type [AudioDescription](#jobsqueries-id-model-audiodescription) | False | Contains groups of audio encoding settings organized by audio codec. Include one instance of per output. Can contain multiple groups of encoding settings. |
| captionDescriptions | Array of type [CaptionDescription](#jobsqueries-id-model-captiondescription) | False | Contains groups of captions settings. For each output that has captions, include one instance of CaptionDescriptions. Can contain multiple groups of captions settings. |
| containerSettings | [ContainerSettings](#jobsqueries-id-model-containersettings) | False | Container specific settings. |
| extension | string<br />MaxLength: 256 | False | Use Extension to specify the file extension for outputs in File output groups. If you do not specify a value, the service will use default extensions by container type as follows \* MPEG-2 transport stream, m2ts \* Quicktime, mov \* MXF container, mxf \* MPEG-4 container, mp4 \* WebM container, webm \* Animated GIF container, gif \* No Container, the service will use codec extensions (e.g. AAC, H265, H265, AC3) |
| nameModifier | string<br />MinLength: 1<br />MaxLength: 256 | False | Use Name modifier to have the service add a string to the end of each output filename. You specify the base filename as part of your destination URI. When you create multiple outputs in the same output group, Name modifier is required. Name modifier also accepts format identifiers. For DASH ISO outputs, if you use the format identifiers $Number$ or $Time$ in one output, you must use them in the same way in all outputs of the output group. |
| outputSettings | [OutputSettings](#jobsqueries-id-model-outputsettings) | False | Specific settings for this type of output. |
| preset | string<br />MinLength: 0 | False | Use Preset to specify a preset for your transcoding settings. Provide the system or custom preset name. You can specify either Preset or Container settings, but not both. |
| videoDescription | [VideoDescription](#jobsqueries-id-model-videodescription) | False | VideoDescription contains a group of video encoding settings. The specific video settings depend on the video codec that you choose for the property codec. Include one instance of VideoDescription per output. |

### OutputChannelMapping
<a name="jobsqueries-id-model-outputchannelmapping"></a>

OutputChannel mapping settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputChannels | Array of type integer<br />Minimum: -60<br />Maximum: 6 | False | Use this setting to specify your remix values when they are integers, such as -10, 0, or 4. |
| inputChannelsFineTune | Array of type number<br />Format: float<br />Minimum: -60.0<br />Maximum: 6.0 | False | Use this setting to specify your remix values when they have a decimal component, such as -10.312, 0.08, or 4.9. MediaConvert rounds your remixing values to the nearest thousandth. |

### OutputDetail
<a name="jobsqueries-id-model-outputdetail"></a>

Details regarding output

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| durationInMs | integer | False | Duration in milliseconds |
| videoDetails | [VideoDetail](#jobsqueries-id-model-videodetail) | False | Contains details about the output's video stream |

### OutputGroup
<a name="jobsqueries-id-model-outputgroup"></a>

Group of outputs

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| automatedEncodingSettings | [AutomatedEncodingSettings](#jobsqueries-id-model-automatedencodingsettings) | False | Use automated encoding to have MediaConvert choose your encoding settings for you, based on characteristics of your input video. |
| customName | string | False | Use Custom Group Name to specify a name for the output group. This value is displayed on the console and can make your job settings JSON more human-readable. It does not affect your outputs. Use up to twelve characters that are either letters, numbers, spaces, or underscores. |
| name | string<br />MaxLength: 2048 | False | Name of the output group |
| outputGroupSettings | [OutputGroupSettings](#jobsqueries-id-model-outputgroupsettings) | False | Output Group settings, including type |
| outputs | Array of type [Output](#jobsqueries-id-model-output) | False | This object holds groups of encoding settings, one group of settings per output. |

### OutputGroupDetail
<a name="jobsqueries-id-model-outputgroupdetail"></a>

Contains details about the output groups specified in the job settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| outputDetails | Array of type [OutputDetail](#jobsqueries-id-model-outputdetail) | False | Details about the output |

### OutputGroupSettings
<a name="jobsqueries-id-model-outputgroupsettings"></a>

Output Group settings, including type

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cmafGroupSettings | [CmafGroupSettings](#jobsqueries-id-model-cmafgroupsettings) | False | Settings related to your CMAF output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. |
| dashIsoGroupSettings | [DashIsoGroupSettings](#jobsqueries-id-model-dashisogroupsettings) | False | Settings related to your DASH output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. |
| fileGroupSettings | [FileGroupSettings](#jobsqueries-id-model-filegroupsettings) | False | Settings related to your File output group. MediaConvert uses this group of settings to generate a single standalone file, rather than a streaming package. |
| hlsGroupSettings | [HlsGroupSettings](#jobsqueries-id-model-hlsgroupsettings) | False | Settings related to your HLS output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. |
| msSmoothGroupSettings | [MsSmoothGroupSettings](#jobsqueries-id-model-mssmoothgroupsettings) | False | Settings related to your Microsoft Smooth Streaming output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| type | [OutputGroupType](#jobsqueries-id-model-outputgrouptype) | False | Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF) |

### OutputGroupType
<a name="jobsqueries-id-model-outputgrouptype"></a>

Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)
+ `HLS_GROUP_SETTINGS`
+ `DASH_ISO_GROUP_SETTINGS`
+ `FILE_GROUP_SETTINGS`
+ `MS_SMOOTH_GROUP_SETTINGS`
+ `CMAF_GROUP_SETTINGS`

### OutputSdt
<a name="jobsqueries-id-model-outputsdt"></a>

Selects method of inserting SDT information into output stream. "Follow input SDT" copies SDT information from input stream to output stream. "Follow input SDT if present" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter "SDT Manually" means user will enter the SDT information. "No SDT" means output stream will not contain SDT information.
+ `SDT_FOLLOW`
+ `SDT_FOLLOW_IF_PRESENT`
+ `SDT_MANUAL`
+ `SDT_NONE`

### OutputSettings
<a name="jobsqueries-id-model-outputsettings"></a>

Specific settings for this type of output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsSettings | [HlsSettings](#jobsqueries-id-model-hlssettings) | False | Settings for HLS output groups |

### PadVideo
<a name="jobsqueries-id-model-padvideo"></a>

Use this setting if your input has video and audio durations that don't align, and your output or player has strict alignment requirements. Examples: Input audio track has a delayed start. Input video track ends before audio ends. When you set Pad video to Black, MediaConvert generates black video frames so that output video and audio durations match. Black video frames are added at the beginning or end, depending on your input. To keep the default behavior and not generate black video, set Pad video to Disabled or leave blank.
+ `DISABLED`
+ `BLACK`

### PartnerWatermarking
<a name="jobsqueries-id-model-partnerwatermarking"></a>

If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nexguardFileMarkerSettings | [NexGuardFileMarkerSettings](#jobsqueries-id-model-nexguardfilemarkersettings) | False | For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows. |

### PassthroughSettings
<a name="jobsqueries-id-model-passthroughsettings"></a>

Optional settings when you set Codec to the value Passthrough.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| frameControl | [FrameControl](#jobsqueries-id-model-framecontrol) | False | Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players. |
| videoSelectorMode | [VideoSelectorMode](#jobsqueries-id-model-videoselectormode) | False | AUTO will select the highest bitrate input in the video selector source. REMUX\_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX\_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source. |

### PresetSpeke20Audio
<a name="jobsqueries-id-model-presetspeke20audio"></a>

Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted).
+ `PRESET_AUDIO_1`
+ `PRESET_AUDIO_2`
+ `PRESET_AUDIO_3`
+ `SHARED`
+ `UNENCRYPTED`

### PresetSpeke20Video
<a name="jobsqueries-id-model-presetspeke20video"></a>

Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted).
+ `PRESET_VIDEO_1`
+ `PRESET_VIDEO_2`
+ `PRESET_VIDEO_3`
+ `PRESET_VIDEO_4`
+ `PRESET_VIDEO_5`
+ `PRESET_VIDEO_6`
+ `PRESET_VIDEO_7`
+ `PRESET_VIDEO_8`
+ `SHARED`
+ `UNENCRYPTED`

### ProresChromaSampling
<a name="jobsqueries-id-model-proreschromasampling"></a>

This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10\+, or Noise reducer.
+ `PRESERVE_444_SAMPLING`
+ `SUBSAMPLE_TO_422`

### ProresCodecProfile
<a name="jobsqueries-id-model-prorescodecprofile"></a>

Use Profile to specify the type of Apple ProRes codec to use for this output.
+ `APPLE_PRORES_422`
+ `APPLE_PRORES_422_HQ`
+ `APPLE_PRORES_422_LT`
+ `APPLE_PRORES_422_PROXY`
+ `APPLE_PRORES_4444`
+ `APPLE_PRORES_4444_XQ`

### ProresFramerateControl
<a name="jobsqueries-id-model-proresframeratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### ProresFramerateConversionAlgorithm
<a name="jobsqueries-id-model-proresframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### ProresInterlaceMode
<a name="jobsqueries-id-model-proresinterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### ProresParControl
<a name="jobsqueries-id-model-proresparcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### ProresScanTypeConversionMode
<a name="jobsqueries-id-model-proresscantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### ProresSettings
<a name="jobsqueries-id-model-proressettings"></a>

Required when you set Codec to the value PRORES.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| chromaSampling | [ProresChromaSampling](#jobsqueries-id-model-proreschromasampling) | False | This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10\+, or Noise reducer. |
| codecProfile | [ProresCodecProfile](#jobsqueries-id-model-prorescodecprofile) | False | Use Profile to specify the type of Apple ProRes codec to use for this output. |
| framerateControl | [ProresFramerateControl](#jobsqueries-id-model-proresframeratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [ProresFramerateConversionAlgorithm](#jobsqueries-id-model-proresframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [ProresInterlaceMode](#jobsqueries-id-model-proresinterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| parControl | [ProresParControl](#jobsqueries-id-model-proresparcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| scanTypeConversionMode | [ProresScanTypeConversionMode](#jobsqueries-id-model-proresscantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [ProresSlowPal](#jobsqueries-id-model-proresslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25. |
| telecine | [ProresTelecine](#jobsqueries-id-model-prorestelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### ProresSlowPal
<a name="jobsqueries-id-model-proresslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### ProresTelecine
<a name="jobsqueries-id-model-prorestelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### QueueTransition
<a name="jobsqueries-id-model-queuetransition"></a>

Description of the source and destination queues between which the job has moved, along with the timestamp of the move

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationQueue | string | False | The queue that the job was on after the transition. |
| sourceQueue | string | False | The queue that the job was on before the transition. |
| timestamp | string<br />Format: date-time | False | The time, in Unix epoch format, that the job moved from the source queue to the destination queue. |

### Rectangle
<a name="jobsqueries-id-model-rectangle"></a>

Use Rectangle to identify a specific area of the video frame.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 2<br />Maximum: 2147483647 | False | Height of rectangle in pixels. Specify only even numbers. |
| width | integer<br />Minimum: 2<br />Maximum: 2147483647 | False | Width of rectangle in pixels. Specify only even numbers. |
| x | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers. |
| y | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers. |

### RemixSettings
<a name="jobsqueries-id-model-remixsettings"></a>

Use Manual audio remixing to adjust audio levels for each audio channel in each output of your job. With audio remixing, you can output more or fewer audio channels than your input audio source provides.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioDescriptionAudioChannel | integer<br />Minimum: 1<br />Maximum: 64 | False | Optionally specify the channel in your input that contains your audio description audio signal. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description audio channel, you must also specify an audio description data channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers. |
| audioDescriptionDataChannel | integer<br />Minimum: 1<br />Maximum: 64 | False | Optionally specify the channel in your input that contains your audio description data stream. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description data channel, you must also specify an audio description audio channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers. |
| channelMapping | [ChannelMapping](#jobsqueries-id-model-channelmapping) | False | Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Don't use both. |
| channelsIn | integer<br />Minimum: 1<br />Maximum: 64 | False | Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different. If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping. |
| channelsOut | integer<br />Minimum: 1<br />Maximum: 64 | False | Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and even numbers to 64.) If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping. |

### RemoveRubyReserveAttributes
<a name="jobsqueries-id-model-removerubyreserveattributes"></a>

Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### RequiredFlag
<a name="jobsqueries-id-model-requiredflag"></a>

Set to ENABLED to force a rendition to be included.
+ `ENABLED`
+ `DISABLED`

### RespondToAfd
<a name="jobsqueries-id-model-respondtoafd"></a>

Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. \* Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. \* Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. \* Choose None to remove all input AFD values from this output.
+ `NONE`
+ `RESPOND`
+ `PASSTHROUGH`

### RuleType
<a name="jobsqueries-id-model-ruletype"></a>

Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. \* The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. \* If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution. Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. \* The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. \* If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size. Use Force include renditions to specify one or more resolutions to include your ABR stack. \* (Recommended) To optimize automated ABR, specify as few resolutions as possible. \* (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. \* If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. \* If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. \* If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. \* Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting. Use Allowed renditions to specify a list of possible resolutions in your ABR stack. \* (Required) The number of resolutions that you specify must be equal to, or greater than, the Max renditions setting. \* MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. \* Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. \* You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. \* If you specify Allowed renditions, you must not specify a separate rule for Force include renditions.
+ `MIN_TOP_RENDITION_SIZE`
+ `MIN_BOTTOM_RENDITION_SIZE`
+ `FORCE_INCLUDE_RENDITIONS`
+ `ALLOWED_RENDITIONS`

### S3DestinationAccessControl
<a name="jobsqueries-id-model-s3destinationaccesscontrol"></a>

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you don't use this setting, S3 automatically applies the default access control list PRIVATE.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cannedAcl | [S3ObjectCannedAcl](#jobsqueries-id-model-s3objectcannedacl) | False | Choose an Amazon S3 canned ACL for MediaConvert to apply to this output. |

### S3DestinationSettings
<a name="jobsqueries-id-model-s3destinationsettings"></a>

Settings associated with S3 destination

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessControl | [S3DestinationAccessControl](#jobsqueries-id-model-s3destinationaccesscontrol) | False | Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you don't use this setting, S3 automatically applies the default access control list PRIVATE. |
| encryption | [S3EncryptionSettings](#jobsqueries-id-model-s3encryptionsettings) | False | Settings for how your job outputs are encrypted as they are uploaded to Amazon S3. |
| storageClass | [S3StorageClass](#jobsqueries-id-model-s3storageclass) | False | Specify the S3 storage class to use for this output. To use your destination's default storage class: Keep the default value, Not set. For more information about S3 storage classes, see https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html |

### S3EncryptionSettings
<a name="jobsqueries-id-model-s3encryptionsettings"></a>

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionType | [S3ServerSideEncryptionType](#jobsqueries-id-model-s3serversideencryptiontype) | False | Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN. |
| kmsEncryptionContext | string<br />Pattern: `^[A-Za-z0-9+\/]+={0,2}$` | False | Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html\#encrypt\_context. |
| kmsKeyArn | string<br />Pattern: `^arn:aws(-us-gov\|-cn)?:kms:[a-z-]{2,6}-(east\|west\|central\|((north\|south)(east\|west)?))-[1-9]{1,2}:\d{12}:key/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|mrk-[a-fA-F0-9]{32})$` | False | Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3. |

### S3ObjectCannedAcl
<a name="jobsqueries-id-model-s3objectcannedacl"></a>

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.
+ `PUBLIC_READ`
+ `AUTHENTICATED_READ`
+ `BUCKET_OWNER_READ`
+ `BUCKET_OWNER_FULL_CONTROL`

### S3ServerSideEncryptionType
<a name="jobsqueries-id-model-s3serversideencryptiontype"></a>

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.
+ `SERVER_SIDE_ENCRYPTION_S3`
+ `SERVER_SIDE_ENCRYPTION_KMS`

### S3StorageClass
<a name="jobsqueries-id-model-s3storageclass"></a>

Specify the S3 storage class to use for this output. To use your destination's default storage class: Keep the default value, Not set. For more information about S3 storage classes, see https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
+ `STANDARD`
+ `REDUCED_REDUNDANCY`
+ `STANDARD_IA`
+ `ONEZONE_IA`
+ `INTELLIGENT_TIERING`
+ `GLACIER`
+ `DEEP_ARCHIVE`

### SampleRangeConversion
<a name="jobsqueries-id-model-samplerangeconversion"></a>

Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output.
+ `LIMITED_RANGE_SQUEEZE`
+ `NONE`
+ `LIMITED_RANGE_CLIP`

### ScalingBehavior
<a name="jobsqueries-id-model-scalingbehavior"></a>

Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported).
+ `DEFAULT`
+ `STRETCH_TO_OUTPUT`
+ `FIT`
+ `FIT_NO_UPSCALE`
+ `FILL`
+ `SMART_CROP`

### SccDestinationFramerate
<a name="jobsqueries-id-model-sccdestinationframerate"></a>

Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video\_insertion=true and drop\_frame\_timecode=true; otherwise, choose 29.97 non-dropframe.
+ `FRAMERATE_23_97`
+ `FRAMERATE_24`
+ `FRAMERATE_25`
+ `FRAMERATE_29_97_DROPFRAME`
+ `FRAMERATE_29_97_NON_DROPFRAME`

### SccDestinationSettings
<a name="jobsqueries-id-model-sccdestinationsettings"></a>

Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerate | [SccDestinationFramerate](#jobsqueries-id-model-sccdestinationframerate) | False | Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video\_insertion=true and drop\_frame\_timecode=true; otherwise, choose 29.97 non-dropframe. |

### SimulateReservedQueue
<a name="jobsqueries-id-model-simulatereservedqueue"></a>

Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default.
+ `DISABLED`
+ `ENABLED`

### SlowPalPitchCorrection
<a name="jobsqueries-id-model-slowpalpitchcorrection"></a>

Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### SpekeKeyProvider
<a name="jobsqueries-id-model-spekekeyprovider"></a>

If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />Pattern: `^arn:aws(-us-gov)?:acm:.*$` | False | If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificate's Amazon Resource Name (ARN) here. |
| encryptionContractConfiguration | [EncryptionContractConfiguration](#jobsqueries-id-model-encryptioncontractconfiguration) | False | Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset. |
| resourceId | string | False | Specify the resource ID that your SPEKE-compliant key provider uses to identify this content. |
| systemIds | Array of type string<br />Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$` | False | Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. HLS output groups support a max of 3 system ids. Other group types support one system id. See https://dashif.org/identifiers/content\_protection/ for more details. |
| url | string<br />Format: uri<br />Pattern: `^https:\/\/[^:@\/]*(:\d*)?(\/.*)?$` | False | Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content. |

### SpekeKeyProviderCmaf
<a name="jobsqueries-id-model-spekekeyprovidercmaf"></a>

If your output group type is CMAF, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider settings instead.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />Pattern: `^arn:aws(-us-gov)?:acm:.*$` | False | If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificate's Amazon Resource Name (ARN) here. |
| dashSignaledSystemIds | Array of type string<br />Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`<br />MinLength: 36<br />MaxLength: 36 | False | Specify the DRM system IDs that you want signaled in the DASH manifest that MediaConvert creates as part of this CMAF package. The DASH manifest can currently signal up to three system IDs. For more information, see https://dashif.org/identifiers/content\_protection/. |
| encryptionContractConfiguration | [EncryptionContractConfiguration](#jobsqueries-id-model-encryptioncontractconfiguration) | False | Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset. |
| hlsSignaledSystemIds | Array of type string<br />Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`<br />MinLength: 36<br />MaxLength: 36 | False | Specify up to 3 DRM system IDs that you want signaled in the HLS manifest that MediaConvert creates as part of this CMAF package. For more information, see https://dashif.org/identifiers/content\_protection/. |
| resourceId | string<br />Pattern: `^[\w-]+$` | False | Specify the resource ID that your SPEKE-compliant key provider uses to identify this content. |
| url | string<br />Format: uri<br />Pattern: `^https:\/\/[^:@\/]*(:\d*)?(\/.*)?$` | False | Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content. |

### SrtDestinationSettings
<a name="jobsqueries-id-model-srtdestinationsettings"></a>

Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stylePassthrough | [SrtStylePassthrough](#jobsqueries-id-model-srtstylepassthrough) | False | Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions. |

### SrtStylePassthrough
<a name="jobsqueries-id-model-srtstylepassthrough"></a>

Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions.
+ `ENABLED`
+ `DISABLED`

### StaticKeyProvider
<a name="jobsqueries-id-model-statickeyprovider"></a>

Use these settings to set up encryption with a static key provider.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| keyFormat | string<br />Pattern: `^(identity\|[A-Za-z]{2,6}(\.[A-Za-z0-9-]{1,63})+)$` | False | Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS string. May be omitted to indicate an implicit value of 'identity'. |
| keyFormatVersions | string<br />Pattern: `^(\d+(\/\d+)*)$` | False | Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3). |
| staticKeyValue | string<br />Pattern: `^[A-Za-z0-9]{32}$` | False | Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value. |
| url | string<br />Format: uri | False | Relates to DRM implementation. The location of the license server used for protecting content. |

### StatusUpdateInterval
<a name="jobsqueries-id-model-statusupdateinterval"></a>

Specify how often MediaConvert sends STATUS\_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.
+ `SECONDS_10`
+ `SECONDS_12`
+ `SECONDS_15`
+ `SECONDS_20`
+ `SECONDS_30`
+ `SECONDS_60`
+ `SECONDS_120`
+ `SECONDS_180`
+ `SECONDS_240`
+ `SECONDS_300`
+ `SECONDS_360`
+ `SECONDS_420`
+ `SECONDS_480`
+ `SECONDS_540`
+ `SECONDS_600`

### TamsGapHandling
<a name="jobsqueries-id-model-tamsgaphandling"></a>

Specify how MediaConvert handles gaps between media segments in your TAMS source. Gaps can occur in live streams due to network issues or other interruptions. Choose from the following options: \* Skip gaps - Default. Skip over gaps and join segments together. This creates a continuous output with no blank frames, but may cause timeline discontinuities. \* Fill with black - Insert black frames to fill gaps between segments. This maintains timeline continuity but adds black frames where content is missing. \* Hold last frame - Repeat the last frame before a gap until the next segment begins. This maintains visual continuity during gaps.
+ `SKIP_GAPS`
+ `FILL_WITH_BLACK`
+ `HOLD_LAST_FRAME`

### TeletextDestinationSettings
<a name="jobsqueries-id-model-teletextdestinationsettings"></a>

Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pageNumber | string<br />Pattern: `^[1-8][0-9a-fA-F][0-9a-eA-E]$`<br />MinLength: 3<br />MaxLength: 3 | False | Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field. |
| pageTypes | Array of type [TeletextPageType](#jobsqueries-id-model-teletextpagetype) | False | Specify the page types for this Teletext page. If you don't specify a value here, the service sets the page type to the default value Subtitle. If you pass through the entire set of Teletext data, don't use this field. When you pass through a set of Teletext pages, your output has the same page types as your input. |

### TeletextPageType
<a name="jobsqueries-id-model-teletextpagetype"></a>

A page type as defined in the standard ETSI EN 300 468, Table 94
+ `PAGE_TYPE_INITIAL`
+ `PAGE_TYPE_SUBTITLE`
+ `PAGE_TYPE_ADDL_INFO`
+ `PAGE_TYPE_PROGRAM_SCHEDULE`
+ `PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE`

### TeletextSourceSettings
<a name="jobsqueries-id-model-teletextsourcesettings"></a>

Settings specific to Teletext caption sources, including Page number.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pageNumber | string<br />Pattern: `^[1-8][0-9a-fA-F][0-9a-eA-E]$`<br />MinLength: 3<br />MaxLength: 3 | False | Use Page Number to specify the three-digit hexadecimal page number that will be used for Teletext captions. Do not use this setting if you are passing through teletext from the input source to output. |

### TimecodeBurnin
<a name="jobsqueries-id-model-timecodeburnin"></a>

Settings for burning the output timecode and specified prefix into the output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fontSize | integer<br />Minimum: 10<br />Maximum: 48 | False | Use Font size to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48. |
| position | [TimecodeBurninPosition](#jobsqueries-id-model-timecodeburninposition) | False | Use Position under Timecode burn-in to specify the location the burned-in timecode on output video. |
| prefix | string<br />Pattern: `^[ -~]+$` | False | Use Prefix to place ASCII characters before any burned-in timecode. For example, a prefix of "EZ-" will result in the timecode "EZ-00:00:00:00". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard. |

### TimecodeBurninPosition
<a name="jobsqueries-id-model-timecodeburninposition"></a>

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

### TimecodeConfig
<a name="jobsqueries-id-model-timecodeconfig"></a>

These settings control how the service handles timecodes throughout the job. These settings don't affect input clipping.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anchor | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | If you use an editing platform that relies on an anchor timecode, use Anchor Timecode to specify a timecode that will match the input video frame to the output video frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores frame rate conversion. System behavior for Anchor Timecode varies depending on your setting for Source. \* If Source is set to Specified Start, the first input frame is the specified value in Start Timecode. Anchor Timecode and Start Timecode are used calculate output timecode. \* If Source is set to Start at 0 the first frame is 00:00:00:00. \* If Source is set to Embedded, the first frame is the timecode value on the first input frame of the input. |
| source | [TimecodeSource](#jobsqueries-id-model-timecodesource) | False | Use Source to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). \* Embedded - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 instead. \* Start at 0 - Set the timecode of the initial frame to 00:00:00:00. \* Specified Start - Set the timecode of the initial frame to a value other than zero. You use Start timecode to provide this value. |
| start | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Only use when you set Source to Specified start. Use Start timecode to specify the timecode for the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). |
| timestampOffset | string<br />Pattern: `^([0-9]{4})-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])$` | False | Only applies to outputs that support program-date-time stamp. Use Timestamp offset to overwrite the timecode date without affecting the time and frame number. Provide the new date as a string in the format "yyyy-mm-dd". To use Timestamp offset, you must also enable Insert program-date-time in the output settings. For example, if the date part of your timecodes is 2002-1-25 and you want to change it to one year later, set Timestamp offset to 2003-1-25. |

### TimecodeSource
<a name="jobsqueries-id-model-timecodesource"></a>

Use Source to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). \* Embedded - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 instead. \* Start at 0 - Set the timecode of the initial frame to 00:00:00:00. \* Specified Start - Set the timecode of the initial frame to a value other than zero. You use Start timecode to provide this value.
+ `EMBEDDED`
+ `ZEROBASED`
+ `SPECIFIEDSTART`

### TimecodeTrack
<a name="jobsqueries-id-model-timecodetrack"></a>

To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled.
+ `DISABLED`
+ `ENABLED`

### TimedMetadata
<a name="jobsqueries-id-model-timedmetadata"></a>

Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank.
+ `PASSTHROUGH`
+ `NONE`

### TimedMetadataInsertion
<a name="jobsqueries-id-model-timedmetadatainsertion"></a>

Insert user-defined custom ID3 metadata at timecodes that you specify. In each output that you want to include this metadata, you must set ID3 metadata to Passthrough.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id3Insertions | Array of type [Id3Insertion](#jobsqueries-id-model-id3insertion) | False | Id3Insertions contains the array of Id3Insertion instances. |

### Timing
<a name="jobsqueries-id-model-timing"></a>

Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| finishTime | string<br />Format: date-time | False | The time, in Unix epoch format, that the transcoding job finished |
| startTime | string<br />Format: date-time | False | The time, in Unix epoch format, that transcoding for the job began. |
| submitTime | string<br />Format: date-time | False | The time, in Unix epoch format, that you submitted the job. |

### TrackSourceSettings
<a name="jobsqueries-id-model-tracksourcesettings"></a>

Settings specific to caption sources that are specified by track number. Currently, this is only IMSC captions in an IMF package. If your caption source is IMSC 1.1 in a separate xml file, use FileSourceSettings instead of TrackSourceSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| streamNumber | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Use this setting to select a single captions track from a source. Stream numbers include all tracks in the source file, regardless of type, and correspond to either the order of tracks in the file, or if applicable, the stream number metadata of the track. Although all tracks count toward these stream numbers, in this caption selector context, only the stream number of a track containing caption data may be used. To include more than one captions track in your job outputs, create multiple input captions selectors. Specify one stream per selector. If your source file contains a track which is not recognized by the service, then the corresponding stream number will still be reserved for future use. If more types of caption data get recognized in the future, these numberings will not shift. |
| trackNumber | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Use this setting to select a single captions track from a source. Track numbers correspond to the order in the captions source file. For IMF sources, track numbering is based on the order that the captions appear in the CPL. For example, use 1 to select the captions asset that is listed first in the CPL. To include more than one captions track in your job outputs, create multiple input captions selectors. Specify one track per selector. If more types of caption data get recognized in the future, these numberings may shift, but the numberings used for streamNumber will not. |

### TsPtsOffset
<a name="jobsqueries-id-model-tsptsoffset"></a>

Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset.
+ `AUTO`
+ `SECONDS`
+ `MILLISECONDS`

### TtmlDestinationSettings
<a name="jobsqueries-id-model-ttmldestinationsettings"></a>

Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stylePassthrough | [TtmlStylePassthrough](#jobsqueries-id-model-ttmlstylepassthrough) | False | Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output. |

### TtmlStylePassthrough
<a name="jobsqueries-id-model-ttmlstylepassthrough"></a>

Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output.
+ `ENABLED`
+ `DISABLED`

### UncompressedFourcc
<a name="jobsqueries-id-model-uncompressedfourcc"></a>

The four character code for the uncompressed video.
+ `I420`
+ `I422`
+ `I444`

### UncompressedFramerateControl
<a name="jobsqueries-id-model-uncompressedframeratecontrol"></a>

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### UncompressedFramerateConversionAlgorithm
<a name="jobsqueries-id-model-uncompressedframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### UncompressedInterlaceMode
<a name="jobsqueries-id-model-uncompressedinterlacemode"></a>

Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output.
+ `INTERLACED`
+ `PROGRESSIVE`

### UncompressedScanTypeConversionMode
<a name="jobsqueries-id-model-uncompressedscantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### UncompressedSettings
<a name="jobsqueries-id-model-uncompressedsettings"></a>

Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fourcc | [UncompressedFourcc](#jobsqueries-id-model-uncompressedfourcc) | False | The four character code for the uncompressed video. |
| framerateControl | [UncompressedFramerateControl](#jobsqueries-id-model-uncompressedframeratecontrol) | False | Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [UncompressedFramerateConversionAlgorithm](#jobsqueries-id-model-uncompressedframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [UncompressedInterlaceMode](#jobsqueries-id-model-uncompressedinterlacemode) | False | Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output. |
| scanTypeConversionMode | [UncompressedScanTypeConversionMode](#jobsqueries-id-model-uncompressedscantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [UncompressedSlowPal](#jobsqueries-id-model-uncompressedslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25. |
| telecine | [UncompressedTelecine](#jobsqueries-id-model-uncompressedtelecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |

### UncompressedSlowPal
<a name="jobsqueries-id-model-uncompressedslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### UncompressedTelecine
<a name="jobsqueries-id-model-uncompressedtelecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### Vc3Class
<a name="jobsqueries-id-model-vc3class"></a>

Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output.
+ `CLASS_145_8BIT`
+ `CLASS_220_8BIT`
+ `CLASS_220_10BIT`

### Vc3FramerateControl
<a name="jobsqueries-id-model-vc3frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vc3FramerateConversionAlgorithm
<a name="jobsqueries-id-model-vc3framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vc3InterlaceMode
<a name="jobsqueries-id-model-vc3interlacemode"></a>

Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output.
+ `INTERLACED`
+ `PROGRESSIVE`

### Vc3ScanTypeConversionMode
<a name="jobsqueries-id-model-vc3scantypeconversionmode"></a>

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.
+ `INTERLACED`
+ `INTERLACED_OPTIMIZE`

### Vc3Settings
<a name="jobsqueries-id-model-vc3settings"></a>

Required when you set Codec to the value VC3

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| framerateControl | [Vc3FramerateControl](#jobsqueries-id-model-vc3frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vc3FramerateConversionAlgorithm](#jobsqueries-id-model-vc3framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| interlaceMode | [Vc3InterlaceMode](#jobsqueries-id-model-vc3interlacemode) | False | Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output. |
| scanTypeConversionMode | [Vc3ScanTypeConversionMode](#jobsqueries-id-model-vc3scantypeconversionmode) | False | Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive. |
| slowPal | [Vc3SlowPal](#jobsqueries-id-model-vc3slowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25. |
| telecine | [Vc3Telecine](#jobsqueries-id-model-vc3telecine) | False | When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture. |
| vc3Class | [Vc3Class](#jobsqueries-id-model-vc3class) | False | Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output. |

### Vc3SlowPal
<a name="jobsqueries-id-model-vc3slowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.
+ `DISABLED`
+ `ENABLED`

### Vc3Telecine
<a name="jobsqueries-id-model-vc3telecine"></a>

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.
+ `NONE`
+ `HARD`

### VchipAction
<a name="jobsqueries-id-model-vchipaction"></a>

The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions.
+ `PASSTHROUGH`
+ `STRIP`

### VideoCodec
<a name="jobsqueries-id-model-videocodec"></a>

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
<a name="jobsqueries-id-model-videocodecsettings"></a>

Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. \* AV1, Av1Settings \* AVC\_INTRA, AvcIntraSettings \* FRAME\_CAPTURE, FrameCaptureSettings \* GIF, GifSettings \* H\_264, H264Settings \* H\_265, H265Settings \* MPEG2, Mpeg2Settings \* PRORES, ProresSettings \* UNCOMPRESSED, UncompressedSettings \* VC3, Vc3Settings \* VP8, Vp8Settings \* VP9, Vp9Settings \* XAVC, XavcSettings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| av1Settings | [Av1Settings](#jobsqueries-id-model-av1settings) | False | Required when you set Codec, under VideoDescription>CodecSettings to the value AV1. |
| avcIntraSettings | [AvcIntraSettings](#jobsqueries-id-model-avcintrasettings) | False | Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf. |
| codec | [VideoCodec](#jobsqueries-id-model-videocodec) | False | Specifies the video codec. This must be equal to one of the enum values defined by the object VideoCodec. To passthrough the video stream of your input without any video encoding: Choose Passthrough. More information about passthrough codec support and job settings requirements, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/video-passthrough-feature-restrictions.html |
| frameCaptureSettings | [FrameCaptureSettings](#jobsqueries-id-model-framecapturesettings) | False | Required when you set Codec to the value FRAME\_CAPTURE. |
| gifSettings | [GifSettings](#jobsqueries-id-model-gifsettings) | False | Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF |
| h264Settings | [H264Settings](#jobsqueries-id-model-h264settings) | False | Required when you set Codec to the value H\_264. |
| h265Settings | [H265Settings](#jobsqueries-id-model-h265settings) | False | Settings for H265 codec |
| mpeg2Settings | [Mpeg2Settings](#jobsqueries-id-model-mpeg2settings) | False | Required when you set Codec to the value MPEG2. |
| passthroughSettings | [PassthroughSettings](#jobsqueries-id-model-passthroughsettings) | False | Optional settings when you set Codec to the value Passthrough. |
| proresSettings | [ProresSettings](#jobsqueries-id-model-proressettings) | False | Required when you set Codec to the value PRORES. |
| uncompressedSettings | [UncompressedSettings](#jobsqueries-id-model-uncompressedsettings) | False | Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED. |
| vc3Settings | [Vc3Settings](#jobsqueries-id-model-vc3settings) | False | Required when you set Codec to the value VC3 |
| vp8Settings | [Vp8Settings](#jobsqueries-id-model-vp8settings) | False | Required when you set Codec to the value VP8. |
| vp9Settings | [Vp9Settings](#jobsqueries-id-model-vp9settings) | False | Required when you set Codec to the value VP9. |
| xavcSettings | [XavcSettings](#jobsqueries-id-model-xavcsettings) | False | Required when you set Codec to the value XAVC. |

### VideoDescription
<a name="jobsqueries-id-model-videodescription"></a>

Settings related to video encoding of your output. The specific video settings depend on the video codec that you choose.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| afdSignaling | [AfdSignaling](#jobsqueries-id-model-afdsignaling) | False | This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. \* Choose None to remove all AFD values from this output. \* Choose Fixed to ignore input AFD values and instead encode the value specified in the job. \* Choose Auto to calculate output AFD values based on the input AFD scaler data. |
| antiAlias | [AntiAlias](#jobsqueries-id-model-antialias) | False | The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting. |
| chromaPositionMode | [ChromaPositionMode](#jobsqueries-id-model-chromapositionmode) | False | Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left. |
| codecSettings | [VideoCodecSettings](#jobsqueries-id-model-videocodecsettings) | False | Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. \* AV1, Av1Settings \* AVC\_INTRA, AvcIntraSettings \* FRAME\_CAPTURE, FrameCaptureSettings \* GIF, GifSettings \* H\_264, H264Settings \* H\_265, H265Settings \* MPEG2, Mpeg2Settings \* PRORES, ProresSettings \* UNCOMPRESSED, UncompressedSettings \* VC3, Vc3Settings \* VP8, Vp8Settings \* VP9, Vp9Settings \* XAVC, XavcSettings |
| colorMetadata | [ColorMetadata](#jobsqueries-id-model-colormetadata) | False | Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default. |
| crop | [Rectangle](#jobsqueries-id-model-rectangle) | False | Use Cropping selection to specify the video area that the service will include in the output video frame. |
| dropFrameTimecode | [DropFrameTimecode](#jobsqueries-id-model-dropframetimecode) | False | Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled. |
| fixedAfd | integer<br />Minimum: 0<br />Maximum: 15 | False | Applies only if you set AFD Signaling to Fixed. Use Fixed to specify a four-bit AFD value which the service will write on all frames of this video output. |
| height | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Height to define the video resolution height, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Height blank and enter a value for Width. For example, if your input is 1920x1080 and you set Width to 1280, your output will be 1280x720. |
| position | [Rectangle](#jobsqueries-id-model-rectangle) | False | Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black. |
| respondToAfd | [RespondToAfd](#jobsqueries-id-model-respondtoafd) | False | Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. \* Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. \* Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. \* Choose None to remove all input AFD values from this output. |
| scalingBehavior | [ScalingBehavior](#jobsqueries-id-model-scalingbehavior) | False | Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported). |
| sharpness | integer<br />Minimum: 0<br />Maximum: 100 | False | Use Sharpness setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content. |
| timecodeInsertion | [VideoTimecodeInsertion](#jobsqueries-id-model-videotimecodeinsertion) | False | Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC\_TIMING\_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does. |
| timecodeTrack | [TimecodeTrack](#jobsqueries-id-model-timecodetrack) | False | To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled. |
| videoPreprocessors | [VideoPreprocessor](#jobsqueries-id-model-videopreprocessor) | False | Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default. |
| width | integer<br />Minimum: 32<br />Maximum: 8192 | False | Use Width to define the video resolution width, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Width blank and enter a value for Height. For example, if your input is 1920x1080 and you set Height to 720, your output will be 1280x720. |

### VideoDetail
<a name="jobsqueries-id-model-videodetail"></a>

Contains details about the output's video stream

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| heightInPx | integer | False | Height in pixels for the output |
| widthInPx | integer | False | Width in pixels for the output |

### VideoOverlay
<a name="jobsqueries-id-model-videooverlay"></a>

Overlay one or more videos on top of your input video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-overlays.html

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| crop | [VideoOverlayCrop](#jobsqueries-id-model-videooverlaycrop) | False | Specify a rectangle of content to crop and use from your video overlay's input video. When you do, MediaConvert uses the cropped dimensions that you specify under X offset, Y offset, Width, and Height. |
| endTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Enter the end timecode in the base input video for this overlay. Your overlay will be active through this frame. To display your video overlay for the duration of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS isthe second, and FF is the frame number. When entering this value, take into account your choice for the base input video's timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to end ten minutes into the video, enter 01:10:00:00. |
| initialPosition | [VideoOverlayPosition](#jobsqueries-id-model-videooverlayposition) | False | Specify the Initial position of your video overlay. To specify the Initial position of your video overlay, including distance from the left or top edge of the base input video's frame, or size: Enter a value for X position, Y position, Width, or Height. To use the full frame of the base input video: Leave blank. |
| input | [VideoOverlayInput](#jobsqueries-id-model-videooverlayinput) | False | Input settings for Video overlay. You can include one or more video overlays in sequence at different times that you specify. |
| playback | [VideoOverlayPlayBackMode](#jobsqueries-id-model-videooverlayplaybackmode) | False | Specify whether your video overlay repeats or plays only once. To repeat your video overlay on a loop: Keep the default value, Repeat. Your overlay will repeat for the duration of the base input video. To playback your video overlay only once: Choose Once. With either option, you can end playback at a time that you specify by entering a value for End timecode. |
| startTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Enter the start timecode in the base input video for this overlay. Your overlay will be active starting with this frame. To display your video overlay starting at the beginning of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for the base input video's timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to begin five minutes into the video, enter 01:05:00:00. |
| transitions | Array of type [VideoOverlayTransition](#jobsqueries-id-model-videooverlaytransition) | False | Specify one or more transitions for your video overlay. Use Transitions to reposition or resize your overlay over time. To use the same position and size for the duration of your video overlay: Leave blank. To specify a Transition: Enter a value for Start timecode, End Timecode, X Position, Y Position, Width, or Height. |

### VideoOverlayCrop
<a name="jobsqueries-id-model-videooverlaycrop"></a>

Specify a rectangle of content to crop and use from your video overlay's input video. When you do, MediaConvert uses the cropped dimensions that you specify under X offset, Y offset, Width, and Height.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the height of the video overlay cropping rectangle. To use the same height as your overlay input video: Keep blank, or enter 0. To specify a different height for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will be 100 pixels high. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 108 pixels high. |
| unit | [VideoOverlayUnit](#jobsqueries-id-model-videooverlayunit) | False | Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels. |
| width | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the width of the video overlay cropping rectangle. To use the same width as your overlay input video: Keep blank, or enter 0. To specify a different width for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will be 100 pixels wide. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 192 pixels wide. |
| x | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the distance between the cropping rectangle and the left edge of your overlay video's frame. To position the cropping rectangle along the left edge: Keep blank, or enter 0. To position the cropping rectangle to the right, relative to the left edge of your overlay video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the left edge of the overlay video's frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 192 pixels from the left edge of the overlay video's frame. |
| y | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the distance between the cropping rectangle and the top edge of your overlay video's frame. To position the cropping rectangle along the top edge: Keep blank, or enter 0. To position the cropping rectangle down, relative to the top edge of your overlay video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the top edge of the overlay video's frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 108 pixels from the top edge of the overlay video's frame. |

### VideoOverlayInput
<a name="jobsqueries-id-model-videooverlayinput"></a>

Input settings for Video overlay. You can include one or more video overlays in sequence at different times that you specify.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioSelectors | object | False | Use Audio selectors to specify audio to use during your Video overlay. You can use multiple Audio selectors per Video overlay. When you include an Audio selector within a Video overlay, MediaConvert mutes any Audio selectors with the same name from the underlying input. For example, if your underlying input has Audio selector 1 and Audio selector 2, and your Video overlay only has Audio selector 1, then MediaConvert replaces all audio for Audio selector 1 during the Video overlay. To replace all audio for all Audio selectors from the underlying input by using a single Audio selector in your overlay, set DefaultSelection to DEFAULT (Check \\"Use as default\\" in the MediaConvert console). |
| fileInput | string<br />Pattern: `^s3://([^\/]+\/+)+((([^\/]*)))\|^https?://[^\/].*[^&]$` | False | Specify the input file S3, HTTP, or HTTPS URL for your video overlay. To specify one or more Transitions for your base input video instead: Leave blank. |
| inputClippings | Array of type [VideoOverlayInputClipping](#jobsqueries-id-model-videooverlayinputclipping) | False | Specify one or more clips to use from your video overlay. When you include an input clip, you must also specify its start timecode, end timecode, or both start and end timecode. |
| timecodeSource | [InputTimecodeSource](#jobsqueries-id-model-inputtimecodesource) | False | Specify the timecode source for your video overlay input clips. To use the timecode present in your video overlay: Choose Embedded. To use a zerobased timecode: Choose Start at 0. To choose a timecode: Choose Specified start. When you do, enter the starting timecode in Start timecode. If you don't specify a value for Timecode source, MediaConvert uses Embedded by default. |
| timecodeStart | string<br />Pattern: `^((([0-1]\d)\|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`<br />MinLength: 11<br />MaxLength: 11 | False | Specify the starting timecode for this video overlay. To use this setting, you must set Timecode source to Specified start. |

### VideoOverlayInputClipping
<a name="jobsqueries-id-model-videooverlayinputclipping"></a>

To transcode only portions of your video overlay, include one input clip for each part of your video overlay that you want in your output.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}(@[0-9]+(\.[0-9]+)?(:[0-9]+)?)?$` | False | Specify the timecode of the last frame to include in your video overlay's clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source. |
| startTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}(@[0-9]+(\.[0-9]+)?(:[0-9]+)?)?$` | False | Specify the timecode of the first frame to include in your video overlay's clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source. |

### VideoOverlayPlayBackMode
<a name="jobsqueries-id-model-videooverlayplaybackmode"></a>

Specify whether your video overlay repeats or plays only once. To repeat your video overlay on a loop: Keep the default value, Repeat. Your overlay will repeat for the duration of the base input video. To playback your video overlay only once: Choose Once. With either option, you can end playback at a time that you specify by entering a value for End timecode.
+ `ONCE`
+ `REPEAT`

### VideoOverlayPosition
<a name="jobsqueries-id-model-videooverlayposition"></a>

position of video overlay

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| height | integer<br />Minimum: -1<br />Maximum: 2147483647 | False | To scale your video overlay to the same height as the base input video: Leave blank. To scale the height of your video overlay to a different height: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 360 and choose Pixels, your video overlay will be rendered with a height of 360. When you enter 50, choose Percentage, and your overlay's source has a height of 1080, your video overlay will be rendered with a height of 540. To scale your overlay to a specific height while automatically maintaining its original aspect ratio, enter a value for Height and leave Width blank. |
| opacity | integer<br />Minimum: 0<br />Maximum: 100 | False | Use Opacity to specify how much of the underlying video shows through the overlay video. 0 is transparent and 100 is fully opaque. Default is 100. |
| unit | [VideoOverlayUnit](#jobsqueries-id-model-videooverlayunit) | False | Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels. |
| width | integer<br />Minimum: -1<br />Maximum: 2147483647 | False | To scale your video overlay to the same width as the base input video: Leave blank. To scale the width of your video overlay to a different width: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 640 and choose Pixels, your video overlay will scale to a height of 640 pixels. When you enter 50, choose Percentage, and your overlay's source has a width of 1920, your video overlay will scale to a width of 960. To scale your overlay to a specific width while automatically maintaining its original aspect ratio, enter a value for Width and leave Height blank. |
| xPosition | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | To position the left edge of your video overlay along the left edge of the base input video's frame: Keep blank, or enter 0. To position the left edge of your video overlay to the right, relative to the left edge of the base input video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the left edge of the base input video's frame. When you enter 10, choose Percentage, and your base input video is 1920x1080, your video overlay will be positioned 192 pixels from the left edge of the base input video's frame. |
| yPosition | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | To position the top edge of your video overlay along the top edge of the base input video's frame: Keep blank, or enter 0. To position the top edge of your video overlay down, relative to the top edge of the base input video's frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the top edge of the base input video's frame. When you enter 10, choose Percentage, and your underlying video is 1920x1080, your video overlay will be positioned 108 pixels from the top edge of the base input video's frame. |

### VideoOverlayTransition
<a name="jobsqueries-id-model-videooverlaytransition"></a>

Specify one or more Transitions for your video overlay. Use Transitions to reposition or resize your overlay over time. To use the same position and size for the duration of your video overlay: Leave blank. To specify a Transition: Enter a value for Start timecode, End Timecode, X Position, Y Position, Width, Height, or Opacity

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endPosition | [VideoOverlayPosition](#jobsqueries-id-model-videooverlayposition) | False | Specify the ending position for this transition, relative to the base input video's frame. Your video overlay will move smoothly to this position, beginning at this transition's Start timecode and ending at this transition's End timecode. |
| endTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Specify the timecode for when this transition ends. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source. |
| startTimecode | string<br />Format: timecode<br />Pattern: `^([01][0-9]\|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$` | False | Specify the timecode for when this transition begins. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source. |

### VideoOverlayUnit
<a name="jobsqueries-id-model-videooverlayunit"></a>

Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels.
+ `PIXELS`
+ `PERCENTAGE`

### VideoPreprocessor
<a name="jobsqueries-id-model-videopreprocessor"></a>

Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| colorCorrector | [ColorCorrector](#jobsqueries-id-model-colorcorrector) | False | Use these settings to convert the color space or to modify properties such as hue and contrast for this output. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html. |
| deinterlacer | [Deinterlacer](#jobsqueries-id-model-deinterlacer) | False | Use the deinterlacer to produce smoother motion and a clearer picture. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html. |
| dolbyVision | [DolbyVision](#jobsqueries-id-model-dolbyvision) | False | Enable Dolby Vision feature to produce Dolby Vision compatible video output. |
| hdr10Plus | [Hdr10Plus](#jobsqueries-id-model-hdr10plus) | False | Enable HDR10\+ analysis and metadata injection. Compatible with HEVC only. |
| imageInserter | [ImageInserter](#jobsqueries-id-model-imageinserter) | False | Enable the Image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default. |
| noiseReducer | [NoiseReducer](#jobsqueries-id-model-noisereducer) | False | Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter. |
| partnerWatermarking | [PartnerWatermarking](#jobsqueries-id-model-partnerwatermarking) | False | If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output. |
| timecodeBurnin | [TimecodeBurnin](#jobsqueries-id-model-timecodeburnin) | False | Settings for burning the output timecode and specified prefix into the output. |

### VideoSelector
<a name="jobsqueries-id-model-videoselector"></a>

Input video selectors contain the video settings for the input. Each of your inputs can have up to one video selector.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| alphaBehavior | [AlphaBehavior](#jobsqueries-id-model-alphabehavior) | False | Ignore this setting unless this input is a QuickTime animation with an alpha channel. Use this setting to create separate Key and Fill outputs. In each output, specify which part of the input MediaConvert uses. Leave this setting at the default value DISCARD to delete the alpha channel and preserve the video. Set it to REMAP\_TO\_LUMA to delete the video and map the alpha channel to the luma channel of your outputs. |
| colorSpace | [ColorSpace](#jobsqueries-id-model-colorspace) | False | If your input video has accurate color space metadata, or if you don't know about color space: Keep the default value, Follow. MediaConvert will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or has missing metadata: Specify the accurate color space here. If your input video is HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata isn't present in your video stream, or if that metadata is present but not accurate: Choose Force HDR 10. Specify correct values in the input HDR 10 metadata settings. For more information about HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. When you specify an input color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: \* HDR 10: BT.2020, PQ, BT.2020 non-constant \* HLG 2020: BT.2020, HLG, BT.2020 non-constant \* P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 \* P3D65 (SDR): Display P3, sRGB, BT.709 \* P3D65 (HDR): Display P3, PQ, BT.709 |
| colorSpaceUsage | [ColorSpaceUsage](#jobsqueries-id-model-colorspaceusage) | False | There are two sources for color metadata, the input file and the job input settings Color space and HDR master display information settings. The Color space usage setting determines which takes precedence. Choose Force to use color metadata from the input job settings. If you don't specify values for those settings, the service defaults to using metadata from your input. FALLBACK - Choose Fallback to use color metadata from the source when it is present. If there's no color metadata in your input file, the service defaults to using values you specify in the input settings. |
| embeddedTimecodeOverride | [EmbeddedTimecodeOverride](#jobsqueries-id-model-embeddedtimecodeoverride) | False | Set Embedded timecode override to Use MDPM when your AVCHD input contains timecode tag data in the Modified Digital Video Pack Metadata. When you do, we recommend you also set Timecode source to Embedded. Leave Embedded timecode override blank, or set to None, when your input does not contain MDPM timecode. |
| hdr10Metadata | [Hdr10Metadata](#jobsqueries-id-model-hdr10metadata) | False | Use these settings to provide HDR 10 metadata that is missing or inaccurate in your input video. Appropriate values vary depending on the input video and must be provided by a color grader. The color grader generates these values during the HDR 10 mastering process. The valid range for each of these settings is 0 to 50,000. Each increment represents 0.00002 in CIE1931 color coordinate. Related settings - When you specify these values, you must also set Color space to HDR 10. To specify whether the the values you specify here take precedence over the values in the metadata of your input file, set Color space usage. To specify whether color metadata is included in an output, set Color metadata. For more information about MediaConvert HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. |
| maxLuminance | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits. |
| padVideo | [PadVideo](#jobsqueries-id-model-padvideo) | False | Use this setting if your input has video and audio durations that don't align, and your output or player has strict alignment requirements. Examples: Input audio track has a delayed start. Input video track ends before audio ends. When you set Pad video to Black, MediaConvert generates black video frames so that output video and audio durations match. Black video frames are added at the beginning or end, depending on your input. To keep the default behavior and not generate black video, set Pad video to Disabled or leave blank. |
| pid | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Use PID to select specific video data from an input file. Specify this value as an integer; the system automatically converts it to the hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet identifier, is an identifier for a set of data in an MPEG-2 transport stream container. |
| programNumber | integer<br />Minimum: -2147483648<br />Maximum: 2147483647 | False | Selects a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. |
| rotate | [InputRotate](#jobsqueries-id-model-inputrotate) | False | Use Rotate to specify how the service rotates your video. You can choose automatic rotation or specify a rotation. You can specify a clockwise rotation of 0, 90, 180, or 270 degrees. If your input video container is .mov or .mp4 and your input has rotation metadata, you can choose Automatic to have the service rotate your video according to the rotation specified in the metadata. The rotation must be within one degree of 90, 180, or 270 degrees. If the rotation metadata specifies any other rotation, the service will default to no rotation. By default, the service does no rotation, even if your input video has rotation metadata. The service doesn't pass through rotation metadata. |
| sampleRange | [InputSampleRange](#jobsqueries-id-model-inputsamplerange) | False | If the sample range metadata in your input video is accurate, or if you don't know about sample range, keep the default value, Follow, for this setting. When you do, the service automatically detects your input sample range. If your input video has metadata indicating the wrong sample range, specify the accurate sample range here. When you do, MediaConvert ignores any sample range information in the input metadata. Regardless of whether MediaConvert uses the input sample range or the sample range that you specify, MediaConvert uses the sample range for transcoding and also writes it to the output metadata. |
| selectorType | [VideoSelectorType](#jobsqueries-id-model-videoselectortype) | False | Choose the video selector type for your HLS input. Use to specify which video rendition MediaConvert uses from your HLS input. To have MediaConvert automatically use the highest bitrate rendition from your HLS input: Keep the default value, Auto. To manually specify a rendition: Choose Stream. Then enter the unique stream number in the Streams array, starting at 1, corresponding to the stream order in the manifest. |
| streams | Array of type integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Specify one or more video streams for MediaConvert to use from your HLS input. Enter an integer corresponding to the stream number, with the first stream in your HLS multivariant playlist starting at 1. For re-encoding workflows, MediaConvert uses the video stream that you select with the highest bitrate as the input. For video passthrough workflows, you specify whether to passthrough a single video stream or multiple video streams under Video selector source in the output video encoding settings. |

### VideoSelectorMode
<a name="jobsqueries-id-model-videoselectormode"></a>

AUTO will select the highest bitrate input in the video selector source. REMUX\_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX\_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source.
+ `AUTO`
+ `REMUX_ALL`

### VideoSelectorType
<a name="jobsqueries-id-model-videoselectortype"></a>

Choose the video selector type for your HLS input. Use to specify which video rendition MediaConvert uses from your HLS input. To have MediaConvert automatically use the highest bitrate rendition from your HLS input: Keep the default value, Auto. To manually specify a rendition: Choose Stream. Then enter the unique stream number in the Streams array, starting at 1, corresponding to the stream order in the manifest.
+ `AUTO`
+ `STREAM`

### VideoTimecodeInsertion
<a name="jobsqueries-id-model-videotimecodeinsertion"></a>

Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC\_TIMING\_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does.
+ `DISABLED`
+ `PIC_TIMING_SEI`

### VorbisSettings
<a name="jobsqueries-id-model-vorbissettings"></a>

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channels | integer<br />Minimum: 0<br />Maximum: 2 | False | Optional. Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono on the console gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. The default value is 2. |
| sampleRate | integer<br />Minimum: 22050<br />Maximum: 48000 | False | Optional. Specify the audio sample rate in Hz. Valid values are 22050, 32000, 44100, and 48000. The default value is 48000. |
| vbrQuality | integer<br />Minimum: -1<br />Maximum: 10 | False | Optional. Specify the variable audio quality of this Vorbis output from -1 (lowest quality, \~45 kbit/s) to 10 (highest quality, \~500 kbit/s). The default value is 4 (\~128 kbit/s). Values 5 and 6 are approximately 160 and 192 kbit/s, respectively. |

### Vp8FramerateControl
<a name="jobsqueries-id-model-vp8frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp8FramerateConversionAlgorithm
<a name="jobsqueries-id-model-vp8framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vp8ParControl
<a name="jobsqueries-id-model-vp8parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp8QualityTuningLevel
<a name="jobsqueries-id-model-vp8qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.
+ `MULTI_PASS`
+ `MULTI_PASS_HQ`

### Vp8RateControlMode
<a name="jobsqueries-id-model-vp8ratecontrolmode"></a>

With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode.
+ `VBR`

### Vp8Settings
<a name="jobsqueries-id-model-vp8settings"></a>

Required when you set Codec to the value VP8.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Target bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| framerateControl | [Vp8FramerateControl](#jobsqueries-id-model-vp8frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vp8FramerateConversionAlgorithm](#jobsqueries-id-model-vp8framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | GOP Length (keyframe interval) in frames. Must be greater than zero. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Optional. Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 1152000000 | False | Ignore this setting unless you set qualityTuningLevel to MULTI\_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate. |
| parControl | [Vp8ParControl](#jobsqueries-id-model-vp8parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| qualityTuningLevel | [Vp8QualityTuningLevel](#jobsqueries-id-model-vp8qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding. |
| rateControlMode | [Vp8RateControlMode](#jobsqueries-id-model-vp8ratecontrolmode) | False | With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode. |

### Vp9FramerateControl
<a name="jobsqueries-id-model-vp9frameratecontrol"></a>

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp9FramerateConversionAlgorithm
<a name="jobsqueries-id-model-vp9framerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### Vp9ParControl
<a name="jobsqueries-id-model-vp9parcontrol"></a>

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### Vp9QualityTuningLevel
<a name="jobsqueries-id-model-vp9qualitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.
+ `MULTI_PASS`
+ `MULTI_PASS_HQ`

### Vp9RateControlMode
<a name="jobsqueries-id-model-vp9ratecontrolmode"></a>

With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode.
+ `VBR`

### Vp9Settings
<a name="jobsqueries-id-model-vp9settings"></a>

Required when you set Codec to the value VP9.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrate | integer<br />Minimum: 1000<br />Maximum: 480000000 | False | Target bitrate in bits/second. For example, enter five megabits per second as 5000000. |
| framerateControl | [Vp9FramerateControl](#jobsqueries-id-model-vp9frameratecontrol) | False | If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. |
| framerateConversionAlgorithm | [Vp9FramerateConversionAlgorithm](#jobsqueries-id-model-vp9framerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| gopSize | number<br />Format: float<br />Minimum: 0.0 | False | GOP Length (keyframe interval) in frames. Must be greater than zero. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 47185920 | False | Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000. |
| maxBitrate | integer<br />Minimum: 1000<br />Maximum: 480000000 | False | Ignore this setting unless you set qualityTuningLevel to MULTI\_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate. |
| parControl | [Vp9ParControl](#jobsqueries-id-model-vp9parcontrol) | False | Optional. Specify how the service determines the pixel aspect ratio for this output. The default behavior is to use the same pixel aspect ratio as your input video. |
| parDenominator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33. |
| parNumerator | integer<br />Minimum: 1<br />Maximum: 2147483647 | False | Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40. |
| qualityTuningLevel | [Vp9QualityTuningLevel](#jobsqueries-id-model-vp9qualitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding. |
| rateControlMode | [Vp9RateControlMode](#jobsqueries-id-model-vp9ratecontrolmode) | False | With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode. |

### WarningGroup
<a name="jobsqueries-id-model-warninggroup"></a>

Contains any warning codes and their count for the job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | integer<br />Format: int32 | True | Warning code that identifies a specific warning in the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/warning\_codes.html |
| count | integer<br />Format: int32 | True | The number of times this warning occurred in the job. |

### WatermarkingStrength
<a name="jobsqueries-id-model-watermarkingstrength"></a>

Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value.
+ `LIGHTEST`
+ `LIGHTER`
+ `DEFAULT`
+ `STRONGER`
+ `STRONGEST`

### WavFormat
<a name="jobsqueries-id-model-wavformat"></a>

Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible.
+ `RIFF`
+ `RF64`
+ `EXTENSIBLE`

### WavSettings
<a name="jobsqueries-id-model-wavsettings"></a>

Required when you set Codec to the value WAV.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer<br />Minimum: 16<br />Maximum: 24 | False | Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track. |
| channels | integer<br />Minimum: 0<br />Maximum: 64 | False | Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 64. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and so on, up to 64. |
| format | [WavFormat](#jobsqueries-id-model-wavformat) | False | Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible. |
| sampleRate | integer<br />Minimum: 8000<br />Maximum: 192000 | False | Sample rate in Hz. |

### WebvttAccessibilitySubs
<a name="jobsqueries-id-model-webvttaccessibilitysubs"></a>

If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>.
+ `DISABLED`
+ `ENABLED`

### WebvttDestinationSettings
<a name="jobsqueries-id-model-webvttdestinationsettings"></a>

Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessibility | [WebvttAccessibilitySubs](#jobsqueries-id-model-webvttaccessibilitysubs) | False | If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>. |
| stylePassthrough | [WebvttStylePassthrough](#jobsqueries-id-model-webvttstylepassthrough) | False | Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range. |

### WebvttHlsSourceSettings
<a name="jobsqueries-id-model-webvtthlssourcesettings"></a>

Settings specific to WebVTT sources in HLS alternative rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique subtitle track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the specified properties, the job fails. If there is only one subtitle track in the rendition group, the settings can be left empty and the default subtitle track will be chosen. If your caption source is a sidecar file, use FileSourceSettings instead of WebvttHlsSourceSettings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| renditionGroupId | string | False | Optional. Specify alternative group ID |
| renditionLanguageCode | [LanguageCode](#jobsqueries-id-model-languagecode) | False | Optionally specify the language, using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code\_list.php |
| renditionName | string | False | Optional. Specify media name |

### WebvttStylePassthrough
<a name="jobsqueries-id-model-webvttstylepassthrough"></a>

Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range.
+ `ENABLED`
+ `DISABLED`
+ `STRICT`
+ `MERGE`

### Xavc4kIntraCbgProfileClass
<a name="jobsqueries-id-model-xavc4kintracbgprofileclass"></a>

Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_100`
+ `CLASS_300`
+ `CLASS_480`

### Xavc4kIntraCbgProfileSettings
<a name="jobsqueries-id-model-xavc4kintracbgprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K\_INTRA\_CBG.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [Xavc4kIntraCbgProfileClass](#jobsqueries-id-model-xavc4kintracbgprofileclass) | False | Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### Xavc4kIntraVbrProfileClass
<a name="jobsqueries-id-model-xavc4kintravbrprofileclass"></a>

Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_100`
+ `CLASS_300`
+ `CLASS_480`

### Xavc4kIntraVbrProfileSettings
<a name="jobsqueries-id-model-xavc4kintravbrprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K\_INTRA\_VBR.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [Xavc4kIntraVbrProfileClass](#jobsqueries-id-model-xavc4kintravbrprofileclass) | False | Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### Xavc4kProfileBitrateClass
<a name="jobsqueries-id-model-xavc4kprofilebitrateclass"></a>

Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `BITRATE_CLASS_100`
+ `BITRATE_CLASS_140`
+ `BITRATE_CLASS_200`

### Xavc4kProfileCodecProfile
<a name="jobsqueries-id-model-xavc4kprofilecodecprofile"></a>

Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH\_422). These profiles are specified in ITU-T H.264.
+ `HIGH`
+ `HIGH_422`

### Xavc4kProfileQualityTuningLevel
<a name="jobsqueries-id-model-xavc4kprofilequalitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### Xavc4kProfileSettings
<a name="jobsqueries-id-model-xavc4kprofilesettings"></a>

Required when you set Profile to the value XAVC\_4K.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrateClass | [Xavc4kProfileBitrateClass](#jobsqueries-id-model-xavc4kprofilebitrateclass) | False | Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |
| codecProfile | [Xavc4kProfileCodecProfile](#jobsqueries-id-model-xavc4kprofilecodecprofile) | False | Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH\_422). These profiles are specified in ITU-T H.264. |
| flickerAdaptiveQuantization | [XavcFlickerAdaptiveQuantization](#jobsqueries-id-model-xavcflickeradaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides. |
| gopBReference | [XavcGopBReference](#jobsqueries-id-model-xavcgopbreference) | False | Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point. |
| qualityTuningLevel | [Xavc4kProfileQualityTuningLevel](#jobsqueries-id-model-xavc4kprofilequalitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| slices | integer<br />Minimum: 8<br />Maximum: 12 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |

### XavcAdaptiveQuantization
<a name="jobsqueries-id-model-xavcadaptivequantization"></a>

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization.
+ `OFF`
+ `AUTO`
+ `LOW`
+ `MEDIUM`
+ `HIGH`
+ `HIGHER`
+ `MAX`

### XavcEntropyEncoding
<a name="jobsqueries-id-model-xavcentropyencoding"></a>

Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point.
+ `AUTO`
+ `CABAC`
+ `CAVLC`

### XavcFlickerAdaptiveQuantization
<a name="jobsqueries-id-model-xavcflickeradaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides.
+ `DISABLED`
+ `ENABLED`

### XavcFramerateControl
<a name="jobsqueries-id-model-xavcframeratecontrol"></a>

If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions.
+ `INITIALIZE_FROM_SOURCE`
+ `SPECIFIED`

### XavcFramerateConversionAlgorithm
<a name="jobsqueries-id-model-xavcframerateconversionalgorithm"></a>

Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.
+ `DUPLICATE_DROP`
+ `INTERPOLATE`
+ `FRAMEFORMER`
+ `MAINTAIN_FRAME_COUNT`

### XavcGopBReference
<a name="jobsqueries-id-model-xavcgopbreference"></a>

Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames.
+ `DISABLED`
+ `ENABLED`

### XavcHdIntraCbgProfileClass
<a name="jobsqueries-id-model-xavchdintracbgprofileclass"></a>

Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `CLASS_50`
+ `CLASS_100`
+ `CLASS_200`

### XavcHdIntraCbgProfileSettings
<a name="jobsqueries-id-model-xavchdintracbgprofilesettings"></a>

Required when you set Profile to the value XAVC\_HD\_INTRA\_CBG.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| xavcClass | [XavcHdIntraCbgProfileClass](#jobsqueries-id-model-xavchdintracbgprofileclass) | False | Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |

### XavcHdProfileBitrateClass
<a name="jobsqueries-id-model-xavchdprofilebitrateclass"></a>

Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.
+ `BITRATE_CLASS_25`
+ `BITRATE_CLASS_35`
+ `BITRATE_CLASS_50`

### XavcHdProfileQualityTuningLevel
<a name="jobsqueries-id-model-xavchdprofilequalitytuninglevel"></a>

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.
+ `SINGLE_PASS`
+ `SINGLE_PASS_HQ`
+ `MULTI_PASS_HQ`

### XavcHdProfileSettings
<a name="jobsqueries-id-model-xavchdprofilesettings"></a>

Required when you set Profile to the value XAVC\_HD.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitrateClass | [XavcHdProfileBitrateClass](#jobsqueries-id-model-xavchdprofilebitrateclass) | False | Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class. |
| flickerAdaptiveQuantization | [XavcFlickerAdaptiveQuantization](#jobsqueries-id-model-xavcflickeradaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides. |
| gopBReference | [XavcGopBReference](#jobsqueries-id-model-xavcgopbreference) | False | Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames. |
| gopClosedCadence | integer<br />Minimum: 0<br />Maximum: 2147483647 | False | Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting. |
| hrdBufferSize | integer<br />Minimum: 0<br />Maximum: 1152000000 | False | Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you don't set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point. |
| interlaceMode | [XavcInterlaceMode](#jobsqueries-id-model-xavcinterlacemode) | False | Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose. |
| qualityTuningLevel | [XavcHdProfileQualityTuningLevel](#jobsqueries-id-model-xavchdprofilequalitytuninglevel) | False | Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding. |
| slices | integer<br />Minimum: 4<br />Maximum: 12 | False | Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. |
| telecine | [XavcHdProfileTelecine](#jobsqueries-id-model-xavchdprofiletelecine) | False | Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html. |

### XavcHdProfileTelecine
<a name="jobsqueries-id-model-xavchdprofiletelecine"></a>

Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html.
+ `NONE`
+ `HARD`

### XavcInterlaceMode
<a name="jobsqueries-id-model-xavcinterlacemode"></a>

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.
+ `PROGRESSIVE`
+ `TOP_FIELD`
+ `BOTTOM_FIELD`
+ `FOLLOW_TOP_FIELD`
+ `FOLLOW_BOTTOM_FIELD`

### XavcProfile
<a name="jobsqueries-id-model-xavcprofile"></a>

Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC\_HD\_INTRA\_CBG. To create an interlaced XAVC output, choose the profile XAVC\_HD.
+ `XAVC_HD_INTRA_CBG`
+ `XAVC_4K_INTRA_CBG`
+ `XAVC_4K_INTRA_VBR`
+ `XAVC_HD`
+ `XAVC_4K`

### XavcSettings
<a name="jobsqueries-id-model-xavcsettings"></a>

Required when you set Codec to the value XAVC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adaptiveQuantization | [XavcAdaptiveQuantization](#jobsqueries-id-model-xavcadaptivequantization) | False | Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization. |
| entropyEncoding | [XavcEntropyEncoding](#jobsqueries-id-model-xavcentropyencoding) | False | Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point. |
| framerateControl | [XavcFramerateControl](#jobsqueries-id-model-xavcframeratecontrol) | False | If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions. |
| framerateConversionAlgorithm | [XavcFramerateConversionAlgorithm](#jobsqueries-id-model-xavcframerateconversionalgorithm) | False | Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates. |
| framerateDenominator | integer<br />Minimum: 1<br />Maximum: 1001 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Frame rate. In this example, specify 23.976. |
| framerateNumerator | integer<br />Minimum: 24<br />Maximum: 60000 | False | When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976. |
| perFrameMetrics | Array of type [frameMetricType](#jobsqueries-id-model-framemetrictype) | False | Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile\_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: \* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes |
| profile | [XavcProfile](#jobsqueries-id-model-xavcprofile) | False | Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC\_HD\_INTRA\_CBG. To create an interlaced XAVC output, choose the profile XAVC\_HD. |
| slowPal | [XavcSlowPal](#jobsqueries-id-model-xavcslowpal) | False | Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25. |
| softness | integer<br />Minimum: 0<br />Maximum: 128 | False | Ignore this setting unless your downstream workflow requires that you specify it explicitly. Otherwise, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video. |
| spatialAdaptiveQuantization | [XavcSpatialAdaptiveQuantization](#jobsqueries-id-model-xavcspatialadaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. |
| temporalAdaptiveQuantization | [XavcTemporalAdaptiveQuantization](#jobsqueries-id-model-xavctemporaladaptivequantization) | False | The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization. |
| xavc4kIntraCbgProfileSettings | [Xavc4kIntraCbgProfileSettings](#jobsqueries-id-model-xavc4kintracbgprofilesettings) | False | Required when you set Profile to the value XAVC\_4K\_INTRA\_CBG. |
| xavc4kIntraVbrProfileSettings | [Xavc4kIntraVbrProfileSettings](#jobsqueries-id-model-xavc4kintravbrprofilesettings) | False | Required when you set Profile to the value XAVC\_4K\_INTRA\_VBR. |
| xavc4kProfileSettings | [Xavc4kProfileSettings](#jobsqueries-id-model-xavc4kprofilesettings) | False | Required when you set Profile to the value XAVC\_4K. |
| xavcHdIntraCbgProfileSettings | [XavcHdIntraCbgProfileSettings](#jobsqueries-id-model-xavchdintracbgprofilesettings) | False | Required when you set Profile to the value XAVC\_HD\_INTRA\_CBG. |
| xavcHdProfileSettings | [XavcHdProfileSettings](#jobsqueries-id-model-xavchdprofilesettings) | False | Required when you set Profile to the value XAVC\_HD. |

### XavcSlowPal
<a name="jobsqueries-id-model-xavcslowpal"></a>

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25.
+ `DISABLED`
+ `ENABLED`

### XavcSpatialAdaptiveQuantization
<a name="jobsqueries-id-model-xavcspatialadaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.
+ `DISABLED`
+ `ENABLED`

### XavcTemporalAdaptiveQuantization
<a name="jobsqueries-id-model-xavctemporaladaptivequantization"></a>

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization.
+ `DISABLED`
+ `ENABLED`

### frameMetricType
<a name="jobsqueries-id-model-framemetrictype"></a>

\* PSNR: Peak Signal-to-Noise Ratio \* SSIM: Structural Similarity Index Measure \* MS\_SSIM: Multi-Scale Similarity Index Measure \* PSNR\_HVS: Peak Signal-to-Noise Ratio, Human Visual System \* VMAF: Video Multi-Method Assessment Fusion \* QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. \* SHOT\_CHANGE: Shot Changes
+ `PSNR`
+ `SSIM`
+ `MS_SSIM`
+ `PSNR_HVS`
+ `VMAF`
+ `QVBR`
+ `SHOT_CHANGE`

## See also
<a name="jobsqueries-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetJobsQueryResults
<a name="GetJobsQueryResults-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/GetJobsQueryResults)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/GetJobsQueryResults)
