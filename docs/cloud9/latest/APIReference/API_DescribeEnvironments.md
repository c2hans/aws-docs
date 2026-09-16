---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironments.html
---

# DescribeEnvironments
<a name="API_DescribeEnvironments"></a>

Gets information about AWS Cloud9 development environments.

**Important**
 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

## Request Syntax
<a name="API_DescribeEnvironments_RequestSyntax"></a>

```
{
   "environmentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeEnvironments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [environmentIds](#API_DescribeEnvironments_RequestSyntax) **   <a name="cloud9-DescribeEnvironments-request-environmentIds"></a>
The IDs of individual environments to get information about.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^[a-zA-Z0-9]{8,32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeEnvironments_ResponseSyntax"></a>

```
{
   "environments": [
      {
         "arn": "string",
         "connectionType": "string",
         "description": "string",
         "id": "string",
         "lifecycle": {
            "failureResource": "string",
            "reason": "string",
            "status": "string"
         },
         "managedCredentialsStatus": "string",
         "name": "string",
         "ownerArn": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environments](#API_DescribeEnvironments_ResponseSyntax) **   <a name="cloud9-DescribeEnvironments-response-environments"></a>
Information about the environments that are returned.
Type: Array of [Environment](API_Environment.md) objects

## Errors
<a name="API_DescribeEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The target request is invalid.
HTTP Status Code: 400

 ** ConflictException **
A conflict occurred.
HTTP Status Code: 400

 ** ForbiddenException **
An access permissions issue occurred.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit was exceeded.
HTTP Status Code: 400

 ** NotFoundException **
The target resource cannot be found.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many service requests were made over the given time period.
HTTP Status Code: 400

## Examples
<a name="API_DescribeEnvironments_Examples"></a>

### Example
<a name="API_DescribeEnvironments_Example_1"></a>

The following example gets information about the specified AWS Cloud9 development environments.

#### Sample Request
<a name="API_DescribeEnvironments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
X-Amz-Date: <Date>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCloud9WorkspaceManagementService.DescribeEnvironments
User-Agent: <UserAgentString>

{
  "environmentIds": [
    "8d9967e2f0624182b74e7690ad69ebEX",
    "349c86d4579e4e7298d500ff57a6b2EX"
  ]
}
```

#### Sample Response
<a name="API_DescribeEnvironments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <Date>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
x-amzn-RequestId: <RequestId>
Connection: Keep-alive

{
  "environments": [
    {
      "arn": "arn:aws:cloud9:eu-west-1:123456789012:environment:8d9967e2f0624182b74e7690ad69ebEX",
      "description": "foo",
      "id": "8d9967e2f0624182b74e7690ad69ebEX",
      "lifecycle": {
        "reasonCode": "CREATE_SUCCESS",
        "status": "CREATED"
      },
      "managedCredentialsStatus": "DISABLED_BY_COLLABORATOR",
      "name": "foo",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "type": "ec2"
    },
    {
      "arn": "arn:aws:cloud9:eu-west-1:123456789012:environment:349c86d4579e4e7298d500ff57a6b2EX",
      "description": "",
      "id": "349c86d4579e4e7298d500ff57a6b2EX",
      "lifecycle": {
        "reasonCode": "CREATE_SUCCESS",
        "status": "CREATED"
      },
      "name": "TestEnv",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "managedCredentialsStatus": "ENABLED_BY_OWNER",
      "type": "ec2"
    }
  ]
}
```

## See Also
<a name="API_DescribeEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DescribeEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DescribeEnvironments)
