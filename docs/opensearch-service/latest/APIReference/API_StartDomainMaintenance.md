---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartDomainMaintenance.html
---

# StartDomainMaintenance
<a name="API_StartDomainMaintenance"></a>

Starts the node maintenance process on the data node. These processes can include a node reboot, an Opensearch or Elasticsearch process restart, or a Dashboard or Kibana restart.

## Request Syntax
<a name="API_StartDomainMaintenance_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/domainMaintenance HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "NodeId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartDomainMaintenance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_StartDomainMaintenance_RequestSyntax) **   <a name="opensearchservice-StartDomainMaintenance-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_StartDomainMaintenance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_StartDomainMaintenance_RequestSyntax) **   <a name="opensearchservice-StartDomainMaintenance-request-Action"></a>
The name of the action.
Type: String
Valid Values: `REBOOT_NODE | RESTART_SEARCH_PROCESS | RESTART_DASHBOARD`
Required: Yes

 ** [NodeId](#API_StartDomainMaintenance_RequestSyntax) **   <a name="opensearchservice-StartDomainMaintenance-request-NodeId"></a>
The ID of the data node.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 40.
Required: No

## Response Syntax
<a name="API_StartDomainMaintenance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MaintenanceId": "string"
}
```

## Response Elements
<a name="API_StartDomainMaintenance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaintenanceId](#API_StartDomainMaintenance_ResponseSyntax) **   <a name="opensearchservice-StartDomainMaintenance-response-MaintenanceId"></a>
The request ID of requested action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([\s\S]*)$`

## Errors
<a name="API_StartDomainMaintenance_Errors"></a>

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
<a name="API_StartDomainMaintenance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/StartDomainMaintenance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/StartDomainMaintenance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
