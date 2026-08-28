---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteIngestionDestination.html
---

# DeleteIngestionDestination
<a name="API_DeleteIngestionDestination"></a>

Deletes an ingestion destination.

This deletes the association between an ingestion and it's destination. It doesn't delete previously ingested data or the storage destination, such as the Amazon S3 bucket where the data is delivered. If the ingestion destination is deleted while the associated ingestion is enabled, the ingestion will fail and is eventually disabled.

## Request Syntax
<a name="API_DeleteIngestionDestination_RequestSyntax"></a>

```
DELETE /appbundles/{{appBundleIdentifier}}/ingestions/{{ingestionIdentifier}}/ingestiondestinations/{{ingestionDestinationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteIngestionDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appBundleIdentifier](#API_DeleteIngestionDestination_RequestSyntax) **   <a name="appfabric-DeleteIngestionDestination-request-uri-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [ingestionDestinationIdentifier](#API_DeleteIngestionDestination_RequestSyntax) **   <a name="appfabric-DeleteIngestionDestination-request-uri-ingestionDestinationIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [ingestionIdentifier](#API_DeleteIngestionDestination_RequestSyntax) **   <a name="appfabric-DeleteIngestionDestination-request-uri-ingestionIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_DeleteIngestionDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteIngestionDestination_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteIngestionDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteIngestionDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request rate exceeds the limit.
 ** quotaCode **
The code for the quota exceeded.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
 ** serviceCode **
The code of the service.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
 ** fieldList **
The field list.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteIngestionDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/DeleteIngestionDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/DeleteIngestionDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
