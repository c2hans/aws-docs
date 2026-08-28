---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

Updates the Amazon Quick Sight settings in your AWS account.

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/settings HTTP/1.1
Content-type: application/json

{
   "DefaultNamespace": "{{string}}",
   "NotificationEmail": "{{string}}",
   "TerminationProtectionEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateAccountSettings_RequestSyntax) **   <a name="QS-UpdateAccountSettings-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the Quick Sight settings that you want to list.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAccountSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DefaultNamespace](#API_UpdateAccountSettings_RequestSyntax) **   <a name="QS-UpdateAccountSettings-request-DefaultNamespace"></a>
The default namespace for this AWS account. Currently, the default is `default`. IAM users that register for the first time with Amazon Quick Sight provide an email address that becomes associated with the default namespace.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** [NotificationEmail](#API_UpdateAccountSettings_RequestSyntax) **   <a name="QS-UpdateAccountSettings-request-NotificationEmail"></a>
The email address that you want Quick Sight to send notifications to regarding your AWS account or Quick Sight subscription.
Type: String
Required: No

 ** [TerminationProtectionEnabled](#API_UpdateAccountSettings_RequestSyntax) **   <a name="QS-UpdateAccountSettings-request-TerminationProtectionEnabled"></a>
A boolean value that determines whether or not an Quick Sight account can be deleted. A `True` value doesn't allow the account to be deleted and results in an error message if a user tries to make a `DeleteAccountSubscription` request. A `False` value will allow the account to be deleted.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="QS-UpdateAccountSettings-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="QS-UpdateAccountSettings-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

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

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
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
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
