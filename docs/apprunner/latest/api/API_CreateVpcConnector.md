---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CreateVpcConnector.html
---

# CreateVpcConnector
<a name="API_CreateVpcConnector"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Create an AWS App Runner VPC connector resource. App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud (Amazon VPC).

## Request Syntax
<a name="API_CreateVpcConnector_RequestSyntax"></a>

```
{
   "SecurityGroups": [ "{{string}}" ],
   "Subnets": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcConnectorName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVpcConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecurityGroups](#API_CreateVpcConnector_RequestSyntax) **   <a name="apprunner-CreateVpcConnector-request-SecurityGroups"></a>
A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** [Subnets](#API_CreateVpcConnector_RequestSyntax) **   <a name="apprunner-CreateVpcConnector-request-Subnets"></a>
A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
 App Runner only supports subnets of IP address type *IPv4* and *dual stack* (IPv4 and IPv6).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: Yes

 ** [Tags](#API_CreateVpcConnector_RequestSyntax) **   <a name="apprunner-CreateVpcConnector-request-Tags"></a>
A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VpcConnectorName](#API_CreateVpcConnector_RequestSyntax) **   <a name="apprunner-CreateVpcConnector-request-VpcConnectorName"></a>
A name for the VPC connector.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,39}`
Required: Yes

## Response Syntax
<a name="API_CreateVpcConnector_ResponseSyntax"></a>

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
<a name="API_CreateVpcConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcConnector](#API_CreateVpcConnector_ResponseSyntax) **   <a name="apprunner-CreateVpcConnector-response-VpcConnector"></a>
A description of the App Runner VPC connector that's created by this request.
Type: [VpcConnector](API_VpcConnector.md) object

## Errors
<a name="API_CreateVpcConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
App Runner can't create this resource. You've reached your account quota for this resource type.
For App Runner per-resource quotas, see [AWS App Runner endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/apprunner.html) in the * AWS General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_CreateVpcConnector_Examples"></a>

### Create a VPC connector
<a name="API_CreateVpcConnector_Example_1"></a>

This example illustrates how to create a VPC connector.

#### Sample Request
<a name="API_CreateVpcConnector_Example_1_Request"></a>

```
$ aws apprunner create-vpc-connector --cli-input-json "`cat`"
{
  "VpcConnectorName": "my-vpc-connector",
  "Subnets": ["subnet-123", "subnet-456"],
  "SecurityGroups": ["sg-123", "sg-456"]
}
```

#### Sample Response
<a name="API_CreateVpcConnector_Example_1_Response"></a>

```
{
  "VpcConnector": {
    "VpcConnectorArn": "arn:aws:apprunner:us-east-1:123456789012:vpcconnector/my-vpc-connector/1/3f2eb10e2c494674952026f646844e3d",
    "VpcConnectorName": "my-vpc-connector",
    "VpcConnectorRevision": 1,
    "Subnets": ["subnet-123", "subnet-456"],
    "SecurityGroups": ["sg-123", "sg-456"],
    "Status": "ACTIVE",
    "CreatedAt": "2021-08-18T23:36:45.374Z"
  }
}
```

## See Also
<a name="API_CreateVpcConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/CreateVpcConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CreateVpcConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
