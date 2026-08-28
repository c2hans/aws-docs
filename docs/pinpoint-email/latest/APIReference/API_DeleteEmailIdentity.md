---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.html
---

# DeleteEmailIdentity
<a name="API_DeleteEmailIdentity"></a>

Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.

## Request Syntax
<a name="API_DeleteEmailIdentity_RequestSyntax"></a>

```
DELETE /v1/email/identities/{{EmailIdentity}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEmailIdentity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_DeleteEmailIdentity_RequestSyntax) **   <a name="pinpoint-DeleteEmailIdentity-request-uri-EmailIdentity"></a>
The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
Required: Yes

## Request Body
<a name="API_DeleteEmailIdentity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEmailIdentity_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteEmailIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEmailIdentity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** ConcurrentModificationException **
The resource is being modified by another operation or thread.
HTTP Status Code: 500

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_DeleteEmailIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/DeleteEmailIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DeleteEmailIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
