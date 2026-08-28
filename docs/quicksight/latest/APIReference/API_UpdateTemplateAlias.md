---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplateAlias.html
---

# UpdateTemplateAlias
<a name="API_UpdateTemplateAlias"></a>

Updates the template alias of a template.

## Request Syntax
<a name="API_UpdateTemplateAlias_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/aliases/{{AliasName}} HTTP/1.1
Content-type: application/json

{
   "TemplateVersionNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateTemplateAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_UpdateTemplateAlias_RequestSyntax) **   <a name="QS-UpdateTemplateAlias-request-uri-AliasName"></a>
The alias of the template that you want to update. If you name a specific alias, you update the version that the alias points to. You can specify the latest version of the template by providing the keyword `$LATEST` in the `AliasName` parameter. The keyword `$PUBLISHED` doesn't apply to templates.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`
Required: Yes

 ** [AwsAccountId](#API_UpdateTemplateAlias_RequestSyntax) **   <a name="QS-UpdateTemplateAlias-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template alias that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [TemplateId](#API_UpdateTemplateAlias_RequestSyntax) **   <a name="QS-UpdateTemplateAlias-request-uri-TemplateId"></a>
The ID for the template.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateTemplateAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TemplateVersionNumber](#API_UpdateTemplateAlias_RequestSyntax) **   <a name="QS-UpdateTemplateAlias-request-TemplateVersionNumber"></a>
The version number of the template.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_UpdateTemplateAlias_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "TemplateAlias": {
      "AliasName": "string",
      "Arn": "string",
      "TemplateVersionNumber": number
   }
}
```

## Response Elements
<a name="API_UpdateTemplateAlias_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateTemplateAlias_ResponseSyntax) **   <a name="QS-UpdateTemplateAlias-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateTemplateAlias_ResponseSyntax) **   <a name="QS-UpdateTemplateAlias-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TemplateAlias](#API_UpdateTemplateAlias_ResponseSyntax) **   <a name="QS-UpdateTemplateAlias-response-TemplateAlias"></a>
The template alias.
Type: [TemplateAlias](API_TemplateAlias.md) object

## Errors
<a name="API_UpdateTemplateAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateTemplateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateTemplateAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateTemplateAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
