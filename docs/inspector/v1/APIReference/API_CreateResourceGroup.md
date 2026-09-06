---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_CreateResourceGroup.html
---

# CreateResourceGroup
<a name="API_CreateResourceGroup"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector Classic assessment target. The created resource group is then used to create an Amazon Inspector Classic assessment target. For more information, see [CreateAssessmentTarget](API_CreateAssessmentTarget.md).

## Request Syntax
<a name="API_CreateResourceGroup_RequestSyntax"></a>

```
{
   "resourceGroupTags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateResourceGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceGroupTags](#API_CreateResourceGroup_RequestSyntax) **   <a name="Inspector-CreateResourceGroup-request-resourceGroupTags"></a>
A collection of keys and an array of possible values, '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.
For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.
Type: Array of [ResourceGroupTag](API_ResourceGroupTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_CreateResourceGroup_ResponseSyntax"></a>

```
{
   "resourceGroupArn": "string"
}
```

## Response Elements
<a name="API_CreateResourceGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceGroupArn](#API_CreateResourceGroup_ResponseSyntax) **   <a name="Inspector-CreateResourceGroup-response-resourceGroupArn"></a>
The ARN that specifies the resource group that is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_CreateResourceGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.
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
<a name="API_CreateResourceGroup_Examples"></a>

### Example
<a name="API_CreateResourceGroup_Example_1"></a>

This example illustrates one usage of CreateResourceGroup.

#### Sample Request
<a name="API_CreateResourceGroup_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 67
                  X-Amz-Target: InspectorService.CreateResourceGroup
                  X-Amz-Date: 20160331T171757Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "resourceGroupTags": [
                      {
                        "key": "Name",
                        "value": "example"
                      }
                    ]
                  }
```

#### Sample Response
<a name="API_CreateResourceGroup_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 8416dfb4-f764-11e5-872a-fde3682789d5
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 88
                  Date: Thu, 31 Mar 2016 17:17:58 GMT
                  {
                    "resourceGroupArn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv"
                  }
```

## See Also
<a name="API_CreateResourceGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/CreateResourceGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/CreateResourceGroup)
