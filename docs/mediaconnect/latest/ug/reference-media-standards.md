---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html
---

# Reference: Supported media standards
<a name="reference-media-standards"></a>

**Important**
MediaConnect complies with and implements many media industry standards from different organizations. This reference is not intended to be a comprehensive list, but contains highlighted standards from specific organizations.

## Video Services Forum: technical recommendations
<a name="reference-vsf-tr"></a>

AWS Elemental MediaConnect supports *technical recommendations (TR)* from the *Video Services Forum (VSF)* for some features. This reference guide can be used to identify which TRs are supported by MediaConnect. For more information about technical recommendations, visit the VSF website: [VSF technical recommendations](https://www.videoservicesforum.org/technical_recommendations.shtml)

**Supported VSF technical recommendations**

| Technical recommendation | Description |
| --- | --- |
| TR-06-01: Reliable Internet Stream Transport (RIST) [Simple Profile] | This technical recommendation is for RIST Simple Profile support only. MediaConnect does not support Main, Enhanced, or Scalable Profiles when using RIST.  |
| TR-07: Transport of JPEG XS Video in MPEG-2 Transport Stream (TS) over IP TR-07 is automatically invoked when you use a supported protocol and the maximum bitrate is greater than 200 Mbps.  | MediaConnect supports JPEG XS transport in MPEG-2 TS over IP with the following requirements and limitations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html) |
| TR-08: Transport of JPEG XS Video in ST 2110-22 For JPEG XS passthrough flows where the video frames are not encoded by MediaConnect, the video frames are not decoded. As a result, no validation of TR-08 compliance is performed.  | MediaConnect supports JPEG XS transport over SMPTE ST 2110-22 with the following requirements and limitations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html)Supported color space, bit depth, and chroma sampling configurations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html) |

## SMPTE-2022
<a name="reference-media-standards-smpte-2022"></a>

MediaConnect supports many SMPTE (Society of Motion Picture and Television Engineers) standards. The following table is specific to SMPTE-2022 and includes a selection of standards. It is not a comprehensive list of all supported SMPTE standards.

**Supported SMPTE-2022 standards**

| Standard | Description |
| --- | --- |
| SMPTE-2022-7: Seamless Protection Switching of RTP |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html)  |
