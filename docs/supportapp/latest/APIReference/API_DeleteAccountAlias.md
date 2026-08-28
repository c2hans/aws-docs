---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteAccountAlias.html
---

# DeleteAccountAlias
<a name="API_DeleteAccountAlias"></a>

Deletes an alias for an AWS account ID. The alias appears in the Support App page of the AWS Support Center. The alias also appears in Slack messages from the Support App.

## Request Syntax
<a name="API_DeleteAccountAlias_RequestSyntax"></a>

```
POST /control/delete-account-alias HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountAlias_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAccountAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccountAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAccountAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccountAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.
HTTP Status Code: 404

## See Also
<a name="API_DeleteAccountAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/DeleteAccountAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/DeleteAccountAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support App in Slack. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportapp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
