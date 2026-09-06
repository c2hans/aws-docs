---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-versions.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Segment Versions
<a name="apps-application-id-segments-segment-id-versions"></a>

A *segment* designates which users receive messages from a campaign or journey. The Segment Versions resource provides information about versions of a specific segment, such as the dimension settings and criteria values that were used by each version of the segment.

You can use this resource to retrieve information about versions of a segment.

## URI
<a name="apps-application-id-segments-segment-id-versions-url"></a>

`/v1/apps/{{application-id}}/segments/{{segment-id}}/versions`

## HTTP methods
<a name="apps-application-id-segments-segment-id-versions-http-methods"></a>

### GET
<a name="apps-application-id-segments-segment-id-versionsget"></a>

**Operation ID:** `GetSegmentVersions`

Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that's associated with an application.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{segment-id}} | String | True | The unique identifier for the segment. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| token | String | False | The `NextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | SegmentsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-segments-segment-id-versionsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Segment Versions resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{segment-id}} | String | True | The unique identifier for the segment. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-segments-segment-id-versions-schemas"></a>

### Response bodies
<a name="apps-application-id-segments-segment-id-versions-response-examples"></a>

#### SegmentsResponse schema
<a name="apps-application-id-segments-segment-id-versions-response-body-segmentsresponse-example"></a>

