---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetVpcEndpoint.html
---

# BatchGetVpcEndpoint
<a name="API_BatchGetVpcEndpoint"></a>

Returns attributes for one or more VPC endpoints associated with the current account. For more information, see [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

## Request Syntax
<a name="API_BatchGetVpcEndpoint_RequestSyntax"></a>

```
{
   "ids": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetVpcEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ids](#API_BatchGetVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-BatchGetVpcEndpoint-request-ids"></a>
A list of VPC endpoint identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetVpcEndpoint_ResponseSyntax"></a>

```
{
   "vpcEndpointDetails": [
      {
         "createdDate": number,
         "failureCode": "string",
         "failureMessage": "string",
         "id": "string",
         "name": "string",
         "securityGroupIds": [ "string" ],
         "status": "string",
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   ],
   "vpcEndpointErrorDetails": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vpcEndpointDetails](#API_BatchGetVpcEndpoint_ResponseSyntax) **   <a name="opensearchserverless-BatchGetVpcEndpoint-response-vpcEndpointDetails"></a>
Details about the specified VPC endpoint.
Type: Array of [VpcEndpointDetail](API_VpcEndpointDetail.md) objects

 ** [vpcEndpointErrorDetails](#API_BatchGetVpcEndpoint_ResponseSyntax) **   <a name="opensearchserverless-BatchGetVpcEndpoint-response-vpcEndpointErrorDetails"></a>
Error information for a failed request.
Type: Array of [VpcEndpointErrorDetail](API_VpcEndpointErrorDetail.md) objects

## Errors
<a name="API_BatchGetVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/BatchGetVpcEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
