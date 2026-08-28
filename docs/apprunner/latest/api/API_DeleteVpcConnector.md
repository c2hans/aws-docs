---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteVpcConnector.html
---

# DeleteVpcConnector
<a name="API_DeleteVpcConnector"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Delete an AWS App Runner VPC connector resource. You can't delete a connector that's used by one or more App Runner services.

## Request Syntax
<a name="API_DeleteVpcConnector_RequestSyntax"></a>

```
{
   "VpcConnectorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteVpcConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VpcConnectorArn](#API_DeleteVpcConnector_RequestSyntax) **   <a name="apprunner-DeleteVpcConnector-request-VpcConnectorArn"></a>
The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to delete.
The ARN must be a full VPC connector ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DeleteVpcConnector_ResponseSyntax"></a>

```
{
   "VpcConnector": {
      "CreatedAt": number,
      "DeletedAt": number,
      "SecurityGroups": [ "string" ],
      "Status": "string",
      "Subnets": [ "string" ],
      "VpcConnectorArn": "string",
      "VpcConnectorName": "string",
      "VpcConnectorRevision": number
   }
}
```

## Response Elements
<a name="API_DeleteVpcConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcConnector](#API_DeleteVpcConnector_ResponseSyntax) **   <a name="apprunner-DeleteVpcConnector-response-VpcConnector"></a>
A description of the App Runner VPC connector that this request just deleted.
Type: [VpcConnector](API_VpcConnector.md) object

## Errors
<a name="API_DeleteVpcConnector_Errors"></a>

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

## Examples
<a name="API_DeleteVpcConnector_Examples"></a>

### Delete a VPC connector
<a name="API_DeleteVpcConnector_Example_1"></a>

This example illustrates how to delete an App Runner VPC connector.

#### Sample Request
<a name="API_DeleteVpcConnector_Example_1_Request"></a>

```
$ aws apprunner delete-vpc-connector --cli-input-json "`cat`"
{
  "VpcConnectorArn": "arn:aws:apprunner:us-east-1:123456789012:vpcconnector/my-vpc-connector/1/3f2eb10e2c494674952026f646844e3d"
}
```

#### Sample Response
<a name="API_DeleteVpcConnector_Example_1_Response"></a>

```
{
  "VpcConnector": {
    "VpcConnectorArn": "arn:aws:apprunner:us-east-1:123456789012:vpcconnector/my-vpc-connector/1/3f2eb10e2c494674952026f646844e3d",
    "VpcConnectorName": "my-vpc-connector",
    "VpcConnectorRevision": 1,
    "Subnets": ["subnet-123", "subnet-456"],
    "SecurityGroups": ["sg-123", "sg-456"],
    "Status": "INACTIVE",
    "CreatedAt": "2021-08-18T23:36:45.374Z",
    "DeletedAt": "2021-09-23T11:42:17.545Z"
  }
}
```

## See Also
<a name="API_DeleteVpcConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DeleteVpcConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DeleteVpcConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
