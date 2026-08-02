---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRules.html
---

# SearchRules
<a name="API_SearchRules"></a>

Searches rules in an Connect Customer instance, with optional filtering.

## Request Syntax
<a name="API_SearchRules_RequestSyntax"></a>

```
POST /search-rules HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "RulesSearchCriteria"
      ],
      "OrConditions": [
         "RulesSearchCriteria"
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
<a name="API_SearchRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchRules_RequestSyntax) **   <a name="connect-SearchRules-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchRules_RequestSyntax) **   <a name="connect-SearchRules-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_SearchRules_RequestSyntax) **   <a name="connect-SearchRules-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchRules_RequestSyntax) **   <a name="connect-SearchRules-request-SearchCriteria"></a>
The search criteria to be used to return rules.
Type: [RulesSearchCriteria](API_RulesSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchRules_RequestSyntax) **   <a name="connect-SearchRules-request-SearchFilter"></a>
Filters to be applied to search results, such as tag-based filters.
Type: [RulesSearchFilter](API_RulesSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "Rules": [
      {
         "ActionSummaries": [
            {
               "ActionType": "string"
            }
         ],
         "CreatedTime": number,
         "LastUpdatedBy": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "PublishStatus": "string",
         "RuleArn": "string",
         "RuleCapabilityTiers": [ "string" ],
         "RuleId": "string",
         "Tags": {
            "string" : "string"
         },
         "TriggerEventSource": {
            "EventSourceName": "string",
            "IntegrationAssociationId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchRules_ResponseSyntax) **   <a name="connect-SearchRules-response-ApproximateTotalCount"></a>
The total number of rules which matched your search query.
Type: Long

 ** [NextToken](#API_SearchRules_ResponseSyntax) **   <a name="connect-SearchRules-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [Rules](#API_SearchRules_ResponseSyntax) **   <a name="connect-SearchRules-response-Rules"></a>
Information about the rules.
Type: Array of [RuleSearchSummary](API_RuleSearchSummary.md) objects

## Errors
<a name="API_SearchRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_SearchRules_Examples"></a>

### Example
<a name="API_SearchRules_Example_1"></a>

The following example searches for published rules in an instance.

#### Sample Request
<a name="API_SearchRules_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "MaxResults": 10,
   "SearchCriteria": {
      "StringCondition": {
         "FieldName": "PublishStatus",
         "Value": "PUBLISHED",
         "ComparisonType": "EXACT"
      }
   }
}
```

#### Sample Response
<a name="API_SearchRules_Example_1_Response"></a>

```
{
   "Rules": [
      {
         "Name": "MyRule",
         "RuleId": "[rule_id]",
         "RuleArn": "arn:aws:connect:[region]:[account_id]:instance/[instance_id]/rule/[rule_id]",
         "PublishStatus": "PUBLISHED",
         "RuleCapabilityTiers": [],
         "CreatedTime": "2026-01-15T10:00:00Z",
         "LastUpdatedTime": "2026-03-20T14:30:00Z"
      }
   ],
   "ApproximateTotalCount": 1
}
```

## See Also
<a name="API_SearchRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchRules)
