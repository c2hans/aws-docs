---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/probe.html
---

# Probe
<a name="probe"></a>

## URI
<a name="probe-url"></a>

`/2017-08-29/probe`

## HTTP methods
<a name="probe-http-methods"></a>

### POST
<a name="probepost"></a>

**Operation ID:** `Probe`

Use Probe to obtain detailed information about your input media files. Probe returns a JSON that includes container, codec, frame rate, resolution, track count, audio layout, captions, and more. You can use this information to learn more about your media files, or to help make decisions while automating your transcoding workflow. Probe supports the following input container formats: MP4, QuickTime (MOV), 3GP, 3G2, Matroska (MKV), WebM, MXF, MPEG-TS, MPEG-PS, AVI, WAV, MP3, FLAC, Ogg, and ASF (Windows Media / WMA). The fields that Probe returns vary by container and codec. A field isn't returned when the source doesn't contain it, or when it isn't available for that container and codec.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ProbeResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 422 | ExceptionBody | The input file was recognized but appears to be malformed or corrupt. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="probeoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="probe-schemas"></a>

### Request bodies
<a name="probe-request-examples"></a>

#### POST schema
<a name="probe-request-body-post-example"></a>

```
{
  "inputFiles": [
    {
      "fileUrl": "string"
    }
  ]
}
```

### Response bodies
<a name="probe-response-examples"></a>

#### ProbeResponse schema
<a name="probe-response-body-proberesponse-example"></a>

```
{
  "probeResults": [
    {
      "metadata": {
        "fileSize": integer,
        "eTag": "string",
        "lastModified": "string",
        "mimeType": "string"
      },
      "container": {
        "format": enum,
        "duration": number,
        "bitRate": integer,
        "startTimecode": "string",
        "tracks": [
          {
            "index": integer,
            "codec": enum,
            "duration": number,
            "trackType": enum,
            "videoProperties": {
              "frameRate": {
                "numerator": integer,
                "denominator": integer
              },
              "width": integer,
              "height": integer,
              "bitDepth": integer,
              "bitRate": integer,
              "colorPrimaries": enum,
              "matrixCoefficients": enum,
              "transferCharacteristics": enum,
              "codecMetadata": {
                "profile": "string",
                "level": "string",
                "chromaSubsampling": "string",
                "scanType": "string",
                "codedFrameRate": {
                  "numerator": integer,
                  "denominator": integer
                },
                "width": integer,
                "height": integer,
                "bitDepth": integer,
                "colorPrimaries": enum,
                "matrixCoefficients": enum,
                "transferCharacteristics": enum,
                "contentLightLevel": {
                  "maxContentLightLevel": integer,
                  "maxFrameAverageLightLevel": integer
                },
                "hdr10PlusPresence": enum,
                "rotation": integer,
                "fieldOrder": "string",
                "dolbyVision": {
                  "profile": integer,
                  "level": integer,
                  "rpu": enum,
                  "baseLayer": enum,
                  "enhancementLayer": enum
                },
                "sampleAspectRatio": {
                  "numerator": integer,
                  "denominator": integer
                },
                "displayAspectRatio": {
                  "numerator": integer,
                  "denominator": integer
                }
              },
              "hdrMetadata": {
                "masteringDisplayColorVolume": {
                  "redPrimaryX": integer,
                  "redPrimaryY": integer,
                  "greenPrimaryX": integer,
                  "greenPrimaryY": integer,
                  "bluePrimaryX": integer,
                  "bluePrimaryY": integer,
                  "whitePointX": integer,
                  "whitePointY": integer,
                  "maxLuminance": integer,
                  "minLuminance": integer
                },
                "contentLightLevel": {
                  "maxContentLightLevel": integer,
                  "maxFrameAverageLightLevel": integer
                }
              },
              "rotation": integer,
              "sampleAspectRatio": {
                "numerator": integer,
                "denominator": integer
              },
              "displayAspectRatio": {
                "numerator": integer,
                "denominator": integer
              }
            },
            "audioProperties": {
              "frameRate": {
                "numerator": integer,
                "denominator": integer
              },
              "sampleRate": integer,
              "channels": integer,
              "channelLayout": "string",
              "languageCode": "string",
              "bitDepth": integer,
              "bitRate": integer,
              "objectCount": integer
            },
            "dataProperties": {
              "languageCode": "string"
            }
          }
        ]
      },
      "trackMappings": [
        {
          "videoTrackIndexes": [
            integer
          ],
          "audioTrackIndexes": [
            integer
          ],
          "dataTrackIndexes": [
            integer
          ]
        }
      ]
    }
  ]
}
```

