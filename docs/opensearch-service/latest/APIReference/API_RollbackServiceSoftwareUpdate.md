---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RollbackServiceSoftwareUpdate.html
---

# RollbackServiceSoftwareUpdate
<a name="API_RollbackServiceSoftwareUpdate"></a>

Rolls back a service software update for a domain to the previous version. For more information, see [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html).

## Request Syntax
<a name="API_RollbackServiceSoftwareUpdate_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/serviceSoftwareUpdate/rollback HTTP/1.1
Content-type: application/json

{
   "DomainName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RollbackServiceSoftwareUpdate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RollbackServiceSoftwareUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DomainName](#API_RollbackServiceSoftwareUpdate_RequestSyntax) **   <a name="opensearchservice-RollbackServiceSoftwareUpdate-request-DomainName"></a>
The name of the domain to roll back the service software update on.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_RollbackServiceSoftwareUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RollbackServiceSoftwareOptions": {
      "CurrentVersion": "string",
      "Description": "string",
      "NewVersion": "string",
      "RollbackAvailable": boolean
   }
}
```

## Response Elements
<a name="API_RollbackServiceSoftwareUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RollbackServiceSoftwareOptions](#API_RollbackServiceSoftwareUpdate_ResponseSyntax) **   <a name="opensearchservice-RollbackServiceSoftwareUpdate-response-RollbackServiceSoftwareOptions"></a>
The rollback options for the service software update.
Type: [RollbackServiceSoftwareOptions](API_RollbackServiceSoftwareOptions.md) object

## Errors
<a name="API_RollbackServiceSoftwareUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_RollbackServiceSoftwareUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RollbackServiceSoftwareUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