```
{
  "Item": [
    {
      "Name": "string",
      "Dimensions": {
        "Demographic": {
          "Channel": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "Platform": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "DeviceType": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "AppVersion": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "Make": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "Model": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          }
        },
        "Location": {
          "Country": {
            "DimensionType": enum,
            "Values": [
              "string"
            ]
          },
          "GPSPoint": {
            "Coordinates": {
              "Latitude": number,
              "Longitude": number
            },
            "RangeInKilometers": number
          }
        },
        "Behavior": {
          "Recency": {
            "RecencyType": enum,
            "Duration": enum
          }
        },
        "Attributes": {
        },
        "Metrics": {
        },
        "UserAttributes": {
        }
      },
      "SegmentGroups": {
        "Include": enum,
        "Groups": [
          {
            "Type": enum,
            "Dimensions": [
              {
                "Demographic": {
                  "Channel": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "Platform": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "DeviceType": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "AppVersion": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "Make": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "Model": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  }
                },
                "Location": {
                  "Country": {
                    "DimensionType": enum,
                    "Values": [
                      "string"
                    ]
                  },
                  "GPSPoint": {
                    "Coordinates": {
                      "Latitude": number,
                      "Longitude": number
                    },
                    "RangeInKilometers": number
                  }
                },
                "Behavior": {
                  "Recency": {
                    "RecencyType": enum,
                    "Duration": enum
                  }
                },
                "Attributes": {
                },
                "Metrics": {
                },
                "UserAttributes": {
                }
              }
            ],
            "SourceType": enum,
            "SourceSegments": [
              {
                "Id": "string",
                "Version": integer
              }
            ]
          }
        ]
      },
      "Id": "string",
      "ApplicationId": "string",
      "CreationDate": "string",
      "LastModifiedDate": "string",
      "Version": integer,
      "SegmentType": enum,
      "ImportDefinition": {
        "Size": integer,
        "S3Url": "string",
        "RoleArn": "string",
        "ExternalId": "string",
        "Format": enum,
        "ChannelCounts": {
        }
      },
      "Arn": "string",
      "tags": {
      }
    }
  ],
  "NextToken": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-segments-segment-id-versions-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-segments-segment-id-versions-properties"></a>

### AttributeDimension
<a name="apps-application-id-segments-segment-id-versions-model-attributedimension"></a>

Specifies attribute-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AttributeType | string<br />Values: `INCLUSIVE \| EXCLUSIVE \| CONTAINS \| BEFORE \| AFTER \| BETWEEN \| NOT_BETWEEN \| ON` | False | The type of segment dimension to use. Valid values are:+   `INCLUSIVE` – endpoints that have attributes matching the values are included in the segment. <br />+   `EXCLUSIVE` – endpoints that have attributes matching the values are excluded from the segment. <br />+   `CONTAINS` – endpoints that have attributes' substrings match the values are included in the segment. <br />+   `BEFORE` – endpoints with attributes read as ISO\_INSTANT datetimes before the value are included in the segment. <br />+   `AFTER` – endpoints with attributes read as ISO\_INSTANT datetimes after the value are included in the segment. <br />+   `BETWEEN` – endpoints with attributes read as ISO\_INSTANT datetimes between the values are included in the segment. <br />+   `ON` – endpoints with attributes read as ISO\_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.  |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `AttributeType` property, endpoints are included or excluded from the segment if their attribute values match the criteria values. |

### GPSCoordinates
<a name="apps-application-id-segments-segment-id-versions-model-gpscoordinates"></a>

Specifies the GPS coordinates of a location.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Latitude | number | True | The latitude coordinate of the location. |
| Longitude | number | True | The longitude coordinate of the location. |

### GPSPointDimension
<a name="apps-application-id-segments-segment-id-versions-model-gpspointdimension"></a>

Specifies GPS-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Coordinates | [GPSCoordinates](#apps-application-id-segments-segment-id-versions-model-gpscoordinates) | True | The GPS coordinates to measure distance from. |
| RangeInKilometers | number | False | The range, in kilometers, from the GPS coordinates. |

### MessageBody
<a name="apps-application-id-segments-segment-id-versions-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MetricDimension
<a name="apps-application-id-segments-segment-id-versions-model-metricdimension"></a>

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ComparisonOperator | string | True | The operator to use when comparing metric values. Valid values are: `GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN_OR_EQUAL`, and `EQUAL`. |
| Value | number | True | The value to compare. |

### RecencyDimension
<a name="apps-application-id-segments-segment-id-versions-model-recencydimension"></a>

Specifies criteria for including or excluding endpoints from a segment based on how recently an endpoint was active.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Duration | string<br />Values: `HR_24 \| DAY_7 \| DAY_14 \| DAY_30` | True | The duration to use when determining whether an endpoint is active or inactive. |
| RecencyType | string<br />Values: `ACTIVE \| INACTIVE` | True | The type of recency dimension to use for the segment. Valid values are: `ACTIVE`, endpoints that were active within the specified duration are included in the segment; and, `INACTIVE`, endpoints that weren't active within the specified duration are included in the segment. |

### SegmentBehaviors
<a name="apps-application-id-segments-segment-id-versions-model-segmentbehaviors"></a>

Specifies dimension settings for including or excluding endpoints from a segment based on how recently an endpoint was active.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Recency | [RecencyDimension](#apps-application-id-segments-segment-id-versions-model-recencydimension) | False | The dimension settings that are based on how recently an endpoint was active. |

### SegmentDemographics
<a name="apps-application-id-segments-segment-id-versions-model-segmentdemographics"></a>

Specifies demographic-based dimension settings for including or excluding endpoints from a segment. These settings derive from characteristics of endpoint devices, such as platform, make, and model.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AppVersion | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The app version criteria for the segment. |
| Channel | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The channel criteria for the segment. |
| DeviceType | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The device type criteria for the segment. |
| Make | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The device make criteria for the segment. |
| Model | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The device model criteria for the segment. |
| Platform | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The device platform criteria for the segment. |

### SegmentDimensions
<a name="apps-application-id-segments-segment-id-versions-model-segmentdimensions"></a>

Specifies the dimension settings for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | One or more custom attributes to use as criteria for the segment. For more information see [AttributeDimension](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#apps-application-id-segments-model-attributedimension) |
| Behavior | [SegmentBehaviors](#apps-application-id-segments-segment-id-versions-model-segmentbehaviors) | False | The behavior-based criteria, such as how recently users have used your app, for the segment. |
| Demographic | [SegmentDemographics](#apps-application-id-segments-segment-id-versions-model-segmentdemographics) | False | The demographic-based criteria, such as device platform, for the segment. |
| Location | [SegmentLocation](#apps-application-id-segments-segment-id-versions-model-segmentlocation) | False | The location-based criteria, such as region or GPS coordinates, for the segment. |
| Metrics | object | False | One or more custom metrics to use as criteria for the segment. |
| UserAttributes | object | False | One or more custom user attributes to use as criteria for the segment. |

### SegmentGroup
<a name="apps-application-id-segments-segment-id-versions-model-segmentgroup"></a>

Specifies the base segments and dimensions for a segment, and the relationships between these base segments and dimensions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Dimensions | Array of type [SegmentDimensions](#apps-application-id-segments-segment-id-versions-model-segmentdimensions) | False | An array that defines the dimensions for the segment. |
| SourceSegments | Array of type [SegmentReference](#apps-application-id-segments-segment-id-versions-model-segmentreference) | False | The base segment to build the segment on. A base segment, also referred to as a *source segment*, defines the initial population of endpoints for a segment. When you add dimensions to a segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.<br />You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the Amazon Pinpoint console displays a segment size estimate that indicates the size of the imported segment without any filters applied to it. |
| SourceType | string<br />Values: `ALL \| ANY \| NONE` | False | Specifies how to handle multiple base segments for the segment. For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments. |
| Type | string<br />Values: `ALL \| ANY \| NONE` | False | Specifies how to handle multiple dimensions for the segment. For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions. |

### SegmentGroupList
<a name="apps-application-id-segments-segment-id-versions-model-segmentgrouplist"></a>

Specifies the settings that define the relationships between segment groups for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Groups | Array of type [SegmentGroup](#apps-application-id-segments-segment-id-versions-model-segmentgroup) | False | An array that defines the set of segment criteria to evaluate when handling segment groups for the segment. |
| Include | string<br />Values: `ALL \| ANY \| NONE` | False | Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups. |

### SegmentImportResource
<a name="apps-application-id-segments-segment-id-versions-model-segmentimportresource"></a>

Provides information about the import job that created a segment. An import job is a job that creates a user segment by importing endpoint definitions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ChannelCounts | object | False | The number of channel types in the endpoint definitions that were imported to create the segment. |
| ExternalId | string | True | (Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint. |
| Format | string<br />Values: `CSV \| JSON` | True | The format of the files that were imported to create the segment. Valid values are: `CSV`, for comma-separated values format; and, `JSON`, for newline-delimited JSON format. |
| RoleArn | string | True | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorized Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from. |
| S3Url | string | True | The URL of the Amazon Simple Storage Service (Amazon S3) bucket that the endpoint definitions were imported from to create the segment. |
| Size | integer | True | The number of endpoint definitions that were imported successfully to create the segment. |

### SegmentLocation
<a name="apps-application-id-segments-segment-id-versions-model-segmentlocation"></a>

Specifies geographical dimension settings for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Country | [SetDimension](#apps-application-id-segments-segment-id-versions-model-setdimension) | False | The country or region code, in ISO 3166-1 alpha-2 format, for the segment. |
| GPSPoint | [GPSPointDimension](#apps-application-id-segments-segment-id-versions-model-gpspointdimension) | False | The GPS location and range for the segment. |

### SegmentReference
<a name="apps-application-id-segments-segment-id-versions-model-segmentreference"></a>

Specifies the segment identifier and version of a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Id | string | True | The unique identifier for the segment. |
| Version | integer | False | The version number of the segment. |

### SegmentResponse
<a name="apps-application-id-segments-segment-id-versions-model-segmentresponse"></a>

Provides information about the configuration, dimension, and other settings for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that the segment is associated with. |
| Arn | string | True | The Amazon Resource Name (ARN) of the segment. |
| CreationDate | string | True | The date and time when the segment was created. |
| Dimensions | [SegmentDimensions](#apps-application-id-segments-segment-id-versions-model-segmentdimensions) | False | The dimension settings for the segment. |
| Id | string | True | The unique identifier for the segment. |
| ImportDefinition | [SegmentImportResource](#apps-application-id-segments-segment-id-versions-model-segmentimportresource) | False | The settings for the import job that's associated with the segment. |
| LastModifiedDate | string | False | The date and time when the segment was last modified. |
| Name | string | False | The name of the segment. |
| SegmentGroups | [SegmentGroupList](#apps-application-id-segments-segment-id-versions-model-segmentgrouplist) | False | A list of one or more segment groups that apply to the segment. Each segment group consists of zero or more base segments and the dimensions that are applied to those base segments. |
| SegmentType | string<br />Values: `DIMENSIONAL \| IMPORT` | True | The segment type. Valid values are:+   `DIMENSIONAL` – A dynamic segment, which is a segment that uses selection criteria that you specify and is based on endpoint data that's reported by your app. Dynamic segments can change over time. <br />+   `IMPORT` – A static segment, which is a segment that uses selection criteria that you specify and is based on endpoint definitions that you import from a file. Imported segments are static; they don't change over time.  |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the segment. Each tag consists of a required tag key and an associated tag value. |
| Version | integer | False | The version number of the segment. |

### SegmentsResponse
<a name="apps-application-id-segments-segment-id-versions-model-segmentsresponse"></a>

Provides information about all the segments that are associated with an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [SegmentResponse](#apps-application-id-segments-segment-id-versions-model-segmentresponse) | True | An array of responses, one for each segment that's associated with the application (Segments resource) or each version of a segment that's associated with the application (Segment Versions resource). |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### SetDimension
<a name="apps-application-id-segments-segment-id-versions-model-setdimension"></a>

Specifies the dimension type and values for a segment dimension.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DimensionType | string<br />Values: `INCLUSIVE \| EXCLUSIVE` | False | The type of segment dimension to use. Valid values are: `INCLUSIVE`, endpoints that match the criteria are included in the segment; and, `EXCLUSIVE`, endpoints that match the criteria are excluded from the segment. |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `DimensionType` property, endpoints are included or excluded from the segment if their values match the criteria values. |

## See also
<a name="apps-application-id-segments-segment-id-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSegmentVersions
<a name="GetSegmentVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetSegmentVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetSegmentVersions)
