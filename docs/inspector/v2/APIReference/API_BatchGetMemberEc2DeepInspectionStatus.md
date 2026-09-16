---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetMemberEc2DeepInspectionStatus.html
---

# BatchGetMemberEc2DeepInspectionStatus
<a name="API_BatchGetMemberEc2DeepInspectionStatus"></a>

Retrieves Amazon Inspector deep inspection activation status of multiple member accounts within your organization. You must be the delegated administrator of an organization in Amazon Inspector to use this API.

## Request Syntax
<a name="API_BatchGetMemberEc2DeepInspectionStatus_RequestSyntax"></a>

```
POST /ec2deepinspectionstatus/member/batch/get HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetMemberEc2DeepInspectionStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetMemberEc2DeepInspectionStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_BatchGetMemberEc2DeepInspectionStatus_RequestSyntax) **   <a name="inspector2-BatchGetMemberEc2DeepInspectionStatus-request-accountIds"></a>
The unique identifiers for the AWS accounts to retrieve Amazon Inspector deep inspection activation status for.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_BatchGetMemberEc2DeepInspectionStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountIds": [
      {
         "accountId": "string",
         "errorMessage": "string",
         "status": "string"
      }
   ],
   "failedAccountIds": [
      {
         "accountId": "string",
         "ec2ScanStatus": "string",
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetMemberEc2DeepInspectionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountIds](#API_BatchGetMemberEc2DeepInspectionStatus_ResponseSyntax) **   <a name="inspector2-BatchGetMemberEc2DeepInspectionStatus-response-accountIds"></a>
An array of objects that provide details on the activation status of Amazon Inspector deep inspection for each of the requested accounts.
Type: Array of [MemberAccountEc2DeepInspectionStatusState](API_MemberAccountEc2DeepInspectionStatusState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [failedAccountIds](#API_BatchGetMemberEc2DeepInspectionStatus_ResponseSyntax) **   <a name="inspector2-BatchGetMemberEc2DeepInspectionStatus-response-failedAccountIds"></a>
An array of objects that provide details on any accounts that failed to activate Amazon Inspector deep inspection and why.
Type: Array of [FailedMemberAccountEc2DeepInspectionStatusState](API_FailedMemberAccountEc2DeepInspectionStatusState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_BatchGetMemberEc2DeepInspectionStatus_Errors"></a>

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
<a name="API_BatchGetMemberEc2DeepInspectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchGetMemberEc2DeepInspectionStatus)
