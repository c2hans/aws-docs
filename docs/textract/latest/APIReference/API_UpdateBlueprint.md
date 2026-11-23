---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_UpdateBlueprint.html
---

# UpdateBlueprint

Updates an existing blueprint, replacing its schema and, optionally, its encryption configuration.

## Request Syntax
<a name="API_UpdateBlueprint_RequestSyntax"></a>

```
{
   "BlueprintArn": "{{string}}",
   "EncryptionConfiguration": {
      "KmsEncryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "KmsKeyId": "{{string}}"
   },
   "Schema": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateBlueprint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintArn](#API_UpdateBlueprint_RequestSyntax) **   <a name="Textract-UpdateBlueprint-request-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: Yes

 ** [EncryptionConfiguration](#API_UpdateBlueprint_RequestSyntax) **   <a name="Textract-UpdateBlueprint-request-EncryptionConfiguration"></a>
The AWS KMS encryption configuration used to encrypt the blueprint at rest.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [Schema](#API_UpdateBlueprint_RequestSyntax) **   <a name="Textract-UpdateBlueprint-request-Schema"></a>
The updated schema of the blueprint, which defines the fields to extract and their expected structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7AF\u3400-\u4DBF]+$`
Required: No

## Response Syntax
<a name="API_UpdateBlueprint_ResponseSyntax"></a>

```
{
   "BlueprintArn": "string"
}
```

## Response Elements
<a name="API_UpdateBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlueprintArn](#API_UpdateBlueprint_ResponseSyntax) **   <a name="Textract-UpdateBlueprint-response-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`

## Errors
<a name="API_UpdateBlueprint_Errors"></a>

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

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_UpdateBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/UpdateBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/UpdateBlueprint)
