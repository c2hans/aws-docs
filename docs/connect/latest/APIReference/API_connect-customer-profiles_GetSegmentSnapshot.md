---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSegmentSnapshot.html
---

# GetSegmentSnapshot
<a name="API_connect-customer-profiles_GetSegmentSnapshot"></a>

Retrieve the latest status of a segment snapshot.

## Request Syntax
<a name="API_connect-customer-profiles_GetSegmentSnapshot_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/segments/{{SegmentDefinitionName}}/snapshots/{{SnapshotId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSegmentSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-request-uri-DomainName"></a>
The unique identifier of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-request-uri-SegmentDefinitionName"></a>
The unique name of the segment definition.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SnapshotId](#API_connect-customer-profiles_GetSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-request-uri-SnapshotId"></a>
The unique identifier of the segment snapshot.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetSegmentSnapshot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataFormat": "string",
   "DestinationUri": "string",
   "EncryptionKey": "string",
   "RoleArn": "string",
   "SnapshotId": "string",
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSegmentSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataFormat](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-DataFormat"></a>
The format in which the segment will be exported.
Type: String
Valid Values: `CSV | JSONL | ORC`

 ** [DestinationUri](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-DestinationUri"></a>
The destination to which the segment will be exported. This field must be provided if the request is not submitted from the Connect Customer Admin Website.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [EncryptionKey](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-EncryptionKey"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the exported segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [RoleArn](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting KMS and S3 operations.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`

 ** [SnapshotId](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-SnapshotId"></a>
The unique identifier of the segment snapshot.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [Status](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-Status"></a>
The status of the asynchronous job for exporting the segment snapshot.
Type: String
Valid Values: `COMPLETED | IN_PROGRESS | FAILED`

 ** [StatusMessage](#API_connect-customer-profiles_GetSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSnapshot-response-StatusMessage"></a>
The status message of the asynchronous job for exporting the segment snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_connect-customer-profiles_GetSegmentSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetSegmentSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSegmentSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSegmentSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
