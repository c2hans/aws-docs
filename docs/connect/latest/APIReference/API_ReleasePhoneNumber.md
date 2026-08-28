---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReleasePhoneNumber.html
---

# ReleasePhoneNumber
<a name="API_ReleasePhoneNumber"></a>

Releases a phone number previously claimed to an Connect Customer instance or traffic distribution group. You can call this API only in the AWS Region where the number was claimed.

**Important**
To release phone numbers from a traffic distribution group, use the `ReleasePhoneNumber` API, not the Connect Customer admin website.
After releasing a phone number, the phone number enters into a cooldown period for up to 180 days. It cannot be searched for or claimed again until the period has ended. If you accidentally release a phone number, contact Support.

If you plan to claim and release numbers frequently, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until up to 180 days past the oldest number released has expired.

By default you can claim and release up to 200% of your maximum number of active phone numbers. If you claim and release phone numbers using the UI or API during a rolling 180 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 180 days past the oldest number released has expired.

For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 180 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an AWS support ticket.

## Request Syntax
<a name="API_ReleasePhoneNumber_RequestSyntax"></a>

```
DELETE /phone-number/{{PhoneNumberId}}?clientToken={{ClientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ReleasePhoneNumber_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_ReleasePhoneNumber_RequestSyntax) **   <a name="connect-ReleasePhoneNumber-request-uri-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Length Constraints: Maximum length of 500.

 ** [PhoneNumberId](#API_ReleasePhoneNumber_RequestSyntax) **   <a name="connect-ReleasePhoneNumber-request-uri-PhoneNumberId"></a>
A unique identifier for the phone number.
Required: Yes

## Request Body
<a name="API_ReleasePhoneNumber_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ReleasePhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ReleasePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ReleasePhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

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

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
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
<a name="API_ReleasePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ReleasePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReleasePhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
