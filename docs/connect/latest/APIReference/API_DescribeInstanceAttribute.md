---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeInstanceAttribute.html
---

# DescribeInstanceAttribute
<a name="API_DescribeInstanceAttribute"></a>

This API is in preview release for Connect Customer and is subject to change.

Describes the specified instance attribute.

## Request Syntax
<a name="API_DescribeInstanceAttribute_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/attribute/{{AttributeType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInstanceAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeType](#API_DescribeInstanceAttribute_RequestSyntax) **   <a name="connect-DescribeInstanceAttribute-request-uri-AttributeType"></a>
The type of attribute.
Valid Values: `INBOUND_CALLS | OUTBOUND_CALLS | CONTACTFLOW_LOGS | CONTACT_LENS | AUTO_RESOLVE_BEST_VOICES | USE_CUSTOM_TTS_VOICES | EARLY_MEDIA | MULTI_PARTY_CONFERENCE | HIGH_VOLUME_OUTBOUND | ENHANCED_CONTACT_MONITORING | ENHANCED_CHAT_MONITORING | MULTI_PARTY_CHAT_CONFERENCE | MESSAGE_STREAMING`
Required: Yes

 ** [InstanceId](#API_DescribeInstanceAttribute_RequestSyntax) **   <a name="connect-DescribeInstanceAttribute-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeInstanceAttribute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInstanceAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attribute": {
      "AttributeType": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_DescribeInstanceAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attribute](#API_DescribeInstanceAttribute_ResponseSyntax) **   <a name="connect-DescribeInstanceAttribute-response-Attribute"></a>
The type of attribute.
Type: [Attribute](API_Attribute.md) object

## Errors
<a name="API_DescribeInstanceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeInstanceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeInstanceAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
