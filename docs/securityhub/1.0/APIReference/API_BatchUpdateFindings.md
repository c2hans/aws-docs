---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html
---

# BatchUpdateFindings
<a name="API_BatchUpdateFindings"></a>

 Used by Security Hub CSPM customers to update information about their investigation into one or more findings. Requested by administrator accounts or member accounts. Administrator accounts can update findings for their account and their member accounts. A member account can update findings only for their own account. Administrator and member accounts can use this operation to update the following fields and objects for one or more findings:
+  `Confidence`
+  `Criticality`
+  `Note`
+  `RelatedFindings`
+  `Severity`
+  `Types`
+  `UserDefinedFields`
+  `VerificationState`
+  `Workflow`

 If you use this operation to update a finding, your updates don’t affect the value for the `UpdatedAt` field of the finding. Also note that it can take several minutes for Security Hub CSPM to process your request and update each finding specified in the request.

 You can configure IAM policies to restrict access to fields and field values. For example, you might not want member accounts to be able to suppress findings or change the finding severity. For more information see [Configuring access to BatchUpdateFindings](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html#batchupdatefindings-configure-access) in the * AWS Security Hub CSPM User Guide*.

## Request Syntax
<a name="API_BatchUpdateFindings_RequestSyntax"></a>

```
PATCH /findings/batchupdate HTTP/1.1
Content-type: application/json

{
   "Confidence": {{number}},
   "Criticality": {{number}},
   "FindingIdentifiers": [
      {
         "Id": "{{string}}",
         "ProductArn": "{{string}}"
      }
   ],
   "Note": {
      "Text": "{{string}}",
      "UpdatedBy": "{{string}}"
   },
   "RelatedFindings": [
      {
         "Id": "{{string}}",
         "ProductArn": "{{string}}"
      }
   ],
   "Severity": {
      "Label": "{{string}}",
      "Normalized": {{number}},
      "Product": {{number}}
   },
   "Types": [ "{{string}}" ],
   "UserDefinedFields": {
      "{{string}}" : "{{string}}"
   },
   "VerificationState": "{{string}}",
   "Workflow": {
      "Status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_BatchUpdateFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Confidence](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Confidence"></a>
The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [Criticality](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Criticality"></a>
The updated value for the level of importance assigned to the resources associated with the findings.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [FindingIdentifiers](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-FindingIdentifiers"></a>
The list of findings to update. `BatchUpdateFindings` can be used to update up to 100 findings at a time.
For each finding, the list provides the finding identifier and the ARN of the finding provider.
Type: Array of [AwsSecurityFindingIdentifier](API_AwsSecurityFindingIdentifier.md) objects
Required: Yes

 ** [Note](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Note"></a>
The updated note.
Type: [NoteUpdate](API_NoteUpdate.md) object
Required: No

 ** [RelatedFindings](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-RelatedFindings"></a>
A list of findings that are related to the updated findings.
Type: Array of [RelatedFinding](API_RelatedFinding.md) objects
Required: No

 ** [Severity](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Severity"></a>
Used to update the finding severity.
Type: [SeverityUpdate](API_SeverityUpdate.md) object
Required: No

 ** [Types](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Types"></a>
One or more finding types in the format of namespace/category/classifier that classify a finding.
Valid namespace values are as follows.
+ Software and Configuration Checks
+ TTPs
+ Effects
+ Unusual Behaviors
+ Sensitive Data Identifications
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** [UserDefinedFields](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-UserDefinedFields"></a>
A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** [VerificationState](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-VerificationState"></a>
Indicates the veracity of a finding.
The available values for `VerificationState` are as follows.
+  `UNKNOWN` – The default disposition of a security finding
+  `TRUE_POSITIVE` – The security finding is confirmed
+  `FALSE_POSITIVE` – The security finding was determined to be a false alarm
+  `BENIGN_POSITIVE` – A special case of `TRUE_POSITIVE` where the finding doesn't pose any threat, is expected, or both
Type: String
Valid Values: `UNKNOWN | TRUE_POSITIVE | FALSE_POSITIVE | BENIGN_POSITIVE`
Required: No

 ** [Workflow](#API_BatchUpdateFindings_RequestSyntax) **   <a name="securityhub-BatchUpdateFindings-request-Workflow"></a>
Used to update the workflow status of a finding.
The workflow status indicates the progress of the investigation into the finding.
Type: [WorkflowUpdate](API_WorkflowUpdate.md) object
Required: No

## Response Syntax
<a name="API_BatchUpdateFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProcessedFindings": [
      {
         "Id": "string",
         "ProductArn": "string"
      }
   ],
   "UnprocessedFindings": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "FindingIdentifier": {
            "Id": "string",
            "ProductArn": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessedFindings](#API_BatchUpdateFindings_ResponseSyntax) **   <a name="securityhub-BatchUpdateFindings-response-ProcessedFindings"></a>
The list of findings that were updated successfully.
Type: Array of [AwsSecurityFindingIdentifier](API_AwsSecurityFindingIdentifier.md) objects

 ** [UnprocessedFindings](#API_BatchUpdateFindings_ResponseSyntax) **   <a name="securityhub-BatchUpdateFindings-response-UnprocessedFindings"></a>
The list of findings that were not updated.
Type: Array of [BatchUpdateFindingsUnprocessedFinding](API_BatchUpdateFindingsUnprocessedFinding.md) objects

## Errors
<a name="API_BatchUpdateFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchUpdateFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchUpdateFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateFindings)
