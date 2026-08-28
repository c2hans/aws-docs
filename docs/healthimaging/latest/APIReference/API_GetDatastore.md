---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDatastore.html
---

# GetDatastore
<a name="API_GetDatastore"></a>

Get data store properties.

## Request Syntax
<a name="API_GetDatastore_RequestSyntax"></a>

```
GET /datastore/{{datastoreId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDatastore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_GetDatastore_RequestSyntax) **   <a name="healthimaging-GetDatastore-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_GetDatastore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDatastore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreProperties": {
      "createdAt": number,
      "datastoreArn": "string",
      "datastoreId": "string",
      "datastoreName": "string",
      "datastoreStatus": "string",
      "kmsKeyArn": "string",
      "lambdaAuthorizerArn": "string",
      "losslessStorageFormat": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreProperties](#API_GetDatastore_ResponseSyntax) **   <a name="healthimaging-GetDatastore-response-datastoreProperties"></a>
The data store properties.
Type: [DatastoreProperties](API_DatastoreProperties.md) object

## Errors
<a name="API_GetDatastore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/GetDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/GetDatastore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
