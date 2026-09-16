---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html
---

# SearchRoutingProfiles
<a name="API_SearchRoutingProfiles"></a>

Searches routing profiles in an Connect Customer instance, with optional filtering.

**Note**
 `SearchRoutingProfiles` does not populate LastModifiedRegion, LastModifiedTime, MediaConcurrencies.CrossChannelBehavior, and AgentAvailabilityTimer in its response, but [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) does.

## Request Syntax
<a name="API_SearchRoutingProfiles_RequestSyntax"></a>

```
POST /search-routing-profiles HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "RoutingProfileSearchCriteria"
      ],
      "OrConditions": [
         "RoutingProfileSearchCriteria"
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
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchRoutingProfiles_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchRoutingProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchRoutingProfiles_RequestSyntax) **   <a name="connect-SearchRoutingProfiles-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchRoutingProfiles_RequestSyntax) **   <a name="connect-SearchRoutingProfiles-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_SearchRoutingProfiles_RequestSyntax) **   <a name="connect-SearchRoutingProfiles-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchRoutingProfiles_RequestSyntax) **   <a name="connect-SearchRoutingProfiles-request-SearchCriteria"></a>
The search criteria to be used to return routing profiles.
The `name` and `description` fields support "contains" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.
Type: [RoutingProfileSearchCriteria](API_RoutingProfileSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchRoutingProfiles_RequestSyntax) **   <a name="connect-SearchRoutingProfiles-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [RoutingProfileSearchFilter](API_RoutingProfileSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchRoutingProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "RoutingProfiles": [
      {
         "AgentAvailabilityTimer": "string",
         "AssociatedManualAssignmentQueueIds": [ "string" ],
         "AssociatedQueueIds": [ "string" ],
         "DefaultOutboundQueueId": "string",
         "Description": "string",
         "InstanceId": "string",
         "IsDefault": boolean,
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "MediaConcurrencies": [
            {
               "Channel": "string",
               "Concurrency": number,
               "CrossChannelBehavior": {
                  "BehaviorType": "string"
               },
               "WorkloadTypeConcurrencies": [
                  {
                     "Concurrency": number,
                     "CrossChannelWorkloadBehavior": {
                        "ChannelWorkloadBehaviorType": "string"
                     },
                     "WorkloadType": "string"
                  }
               ]
            }
         ],
         "Name": "string",
         "NumberOfAssociatedManualAssignmentQueues": number,
         "NumberOfAssociatedQueues": number,
         "NumberOfAssociatedUsers": number,
         "RoutingProfileArn": "string",
         "RoutingProfileId": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchRoutingProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchRoutingProfiles_ResponseSyntax) **   <a name="connect-SearchRoutingProfiles-response-ApproximateTotalCount"></a>
The total number of routing profiles which matched your search query.
Type: Long

 ** [NextToken](#API_SearchRoutingProfiles_ResponseSyntax) **   <a name="connect-SearchRoutingProfiles-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [RoutingProfiles](#API_SearchRoutingProfiles_ResponseSyntax) **   <a name="connect-SearchRoutingProfiles-response-RoutingProfiles"></a>
Information about the routing profiles.
Type: Array of [RoutingProfile](API_RoutingProfile.md) objects

## Errors
<a name="API_SearchRoutingProfiles_Errors"></a>

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
<a name="API_SearchRoutingProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchRoutingProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchRoutingProfiles)
