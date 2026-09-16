---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchAgentStatuses.html
---

# SearchAgentStatuses
<a name="API_SearchAgentStatuses"></a>

Searches AgentStatuses in an Connect Customer instance, with optional filtering.

## Request Syntax
<a name="API_SearchAgentStatuses_RequestSyntax"></a>

```
POST /search-agent-statuses HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "AgentStatusSearchCriteria"
      ],
      "OrConditions": [
         "AgentStatusSearchCriteria"
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
<a name="API_SearchAgentStatuses_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchAgentStatuses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchAgentStatuses_RequestSyntax) **   <a name="connect-SearchAgentStatuses-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchAgentStatuses_RequestSyntax) **   <a name="connect-SearchAgentStatuses-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchAgentStatuses_RequestSyntax) **   <a name="connect-SearchAgentStatuses-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchAgentStatuses_RequestSyntax) **   <a name="connect-SearchAgentStatuses-request-SearchCriteria"></a>
The search criteria to be used to return agent statuses.
Type: [AgentStatusSearchCriteria](API_AgentStatusSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchAgentStatuses_RequestSyntax) **   <a name="connect-SearchAgentStatuses-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [AgentStatusSearchFilter](API_AgentStatusSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchAgentStatuses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentStatuses": [
      {
         "AgentStatusARN": "string",
         "AgentStatusId": "string",
         "Description": "string",
         "DisplayOrder": number,
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "State": "string",
         "Tags": {
            "string" : "string"
         },
         "Type": "string"
      }
   ],
   "ApproximateTotalCount": number,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchAgentStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentStatuses](#API_SearchAgentStatuses_ResponseSyntax) **   <a name="connect-SearchAgentStatuses-response-AgentStatuses"></a>
The search criteria to be used to return agent statuses.
Type: Array of [AgentStatus](API_AgentStatus.md) objects

 ** [ApproximateTotalCount](#API_SearchAgentStatuses_ResponseSyntax) **   <a name="connect-SearchAgentStatuses-response-ApproximateTotalCount"></a>
The total number of agent statuses which matched your search query.
Type: Long

 ** [NextToken](#API_SearchAgentStatuses_ResponseSyntax) **   <a name="connect-SearchAgentStatuses-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

## Errors
<a name="API_SearchAgentStatuses_Errors"></a>

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
<a name="API_SearchAgentStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchAgentStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchAgentStatuses)
