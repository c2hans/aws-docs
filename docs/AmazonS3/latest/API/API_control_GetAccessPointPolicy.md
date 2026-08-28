---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html
---

# GetAccessPointPolicy
<a name="API_control_GetAccessPointPolicy"></a>

Returns the access point policy associated with the specified access point.

The following actions are related to `GetAccessPointPolicy`:
+  [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)
+  [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)

## Request Syntax
<a name="API_control_GetAccessPointPolicy_RequestSyntax"></a>

```
GET /v20180820/accesspoint/{{name}}/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPointPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicy-request-uri-uri-Name"></a>
The name of the access point whose policy you want to retrieve.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the access point accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name>`. For example, to access the access point `reports-ap` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap`. The value must be URL encoded.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicy-request-header-AccountId"></a>
The account ID for the account that owns the specified access point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPointPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPointPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointPolicyResult>
   <Policy>string</Policy>
</GetAccessPointPolicyResult>
```

## Response Elements
<a name="API_control_GetAccessPointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointPolicyResult](#API_control_GetAccessPointPolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicy-response-GetAccessPointPolicyResult"></a>
Root level tag for the GetAccessPointPolicyResult parameters.
Required: Yes

 ** [Policy](#API_control_GetAccessPointPolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicy-response-Policy"></a>
The access point policy associated with the specified access point.
Type: String

## Examples
<a name="API_control_GetAccessPointPolicy_Examples"></a>

### Sample request
<a name="API_control_GetAccessPointPolicy_Example_1"></a>

The following request returns the access point of the specified Amazon S3 on Outposts.

```
           GET /v20180820/accesspoint/example-access-point/policy  HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2020 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: 123456789012
           x-amz-outpost-id: op-123456
```

## See Also
<a name="API_control_GetAccessPointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
