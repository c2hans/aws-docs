---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/sample-json.html
---

# Sample Job Settings Specifications in JSON
<a name="sample-json"></a>

These sample AWS Elemental MediaConvert jobs are specified in JSON. When you use the Python SDK or the AWS CLI, you pass in your job settings directly as a JSON object. When you use the other SDKs, translate the job settings according to the SDK documentation.

The following examples are meant for testing purposes only. You can use them to verify that you can successfully submit your CreateJob request to MediaConvert. We recommend that you use the MediaConvert console to set up jobs for production. For more information, see [Creating Your Job Specification](creating-your-json-job-specification.md).

**Tip**
We recommend that you *don't* construct your production job settings specifications by starting from one of the samples in this chapter and then adding settings. This approach usually results in a series of validation errors that can be frustrating to resolve. Instead, use the MediaConvert console to set up and run your initial job and then export the JSON job object to use to programmatically submit future jobs.

## Simple Example
<a name="simple-example"></a>

This example JSON job settings specification describes a job that creates a single file output:

```
{
    "Queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
    "UserMetadata": {
        "Customer": "Amazon"
    },
    "Role": "arn:aws:iam::111122223333:role/EMFRoleSPNames",
    "Settings": {
        "TimecodeConfig": {
            "Source": "EMBEDDED"
        },
        "OutputGroups": [{
            "Name": "File Group",
            "Outputs": [{
                "ContainerSettings": {
                    "Container": "MP4",
                    "Mp4Settings": {
                        "CslgAtom": "INCLUDE",
                        "FreeSpaceBox": "EXCLUDE",
                        "MoovPlacement": "PROGRESSIVE_DOWNLOAD"
                    }
                },
                "VideoDescription": {
                    "ScalingBehavior": "DEFAULT",
                    "TimecodeInsertion": "DISABLED",
                    "AntiAlias": "ENABLED",
                    "Sharpness": 50,
                    "CodecSettings": {
                        "Codec": "H_264",
                        "H264Settings": {
                            "InterlaceMode": "PROGRESSIVE",
                            "ParNumerator": 1,
                            "NumberReferenceFrames": 3,
                            "Syntax": "DEFAULT",
                            "Softness": 0,
                            "FramerateDenominator": 1,
                            "GopClosedCadence": 1,
                            "GopSize": 2,
                            "Slices": 1,
                            "GopBReference": "DISABLED",
                            "MaxBitrate": 25000000,
                            "SlowPal": "DISABLED",
                            "ParDenominator": 1,
                            "SpatialAdaptiveQuantization": "ENABLED",
                            "TemporalAdaptiveQuantization": "ENABLED",
                            "FlickerAdaptiveQuantization": "DISABLED",
                            "EntropyEncoding": "CABAC",
                            "FramerateControl": "SPECIFIED",
                            "RateControlMode": "QVBR",
                            "CodecProfile": "MAIN",
                            "Telecine": "NONE",
                            "FramerateNumerator": 30,
                            "MinIInterval": 0,
                            "AdaptiveQuantization": "HIGH",
                            "CodecLevel": "AUTO",
                            "FieldEncoding": "PAFF",
                            "SceneChangeDetect": "TRANSITION_DETECTION",
                            "QualityTuningLevel": "SINGLE_PASS_HQ",
                            "FramerateConversionAlgorithm": "DUPLICATE_DROP",
                            "UnregisteredSeiTimecode": "DISABLED",
                            "GopSizeUnits": "SECONDS",
                            "ParControl": "SPECIFIED",
                            "NumberBFramesBetweenReferenceFrames": 2,
                            "RepeatPps": "DISABLED"
                        }
                    },
                    "AfdSignaling": "NONE",
                    "DropFrameTimecode": "ENABLED",
                    "RespondToAfd": "NONE",
                    "ColorMetadata": "INSERT"
                },
                "AudioDescriptions": [{
                    "AudioTypeControl": "FOLLOW_INPUT",
                    "AudioSourceName": "Audio Selector 1",
                    "CodecSettings": {
                        "Codec": "AAC",
                        "AacSettings": {
                            "AudioDescriptionBroadcasterMix": "NORMAL",
                            "Bitrate": 64000,
                            "RateControlMode": "CBR",
                            "CodecProfile": "LC",
                            "CodingMode": "CODING_MODE_2_0",
                            "RawFormat": "NONE",
                            "SampleRate": 48000,
                            "Specification": "MPEG4"
                        }
                    },
                    "LanguageCodeControl": "FOLLOW_INPUT"
                }],
                "NameModifier": "_1"
            }],
            "OutputGroupSettings": {
                "Type": "FILE_GROUP_SETTINGS",
                "FileGroupSettings": {
                    "Destination": "s3://amzn-s3-demo-bucket/output"
                }
            }
        }],
        "AdAvailOffset": 0,
        "Inputs": [{
            "AudioSelectors": {
                "Audio Selector 1": {
                    "Tracks": [1],
                    "Offset": 0,
                    "DefaultSelection": "NOT_DEFAULT",
                    "SelectorType": "TRACK",
                    "ProgramSelection": 1
                }
            },
            "VideoSelector": {
                "ColorSpace": "FOLLOW"
            },
            "FilterEnable": "AUTO",
            "PsiControl": "USE_PSI",
            "FilterStrength": 0,
            "DeblockFilter": "DISABLED",
            "DenoiseFilter": "DISABLED",
            "TimecodeSource": "EMBEDDED",
            "FileInput": "s3://amzn-s3-demo-bucket/720/example_input_720p.mov"
        }]
    },
    "AccelerationSettings": {
        "Mode": "DISABLED"
    },
    "StatusUpdateInterval": "SECONDS_60",
    "Priority": 0
}
```

