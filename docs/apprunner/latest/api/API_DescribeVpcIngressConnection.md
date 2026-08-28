---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeVpcIngressConnection.html
---

# DescribeVpcIngressConnection
<a name="API_DescribeVpcIngressConnection"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Return a full description of an AWS App Runner VPC Ingress Connection resource.

## Request Syntax
<a name="API_DescribeVpcIngressConnection_RequestSyntax"></a>

```
{
   "VpcIngressConnectionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeVpcIngressConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VpcIngressConnectionArn](#API_DescribeVpcIngressConnection_RequestSyntax) **   <a name="apprunner-DescribeVpcIngressConnection-request-VpcIngressConnectionArn"></a>
The Amazon Resource Name (ARN) of the App Runner VPC Ingress Connection that you want a description for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DescribeVpcIngressConnection_ResponseSyntax"></a>

```
{
   "VpcIngressConnection": {
      "AccountId": "string",
      "CreatedAt": number,
      "DeletedAt": number,
      "DomainName": "string",
      "IngressVpcConfiguration": {
         "VpcEndpointId": "string",
         "VpcId": "string"
      },
      "ServiceArn": "string",
      "Status": "string",
      "VpcIngressConnectionArn": "string",
      "VpcIngressConnectionName": "string"
   }
}
```

## Response Elements
<a name="API_DescribeVpcIngressConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcIngressConnection](#API_DescribeVpcIngressConnection_ResponseSyntax) **   <a name="apprunner-DescribeVpcIngressConnection-response-VpcIngressConnection"></a>
A description of the App Runner VPC Ingress Connection that you specified in this request.
Type: [VpcIngressConnection](API_VpcIngressConnection.md) object

## Errors
<a name="API_DescribeVpcIngressConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVpcIngressConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DescribeVpcIngressConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DescribeVpcIngressConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
