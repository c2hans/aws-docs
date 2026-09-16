---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentUserData.html
---

# GetCurrentUserData
<a name="API_GetCurrentUserData"></a>

Gets the real-time active user data from the specified Connect Customer instance.

## Request Syntax
<a name="API_GetCurrentUserData_RequestSyntax"></a>

```
POST /metrics/userdata/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "Agents": [ "{{string}}" ],
      "ContactFilter": {
         "ContactStates": [ "{{string}}" ]
      },
      "Queues": [ "{{string}}" ],
      "RoutingProfiles": [ "{{string}}" ],
      "UserHierarchyGroups": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCurrentUserData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetCurrentUserData_RequestSyntax) **   <a name="connect-GetCurrentUserData-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetCurrentUserData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetCurrentUserData_RequestSyntax) **   <a name="connect-GetCurrentUserData-request-Filters"></a>
The filters to apply to returned user data. You can filter up to the following limits:
+ Queues: 100
+ Routing profiles: 100
+ Agents: 100
+ Contact states: 9
+ User hierarchy groups: 1
 The user data is retrieved for only the specified values/resources in the filter. A maximum of one filter can be passed from queues, routing profiles, agents, and user hierarchy groups.
Currently tagging is only supported on the resources that are passed in the filter.
Type: [UserDataFilters](API_UserDataFilters.md) object
Required: Yes

 ** [MaxResults](#API_GetCurrentUserData_RequestSyntax) **   <a name="connect-GetCurrentUserData-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetCurrentUserData_RequestSyntax) **   <a name="connect-GetCurrentUserData-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_GetCurrentUserData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "UserDataList": [
      {
         "ActiveSlotsByChannel": {
            "string" : number
         },
         "AvailableSlotsByChannel": {
            "string" : number
         },
         "Contacts": [
            {
               "AgentContactState": "string",
               "Channel": "string",
               "ConnectedToAgentTimestamp": number,
               "ContactId": "string",
               "InitiationMethod": "string",
               "Queue": {
                  "Arn": "string",
                  "Id": "string"
               },
               "StateStartTimestamp": number
            }
         ],
         "HierarchyPath": {
            "LevelFive": {
               "Arn": "string",
               "Id": "string"
            },
            "LevelFour": {
               "Arn": "string",
               "Id": "string"
            },
            "LevelOne": {
               "Arn": "string",
               "Id": "string"
            },
            "LevelThree": {
               "Arn": "string",
               "Id": "string"
            },
            "LevelTwo": {
               "Arn": "string",
               "Id": "string"
            }
         },
         "MaxSlotsByChannel": {
            "string" : number
         },
         "NextStatus": "string",
         "RoutingProfile": {
            "Arn": "string",
            "Id": "string"
         },
         "Status": {
            "StatusArn": "string",
            "StatusName": "string",
            "StatusStartTimestamp": number
         },
         "User": {
            "Arn": "string",
            "Id": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetCurrentUserData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_GetCurrentUserData_ResponseSyntax) **   <a name="connect-GetCurrentUserData-response-ApproximateTotalCount"></a>
The total count of the result, regardless of the current page size.
Type: Long

 ** [NextToken](#API_GetCurrentUserData_ResponseSyntax) **   <a name="connect-GetCurrentUserData-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [UserDataList](#API_GetCurrentUserData_ResponseSyntax) **   <a name="connect-GetCurrentUserData-response-UserDataList"></a>
A list of the user data that is returned.
Type: Array of [UserData](API_UserData.md) objects

## Errors
<a name="API_GetCurrentUserData_Errors"></a>

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
<a name="API_GetCurrentUserData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetCurrentUserData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetCurrentUserData)
