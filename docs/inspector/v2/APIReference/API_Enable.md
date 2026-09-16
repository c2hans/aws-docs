---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Enable.html
---

# Enable
<a name="API_Enable"></a>

Enables Amazon Inspector scans for one or more AWS accounts.

## Request Syntax
<a name="API_Enable_RequestSyntax"></a>

```
POST /enable HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "resourceTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_Enable_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_Enable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_Enable_RequestSyntax) **   <a name="inspector2-Enable-request-accountIds"></a>
A list of account IDs you want to enable Amazon Inspector scans for.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** [clientToken](#API_Enable_RequestSyntax) **   <a name="inspector2-Enable-request-clientToken"></a>
The idempotency token for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [resourceTypes](#API_Enable_RequestSyntax) **   <a name="inspector2-Enable-request-resourceTypes"></a>
The resource scan types you want to enable.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `EC2 | ECR | LAMBDA | LAMBDA_CODE | CODE_REPOSITORY`
Required: Yes

## Response Syntax
<a name="API_Enable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accounts": [
      {
         "accountId": "string",
         "resourceStatus": {
            "codeRepository": "string",
            "ec2": "string",
            "ecr": "string",
            "lambda": "string",
            "lambdaCode": "string"
         },
         "status": "string"
      }
   ],
   "failedAccounts": [
      {
         "accountId": "string",
         "errorCode": "string",
         "errorMessage": "string",
         "resourceStatus": {
            "codeRepository": "string",
            "ec2": "string",
            "ecr": "string",
            "lambda": "string",
            "lambdaCode": "string"
         },
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_Enable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accounts](#API_Enable_ResponseSyntax) **   <a name="inspector2-Enable-response-accounts"></a>
Information on the accounts that have had Amazon Inspector scans successfully enabled. Details are provided for each account.
Type: Array of [Account](API_Account.md) objects

 ** [failedAccounts](#API_Enable_ResponseSyntax) **   <a name="inspector2-Enable-response-failedAccounts"></a>
Information on any accounts for which Amazon Inspector scans could not be enabled. Details are provided for each account.
Type: Array of [FailedAccount](API_FailedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_Enable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_Enable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/Enable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/Enable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Enable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/Enable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Enable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/Enable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/Enable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/Enable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/Enable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Enable)
