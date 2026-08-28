---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Lists the applications registered with the user or AWS account.

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="CodeDeploy-ListApplications-request-nextToken"></a>
An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.
Type: String
Required: No

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
{
   "applications": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_ListApplications_ResponseSyntax) **   <a name="CodeDeploy-ListApplications-response-applications"></a>
A list of application names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="CodeDeploy-ListApplications-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications in the list.
Type: String

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_ListApplications_Examples"></a>

### Example
<a name="API_ListApplications_Example_1"></a>

This example illustrates one usage of ListApplications.

#### Sample Request
<a name="API_ListApplications_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodeDeploy_20141006.ListApplications
X-Amz-Date: 20160707T021119Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListApplications_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: aa51ec1f-88e2-11e5-9958-cd5094947bf1
Content-Type: application/x-amz-json-1.1
Content-Length: 211

{
    "applications": [
        "TestApp-eu-west-1",
        "ProductionApp-us-west-2",
        "TestApp-us-east-1",
        "ProductionApp-us-east-1",
        "TestApp-ap-northeast-1",
        "ProductionApp-eu-central-1",
        "ProductionApp-us-west-2"
    ]
}
```

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
