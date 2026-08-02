---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/offerings-offeringid-purchase.html
---

# Offerings: purchase offering
<a name="offerings-offeringid-purchase"></a>

## URI
<a name="offerings-offeringid-purchase-url"></a>

`/prod/offerings/{{offeringId}}/purchase`

## HTTP methods
<a name="offerings-offeringid-purchase-http-methods"></a>

### POST
<a name="offerings-offeringid-purchasepost"></a>

**Operation ID:** `PurchaseOffering`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{offeringId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | PurchaseOfferingResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="offerings-offeringid-purchase-schemas"></a>

### Request bodies
<a name="offerings-offeringid-purchase-request-examples"></a>

#### POST schema
<a name="offerings-offeringid-purchase-request-body-post-example"></a>

```
{
  "count": integer,
  "name": "string",
  "requestId": "string",
  "start": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="offerings-offeringid-purchase-response-examples"></a>

#### PurchaseOfferingResultModel schema
<a name="offerings-offeringid-purchase-response-body-purchaseofferingresultmodel-example"></a>

```
{
  "reservation": {
    "arn": "string",
    "count": integer,
    "currencyCode": "string",
    "duration": integer,
    "durationUnits": enum,
    "end": "string",
    "fixedPrice": number,
    "name": "string",
    "offeringDescription": "string",
    "offeringId": "string",
    "offeringType": enum,
    "region": "string",
    "reservationId": "string",
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
    "start": "string",
    "state": enum,
    "tags": {
    },
    "usagePrice": number
  }
}
```

#### InvalidRequest schema
<a name="offerings-offeringid-purchase-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="offerings-offeringid-purchase-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="offerings-offeringid-purchase-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="offerings-offeringid-purchase-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="offerings-offeringid-purchase-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="offerings-offeringid-purchase-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="offerings-offeringid-purchase-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="offerings-offeringid-purchase-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="offerings-offeringid-purchase-properties"></a>

### AccessDenied
<a name="offerings-offeringid-purchase-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="offerings-offeringid-purchase-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ChannelClass
<a name="offerings-offeringid-purchase-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### GatewayTimeoutException
<a name="offerings-offeringid-purchase-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="offerings-offeringid-purchase-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="offerings-offeringid-purchase-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="offerings-offeringid-purchase-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### OfferingDurationUnits
<a name="offerings-offeringid-purchase-model-offeringdurationunits"></a>

Units for duration, e.g. 'MONTHS'
+ `MONTHS`

### OfferingType
<a name="offerings-offeringid-purchase-model-offeringtype"></a>

Offering type, e.g. 'NO\_UPFRONT'
+ `NO_UPFRONT`

### PurchaseOffering
<a name="offerings-offeringid-purchase-model-purchaseoffering"></a>

PurchaseOffering request

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| count | integer<br />Minimum: 1 | True | Number of resources |
| name | string | False | Name for the new reservation |
| requestId | string | False | Unique request ID to be specified. This is needed to prevent retries from creating multiple resources. |
| start | string | False | Requested reservation start time (UTC) in ISO-8601 format. The specified time must be between the first day of the current month and one year from now. If no value is given, the default is now. |
| tags | [Tags](#offerings-offeringid-purchase-model-tags) | False | A collection of key-value pairs |

### PurchaseOfferingResultModel
<a name="offerings-offeringid-purchase-model-purchaseofferingresultmodel"></a>

PurchaseOffering response

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| reservation | [Reservation](#offerings-offeringid-purchase-model-reservation) | False |  |

### Reservation
<a name="offerings-offeringid-purchase-model-reservation"></a>

Reserved resources available to use

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567' |
| count | integer | False | Number of reserved resources |
| currencyCode | string | False | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD' |
| duration | integer | False | Lease duration, e.g. '12' |
| durationUnits | [OfferingDurationUnits](#offerings-offeringid-purchase-model-offeringdurationunits) | False | Units for duration, e.g. 'MONTHS' |
| end | string | False | Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00' |
| fixedPrice | number | False | One-time charge for each reserved resource, e.g. '0.0' for a NO\_UPFRONT offering |
| name | string | False | User specified reservation name |
| offeringDescription | string | False | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offeringId | string | False | Unique offering ID, e.g. '87654321' |
| offeringType | [OfferingType](#offerings-offeringid-purchase-model-offeringtype) | False | Offering type, e.g. 'NO\_UPFRONT' |
| region | string | False | AWS Region, e.g. 'us-west-2' |
| reservationId | string | False | Unique reservation ID, e.g. '1234567' |
| resourceSpecification | [ReservationResourceSpecification](#offerings-offeringid-purchase-model-reservationresourcespecification) | False | Resource configuration details |
| start | string | False | Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00' |
| state | [ReservationState](#offerings-offeringid-purchase-model-reservationstate) | False | Current state of reservation, e.g. 'ACTIVE' |
| tags | [Tags](#offerings-offeringid-purchase-model-tags) | False | A collection of key-value pairs |
| usagePrice | number | False | Recurring usage charge for each reserved resource, e.g. '157.0' |

### ReservationCodec
<a name="offerings-offeringid-purchase-model-reservationcodec"></a>

Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
+ `MPEG2`
+ `AVC`
+ `HEVC`
+ `AUDIO`
+ `LINK`

### ReservationMaximumBitrate
<a name="offerings-offeringid-purchase-model-reservationmaximumbitrate"></a>

Maximum bitrate in megabits per second
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### ReservationMaximumFramerate
<a name="offerings-offeringid-purchase-model-reservationmaximumframerate"></a>

Maximum framerate in frames per second (Outputs only)
+ `MAX_30_FPS`
+ `MAX_60_FPS`

### ReservationResolution
<a name="offerings-offeringid-purchase-model-reservationresolution"></a>

Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### ReservationResourceSpecification
<a name="offerings-offeringid-purchase-model-reservationresourcespecification"></a>

Resource configuration (codec, resolution, bitrate, ...)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelClass | [ChannelClass](#offerings-offeringid-purchase-model-channelclass) | False | Channel class, e.g. 'STANDARD' |
| codec | [ReservationCodec](#offerings-offeringid-purchase-model-reservationcodec) | False | Codec, e.g. 'AVC' |
| maximumBitrate | [ReservationMaximumBitrate](#offerings-offeringid-purchase-model-reservationmaximumbitrate) | False | Maximum bitrate, e.g. 'MAX\_20\_MBPS' |
| maximumFramerate | [ReservationMaximumFramerate](#offerings-offeringid-purchase-model-reservationmaximumframerate) | False | Maximum framerate, e.g. 'MAX\_30\_FPS' (Outputs only) |
| resolution | [ReservationResolution](#offerings-offeringid-purchase-model-reservationresolution) | False | Resolution, e.g. 'HD' |
| resourceType | [ReservationResourceType](#offerings-offeringid-purchase-model-reservationresourcetype) | False | Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL' |
| specialFeature | [ReservationSpecialFeature](#offerings-offeringid-purchase-model-reservationspecialfeature) | False | Special feature, e.g. 'AUDIO\_NORMALIZATION' (Channels only) |
| videoQuality | [ReservationVideoQuality](#offerings-offeringid-purchase-model-reservationvideoquality) | False | Video quality, e.g. 'STANDARD' (Outputs only) |

### ReservationResourceType
<a name="offerings-offeringid-purchase-model-reservationresourcetype"></a>

Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
+ `INPUT`
+ `OUTPUT`
+ `MULTIPLEX`
+ `CHANNEL`

### ReservationSpecialFeature
<a name="offerings-offeringid-purchase-model-reservationspecialfeature"></a>

Special features, 'ADVANCED\_AUDIO' 'AUDIO\_NORMALIZATION' 'MGHD' or 'MGUHD'
+ `ADVANCED_AUDIO`
+ `AUDIO_NORMALIZATION`
+ `MGHD`
+ `MGUHD`

### ReservationState
<a name="offerings-offeringid-purchase-model-reservationstate"></a>

Current reservation state
+ `ACTIVE`
+ `EXPIRED`
+ `CANCELED`
+ `DELETED`

### ReservationVideoQuality
<a name="offerings-offeringid-purchase-model-reservationvideoquality"></a>

Video quality, e.g. 'STANDARD' (Outputs only)
+ `STANDARD`
+ `ENHANCED`
+ `PREMIUM`

### ResourceConflict
<a name="offerings-offeringid-purchase-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="offerings-offeringid-purchase-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="offerings-offeringid-purchase-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="offerings-offeringid-purchase-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### PurchaseOffering
<a name="PurchaseOffering-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/PurchaseOffering)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/PurchaseOffering)
