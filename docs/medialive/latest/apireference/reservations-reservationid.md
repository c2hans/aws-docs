---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/reservations-reservationid.html
---

# Reservations: describe reservation
<a name="reservations-reservationid"></a>

## URI
<a name="reservations-reservationid-url"></a>

`/prod/reservations/{{reservationId}}`

## HTTP methods
<a name="reservations-reservationid-http-methods"></a>

### DELETE
<a name="reservations-reservationiddelete"></a>

**Operation ID:** `DeleteReservation`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{reservationId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Reservation | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### GET
<a name="reservations-reservationidget"></a>

**Operation ID:** `DescribeReservation`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{reservationId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Reservation | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="reservations-reservationidput"></a>

**Operation ID:** `UpdateReservation`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{reservationId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateReservationResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="reservations-reservationid-schemas"></a>

### Request bodies
<a name="reservations-reservationid-request-examples"></a>

#### PUT schema
<a name="reservations-reservationid-request-body-put-example"></a>

```
{
  "name": "string"
}
```

### Response bodies
<a name="reservations-reservationid-response-examples"></a>

#### Reservation schema
<a name="reservations-reservationid-response-body-reservation-example"></a>

```
{
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
```

#### UpdateReservationResultModel schema
<a name="reservations-reservationid-response-body-updatereservationresultmodel-example"></a>

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
<a name="reservations-reservationid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="reservations-reservationid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="reservations-reservationid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="reservations-reservationid-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="reservations-reservationid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="reservations-reservationid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="reservations-reservationid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="reservations-reservationid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="reservations-reservationid-properties"></a>

### AccessDenied
<a name="reservations-reservationid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="reservations-reservationid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ChannelClass
<a name="reservations-reservationid-model-channelclass"></a>

A standard channel has two encoding pipelines and a single pipeline channel only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### GatewayTimeoutException
<a name="reservations-reservationid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="reservations-reservationid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="reservations-reservationid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="reservations-reservationid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### OfferingDurationUnits
<a name="reservations-reservationid-model-offeringdurationunits"></a>

Units for duration, e.g. 'MONTHS'
+ `MONTHS`

### OfferingType
<a name="reservations-reservationid-model-offeringtype"></a>

Offering type, e.g. 'NO\_UPFRONT'
+ `NO_UPFRONT`

### Reservation
<a name="reservations-reservationid-model-reservation"></a>

Reserved resources available to use

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567' |
| count | integer | False | Number of reserved resources |
| currencyCode | string | False | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD' |
| duration | integer | False | Lease duration, e.g. '12' |
| durationUnits | [OfferingDurationUnits](#reservations-reservationid-model-offeringdurationunits) | False | Units for duration, e.g. 'MONTHS' |
| end | string | False | Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00' |
| fixedPrice | number | False | One-time charge for each reserved resource, e.g. '0.0' for a NO\_UPFRONT offering |
| name | string | False | User specified reservation name |
| offeringDescription | string | False | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offeringId | string | False | Unique offering ID, e.g. '87654321' |
| offeringType | [OfferingType](#reservations-reservationid-model-offeringtype) | False | Offering type, e.g. 'NO\_UPFRONT' |
| region | string | False | AWS Region, e.g. 'us-west-2' |
| reservationId | string | False | Unique reservation ID, e.g. '1234567' |
| resourceSpecification | [ReservationResourceSpecification](#reservations-reservationid-model-reservationresourcespecification) | False | Resource configuration details |
| start | string | False | Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00' |
| state | [ReservationState](#reservations-reservationid-model-reservationstate) | False | Current state of reservation, e.g. 'ACTIVE' |
| tags | [Tags](#reservations-reservationid-model-tags) | False | A collection of key-value pairs |
| usagePrice | number | False | Recurring usage charge for each reserved resource, e.g. '157.0' |

### ReservationCodec
<a name="reservations-reservationid-model-reservationcodec"></a>

Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
+ `MPEG2`
+ `AVC`
+ `HEVC`
+ `AUDIO`
+ `LINK`

### ReservationMaximumBitrate
<a name="reservations-reservationid-model-reservationmaximumbitrate"></a>

Maximum bitrate in megabits per second
+ `MAX_10_MBPS`
+ `MAX_20_MBPS`
+ `MAX_50_MBPS`

### ReservationMaximumFramerate
<a name="reservations-reservationid-model-reservationmaximumframerate"></a>

Maximum framerate in frames per second (Outputs only)
+ `MAX_30_FPS`
+ `MAX_60_FPS`

### ReservationResolution
<a name="reservations-reservationid-model-reservationresolution"></a>

Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines
+ `SD`
+ `HD`
+ `FHD`
+ `UHD`

### ReservationResourceSpecification
<a name="reservations-reservationid-model-reservationresourcespecification"></a>

Resource configuration (codec, resolution, bitrate, ...)

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelClass | [ChannelClass](#reservations-reservationid-model-channelclass) | False | Channel class, e.g. 'STANDARD' |
| codec | [ReservationCodec](#reservations-reservationid-model-reservationcodec) | False | Codec, e.g. 'AVC' |
| maximumBitrate | [ReservationMaximumBitrate](#reservations-reservationid-model-reservationmaximumbitrate) | False | Maximum bitrate, e.g. 'MAX\_20\_MBPS' |
| maximumFramerate | [ReservationMaximumFramerate](#reservations-reservationid-model-reservationmaximumframerate) | False | Maximum framerate, e.g. 'MAX\_30\_FPS' (Outputs only) |
| resolution | [ReservationResolution](#reservations-reservationid-model-reservationresolution) | False | Resolution, e.g. 'HD' |
| resourceType | [ReservationResourceType](#reservations-reservationid-model-reservationresourcetype) | False | Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL' |
| specialFeature | [ReservationSpecialFeature](#reservations-reservationid-model-reservationspecialfeature) | False | Special feature, e.g. 'AUDIO\_NORMALIZATION' (Channels only) |
| videoQuality | [ReservationVideoQuality](#reservations-reservationid-model-reservationvideoquality) | False | Video quality, e.g. 'STANDARD' (Outputs only) |

### ReservationResourceType
<a name="reservations-reservationid-model-reservationresourcetype"></a>

Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
+ `INPUT`
+ `OUTPUT`
+ `MULTIPLEX`
+ `CHANNEL`

### ReservationSpecialFeature
<a name="reservations-reservationid-model-reservationspecialfeature"></a>

Special features, 'ADVANCED\_AUDIO' 'AUDIO\_NORMALIZATION' 'MGHD' or 'MGUHD'
+ `ADVANCED_AUDIO`
+ `AUDIO_NORMALIZATION`
+ `MGHD`
+ `MGUHD`

### ReservationState
<a name="reservations-reservationid-model-reservationstate"></a>

Current reservation state
+ `ACTIVE`
+ `EXPIRED`
+ `CANCELED`
+ `DELETED`

### ReservationVideoQuality
<a name="reservations-reservationid-model-reservationvideoquality"></a>

Video quality, e.g. 'STANDARD' (Outputs only)
+ `STANDARD`
+ `ENHANCED`
+ `PREMIUM`

### ResourceConflict
<a name="reservations-reservationid-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="reservations-reservationid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="reservations-reservationid-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateReservation
<a name="reservations-reservationid-model-updatereservation"></a>

UpdateReservation request

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | Name of the reservation |

### UpdateReservationResultModel
<a name="reservations-reservationid-model-updatereservationresultmodel"></a>

UpdateReservation response

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| reservation | [Reservation](#reservations-reservationid-model-reservation) | False |  |

## See also
<a name="reservations-reservationid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteReservation
<a name="DeleteReservation-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteReservation)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteReservation)

### DescribeReservation
<a name="DescribeReservation-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DescribeReservation)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeReservation)

### UpdateReservation
<a name="UpdateReservation-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/UpdateReservation)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateReservation)