#### ExceptionBody schema
<a name="probe-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="probe-properties"></a>

### AspectRatio
<a name="probe-model-aspectratio"></a>

An aspect ratio expressed as a fraction with numerator and denominator values, reduced to lowest terms. Used for the sample (pixel) aspect ratio and the display aspect ratio of a video track. For example, a 720x576 anamorphic track has a sample aspect ratio of 64 / 45 and a display aspect ratio of 16 / 9. A video track can declare an aspect ratio in two independent places, and MediaConvert reports each one where it was found rather than choosing between them. The ratio declared by the container appears on the video track itself, and the ratio declared by the video essence appears under codecMetadata. When a file declares an aspect ratio in only one of the two places, the other is null; when it declares both and they disagree, you can compare them and decide which to use.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| denominator | integer | False | The denominator, or bottom number, in the fractional aspect ratio. For example, for a display aspect ratio of 16 / 9, the denominator would be 9. |
| numerator | integer | False | The numerator, or top number, in the fractional aspect ratio. For example, for a display aspect ratio of 16 / 9, the numerator would be 16. |

### AudioProperties
<a name="probe-model-audioproperties"></a>

Details about the media file's audio track.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer | False | The bit depth of the audio track. This value is exact for PCM and FLAC audio. For lossy codecs, such as AAC, AC-3, and E-AC-3, it is a nominal value and should be treated as approximate. |
| bitRate | integer<br />Format: int64 | False | The bit rate of the audio track, in bits per second. |
| channelLayout | string | False | The audio channel layout of the track, such as "mono", "stereo", "5.1", or "7.1". Object-based or immersive audio is reported as "5.1.4" or "7.1.4". The layout is exact for AC-3 and E-AC-3 audio. For other codecs, it is inferred from the channel count and should be treated as approximate. |
| channels | integer | False | The number of audio channels in the audio track. |
| frameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| languageCode | string | False | The language code of the audio track, in three character ISO 639-3 format. |
| objectCount | integer | False | The number of audio objects in an object-based or immersive audio track. This field is present for codecs that support object-based audio, such as E-AC-3 with Joint Object Coding (JOC) or IAMF. This field is null when the audio track does not contain object-based audio metadata. |
| sampleRate | integer | False | The sample rate of the audio track. |

### CodecMetadata
<a name="probe-model-codecmetadata"></a>

