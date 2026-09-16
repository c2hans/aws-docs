---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/offerings.html
---

# Offerings: list offerings
<a name="offerings"></a>

## URI
<a name="offerings-url"></a>

`/prod/offerings`

## HTTP methods
<a name="offerings-http-methods"></a>

### GET
<a name="offeringsget"></a>

**Operation ID:** `ListOfferings`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceType | String | False |  |
| nextToken | String | False |  |
| channelConfiguration | String | False |  |
| duration | String | False |  |
| codec | String | False |  |
| videoQuality | String | False |  |
| resolution | String | False |  |
| maximumFramerate | String | False |  |
| channelClass | String | False |  |
| maxResults | String | False |  |
| maximumBitrate | String | False |  |
| specialFeature | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListOfferingsResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="offerings-schemas"></a>

### Response bodies
<a name="offerings-response-examples"></a>

#### ListOfferingsResultModel schema
<a name="offerings-response-body-listofferingsresultmodel-example"></a>

```
{
  "nextToken": "string",
  "offerings": [
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
  ]
}
```

#### InvalidRequest schema
<a name="offerings-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="offerings-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="offerings-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="offerings-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="offerings-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="offerings-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="offerings-properties"></a>

### AccessDenied
<a name="offerings-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="offerings-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ChannelClass
<a name="offerings-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### GatewayTimeoutException
<a name="offerings-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="offerings-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="offerings-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="offerings-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListOfferingsResultModel
<a name="offerings-model-listofferingsresultmodel"></a>

ListOfferings response

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Token to retrieve the next page of results |
| offerings | Array of type [Offering](#offerings-model-offering) | False | List of offerings |

### Offering
<a name="offerings-model-offering"></a>

Reserved resources available for purchase

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321' |
| currencyCode | string | False | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD' |
| duration | integer | False | Lease duration, e.g. '12' |
| durationUnits | [OfferingDurationUnits](#offerings-model-offeringdurationunits) | False | Units for duration, e.g. 'MONTHS' |
| fixedPrice | number | False | One-time charge for each reserved resource, e.g. '0.0' for a NO\_UPFRONT offering |
| offeringDescription | string | False | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offeringId | string | False | Unique offering ID, e.g. '87654321' |
| offeringType | [OfferingType](#offerings-model-offeringtype) | False | Offering type, e.g. 'NO\_UPFRONT' |
| region | string | False | AWS Region, e.g. 'us-west-2' |
| resourceSpecification | [ReservationResourceSpecification](#offerings-model-reservationresourcespecification) | False | Resource configuration details |
| usagePrice | number | False | Recurring usage charge for each reserved resource, e.g. '157.0' |

### OfferingDurationUnits
<a name="offerings-model-offeringdurationunits"></a>

Units for duration, e.g. 'MONTHS'
+ `MONTHS`

### OfferingType
<a name="offerings-model-offeringtype"></a>

Offering type, e.g. 'NO\_UPFRONT'
+ `NO_UPFRONT`

### ReservationCodec
<a name="offerings-model-reservationcodec"></a>

Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
+ `MPEG2`
+ `AVC`
+ `HEVC`
+ `AUDIO`
+ `LINK`

### ReservationMaximumBitrate
<a name="offerings-model-reservationmaximumbitrate"></a>

Maximum bitrate in megabits per second
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### ReservationMaximumFramerate
<a name="offerings-model-reservationmaximumframerate"></a>

Maximum framerate in frames per second (Outputs only)
+ `MAX_30_FPS`
+ `MAX_60_FPS`

### ReservationResolution
<a name="offerings-model-reservationresolution"></a>

Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### ReservationResourceSpecification
<a name="offerings-model-reservationresourcespecification"></a>

Resource configuration (codec, resolution, bitrate, ...)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelClass | [ChannelClass](#offerings-model-channelclass) | False | Channel class, e.g. 'STANDARD' |
| codec | [ReservationCodec](#offerings-model-reservationcodec) | False | Codec, e.g. 'AVC' |
| maximumBitrate | [ReservationMaximumBitrate](#offerings-model-reservationmaximumbitrate) | False | Maximum bitrate, e.g. 'MAX\_20\_MBPS' |
| maximumFramerate | [ReservationMaximumFramerate](#offerings-model-reservationmaximumframerate) | False | Maximum framerate, e.g. 'MAX\_30\_FPS' (Outputs only) |
| resolution | [ReservationResolution](#offerings-model-reservationresolution) | False | Resolution, e.g. 'HD' |
| resourceType | [ReservationResourceType](#offerings-model-reservationresourcetype) | False | Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL' |
| specialFeature | [ReservationSpecialFeature](#offerings-model-reservationspecialfeature) | False | Special feature, e.g. 'AUDIO\_NORMALIZATION' (Channels only) |
| videoQuality | [ReservationVideoQuality](#offerings-model-reservationvideoquality) | False | Video quality, e.g. 'STANDARD' (Outputs only) |

### ReservationResourceType
<a name="offerings-model-reservationresourcetype"></a>

Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
+ `INPUT`
+ `OUTPUT`
+ `MULTIPLEX`
+ `CHANNEL`

### ReservationSpecialFeature
<a name="offerings-model-reservationspecialfeature"></a>

Special features, 'ADVANCED\_AUDIO' 'AUDIO\_NORMALIZATION' 'MGHD' or 'MGUHD'
+ `ADVANCED_AUDIO`
+ `AUDIO_NORMALIZATION`
+ `MGHD`
+ `MGUHD`

### ReservationVideoQuality
<a name="offerings-model-reservationvideoquality"></a>

Video quality, e.g. 'STANDARD' (Outputs only)
+ `STANDARD`
+ `ENHANCED`
+ `PREMIUM`

## See also
<a name="offerings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListOfferings
<a name="ListOfferings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/ListOfferings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListOfferings)
