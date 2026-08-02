---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionCodeLocation.html
---

# FunctionCodeLocation
<a name="API_FunctionCodeLocation"></a>

Details about a function's deployment package.

## Contents
<a name="API_FunctionCodeLocation_Contents"></a>

 ** Error **   <a name="lambda-Type-FunctionCodeLocation-Error"></a>
An object that contains details about an error related to function deployment package retrieval.
Type: [FunctionCodeLocationError](API_FunctionCodeLocationError.md) object
Required: No

 ** ImageUri **   <a name="lambda-Type-FunctionCodeLocation-ImageUri"></a>
URI of a container image in the Amazon ECR registry.
Type: String
Required: No

 ** Location **   <a name="lambda-Type-FunctionCodeLocation-Location"></a>
A presigned URL that you can use to download the deployment package.
Type: String
Required: No

 ** RepositoryType **   <a name="lambda-Type-FunctionCodeLocation-RepositoryType"></a>
The service that's hosting the file.
Type: String
Required: No

 ** ResolvedImageUri **   <a name="lambda-Type-FunctionCodeLocation-ResolvedImageUri"></a>
The resolved URI for the image.
Type: String
Required: No

 ** ResolvedS3Object **   <a name="lambda-Type-FunctionCodeLocation-ResolvedS3Object"></a>
The resolved Amazon S3 object that contains the deployment package.
Type: [ResolvedS3Object](API_ResolvedS3Object.md) object
Required: No

 ** SourceKMSKeyArn **   <a name="lambda-Type-FunctionCodeLocation-SourceKMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk).
Type: String
Required: No

## See Also
<a name="API_FunctionCodeLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionCodeLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionCodeLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionCodeLocation)
