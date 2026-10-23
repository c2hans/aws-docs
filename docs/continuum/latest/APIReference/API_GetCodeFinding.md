---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeFinding.html
---

# GetCodeFinding
<a name="API_GetCodeFinding"></a>

Retrieves the current state and details of a finding.

## Request Syntax
<a name="API_GetCodeFinding_RequestSyntax"></a>

```
GET /environments/{{environmentId}}/code-findings/{{findingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodeFinding_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetCodeFinding_RequestSyntax) **   <a name="continuum-GetCodeFinding-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [findingId](#API_GetCodeFinding_RequestSyntax) **   <a name="continuum-GetCodeFinding-request-uri-findingId"></a>
The identifier of the finding.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetCodeFinding_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodeFinding_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "affectedPackages": [
      {
         "fixedInVersion": "string",
         "name": "string",
         "packageManager": "string",
         "version": "string"
      }
   ],
   "category": "string",
   "completedAt": "string",
   "createdAt": "string",
   "createdIssueId": "string",
   "cveId": "string",
   "cvssBaseScore": number,
   "cweIds": [ "string" ],
   "detailedDescription": "string",
   "discardReason": "string",
   "discardReasoning": "string",
   "duplicateOfIssueId": "string",
   "endLine": number,
   "environmentId": "string",
   "filePath": "string",
   "findingArn": "string",
   "findingId": "string",
   "findingTypes": [ "string" ],
   "firstSeenAt": "string",
   "lineNumber": number,
   "mitigation": "string",
   "mitreTechniques": [ "string" ],
   "ocsfClass": "string",
   "ocsfSchemaVersion": "string",
   "owaspCategory": "string",
   "posture": {
      "application": "string",
      "applicationUid": "string",
      "applicationVersion": "string",
      "checks": [
         {
            "description": "string",
            "name": "string",
            "uid": "string"
         }
      ],
      "control": "string",
      "description": "string",
      "remediation": "string",
      "remediationReferences": [ "string" ],
      "requirements": [ "string" ],
      "standards": [ "string" ],
      "status": "string",
      "statusId": number
   },
   "productName": "string",
   "productVendorName": "string",
   "productVersion": "string",
   "relevantInputs": [ "string" ],
   "remediationReferences": [ "string" ],
   "reportedAt": "string",
   "resources": [
      {
         "name": "string",
         "region": "string",
         "type": "string",
         "uid": "string"
      }
   ],
   "scanRunId": "string",
   "severity": "string",
   "source": "string",
   "sourceFindingId": "string",
   "sourceStatus": "string",
   "sourceStatusId": number,
   "status": "string",
   "statusMessage": "string",
   "statusUpdatedAt": "string",
   "stepsToReproduce": [ "string" ],
   "subCategory": "string",
   "summary": "string",
   "title": "string",
   "type": "string",
   "validation": {
      "blockingReason": "string",
      "confidence": number,
      "evidence": [
         {
            "file": "string",
            "line": number,
            "snippet": "string"
         }
      ],
      "mitigatingControls": [ "string" ],
      "preconditions": [ "string" ],
      "rationale": "string",
      "severityAdjustment": "string",
      "verdict": "string"
   },
   "vulnerabilities": [
      {
         "additionalCweIds": [ "string" ],
         "affectedPackages": [
            {
               "fixedInVersion": "string",
               "name": "string",
               "packageManager": "string",
               "version": "string"
            }
         ],
         "code": "string",
         "cveId": "string",
         "cvssBaseScore": number,
         "cweCaption": "string",
         "cweId": "string",
         "description": "string",
         "details": "string",
         "fixCoverage": "string",
         "fixCoverageId": number,
         "locations": [
            {
               "endLine": number,
               "filePath": "string",
               "startLine": number
            }
         ],
         "remediation": "string",
         "remediationReferences": [ "string" ],
         "title": "string"
      }
   ],
   "vulnerableCode": "string"
}
```

