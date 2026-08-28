---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html
---

# BatchUpdateMemberEc2DeepInspectionStatus
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus"></a>

Activates or deactivates Amazon Inspector deep inspection for the provided member accounts in your organization. You must be the delegated administrator of an organization in Amazon Inspector to use this API.

## Request Syntax
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_RequestSyntax"></a>

```
POST /ec2deepinspectionstatus/member/batch/update HTTP/1.1
Content-type: application/json

{
   "accountIds": [
      {
         "accountId": "{{string}}",
         "activateDeepInspection": {{boolean}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_BatchUpdateMemberEc2DeepInspectionStatus_RequestSyntax) **   <a name="inspector2-BatchUpdateMemberEc2DeepInspectionStatus-request-accountIds"></a>
The unique identifiers for the AWS accounts to change Amazon Inspector deep inspection status for.
Type: Array of [MemberAccountEc2DeepInspectionStatus](API_MemberAccountEc2DeepInspectionStatus.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_ResponseSyntax"></a>

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
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountIds](#API_BatchUpdateMemberEc2DeepInspectionStatus_ResponseSyntax) **   <a name="inspector2-BatchUpdateMemberEc2DeepInspectionStatus-response-accountIds"></a>
An array of objects that provide details for each of the accounts that Amazon Inspector deep inspection status was successfully changed for.
Type: Array of [MemberAccountEc2DeepInspectionStatusState](API_MemberAccountEc2DeepInspectionStatusState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [failedAccountIds](#API_BatchUpdateMemberEc2DeepInspectionStatus_ResponseSyntax) **   <a name="inspector2-BatchUpdateMemberEc2DeepInspectionStatus-response-failedAccountIds"></a>
An array of objects that provide details for each of the accounts that Amazon Inspector deep inspection status could not be successfully changed for.
Type: Array of [FailedMemberAccountEc2DeepInspectionStatusState](API_FailedMemberAccountEc2DeepInspectionStatusState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_Errors"></a>

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
<a name="API_BatchUpdateMemberEc2DeepInspectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchUpdateMemberEc2DeepInspectionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
