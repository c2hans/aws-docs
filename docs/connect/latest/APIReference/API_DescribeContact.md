---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html
---

# DescribeContact
<a name="API_DescribeContact"></a>

This API is in preview release for Connect Customer and is subject to change.

Describes the specified contact.

 **Use cases**

Following are common uses cases for this API:
+ Retrieve contact information such as the caller's phone number and the specific number the caller dialed to integrate into custom monitoring or custom agent experience solutions.
+ Detect when a customer chat session disconnects due to a network issue on the agent's end. Use the DisconnectReason field in the [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) to detect this event and then re-queue the chat for followup.
+ Identify after contact work (ACW) duration and call recordings information when a COMPLETED event is received by using the [contact event stream](https://docs.aws.amazon.com/connect/latest/adminguide/contact-events.html).

 **Important things to know**
+  `SystemEndpoint` is not populated for contacts with initiation method of MONITOR, QUEUE\_TRANSFER, or CALLBACK
+ Contact information remains available in Connect Customer for 24 months from the `InitiationTimestamp`, and then it is deleted. Only contact information that is available in Connect Customer is returned by this API.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_DescribeContact_RequestSyntax"></a>

```
GET /contacts/{{InstanceId}}/{{ContactId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_DescribeContact_RequestSyntax) **   <a name="connect-DescribeContact-request-uri-ContactId"></a>
The identifier of the contact.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DescribeContact_RequestSyntax) **   <a name="connect-DescribeContact-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeContact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Contact": {
      "AdditionalEmailRecipients": {
         "CcList": [
            {
               "Address": "string",
               "DisplayName": "string"
            }
         ],
         "ToList": [
            {
               "Address": "string",
               "DisplayName": "string"
            }
         ]
      },
      "AgentInfo": {
         "AcceptedByAgentTimestamp": number,
         "AfterContactWorkDuration": number,
         "AfterContactWorkEndTimestamp": number,
         "AfterContactWorkStartTimestamp": number,
         "AgentInitiatedHoldDuration": number,
         "AgentPauseDurationInSeconds": number,
         "Capabilities": {
            "ScreenShare": "string",
            "Video": "string"
         },
         "ConnectedToAgentTimestamp": number,
         "DeviceInfo": {
            "OperatingSystem": "string",
            "PlatformName": "string",
            "PlatformVersion": "string"
         },
         "HierarchyGroups": {
            "Level1": {
               "Arn": "string"
            },
            "Level2": {
               "Arn": "string"
            },
            "Level3": {
               "Arn": "string"
            },
            "Level4": {
               "Arn": "string"
            },
            "Level5": {
               "Arn": "string"
            }
         },
         "Id": "string",
         "PreviewEndTimestamp": number,
         "StateTransitions": [
            {
               "State": "string",
               "StateEndTimestamp": number,
               "StateStartTimestamp": number
            }
         ],
         "VoiceEnhancementMode": "string"
      },
      "AnsweringMachineDetectionStatus": "string",
      "Arn": "string",
      "Attributes": {
         "string" : "string"
      },
      "Campaign": {
         "CampaignId": "string"
      },
      "Channel": "string",
      "ChatMetrics": {
         "AgentMetrics": {
            "ConversationAbandon": boolean,
            "LastMessageTimestamp": number,
            "MaxResponseTimeInMillis": number,
            "MessageLengthInChars": number,
            "MessagesSent": number,
            "NumResponses": number,
            "ParticipantId": "string",
            "ParticipantType": "string",
            "TotalResponseTimeInMillis": number
         },
         "ChatContactMetrics": {
            "AgentFirstResponseTimeInMillis": number,
            "AgentFirstResponseTimestamp": number,
            "ConversationCloseTimeInMillis": number,
            "ConversationTurnCount": number,
            "MultiParty": boolean,
            "TotalBotMessageLengthInChars": number,
            "TotalBotMessages": number,
            "TotalMessages": number
         },
         "CustomerMetrics": {
            "ConversationAbandon": boolean,
            "LastMessageTimestamp": number,
            "MaxResponseTimeInMillis": number,
            "MessageLengthInChars": number,
            "MessagesSent": number,
            "NumResponses": number,
            "ParticipantId": "string",
            "ParticipantType": "string",
            "TotalResponseTimeInMillis": number
         }
      },
      "ConnectedToSystemTimestamp": number,
      "ContactAssociationId": "string",
      "ContactDetails": {
         "Description": "string",
         "Name": "string"
      },
      "ContactEvaluations": {
         "string" : {
            "DeleteTimestamp": number,
            "EndTimestamp": number,
            "EvaluationArn": "string",
            "ExportLocation": "string",
            "FormId": "string",
            "StartTimestamp": number,
            "Status": "string"
         }
      },
      "Customer": {
         "Capabilities": {
            "ScreenShare": "string",
            "Video": "string"
         },
         "DeviceInfo": {
            "OperatingSystem": "string",
            "PlatformName": "string",
            "PlatformVersion": "string"
         }
      },
      "CustomerEndpoint": {
         "Address": "string",
         "DisplayName": "string",
         "Type": "string"
      },
      "CustomerId": "string",
      "CustomerVoiceActivity": {
         "GreetingEndTimestamp": number,
         "GreetingStartTimestamp": number
      },
      "Description": "string",
      "DisconnectDetails": {
         "PotentialDisconnectIssue": "string"
      },
      "DisconnectReason": "string",
      "DisconnectTimestamp": number,
      "GlobalResiliencyMetadata": {
         "ActiveRegion": "string",
         "OriginRegion": "string",
         "TrafficDistributionGroupId": "string"
      },
      "Id": "string",
      "InitialContactId": "string",
      "InitiationMethod": "string",
      "InitiationTimestamp": number,
      "LastPausedTimestamp": number,
      "LastResumedTimestamp": number,
      "LastUpdateTimestamp": number,
      "Name": "string",
      "NextContacts": [
         {
            "NextContactMetadata": { ... },
            "Type": "string"
         }
      ],
      "OutboundStrategy": {
         "Config": {
            "AgentFirst": {
               "Preview": {
                  "AllowedUserActions": [ "string" ],
                  "PostAcceptTimeoutConfig": {
                     "DurationInSeconds": number
                  }
               }
            }
         },
         "Type": "string"
      },
      "PreviousContactId": "string",
      "QualityMetrics": {
         "Agent": {
            "Audio": {
               "PotentialQualityIssues": [ "string" ],
               "QualityScore": number
            }
         },
         "Customer": {
            "Audio": {
               "PotentialQualityIssues": [ "string" ],
               "QualityScore": number
            }
         }
      },
      "QueueInfo": {
         "EnqueueTimestamp": number,
         "Id": "string"
      },
      "QueuePriority": number,
      "QueueTimeAdjustmentSeconds": number,
      "Recordings": [
         {
            "DeletionReason": "string",
            "FragmentStartNumber": "string",
            "FragmentStopNumber": "string",
            "Location": "string",
            "MediaStreamType": "string",
            "ParticipantType": "string",
            "StartTimestamp": number,
            "Status": "string",
            "StopTimestamp": number,
            "StorageType": "string",
            "UnprocessedTranscriptLocation": "string"
         }
      ],
      "RelatedContactId": "string",
      "RingStartTimestamp": number,
      "RoutingCriteria": {
         "ActivationTimestamp": number,
         "Index": number,
         "Steps": [
            {
               "Expiry": {
                  "DurationInSeconds": number,
                  "ExpiryTimestamp": number
               },
               "Expression": {
                  "AndExpression": [
                     "Expression"
                  ],
                  "AttributeCondition": {
                     "ComparisonOperator": "string",
                     "MatchCriteria": {
                        "AgentsCriteria": {
                           "AgentIds": [ "string" ]
                        }
                     },
                     "Name": "string",
                     "ProficiencyLevel": number,
                     "Range": {
                        "MaxProficiencyLevel": number,
                        "MinProficiencyLevel": number
                     },
                     "Value": "string"
                  },
                  "NotAttributeCondition": {
                     "ComparisonOperator": "string",
                     "MatchCriteria": {
                        "AgentsCriteria": {
                           "AgentIds": [ "string" ]
                        }
                     },
                     "Name": "string",
                     "ProficiencyLevel": number,
                     "Range": {
                        "MaxProficiencyLevel": number,
                        "MinProficiencyLevel": number
                     },
                     "Value": "string"
                  },
                  "OrExpression": [
                     "Expression"
                  ]
               },
               "Status": "string"
            }
         ]
      },
      "ScheduledTimestamp": number,
      "SegmentAttributes": {
         "string" : {
            "ValueArn": "string",
            "ValueInteger": number,
            "ValueList": [
               "SegmentAttributeValue"
            ],
            "ValueMap": {
               "string" : "SegmentAttributeValue"
            },
            "ValueString": "string"
         }
      },
      "SystemEndpoint": {
         "Address": "string",
         "DisplayName": "string",
         "Type": "string"
      },
      "Tags": {
         "string" : "string"
      },
      "TaskTemplateInfo": {
         "Arn": "string",
         "Name": "string"
      },
      "TotalPauseCount": number,
      "TotalPauseDurationInSeconds": number,
      "WisdomInfo": {
         "AiAgents": [
            {
               "AiAgentEscalated": boolean,
               "AiAgentVersionId": "string",
               "AiUseCase": "string"
            }
         ],
         "SessionArn": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Contact](#API_DescribeContact_ResponseSyntax) **   <a name="connect-DescribeContact-response-Contact"></a>
Information about the contact.
Type: [Contact](API_Contact.md) object

## Errors
<a name="API_DescribeContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeContact)
