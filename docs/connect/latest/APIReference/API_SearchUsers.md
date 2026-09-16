---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchUsers.html
---

# SearchUsers
<a name="API_SearchUsers"></a>

Searches users in an Connect Customer instance, with optional filtering.

**Note**
 `AfterContactWorkTimeLimit` is returned in milliseconds.

## Request Syntax
<a name="API_SearchUsers_RequestSyntax"></a>

```
POST /search-users HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "UserSearchCriteria"
      ],
      "HierarchyGroupCondition": {
         "HierarchyGroupMatchType": "{{string}}",
         "Value": "{{string}}"
      },
      "ListCondition": {
         "Conditions": [
            {
               "NumberCondition": {
                  "ComparisonType": "{{string}}",
                  "FieldName": "{{string}}",
                  "MaxValue": {{number}},
                  "MinValue": {{number}}
               },
               "StringCondition": {
                  "ComparisonType": "{{string}}",
                  "FieldName": "{{string}}",
                  "Value": "{{string}}"
               }
            }
         ],
         "TargetListType": "{{string}}"
      },
      "OrConditions": [
         "UserSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "TagFilter": {
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
      "UserAttributeFilter": {
         "AndCondition": {
            "HierarchyGroupCondition": {
               "HierarchyGroupMatchType": "{{string}}",
               "Value": "{{string}}"
            },
            "TagConditions": [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         },
         "HierarchyGroupCondition": {
            "HierarchyGroupMatchType": "{{string}}",
            "Value": "{{string}}"
         },
         "OrConditions": [
            {
               "HierarchyGroupCondition": {
                  "HierarchyGroupMatchType": "{{string}}",
                  "Value": "{{string}}"
               },
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
<a name="API_SearchUsers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchUsers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchUsers_RequestSyntax) **   <a name="connect-SearchUsers-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchUsers_RequestSyntax) **   <a name="connect-SearchUsers-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_SearchUsers_RequestSyntax) **   <a name="connect-SearchUsers-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchUsers_RequestSyntax) **   <a name="connect-SearchUsers-request-SearchCriteria"></a>
The search criteria to be used to return users.
The `name` and `description` fields support "contains" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.
Type: [UserSearchCriteria](API_UserSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchUsers_RequestSyntax) **   <a name="connect-SearchUsers-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [UserSearchFilter](API_UserSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchUsers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "Users": [
      {
         "AfterContactWorkConfigs": [
            {
               "AfterContactWorkConfig": {
                  "AfterContactWorkTimeLimit": number
               },
               "AgentFirstCallbackAfterContactWorkConfig": {
                  "AfterContactWorkTimeLimit": number
               },
               "Channel": "string"
            }
         ],
         "Arn": "string",
         "AutoAcceptConfigs": [
            {
               "AgentFirstCallbackAutoAccept": boolean,
               "AutoAccept": boolean,
               "Channel": "string"
            }
         ],
         "DirectoryUserId": "string",
         "HierarchyGroupId": "string",
         "Id": "string",
         "IdentityInfo": {
            "FirstName": "string",
            "LastName": "string"
         },
         "PersistentConnectionConfigs": [
            {
               "Channel": "string",
               "PersistentConnection": boolean
            }
         ],
         "PhoneConfig": {
            "AfterContactWorkTimeLimit": number,
            "AutoAccept": boolean,
            "DeskPhoneNumber": "string",
            "PersistentConnection": boolean,
            "PhoneType": "string"
         },
         "PhoneNumberConfigs": [
            {
               "Channel": "string",
               "PhoneNumber": "string",
               "PhoneType": "string"
            }
         ],
         "RoutingProfileId": "string",
         "SecurityProfileIds": [ "string" ],
         "Tags": {
            "string" : "string"
         },
         "Username": "string",
         "VoiceEnhancementConfigs": [
            {
               "Channel": "string",
               "VoiceEnhancementMode": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_SearchUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchUsers_ResponseSyntax) **   <a name="connect-SearchUsers-response-ApproximateTotalCount"></a>
The total number of users who matched your search query.
Type: Long

 ** [NextToken](#API_SearchUsers_ResponseSyntax) **   <a name="connect-SearchUsers-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [Users](#API_SearchUsers_ResponseSyntax) **   <a name="connect-SearchUsers-response-Users"></a>
Information about the users.
Type: Array of [UserSearchSummary](API_UserSearchSummary.md) objects

## Errors
<a name="API_SearchUsers_Errors"></a>

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
<a name="API_SearchUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchUsers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchUsers)
