---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdateChangeset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# UpdateChangeset
<a name="API_UpdateChangeset"></a>

Updates a FinSpace Changeset.

## Request Syntax
<a name="API_UpdateChangeset_RequestSyntax"></a>

```
PUT /datasets/{{datasetId}}/changesetsv2/{{changesetId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "formatParams": {
      "{{string}}" : "{{string}}"
   },
   "sourceParams": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateChangeset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [changesetId](#API_UpdateChangeset_RequestSyntax) **   <a name="finspace-UpdateChangeset-request-uri-changesetId"></a>
The unique identifier for the Changeset to update.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

 ** [datasetId](#API_UpdateChangeset_RequestSyntax) **   <a name="finspace-UpdateChangeset-request-uri-datasetId"></a>
The unique identifier for the FinSpace Dataset in which the Changeset is created.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_UpdateChangeset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [formatParams](#API_UpdateChangeset_RequestSyntax) **   <a name="finspace-UpdateChangeset-request-formatParams"></a>
Options that define the structure of the source file(s) including the format type (`formatType`), header row (`withHeader`), data separation character (`separator`) and the type of compression (`compression`).
 `formatType` is a required attribute and can have the following values:
+  `PARQUET` – Parquet source file format.
+  `CSV` – CSV source file format.
+  `JSON` – JSON source file format.
+  `XML` – XML source file format.
Here is an example of how you could specify the `formatParams`:
 ` "formatParams": { "formatType": "CSV", "withHeader": "true", "separator": ",", "compression":"None" } `
Note that if you only provide `formatType` as `CSV`, the rest of the attributes will automatically default to CSV values as following:
 ` { "withHeader": "true", "separator": "," } `
 For more information about supported file formats, see [Supported Data Types and File Formats](https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html) in the FinSpace User Guide.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** [sourceParams](#API_UpdateChangeset_RequestSyntax) **   <a name="finspace-UpdateChangeset-request-sourceParams"></a>
Options that define the location of the data being ingested (`s3SourcePath`) and the source of the changeset (`sourceType`).
Both `s3SourcePath` and `sourceType` are required attributes.
Here is an example of how you could specify the `sourceParams`:
 ` "sourceParams": { "s3SourcePath": "s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv", "sourceType": "S3" } `
The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see [Loading data from an Amazon S3 Bucket using the FinSpace API](https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets)section.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** [clientToken](#API_UpdateChangeset_RequestSyntax) **   <a name="finspace-UpdateChangeset-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateChangeset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "changesetId": "string",
   "datasetId": "string"
}
```

## Response Elements
<a name="API_UpdateChangeset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [changesetId](#API_UpdateChangeset_ResponseSyntax) **   <a name="finspace-UpdateChangeset-response-changesetId"></a>
The unique identifier for the Changeset to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [datasetId](#API_UpdateChangeset_ResponseSyntax) **   <a name="finspace-UpdateChangeset-response-datasetId"></a>
The unique identifier for the FinSpace Dataset in which the Changeset is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

## Errors
<a name="API_UpdateChangeset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateChangeset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/UpdateChangeset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/UpdateChangeset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
