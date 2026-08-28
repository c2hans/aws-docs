---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContactFlow.html
---

# DescribeContactFlow
<a name="API_DescribeContactFlow"></a>

Describes the specified flow.

You can also create and update flows using the [Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html).

Use the `$SAVED` alias in the request to describe the `SAVED` content of a Flow. For example, `arn:aws:.../contact-flow/{id}:$SAVED`. After a flow is published, `$SAVED` needs to be supplied to view saved content that has not been published.

Use `arn:aws:.../contact-flow/{id}:{version}` to retrieve the content of a specific flow version.

In the response, **Status** indicates the flow status as either `SAVED` or `PUBLISHED`. The `PUBLISHED` status will initiate validation on the content. `SAVED` does not initiate validation of the content. `SAVED` \| `PUBLISHED`

## Request Syntax
<a name="API_DescribeContactFlow_RequestSyntax"></a>

```
GET /contact-flows/{{InstanceId}}/{{ContactFlowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeContactFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowId](#API_DescribeContactFlow_RequestSyntax) **   <a name="connect-DescribeContactFlow-request-uri-ContactFlowId"></a>
The identifier of the flow.
Length Constraints: Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_DescribeContactFlow_RequestSyntax) **   <a name="connect-DescribeContactFlow-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeContactFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeContactFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlow": {
      "Arn": "string",
      "Content": "string",
      "Description": "string",
      "FlowContentSha256": "string",
      "Id": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "State": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "Type": "string",
      "Version": number,
      "VersionDescription": "string"
   }
}
```

## Response Elements
<a name="API_DescribeContactFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlow](#API_DescribeContactFlow_ResponseSyntax) **   <a name="connect-DescribeContactFlow-response-ContactFlow"></a>
Information about the flow.
Type: [ContactFlow](API_ContactFlow.md) object

## Errors
<a name="API_DescribeContactFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ContactFlowNotPublishedException **
The flow has not been published.
HTTP Status Code: 404

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
<a name="API_DescribeContactFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeContactFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeContactFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
