---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetAttributes.html
---

# UpdateFleetAttributes
<a name="API_UpdateFleetAttributes"></a>

 **This API works with the following fleet types:** EC2, Anywhere

Updates a fleet's mutable attributes, such as game session protection and resource creation limits.

To update fleet attributes, specify the fleet ID and the property values that you want to change. If successful, Amazon GameLift Servers returns the identifiers for the updated fleet.

**Note**
A managed fleet's runtime environment, which depends on the fleet's Amazon Machine Image {AMI} version, can't be updated. You must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see [ Security best practices for Amazon GameLift Servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html).

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_UpdateFleetAttributes_RequestSyntax"></a>

```
{
   "AnywhereConfiguration": {
      "Cost": "{{string}}"
   },
   "Description": "{{string}}",
   "FleetId": "{{string}}",
   "MetricGroups": [ "{{string}}" ],
   "Name": "{{string}}",
   "NewGameSessionProtectionPolicy": "{{string}}",
   "ResourceCreationLimitPolicy": {
      "NewGameSessionsPerCreator": {{number}},
      "PolicyPeriodInMinutes": {{number}}
   }
}
```

## Request Parameters
<a name="API_UpdateFleetAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-FleetId"></a>
A unique identifier for the fleet to update attribute metadata for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [AnywhereConfiguration](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-AnywhereConfiguration"></a>
Amazon GameLift Servers Anywhere configuration options.
Type: [AnywhereConfiguration](API_AnywhereConfiguration.md) object
Required: No

 ** [Description](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-Description"></a>
A human-readable description of a fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [MetricGroups](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-MetricGroups"></a>
The name of a metric group to add this fleet to. Use a metric group in Amazon CloudWatch to aggregate the metrics from multiple fleets. Provide an existing metric group name, or create a new metric group by providing a new name. A fleet can only be in one metric group at a time.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Name](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-Name"></a>
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [NewGameSessionProtectionPolicy](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-NewGameSessionProtectionPolicy"></a>
The game session protection policy to apply to all new game sessions created in this fleet. Game sessions that already exist are not affected. You can set protection for individual game sessions using [UpdateGameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html) .
+  **NoProtection** -- The game session can be terminated during a scale-down event.
+  **FullProtection** -- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** [ResourceCreationLimitPolicy](#API_UpdateFleetAttributes_RequestSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-request-ResourceCreationLimitPolicy"></a>
Policy settings that limit the number of game sessions an individual player can create over a span of time.
Type: [ResourceCreationLimitPolicy](API_ResourceCreationLimitPolicy.md) object
Required: No

## Response Syntax
<a name="API_UpdateFleetAttributes_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string"
}
```

## Response Elements
<a name="API_UpdateFleetAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_UpdateFleetAttributes_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_UpdateFleetAttributes_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetAttributes-response-FleetId"></a>
A unique identifier for the fleet that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

## Errors
<a name="API_UpdateFleetAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidFleetStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFleetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateFleetAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateFleetAttributes)
