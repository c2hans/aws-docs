---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteAsset.html
---

# DeleteAsset
<a name="API_DeleteAsset"></a>

This operation deletes an asset.

## Request Syntax
<a name="API_DeleteAsset_RequestSyntax"></a>

```
DELETE /v1/data-sets/{{DataSetId}}/revisions/{{RevisionId}}/assets/{{AssetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetId](#API_DeleteAsset_RequestSyntax) **   <a name="dataexchange-DeleteAsset-request-uri-AssetId"></a>
The unique identifier for an asset.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [DataSetId](#API_DeleteAsset_RequestSyntax) **   <a name="dataexchange-DeleteAsset-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [RevisionId](#API_DeleteAsset_RequestSyntax) **   <a name="dataexchange-DeleteAsset-request-uri-RevisionId"></a>
The unique identifier for a revision.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_DeleteAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAsset_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAsset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** Message **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** ResourceId **
The unique identifier for the resource with the conflict.
 ** ResourceType **
The type of the resource with the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/DeleteAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/DeleteAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
