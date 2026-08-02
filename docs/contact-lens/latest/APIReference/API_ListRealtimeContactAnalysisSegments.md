---
source_url: https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.html
---

# ListRealtimeContactAnalysisSegments
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments"></a>

Provides a list of analysis segments for a real-time analysis session for voice.

**Note**
Voice data is retained for 24 hours. You must invoke this API during that time.

## Request Syntax
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestSyntax"></a>

```
POST /realtime-contact-analysis/analysis-segments HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-request-ContactId"></a>
The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [InstanceId](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-request-InstanceId"></a>
The identifier of the Amazon Connect instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [MaxResults](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_RequestSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131070.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Segments": [
      {
         "Categories": {
            "MatchedCategories": [ "string" ],
            "MatchedDetails": {
               "string" : {
                  "PointsOfInterest": [
                     {
                        "BeginOffsetMillis": number,
                        "EndOffsetMillis": number
                     }
                  ]
               }
            }
         },
         "PostContactSummary": {
            "Content": "string",
            "FailureCode": "string",
            "Status": "string"
         },
         "Transcript": {
            "BeginOffsetMillis": number,
            "Content": "string",
            "EndOffsetMillis": number,
            "Id": "string",
            "IssuesDetected": [
               {
                  "CharacterOffsets": {
                     "BeginOffsetChar": number,
                     "EndOffsetChar": number
                  }
               }
            ],
            "ParticipantId": "string",
            "ParticipantRole": "string",
            "Sentiment": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_ResponseSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-response-NextToken"></a>
If there are additional results, this is the token for the next set of results. If response includes `nextToken` there are two possible scenarios:
+ There are more segments so another call is required to get them.
+ There are no more segments at this time, but more may be available later (real-time analysis is in progress) so the client should call the operation again to get new segments.
If response does not include `nextToken`, the analysis is completed (successfully or failed) and there are no more segments to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131070.
Pattern: `.*\S.*`

 ** [Segments](#API_connect-contact-lens_ListRealtimeContactAnalysisSegments_ResponseSyntax) **   <a name="connect-connect-contact-lens_ListRealtimeContactAnalysisSegments-response-Segments"></a>
An analyzed transcript or category.
Type: Array of [RealtimeContactAnalysisSegment](API_connect-contact-lens_RealtimeContactAnalysisSegment.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_Examples"></a>

### Example
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_Example_1"></a>

This example illustrates one usage of ListRealtimeContactAnalysisSegments.

#### Sample Request
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_Example_1_Request"></a>

```
POST /realtime-contact-analysis/analysis-segments
{
  "InstanceId": "eeeeeee-eeee-eeee-eeee-eeeeeeeeeeee",
  "ContactId": "11111111-1111-1111-1111-11111111111",
  "MaxResults": 50,
  "NextToken": "fdsfsadgdfsgdfgfdhfghfghfgjmbnmnm"
}
```

#### Sample Response
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_Example_1_Response"></a>

```
{
    "Segments": [
        {
            "Transcript": {
                "Id": "tttttttt-tttt-tttt-tttt-tttttttt",
                "ParticipantId": "AGENT",
                "ParticipantRole": "AGENT",
                "Content": "I can't login.",
                "BeginOffsetMillis": 19010,
                "EndOffsetMillis": 22690,
                "Sentiment": "NEUTRAL",
                "IssuesDetected": [
                    {
                        "CharacterOffsets": {
                            "BeginOffsetChar": 8,
                            "EndOffsetChar": 12
                        }
                    }
                ]
            }
        },
        {
            "Categories": {
                "MatchedCategories": [
                    "CreditCardRelated",
                    "CardBrokenIssue"
                ],
                "MatchedDetails": {
                    "CreditCardRelated": {
                        "PointsOfInterest": [
                            {
                                "BeginOffsetMillis": 19010,
                                "EndOffsetMillis": 22690
                            }
                        ]
                    },
                    "CardBrokenIssue": {
                        "PointsOfInterest": [
                            {
                                "BeginOffsetMillis": 25000,
                                "EndOffsetMillis": 29690
                            }
                        ]
                    }
                }
            }
        }
    ],
    "NextToken": "fdsfsadgdfsgdfgfdhfghfghfgjmbnmnm"
}
```

## See Also
<a name="API_connect-contact-lens_ListRealtimeContactAnalysisSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)
