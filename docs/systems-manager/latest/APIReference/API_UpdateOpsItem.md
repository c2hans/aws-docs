---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateOpsItem.html
---

# UpdateOpsItem
<a name="API_UpdateOpsItem"></a>

Edit or change an OpsItem. You must have permission in AWS Identity and Access Management (IAM) to update an OpsItem. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the * AWS Systems Manager User Guide*.

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_UpdateOpsItem_RequestSyntax"></a>

```
{
   "ActualEndTime": {{number}},
   "ActualStartTime": {{number}},
   "Category": "{{string}}",
   "Description": "{{string}}",
   "Notifications": [
      {
         "Arn": "{{string}}"
      }
   ],
   "OperationalData": {
      "{{string}}" : {
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "OperationalDataToDelete": [ "{{string}}" ],
   "OpsItemArn": "{{string}}",
   "OpsItemId": "{{string}}",
   "PlannedEndTime": {{number}},
   "PlannedStartTime": {{number}},
   "Priority": {{number}},
   "RelatedOpsItems": [
      {
         "OpsItemId": "{{string}}"
      }
   ],
   "Severity": "{{string}}",
   "Status": "{{string}}",
   "Title": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateOpsItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActualEndTime](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-ActualEndTime"></a>
The time a runbook workflow ended. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [ActualStartTime](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-ActualStartTime"></a>
The time a runbook workflow started. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [Category](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Category"></a>
Specify a new category for an OpsItem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** [Description](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Description"></a>
User-defined text that contains information about the OpsItem, in Markdown format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** [Notifications](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Notifications"></a>
The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.
Type: Array of [OpsItemNotification](API_OpsItemNotification.md) objects
Required: No

 ** [OperationalData](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-OperationalData"></a>
Add new keys or edit existing key-value pairs of the OperationalData map in the OpsItem object.
Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.
Operational data keys *can't* begin with the following: `amazon`, `aws`, `amzn`, `ssm`, `/amazon`, `/aws`, `/amzn`, `/ssm`.
You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the [DescribeOpsItems](API_DescribeOpsItems.md) API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the [GetOpsItem](API_GetOpsItem.md) API operation).
Use the `/aws/resources` key in OperationalData to specify a related resource in the request. Use the `/aws/automations` key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see [Creating OpsItems manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html) in the * AWS Systems Manager User Guide*.
Type: String to [OpsItemDataValue](API_OpsItemDataValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** [OperationalDataToDelete](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-OperationalDataToDelete"></a>
Keys that you want to remove from the OperationalData map.
Type: Array of strings
Required: No

 ** [OpsItemArn](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-OpsItemArn"></a>
The OpsItem Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[0-9]{12}:opsitem.*`
Required: No

 ** [OpsItemId](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-OpsItemId"></a>
The ID of the OpsItem.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

 ** [PlannedEndTime](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-PlannedEndTime"></a>
The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [PlannedStartTime](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-PlannedStartTime"></a>
The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [Priority](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Priority"></a>
The importance of this OpsItem in relation to other OpsItems in the system.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [RelatedOpsItems](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-RelatedOpsItems"></a>
One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.
Type: Array of [RelatedOpsItem](API_RelatedOpsItem.md) objects
Required: No

 ** [Severity](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Severity"></a>
Specify a new severity for an OpsItem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** [Status](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Status"></a>
The OpsItem status. For more information, see [Editing OpsItem details](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `Open | InProgress | Resolved | Pending | TimedOut | Cancelling | Cancelled | Failed | CompletedWithSuccess | CompletedWithFailure | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | PendingApproval | Approved | Revoked | Rejected | Closed`
Required: No

 ** [Title](#API_UpdateOpsItem_RequestSyntax) **   <a name="systemsmanager-UpdateOpsItem-request-Title"></a>
A short heading that describes the nature of the OpsItem and the impacted resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

## Response Elements
<a name="API_UpdateOpsItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateOpsItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemAccessDeniedException **
You don't have permission to view OpsItems in the specified account. Verify that your account is configured either as a Systems Manager delegated administrator or that you are logged into the AWS Organizations management account.
HTTP Status Code: 400

 ** OpsItemAlreadyExistsException **
The OpsItem already exists.
HTTP Status Code: 400

 ** OpsItemConflictException **
The specified OpsItem is in the process of being deleted.
HTTP Status Code: 400

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

 ** OpsItemLimitExceededException **
The request caused OpsItems to exceed one or more quotas.
HTTP Status Code: 400

 ** OpsItemNotFoundException **
The specified OpsItem ID doesn't exist. Verify the ID and try again.
HTTP Status Code: 400

## Examples
<a name="API_UpdateOpsItem_Examples"></a>

### Example
<a name="API_UpdateOpsItem_Example_1"></a>

This example illustrates one usage of UpdateOpsItem.

#### Sample Request
<a name="API_UpdateOpsItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateOpsItem
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T184738Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 54

{
    "Status": "Resolved",
    "OpsItemId": "oi-1f050EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateOpsItem_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateOpsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateOpsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateOpsItem)
