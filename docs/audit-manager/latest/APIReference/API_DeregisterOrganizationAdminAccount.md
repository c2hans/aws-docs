---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterOrganizationAdminAccount.html
---

# DeregisterOrganizationAdminAccount
<a name="API_DeregisterOrganizationAdminAccount"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Removes the specified AWS account as a delegated administrator for AWS Audit Manager.

When you remove a delegated administrator from your Audit Manager settings, you continue to have access to the evidence that you previously collected under that account. This is also the case when you deregister a delegated administrator from AWS Organizations. However, Audit Manager stops collecting and attaching evidence to that delegated administrator account moving forward.

**Important**
Keep in mind the following cleanup task if you use evidence finder:
Before you use your management account to remove a delegated administrator, make sure that the current delegated administrator account signs in to Audit Manager and disables evidence finder first. Disabling evidence finder automatically deletes the event data store that was created in their account when they enabled evidence finder. If this task isn’t completed, the event data store remains in their account. In this case, we recommend that the original delegated administrator goes to CloudTrail Lake and manually [deletes the event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-disable-termination.html).
This cleanup task is necessary to ensure that you don't end up with multiple event data stores. Audit Manager ignores an unused event data store after you remove or change a delegated administrator account. However, the unused event data store continues to incur storage costs from CloudTrail Lake if you don't delete it.

When you deregister a delegated administrator account for Audit Manager, the data for that account isn’t deleted. If you want to delete resource data for a delegated administrator account, you must perform that task separately before you deregister the account. Either, you can do this in the Audit Manager console. Or, you can use one of the delete API operations that are provided by Audit Manager.

To delete your Audit Manager resource data, see the following instructions:
+  [DeleteAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html) (see also: [Deleting an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html) in the * AWS Audit Manager User Guide*)
+  [DeleteAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html) (see also: [Deleting a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html) in the * AWS Audit Manager User Guide*)
+  [DeleteAssessmentFrameworkShare](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html) (see also: [Deleting a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/deleting-shared-framework-requests.html) in the * AWS Audit Manager User Guide*)
+  [DeleteAssessmentReport](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html) (see also: [Deleting an assessment report](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#delete-assessment-report-steps) in the * AWS Audit Manager User Guide*)
+  [DeleteControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html) (see also: [Deleting a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html) in the * AWS Audit Manager User Guide*)

At this time, Audit Manager doesn't provide an option to delete evidence for a specific delegated administrator. Instead, when your management account deregisters Audit Manager, we perform a cleanup for the current delegated administrator account at the time of deregistration.

## Request Syntax
<a name="API_DeregisterOrganizationAdminAccount_RequestSyntax"></a>

```
POST /account/deregisterOrganizationAdminAccount HTTP/1.1
Content-type: application/json

{
   "adminAccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeregisterOrganizationAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeregisterOrganizationAdminAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [adminAccountId](#API_DeregisterOrganizationAdminAccount_RequestSyntax) **   <a name="auditmanager-DeregisterOrganizationAdminAccount-request-adminAccountId"></a>
 The identifier for the administrator account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

## Response Syntax
<a name="API_DeregisterOrganizationAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeregisterOrganizationAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterOrganizationAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterOrganizationAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/DeregisterOrganizationAdminAccount)
