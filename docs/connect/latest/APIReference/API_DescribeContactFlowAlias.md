---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContactFlowAlias.html
---

# DescribeContactFlowAlias
<a name="API_DescribeContactFlowAlias"></a>

Returns information about a specific flow alias, including the version that it points to.

## Request Syntax
<a name="API_DescribeContactFlowAlias_RequestSyntax"></a>

```
GET /contact-flows/{{InstanceId}}/{{ContactFlowId}}/alias/{{AliasId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeContactFlowAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasId](#API_DescribeContactFlowAlias_RequestSyntax) **   <a name="connect-DescribeContactFlowAlias-request-uri-AliasId"></a>
The identifier of the alias.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [ContactFlowId](#API_DescribeContactFlowAlias_RequestSyntax) **   <a name="connect-DescribeContactFlowAlias-request-uri-ContactFlowId"></a>
The identifier of the flow.
Required: Yes

 ** [InstanceId](#API_DescribeContactFlowAlias_RequestSyntax) **   <a name="connect-DescribeContactFlowAlias-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeContactFlowAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeContactFlowAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowAlias": {
      "AliasId": "string",
      "ContactFlowArn": "string",
      "ContactFlowId": "string",
      "Description": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Version": number
   }
}
```

## Response Elements
<a name="API_DescribeContactFlowAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowAlias](#API_DescribeContactFlowAlias_ResponseSyntax) **   <a name="connect-DescribeContactFlowAlias-response-ContactFlowAlias"></a>
Information about the flow alias.
Type: [ContactFlowAliasInfo](API_ContactFlowAliasInfo.md) object

## Errors
<a name="API_DescribeContactFlowAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

## Examples
<a name="API_DescribeContactFlowAlias_Examples"></a>

### Sample Response
<a name="API_DescribeContactFlowAlias_Example_1"></a>

This example illustrates one usage of DescribeContactFlowAlias.

```
{
  "ContactFlowAlias": {
    "ContactFlowId": "abcdefgh-1234-5678-9012-abcdefghijkl",
    "ContactFlowArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/contact-flow/abcdefgh-1234-5678-9012-abcdefghijkl",
    "AliasId": "87654321-4321-4321-4321-210987654321",
    "Version": 2,
    "Name": "production",
    "Description": "Production version of the customer service flow",
    "LastModifiedRegion": "us-west-2",
    "LastModifiedTime": "2026-09-15T10:30:00.000Z"
  }
}
```

## See Also
<a name="API_DescribeContactFlowAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeContactFlowAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeContactFlowAlias)
