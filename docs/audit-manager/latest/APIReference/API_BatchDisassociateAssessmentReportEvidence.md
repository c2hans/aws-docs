---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchDisassociateAssessmentReportEvidence.html
---

# BatchDisassociateAssessmentReportEvidence
<a name="API_BatchDisassociateAssessmentReportEvidence"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Disassociates a list of evidence from an assessment report in AWS Audit Manager.

## Request Syntax
<a name="API_BatchDisassociateAssessmentReportEvidence_RequestSyntax"></a>

```
PUT /assessments/{{assessmentId}}/batchDisassociateFromAssessmentReport HTTP/1.1
Content-type: application/json

{
   "evidenceFolderId": "{{string}}",
   "evidenceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDisassociateAssessmentReportEvidence_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_BatchDisassociateAssessmentReportEvidence_RequestSyntax) **   <a name="auditmanager-BatchDisassociateAssessmentReportEvidence-request-uri-assessmentId"></a>
 The identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_BatchDisassociateAssessmentReportEvidence_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [evidenceFolderId](#API_BatchDisassociateAssessmentReportEvidence_RequestSyntax) **   <a name="auditmanager-BatchDisassociateAssessmentReportEvidence-request-evidenceFolderId"></a>
 The identifier for the folder that the evidence is stored in.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [evidenceIds](#API_BatchDisassociateAssessmentReportEvidence_RequestSyntax) **   <a name="auditmanager-BatchDisassociateAssessmentReportEvidence-request-evidenceIds"></a>
 The list of evidence identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateAssessmentReportEvidence_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "evidenceId": "string"
      }
   ],
   "evidenceIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchDisassociateAssessmentReportEvidence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDisassociateAssessmentReportEvidence_ResponseSyntax) **   <a name="auditmanager-BatchDisassociateAssessmentReportEvidence-response-errors"></a>
 A list of errors that the `BatchDisassociateAssessmentReportEvidence` API returned.
Type: Array of [AssessmentReportEvidenceError](API_AssessmentReportEvidenceError.md) objects

 ** [evidenceIds](#API_BatchDisassociateAssessmentReportEvidence_ResponseSyntax) **   <a name="auditmanager-BatchDisassociateAssessmentReportEvidence-response-evidenceIds"></a>
 The identifier for the evidence.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

## Errors
<a name="API_BatchDisassociateAssessmentReportEvidence_Errors"></a>

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
<a name="API_BatchDisassociateAssessmentReportEvidence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/BatchDisassociateAssessmentReportEvidence)
