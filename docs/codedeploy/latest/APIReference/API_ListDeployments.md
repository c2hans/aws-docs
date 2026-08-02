---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeployments.html
---

# ListDeployments
<a name="API_ListDeployments"></a>

Lists the deployments in a deployment group for an application registered with the user or AWS account.

## Request Syntax
<a name="API_ListDeployments_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "createTimeRange": {
      "end": {{number}},
      "start": {{number}}
   },
   "deploymentGroupName": "{{string}}",
   "externalId": "{{string}}",
   "includeOnlyStatuses": [ "{{string}}" ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
If `applicationName` is specified, then `deploymentGroupName` must be specified. If it is not specified, then `deploymentGroupName` must not be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [createTimeRange](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-createTimeRange"></a>
A time range (start and end) for returning a subset of the list of deployments.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** [deploymentGroupName](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-deploymentGroupName"></a>
The name of a deployment group for the specified application.
If `deploymentGroupName` is specified, then `applicationName` must be specified. If it is not specified, then `applicationName` must not be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [externalId](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-externalId"></a>
The unique ID of an external resource for returning deployments linked to the external resource.
Type: String
Required: No

 ** [includeOnlyStatuses](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-includeOnlyStatuses"></a>
A subset of deployments to list by status:
+  `Created`: Include created deployments in the resulting list.
+  `Queued`: Include queued deployments in the resulting list.
+  `In Progress`: Include in-progress deployments in the resulting list.
+  `Succeeded`: Include successful deployments in the resulting list.
+  `Failed`: Include failed deployments in the resulting list.
+  `Stopped`: Include stopped deployments in the resulting list.
Type: Array of strings
Valid Values: `Created | Queued | InProgress | Baking | Succeeded | Failed | Stopped | Ready`
Required: No

 ** [nextToken](#API_ListDeployments_RequestSyntax) **   <a name="CodeDeploy-ListDeployments-request-nextToken"></a>
An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.
Type: String
Required: No

## Response Syntax
<a name="API_ListDeployments_ResponseSyntax"></a>

```
{
   "deployments": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployments](#API_ListDeployments_ResponseSyntax) **   <a name="CodeDeploy-ListDeployments-response-deployments"></a>
A list of deployment IDs.
Type: Array of strings

 ** [nextToken](#API_ListDeployments_ResponseSyntax) **   <a name="CodeDeploy-ListDeployments-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployments call to return the next set of deployments in the list.
Type: String

## Errors
<a name="API_ListDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentGroupNameRequiredException **
The deployment group name was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentGroupNameException **
The deployment group name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentStatusException **
The specified deployment status doesn't exist or cannot be determined.
HTTP Status Code: 400

 ** InvalidExternalIdException **
The external ID was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidInputException **
The input was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTimeRangeException **
The specified time range was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_ListDeployments_Examples"></a>

### Example
<a name="API_ListDeployments_Example_1"></a>

This example illustrates one usage of ListDeployments.

#### Sample Request
<a name="API_ListDeployments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 99
X-Amz-Target: CodeDeploy_20141006.ListDeployments
X-Amz-Date: 20160707T021907Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
	"applicationName": "TestApp-us-east-1",
	"deploymentGroupName": "dep-group-def-456"
}
```

#### Sample Response
<a name="API_ListDeployments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: c15efe85-88e3-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 45

{
    "deployments": [
        "d-74D87AS7C",
        "d-D1EGTDV4C"
    ]
}
```

## See Also
<a name="API_ListDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListDeployments)
