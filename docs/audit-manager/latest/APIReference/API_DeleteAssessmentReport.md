---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html
---

# DeleteAssessmentReport
<a name="API_DeleteAssessmentReport"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Deletes an assessment report in AWS Audit Manager.

When you run the `DeleteAssessmentReport` operation, Audit Manager attempts to delete the following data:

1. The specified assessment report that’s stored in your S3 bucket

1. The associated metadata that’s stored in Audit Manager

If Audit Manager can’t access the assessment report in your S3 bucket, the report isn’t deleted. In this event, the `DeleteAssessmentReport` operation doesn’t fail. Instead, it proceeds to delete the associated metadata only. You must then delete the assessment report from the S3 bucket yourself.

This scenario happens when Audit Manager receives a `403 (Forbidden)` or `404 (Not Found)` error from Amazon S3. To avoid this, make sure that your S3 bucket is available, and that you configured the correct permissions for Audit Manager to delete resources in your S3 bucket. For an example permissions policy that you can use, see [Assessment report destination permissions](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#full-administrator-access-assessment-report-destination) in the * AWS Audit Manager User Guide*. For information about the issues that could cause a `403 (Forbidden)` or `404 (Not Found`) error from Amazon S3, see [List of Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList) in the *Amazon Simple Storage Service API Reference*.

## Request Syntax
<a name="API_DeleteAssessmentReport_RequestSyntax"></a>

```
DELETE /assessments/{{assessmentId}}/reports/{{assessmentReportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAssessmentReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_DeleteAssessmentReport_RequestSyntax) **   <a name="auditmanager-DeleteAssessmentReport-request-uri-assessmentId"></a>
 The unique identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [assessmentReportId](#API_DeleteAssessmentReport_RequestSyntax) **   <a name="auditmanager-DeleteAssessmentReport-request-uri-assessmentReportId"></a>
 The unique identifier for the assessment report.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DeleteAssessmentReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAssessmentReport_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAssessmentReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAssessmentReport_Errors"></a>

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
<a name="API_DeleteAssessmentReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/DeleteAssessmentReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/DeleteAssessmentReport)
