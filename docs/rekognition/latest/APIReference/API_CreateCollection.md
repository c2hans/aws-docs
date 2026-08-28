---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html
---

# CreateCollection
<a name="API_CreateCollection"></a>

Creates a collection in an AWS Region. You can add faces to the collection using the [IndexFaces](API_IndexFaces.md) operation.

For example, you might create collections, one for each of your application users. A user can then index faces using the `IndexFaces` operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container.

When you create a collection, it is associated with the latest version of the face model version.

**Note**
Collection names are case-sensitive.

This operation requires permissions to perform the `rekognition:CreateCollection` action. If you want to tag your collection, you also require permission to perform the `rekognition:TagResource` operation.

## Request Syntax
<a name="API_CreateCollection_RequestSyntax"></a>

```
{
   "CollectionId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCollection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CollectionId](#API_CreateCollection_RequestSyntax) **   <a name="rekognition-CreateCollection-request-CollectionId"></a>
ID for the collection that you are creating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [Tags](#API_CreateCollection_RequestSyntax) **   <a name="rekognition-CreateCollection-request-Tags"></a>
 A set of tags (key-value pairs) that you want to attach to the collection.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateCollection_ResponseSyntax"></a>

```
{
   "CollectionArn": "string",
   "FaceModelVersion": "string",
   "StatusCode": number
}
```

## Response Elements
<a name="API_CreateCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CollectionArn](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-CollectionArn"></a>
Amazon Resource Name (ARN) of the collection. You can use this to manage permissions on your resources.
Type: String

 ** [FaceModelVersion](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-FaceModelVersion"></a>
Version number of the face detection model associated with the collection you are creating.
Type: String

 ** [StatusCode](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-StatusCode"></a>
HTTP status code indicating the result of the operation.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_CreateCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
A resource with the specified ID already exists.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

The size of the resource exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CreateCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
