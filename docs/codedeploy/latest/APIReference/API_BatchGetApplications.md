---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplications.html
---

# BatchGetApplications
<a name="API_BatchGetApplications"></a>

Gets information about one or more applications. The maximum number of applications that can be returned is 100.

## Request Syntax
<a name="API_BatchGetApplications_RequestSyntax"></a>

```
{
   "applicationNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetApplications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationNames](#API_BatchGetApplications_RequestSyntax) **   <a name="CodeDeploy-BatchGetApplications-request-applicationNames"></a>
A list of application names separated by spaces. The maximum number of application names you can specify is 100.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_BatchGetApplications_ResponseSyntax"></a>

```
{
   "applicationsInfo": [
      {
         "applicationId": "string",
         "applicationName": "string",
         "computePlatform": "string",
         "createTime": number,
         "gitHubAccountName": "string",
         "linkedToGitHub": boolean
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationsInfo](#API_BatchGetApplications_ResponseSyntax) **   <a name="CodeDeploy-BatchGetApplications-response-applicationsInfo"></a>
Information about the applications.
Type: Array of [ApplicationInfo](API_ApplicationInfo.md) objects

## Errors
<a name="API_BatchGetApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetApplications_Examples"></a>

### Example
<a name="API_BatchGetApplications_Example_1"></a>

This example illustrates one usage of BatchGetApplications.

#### Sample Request
<a name="API_BatchGetApplications_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 81
X-Amz-Target: CodeDeploy_20141006.BatchGetApplications
X-Amz-Date: 20160707T230945Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationNames": [
        "ProductionApp-us-east-1",
        "ProductionApp-us-west-2"
    ]
}
```

#### Sample Response
<a name="API_BatchGetApplications_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4ccc9cf0-88c9-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 335

{
    "applicationsInfo": [
        {
            "applicationId": "d8347436-bc51-459e-9c44-f98abEXAMPLE",
            "applicationName": "ProductionApp-us-west-2",
            "createTime": 1446136767.311,
            "linkedToGitHub": false
        },
        {
            "applicationId": "1ecfe802-63f1-4038-8f0d-06688EXAMPLE",
            "applicationName": "ProductionApp-us-east-1",
            "createTime": 1439488406.152,
            "linkedToGitHub": false
        }
    ]
}
```

## See Also
<a name="API_BatchGetApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
