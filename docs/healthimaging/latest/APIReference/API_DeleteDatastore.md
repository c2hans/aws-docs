---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DeleteDatastore.html
---

# DeleteDatastore
<a name="API_DeleteDatastore"></a>

Delete a data store.

**Note**
Before a data store can be deleted, you must first delete all image sets within it.

## Request Syntax
<a name="API_DeleteDatastore_RequestSyntax"></a>

```
DELETE /datastore/{{datastoreId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDatastore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_DeleteDatastore_RequestSyntax) **   <a name="healthimaging-DeleteDatastore-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_DeleteDatastore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDatastore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreId": "string",
   "datastoreStatus": "string"
}
```

## Response Elements
<a name="API_DeleteDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreId](#API_DeleteDatastore_ResponseSyntax) **   <a name="healthimaging-DeleteDatastore-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [datastoreStatus](#API_DeleteDatastore_ResponseSyntax) **   <a name="healthimaging-DeleteDatastore-response-datastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED`

## Errors
<a name="API_DeleteDatastore_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/DeleteDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DeleteDatastore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
