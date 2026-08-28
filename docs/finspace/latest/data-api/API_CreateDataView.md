---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateDataView.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# CreateDataView
<a name="API_CreateDataView"></a>

Creates a Dataview for a Dataset.

## Request Syntax
<a name="API_CreateDataView_RequestSyntax"></a>

```
POST /datasets/{{datasetId}}/dataviewsv2 HTTP/1.1
Content-type: application/json

{
   "asOfTimestamp": {{number}},
   "autoUpdate": {{boolean}},
   "clientToken": "{{string}}",
   "destinationTypeParams": {
      "destinationType": "{{string}}",
      "s3DestinationExportFileFormat": "{{string}}",
      "s3DestinationExportFileFormatOptions": {
         "{{string}}" : "{{string}}"
      }
   },
   "partitionColumns": [ "{{string}}" ],
   "sortColumns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateDataView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-uri-datasetId"></a>
The unique Dataset identifier that is used to create a Dataview.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_CreateDataView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationTypeParams](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-destinationTypeParams"></a>
Options that define the destination type for the Dataview.
Type: [DataViewDestinationTypeParams](API_DataViewDestinationTypeParams.md) object
Required: Yes

 ** [asOfTimestamp](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-asOfTimestamp"></a>
Beginning time to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** [autoUpdate](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-autoUpdate"></a>
Flag to indicate Dataview should be updated automatically.
Type: Boolean
Required: No

 ** [clientToken](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** [partitionColumns](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-partitionColumns"></a>
Ordered set of column names used to partition data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** [sortColumns](#API_CreateDataView_RequestSyntax) **   <a name="finspace-CreateDataView-request-sortColumns"></a>
Columns to be used for sorting the data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## Response Syntax
<a name="API_CreateDataView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetId": "string",
   "dataViewId": "string"
}
```

## Response Elements
<a name="API_CreateDataView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetId](#API_CreateDataView_ResponseSyntax) **   <a name="finspace-CreateDataView-response-datasetId"></a>
The unique identifier of the Dataset used for the Dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [dataViewId](#API_CreateDataView_ResponseSyntax) **   <a name="finspace-CreateDataView-response-dataViewId"></a>
The unique identifier for the created Dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

## Errors
<a name="API_CreateDataView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A limit has exceeded.
HTTP Status Code: 400

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
<a name="API_CreateDataView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/CreateDataView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/CreateDataView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
