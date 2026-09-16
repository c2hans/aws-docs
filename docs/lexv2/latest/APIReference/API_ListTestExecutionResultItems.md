---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestExecutionResultItems.html
---

# ListTestExecutionResultItems
<a name="API_ListTestExecutionResultItems"></a>

Gets a list of test execution result items.

## Request Syntax
<a name="API_ListTestExecutionResultItems_RequestSyntax"></a>

```
POST /testexecutions/{{testExecutionId}}/results HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resultFilterBy": {
      "conversationLevelTestResultsFilterBy": {
         "endToEndResult": "{{string}}"
      },
      "resultTypeFilter": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListTestExecutionResultItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testExecutionId](#API_ListTestExecutionResultItems_RequestSyntax) **   <a name="lexv2-ListTestExecutionResultItems-request-uri-testExecutionId"></a>
The unique identifier of the test execution to list the result items.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListTestExecutionResultItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTestExecutionResultItems_RequestSyntax) **   <a name="lexv2-ListTestExecutionResultItems-request-maxResults"></a>
The maximum number of test execution result items to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestExecutionResultItems_RequestSyntax) **   <a name="lexv2-ListTestExecutionResultItems-request-nextToken"></a>
If the response from the `ListTestExecutionResultItems` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response. Use that token in the `nextToken` parameter to return the next page of results.
Type: String
Required: No

 ** [resultFilterBy](#API_ListTestExecutionResultItems_RequestSyntax) **   <a name="lexv2-ListTestExecutionResultItems-request-resultFilterBy"></a>
The filter for the list of results from the test set execution.
Type: [TestExecutionResultFilterBy](API_TestExecutionResultFilterBy.md) object
Required: Yes

## Response Syntax
<a name="API_ListTestExecutionResultItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testExecutionResults": {
      "conversationLevelTestResults": {
         "items": [
            {
               "conversationId": "string",
               "endToEndResult": "string",
               "intentClassificationResults": [
                  {
                     "intentName": "string",
                     "matchResult": "string"
                  }
               ],
               "slotResolutionResults": [
                  {
                     "intentName": "string",
                     "matchResult": "string",
                     "slotName": "string"
                  }
               ],
               "speechTranscriptionResult": "string"
            }
         ]
      },
      "intentClassificationTestResults": {
         "items": [
            {
               "intentName": "string",
               "multiTurnConversation": boolean,
               "resultCounts": {
                  "intentMatchResultCounts": {
                     "string" : number
                  },
                  "speechTranscriptionResultCounts": {
                     "string" : number
                  },
                  "totalResultCount": number
               }
            }
         ]
      },
      "intentLevelSlotResolutionTestResults": {
         "items": [
            {
               "intentName": "string",
               "multiTurnConversation": boolean,
               "slotResolutionResults": [
                  {
                     "resultCounts": {
                        "slotMatchResultCounts": {
                           "string" : number
                        },
                        "speechTranscriptionResultCounts": {
                           "string" : number
                        },
                        "totalResultCount": number
                     },
                     "slotName": "string"
                  }
               ]
            }
         ]
      },
      "overallTestResults": {
         "items": [
            {
               "endToEndResultCounts": {
                  "string" : number
               },
               "multiTurnConversation": boolean,
               "speechTranscriptionResultCounts": {
                  "string" : number
               },
               "totalResultCount": number
            }
         ]
      },
      "utteranceLevelTestResults": {
         "items": [
            {
               "conversationId": "string",
               "recordNumber": number,
               "turnResult": {
                  "agent": {
                     "actualAgentPrompt": "string",
                     "actualElicitedSlot": "string",
                     "actualIntent": "string",
                     "errorDetails": {
                        "errorCode": "string",
                        "errorMessage": "string"
                     },
                     "expectedAgentPrompt": "string"
                  },
                  "user": {
                     "actualOutput": {
                        "activeContexts": [
                           {
                              "name": "string"
                           }
                        ],
                        "intent": {
                           "name": "string",
                           "slots": {
                              "string" : {
                                 "subSlots": {
                                    "string" : "UserTurnSlotOutput"
                                 },
                                 "value": "string",
                                 "values": [
                                    "UserTurnSlotOutput"
                                 ]
                              }
                           }
                        },
                        "transcript": "string"
                     },
                     "conversationLevelResult": {
                        "endToEndResult": "string",
                        "speechTranscriptionResult": "string"
                     },
                     "endToEndResult": "string",
                     "errorDetails": {
                        "errorCode": "string",
                        "errorMessage": "string"
                     },
                     "expectedOutput": {
                        "activeContexts": [
                           {
                              "name": "string"
                           }
                        ],
                        "intent": {
                           "name": "string",
                           "slots": {
                              "string" : {
                                 "subSlots": {
                                    "string" : "UserTurnSlotOutput"
                                 },
                                 "value": "string",
                                 "values": [
                                    "UserTurnSlotOutput"
                                 ]
                              }
                           }
                        },
                        "transcript": "string"
                     },
                     "input": {
                        "requestAttributes": {
                           "string" : "string"
                        },
                        "sessionState": {
                           "activeContexts": [
                              {
                                 "name": "string"
                              }
                           ],
                           "runtimeHints": {
                              "slotHints": {
                                 "string" : {
                                    "string" : {
                                       "runtimeHintValues": [
                                          {
                                             "phrase": "string"
                                          }
                                       ],
                                       "subSlotHints": {
                                          "string" : "RuntimeHintDetails"
                                       }
                                    }
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "string" : "string"
                           }
                        },
                        "utteranceInput": {
                           "audioInput": {
                              "audioFileS3Location": "string"
                           },
                           "textInput": "string"
                        }
                     },
                     "intentMatchResult": "string",
                     "slotMatchResult": "string",
                     "speechTranscriptionResult": "string"
                  }
               }
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_ListTestExecutionResultItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestExecutionResultItems_ResponseSyntax) **   <a name="lexv2-ListTestExecutionResultItems-response-nextToken"></a>
A token that indicates whether there are more results to return in a response to the `ListTestExecutionResultItems` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListTestExecutionResultItems` operation request to get the next page of results.
Type: String

 ** [testExecutionResults](#API_ListTestExecutionResultItems_ResponseSyntax) **   <a name="lexv2-ListTestExecutionResultItems-response-testExecutionResults"></a>
The list of results from the test execution.
Type: [TestExecutionResultItems](API_TestExecutionResultItems.md) object

## Errors
<a name="API_ListTestExecutionResultItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListTestExecutionResultItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListTestExecutionResultItems)
