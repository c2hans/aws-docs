---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindingsV2.html
---

# BatchUpdateFindingsV2
<a name="API_BatchUpdateFindingsV2"></a>

Updates information about a customer's investigation into a finding. Delegated administrator accounts can update findings for their account and their member accounts. Member accounts can update findings for their own account.

 `BatchUpdateFindings` and `BatchUpdateFindingsV2` both use `securityhub:BatchUpdateFindings` in the `Action` element of an IAM policy statement. You must have permission to perform the `securityhub:BatchUpdateFindings` action. You can configure IAM policies to restrict access to specific finding fields or field values by using the `securityhub:OCSFSyntaxPath/<fieldName>` condition key, where `<fieldName>` is one of the following supported fields: `SeverityId`, `StatusId`, or `Comment`.

To prevent a user from updating a specific field, use a `Null` condition with `securityhub:OCSFSyntaxPath/<fieldName>` set to `"false"`. To prevent a user from setting a field to a specific value, use a `StringEquals` condition with `securityhub:OCSFSyntaxPath/<fieldName>` set to the disallowed value or list of values.

Updates from `BatchUpdateFindingsV2` don't affect the value of `finding_info.modified_time`, `finding_info.modified_time_dt`, `time`, or `time_dt` for a finding.

## Request Syntax
<a name="API_BatchUpdateFindingsV2_RequestSyntax"></a>

```
PATCH /findingsv2/batchupdatev2 HTTP/1.1
Content-type: application/json

{
   "Comment": "{{string}}",
   "FindingIdentifiers": [
      {
         "CloudAccountUid": "{{string}}",
         "FindingInfoUid": "{{string}}",
         "MetadataProductUid": "{{string}}"
      }
   ],
   "MetadataUids": [ "{{string}}" ],
   "SeverityId": {{number}},
   "StatusId": {{number}}
}
```

## URI Request Parameters
<a name="API_BatchUpdateFindingsV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateFindingsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Comment](#API_BatchUpdateFindingsV2_RequestSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-request-Comment"></a>
The updated value for a user provided comment about the finding. Minimum character length 1. Maximum character length 512.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [FindingIdentifiers](#API_BatchUpdateFindingsV2_RequestSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-request-FindingIdentifiers"></a>
Provides information to identify a specific V2 finding.
Type: Array of [OcsfFindingIdentifier](API_OcsfFindingIdentifier.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [MetadataUids](#API_BatchUpdateFindingsV2_RequestSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-request-MetadataUids"></a>
The list of finding `metadata.uid` to indicate findings to update. Finding `metadata.uid` is a globally unique identifier associated with the finding. Customers cannot use `MetadataUids` together with `FindingIdentifiers`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: No

 ** [SeverityId](#API_BatchUpdateFindingsV2_RequestSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-request-SeverityId"></a>
The updated value for the normalized severity identifier. The severity ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 6, 99]. When customer provides the updated severity ID, the string sibling severity will automatically be updated in the finding.
Type: Integer
Required: No

 ** [StatusId](#API_BatchUpdateFindingsV2_RequestSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-request-StatusId"></a>
The updated value for the normalized status identifier. The status ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 99]. When customer provides the updated status ID, the string sibling status will automatically be updated in the finding.
Type: Integer
Required: No

## Response Syntax
<a name="API_BatchUpdateFindingsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProcessedFindings": [
      {
         "FindingIdentifier": {
            "CloudAccountUid": "string",
            "FindingInfoUid": "string",
            "MetadataProductUid": "string"
         },
         "MetadataUid": "string"
      }
   ],
   "UnprocessedFindings": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "FindingIdentifier": {
            "CloudAccountUid": "string",
            "FindingInfoUid": "string",
            "MetadataProductUid": "string"
         },
         "MetadataUid": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateFindingsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessedFindings](#API_BatchUpdateFindingsV2_ResponseSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-response-ProcessedFindings"></a>
The list of findings that were updated successfully.
Type: Array of [BatchUpdateFindingsV2ProcessedFinding](API_BatchUpdateFindingsV2ProcessedFinding.md) objects

 ** [UnprocessedFindings](#API_BatchUpdateFindingsV2_ResponseSyntax) **   <a name="securityhub-BatchUpdateFindingsV2-response-UnprocessedFindings"></a>
The list of V2 findings that were not updated.
Type: Array of [BatchUpdateFindingsV2UnprocessedFinding](API_BatchUpdateFindingsV2UnprocessedFinding.md) objects

## Errors
<a name="API_BatchUpdateFindingsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_BatchUpdateFindingsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchUpdateFindingsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateFindingsV2)
