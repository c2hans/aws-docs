---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateUploadJob.html
---

# CreateUploadJob
<a name="API_connect-customer-profiles_CreateUploadJob"></a>

Creates an Upload job to ingest data for segment imports. The metadata is created for the job with the provided field mapping and unique key.

## Request Syntax
<a name="API_connect-customer-profiles_CreateUploadJob_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/upload-jobs HTTP/1.1
Content-type: application/json

{
   "DataExpiry": {{number}},
   "DisplayName": "{{string}}",
   "Fields": {
      "{{string}}" : {
         "ContentType": "{{string}}",
         "Source": "{{string}}",
         "Target": "{{string}}"
      }
   },
   "UniqueKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateUploadJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-request-uri-DomainName"></a>
The unique name of the domain. Domain should be exists for the upload job to be created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateUploadJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataExpiry](#API_connect-customer-profiles_CreateUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-request-DataExpiry"></a>
The expiry duration for the profiles ingested with the job. If not provided, the system default of 2 weeks is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.
Required: No

 ** [DisplayName](#API_connect-customer-profiles_CreateUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-request-DisplayName"></a>
The unique name of the upload job. Could be a file name to identify the upload job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Fields](#API_connect-customer-profiles_CreateUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-request-Fields"></a>
The mapping between CSV Columns and Profile Object attributes. A map of the name and ObjectType field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Required: Yes

 ** [UniqueKey](#API_connect-customer-profiles_CreateUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-request-UniqueKey"></a>
The unique key columns for de-duping the profiles used to map data to the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_CreateUploadJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateUploadJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_connect-customer-profiles_CreateUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateUploadJob-response-JobId"></a>
The unique identifier for the created upload job.
Type: String
Pattern: `[a-f0-9]{32}`

## Errors
<a name="API_connect-customer-profiles_CreateUploadJob_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateUploadJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateUploadJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateUploadJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
