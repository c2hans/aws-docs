---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/offerings-offeringid.html
---

# Offerings: describe offering
<a name="offerings-offeringid"></a>

## URI
<a name="offerings-offeringid-url"></a>

`/prod/offerings/{{offeringId}}`

## HTTP methods
<a name="offerings-offeringid-http-methods"></a>

### GET
<a name="offerings-offeringidget"></a>

**Operation ID:** `DescribeOffering`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{offeringId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Offering | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="offerings-offeringid-schemas"></a>

### Response bodies
<a name="offerings-offeringid-response-examples"></a>

#### Offering schema
<a name="offerings-offeringid-response-body-offering-example"></a>

```
{
  "arn": "string",
  "currencyCode": "string",
  "duration": integer,
  "durationUnits": enum,
  "fixedPrice": number,
  "offeringDescription": "string",
  "offeringId": "string",
  "offeringType": enum,
  "region": "string",
  "resourceSpecification": {
    "channelClass": enum,
    "codec": enum,
    "maximumBitrate": enum,
    "maximumFramerate": enum,
    "resolution": enum,
    "resourceType": enum,
    "specialFeature": enum,
    "videoQuality": enum
  },
  "usagePrice": number
}
```

#### InvalidRequest schema
<a name="offerings-offeringid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="offerings-offeringid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="offerings-offeringid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="offerings-offeringid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="offerings-offeringid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="offerings-offeringid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="offerings-offeringid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="offerings-offeringid-properties"></a>

### AccessDenied
<a name="offerings-offeringid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="offerings-offeringid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ChannelClass
<a name="offerings-offeringid-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### GatewayTimeoutException
<a name="offerings-offeringid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="offerings-offeringid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="offerings-offeringid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="offerings-offeringid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Offering
<a name="offerings-offeringid-model-offering"></a>

Reserved resources available for purchase

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321' |
| currencyCode | string | False | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD' |
| duration | integer | False | Lease duration, e.g. '12' |
| durationUnits | [OfferingDurationUnits](#offerings-offeringid-model-offeringdurationunits) | False | Units for duration, e.g. 'MONTHS' |
| fixedPrice | number | False | One-time charge for each reserved resource, e.g. '0.0' for a NO\_UPFRONT offering |
| offeringDescription | string | False | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offeringId | string | False | Unique offering ID, e.g. '87654321' |
| offeringType | [OfferingType](#offerings-offeringid-model-offeringtype) | False | Offering type, e.g. 'NO\_UPFRONT' |
| region | string | False | AWS Region, e.g. 'us-west-2' |
| resourceSpecification | [ReservationResourceSpecification](#offerings-offeringid-model-reservationresourcespecification) | False | Resource configuration details |
| usagePrice | number | False | Recurring usage charge for each reserved resource, e.g. '157.0' |

### OfferingDurationUnits
<a name="offerings-offeringid-model-offeringdurationunits"></a>

Units for duration, e.g. 'MONTHS'
+ `MONTHS`

### OfferingType
<a name="offerings-offeringid-model-offeringtype"></a>

Offering type, e.g. 'NO\_UPFRONT'
+ `NO_UPFRONT`

### ReservationCodec
<a name="offerings-offeringid-model-reservationcodec"></a>

Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
+ `MPEG2`
+ `AVC`
+ `HEVC`
+ `AUDIO`
+ `LINK`

### ReservationMaximumBitrate
<a name="offerings-offeringid-model-reservationmaximumbitrate"></a>

Maximum bitrate in megabits per second
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### ReservationMaximumFramerate
<a name="offerings-offeringid-model-reservationmaximumframerate"></a>

Maximum framerate in frames per second (Outputs only)
+ `MAX_30_FPS`
+ `MAX_60_FPS`

### ReservationResolution
<a name="offerings-offeringid-model-reservationresolution"></a>

Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### ReservationResourceSpecification
<a name="offerings-offeringid-model-reservationresourcespecification"></a>

Resource configuration (codec, resolution, bitrate, ...)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelClass | [ChannelClass](#offerings-offeringid-model-channelclass) | False | Channel class, e.g. 'STANDARD' |
| codec | [ReservationCodec](#offerings-offeringid-model-reservationcodec) | False | Codec, e.g. 'AVC' |
| maximumBitrate | [ReservationMaximumBitrate](#offerings-offeringid-model-reservationmaximumbitrate) | False | Maximum bitrate, e.g. 'MAX\_20\_MBPS' |
| maximumFramerate | [ReservationMaximumFramerate](#offerings-offeringid-model-reservationmaximumframerate) | False | Maximum framerate, e.g. 'MAX\_30\_FPS' (Outputs only) |
| resolution | [ReservationResolution](#offerings-offeringid-model-reservationresolution) | False | Resolution, e.g. 'HD' |
| resourceType | [ReservationResourceType](#offerings-offeringid-model-reservationresourcetype) | False | Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL' |
| specialFeature | [ReservationSpecialFeature](#offerings-offeringid-model-reservationspecialfeature) | False | Special feature, e.g. 'AUDIO\_NORMALIZATION' (Channels only) |
| videoQuality | [ReservationVideoQuality](#offerings-offeringid-model-reservationvideoquality) | False | Video quality, e.g. 'STANDARD' (Outputs only) |

### ReservationResourceType
<a name="offerings-offeringid-model-reservationresourcetype"></a>

Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
+ `INPUT`
+ `OUTPUT`
+ `MULTIPLEX`
+ `CHANNEL`

### ReservationSpecialFeature
<a name="offerings-offeringid-model-reservationspecialfeature"></a>

Special features, 'ADVANCED\_AUDIO' 'AUDIO\_NORMALIZATION' 'MGHD' or 'MGUHD'
+ `ADVANCED_AUDIO`
+ `AUDIO_NORMALIZATION`
+ `MGHD`
+ `MGUHD`

### ReservationVideoQuality
<a name="offerings-offeringid-model-reservationvideoquality"></a>

Video quality, e.g. 'STANDARD' (Outputs only)
+ `STANDARD`
+ `ENHANCED`
+ `PREMIUM`

### ResourceNotFound
<a name="offerings-offeringid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="offerings-offeringid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeOffering
<a name="DescribeOffering-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DescribeOffering)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeOffering)
