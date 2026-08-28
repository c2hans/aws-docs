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

Use Probe to obtain detailed information about your input media files. Probe returns a JSON that includes container, codec, frame rate, resolution, track count, audio layout, captions, and more. You can use this information to learn more about your media files, or to help make decisions while automating your transcoding workflow.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ProbeResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
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
                "transferCharacteristics": enum
              }
            },
            "audioProperties": {
              "frameRate": {
                "numerator": integer,
                "denominator": integer
              },
              "sampleRate": integer,
              "channels": integer,
              "languageCode": "string",
              "bitDepth": integer,
              "bitRate": integer
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

### AudioProperties
<a name="probe-model-audioproperties"></a>

Details about the media file's audio track.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer | False | The bit depth of the audio track. |
| bitRate | integer<br />Format: int64 | False | The bit rate of the audio track, in bits per second. |
| channels | integer | False | The number of audio channels in the audio track. |
| frameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| languageCode | string | False | The language code of the audio track, in three character ISO 639-3 format. |
| sampleRate | integer | False | The sample rate of the audio track. |

### CodecMetadata
<a name="probe-model-codecmetadata"></a>

Codec-specific parameters parsed from the video essence headers. This information provides detailed technical specifications about how the video was encoded, including profile settings, resolution details, and color space information that can help you understand the source video characteristics and make informed encoding decisions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bitDepth | integer | False | The number of bits used per color component in the video essence such as 8, 10, or 12 bits. Standard range (SDR) video typically uses 8-bit, while 10-bit is common for high dynamic range (HDR). |
| chromaSubsampling | string | False | The chroma subsampling format used in the video encoding, such as "4:2:0" or "4:4:4". This describes how color information is sampled relative to brightness information. Different subsampling ratios affect video quality and file size, with "4:4:4" providing the highest color fidelity and "4:2:0" being most common for standard video. |
| codedFrameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| colorPrimaries | [ColorPrimaries](#probe-model-colorprimaries) | False | The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding. |
| height | integer | False | The height in pixels as coded by the codec. This represents the actual encoded video height as specified in the video stream headers. |
| level | string | False | The codec level or tier that specifies the maximum processing requirements and capabilities. Levels define constraints such as maximum bit rate, frame rate, and resolution. |
| matrixCoefficients | [MatrixCoefficients](#probe-model-matrixcoefficients) | False | The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes. |
| profile | string | False | The codec profile used to encode the video. Profiles define specific feature sets and capabilities within a codec standard. For example, H.264 profiles include Baseline, Main, and High, each supporting different encoding features and complexity levels. |
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
| duration | number<br />Format: double | False | The total duration of your media file, in seconds. |
| format | string<br />Values: `mp4 \| quicktime \| matroska \| webm \| mxf \| wave \| avi \| mpegts` | False | The format of your media file. For example: MP4, QuickTime (MOV), Matroska (MKV), WebM, MXF, Wave, AVI, or MPEG-TS. Note that this will be blank if your media file has a format that the MediaConvert Probe operation does not recognize. |
| startTimecode | string | False | The start timecode of the media file, in HH:MM:SS:FF format (or HH:MM:SS;FF for drop frame timecode). Note that this field is null when the container does not include an embedded start timecode. |
| tracks | Array of type [Track](#probe-model-track) | False | Details about each track (video, audio, or data) in the media file. |

### DataProperties
<a name="probe-model-dataproperties"></a>

Details about the media file's data track.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| languageCode | string | False | The language code of the data track, in three character ISO 639-3 format. |

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
| codec | string<br />Values: `UNKNOWN \| AAC \| AC3 \| EAC3 \| FLAC \| MP3 \| OPUS \| PCM \| VORBIS \| AV1 \| AVC \| HEVC \| JPEG2000 \| MJPEG \| MPEG1 \| MP4V \| MPEG2 \| PRORES \| QTRLE \| THEORA \| UNCOMPRESSED \| VFW \| VP8 \| VP9 \| C608 \| C708 \| WEBVTT` | False | The codec of the audio or video track, or caption format of the data track. |
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
| codecMetadata | [CodecMetadata](#probe-model-codecmetadata) | False | Codec-specific parameters parsed from the video essence headers. This information provides detailed technical specifications about how the video was encoded, including profile settings, resolution details, and color space information that can help you understand the source video characteristics and make informed encoding decisions. |
| colorPrimaries | [ColorPrimaries](#probe-model-colorprimaries) | False | The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding. |
| frameRate | [FrameRate](#probe-model-framerate) | False | The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values. |
| height | integer | False | The height of the video track, in pixels. |
| matrixCoefficients | [MatrixCoefficients](#probe-model-matrixcoefficients) | False | The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes. |
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
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/Probe)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/Probe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
