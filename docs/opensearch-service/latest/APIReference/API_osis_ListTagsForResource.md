---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_osis_ListTagsForResource"></a>

Lists all resource tags associated with an OpenSearch Ingestion pipeline. For more information, see [Tagging Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html).

## Request Syntax
<a name="API_osis_ListTagsForResource_RequestSyntax"></a>

```
GET /2022-01-01/osis/listTagsForResource/?arn={{Arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_osis_ListTagsForResource_RequestSyntax) **   <a name="opensearchservice-osis_ListTagsForResource-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the pipeline to retrieve tags for.
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: Yes

## Request Body
<a name="API_osis_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_osis_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_osis_ListTagsForResource_ResponseSyntax) **   <a name="opensearchservice-osis_ListTagsForResource-response-Tags"></a>
A list of tags associated with the given pipeline.
Type: Array of [Tag](API_osis_Tag.md) objects

## Errors
<a name="API_osis_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** ResourceNotFoundException **
You attempted to access or delete a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ListTagsForResource)
