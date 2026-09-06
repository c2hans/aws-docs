---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html
---

# DescribeRoutingProfile
<a name="API_DescribeRoutingProfile"></a>

Describes the specified routing profile.

**Note**
 `DescribeRoutingProfile` does not populate AssociatedQueueIds in its response. The example Response Syntax shown on this page is incorrect; we are working to update it. [SearchRoutingProfiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) does include AssociatedQueueIds.

## Request Syntax
<a name="API_DescribeRoutingProfile_RequestSyntax"></a>

```
GET /routing-profiles/{{InstanceId}}/{{RoutingProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRoutingProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeRoutingProfile_RequestSyntax) **   <a name="connect-DescribeRoutingProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [RoutingProfileId](#API_DescribeRoutingProfile_RequestSyntax) **   <a name="connect-DescribeRoutingProfile-request-uri-RoutingProfileId"></a>
The identifier of the routing profile.
Required: Yes

## Request Body
<a name="API_DescribeRoutingProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRoutingProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RoutingProfile": {
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
            }
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
}
```

## Response Elements
<a name="API_DescribeRoutingProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RoutingProfile](#API_DescribeRoutingProfile_ResponseSyntax) **   <a name="connect-DescribeRoutingProfile-response-RoutingProfile"></a>
The routing profile.
Type: [RoutingProfile](API_RoutingProfile.md) object

## Errors
<a name="API_DescribeRoutingProfile_Errors"></a>

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
<a name="API_DescribeRoutingProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeRoutingProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeRoutingProfile)
