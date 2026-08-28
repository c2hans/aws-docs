---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKeyRegistration.html
---

# UpdateKeyRegistration
<a name="API_UpdateKeyRegistration"></a>

Updates a customer managed key in a Quick Sight account.

## Request Syntax
<a name="API_UpdateKeyRegistration_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/key-registration HTTP/1.1
Content-type: application/json

{
   "KeyRegistration": [
      {
         "DefaultKey": {{boolean}},
         "KeyArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateKeyRegistration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateKeyRegistration_RequestSyntax) **   <a name="QS-UpdateKeyRegistration-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the customer managed key registration that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateKeyRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyRegistration](#API_UpdateKeyRegistration_RequestSyntax) **   <a name="QS-UpdateKeyRegistration-request-KeyRegistration"></a>
A list of `RegisteredCustomerManagedKey` objects to be updated to the Quick Sight account.
Type: Array of [RegisteredCustomerManagedKey](API_RegisteredCustomerManagedKey.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateKeyRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailedKeyRegistration": [
      {
         "KeyArn": "string",
         "Message": "string",
         "SenderFault": boolean,
         "StatusCode": number
      }
   ],
   "RequestId": "string",
   "SuccessfulKeyRegistration": [
      {
         "KeyArn": "string",
         "StatusCode": number
      }
   ]
}
```

## Response Elements
<a name="API_UpdateKeyRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedKeyRegistration](#API_UpdateKeyRegistration_ResponseSyntax) **   <a name="QS-UpdateKeyRegistration-response-FailedKeyRegistration"></a>
A list of all customer managed key registrations that failed to update.
Type: Array of [FailedKeyRegistrationEntry](API_FailedKeyRegistrationEntry.md) objects

 ** [RequestId](#API_UpdateKeyRegistration_ResponseSyntax) **   <a name="QS-UpdateKeyRegistration-response-RequestId"></a>
The AWS request ID for this operation.
Type: String
Pattern: `.*\S.*`

 ** [SuccessfulKeyRegistration](#API_UpdateKeyRegistration_ResponseSyntax) **   <a name="QS-UpdateKeyRegistration-response-SuccessfulKeyRegistration"></a>
A list of all customer managed key registrations that were successfully updated.
Type: Array of [SuccessfulKeyRegistrationEntry](API_SuccessfulKeyRegistrationEntry.md) objects

## Errors
<a name="API_UpdateKeyRegistration_Errors"></a>

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

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateKeyRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateKeyRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateKeyRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
