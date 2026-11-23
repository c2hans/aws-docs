---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_GetBlueprint.html
---

# GetBlueprint

Gets the details of a blueprint, including its schema, encryption settings, and timestamps.

## Request Syntax
<a name="API_GetBlueprint_RequestSyntax"></a>

```
{
   "BlueprintArn": "{{string}}",
   "BlueprintVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBlueprint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintArn](#API_GetBlueprint_RequestSyntax) **   <a name="Textract-GetBlueprint-request-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: Yes

 ** [BlueprintVersion](#API_GetBlueprint_RequestSyntax) **   <a name="Textract-GetBlueprint-request-BlueprintVersion"></a>
The version of the blueprint to retrieve. If omitted, the latest version is returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]*$`
Required: No

## Response Syntax
<a name="API_GetBlueprint_ResponseSyntax"></a>

```
{
   "BlueprintArn": "string",
   "BlueprintName": "string",
   "BlueprintVersion": "string",
   "CreationTime": number,
   "KmsEncryptionContext": {
      "string" : "string"
   },
   "KmsKeyId": "string",
   "LastModifiedTime": number,
   "Schema": "string"
}
```

## Response Elements
<a name="API_GetBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlueprintArn](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`

 ** [BlueprintName](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-BlueprintName"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`

 ** [BlueprintVersion](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-BlueprintVersion"></a>
The version of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]*$`

 ** [CreationTime](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-CreationTime"></a>
The date and time that the blueprint was created.
Type: Timestamp

 ** [KmsEncryptionContext](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-KmsEncryptionContext"></a>
The AWS KMS encryption context used when encrypting the blueprint.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: `^.*\S.*$`
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: `^.*\S.*$`

 ** [KmsKeyId](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-KmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

 ** [LastModifiedTime](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-LastModifiedTime"></a>
The date and time that the blueprint was last modified.
Type: Timestamp

 ** [Schema](#API_GetBlueprint_ResponseSyntax) **   <a name="Textract-GetBlueprint-response-Schema"></a>
The schema of the blueprint, which defines the fields to extract and their expected structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7AF\u3400-\u4DBF]+$`

## Errors
<a name="API_GetBlueprint_Errors"></a>

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

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_GetBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/GetBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/GetBlueprint)
