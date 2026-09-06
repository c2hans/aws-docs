---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchWorkspaceAssociations.html
---

# SearchWorkspaceAssociations
<a name="API_SearchWorkspaceAssociations"></a>

Searches for workspace associations with users or routing profiles based on various criteria.

## Request Syntax
<a name="API_SearchWorkspaceAssociations_RequestSyntax"></a>

```
POST /search-workspace-associations HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "WorkspaceAssociationSearchCriteria"
      ],
      "OrConditions": [
         "WorkspaceAssociationSearchCriteria"
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
<a name="API_SearchWorkspaceAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchWorkspaceAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchWorkspaceAssociations_RequestSyntax) **   <a name="connect-SearchWorkspaceAssociations-request-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchWorkspaceAssociations_RequestSyntax) **   <a name="connect-SearchWorkspaceAssociations-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_SearchWorkspaceAssociations_RequestSyntax) **   <a name="connect-SearchWorkspaceAssociations-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchWorkspaceAssociations_RequestSyntax) **   <a name="connect-SearchWorkspaceAssociations-request-SearchCriteria"></a>
The search criteria, including workspace ID, resource ID, or resource type.
Type: [WorkspaceAssociationSearchCriteria](API_WorkspaceAssociationSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchWorkspaceAssociations_RequestSyntax) **   <a name="connect-SearchWorkspaceAssociations-request-SearchFilter"></a>
Filters to apply to the search, such as tag-based filters.
Type: [WorkspaceAssociationSearchFilter](API_WorkspaceAssociationSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchWorkspaceAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "WorkspaceAssociations": [
      {
         "ResourceArn": "string",
         "ResourceId": "string",
         "ResourceName": "string",
         "ResourceType": "string",
         "WorkspaceArn": "string",
         "WorkspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchWorkspaceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchWorkspaceAssociations_ResponseSyntax) **   <a name="connect-SearchWorkspaceAssociations-response-ApproximateTotalCount"></a>
The approximate total number of workspace associations that match the search criteria.
Type: Long

 ** [NextToken](#API_SearchWorkspaceAssociations_ResponseSyntax) **   <a name="connect-SearchWorkspaceAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [WorkspaceAssociations](#API_SearchWorkspaceAssociations_ResponseSyntax) **   <a name="connect-SearchWorkspaceAssociations-response-WorkspaceAssociations"></a>
A list of workspace associations that match the search criteria.
Type: Array of [WorkspaceAssociationSearchSummary](API_WorkspaceAssociationSearchSummary.md) objects

## Errors
<a name="API_SearchWorkspaceAssociations_Errors"></a>

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

## See Also
<a name="API_SearchWorkspaceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchWorkspaceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchWorkspaceAssociations)
