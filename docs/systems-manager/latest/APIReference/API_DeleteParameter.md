---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameter.html
---

# DeleteParameter
<a name="API_DeleteParameter"></a>

Delete a parameter from the system. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.

## Request Syntax
<a name="API_DeleteParameter_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteParameter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteParameter_RequestSyntax) **   <a name="systemsmanager-DeleteParameter-request-Name"></a>
The name of the parameter to delete.
You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_DeleteParameter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteParameter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ParameterNotFound **
The parameter couldn't be found. Verify the name and try again.
For the `DeleteParameter` and `GetParameter` actions, if the specified parameter doesn't exist, the `ParameterNotFound` exception is *not* recorded in AWS CloudTrail event logs.
HTTP Status Code: 400

## Examples
<a name="API_DeleteParameter_Examples"></a>

### Example
<a name="API_DeleteParameter_Example_1"></a>

This example illustrates one usage of DeleteParameter.

#### Sample Request
<a name="API_DeleteParameter_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 28
X-Amz-Target: AmazonSSM.DeleteParameter
X-Amz-Date: 20240316T010702Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Name": "EC2DevServerType"
}
```

#### Sample Response
<a name="API_DeleteParameter_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteParameter)
