---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetVpcEndpointServiceName.html
---

# GetVpcEndpointServiceName
<a name="API_GetVpcEndpointServiceName"></a>

Retrieves the VPC endpoint service name.

## Request Syntax
<a name="API_GetVpcEndpointServiceName_RequestSyntax"></a>

```
GET /clusters/{{identifier}}/vpc-endpoint-service-name HTTP/1.1
```

## URI Request Parameters
<a name="API_GetVpcEndpointServiceName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_GetVpcEndpointServiceName_RequestSyntax) **   <a name="auroradsql-GetVpcEndpointServiceName-request-uri-identifier"></a>
The ID of the cluster to retrieve.
Pattern: `[a-z0-9]{26}`
Required: Yes

## Request Body
<a name="API_GetVpcEndpointServiceName_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetVpcEndpointServiceName_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clusterVpcEndpoint": "string",
   "serviceName": "string"
}
```

## Response Elements
<a name="API_GetVpcEndpointServiceName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusterVpcEndpoint](#API_GetVpcEndpointServiceName_ResponseSyntax) **   <a name="auroradsql-GetVpcEndpointServiceName-response-clusterVpcEndpoint"></a>
The VPC connection endpoint for the cluster.
Type: String
Pattern: `[a-zA-Z0-9.-]+`

 ** [serviceName](#API_GetVpcEndpointServiceName_ResponseSyntax) **   <a name="auroradsql-GetVpcEndpointServiceName-response-serviceName"></a>
The VPC endpoint service name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `com\.amazonaws\.[a-z0-9-]+\.dsql[a-z0-9-]*`

## Errors
<a name="API_GetVpcEndpointServiceName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
Retry after seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceId **
The resource ID could not be found.
 ** resourceType **
The resource type could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
The message that the request was denied due to request throttling.
 ** quotaCode **
The request exceeds a request rate quota.
 ** retryAfterSeconds **
The request exceeds a request rate quota. Retry after seconds.
 ** serviceCode **
The request exceeds a service quota.
HTTP Status Code: 429

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetVpcEndpointServiceName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/GetVpcEndpointServiceName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/GetVpcEndpointServiceName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
