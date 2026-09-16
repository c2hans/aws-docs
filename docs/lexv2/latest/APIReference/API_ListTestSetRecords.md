---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestSetRecords.html
---

# ListTestSetRecords
<a name="API_ListTestSetRecords"></a>

The list of test set records.

## Request Syntax
<a name="API_ListTestSetRecords_RequestSyntax"></a>

```
POST /testsets/{{testSetId}}/records HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTestSetRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetId](#API_ListTestSetRecords_RequestSyntax) **   <a name="lexv2-ListTestSetRecords-request-uri-testSetId"></a>
The identifier of the test set to list its test set records.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListTestSetRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTestSetRecords_RequestSyntax) **   <a name="lexv2-ListTestSetRecords-request-maxResults"></a>
The maximum number of test set records to return in each page. If there are fewer records than the max page size, only the actual number of records are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestSetRecords_RequestSyntax) **   <a name="lexv2-ListTestSetRecords-request-nextToken"></a>
If the response from the ListTestSetRecords operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListTestSetRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testSetRecords": [
      {
         "conversationId": "string",
         "recordNumber": number,
         "turnNumber": number,
         "turnSpecification": {
            "agentTurn": {
               "agentPrompt": "string"
            },
            "userTurn": {
               "expected": {
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
               }
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTestSetRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestSetRecords_ResponseSyntax) **   <a name="lexv2-ListTestSetRecords-response-nextToken"></a>
A token that indicates whether there are more records to return in a response to the ListTestSetRecords operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestSetRecords operation request to get the next page of records.
Type: String

 ** [testSetRecords](#API_ListTestSetRecords_ResponseSyntax) **   <a name="lexv2-ListTestSetRecords-response-testSetRecords"></a>
The list of records from the test set.
Type: Array of [TestSetTurnRecord](API_TestSetTurnRecord.md) objects

## Errors
<a name="API_ListTestSetRecords_Errors"></a>

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
<a name="API_ListTestSetRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListTestSetRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListTestSetRecords)
