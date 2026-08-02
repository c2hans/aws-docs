---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRcsAgents.html
---

# DescribeRcsAgents
<a name="API_DescribeRcsAgents"></a>

Retrieves the specified RCS agents or all RCS agents associated with your AWS account.

If you specify RCS agent IDs, the output includes information for only the specified RCS agents. If you specify filters, the output includes information for only those RCS agents that meet the filter criteria. If you don't specify RCS agent IDs or filters, the output includes information for all RCS agents.

## Request Syntax
<a name="API_DescribeRcsAgents_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Owner": "{{string}}",
   "RcsAgentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRcsAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRcsAgents_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgents-request-Filters"></a>
An array of RcsAgentFilter objects to filter the results.
Type: Array of [RcsAgentFilter](API_RcsAgentFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeRcsAgents_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgents-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRcsAgents_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgents-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [Owner](#API_DescribeRcsAgents_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgents-request-Owner"></a>
Use `SELF` to filter the list of RCS agents to ones your account owns or use `SHARED` to filter on RCS agents shared with your account. The `Owner` and `RcsAgentIds` parameters can't be used at the same time.
Type: String
Valid Values: `SELF | SHARED`
Required: No

 ** [RcsAgentIds](#API_DescribeRcsAgents_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgents-request-RcsAgentIds"></a>
An array of unique identifiers for the RCS agents. This is an array of strings that can be either the RcsAgentId or RcsAgentArn.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## Response Syntax
<a name="API_DescribeRcsAgents_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RcsAgents": [
      {
         "CreatedTimestamp": number,
         "DeletionProtectionEnabled": boolean,
         "OptOutListName": "string",
         "PoolId": "string",
         "RcsAgentArn": "string",
         "RcsAgentId": "string",
         "SelfManagedOptOutsEnabled": boolean,
         "Status": "string",
         "TestingAgent": {
            "RegistrationId": "string",
            "Status": "string",
            "TestingAgentId": "string"
         },
         "TwoWayChannelArn": "string",
         "TwoWayChannelRole": "string",
         "TwoWayEnabled": boolean,
         "TwoWayMediaS3BucketName": "string",
         "TwoWayMediaS3KeyPrefix": "string",
         "TwoWayMediaS3Role": "string",
         "TwoWayRcsEventsEnabled": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRcsAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRcsAgents_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgents-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RcsAgents](#API_DescribeRcsAgents_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgents-response-RcsAgents"></a>
An array of RcsAgentInformation objects that contain the details for the requested RCS agents.
Type: Array of [RcsAgentInformation](API_RcsAgentInformation.md) objects

## Errors
<a name="API_DescribeRcsAgents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRcsAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgents)
