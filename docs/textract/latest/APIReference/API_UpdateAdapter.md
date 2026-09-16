---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_UpdateAdapter.html
---

# UpdateAdapter
<a name="API_UpdateAdapter"></a>

Update the configuration for an adapter. FeatureTypes configurations cannot be updated. At least one new parameter must be specified as an argument.

## Request Syntax
<a name="API_UpdateAdapter_RequestSyntax"></a>

```
{
   "AdapterId": "{{string}}",
   "AdapterName": "{{string}}",
   "AutoUpdate": "{{string}}",
   "Description": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAdapter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdapterId](#API_UpdateAdapter_RequestSyntax) **   <a name="Textract-UpdateAdapter-request-AdapterId"></a>
A string containing a unique ID for the adapter that will be updated.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.
Required: Yes

 ** [AdapterName](#API_UpdateAdapter_RequestSyntax) **   <a name="Textract-UpdateAdapter-request-AdapterName"></a>
The new name to be applied to the adapter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [AutoUpdate](#API_UpdateAdapter_RequestSyntax) **   <a name="Textract-UpdateAdapter-request-AutoUpdate"></a>
The new auto-update status to be applied to the adapter.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Description](#API_UpdateAdapter_RequestSyntax) **   <a name="Textract-UpdateAdapter-request-Description"></a>
The new description to be applied to the adapter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
Required: No

## Response Syntax
<a name="API_UpdateAdapter_ResponseSyntax"></a>

```
{
   "AdapterId": "string",
   "AdapterName": "string",
   "AutoUpdate": "string",
   "CreationTime": number,
   "Description": "string",
   "FeatureTypes": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateAdapter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdapterId](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-AdapterId"></a>
A string containing a unique ID for the adapter that has been updated.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.

 ** [AdapterName](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-AdapterName"></a>
A string containing the name of the adapter that has been updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [AutoUpdate](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-AutoUpdate"></a>
The auto-update status of the adapter that has been updated.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [CreationTime](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-CreationTime"></a>
An object specifying the creation time of the the adapter that has been updated.
Type: Timestamp

 ** [Description](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-Description"></a>
A string containing the description of the adapter that has been updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`

 ** [FeatureTypes](#API_UpdateAdapter_ResponseSyntax) **   <a name="Textract-UpdateAdapter-response-FeatureTypes"></a>
List of the targeted feature types for the updated adapter.
Type: Array of strings
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

## Errors
<a name="API_UpdateAdapter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
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
<a name="API_UpdateAdapter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/UpdateAdapter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/UpdateAdapter)
