---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html
---

# BatchImportEvidenceToAssessmentControl
<a name="API_BatchImportEvidenceToAssessmentControl"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Adds one or more pieces of evidence to a control in an Audit Manager assessment.

You can import manual evidence from any S3 bucket by specifying the S3 URI of the object. You can also upload a file from your browser, or enter plain text in response to a risk assessment question.

The following restrictions apply to this action:
+  `manualEvidence` can be only one of the following: `evidenceFileName`, `s3ResourcePath`, or `textResponse`
+ Maximum size of an individual evidence file: 100 MB
+ Number of daily manual evidence uploads per control: 100
+ Supported file formats: See [Supported file types for manual evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files) in the * AWS Audit Manager User Guide*

For more information about Audit Manager service restrictions, see [Quotas and restrictions for AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html).

## Request Syntax
<a name="API_BatchImportEvidenceToAssessmentControl_RequestSyntax"></a>

```
POST /assessments/{{assessmentId}}/controlSets/{{controlSetId}}/controls/{{controlId}}/evidence HTTP/1.1
Content-type: application/json

{
   "manualEvidence": [
      {
         "evidenceFileName": "{{string}}",
         "s3ResourcePath": "{{string}}",
         "textResponse": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchImportEvidenceToAssessmentControl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_BatchImportEvidenceToAssessmentControl_RequestSyntax) **   <a name="auditmanager-BatchImportEvidenceToAssessmentControl-request-uri-assessmentId"></a>
 The identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [controlId](#API_BatchImportEvidenceToAssessmentControl_RequestSyntax) **   <a name="auditmanager-BatchImportEvidenceToAssessmentControl-request-uri-controlId"></a>
 The identifier for the control.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [controlSetId](#API_BatchImportEvidenceToAssessmentControl_RequestSyntax) **   <a name="auditmanager-BatchImportEvidenceToAssessmentControl-request-uri-controlSetId"></a>
 The identifier for the control set.
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: Yes

## Request Body
<a name="API_BatchImportEvidenceToAssessmentControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [manualEvidence](#API_BatchImportEvidenceToAssessmentControl_RequestSyntax) **   <a name="auditmanager-BatchImportEvidenceToAssessmentControl-request-manualEvidence"></a>
 The list of manual evidence objects.
Type: Array of [ManualEvidence](API_ManualEvidence.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchImportEvidenceToAssessmentControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "manualEvidence": {
            "evidenceFileName": "string",
            "s3ResourcePath": "string",
            "textResponse": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchImportEvidenceToAssessmentControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchImportEvidenceToAssessmentControl_ResponseSyntax) **   <a name="auditmanager-BatchImportEvidenceToAssessmentControl-response-errors"></a>
 A list of errors that the `BatchImportEvidenceToAssessmentControl` API returned.
Type: Array of [BatchImportEvidenceToAssessmentControlError](API_BatchImportEvidenceToAssessmentControlError.md) objects

## Errors
<a name="API_BatchImportEvidenceToAssessmentControl_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_BatchImportEvidenceToAssessmentControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)
