---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_GetAccountAlias.html
---

# GetAccountAlias
<a name="API_GetAccountAlias"></a>

Retrieves the alias from an AWS account ID. The alias appears in the Support App page of the AWS Support Center. The alias also appears in Slack messages from the Support App.

## Request Syntax
<a name="API_GetAccountAlias_RequestSyntax"></a>

```
POST /control/get-account-alias HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountAlias_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountAlias": "string"
}
```

## Response Elements
<a name="API_GetAccountAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountAlias](#API_GetAccountAlias_ResponseSyntax) **   <a name="supportapp-GetAccountAlias-response-accountAlias"></a>
An alias or short name for an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[\w\- ]+`

## Errors
<a name="API_GetAccountAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_GetAccountAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/GetAccountAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/GetAccountAlias)
