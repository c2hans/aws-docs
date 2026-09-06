---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFreeTrialInfo.html
---

# BatchGetFreeTrialInfo
<a name="API_BatchGetFreeTrialInfo"></a>

Gets free trial status for multiple AWS accounts.

## Request Syntax
<a name="API_BatchGetFreeTrialInfo_RequestSyntax"></a>

```
POST /freetrialinfo/batchget HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetFreeTrialInfo_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetFreeTrialInfo_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_BatchGetFreeTrialInfo_RequestSyntax) **   <a name="inspector2-BatchGetFreeTrialInfo-request-accountIds"></a>
The account IDs to get free trial status for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*[0-9]{12}.*`
Required: Yes

## Response Syntax
<a name="API_BatchGetFreeTrialInfo_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accounts": [
      {
         "accountId": "string",
         "freeTrialInfo": [
            {
               "cloudProvider": "string",
               "end": number,
               "start": number,
               "status": "string",
               "type": "string"
            }
         ]
      }
   ],
   "failedAccounts": [
      {
         "accountId": "string",
         "code": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetFreeTrialInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accounts](#API_BatchGetFreeTrialInfo_ResponseSyntax) **   <a name="inspector2-BatchGetFreeTrialInfo-response-accounts"></a>
An array of objects that provide Amazon Inspector free trial details for each of the requested accounts.
Type: Array of [FreeTrialAccountInfo](API_FreeTrialAccountInfo.md) objects

 ** [failedAccounts](#API_BatchGetFreeTrialInfo_ResponseSyntax) **   <a name="inspector2-BatchGetFreeTrialInfo-response-failedAccounts"></a>
An array of objects detailing any accounts that free trial data could not be returned for.
Type: Array of [FreeTrialInfoError](API_FreeTrialInfoError.md) objects

## Errors
<a name="API_BatchGetFreeTrialInfo_Errors"></a>

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
<a name="API_BatchGetFreeTrialInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchGetFreeTrialInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchGetFreeTrialInfo)
