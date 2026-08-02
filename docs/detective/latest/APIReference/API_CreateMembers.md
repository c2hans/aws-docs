---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateMembers.html
---

# CreateMembers
<a name="API_CreateMembers"></a>

 `CreateMembers` is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses `CreateMembers` to enable organization accounts as member accounts.

For invited accounts, `CreateMembers` sends a request to invite the specified AWS accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph.

 `CreateMembers` verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.

For organization accounts in the organization behavior graph, `CreateMembers` attempts to enable the accounts. The organization accounts do not receive invitations.

The request provides the behavior graph ARN and the list of accounts to invite or to enable.

The response separates the requested accounts into two lists:
+ The accounts that `CreateMembers` was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.
+ The accounts that `CreateMembers` was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.

## Request Syntax
<a name="API_CreateMembers_RequestSyntax"></a>

```
POST /graph/members HTTP/1.1
Content-type: application/json

{
   "Accounts": [
      {
         "AccountId": "{{string}}",
         "EmailAddress": "{{string}}"
      }
   ],
   "DisableEmailNotification": {{boolean}},
   "GraphArn": "{{string}}",
   "Message": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMembers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Accounts](#API_CreateMembers_RequestSyntax) **   <a name="detective-CreateMembers-request-Accounts"></a>
The list of AWS accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the AWS account root user email address. For organization accounts in the organization behavior graph, the email address is not required.
Type: Array of [Account](API_Account.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** [DisableEmailNotification](#API_CreateMembers_RequestSyntax) **   <a name="detective-CreateMembers-request-DisableEmailNotification"></a>
if set to `true`, then the invited accounts do not receive email notifications. By default, this is set to `false`, and the invited accounts receive email notifications.
Organization accounts in the organization behavior graph do not receive email notifications.
Type: Boolean
Required: No

 ** [GraphArn](#API_CreateMembers_RequestSyntax) **   <a name="detective-CreateMembers-request-GraphArn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [Message](#API_CreateMembers_RequestSyntax) **   <a name="detective-CreateMembers-request-Message"></a>
Customized message text to include in the invitation email message to the invited member accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_CreateMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Members": [
      {
         "AccountId": "string",
         "AdministratorId": "string",
         "DatasourcePackageIngestStates": {
            "string" : "string"
         },
         "DisabledReason": "string",
         "EmailAddress": "string",
         "GraphArn": "string",
         "InvitationType": "string",
         "InvitedTime": "string",
         "MasterId": "string",
         "PercentOfGraphUtilization": number,
         "PercentOfGraphUtilizationUpdatedTime": "string",
         "Status": "string",
         "UpdatedTime": "string",
         "VolumeUsageByDatasourcePackage": {
            "string" : {
               "VolumeUsageInBytes": number,
               "VolumeUsageUpdateTime": "string"
            }
         },
         "VolumeUsageInBytes": number,
         "VolumeUsageUpdatedTime": "string"
      }
   ],
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "Reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Members](#API_CreateMembers_ResponseSyntax) **   <a name="detective-CreateMembers-response-Members"></a>
The set of member account invitation or enablement requests that Detective was able to process. This includes accounts that are being verified, that failed verification, and that passed verification and are being sent an invitation or are being enabled.
Type: Array of [MemberDetail](API_MemberDetail.md) objects

 ** [UnprocessedAccounts](#API_CreateMembers_ResponseSyntax) **   <a name="detective-CreateMembers-response-UnprocessedAccounts"></a>
The list of accounts for which Detective was unable to process the invitation or enablement request. For each account, the list provides the reason why the request could not be processed. The list includes accounts that are already member accounts in the behavior graph.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects

## Errors
<a name="API_CreateMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
This request cannot be completed for one of the following reasons.
+ This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.
+ This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.
 ** Resources **
The type of resource that has exceeded the service quota.
HTTP Status Code: 402

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_CreateMembers_Examples"></a>

### Example
<a name="API_CreateMembers_Example_1"></a>

This example illustrates one usage of CreateMembers.

#### Sample Request
<a name="API_CreateMembers_Example_1_Request"></a>

```
PUT /graph/members HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 442
Authorization: AUTHPARAMS
X-Amz-Date: 20200123T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
 "Accounts": [
 {
  "AccountId": "444455556666",
  "EmailAddress": "mmajor@example.com"
 },
 {
  "AccountId": "123456789012",
  "EmailAddress": "jstiles@example.com"
 }
 ],
 "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
 "Message": "This is Paul Santos. I need to add your account to the data we use for security investigation in Detective. If you have any questions, contact me at psantos@example.com."
}
```

### Example
<a name="API_CreateMembers_Example_2"></a>

This example illustrates one usage of CreateMembers.

#### Sample Response
<a name="API_CreateMembers_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 625
Date: Thu, 23 Jan 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive

{
 "Members": [
 {
  "AccountId": "444455556666",
  "AdministratorId": "111122223333",
  "EmailAddress": "mmajor@example.com",
  "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
  "InvitedTime": "2020-01-24T12:35:0.1587Z",
  "MasterId": "111122223333",
  "Status": "INVITED",
  "UpdatedTime": "2020-01-24T12:35:0.1587Z"
 },
 {
  "AccountId": "123456789012",
  "AdministratorId": "111122223333",
  "EmailAddress": "jstiles@example.com",
  "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
  "InvitedTime": "2020-01-24T12:35:0.1587Z",
  "MasterId": "111122223333",
  "Status": "VERIFICATION_IN_PROGRESS",
  "UpdatedTime": "2020-01-24T12:35:0.1587Z"
 }
 ],
 "UnprocessedAccounts": [ ]
}
```

## See Also
<a name="API_CreateMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/CreateMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/CreateMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/CreateMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/CreateMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/CreateMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/CreateMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/CreateMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/CreateMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/CreateMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/CreateMembers)