Codec-specific parameters parsed from the video essence headers. This information provides detailed technical specifications about how the video was encoded, including profile settings, resolution details, and color space information that can help you understand the source video characteristics and make informed encoding decisions. These fields are returned for H.264 (AVC), H.265 (HEVC), and MPEG-2 video, and might not be returned for other codecs. For MPEG-TS and MPEG-PS inputs, color information (color primaries, transfer characteristics, and matrix coefficients) appears in these fields rather than in the top-level videoProperties.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer | False | The number of bits used per color component in the video essence such as 8, 10, or 12 bits. Standard range (SDR) video typically uses 8-bit, while 10-bit is common for high dynamic range (HDR). |
| chromaSubsampling | string | False | The chroma subsampling format used in the video encoding, such as "4:2:0" or "4:4:4". This describes how color information is sampled relative to brightness information. Different subsampling ratios affect video quality and file size, with "4:4:4" providing the highest color fidelity and "4:2:0" being most common for standard video. |
| codedFrameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| colorPrimaries | [ColorPrimaries](#probe-model-colorprimaries) | False | The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding. |
| contentLightLevel | [ContentLightLevel](#probe-model-contentlightlevel) | False | Content light level information (CTA-861.3). Describes the light level characteristics of the content. |
| displayAspectRatio | [AspectRatio](#probe-model-aspectratio) | False | An aspect ratio expressed as a fraction with numerator and denominator values, reduced to lowest terms. Used for the sample (pixel) aspect ratio and the display aspect ratio of a video track. For example, a 720x576 anamorphic track has a sample aspect ratio of 64 / 45 and a display aspect ratio of 16 / 9. A video track can declare an aspect ratio in two independent places, and MediaConvert reports each one where it was found rather than choosing between them. The ratio declared by the container appears on the video track itself, and the ratio declared by the video essence appears under codecMetadata. When a file declares an aspect ratio in only one of the two places, the other is null; when it declares both and they disagree, you can compare them and decide which to use. |
| dolbyVision | [DolbyVisionMetadata](#probe-model-dolbyvisionmetadata) | False | Dolby Vision characteristics of the video track: the profile and level, and whether the RPU (dynamic metadata), base layer, and enhancement layer are present. Use this to distinguish Dolby Vision content from standard HEVC and to choose your encoding or passthrough settings. Omitted when the content is not Dolby Vision. |
| fieldOrder | string | False | The field order of interlaced video, which indicates whether the top or bottom field is displayed first. Use this to select the correct deinterlacing behavior. One of "TopFieldFirst" or "BottomFieldFirst". This field is present only for interlaced video; it is omitted for progressive video and when the field order is not indicated by the source. |
| hdr10PlusPresence | [Hdr10PlusPresence](#probe-model-hdr10pluspresence) | False | Indicates that HDR10\+ (SMPTE ST 2094-40) dynamic metadata was detected in the HEVC bitstream. Present only when detected. |
| height | integer | False | The height in pixels as coded by the codec. This represents the actual encoded video height as specified in the video stream headers. |
| level | string | False | The codec level or tier that specifies the maximum processing requirements and capabilities. Levels define constraints such as maximum bit rate, frame rate, and resolution. |
| matrixCoefficients | [MatrixCoefficients](#probe-model-matrixcoefficients) | False | The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes. |
| profile | string | False | The codec profile used to encode the video. Profiles define specific feature sets and capabilities within a codec standard. For example, H.264 profiles include Baseline, Main, and High, each supporting different encoding features and complexity levels. |
| rotation | integer | False | The clockwise rotation angle of the video, in degrees, as specified in the codec bitstream via a Display Orientation SEI message (payload type 47 for both H.264 and H.265). This field is null when the video essence does not contain a Display Orientation SEI message or when the rotation is 0 degrees. |
| sampleAspectRatio | [AspectRatio](#probe-model-aspectratio) | False | An aspect ratio expressed as a fraction with numerator and denominator values, reduced to lowest terms. Used for the sample (pixel) aspect ratio and the display aspect ratio of a video track. For example, a 720x576 anamorphic track has a sample aspect ratio of 64 / 45 and a display aspect ratio of 16 / 9. A video track can declare an aspect ratio in two independent places, and MediaConvert reports each one where it was found rather than choosing between them. The ratio declared by the container appears on the video track itself, and the ratio declared by the video essence appears under codecMetadata. When a file declares an aspect ratio in only one of the two places, the other is null; when it declares both and they disagree, you can compare them and decide which to use. |
| scanType | string | False | The scanning method specified in the video essence, indicating whether the video uses progressive or interlaced scanning. |
| transferCharacteristics | [TransferCharacteristics](#probe-model-transfercharacteristics) | False | The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction. |
| width | integer | False | The width in pixels as coded by the codec. This represents the actual encoded video width as specified in the video stream headers. |

### ColorPrimaries
<a name="probe-model-colorprimaries"></a>

The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding.
+ `ITU_709`
+ `UNSPECIFIED`
+ `RESERVED`
+ `ITU_470M`
+ `ITU_470BG`
+ `SMPTE_170M`
+ `SMPTE_240M`
+ `GENERIC_FILM`
+ `ITU_2020`
+ `SMPTE_428_1`
+ `SMPTE_431_2`
+ `SMPTE_EG_432_1`
+ `IPT`
+ `SMPTE_2067XYZ`
+ `EBU_3213_E`
+ `LAST`

### Container
<a name="probe-model-container"></a>

The container of your media file. This information helps you understand the overall structure and details of your media, including format, duration, and track layout.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitRate | integer<br />Format: int64 | False | The overall bit rate of your media file, in bits per second. This is derived from the file size and duration as (file size in bytes \* 8) / duration in seconds. |
| duration | number<br />Format: double | False | The total duration of your media file, in seconds. |
| format | string<br />Values: `mp4 \| quicktime \| matroska \| webm \| mxf \| wave \| avi \| mpegts \| mpegps \| mp3 \| flac \| asf \| ogg \| three_gp \| three_g2 \| aac \| ac3 \| eac3` | False | The format of your media file. For example: MP4, QuickTime (MOV), Matroska (MKV), WebM, MXF, Wave, AVI, MPEG-TS, MPEG-PS, MP3, FLAC, ASF (Windows Media / WMA), OGG, 3GP, 3G2, AAC (raw ADTS), AC-3, or Enhanced AC-3 (E-AC-3). Note that this will be blank if your media file has a format that the MediaConvert Probe operation does not recognize. |
| startTimecode | string | False | The start timecode of the media file, in HH:MM:SS:FF format (or HH:MM:SS;FF for drop frame timecode). Note that this field is null when the container does not include an embedded start timecode. |
| tracks | Array of type [Track](#probe-model-track) | False | Details about each track (video, audio, or data) in the media file. |

### ContentLightLevel
<a name="probe-model-contentlightlevel"></a>

Content light level information (CTA-861.3). Describes the light level characteristics of the content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxContentLightLevel | integer | False | Maximum content light level (MaxCLL), in cd/m². |
| maxFrameAverageLightLevel | integer | False | Maximum frame-average light level (MaxFALL), in cd/m². |

### DataProperties
<a name="probe-model-dataproperties"></a>

Details about the media file's data track.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | False | The language code of the data track, in three character ISO 639-3 format. |

### DolbyVisionMetadata
<a name="probe-model-dolbyvisionmetadata"></a>

Dolby Vision characteristics of the video track: the profile and level, and whether the RPU (dynamic metadata), base layer, and enhancement layer are present. Use this to distinguish Dolby Vision content from standard HEVC and to choose your encoding or passthrough settings. Omitted when the content is not Dolby Vision.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| baseLayer | [DolbyVisionPresence](#probe-model-dolbyvisionpresence) | False | Whether a Dolby Vision component is present in the track. |
| enhancementLayer | [DolbyVisionPresence](#probe-model-dolbyvisionpresence) | False | Whether a Dolby Vision component is present in the track. |
| level | integer | False | The Dolby Vision level, which indicates the maximum resolution and frame rate. |
| profile | integer | False | The Dolby Vision profile, for example 5, 7, or 8. The profile determines the layer structure and playback compatibility of the content. |
| rpu | [DolbyVisionPresence](#probe-model-dolbyvisionpresence) | False | Whether a Dolby Vision component is present in the track. |

### DolbyVisionPresence
<a name="probe-model-dolbyvisionpresence"></a>

Whether a Dolby Vision component is present in the track.
+ `PRESENT`
+ `ABSENT`

### ExceptionBody
<a name="probe-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### FrameRate
<a name="probe-model-framerate"></a>

The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| denominator | integer | False | The denominator, or bottom number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the denominator would be 1001. |
| numerator | integer | False | The numerator, or top number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the numerator would be 24000. |

### Hdr10PlusPresence
<a name="probe-model-hdr10pluspresence"></a>

Indicates that HDR10\+ (SMPTE ST 2094-40) dynamic metadata was detected in the HEVC bitstream. Present only when detected.
+ `PRESENT`

### HdrMetadata
<a name="probe-model-hdrmetadata"></a>

HDR (High Dynamic Range) metadata extracted from the container, including mastering display color volume and content light level information. This metadata is present in HDR10 and similar HDR content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentLightLevel | [ContentLightLevel](#probe-model-contentlightlevel) | False | Content light level information (CTA-861.3). Describes the light level characteristics of the content. |
| masteringDisplayColorVolume | [MasteringDisplayColorVolume](#probe-model-masteringdisplaycolorvolume) | False | Mastering display color volume metadata (SMPTE ST 2086). Describes the color volume of the display used to master the content. Chromaticity coordinates are in units of 0.00002. Luminance values are in units of 0.0001 cd/m². |

### MasteringDisplayColorVolume
<a name="probe-model-masteringdisplaycolorvolume"></a>

Mastering display color volume metadata (SMPTE ST 2086). Describes the color volume of the display used to master the content. Chromaticity coordinates are in units of 0.00002. Luminance values are in units of 0.0001 cd/m².

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bluePrimaryX | integer | False | Blue primary chromaticity x coordinate, in units of 0.00002. |
| bluePrimaryY | integer | False | Blue primary chromaticity y coordinate, in units of 0.00002. |
| greenPrimaryX | integer | False | Green primary chromaticity x coordinate, in units of 0.00002. |
| greenPrimaryY | integer | False | Green primary chromaticity y coordinate, in units of 0.00002. |
| maxLuminance | integer<br />Format: int64 | False | Maximum display mastering luminance, in units of 0.0001 cd/m². |
| minLuminance | integer<br />Format: int64 | False | Minimum display mastering luminance, in units of 0.0001 cd/m². |
| redPrimaryX | integer | False | Red primary chromaticity x coordinate, in units of 0.00002. |
| redPrimaryY | integer | False | Red primary chromaticity y coordinate, in units of 0.00002. |
| whitePointX | integer | False | White point chromaticity x coordinate, in units of 0.00002. |
| whitePointY | integer | False | White point chromaticity y coordinate, in units of 0.00002. |

### MatrixCoefficients
<a name="probe-model-matrixcoefficients"></a>

The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes.
+ `RGB`
+ `ITU_709`
+ `UNSPECIFIED`
+ `RESERVED`
+ `FCC`
+ `ITU_470BG`
+ `SMPTE_170M`
+ `SMPTE_240M`
+ `YCgCo`
+ `ITU_2020_NCL`
+ `ITU_2020_CL`
+ `SMPTE_2085`
+ `CD_NCL`
+ `CD_CL`
+ `ITU_2100ICtCp`
+ `IPT`
+ `EBU3213`
+ `LAST`

### Metadata
<a name="probe-model-metadata"></a>

Metadata and other file information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| eTag | string | False | The entity tag (ETag) of the file. |
| fileSize | integer<br />Format: int64 | False | The size of the media file, in bytes. |
| lastModified | string<br />Format: date-time | False | The last modification timestamp of the media file, in Unix time. |
| mimeType | string | False | The MIME type of the media file. |

### ProbeInputFile
<a name="probe-model-probeinputfile"></a>

The input file that needs to be analyzed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileUrl | string | False | Specify the S3, HTTP, or HTTPS URL for your media file. |

### ProbeRequest
<a name="probe-model-proberequest"></a>

A request to probe a media file and retrieve its metadata.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputFiles | Array of type [ProbeInputFile](#probe-model-probeinputfile) | False | Specify a media file to probe. |

### ProbeResponse
<a name="probe-model-proberesponse"></a>

The response from a MediaConvert Probe operation, in JSON form, with detailed information about your input media.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| probeResults | Array of type [ProbeResult](#probe-model-proberesult) | False | Probe results for your media file. |

### ProbeResult
<a name="probe-model-proberesult"></a>

Probe results for your media file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| container | [Container](#probe-model-container) | False | The container of your media file. This information helps you understand the overall structure and details of your media, including format, duration, and track layout. |
| metadata | [Metadata](#probe-model-metadata) | False | Metadata and other file information. |
| trackMappings | Array of type [TrackMapping](#probe-model-trackmapping) | False | An array containing track mapping information. |

### Track
<a name="probe-model-track"></a>

Details about each track (video, audio, or data) in the media file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioProperties | [AudioProperties](#probe-model-audioproperties) | False | Details about the media file's audio track. |
| codec | string<br />Values: `UNKNOWN \| AAC \| AC3 \| AMR \| EAC3 \| FLAC \| MP2 \| MP3 \| OPUS \| PCM \| VORBIS \| WMA \| WMA2 \| WMAPRO \| AV1 \| AVC \| DV \| H263 \| HEVC \| JPEG2000 \| MJPEG \| MPEG1 \| MP4V \| MPEG2 \| PRORES \| QTRLE \| THEORA \| UNCOMPRESSED \| VC1 \| VC3 \| VFW \| VP8 \| VP9 \| C608 \| C708 \| WEBVTT` | False | The codec of the audio or video track, or caption format of the data track. |
| dataProperties | [DataProperties](#probe-model-dataproperties) | False | Details about the media file's data track. |
| duration | number<br />Format: double | False | The duration of the track, in seconds. |
| index | integer | False | The unique index number of the track, starting at 1. |
| trackType | string<br />Values: `video \| audio \| data` | False | The type of track: video, audio, or data. |
| videoProperties | [VideoProperties](#probe-model-videoproperties) | False | Details about the media file's video track. |

### TrackMapping
<a name="probe-model-trackmapping"></a>

An array containing track mapping information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioTrackIndexes | Array of type integer | False | The index numbers of the audio tracks in your media file. |
| dataTrackIndexes | Array of type integer | False | The index numbers of the data tracks in your media file. |
| videoTrackIndexes | Array of type integer | False | The index numbers of the video tracks in your media file. |

### TransferCharacteristics
<a name="probe-model-transfercharacteristics"></a>

The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction.
+ `ITU_709`
+ `UNSPECIFIED`
+ `RESERVED`
+ `ITU_470M`
+ `ITU_470BG`
+ `SMPTE_170M`
+ `SMPTE_240M`
+ `LINEAR`
+ `LOG10_2`
+ `LOC10_2_5`
+ `IEC_61966_2_4`
+ `ITU_1361`
+ `IEC_61966_2_1`
+ `ITU_2020_10bit`
+ `ITU_2020_12bit`
+ `SMPTE_2084`
+ `SMPTE_428_1`
+ `ARIB_B67`
+ `LAST`

### VideoProperties
<a name="probe-model-videoproperties"></a>

Details about the media file's video track.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer | False | The number of bits used per color component such as 8, 10, or 12 bits. Standard range (SDR) video typically uses 8-bit, while 10-bit is common for high dynamic range (HDR). |
| bitRate | integer<br />Format: int64 | False | The bit rate of the video track, in bits per second. |
| codecMetadata | [CodecMetadata](#probe-model-codecmetadata) | False | Codec-specific parameters parsed from the video essence headers. This information provides detailed technical specifications about how the video was encoded, including profile settings, resolution details, and color space information that can help you understand the source video characteristics and make informed encoding decisions. These fields are returned for H.264 (AVC), H.265 (HEVC), and MPEG-2 video, and might not be returned for other codecs. For MPEG-TS and MPEG-PS inputs, color information (color primaries, transfer characteristics, and matrix coefficients) appears in these fields rather than in the top-level videoProperties. |
| colorPrimaries | [ColorPrimaries](#probe-model-colorprimaries) | False | The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding. |
| displayAspectRatio | [AspectRatio](#probe-model-aspectratio) | False | An aspect ratio expressed as a fraction with numerator and denominator values, reduced to lowest terms. Used for the sample (pixel) aspect ratio and the display aspect ratio of a video track. For example, a 720x576 anamorphic track has a sample aspect ratio of 64 / 45 and a display aspect ratio of 16 / 9. A video track can declare an aspect ratio in two independent places, and MediaConvert reports each one where it was found rather than choosing between them. The ratio declared by the container appears on the video track itself, and the ratio declared by the video essence appears under codecMetadata. When a file declares an aspect ratio in only one of the two places, the other is null; when it declares both and they disagree, you can compare them and decide which to use. |
| frameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| hdrMetadata | [HdrMetadata](#probe-model-hdrmetadata) | False | HDR (High Dynamic Range) metadata extracted from the container, including mastering display color volume and content light level information. This metadata is present in HDR10 and similar HDR content. |
| height | integer | False | The height of the video track, in pixels. |
| matrixCoefficients | [MatrixCoefficients](#probe-model-matrixcoefficients) | False | The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes. |
| rotation | integer | False | The clockwise rotation angle of the video track, in degrees, as derived from container-level metadata (e.g. the MP4 tkhd transformation matrix or the Matroska ProjectionPoseRoll element). Common values are 90, 180, and 270. This field is null when no rotation metadata is present or when the rotation is 0 degrees. For MP4, non-standard transformation matrices also yield null. |
| sampleAspectRatio | [AspectRatio](#probe-model-aspectratio) | False | An aspect ratio expressed as a fraction with numerator and denominator values, reduced to lowest terms. Used for the sample (pixel) aspect ratio and the display aspect ratio of a video track. For example, a 720x576 anamorphic track has a sample aspect ratio of 64 / 45 and a display aspect ratio of 16 / 9. A video track can declare an aspect ratio in two independent places, and MediaConvert reports each one where it was found rather than choosing between them. The ratio declared by the container appears on the video track itself, and the ratio declared by the video essence appears under codecMetadata. When a file declares an aspect ratio in only one of the two places, the other is null; when it declares both and they disagree, you can compare them and decide which to use. |
| transferCharacteristics | [TransferCharacteristics](#probe-model-transfercharacteristics) | False | The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction. |
| width | integer | False | The width of the video track, in pixels. |

## See also
<a name="probe-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### Probe
<a name="Probe-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/Probe)