## Complex Example
<a name="complex-example"></a>

This example JSON job settings specification describes a job that creates output in multiple packages for viewing on different device types. It uses encryption for digital rights management:

```
{
    "Queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
    "UserMetadata": {
        "Customer": "Amazon"
    },
    "Role": "arn:aws:iam::111122223333:role/MediaConvertRole",
    "Settings": {
        "TimecodeConfig": {
            "Source": "ZEROBASED"
        },
        "OutputGroups": [{
                "Name": "DASH ISO",
                "Outputs": [{
                        "ContainerSettings": {
                            "Container": "MPD"
                        },
                        "VideoDescription": {
                            "Width": 1280,
                            "ScalingBehavior": "DEFAULT",
                            "Height": 720,
                            "TimecodeInsertion": "DISABLED",
                            "AntiAlias": "ENABLED",
                            "Sharpness": 50,
                            "CodecSettings": {
                                "Codec": "H_264",
                                "H264Settings": {
                                    "InterlaceMode": "PROGRESSIVE",
                                    "NumberReferenceFrames": 3,
                                    "Syntax": "DEFAULT",
                                    "Softness": 0,
                                    "FramerateDenominator": 1,
                                    "GopClosedCadence": 1,
                                    "GopSize": 30,
                                    "Slices": 1,
                                    "GopBReference": "DISABLED",
                                    "HrdBufferSize": 10000000,
                                    "MaxBitrate": 5000000,
                                    "SpatialAdaptiveQuantization": "ENABLED",
                                    "TemporalAdaptiveQuantization": "ENABLED",
                                    "FlickerAdaptiveQuantization": "DISABLED",
                                    "EntropyEncoding": "CABAC",
                                    "FramerateControl": "SPECIFIED",
                                    "RateControlMode": "QVBR",
                                    "CodecProfile": "MAIN",
                                    "FramerateNumerator": 30,
                                    "MinIInterval": 0,
                                    "AdaptiveQuantization": "HIGH",
                                    "CodecLevel": "AUTO",
                                    "FieldEncoding": "PAFF",
                                    "SceneChangeDetect": "TRANSITION_DETECTION",
                                    "QualityTuningLevel": "SINGLE_PASS_HQ",
                                    "FramerateConversionAlgorithm": "DUPLICATE_DROP",
                                    "UnregisteredSeiTimecode": "DISABLED",
                                    "GopSizeUnits": "FRAMES",
                                    "ParControl": "INITIALIZE_FROM_SOURCE",
                                    "NumberBFramesBetweenReferenceFrames": 2,
                                    "RepeatPps": "DISABLED"
                                }
                            },
                            "AfdSignaling": "NONE",
                            "DropFrameTimecode": "ENABLED",
                            "RespondToAfd": "NONE",
                            "ColorMetadata": "INSERT"
                        },
                        "NameModifier": "-1080"
                    },
                    {
                        "ContainerSettings": {
                            "Container": "MPD"
                        },
                        "AudioDescriptions": [{
                            "AudioTypeControl": "FOLLOW_INPUT",
                            "AudioSourceName": "Audio Selector 1",
                            "CodecSettings": {
                                "Codec": "AAC",
                                "AacSettings": {
                                    "AudioDescriptionBroadcasterMix": "NORMAL",
                                    "Bitrate": 96000,
                                    "RateControlMode": "CBR",
                                    "CodecProfile": "LC",
                                    "CodingMode": "CODING_MODE_2_0",
                                    "RawFormat": "NONE",
                                    "SampleRate": 48000,
                                    "Specification": "MPEG4"
                                }
                            },
                            "LanguageCodeControl": "FOLLOW_INPUT"
                        }],
                        "NameModifier": "-audio"
                    }
                ],
                "OutputGroupSettings": {
                    "Type": "DASH_ISO_GROUP_SETTINGS",
                    "DashIsoGroupSettings": {
                        "SegmentLength": 30,
                        "Destination": "s3://amzn-s3-demo-bucket/drm/10/dash-drm/master",
                        "Encryption": {
                            "SpekeKeyProvider": {
                                "ResourceId": "drm-test-1",
                                "SystemIds": [
                                    "edef8ba9-79d6-4ace-a3c8-27dcd51d21ed"
                                ],
                                "Url": "https://example.execute-api.us-west-2.amazonaws.com/live/speke/v1.0/copyProtection"
                            }
                        },
                        "FragmentLength": 2,
                        "SegmentControl": "SINGLE_FILE",
                        "HbbtvCompliance": "NONE"
                    }
                }
            },
            {
                "Name": "Apple HLS",
                "Outputs": [{
                        "ContainerSettings": {
                            "Container": "M3U8",
                            "M3u8Settings": {
                                "AudioFramesPerPes": 4,
                                "PcrControl": "PCR_EVERY_PES_PACKET",
                                "PmtPid": 480,
                                "PrivateMetadataPid": 503,
                                "ProgramNumber": 1,
                                "PatInterval": 0,
                                "PmtInterval": 0,
                                "Scte35Source": "NONE",
                                "NielsenId3": "NONE",
                                "TimedMetadata": "NONE",
                                "VideoPid": 481,
                                "AudioPids": [
                                    482,
                                    483,
                                    484,
                                    485,
                                    486,
                                    487,
                                    488,
                                    489,
                                    490,
                                    491,
                                    492
                                ]
                            }
                        },
                        "VideoDescription": {
                            "Width": 1280,
                            "ScalingBehavior": "DEFAULT",
                            "Height": 720,
                            "TimecodeInsertion": "DISABLED",
                            "AntiAlias": "ENABLED",
                            "Sharpness": 50,
                            "CodecSettings": {
                                "Codec": "H_264",
                                "H264Settings": {
                                    "InterlaceMode": "PROGRESSIVE",
                                    "NumberReferenceFrames": 3,
                                    "Syntax": "DEFAULT",
                                    "Softness": 0,
                                    "FramerateDenominator": 1,
                                    "GopClosedCadence": 1,
                                    "GopSize": 60,
                                    "Slices": 1,
                                    "GopBReference": "DISABLED",
                                    "MaxBitrate": 5000000,
                                    "SpatialAdaptiveQuantization": "ENABLED",
                                    "TemporalAdaptiveQuantization": "ENABLED",
                                    "FlickerAdaptiveQuantization": "DISABLED",
                                    "EntropyEncoding": "CABAC",
                                    "FramerateControl": "SPECIFIED",
                                    "RateControlMode": "QVBR",
                                    "CodecProfile": "MAIN",
                                    "FramerateNumerator": 30,
                                    "MinIInterval": 0,
                                    "AdaptiveQuantization": "HIGH",
                                    "CodecLevel": "AUTO",
                                    "FieldEncoding": "PAFF",
                                    "SceneChangeDetect": "TRANSITION_DETECTION",
                                    "QualityTuningLevel": "SINGLE_PASS_HQ",
                                    "FramerateConversionAlgorithm": "DUPLICATE_DROP",
                                    "UnregisteredSeiTimecode": "DISABLED",
                                    "GopSizeUnits": "FRAMES",
                                    "ParControl": "INITIALIZE_FROM_SOURCE",
                                    "NumberBFramesBetweenReferenceFrames": 2,
                                    "RepeatPps": "DISABLED"
                                }
                            },
                            "AfdSignaling": "NONE",
                            "DropFrameTimecode": "ENABLED",
                            "RespondToAfd": "NONE",
                            "ColorMetadata": "INSERT"
                        },
                        "AudioDescriptions": [{
                            "AudioTypeControl": "FOLLOW_INPUT",
                            "CodecSettings": {
                                "Codec": "AAC",
                                "AacSettings": {
                                    "AudioDescriptionBroadcasterMix": "NORMAL",
                                    "RateControlMode": "CBR",
                                    "CodecProfile": "LC",
                                    "CodingMode": "CODING_MODE_2_0",
                                    "RawFormat": "NONE",
                                    "SampleRate": 48000,
                                    "Specification": "MPEG4"
                                }
                            },
                            "LanguageCodeControl": "FOLLOW_INPUT"
                        }],
                        "OutputSettings": {
                            "HlsSettings": {
                                "AudioGroupId": "program_audio",
                                "AudioRenditionSets": "program_audio",
                                "IFrameOnlyManifest": "EXCLUDE"
                            }
                        },
                        "NameModifier": "_v1"
                    },
                    {
                        "ContainerSettings": {
                            "Container": "M3U8",
                            "M3u8Settings": {
                                "AudioFramesPerPes": 4,
                                "PcrControl": "PCR_EVERY_PES_PACKET",
                                "PmtPid": 480,
                                "PrivateMetadataPid": 503,
                                "ProgramNumber": 1,
                                "PatInterval": 0,
                                "PmtInterval": 0,
                                "Scte35Source": "NONE",
                                "NielsenId3": "NONE",
                                "TimedMetadata": "NONE",
                                "VideoPid": 481,
                                "AudioPids": [
                                    482,
                                    483,
                                    484,
                                    485,
                                    486,
                                    487,
                                    488,
                                    489,
                                    490,
                                    491,
                                    492
                                ]
                            }
                        },
                        "AudioDescriptions": [{
                            "AudioTypeControl": "FOLLOW_INPUT",
                            "AudioSourceName": "Audio Selector 1",
                            "CodecSettings": {
                                "Codec": "AAC",
                                "AacSettings": {
                                    "AudioDescriptionBroadcasterMix": "NORMAL",
                                    "Bitrate": 64000,
                                    "RateControlMode": "CBR",
                                    "CodecProfile": "LC",
                                    "CodingMode": "CODING_MODE_2_0",
                                    "RawFormat": "NONE",
                                    "SampleRate": 48000,
                                    "Specification": "MPEG4"
                                }
                            },
                            "StreamName": "English",
                            "LanguageCodeControl": "FOLLOW_INPUT",
                            "LanguageCode": "ENG"
                        }],
                        "OutputSettings": {
                            "HlsSettings": {
                                "AudioGroupId": "program_audio",
                                "AudioRenditionSets": "program_audio",
                                "AudioTrackType": "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
                                "IFrameOnlyManifest": "EXCLUDE"
                            }
                        },
                        "NameModifier": "_a1"
                    },
                    {
                        "ContainerSettings": {
                            "Container": "M3U8",
                            "M3u8Settings": {
                                "AudioFramesPerPes": 4,
                                "PcrControl": "PCR_EVERY_PES_PACKET",
                                "PmtPid": 480,
                                "PrivateMetadataPid": 503,
                                "ProgramNumber": 1,
                                "PatInterval": 0,
                                "PmtInterval": 0,
                                "Scte35Source": "NONE",
                                "NielsenId3": "NONE",
                                "TimedMetadata": "NONE",
                                "VideoPid": 481,
                                "AudioPids": [
                                    482,
                                    483,
                                    484,
                                    485,
                                    486,
                                    487,
                                    488,
                                    489,
                                    490,
                                    491,
                                    492
                                ]
                            }
                        },
                        "AudioDescriptions": [{
                            "AudioTypeControl": "FOLLOW_INPUT",
                            "AudioSourceName": "Audio Selector 2",
                            "CodecSettings": {
                                "Codec": "AAC",
                                "AacSettings": {
                                    "AudioDescriptionBroadcasterMix": "NORMAL",
                                    "Bitrate": 64000,
                                    "RateControlMode": "CBR",
                                    "CodecProfile": "LC",
                                    "CodingMode": "CODING_MODE_2_0",
                                    "RawFormat": "NONE",
                                    "SampleRate": 48000,
                                    "Specification": "MPEG4"
                                }
                            },
                            "StreamName": "Spanish",
                            "LanguageCodeControl": "FOLLOW_INPUT",
                            "LanguageCode": "SPA"
                        }],
                        "OutputSettings": {
                            "HlsSettings": {
                                "AudioGroupId": "program_audio",
                                "AudioRenditionSets": "program_audio",
                                "AudioTrackType": "ALTERNATE_AUDIO_AUTO_SELECT",
                                "IFrameOnlyManifest": "EXCLUDE"
                            }
                        },
                        "NameModifier": "_a2"
                    }
                ],
                "OutputGroupSettings": {
                    "Type": "HLS_GROUP_SETTINGS",
                    "HlsGroupSettings": {
                        "ManifestDurationFormat": "INTEGER",
                        "SegmentLength": 6,
                        "TimedMetadataId3Period": 10,
                        "CaptionLanguageSetting": "OMIT",
                        "Destination": "s3://amzn-s3-demo-bucket/hls/no-drm/master",
                        "TimedMetadataId3Frame": "PRIV",
                        "CodecSpecification": "RFC_4281",
                        "OutputSelection": "MANIFESTS_AND_SEGMENTS",
                        "ProgramDateTimePeriod": 600,
                        "MinSegmentLength": 0,
                        "DirectoryStructure": "SINGLE_DIRECTORY",
                        "ProgramDateTime": "EXCLUDE",
                        "SegmentControl": "SEGMENTED_FILES",
                        "ManifestCompression": "NONE",
                        "ClientCache": "ENABLED",
                        "StreamInfResolution": "INCLUDE"
                    }
                }
            }
        ],
        "AdAvailOffset": 0,
        "Inputs": [{
            "AudioSelectors": {
                "Audio Selector 1": {
                    "Tracks": [
                        1
                    ],
                    "Offset": 0,
                    "DefaultSelection": "DEFAULT",
                    "SelectorType": "TRACK",
                    "ProgramSelection": 1
                },
                "Audio Selector 2": {
                    "Tracks": [
                        2
                    ],
                    "Offset": 0,
                    "DefaultSelection": "NOT_DEFAULT",
                    "SelectorType": "TRACK",
                    "ProgramSelection": 1
                }
            },
            "VideoSelector": {
                "ColorSpace": "FOLLOW"
            },
            "FilterEnable": "AUTO",
            "PsiControl": "USE_PSI",
            "FilterStrength": 0,
            "DeblockFilter": "DISABLED",
            "DenoiseFilter": "DISABLED",
            "TimecodeSource": "EMBEDDED",
            "FileInput": "s3://amzn-s3-demo-bucket/720/test_file.mp4"
        }]
    },
    "AccelerationSettings": {
        "Mode": "DISABLED"
    },
    "StatusUpdateInterval": "SECONDS_60",
    "Priority": 0
}
```
