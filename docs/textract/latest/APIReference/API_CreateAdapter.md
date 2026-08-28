---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateAdapter.html
---

# CreateAdapter
<a name="API_CreateAdapter"></a>

Creates an adapter, which can be fine-tuned for enhanced performance on user provided documents. Takes an AdapterName and FeatureType. Currently the only supported feature type is `QUERIES`. You can also provide a Description, Tags, and a ClientRequestToken. You can choose whether or not the adapter should be AutoUpdated with the AutoUpdate argument. By default, AutoUpdate is set to DISABLED.

## Request Syntax
<a name="API_CreateAdapter_RequestSyntax"></a>

```
{
   "AdapterName": "{{string}}",
   "AutoUpdate": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "FeatureTypes": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAdapter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdapterName](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-AdapterName"></a>
The name to be assigned to the adapter being created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [AutoUpdate](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-AutoUpdate"></a>
Controls whether or not the adapter should automatically update.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ClientRequestToken](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-ClientRequestToken"></a>
Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapter requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Description](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-Description"></a>
The description to be assigned to the adapter being created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
Required: No

 ** [FeatureTypes](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-FeatureTypes"></a>
The type of feature that the adapter is being trained on. Currrenly, supported feature types are: `QUERIES`
Type: Array of strings
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`
Required: Yes

 ** [Tags](#API_CreateAdapter_RequestSyntax) **   <a name="Textract-CreateAdapter-request-Tags"></a>
A list of tags to be added to the adapter.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateAdapter_ResponseSyntax"></a>

```
{
   "AdapterId": "string"
}
```

## Response Elements
<a name="API_CreateAdapter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdapterId](#API_CreateAdapter_ResponseSyntax) **   <a name="Textract-CreateAdapter-response-AdapterId"></a>
A string containing the unique ID for the adapter that has been created.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.

## Errors
<a name="API_CreateAdapter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
A `ClientRequestToken` input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (`StartDocumentTextDetection`, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Returned when a request cannot be completed as it would exceed a maximum service quota.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Textract is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_CreateAdapter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/CreateAdapter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/CreateAdapter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
