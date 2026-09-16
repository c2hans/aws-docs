---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeVocabulary.html
---

# DescribeVocabulary
<a name="API_DescribeVocabulary"></a>

Describes the specified vocabulary.

## Request Syntax
<a name="API_DescribeVocabulary_RequestSyntax"></a>

```
GET /vocabulary/{{InstanceId}}/{{VocabularyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVocabulary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeVocabulary_RequestSyntax) **   <a name="connect-DescribeVocabulary-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [VocabularyId](#API_DescribeVocabulary_RequestSyntax) **   <a name="connect-DescribeVocabulary-request-uri-VocabularyId"></a>
The identifier of the custom vocabulary.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_DescribeVocabulary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVocabulary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Vocabulary": {
      "Arn": "string",
      "Content": "string",
      "FailureReason": "string",
      "Id": "string",
      "LanguageCode": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "State": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Vocabulary](#API_DescribeVocabulary_ResponseSyntax) **   <a name="connect-DescribeVocabulary-response-Vocabulary"></a>
A list of specific words that you want Contact Lens for Connect Customer to recognize in your audio input. They are generally domain-specific words and phrases, words that Contact Lens is not recognizing, or proper nouns.
Type: [Vocabulary](API_Vocabulary.md) object

## Errors
<a name="API_DescribeVocabulary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeVocabulary)
