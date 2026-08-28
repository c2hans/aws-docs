---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateSegmentSnapshot.html
---

# CreateSegmentSnapshot
<a name="API_connect-customer-profiles_CreateSegmentSnapshot"></a>

Triggers a job to export a segment to a specified destination.

## Request Syntax
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/segments/{{SegmentDefinitionName}}/snapshots HTTP/1.1
Content-type: application/json

{
   "DataFormat": "{{string}}",
   "DestinationUri": "{{string}}",
   "EncryptionKey": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-uri-SegmentDefinitionName"></a>
The name of the segment definition used in this snapshot request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataFormat](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-DataFormat"></a>
The format in which the segment will be exported.
Type: String
Valid Values: `CSV | JSONL | ORC`
Required: Yes

 ** [DestinationUri](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-DestinationUri"></a>
The destination to which the segment will be exported. This field must be provided if the request is not submitted from the Connect Customer Admin Website.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [EncryptionKey](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-EncryptionKey"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the exported segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [RoleArn](#API_connect-customer-profiles_CreateSegmentSnapshot_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting KMS and S3 operations.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SnapshotId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotId](#API_connect-customer-profiles_CreateSegmentSnapshot_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentSnapshot-response-SnapshotId"></a>
The unique identifier of the segment snapshot.
Type: String
Pattern: `[a-f0-9]{32}`

## Errors
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateSegmentSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateSegmentSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateSegmentSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
