---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateOpsItem.html
---

# CreateOpsItem
<a name="API_CreateOpsItem"></a>

Creates a new OpsItem. You must have permission in AWS Identity and Access Management (IAM) to create a new OpsItem. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the * AWS Systems Manager User Guide*.

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_CreateOpsItem_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
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
   "OpsItemType": "{{string}}",
   "PlannedEndTime": {{number}},
   "PlannedStartTime": {{number}},
   "Priority": {{number}},
   "RelatedOpsItems": [
      {
         "OpsItemId": "{{string}}"
      }
   ],
   "Severity": "{{string}}",
   "Source": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Title": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateOpsItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-AccountId"></a>
The target AWS account where you want to create an OpsItem. To make this call, your account must be configured to work with OpsItems across accounts. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the * AWS Systems Manager User Guide*.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** [ActualEndTime](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-ActualEndTime"></a>
The time a runbook workflow ended. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [ActualStartTime](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-ActualStartTime"></a>
The time a runbook workflow started. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [Category](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Category"></a>
Specify a category to assign to an OpsItem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** [Description](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Description"></a>
User-defined text that contains information about the OpsItem, in Markdown format.
Provide enough information so that users viewing this OpsItem for the first time understand the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** [Notifications](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Notifications"></a>
The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.
Type: Array of [OpsItemNotification](API_OpsItemNotification.md) objects
Required: No

 ** [OperationalData](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-OperationalData"></a>
Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.
Operational data keys *can't* begin with the following: `amazon`, `aws`, `amzn`, `ssm`, `/amazon`, `/aws`, `/amzn`, `/ssm`.
You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the [DescribeOpsItems](API_DescribeOpsItems.md) API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the [GetOpsItem](API_GetOpsItem.md) API operation).
Use the `/aws/resources` key in OperationalData to specify a related resource in the request. Use the `/aws/automations` key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see [Create OpsItems manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html) in the * AWS Systems Manager User Guide*.
Type: String to [OpsItemDataValue](API_OpsItemDataValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** [OpsItemType](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-OpsItemType"></a>
The type of OpsItem to create. Systems Manager supports the following types of OpsItems:
+  `/aws/issue`

  This type of OpsItem is used for default OpsItems created by OpsCenter.
+  `/aws/insight`

  This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems.
+  `/aws/changerequest`

  This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests.
**Important**
 AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html).
Type: String
Required: No

 ** [PlannedEndTime](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-PlannedEndTime"></a>
The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [PlannedStartTime](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-PlannedStartTime"></a>
The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** [Priority](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Priority"></a>
The importance of this OpsItem in relation to other OpsItems in the system.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [RelatedOpsItems](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-RelatedOpsItems"></a>
One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.
Type: Array of [RelatedOpsItem](API_RelatedOpsItem.md) objects
Required: No

 ** [Severity](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Severity"></a>
Specify a severity to assign to an OpsItem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** [Source](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Source"></a>
The origin of the OpsItem, such as Amazon EC2 or Systems Manager.
The source name can't contain the following strings: `aws`, `amazon`, and `amzn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** [Tags](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Tags"></a>
Optional metadata that you assign to a resource.
Tags use a key-value pair. For example:
 `Key=Department,Value=Finance`
To add tags to a new OpsItem, a user must have IAM permissions for both the `ssm:CreateOpsItems` operation and the `ssm:AddTagsToResource` operation. To add tags to an existing OpsItem, use the [AddTagsToResource](API_AddTagsToResource.md) operation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [Title](#API_CreateOpsItem_RequestSyntax) **   <a name="systemsmanager-CreateOpsItem-request-Title"></a>
A short heading that describes the nature of the OpsItem and the impacted resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: Yes

## Response Syntax
<a name="API_CreateOpsItem_ResponseSyntax"></a>

```
{
   "OpsItemArn": "string",
   "OpsItemId": "string"
}
```

## Response Elements
<a name="API_CreateOpsItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OpsItemArn](#API_CreateOpsItem_ResponseSyntax) **   <a name="systemsmanager-CreateOpsItem-response-OpsItemArn"></a>
The OpsItem Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[0-9]{12}:opsitem.*`

 ** [OpsItemId](#API_CreateOpsItem_ResponseSyntax) **   <a name="systemsmanager-CreateOpsItem-response-OpsItemId"></a>
The ID of the OpsItem.
Type: String

## Errors
<a name="API_CreateOpsItem_Errors"></a>

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

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

 ** OpsItemLimitExceededException **
The request caused OpsItems to exceed one or more quotas.
HTTP Status Code: 400

## Examples
<a name="API_CreateOpsItem_Examples"></a>

### Example
<a name="API_CreateOpsItem_Example_1"></a>

This example illustrates one usage of CreateOpsItem.

#### Sample Request
<a name="API_CreateOpsItem_Example_1_Request"></a>

```
POST / HTTP/1.1
 Host: ssm.us-east-2.amazonaws.com
 Accept-Encoding: identity
 X-Amz-Target: AmazonSSM.CreateOpsItem
 Content-Type: application/x-amz-json-1.1
 User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
 X-Amz-Date: 20240401T161257Z
 Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
 Content-Length: 80

 {
     "Description": "Example Ops Item",
     "Source": "SSM",
     "Title": "DocumentDeleted"
 }
```

#### Sample Response
<a name="API_CreateOpsItem_Example_1_Response"></a>

```
{{
     "OpsItemId": "oi-1f050EXAMPLE"
 }
```

## See Also
<a name="API_CreateOpsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateOpsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateOpsItem)
