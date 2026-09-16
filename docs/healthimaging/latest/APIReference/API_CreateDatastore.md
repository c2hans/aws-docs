---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CreateDatastore.html
---

# CreateDatastore
<a name="API_CreateDatastore"></a>

Create a data store.

## Request Syntax
<a name="API_CreateDatastore_RequestSyntax"></a>

```
POST /datastore HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "datastoreName": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "lambdaAuthorizerArn": "{{string}}",
   "losslessStorageFormat": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDatastore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDatastore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-clientToken"></a>
A unique identifier for API idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [datastoreName](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-datastoreName"></a>
The data store name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9._/#-]+`
Required: No

 ** [kmsKeyArn](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-zA-Z-]{0,16}:kms:[a-z]{2}(-[a-z]{1,16}){1,3}-\d{1}:\d{12}:((key/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})|(alias/[a-zA-Z0-9:/_-]{1,256}))`
Required: No

 ** [lambdaAuthorizerArn](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-lambdaAuthorizerArn"></a>
The ARN of the authorizer's Lambda function.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

 ** [losslessStorageFormat](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-losslessStorageFormat"></a>
The lossless storage format for the datastore.
Type: String
Valid Values: `HTJ2K | JPEG_2000_LOSSLESS`
Required: No

 ** [tags](#API_CreateDatastore_RequestSyntax) **   <a name="healthimaging-CreateDatastore-request-tags"></a>
The tags provided when creating a data store.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDatastore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreId": "string",
   "datastoreStatus": "string"
}
```

## Response Elements
<a name="API_CreateDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreId](#API_CreateDatastore_ResponseSyntax) **   <a name="healthimaging-CreateDatastore-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [datastoreStatus](#API_CreateDatastore_ResponseSyntax) **   <a name="healthimaging-CreateDatastore-response-datastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED`

## Errors
<a name="API_CreateDatastore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request caused a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_CreateDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/CreateDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/CreateDatastore)