## Response Elements
<a name="API_GetCodeFinding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [affectedPackages](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-affectedPackages"></a>
The affected Packages.
Type: Array of [AffectedPackage](API_AffectedPackage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.

 ** [category](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-category"></a>
The category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [completedAt](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-completedAt"></a>
The completed At.
Type: Timestamp

 ** [createdAt](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [createdIssueId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-createdIssueId"></a>
The identifier of the created Issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [cveId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-cveId"></a>
The identifier of the cve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [cvssBaseScore](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-cvssBaseScore"></a>
The cvss Base Score.
Type: Double

 ** [cweIds](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-cweIds"></a>
The cwe Ids.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [detailedDescription](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-detailedDescription"></a>
The detailed Description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [discardReason](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-discardReason"></a>
Why a finding was not escalated into an issue. Present only when status is DISCARDED.
Type: String
Valid Values: `SCANNER_VALIDATED_FALSE_POSITIVE | SCANNER_NEEDS_REVIEW | FALSE_POSITIVE_VALIDATED_AGAINST_CONTEXT | DUPLICATE_OF_OPEN_ISSUE | DUPLICATE_OF_CLOSED_ISSUE | COMPENSATING_CONTROL_PRESENT | OUT_OF_SCOPE | INSUFFICIENT_EVIDENCE | PROCESSING_FAILED | SOURCE_REPO_NOT_FOUND`

 ** [discardReasoning](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-discardReasoning"></a>
The discard Reasoning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [duplicateOfIssueId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-duplicateOfIssueId"></a>
The identifier of the duplicate Of Issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [endLine](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-endLine"></a>
The end Line.
Type: Integer

 ** [environmentId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [filePath](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-filePath"></a>
The file Path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [findingArn](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-findingArn"></a>
The Amazon Resource Name (ARN) of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+/code-findings/[a-z0-9]+`

 ** [findingId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-findingId"></a>
The identifier of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [findingTypes](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-findingTypes"></a>
The finding Types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [firstSeenAt](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-firstSeenAt"></a>
The first Seen At.
Type: Timestamp

 ** [lineNumber](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-lineNumber"></a>
The line Number.
Type: Integer

 ** [mitigation](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-mitigation"></a>
The mitigation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [mitreTechniques](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-mitreTechniques"></a>
The mitre Techniques.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [ocsfClass](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-ocsfClass"></a>
The ocsf Class.
Type: String
Valid Values: `VULNERABILITY_FINDING | APPLICATION_SECURITY_POSTURE_FINDING`

 ** [ocsfSchemaVersion](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-ocsfSchemaVersion"></a>
The ocsf Schema Version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [owaspCategory](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-owaspCategory"></a>
The owasp Category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [posture](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-posture"></a>
The compliance posture a finding reports, for the Application Security Posture Finding class. Absent for a vulnerability finding.
Type: [FindingPosture](API_FindingPosture.md) object

 ** [productName](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-productName"></a>
The product Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [productVendorName](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-productVendorName"></a>
The product Vendor Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [productVersion](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-productVersion"></a>
The product Version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [relevantInputs](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-relevantInputs"></a>
The relevant Inputs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [remediationReferences](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-remediationReferences"></a>
The remediation References.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [reportedAt](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-reportedAt"></a>
The reported At.
Type: Timestamp

 ** [resources](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-resources"></a>
The resources.
Type: Array of [FindingResource](API_FindingResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.

 ** [scanRunId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-scanRunId"></a>
The identifier of the scan Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [severity](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-severity"></a>
The severity.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL | FATAL | OTHER`

 ** [source](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-source"></a>
The source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [sourceFindingId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-sourceFindingId"></a>
The identifier of the source Finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [sourceStatus](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-sourceStatus"></a>
The source Status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [sourceStatusId](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-sourceStatusId"></a>
The identifier of the source Status.
Type: Integer

 ** [status](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-status"></a>
The lifecycle status of a finding as it moves through Continuum's processing pipeline. CONFIRMED and DISCARDED are terminal states — a CONFIRMED finding is promoted into a separate Issue (not yet implemented), which owns the subsequent remediation lifecycle; the finding's own status does not change after that.
Type: String
Valid Values: `SUBMITTED | VALIDATING | CONFIRMED | DISCARDED`

 ** [statusMessage](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [statusUpdatedAt](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp

 ** [stepsToReproduce](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-stepsToReproduce"></a>
The steps To Reproduce.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [subCategory](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-subCategory"></a>
The sub Category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [summary](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-summary"></a>
The summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [title](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-title"></a>
The title.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [type](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-type"></a>
What kind of finding this is, and who produced it.
Type: String
Valid Values: `CONTINUUM_CODE_VULN | CUSTOMER_CODE_VULN`

 ** [validation](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-validation"></a>
A validator's assessment of a finding. Present only when validation actually ran — absent for finding types that are ingested untested, rather than reporting a verdict Continuum did not reach.
Type: [FindingValidation](API_FindingValidation.md) object

 ** [vulnerabilities](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-vulnerabilities"></a>
The vulnerabilities.
Type: Array of [FindingVulnerability](API_FindingVulnerability.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.

 ** [vulnerableCode](#API_GetCodeFinding_ResponseSyntax) **   <a name="continuum-GetCodeFinding-response-vulnerableCode"></a>
The vulnerable Code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.

## Errors
<a name="API_GetCodeFinding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetCodeFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetCodeFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetCodeFinding)
