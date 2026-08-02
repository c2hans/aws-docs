---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchEvaluationForms.html
---

# SearchEvaluationForms
<a name="API_SearchEvaluationForms"></a>

Searches evaluation forms in an Connect Customer instance, with optional filtering.

 **Use cases**

Following are common uses cases for this API:
+ List all evaluation forms in an instance.
+ Find all evaluation forms that meet specific criteria, such as Title, Description, Status, and more.
+ Find all evaluation forms that are tagged with a specific set of tags.

 **Important things to know**
+ A Search operation, unlike a List operation, takes time to index changes to resource (create, update or delete). If you don't see updated information for recently changed contact evaluations, try calling the API again in a few seconds.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_SearchEvaluationForms_RequestSyntax"></a>

```
POST /search-evaluation-forms HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "EvaluationFormSearchCriteria"
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
      "NumberCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "MaxValue": {{number}},
         "MinValue": {{number}}
      },
      "OrConditions": [
         "EvaluationFormSearchCriteria"
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
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchEvaluationForms_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchEvaluationForms_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchEvaluationForms_RequestSyntax) **   <a name="connect-SearchEvaluationForms-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchEvaluationForms_RequestSyntax) **   <a name="connect-SearchEvaluationForms-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchEvaluationForms_RequestSyntax) **   <a name="connect-SearchEvaluationForms-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Required: No

 ** [SearchCriteria](#API_SearchEvaluationForms_RequestSyntax) **   <a name="connect-SearchEvaluationForms-request-SearchCriteria"></a>
The search criteria to be used to return evaluation forms.
Type: [EvaluationFormSearchCriteria](API_EvaluationFormSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchEvaluationForms_RequestSyntax) **   <a name="connect-SearchEvaluationForms-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [EvaluationFormSearchFilter](API_EvaluationFormSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchEvaluationForms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "EvaluationFormSearchSummaryList": [
      {
         "ActiveVersion": number,
         "AutoEvaluationEnabled": boolean,
         "ContactInteractionType": "string",
         "CreatedBy": "string",
         "CreatedTime": number,
         "Description": "string",
         "EvaluationFormArn": "string",
         "EvaluationFormId": "string",
         "EvaluationFormLanguage": "string",
         "LastActivatedBy": "string",
         "LastActivatedTime": number,
         "LastModifiedBy": "string",
         "LastModifiedTime": number,
         "LatestVersion": number,
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchEvaluationForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchEvaluationForms_ResponseSyntax) **   <a name="connect-SearchEvaluationForms-response-ApproximateTotalCount"></a>
The total number of evaluation forms that matched your search query.
Type: Long

 ** [EvaluationFormSearchSummaryList](#API_SearchEvaluationForms_ResponseSyntax) **   <a name="connect-SearchEvaluationForms-response-EvaluationFormSearchSummaryList"></a>
Information about the returned evaluation forms.
Type: Array of [EvaluationFormSearchSummary](API_EvaluationFormSearchSummary.md) objects

 ** [NextToken](#API_SearchEvaluationForms_ResponseSyntax) **   <a name="connect-SearchEvaluationForms-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_SearchEvaluationForms_Errors"></a>

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
<a name="API_SearchEvaluationForms_Examples"></a>

### Example request to retrieve all evaluation forms in an instance
<a name="API_SearchEvaluationForms_Example_1"></a>

This example illustrates one usage of SearchEvaluationForms.

```
{
"InstanceId": "12345678-1234-5678-aabb-123456abcdef"
}
```

### Example request to retrieve an evaluation form with a specific ID in an instance
<a name="API_SearchEvaluationForms_Example_2"></a>

This example illustrates one usage of SearchEvaluationForms.

```
{
  "InstanceId": "12345678-1234-5678-aabb-123456abcdef",
  "SearchCriteria": {
    "StringCondition": {
      "ComparisonType": "EXACT",
      "FieldName": "EvaluationFormId",
      "Value": "87654321-4321-8765-bbaa-abcdef123456"
    }
  }
}
```

### Example request to retrieve evaluation forms by using multiple search criteria in an instance
<a name="API_SearchEvaluationForms_Example_3"></a>

This example illustrates one usage of SearchEvaluationForms.

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
              "FieldName": "LatestVersion",
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
<a name="API_SearchEvaluationForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchEvaluationForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchEvaluationForms)
