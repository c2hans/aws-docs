---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_TagResource.html
---

# TagResource
<a name="API_cur_TagResource"></a>

Associates a set of tags with a report definition.

## Request Syntax
<a name="API_cur_TagResource_RequestSyntax"></a>

```
{
   "ReportName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_cur_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReportName](#API_cur_TagResource_RequestSyntax) **   <a name="awscostmanagement-cur_TagResource-request-ReportName"></a>
The report name of the report definition that tags are to be associated with.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[0-9A-Za-z!\-_.*\'()]+`
Required: Yes

 ** [Tags](#API_cur_TagResource_RequestSyntax) **   <a name="awscostmanagement-cur_TagResource-request-Tags"></a>
The tags to be assigned to the report definition resource.
Type: Array of [Tag](API_cur_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_cur_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_cur_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified report (`ReportName`) in the request doesn't exist.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 400

## Examples
<a name="API_cur_TagResource_Examples"></a>

### The following is a sample request of the TagResource operation.
<a name="API_cur_TagResource_Example_1"></a>

This example illustrates one usage of TagResource.

#### Sample Request
<a name="API_cur_TagResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.cur.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSOrigamiServiceGateway.TagResource
{
  "ReportName": "ExampleReport",
  "Tags": [
    {
      "Key": "key-1",
      "Value": "value-1"
    }
  ]
}
```

## See Also
<a name="API_cur_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cur-2017-01-06/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cur-2017-01-06/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cur-2017-01-06/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cur-2017-01-06/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cur-2017-01-06/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cur-2017-01-06/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cur-2017-01-06/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
