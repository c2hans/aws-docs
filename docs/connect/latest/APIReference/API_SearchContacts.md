---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContacts.html
---

# SearchContacts
<a name="API_SearchContacts"></a>

Searches contacts in an Connect Customer instance.

## Request Syntax
<a name="API_SearchContacts_RequestSyntax"></a>

```
POST /search-contacts HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "ActiveRegions": [ "{{string}}" ],
      "AdditionalTimeRange": {
         "Criteria": [
            {
               "TimeRange": {
                  "EndTime": {{number}},
                  "StartTime": {{number}},
                  "Type": "{{string}}"
               },
               "TimestampCondition": {
                  "ConditionType": "{{string}}",
                  "Type": "{{string}}"
               }
            }
         ],
         "MatchType": "{{string}}"
      },
      "AgentHierarchyGroups": {
         "L1Ids": [ "{{string}}" ],
         "L2Ids": [ "{{string}}" ],
         "L3Ids": [ "{{string}}" ],
         "L4Ids": [ "{{string}}" ],
         "L5Ids": [ "{{string}}" ]
      },
      "AgentIds": [ "{{string}}" ],
      "AiAgents": {
         "Criteria": [
            {
               "AiAgentEscalated": {{boolean}},
               "AiUseCase": "{{string}}",
               "Id": "{{string}}",
               "VersionNumber": {{number}}
            }
         ]
      },
      "Channels": [ "{{string}}" ],
      "ContactAnalysis": {
         "Transcript": {
            "Criteria": [
               {
                  "MatchType": "{{string}}",
                  "ParticipantRole": "{{string}}",
                  "SearchText": [ "{{string}}" ]
               }
            ],
            "MatchType": "{{string}}"
         }
      },
      "ContactTags": {
         "AndConditions": [
            {
               "TagKey": "{{string}}",
               "TagValue": "{{string}}"
            }
         ],
         "OrConditions": [
            [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      },
      "InitiationMethods": [ "{{string}}" ],
      "Name": {
         "MatchType": "{{string}}",
         "SearchText": [ "{{string}}" ]
      },
      "QueueIds": [ "{{string}}" ],
      "RoutingCriteria": {
         "Steps": [
            {
               "AgentCriteria": {
                  "AgentIds": [ "{{string}}" ],
                  "MatchType": "{{string}}"
               }
            }
         ]
      },
      "SearchableContactAttributes": {
         "Criteria": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "MatchType": "{{string}}"
      },
      "SearchableSegmentAttributes": {
         "Criteria": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "MatchType": "{{string}}"
      }
   },
   "Sort": {
      "FieldName": "{{string}}",
      "Order": "{{string}}"
   },
   "TimeRange": {
      "EndTime": {{number}},
      "StartTime": {{number}},
      "Type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_SearchContacts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchContacts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-InstanceId"></a>
The identifier of Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [SearchCriteria](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-SearchCriteria"></a>
The search criteria to be used to return contacts.
Type: [SearchCriteria](API_SearchCriteria.md) object
Required: No

 ** [Sort](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-Sort"></a>
Specifies a field to sort by and a sort order.
Type: [Sort](API_Sort.md) object
Required: No

 ** [TimeRange](#API_SearchContacts_RequestSyntax) **   <a name="connect-SearchContacts-request-TimeRange"></a>
Time range that you want to search results.
Type: [SearchContactsTimeRange](API_SearchContactsTimeRange.md) object
Required: Yes

## Response Syntax
<a name="API_SearchContacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Contacts": [
      {
         "AgentInfo": {
            "ConnectedToAgentTimestamp": number,
            "Id": "string"
         },
         "AiAgentInfo": [
            {
               "AiAgentEscalated": boolean,
               "AiAgentVersionId": "string",
               "AiUseCase": "string"
            }
         ],
         "Arn": "string",
         "Channel": "string",
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
         "Name": "string",
         "PreviousContactId": "string",
         "QueueInfo": {
            "EnqueueTimestamp": number,
            "Id": "string"
         },
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
               "ValueMap": {
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
               "ValueString": "string"
            }
         },
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string",
   "TotalCount": number
}
```

## Response Elements
<a name="API_SearchContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Contacts](#API_SearchContacts_ResponseSyntax) **   <a name="connect-SearchContacts-response-Contacts"></a>
Information about the contacts.
Type: Array of [ContactSearchSummary](API_ContactSearchSummary.md) objects

 ** [NextToken](#API_SearchContacts_ResponseSyntax) **   <a name="connect-SearchContacts-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

 ** [TotalCount](#API_SearchContacts_ResponseSyntax) **   <a name="connect-SearchContacts-response-TotalCount"></a>
The total number of contacts which matched your search query.
Type: Long

## Errors
<a name="API_SearchContacts_Errors"></a>

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
<a name="API_SearchContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchContacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchContacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchContacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchContacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchContacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchContacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchContacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContacts)
