---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentGroups.html
---

# ListDeploymentGroups
<a name="API_ListDeploymentGroups"></a>

Lists the deployment groups for an application registered with the AWS user or AWS account.

## Request Syntax
<a name="API_ListDeploymentGroups_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeploymentGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_ListDeploymentGroups_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentGroups-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

 ** [nextToken](#API_ListDeploymentGroups_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentGroups-request-nextToken"></a>
An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.
Type: String
Required: No

## Response Syntax
<a name="API_ListDeploymentGroups_ResponseSyntax"></a>

```
{
   "applicationName": "string",
   "deploymentGroups": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeploymentGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationName](#API_ListDeploymentGroups_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentGroups-response-applicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`

 ** [deploymentGroups](#API_ListDeploymentGroups_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentGroups-response-deploymentGroups"></a>
A list of deployment group names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`

 ** [nextToken](#API_ListDeploymentGroups_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentGroups-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment groups call to return the next set of deployment groups in the list.
Type: String

## Errors
<a name="API_ListDeploymentGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_ListDeploymentGroups_Examples"></a>

### Example
<a name="API_ListDeploymentGroups_Example_1"></a>

This example illustrates one usage of ListDeploymentGroups.

#### Sample Request
<a name="API_ListDeploymentGroups_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: CodeDeploy_20141006.ListDeploymentGroups
X-Amz-Date: 20160707T021406Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
	"applicationName": "TestApp-us-east-1"
}
```

#### Sample Response
<a name="API_ListDeploymentGroups_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0f5599cb-88e3-11e5-a087-ab26ee53e16e
Content-Type: application/x-amz-json-1.1
Content-Length: 95

{
    "applicationName": "TestApp-us-east-1",
    "deploymentGroups": [
        "dep-group-def-456"
    ]
}
```

## See Also
<a name="API_ListDeploymentGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListDeploymentGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListDeploymentGroups)
