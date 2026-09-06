---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_RegisterCrossAccountAccessRole.html
---

# RegisterCrossAccountAccessRole
<a name="API_RegisterCrossAccountAccessRole"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Registers the IAM role that grants Amazon Inspector Classic access to AWS Services needed to perform security assessments.

## Request Syntax
<a name="API_RegisterCrossAccountAccessRole_RequestSyntax"></a>

```
{
   "roleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterCrossAccountAccessRole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [roleArn](#API_RegisterCrossAccountAccessRole_RequestSyntax) **   <a name="Inspector-RegisterCrossAccountAccessRole-request-roleArn"></a>
The ARN of the IAM role that grants Amazon Inspector Classic access to AWS Services needed to perform security assessments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Elements
<a name="API_RegisterCrossAccountAccessRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterCrossAccountAccessRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidCrossAccountRoleException **
Amazon Inspector Classic cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** ServiceTemporarilyUnavailableException **
The serice is temporary unavailable.
 ** canRetry **
You can wait and then retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_RegisterCrossAccountAccessRole_Examples"></a>

### Example
<a name="API_RegisterCrossAccountAccessRole_Example_1"></a>

This example illustrates one usage of RegisterCrossAccountAccessRole.

#### Sample Request
<a name="API_RegisterCrossAccountAccessRole_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 55
                  X-Amz-Target: InspectorService.RegisterCrossAccountAccessRole
                  X-Amz-Date: 20160329T225544Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS

                  {
                    "roleArn": "arn:aws:iam::123456789012:role/inspector"
                  }
```

#### Sample Response
<a name="API_RegisterCrossAccountAccessRole_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 5f553cfa-f601-11e5-a47c-b7e2de2d572c
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 0
                  Date: Tue, 29 Mar 2016 22:55:46 GMT
```

## See Also
<a name="API_RegisterCrossAccountAccessRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/RegisterCrossAccountAccessRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/RegisterCrossAccountAccessRole)
