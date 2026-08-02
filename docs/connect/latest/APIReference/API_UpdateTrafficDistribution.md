---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html
---

# UpdateTrafficDistribution
<a name="API_UpdateTrafficDistribution"></a>

Updates the traffic distribution for a given traffic distribution group.

**Important**
When you shift telephony traffic, also shift agents and/or agent sign-ins to ensure they can handle the calls in the other Region. If you don't shift the agents, voice calls will go to the shifted Region but there won't be any agents available to receive the calls.

**Note**
The `SignInConfig` distribution is available only on a default `TrafficDistributionGroup` (see the `IsDefault` parameter in the [TrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html) data type). If you call `UpdateTrafficDistribution` with a modified `SignInConfig` and a non-default `TrafficDistributionGroup`, an `InvalidRequestException` is returned.

For more information about updating a traffic distribution group, see [Update telephony traffic distribution across AWS Regions](https://docs.aws.amazon.com/connect/latest/adminguide/update-telephony-traffic-distribution.html) in the *Connect Customer Administrator Guide*.

 **Important things to know**
+ Invoke the UpdateTrafficDistribution API in the region that should handle traffic.

## Request Syntax
<a name="API_UpdateTrafficDistribution_RequestSyntax"></a>

```
PUT /traffic-distribution/{{Id}} HTTP/1.1
Content-type: application/json

{
   "AgentConfig": {
      "Distributions": [
         {
            "Percentage": {{number}},
            "Region": "{{string}}"
         }
      ]
   },
   "SignInConfig": {
      "Distributions": [
         {
            "Enabled": {{boolean}},
            "Region": "{{string}}"
         }
      ]
   },
   "TelephonyConfig": {
      "Distributions": [
         {
            "Percentage": {{number}},
            "Region": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateTrafficDistribution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateTrafficDistribution_RequestSyntax) **   <a name="connect-UpdateTrafficDistribution-request-uri-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateTrafficDistribution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AgentConfig](#API_UpdateTrafficDistribution_RequestSyntax) **   <a name="connect-UpdateTrafficDistribution-request-AgentConfig"></a>
The distribution of agents between the instance and its replica(s).
Type: [AgentConfig](API_AgentConfig.md) object
Required: No

 ** [SignInConfig](#API_UpdateTrafficDistribution_RequestSyntax) **   <a name="connect-UpdateTrafficDistribution-request-SignInConfig"></a>
The distribution that determines which AWS Regions should be used to sign in agents in to both the instance and its replica(s).
Type: [SignInConfig](API_SignInConfig.md) object
Required: No

 ** [TelephonyConfig](#API_UpdateTrafficDistribution_RequestSyntax) **   <a name="connect-UpdateTrafficDistribution-request-TelephonyConfig"></a>
The distribution of traffic between the instance and its replica(s).
Type: [TelephonyConfig](API_TelephonyConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateTrafficDistribution_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTrafficDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTrafficDistribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateTrafficDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateTrafficDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateTrafficDistribution)
