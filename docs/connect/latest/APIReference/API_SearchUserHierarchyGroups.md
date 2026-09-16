---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchUserHierarchyGroups.html
---

# SearchUserHierarchyGroups
<a name="API_SearchUserHierarchyGroups"></a>

Searches UserHierarchyGroups in an Connect Customer instance, with optional filtering.

**Important**
The UserHierarchyGroup with `"LevelId": "0"` is the foundation for building levels on top of an instance. It is not user-definable, nor is it visible in the UI.

## Request Syntax
<a name="API_SearchUserHierarchyGroups_RequestSyntax"></a>

```
POST /search-user-hierarchy-groups HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "UserHierarchyGroupSearchCriteria"
      ],
      "OrConditions": [
         "UserHierarchyGroupSearchCriteria"
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
<a name="API_SearchUserHierarchyGroups_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchUserHierarchyGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchUserHierarchyGroups_RequestSyntax) **   <a name="connect-SearchUserHierarchyGroups-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchUserHierarchyGroups_RequestSyntax) **   <a name="connect-SearchUserHierarchyGroups-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchUserHierarchyGroups_RequestSyntax) **   <a name="connect-SearchUserHierarchyGroups-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchUserHierarchyGroups_RequestSyntax) **   <a name="connect-SearchUserHierarchyGroups-request-SearchCriteria"></a>
The search criteria to be used to return UserHierarchyGroups.
Type: [UserHierarchyGroupSearchCriteria](API_UserHierarchyGroupSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchUserHierarchyGroups_RequestSyntax) **   <a name="connect-SearchUserHierarchyGroups-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [UserHierarchyGroupSearchFilter](API_UserHierarchyGroupSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchUserHierarchyGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "UserHierarchyGroups": [
      {
         "Arn": "string",
         "HierarchyPath": {
            "LevelFive": {
               "Arn": "string",
               "Id": "string",
               "LastModifiedRegion": "string",
               "LastModifiedTime": number,
               "Name": "string"
            },
            "LevelFour": {
               "Arn": "string",
               "Id": "string",
               "LastModifiedRegion": "string",
               "LastModifiedTime": number,
               "Name": "string"
            },
            "LevelOne": {
               "Arn": "string",
               "Id": "string",
               "LastModifiedRegion": "string",
               "LastModifiedTime": number,
               "Name": "string"
            },
            "LevelThree": {
               "Arn": "string",
               "Id": "string",
               "LastModifiedRegion": "string",
               "LastModifiedTime": number,
               "Name": "string"
            },
            "LevelTwo": {
               "Arn": "string",
               "Id": "string",
               "LastModifiedRegion": "string",
               "LastModifiedTime": number,
               "Name": "string"
            }
         },
         "Id": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "LevelId": "string",
         "Name": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchUserHierarchyGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchUserHierarchyGroups_ResponseSyntax) **   <a name="connect-SearchUserHierarchyGroups-response-ApproximateTotalCount"></a>
The total number of userHierarchyGroups which matched your search query.
Type: Long

 ** [NextToken](#API_SearchUserHierarchyGroups_ResponseSyntax) **   <a name="connect-SearchUserHierarchyGroups-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [UserHierarchyGroups](#API_SearchUserHierarchyGroups_ResponseSyntax) **   <a name="connect-SearchUserHierarchyGroups-response-UserHierarchyGroups"></a>
Information about the userHierarchyGroups.
Type: Array of [HierarchyGroup](API_HierarchyGroup.md) objects

## Errors
<a name="API_SearchUserHierarchyGroups_Errors"></a>

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
<a name="API_SearchUserHierarchyGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchUserHierarchyGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchUserHierarchyGroups)
