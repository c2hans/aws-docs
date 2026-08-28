---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_GetAdapterVersion.html
---

# GetAdapterVersion
<a name="API_GetAdapterVersion"></a>

Gets configuration information for the specified adapter version, including: AdapterId, AdapterVersion, FeatureTypes, Status, StatusMessage, DatasetConfig, KMSKeyId, OutputConfig, Tags and EvaluationMetrics.

## Request Syntax
<a name="API_GetAdapterVersion_RequestSyntax"></a>

```
{
   "AdapterId": "{{string}}",
   "AdapterVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAdapterVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdapterId](#API_GetAdapterVersion_RequestSyntax) **   <a name="Textract-GetAdapterVersion-request-AdapterId"></a>
A string specifying a unique ID for the adapter version you want to retrieve information for.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.
Required: Yes

 ** [AdapterVersion](#API_GetAdapterVersion_RequestSyntax) **   <a name="Textract-GetAdapterVersion-request-AdapterVersion"></a>
A string specifying the adapter version you want to retrieve information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_GetAdapterVersion_ResponseSyntax"></a>

```
{
   "AdapterId": "string",
   "AdapterVersion": "string",
   "CreationTime": number,
   "DatasetConfig": {
      "ManifestS3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "EvaluationMetrics": [
      {
         "AdapterVersion": {
            "F1Score": number,
            "Precision": number,
            "Recall": number
         },
         "Baseline": {
            "F1Score": number,
            "Precision": number,
            "Recall": number
         },
         "FeatureType": "string"
      }
   ],
   "FeatureTypes": [ "string" ],
   "KMSKeyId": "string",
   "OutputConfig": {
      "S3Bucket": "string",
      "S3Prefix": "string"
   },
   "Status": "string",
   "StatusMessage": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetAdapterVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdapterId](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-AdapterId"></a>
A string containing a unique ID for the adapter version being retrieved.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.

 ** [AdapterVersion](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-AdapterVersion"></a>
A string containing the adapter version that has been retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [CreationTime](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-CreationTime"></a>
The time that the adapter version was created.
Type: Timestamp

 ** [DatasetConfig](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-DatasetConfig"></a>
Specifies a dataset used to train a new adapter version. Takes a ManifestS3Objec as the value.
Type: [AdapterVersionDatasetConfig](API_AdapterVersionDatasetConfig.md) object

 ** [EvaluationMetrics](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-EvaluationMetrics"></a>
The evaluation metrics (F1 score, Precision, and Recall) for the requested version, grouped by baseline metrics and adapter version.
Type: Array of [AdapterVersionEvaluationMetric](API_AdapterVersionEvaluationMetric.md) objects

 ** [FeatureTypes](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-FeatureTypes"></a>
List of the targeted feature types for the requested adapter version.
Type: Array of strings
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

 ** [KMSKeyId](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-KMSKeyId"></a>
The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

 ** [OutputConfig](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-OutputConfig"></a>
Sets whether or not your output will go to a user created bucket. Used to set the name of the bucket, and the prefix on the output file.
 `OutputConfig` is an optional parameter which lets you adjust where your output will be placed. By default, Amazon Textract will store the results internally and can only be accessed by the Get API operations. With `OutputConfig` enabled, you can set the name of the bucket the output will be sent to the file prefix of the results where you can download your results. Additionally, you can set the `KMSKeyID` parameter to a customer master key (CMK) to encrypt your output. Without this parameter set Amazon Textract will encrypt server-side using the AWS managed CMK for Amazon S3.
Decryption of Customer Content is necessary for processing of the documents by Amazon Textract. If your account is opted out under an AI services opt out policy then all unencrypted Customer Content is immediately and permanently deleted after the Customer Content has been processed by the service. No copy of of the output is retained by Amazon Textract. For information about how to opt out, see [ Managing AI services opt-out policy. ](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)
For more information on data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).
Type: [OutputConfig](API_OutputConfig.md) object

 ** [Status](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-Status"></a>
The status of the adapter version that has been requested.
Type: String
Valid Values: `ACTIVE | AT_RISK | DEPRECATED | CREATION_ERROR | CREATION_IN_PROGRESS`

 ** [StatusMessage](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-StatusMessage"></a>
A message that describes the status of the requested adapter version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`

 ** [Tags](#API_GetAdapterVersion_ResponseSyntax) **   <a name="Textract-GetAdapterVersion-response-Tags"></a>
A set of tags (key-value pairs) that are associated with the adapter version.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_GetAdapterVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 Returned when an operation tried to access a nonexistent resource.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Textract is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_GetAdapterVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/GetAdapterVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/GetAdapterVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
