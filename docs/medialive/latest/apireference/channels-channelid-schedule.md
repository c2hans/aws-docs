---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/channels-channelid-schedule.html
---

# Channels: schedule
<a name="channels-channelid-schedule"></a>

## URI
<a name="channels-channelid-schedule-url"></a>

`/prod/channels/{{channelId}}/schedule`

## HTTP methods
<a name="channels-channelid-schedule-http-methods"></a>

### DELETE
<a name="channels-channelid-scheduledelete"></a>

**Operation ID:** `DeleteSchedule`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{channelId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ScheduleDeleteResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### GET
<a name="channels-channelid-scheduleget"></a>

**Operation ID:** `DescribeSchedule`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{channelId}} | String | True |  |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ScheduleDescribeResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="channels-channelid-scheduleput"></a>

**Operation ID:** `BatchUpdateSchedule`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{channelId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchUpdateScheduleResult | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 422 | ChannelConfigurationValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="channels-channelid-schedule-schemas"></a>

### Request bodies
<a name="channels-channelid-schedule-request-examples"></a>

#### PUT schema
<a name="channels-channelid-schedule-request-body-put-example"></a>

```
{
  "creates": {
    "scheduleActions": [
      {
        "actionName": "string",
        "scheduleActionSettings": {
          "hlsId3SegmentTaggingSettings": {
            "tag": "string"
          },
          "hlsTimedMetadataSettings": {
            "id3": "string"
          },
          "inputPrepareSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "inputSwitchSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "motionGraphicsImageActivateSettings": {
            "duration": integer,
            "passwordParam": "string",
            "url": "string",
            "username": "string"
          },
          "motionGraphicsImageDeactivateSettings": {
          },
          "pauseStateSettings": {
            "pipelines": [
              {
                "pipelineId": enum
              }
            ]
          },
          "scte35ReturnToNetworkSettings": {
            "spliceEventId": integer
          },
          "scte35SpliceInsertSettings": {
            "duration": integer,
            "spliceEventId": integer
          },
          "scte35TimeSignalSettings": {
            "scte35Descriptors": [
              {
                "scte35DescriptorSettings": {
                  "segmentationDescriptorScte35DescriptorSettings": {
                    "deliveryRestrictions": {
                      "archiveAllowedFlag": enum,
                      "deviceRestrictions": enum,
                      "noRegionalBlackoutFlag": enum,
                      "webDeliveryAllowedFlag": enum
                    },
                    "segmentNum": integer,
                    "segmentationCancelIndicator": enum,
                    "segmentationDuration": integer,
                    "segmentationEventId": integer,
                    "segmentationTypeId": integer,
                    "segmentationUpid": "string",
                    "segmentationUpidType": integer,
                    "segmentsExpected": integer,
                    "subSegmentNum": integer,
                    "subSegmentsExpected": integer
                  }
                }
              }
            ]
          },
          "staticImageActivateSettings": {
            "duration": integer,
            "fadeIn": integer,
            "fadeOut": integer,
            "height": integer,
            "image": {
              "passwordParam": "string",
              "uri": "string",
              "username": "string"
            },
            "imageX": integer,
            "imageY": integer,
            "layer": integer,
            "opacity": integer,
            "width": integer
          },
          "staticImageDeactivateSettings": {
            "fadeOut": integer,
            "layer": integer
          }
        },
        "scheduleActionStartSettings": {
          "fixedModeScheduleActionStartSettings": {
            "time": "string"
          },
          "followModeScheduleActionStartSettings": {
            "followPoint": enum,
            "referenceActionName": "string"
          },
          "immediateModeScheduleActionStartSettings": {
            "time": "string"
          }
        }
      }
    ]
  },
  "deletes": {
    "actionNames": [
      "string"
    ]
  }
}
```

### Response bodies
<a name="channels-channelid-schedule-response-examples"></a>

#### ScheduleDeleteResultModel schema
<a name="channels-channelid-schedule-response-body-scheduledeleteresultmodel-example"></a>

```
{
}
```

#### ScheduleDescribeResultModel schema
<a name="channels-channelid-schedule-response-body-scheduledescriberesultmodel-example"></a>

```
{
  "nextToken": "string",
  "scheduleActions": [
    {
      "actionName": "string",
      "scheduleActionSettings": {
        "hlsId3SegmentTaggingSettings": {
          "tag": "string"
        },
        "hlsTimedMetadataSettings": {
          "id3": "string"
        },
        "inputPrepareSettings": {
          "inputAttachmentNameReference": "string",
          "inputClippingSettings": {
            "inputTimecodeSource": enum,
            "startTimecode": {
              "timecode": "string"
            },
            "stopTimecode": {
              "lastFrameClippingBehavior": enum,
              "timecode": "string"
            }
          },
          "urlPath": [
            "string"
          ]
        },
        "inputSwitchSettings": {
          "inputAttachmentNameReference": "string",
          "inputClippingSettings": {
            "inputTimecodeSource": enum,
            "startTimecode": {
              "timecode": "string"
            },
            "stopTimecode": {
              "lastFrameClippingBehavior": enum,
              "timecode": "string"
            }
          },
          "urlPath": [
            "string"
          ]
        },
        "motionGraphicsImageActivateSettings": {
          "duration": integer,
          "passwordParam": "string",
          "url": "string",
          "username": "string"
        },
        "motionGraphicsImageDeactivateSettings": {
        },
        "pauseStateSettings": {
          "pipelines": [
            {
              "pipelineId": enum
            }
          ]
        },
        "scte35ReturnToNetworkSettings": {
          "spliceEventId": integer
        },
        "scte35SpliceInsertSettings": {
          "duration": integer,
          "spliceEventId": integer
        },
        "scte35TimeSignalSettings": {
          "scte35Descriptors": [
            {
              "scte35DescriptorSettings": {
                "segmentationDescriptorScte35DescriptorSettings": {
                  "deliveryRestrictions": {
                    "archiveAllowedFlag": enum,
                    "deviceRestrictions": enum,
                    "noRegionalBlackoutFlag": enum,
                    "webDeliveryAllowedFlag": enum
                  },
                  "segmentNum": integer,
                  "segmentationCancelIndicator": enum,
                  "segmentationDuration": integer,
                  "segmentationEventId": integer,
                  "segmentationTypeId": integer,
                  "segmentationUpid": "string",
                  "segmentationUpidType": integer,
                  "segmentsExpected": integer,
                  "subSegmentNum": integer,
                  "subSegmentsExpected": integer
                }
              }
            }
          ]
        },
        "staticImageActivateSettings": {
          "duration": integer,
          "fadeIn": integer,
          "fadeOut": integer,
          "height": integer,
          "image": {
            "passwordParam": "string",
            "uri": "string",
            "username": "string"
          },
          "imageX": integer,
          "imageY": integer,
          "layer": integer,
          "opacity": integer,
          "width": integer
        },
        "staticImageDeactivateSettings": {
          "fadeOut": integer,
          "layer": integer
        }
      },
      "scheduleActionStartSettings": {
        "fixedModeScheduleActionStartSettings": {
          "time": "string"
        },
        "followModeScheduleActionStartSettings": {
          "followPoint": enum,
          "referenceActionName": "string"
        },
        "immediateModeScheduleActionStartSettings": {
          "time": "string"
        }
      }
    }
  ]
}
```

#### BatchUpdateScheduleResult schema
<a name="channels-channelid-schedule-response-body-batchupdatescheduleresult-example"></a>

```
{
  "creates": {
    "scheduleActions": [
      {
        "actionName": "string",
        "scheduleActionSettings": {
          "hlsId3SegmentTaggingSettings": {
            "tag": "string"
          },
          "hlsTimedMetadataSettings": {
            "id3": "string"
          },
          "inputPrepareSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "inputSwitchSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "motionGraphicsImageActivateSettings": {
            "duration": integer,
            "passwordParam": "string",
            "url": "string",
            "username": "string"
          },
          "motionGraphicsImageDeactivateSettings": {
          },
          "pauseStateSettings": {
            "pipelines": [
              {
                "pipelineId": enum
              }
            ]
          },
          "scte35ReturnToNetworkSettings": {
            "spliceEventId": integer
          },
          "scte35SpliceInsertSettings": {
            "duration": integer,
            "spliceEventId": integer
          },
          "scte35TimeSignalSettings": {
            "scte35Descriptors": [
              {
                "scte35DescriptorSettings": {
                  "segmentationDescriptorScte35DescriptorSettings": {
                    "deliveryRestrictions": {
                      "archiveAllowedFlag": enum,
                      "deviceRestrictions": enum,
                      "noRegionalBlackoutFlag": enum,
                      "webDeliveryAllowedFlag": enum
                    },
                    "segmentNum": integer,
                    "segmentationCancelIndicator": enum,
                    "segmentationDuration": integer,
                    "segmentationEventId": integer,
                    "segmentationTypeId": integer,
                    "segmentationUpid": "string",
                    "segmentationUpidType": integer,
                    "segmentsExpected": integer,
                    "subSegmentNum": integer,
                    "subSegmentsExpected": integer
                  }
                }
              }
            ]
          },
          "staticImageActivateSettings": {
            "duration": integer,
            "fadeIn": integer,
            "fadeOut": integer,
            "height": integer,
            "image": {
              "passwordParam": "string",
              "uri": "string",
              "username": "string"
            },
            "imageX": integer,
            "imageY": integer,
            "layer": integer,
            "opacity": integer,
            "width": integer
          },
          "staticImageDeactivateSettings": {
            "fadeOut": integer,
            "layer": integer
          }
        },
        "scheduleActionStartSettings": {
          "fixedModeScheduleActionStartSettings": {
            "time": "string"
          },
          "followModeScheduleActionStartSettings": {
            "followPoint": enum,
            "referenceActionName": "string"
          },
          "immediateModeScheduleActionStartSettings": {
            "time": "string"
          }
        }
      }
    ]
  },
  "deletes": {
    "scheduleActions": [
      {
        "actionName": "string",
        "scheduleActionSettings": {
          "hlsId3SegmentTaggingSettings": {
            "tag": "string"
          },
          "hlsTimedMetadataSettings": {
            "id3": "string"
          },
          "inputPrepareSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "inputSwitchSettings": {
            "inputAttachmentNameReference": "string",
            "inputClippingSettings": {
              "inputTimecodeSource": enum,
              "startTimecode": {
                "timecode": "string"
              },
              "stopTimecode": {
                "lastFrameClippingBehavior": enum,
                "timecode": "string"
              }
            },
            "urlPath": [
              "string"
            ]
          },
          "motionGraphicsImageActivateSettings": {
            "duration": integer,
            "passwordParam": "string",
            "url": "string",
            "username": "string"
          },
          "motionGraphicsImageDeactivateSettings": {
          },
          "pauseStateSettings": {
            "pipelines": [
              {
                "pipelineId": enum
              }
            ]
          },
          "scte35ReturnToNetworkSettings": {
            "spliceEventId": integer
          },
          "scte35SpliceInsertSettings": {
            "duration": integer,
            "spliceEventId": integer
          },
          "scte35TimeSignalSettings": {
            "scte35Descriptors": [
              {
                "scte35DescriptorSettings": {
                  "segmentationDescriptorScte35DescriptorSettings": {
                    "deliveryRestrictions": {
                      "archiveAllowedFlag": enum,
                      "deviceRestrictions": enum,
                      "noRegionalBlackoutFlag": enum,
                      "webDeliveryAllowedFlag": enum
                    },
                    "segmentNum": integer,
                    "segmentationCancelIndicator": enum,
                    "segmentationDuration": integer,
                    "segmentationEventId": integer,
                    "segmentationTypeId": integer,
                    "segmentationUpid": "string",
                    "segmentationUpidType": integer,
                    "segmentsExpected": integer,
                    "subSegmentNum": integer,
                    "subSegmentsExpected": integer
                  }
                }
              }
            ]
          },
          "staticImageActivateSettings": {
            "duration": integer,
            "fadeIn": integer,
            "fadeOut": integer,
            "height": integer,
            "image": {
              "passwordParam": "string",
              "uri": "string",
              "username": "string"
            },
            "imageX": integer,
            "imageY": integer,
            "layer": integer,
            "opacity": integer,
            "width": integer
          },
          "staticImageDeactivateSettings": {
            "fadeOut": integer,
            "layer": integer
          }
        },
        "scheduleActionStartSettings": {
          "fixedModeScheduleActionStartSettings": {
            "time": "string"
          },
          "followModeScheduleActionStartSettings": {
            "followPoint": enum,
            "referenceActionName": "string"
          },
          "immediateModeScheduleActionStartSettings": {
            "time": "string"
          }
        }
      }
    ]
  }
}
```

#### InvalidRequest schema
<a name="channels-channelid-schedule-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="channels-channelid-schedule-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="channels-channelid-schedule-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ChannelConfigurationValidationError schema
<a name="channels-channelid-schedule-response-body-channelconfigurationvalidationerror-example"></a>

```
{
  "message": "string",
  "validationErrors": [
    {
      "elementPath": "string",
      "errorMessage": "string"
    }
  ]
}
```

#### LimitExceeded schema
<a name="channels-channelid-schedule-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="channels-channelid-schedule-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="channels-channelid-schedule-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="channels-channelid-schedule-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="channels-channelid-schedule-properties"></a>

### AccessDenied
<a name="channels-channelid-schedule-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="channels-channelid-schedule-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BatchScheduleActionCreateRequest
<a name="channels-channelid-schedule-model-batchscheduleactioncreaterequest"></a>

A list of schedule actions to create (in a request) or that have been created (in a response).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scheduleActions | Array of type [ScheduleAction](#channels-channelid-schedule-model-scheduleaction) | True | A list of schedule actions to create. |

### BatchScheduleActionCreateResult
<a name="channels-channelid-schedule-model-batchscheduleactioncreateresult"></a>

List of actions that have been created in the schedule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scheduleActions | Array of type [ScheduleAction](#channels-channelid-schedule-model-scheduleaction) | True | List of actions that have been created in the schedule. |

### BatchScheduleActionDeleteRequest
<a name="channels-channelid-schedule-model-batchscheduleactiondeleterequest"></a>

A list of schedule actions to delete.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actionNames | Array of type string | True | A list of schedule actions to delete. |

### BatchScheduleActionDeleteResult
<a name="channels-channelid-schedule-model-batchscheduleactiondeleteresult"></a>

List of actions that have been deleted from the schedule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scheduleActions | Array of type [ScheduleAction](#channels-channelid-schedule-model-scheduleaction) | True | List of actions that have been deleted from the schedule. |

### BatchUpdateScheduleRequest
<a name="channels-channelid-schedule-model-batchupdateschedulerequest"></a>

A request to create actions (add actions to the schedule), delete actions (remove actions from the schedule), or both create and delete actions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creates | [BatchScheduleActionCreateRequest](#channels-channelid-schedule-model-batchscheduleactioncreaterequest) | False | Schedule actions to create in the schedule. |
| deletes | [BatchScheduleActionDeleteRequest](#channels-channelid-schedule-model-batchscheduleactiondeleterequest) | False | Schedule actions to delete from the schedule. |

### BatchUpdateScheduleResult
<a name="channels-channelid-schedule-model-batchupdatescheduleresult"></a>

Results of a batch schedule update.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creates | [BatchScheduleActionCreateResult](#channels-channelid-schedule-model-batchscheduleactioncreateresult) | False | Schedule actions created in the schedule. |
| deletes | [BatchScheduleActionDeleteResult](#channels-channelid-schedule-model-batchscheduleactiondeleteresult) | False | Schedule actions deleted from the schedule. |

### ChannelConfigurationValidationError
<a name="channels-channelid-schedule-model-channelconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |
| validationErrors | Array of type [ValidationError](#channels-channelid-schedule-model-validationerror) | False | A collection of validation error responses. |

### FixedModeScheduleActionStartSettings
<a name="channels-channelid-schedule-model-fixedmodescheduleactionstartsettings"></a>

Start time for the action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| time | string | True | Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants "T" for time and "Z" for "UTC format". |

### FollowModeScheduleActionStartSettings
<a name="channels-channelid-schedule-model-followmodescheduleactionstartsettings"></a>

Settings to specify if an action follows another.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| followPoint | [FollowPoint](#channels-channelid-schedule-model-followpoint) | True | Identifies whether this action starts relative to the start or relative to the end of the reference action. |
| referenceActionName | string | True | The action name of another action that this one refers to. |

### FollowPoint
<a name="channels-channelid-schedule-model-followpoint"></a>

Follow reference point.
+ `END`
+ `START`

### GatewayTimeoutException
<a name="channels-channelid-schedule-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### HlsId3SegmentTaggingScheduleActionSettings
<a name="channels-channelid-schedule-model-hlsid3segmenttaggingscheduleactionsettings"></a>

Settings for the action to insert a user-defined ID3 tag in each HLS segment

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tag | string | False | ID3 tag to insert into each segment. Supports special keyword identifiers to substitute in segment-related values.\\nSupported keyword identifiers: https://docs.aws.amazon.com/medialive/latest/ug/variable-data-identifiers.html |

### HlsTimedMetadataScheduleActionSettings
<a name="channels-channelid-schedule-model-hlstimedmetadatascheduleactionsettings"></a>

Settings for the action to emit HLS metadata

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id3 | string | True | Base64 string formatted according to the ID3 specification: http://id3.org/id3v2.4.0-structure |

### ImmediateModeScheduleActionStartSettings
<a name="channels-channelid-schedule-model-immediatemodescheduleactionstartsettings"></a>

Settings to configure an action so that it occurs as soon as possible.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| time | string | False | The time that the immediate mode action is scheduled to occur. (MediaLive calculates this time to be as soon as possible after receiving the schedule) |

### InputClippingSettings
<a name="channels-channelid-schedule-model-inputclippingsettings"></a>

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputTimecodeSource | [InputTimecodeSource](#channels-channelid-schedule-model-inputtimecodesource) | True | The source of the timecodes in the source being clipped. |
| startTimecode | [StartTimecode](#channels-channelid-schedule-model-starttimecode) | False | Settings to identify the start of the clip. |
| stopTimecode | [StopTimecode](#channels-channelid-schedule-model-stoptimecode) | False | Settings to identify the end of the clip. |

### InputLocation
<a name="channels-channelid-schedule-model-inputlocation"></a>

Input Location

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | key used to extract the password from EC2 Parameter store |
| uri | string | True | Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live". |
| username | string | False | Username if credentials are required to access a file or publishing point. This can be either a plaintext username, or a reference to an AWS parameter store name from which the username can be retrieved. AWS Parameter store format: "ssm://<parameter name>" |

### InputPrepareScheduleActionSettings
<a name="channels-channelid-schedule-model-inputpreparescheduleactionsettings"></a>

Action to prepare an input for a future immediate input switch.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputAttachmentNameReference | string | False | The name of the input attachment that should be prepared by this action. If no name is provided, the action will stop the most recent prepare (if any) when activated. |
| inputClippingSettings | [InputClippingSettings](#channels-channelid-schedule-model-inputclippingsettings) | False | Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file. |
| urlPath | Array of type string | False | The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source. |

### InputSwitchScheduleActionSettings
<a name="channels-channelid-schedule-model-inputswitchscheduleactionsettings"></a>

Settings for the "switch input" action: to switch from ingesting one input to ingesting another input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputAttachmentNameReference | string | True | The name of the input attachment (not the name of the input\!) to switch to. The name is specified in the channel configuration. |
| inputClippingSettings | [InputClippingSettings](#channels-channelid-schedule-model-inputclippingsettings) | False | Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file. |
| urlPath | Array of type string | False | The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source. |

### InputTimecodeSource
<a name="channels-channelid-schedule-model-inputtimecodesource"></a>

To clip the file, you must specify the timecode for the start and end of the clip. <br>Specify EMBEDDED to use the timecode embedded in the source content. The embedded timecode must exist in the source content, otherwise MediaLive will output black frames until it reaches the end of the source. <br>Specify ZEROBASED to use a timecode that assumes that the first frame in the file has the timestamp 00:00:00.00. <br> There is no default for this field, you must specify a value.
+ `ZEROBASED`
+ `EMBEDDED`

### InternalServiceError
<a name="channels-channelid-schedule-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="channels-channelid-schedule-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LastFrameClippingBehavior
<a name="channels-channelid-schedule-model-lastframeclippingbehavior"></a>

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.
+ `EXCLUDE_LAST_FRAME`
+ `INCLUDE_LAST_FRAME`

### LimitExceeded
<a name="channels-channelid-schedule-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### MotionGraphicsActivateScheduleActionSettings
<a name="channels-channelid-schedule-model-motiongraphicsactivatescheduleactionsettings"></a>

Settings to specify the rendering of motion graphics into the video stream.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| duration | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 86400000 | False | Duration (in milliseconds) that motion graphics should render on to the video stream. Leaving out this property or setting to 0 will result in rendering continuing until a deactivate action is processed. |
| passwordParam | string | False | Key used to extract the password from EC2 Parameter store |
| url | string | False | URI of the HTML5 content to be rendered into the live stream. |
| username | string | False | Username if credentials are required to access a file. This must be a reference to an AWS parameter store name from which the password can be retrieved. AWS Parameter store format: \\"ssm://<parameter name>\\" |

### MotionGraphicsDeactivateScheduleActionSettings
<a name="channels-channelid-schedule-model-motiongraphicsdeactivatescheduleactionsettings"></a>

Settings to specify the ending of rendering motion graphics into the video stream.

### PauseStateScheduleActionSettings
<a name="channels-channelid-schedule-model-pausestatescheduleactionsettings"></a>

Settings for the action to set pause state of a channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pipelines | Array of type [PipelinePauseStateSettings](#channels-channelid-schedule-model-pipelinepausestatesettings) | False |  |

### PipelineId
<a name="channels-channelid-schedule-model-pipelineid"></a>

Pipeline ID
+ `PIPELINE_0`
+ `PIPELINE_1`

### PipelinePauseStateSettings
<a name="channels-channelid-schedule-model-pipelinepausestatesettings"></a>

Settings for pausing a pipeline.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pipelineId | [PipelineId](#channels-channelid-schedule-model-pipelineid) | True | Pipeline ID to pause ("PIPELINE\_0" or "PIPELINE\_1"). |

### ResourceNotFound
<a name="channels-channelid-schedule-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ScheduleAction
<a name="channels-channelid-schedule-model-scheduleaction"></a>

Contains information on a single schedule action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actionName | string | True | The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused. |
| scheduleActionSettings | [ScheduleActionSettings](#channels-channelid-schedule-model-scheduleactionsettings) | True | Settings for this schedule action. |
| scheduleActionStartSettings | [ScheduleActionStartSettings](#channels-channelid-schedule-model-scheduleactionstartsettings) | True | The time for the action to start in the channel. |

### ScheduleActionSettings
<a name="channels-channelid-schedule-model-scheduleactionsettings"></a>

Holds the settings for a single schedule action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hlsId3SegmentTaggingSettings | [HlsId3SegmentTaggingScheduleActionSettings](#channels-channelid-schedule-model-hlsid3segmenttaggingscheduleactionsettings) | False | Action to insert HLS ID3 segment tagging |
| hlsTimedMetadataSettings | [HlsTimedMetadataScheduleActionSettings](#channels-channelid-schedule-model-hlstimedmetadatascheduleactionsettings) | False | Action to insert HLS metadata |
| inputPrepareSettings | [InputPrepareScheduleActionSettings](#channels-channelid-schedule-model-inputpreparescheduleactionsettings) | False | Action to prepare an input for a future immediate input switch |
| inputSwitchSettings | [InputSwitchScheduleActionSettings](#channels-channelid-schedule-model-inputswitchscheduleactionsettings) | False | Action to switch the input |
| motionGraphicsImageActivateSettings | [MotionGraphicsActivateScheduleActionSettings](#channels-channelid-schedule-model-motiongraphicsactivatescheduleactionsettings) | False | Action to activate a motion graphics image overlay |
| motionGraphicsImageDeactivateSettings | [MotionGraphicsDeactivateScheduleActionSettings](#channels-channelid-schedule-model-motiongraphicsdeactivatescheduleactionsettings) | False | Action to deactivate a motion graphics image overlay |
| pauseStateSettings | [PauseStateScheduleActionSettings](#channels-channelid-schedule-model-pausestatescheduleactionsettings) | False | Action to pause or unpause one or both channel pipelines |
| scte35ReturnToNetworkSettings | [Scte35ReturnToNetworkScheduleActionSettings](#channels-channelid-schedule-model-scte35returntonetworkscheduleactionsettings) | False | Action to insert SCTE-35 return\_to\_network message |
| scte35SpliceInsertSettings | [Scte35SpliceInsertScheduleActionSettings](#channels-channelid-schedule-model-scte35spliceinsertscheduleactionsettings) | False | Action to insert SCTE-35 splice\_insert message |
| scte35TimeSignalSettings | [Scte35TimeSignalScheduleActionSettings](#channels-channelid-schedule-model-scte35timesignalscheduleactionsettings) | False | Action to insert SCTE-35 time\_signal message |
| staticImageActivateSettings | [StaticImageActivateScheduleActionSettings](#channels-channelid-schedule-model-staticimageactivatescheduleactionsettings) | False | Action to activate a static image overlay |
| staticImageDeactivateSettings | [StaticImageDeactivateScheduleActionSettings](#channels-channelid-schedule-model-staticimagedeactivatescheduleactionsettings) | False | Action to deactivate a static image overlay |

### ScheduleActionStartSettings
<a name="channels-channelid-schedule-model-scheduleactionstartsettings"></a>

Settings to specify when an action should occur. Only one of the options must be selected.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fixedModeScheduleActionStartSettings | [FixedModeScheduleActionStartSettings](#channels-channelid-schedule-model-fixedmodescheduleactionstartsettings) | False | Option for specifying the start time for an action. |
| followModeScheduleActionStartSettings | [FollowModeScheduleActionStartSettings](#channels-channelid-schedule-model-followmodescheduleactionstartsettings) | False | Option for specifying an action as relative to another action. |
| immediateModeScheduleActionStartSettings | [ImmediateModeScheduleActionStartSettings](#channels-channelid-schedule-model-immediatemodescheduleactionstartsettings) | False | Option for specifying an action that should be applied immediately. |

### ScheduleDeleteResultModel
<a name="channels-channelid-schedule-model-scheduledeleteresultmodel"></a>

Result of a schedule deletion.

### ScheduleDescribeResultModel
<a name="channels-channelid-schedule-model-scheduledescriberesultmodel"></a>

Results of a schedule describe.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The next token; for use in pagination. |
| scheduleActions | Array of type [ScheduleAction](#channels-channelid-schedule-model-scheduleaction) | True | The list of actions in the schedule. |

### Scte35ArchiveAllowedFlag
<a name="channels-channelid-schedule-model-scte35archiveallowedflag"></a>

Corresponds to the archive\_allowed parameter. A value of ARCHIVE\_NOT\_ALLOWED corresponds to 0 (false) in the SCTE-35 specification. If you include one of the "restriction" flags then you must include all four of them.
+ `ARCHIVE_NOT_ALLOWED`
+ `ARCHIVE_ALLOWED`

### Scte35DeliveryRestrictions
<a name="channels-channelid-schedule-model-scte35deliveryrestrictions"></a>

Corresponds to SCTE-35 delivery\_not\_restricted\_flag parameter. To declare delivery restrictions, include this element and its four "restriction" flags. To declare that there are no restrictions, omit this element.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| archiveAllowedFlag | [Scte35ArchiveAllowedFlag](#channels-channelid-schedule-model-scte35archiveallowedflag) | True | Corresponds to SCTE-35 archive\_allowed\_flag. |
| deviceRestrictions | [Scte35DeviceRestrictions](#channels-channelid-schedule-model-scte35devicerestrictions) | True | Corresponds to SCTE-35 device\_restrictions parameter. |
| noRegionalBlackoutFlag | [Scte35NoRegionalBlackoutFlag](#channels-channelid-schedule-model-scte35noregionalblackoutflag) | True | Corresponds to SCTE-35 no\_regional\_blackout\_flag parameter. |
| webDeliveryAllowedFlag | [Scte35WebDeliveryAllowedFlag](#channels-channelid-schedule-model-scte35webdeliveryallowedflag) | True | Corresponds to SCTE-35 web\_delivery\_allowed\_flag parameter. |

### Scte35Descriptor
<a name="channels-channelid-schedule-model-scte35descriptor"></a>

Holds one set of SCTE-35 Descriptor Settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scte35DescriptorSettings | [Scte35DescriptorSettings](#channels-channelid-schedule-model-scte35descriptorsettings) | True | SCTE-35 Descriptor Settings. |

### Scte35DescriptorSettings
<a name="channels-channelid-schedule-model-scte35descriptorsettings"></a>

SCTE-35 Descriptor settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| segmentationDescriptorScte35DescriptorSettings | [Scte35SegmentationDescriptor](#channels-channelid-schedule-model-scte35segmentationdescriptor) | True | SCTE-35 Segmentation Descriptor. |

### Scte35DeviceRestrictions
<a name="channels-channelid-schedule-model-scte35devicerestrictions"></a>

Corresponds to the device\_restrictions parameter in a segmentation\_descriptor. If you include one of the "restriction" flags then you must include all four of them.
+ `NONE`
+ `RESTRICT_GROUP0`
+ `RESTRICT_GROUP1`
+ `RESTRICT_GROUP2`

### Scte35NoRegionalBlackoutFlag
<a name="channels-channelid-schedule-model-scte35noregionalblackoutflag"></a>

Corresponds to the no\_regional\_blackout\_flag parameter. A value of REGIONAL\_BLACKOUT corresponds to 0 (false) in the SCTE-35 specification. If you include one of the "restriction" flags then you must include all four of them.
+ `REGIONAL_BLACKOUT`
+ `NO_REGIONAL_BLACKOUT`

### Scte35ReturnToNetworkScheduleActionSettings
<a name="channels-channelid-schedule-model-scte35returntonetworkscheduleactionsettings"></a>

Settings for a SCTE-35 return\_to\_network message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| spliceEventId | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 4294967295 | True | The splice\_event\_id for the SCTE-35 splice\_insert, as defined in SCTE-35. |

### Scte35SegmentationCancelIndicator
<a name="channels-channelid-schedule-model-scte35segmentationcancelindicator"></a>

Corresponds to SCTE-35 segmentation\_event\_cancel\_indicator. SEGMENTATION\_EVENT\_NOT\_CANCELED corresponds to 0 in the SCTE-35 specification and indicates that this is an insertion request. SEGMENTATION\_EVENT\_CANCELED corresponds to 1 in the SCTE-35 specification and indicates that this is a cancelation request, in which case complete this field and the existing event ID to cancel.
+ `SEGMENTATION_EVENT_NOT_CANCELED`
+ `SEGMENTATION_EVENT_CANCELED`

### Scte35SegmentationDescriptor
<a name="channels-channelid-schedule-model-scte35segmentationdescriptor"></a>

Corresponds to SCTE-35 segmentation\_descriptor.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryRestrictions | [Scte35DeliveryRestrictions](#channels-channelid-schedule-model-scte35deliveryrestrictions) | False | Holds the four SCTE-35 delivery restriction parameters. |
| segmentationCancelIndicator | [Scte35SegmentationCancelIndicator](#channels-channelid-schedule-model-scte35segmentationcancelindicator) | True | Corresponds to SCTE-35 segmentation\_event\_cancel\_indicator. |
| segmentationDuration | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 1099511627775 | False | Corresponds to SCTE-35 segmentation\_duration. Optional. The duration for the time\_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time\_signal will continue until you insert a cancellation message. |
| segmentationEventId | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 4294967295 | True | Corresponds to SCTE-35 segmentation\_event\_id.  |
| segmentationTypeId | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 segmentation\_type\_id. One of the segmentation\_type\_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, "52"). In the CLI, API, or an SDK, enter the ID in hex (for example, "0x34") or decimal (for example, "52"). |
| segmentationUpid | string | False | Corresponds to SCTE-35 segmentation\_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation\_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII "ADS Information" becomes hex "41445320496e666f726d6174696f6e. |
| segmentationUpidType | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 segmentation\_upid\_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, "0x0C" hex from the specification is "12" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, "0x0C" ) or in decimal (for example, "12"). |
| segmentNum | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 segment\_num. A value that is valid for the specified segmentation\_type\_id. |
| segmentsExpected | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 segments\_expected. A value that is valid for the specified segmentation\_type\_id. |
| subSegmentNum | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 sub\_segment\_num. A value that is valid for the specified segmentation\_type\_id. |
| subSegmentsExpected | integer<br />Minimum: 0<br />Maximum: 255 | False | Corresponds to SCTE-35 sub\_segments\_expected. A value that is valid for the specified segmentation\_type\_id. |

### Scte35SpliceInsertScheduleActionSettings
<a name="channels-channelid-schedule-model-scte35spliceinsertscheduleactionsettings"></a>

Settings for a SCTE-35 splice\_insert message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| duration | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 8589934591 | False | Optional, the duration for the splice\_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice\_insert will continue indefinitely and there is an expectation that you will enter a return\_to\_network to end the splice\_insert at the appropriate time. |
| spliceEventId | integer<br />Format: int64<br />Minimum: 0<br />Maximum: 4294967295 | True | The splice\_event\_id for the SCTE-35 splice\_insert, as defined in SCTE-35. |

### Scte35TimeSignalScheduleActionSettings
<a name="channels-channelid-schedule-model-scte35timesignalscheduleactionsettings"></a>

Settings for a SCTE-35 time\_signal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| scte35Descriptors | Array of type [Scte35Descriptor](#channels-channelid-schedule-model-scte35descriptor) | True | The list of SCTE-35 descriptors accompanying the SCTE-35 time\_signal. |

### Scte35WebDeliveryAllowedFlag
<a name="channels-channelid-schedule-model-scte35webdeliveryallowedflag"></a>

Corresponds to the web\_delivery\_allowed\_flag parameter. A value of WEB\_DELIVERY\_NOT\_ALLOWED corresponds to 0 (false) in the SCTE-35 specification. If you include one of the "restriction" flags then you must include all four of them.
+ `WEB_DELIVERY_NOT_ALLOWED`
+ `WEB_DELIVERY_ALLOWED`

### StartTimecode
<a name="channels-channelid-schedule-model-starttimecode"></a>

Settings to identify the start of the clip.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| timecode | string | False | The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF. |

### StaticImageActivateScheduleActionSettings
<a name="channels-channelid-schedule-model-staticimageactivatescheduleactionsettings"></a>

Settings for the action to activate a static image.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| duration | integer<br />Minimum: 0 | False | The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated. |
| fadeIn | integer<br />Minimum: 0 | False | The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in). |
| fadeOut | integer<br />Minimum: 0 | False | Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out). |
| height | integer<br />Minimum: 1 | False | The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay. |
| image | [InputLocation](#channels-channelid-schedule-model-inputlocation) | True | The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video. |
| imageX | integer<br />Minimum: 0 | False | Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right. |
| imageY | integer<br />Minimum: 0 | False | Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom. |
| layer | integer<br />Minimum: 0<br />Maximum: 7 | False | The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0. |
| opacity | integer<br />Minimum: 0<br />Maximum: 100 | False | Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100. |
| width | integer<br />Minimum: 1 | False | The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay. |

### StaticImageDeactivateScheduleActionSettings
<a name="channels-channelid-schedule-model-staticimagedeactivatescheduleactionsettings"></a>

Settings for the action to deactivate the image in a specific layer.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fadeOut | integer<br />Minimum: 0 | False | The time in milliseconds for the image to fade out. Default is 0 (no fade-out). |
| layer | integer<br />Minimum: 0<br />Maximum: 7 | False | The image overlay layer to deactivate, 0 to 7. Default is 0. |

### StopTimecode
<a name="channels-channelid-schedule-model-stoptimecode"></a>

Settings to identify the end of the clip.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lastFrameClippingBehavior | [LastFrameClippingBehavior](#channels-channelid-schedule-model-lastframeclippingbehavior) | False | If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode. |
| timecode | string | False | The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF. |

### ValidationError
<a name="channels-channelid-schedule-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="channels-channelid-schedule-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteSchedule
<a name="DeleteSchedule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteSchedule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteSchedule)

### DescribeSchedule
<a name="DescribeSchedule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DescribeSchedule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeSchedule)

### BatchUpdateSchedule
<a name="BatchUpdateSchedule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/BatchUpdateSchedule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/BatchUpdateSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
