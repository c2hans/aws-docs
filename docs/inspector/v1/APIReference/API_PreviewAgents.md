---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_PreviewAgents.html
---

# PreviewAgents
<a name="API_PreviewAgents"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Previews the agents installed on the EC2 instances that are part of the specified assessment target.

## Request Syntax
<a name="API_PreviewAgents_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "previewAgentsArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PreviewAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_PreviewAgents_RequestSyntax) **   <a name="Inspector-PreviewAgents-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
Type: Integer
Required: No

 ** [nextToken](#API_PreviewAgents_RequestSyntax) **   <a name="Inspector-PreviewAgents-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **PreviewAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [previewAgentsArn](#API_PreviewAgents_RequestSyntax) **   <a name="Inspector-PreviewAgents-request-previewAgentsArn"></a>
The ARN of the assessment target whose agents you want to preview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_PreviewAgents_ResponseSyntax"></a>

```
{
   "agentPreviews": [
      {
         "agentHealth": "string",
         "agentId": "string",
         "agentVersion": "string",
         "autoScalingGroup": "string",
         "hostname": "string",
         "ipv4Address": "string",
         "kernelVersion": "string",
         "operatingSystem": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_PreviewAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentPreviews](#API_PreviewAgents_ResponseSyntax) **   <a name="Inspector-PreviewAgents-response-agentPreviews"></a>
The resulting list of agents.
Type: Array of [AgentPreview](API_AgentPreview.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_PreviewAgents_ResponseSyntax) **   <a name="Inspector-PreviewAgents-response-nextToken"></a>
 When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_PreviewAgents_Errors"></a>

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

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_PreviewAgents_Examples"></a>

### Example
<a name="API_PreviewAgents_Example_1"></a>

This example illustrates one usage of PreviewAgents.

#### Sample Request
<a name="API_PreviewAgents_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 82
                  X-Amz-Target: InspectorService.PreviewAgents
                  X-Amz-Date: 20160329T224634Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "previewAgentsArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq"
                  }
```

#### Sample Response
<a name="API_PreviewAgents_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 176c8915-f600-11e5-ac8a-bb6015f4022c
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 44
                  Date: Tue, 29 Mar 2016 22:46:36 GMT
                  {
                    "agentPreviews": [
                      {
                        "hostname": "example",
                        "agentId": "i-49113b93",
                        "autoScalingGroup": "example",
                        "agentHealth": HEALTHY,
                        "agentVersion": "exampleversion",
                        "operatingSystem": "exampleOS",
                        "kernelVersion": "examplekernelversion",
                        "ipv4Address": "example"
                      }
                    ]
                  }
```

## See Also
<a name="API_PreviewAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/PreviewAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/PreviewAgents)
