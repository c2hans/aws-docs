---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html
---

# CreateTrafficDistributionGroup
<a name="API_CreateTrafficDistributionGroup"></a>

Creates a traffic distribution group given an Connect Customer instance that has been replicated.

**Note**
The `SignInConfig` distribution is available only on a default `TrafficDistributionGroup` (see the `IsDefault` parameter in the [TrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html) data type). If you call `UpdateTrafficDistribution` with a modified `SignInConfig` and a non-default `TrafficDistributionGroup`, an `InvalidRequestException` is returned.

For more information about creating traffic distribution groups, see [Set up traffic distribution groups](https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_CreateTrafficDistributionGroup_RequestSyntax"></a>

```
PUT /traffic-distribution-group HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "InstanceId": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateTrafficDistributionGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrafficDistributionGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateTrafficDistributionGroup_RequestSyntax) **   <a name="connect-CreateTrafficDistributionGroup-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_CreateTrafficDistributionGroup_RequestSyntax) **   <a name="connect-CreateTrafficDistributionGroup-request-Description"></a>
A description for the traffic distribution group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(^[\S].*[\S]$)|(^[\S]$)`
Required: No

 ** [InstanceId](#API_CreateTrafficDistributionGroup_RequestSyntax) **   <a name="connect-CreateTrafficDistributionGroup-request-InstanceId"></a>
The identifier of the Connect Customer instance that has been replicated. You can find the `instanceId` in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [Name](#API_CreateTrafficDistributionGroup_RequestSyntax) **   <a name="connect-CreateTrafficDistributionGroup-request-Name"></a>
The name for the traffic distribution group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[\S].*[\S]$)|(^[\S]$)`
Required: Yes

 ** [Tags](#API_CreateTrafficDistributionGroup_RequestSyntax) **   <a name="connect-CreateTrafficDistributionGroup-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateTrafficDistributionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateTrafficDistributionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateTrafficDistributionGroup_ResponseSyntax) **   <a name="connect-CreateTrafficDistributionGroup-response-Arn"></a>
The Amazon Resource Name (ARN) of the traffic distribution group.
Type: String
Pattern: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [Id](#API_CreateTrafficDistributionGroup_ResponseSyntax) **   <a name="connect-CreateTrafficDistributionGroup-response-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

## Errors
<a name="API_CreateTrafficDistributionGroup_Errors"></a>

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

 ** ResourceNotReadyException **
The resource is not ready.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateTrafficDistributionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateTrafficDistributionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateTrafficDistributionGroup)
