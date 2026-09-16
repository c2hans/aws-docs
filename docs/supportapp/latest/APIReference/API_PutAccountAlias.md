---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_PutAccountAlias.html
---

# PutAccountAlias
<a name="API_PutAccountAlias"></a>

Creates or updates an individual alias for each AWS account ID. The alias appears in the Support App page of the AWS Support Center. The alias also appears in Slack messages from the Support App.

## Request Syntax
<a name="API_PutAccountAlias_RequestSyntax"></a>

```
POST /control/put-account-alias HTTP/1.1
Content-type: application/json

{
   "accountAlias": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAccountAlias_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountAlias](#API_PutAccountAlias_RequestSyntax) **   <a name="supportapp-PutAccountAlias-request-accountAlias"></a>
An alias or short name for an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[\w\- ]+`
Required: Yes

## Response Syntax
<a name="API_PutAccountAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** ValidationException **
Your request input doesn't meet the constraints that the Support App specifies.
HTTP Status Code: 400

## See Also
<a name="API_PutAccountAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/PutAccountAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/PutAccountAlias)
