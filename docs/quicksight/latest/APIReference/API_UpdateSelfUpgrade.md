---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSelfUpgrade.html
---

# UpdateSelfUpgrade
<a name="API_UpdateSelfUpgrade"></a>

Updates a self-upgrade request for a Quick user by approving, denying, or verifying the request.

## Request Syntax
<a name="API_UpdateSelfUpgrade_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/update-self-upgrade-request HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "UpgradeRequestId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSelfUpgrade_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateSelfUpgrade_RequestSyntax) **   <a name="QS-UpdateSelfUpgrade-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the self-upgrade request.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [Namespace](#API_UpdateSelfUpgrade_RequestSyntax) **   <a name="QS-UpdateSelfUpgrade-request-uri-Namespace"></a>
The Quick namespace for the self-upgrade request.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## Request Body
<a name="API_UpdateSelfUpgrade_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_UpdateSelfUpgrade_RequestSyntax) **   <a name="QS-UpdateSelfUpgrade-request-Action"></a>
The action to perform on the self-upgrade request. Valid values are `APPROVE`, `DENY`, or `VERIFY`.
Type: String
Valid Values: `APPROVE | DENY | VERIFY`
Required: Yes

 ** [UpgradeRequestId](#API_UpdateSelfUpgrade_RequestSyntax) **   <a name="QS-UpdateSelfUpgrade-request-UpgradeRequestId"></a>
The ID of the self-upgrade request to update.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateSelfUpgrade_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "SelfUpgradeRequestDetail": {
      "CreationTime": number,
      "lastUpdateAttemptTime": number,
      "lastUpdateFailureReason": "string",
      "OriginalRole": "string",
      "RequestedRole": "string",
      "RequestNote": "string",
      "RequestStatus": "string",
      "UpgradeRequestId": "string",
      "UserName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSelfUpgrade_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateSelfUpgrade_ResponseSyntax) **   <a name="QS-UpdateSelfUpgrade-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateSelfUpgrade_ResponseSyntax) **   <a name="QS-UpdateSelfUpgrade-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [SelfUpgradeRequestDetail](#API_UpdateSelfUpgrade_ResponseSyntax) **   <a name="QS-UpdateSelfUpgrade-response-SelfUpgradeRequestDetail"></a>
Details of the updated self-upgrade request.
Type: [SelfUpgradeRequestDetail](API_SelfUpgradeRequestDetail.md) object

## Errors
<a name="API_UpdateSelfUpgrade_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` value isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **
This resource is currently unavailable.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateSelfUpgrade_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateSelfUpgrade)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateSelfUpgrade)
