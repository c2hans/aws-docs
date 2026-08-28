---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateVpcLink.html
---

# CreateVpcLink
<a name="API_CreateVpcLink"></a>

Creates a VPC link, under the caller's account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.

## Request Syntax
<a name="API_CreateVpcLink_RequestSyntax"></a>

```
POST /vpclinks HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateVpcLink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVpcLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateVpcLink_RequestSyntax) **   <a name="apigw-CreateVpcLink-request-description"></a>
The description of the VPC link.
Type: String
Required: No

 ** [name](#API_CreateVpcLink_RequestSyntax) **   <a name="apigw-CreateVpcLink-request-name"></a>
The name used to label and identify the VPC link.
Type: String
Required: Yes

 ** [tags](#API_CreateVpcLink_RequestSyntax) **   <a name="apigw-CreateVpcLink-request-tags"></a>
The key-value map of strings. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Required: No

 ** [targetArns](#API_CreateVpcLink_RequestSyntax) **   <a name="apigw-CreateVpcLink-request-targetArns"></a>
The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_CreateVpcLink_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "description": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": {
      "string" : "string"
   },
   "targetArns": [ "string" ]
}
```

## Response Elements
<a name="API_CreateVpcLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-description"></a>
The description of the VPC link.
Type: String

 ** [id](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-id"></a>
The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
Type: String

 ** [name](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-name"></a>
The name used to label and identify the VPC link.
Type: String

 ** [status](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-status"></a>
The status of the VPC link. The valid values are `AVAILABLE`, `PENDING`, `DELETING`, or `FAILED`. Deploying an API will wait if the status is `PENDING` and will fail if the status is `DELETING`.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING | FAILED`

 ** [statusMessage](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-statusMessage"></a>
A description about the VPC link status.
Type: String

 ** [tags](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [targetArns](#API_CreateVpcLink_ResponseSyntax) **   <a name="apigw-CreateVpcLink-response-targetArns"></a>
The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
Type: Array of strings

## Errors
<a name="API_CreateVpcLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_CreateVpcLink_Examples"></a>

### Create a VPC link
<a name="API_CreateVpcLink_Example_1"></a>

This example illustrates one usage of CreateVpcLink.

#### Sample Request
<a name="API_CreateVpcLink_Example_1_Request"></a>

```
POST /vpclinks HTTP/1.1
Content-Type: application/json
Host: apigateway.us-eas-t.amazonaws.com
Content-Length: ...
X-Amz-Date: 20160801T235803Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160801/ap-southeast-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sigv4_hash}

{
    "name":"my-test-vpc-link",
    "targetArns": ["arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-vpclink-test-nlb/1f8df693cd094a72"]
}
```

#### Sample Response
<a name="API_CreateVpcLink_Example_1_Response"></a>

```
{
    "id": "gim7c3",
    "name": "my-test-vpc-link",
    "status": "PENDING",
    "targetArns": "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-vpclink-test-nlb/1f8df693cd094a72"
}
```

## See Also
<a name="API_CreateVpcLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateVpcLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateVpcLink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
