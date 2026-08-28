---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetAccountStatus.html
---

# BatchGetAccountStatus
<a name="API_BatchGetAccountStatus"></a>

Retrieves the Amazon Inspector status of multiple AWS accounts within your environment.

## Request Syntax
<a name="API_BatchGetAccountStatus_RequestSyntax"></a>

```
POST /status/batch/get HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetAccountStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetAccountStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_BatchGetAccountStatus_RequestSyntax) **   <a name="inspector2-BatchGetAccountStatus-request-accountIds"></a>
The 12-digit AWS account IDs of the accounts to retrieve Amazon Inspector status for.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_BatchGetAccountStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accounts": [
      {
         "accountId": "string",
         "resourceState": {
            "codeRepository": {
               "errorCode": "string",
               "errorMessage": "string",
               "status": "string"
            },
            "ec2": {
               "errorCode": "string",
               "errorMessage": "string",
               "status": "string"
            },
            "ecr": {
               "errorCode": "string",
               "errorMessage": "string",
               "status": "string"
            },
            "lambda": {
               "errorCode": "string",
               "errorMessage": "string",
               "status": "string"
            },
            "lambdaCode": {
               "errorCode": "string",
               "errorMessage": "string",
               "status": "string"
            }
         },
         "state": {
            "errorCode": "string",
            "errorMessage": "string",
            "status": "string"
         }
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
<a name="API_BatchGetAccountStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accounts](#API_BatchGetAccountStatus_ResponseSyntax) **   <a name="inspector2-BatchGetAccountStatus-response-accounts"></a>
An array of objects that provide details on the status of Amazon Inspector for each of the requested accounts.
Type: Array of [AccountState](API_AccountState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [failedAccounts](#API_BatchGetAccountStatus_ResponseSyntax) **   <a name="inspector2-BatchGetAccountStatus-response-failedAccounts"></a>
An array of objects detailing any accounts that failed to enable Amazon Inspector and why.
Type: Array of [FailedAccount](API_FailedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_BatchGetAccountStatus_Errors"></a>

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
<a name="API_BatchGetAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchGetAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchGetAccountStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
