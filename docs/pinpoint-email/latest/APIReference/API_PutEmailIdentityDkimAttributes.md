---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.html
---

# PutEmailIdentityDkimAttributes
<a name="API_PutEmailIdentityDkimAttributes"></a>

Used to enable or disable DKIM authentication for an email identity.

## Request Syntax
<a name="API_PutEmailIdentityDkimAttributes_RequestSyntax"></a>

```
PUT /v1/email/identities/{{EmailIdentity}}/dkim HTTP/1.1
Content-type: application/json

{
   "SigningEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityDkimAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityDkimAttributes_RequestSyntax) **   <a name="pinpoint-PutEmailIdentityDkimAttributes-request-uri-EmailIdentity"></a>
The email identity that you want to change the DKIM settings for.
Required: Yes

## Request Body
<a name="API_PutEmailIdentityDkimAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SigningEnabled](#API_PutEmailIdentityDkimAttributes_RequestSyntax) **   <a name="pinpoint-PutEmailIdentityDkimAttributes-request-SigningEnabled"></a>
Sets the DKIM signing configuration for the identity.
When you set this value `true`, then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to `false`, then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.
Type: Boolean
Required: No

## Response Syntax
<a name="API_PutEmailIdentityDkimAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutEmailIdentityDkimAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEmailIdentityDkimAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutEmailIdentityDkimAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
