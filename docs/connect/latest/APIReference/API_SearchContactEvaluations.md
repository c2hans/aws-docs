---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactEvaluations.html
---

# SearchContactEvaluations
<a name="API_SearchContactEvaluations"></a>

Searches contact evaluations in an Connect Customer instance, with optional filtering.

 **Use cases**

Following are common uses cases for this API:
+ Find contact evaluations by using specific search criteria.
+ Find contact evaluations that are tagged with a specific set of tags.

 **Important things to know**
+ A Search operation, unlike a List operation, takes time to index changes to resource (create, update or delete). If you don't see updated information for recently changed contact evaluations, try calling the API again in a few seconds.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_SearchContactEvaluations_RequestSyntax"></a>

```
POST /search-contact-evaluations HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "EvaluationSearchCriteria"
      ],
      "BooleanCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}"
      },
      "DateTimeCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "MaxValue": "{{string}}",
         "MinValue": "{{string}}"
      },
      "DecimalCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "MaxValue": {{number}},
         "MinValue": {{number}}
      },
      "NumberCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "MaxValue": {{number}},
         "MinValue": {{number}}
      },
      "OrConditions": [
         "EvaluationSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "AttributeFilter": {
         "AndCondition": {
            "TagConditions": [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         },
         "OrConditions": [
            {
               "TagConditions": [
                  {
                     "TagKey": "{{string}}",
                     "TagValue": "{{string}}"
                  }
               ]
            }
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      },
      "ContactEvaluationAttributeFilter": {
         "AndCondition": {
            "AttributeConditions": [
               {
                  "AttributeKey": "{{string}}",
                  "AttributeValue": {
                     "StringValue": "{{string}}"
                  },
                  "ComparisonType": "{{string}}"
               }
            ],
            "TagConditions": [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         },
         "ContactEvaluationAttributeCondition": {
            "AttributeKey": "{{string}}",
            "AttributeValue": {
               "StringValue": "{{string}}"
            },
            "ComparisonType": "{{string}}"
         },
         "OrConditions": [
            {
               "AttributeConditions": [
                  {
                     "AttributeKey": "{{string}}",
                     "AttributeValue": {
                        "StringValue": "{{string}}"
                     },
                     "ComparisonType": "{{string}}"
                  }
               ],
               "TagConditions": [
                  {
                     "TagKey": "{{string}}",
                     "TagValue": "{{string}}"
                  }
               ]
            }
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchContactEvaluations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchContactEvaluations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchContactEvaluations_RequestSyntax) **   <a name="connect-SearchContactEvaluations-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchContactEvaluations_RequestSyntax) **   <a name="connect-SearchContactEvaluations-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchContactEvaluations_RequestSyntax) **   <a name="connect-SearchContactEvaluations-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Required: No

 ** [SearchCriteria](#API_SearchContactEvaluations_RequestSyntax) **   <a name="connect-SearchContactEvaluations-request-SearchCriteria"></a>
The search criteria to be used to return contact evaluations.
Type: [EvaluationSearchCriteria](API_EvaluationSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchContactEvaluations_RequestSyntax) **   <a name="connect-SearchContactEvaluations-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [EvaluationSearchFilter](API_EvaluationSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchContactEvaluations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "EvaluationSearchSummaryList": [
      {
         "CreatedTime": number,
         "EvaluationArn": "string",
         "EvaluationFormId": "string",
         "EvaluationFormTitle": "string",
         "EvaluationFormVersion": number,
         "EvaluationId": "string",
         "EvaluationType": "string",
         "LastModifiedTime": number,
         "Metadata": {
            "AcknowledgedBy": "string",
            "AcknowledgedTime": number,
            "AcknowledgerComment": "string",
            "AutoEvaluationEnabled": boolean,
            "AutoEvaluationStatus": "string",
            "CalibrationSessionId": "string",
            "ContactAgentId": "string",
            "ContactId": "string",
            "ContactParticipantId": "string",
            "ContactParticipantRole": "string",
            "EarnedPoints": number,
            "EvaluatorArn": "string",
            "MaxBasePoint": number,
            "PerformanceCategory": "string",
            "ReviewId": "string",
            "SamplingJobId": "string",
            "ScoreAutomaticFail": boolean,
            "ScoreNotApplicable": boolean,
            "ScorePercentage": number
         },
         "Status": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchContactEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchContactEvaluations_ResponseSyntax) **   <a name="connect-SearchContactEvaluations-response-ApproximateTotalCount"></a>
The total number of contact evaluations that matched your search query.
Type: Long

 ** [EvaluationSearchSummaryList](#API_SearchContactEvaluations_ResponseSyntax) **   <a name="connect-SearchContactEvaluations-response-EvaluationSearchSummaryList"></a>
Contains information about contact evaluations.
Type: Array of [EvaluationSearchSummary](API_EvaluationSearchSummary.md) objects

 ** [NextToken](#API_SearchContactEvaluations_ResponseSyntax) **   <a name="connect-SearchContactEvaluations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_SearchContactEvaluations_Errors"></a>

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

## Examples
<a name="API_SearchContactEvaluations_Examples"></a>

### Example request to retrieve evaluations in instance
<a name="API_SearchContactEvaluations_Example_1"></a>

This example illustrates one usage of SearchContactEvaluations.

```
{
  "InstanceId": "12345678-1234-5678-aabb-123456abcdef"
}
```

### Example request to retrieve an evaluation with a specific ID in instance
<a name="API_SearchContactEvaluations_Example_2"></a>

This example illustrates one usage of SearchContactEvaluations.

```
{
  "InstanceId": "12345678-1234-5678-aabb-123456abcdef",
  "SearchCriteria": {
    "StringCondition": {
      "ComparisonType": "EXACT",
      "FieldName": "EvaluationId",
      "Value": "87654321-4321-8765-bbaa-abcdef123456"
    }
  }
}
```

### Example request to retrieve evaluations by using multiple search criteria
<a name="API_SearchContactEvaluations_Example_3"></a>

This example illustrates one usage of SearchContactEvaluations.

```
{
  "InstanceId": "12345678-1234-5678-aabb-123456abcdef",
  "SearchCriteria": {
    "OrConditions": [
      {
        "AndConditions": [
          {
            "DateTimeCondition": {
              "ComparisonType": "GREATER_THAN",
              "FieldName": "LastModifiedTime",
              "MinValue": "2020-01-01T00:00:00Z"
            }
          },
          {
            "NumberCondition": {
              "ComparisonType": "EQUAL",
              "FieldName": "EvaluationFormVersion",
              "MinValue": 1
            }
          },
          {
            "BooleanCondition": {
              "ComparisonType": "IS_FALSE",
              "FieldName": "AutoEvaluationEnabled"
            }
          }
        ]
      }
    ]
  }
}
```

## See Also
<a name="API_SearchContactEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchContactEvaluations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContactEvaluations)
