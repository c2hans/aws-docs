---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeVpcEndpoints.html
---

# DescribeVpcEndpoints
<a name="API_DescribeVpcEndpoints"></a>

Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

## Request Syntax
<a name="API_DescribeVpcEndpoints_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/vpcEndpoints/describe HTTP/1.1
Content-type: application/json

{
   "VpcEndpointIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeVpcEndpoints_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeVpcEndpoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VpcEndpointIds](#API_DescribeVpcEndpoints_RequestSyntax) **   <a name="opensearchservice-DescribeVpcEndpoints-request-VpcEndpointIds"></a>
The unique identifiers of the endpoints to get information about.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: Yes

## Response Syntax
<a name="API_DescribeVpcEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VpcEndpointErrors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "VpcEndpointId": "string"
      }
   ],
   "VpcEndpoints": [
      {
         "DomainArn": "string",
         "Endpoint": "string",
         "Status": "string",
         "VpcEndpointId": "string",
         "VpcEndpointOwner": "string",
         "VpcOptions": {
            "AvailabilityZones": [ "string" ],
            "EgressEnabled": boolean,
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "VPCId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeVpcEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpointErrors](#API_DescribeVpcEndpoints_ResponseSyntax) **   <a name="opensearchservice-DescribeVpcEndpoints-response-VpcEndpointErrors"></a>
Any errors associated with the request.
Type: Array of [VpcEndpointError](API_VpcEndpointError.md) objects

 ** [VpcEndpoints](#API_DescribeVpcEndpoints_ResponseSyntax) **   <a name="opensearchservice-DescribeVpcEndpoints-response-VpcEndpoints"></a>
Information about each requested VPC endpoint.
Type: Array of [VpcEndpoint](API_VpcEndpoint.md) objects

## Errors
<a name="API_DescribeVpcEndpoints_Errors"></a>

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

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVpcEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeVpcEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeVpcEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
