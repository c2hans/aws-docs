---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/doc-history.html
---

# Document History
<a name="doc-history"></a>

The following table describes important changes to this documentation.
+ **API version: 2017-08-29**

****

| Change | Description | Date |
| --- | --- | --- |
| Documentation update | Updated [Getting Started with MediaConvert Using the API](getting-started.md) chapter; minor updates to the sample job settings JSONs. | July 5, 2023 |
| Preventing duplicate jobs | Added a section that describes how to create an idempotent request and prevent duplicate jobs from being submitted. | August 1, 2022 |
| Additional captions formatsPer-input graphic image overlay<br />Motion graphic image overlay | Added input caption format support for SCTE-20 and SMI. Added output caption format support for SCTE-20 \+ Embedded, Embedded \+ SCTE-20, SMI, and SMPTE-TT.You can now now specify graphic overlays (inserted images) on individual inputs. <br />You can now overlay motion graphics over your video. | Nov 23, 2018 |
| Reserved transcoding queues | Reserved transcoding allows customers who have consistent video volume to benefit from lower rates in exchange for longer term commitments. | Sept 27, 2018 |
| Quality-Defined Variable Bitrate (QVBR) Encoding | Introduces an encoding mode where the service automatically determines how many bits to use for each portion of the video to maintain constant quality. | Aug 13, 2018 |
| Tagging and cost allocation | Add support for tagging and integration with cost allocation on AWS | July 2, 2018 |
| New CMAF output group | cmafGroupSettings and its children added to schema, under OutputGroupSettings.  | June 12, 2018 |
| New Getting Started Using SDKs or CLI | Added chapter that shows how to get your custom endpoint and send MediaConvert requests to it. Includes examples in various programming languages. | May 17, 2018 |
| New AWS Elemental MediaConvert service release | Initial documentation for the AWS Elemental MediaConvert service. | November 27, 2017 |
