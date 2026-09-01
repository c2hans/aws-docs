---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentInstances.html
---

# ListDeploymentInstances
<a name="API_ListDeploymentInstances"></a>

**Note**
 The newer `BatchGetDeploymentTargets` should be used instead because it works with all compute types. `ListDeploymentInstances` throws an exception if it is used with a compute platform other than EC2/On-premises or AWS Lambda.

 Lists the instance for a deployment associated with the user or AWS account.

## Request Syntax
<a name="API_ListDeploymentInstances_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "instanceStatusFilter": [ "{{string}}" ],
   "instanceTypeFilter": [ "{{string}}" ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeploymentInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_ListDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [instanceStatusFilter](#API_ListDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-request-instanceStatusFilter"></a>
A subset of instances to list by status:
+  `Pending`: Include those instances with pending deployments.
+  `InProgress`: Include those instances where deployments are still in progress.
+  `Succeeded`: Include those instances with successful deployments.
+  `Failed`: Include those instances with failed deployments.
+  `Skipped`: Include those instances with skipped deployments.
+  `Unknown`: Include those instances with deployments in an unknown state.
Type: Array of strings
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

 ** [instanceTypeFilter](#API_ListDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-request-instanceTypeFilter"></a>
The set of instances in a blue/green deployment, either those in the original environment ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance information.
Type: Array of strings
Valid Values: `Blue | Green`
Required: No

 ** [nextToken](#API_ListDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-request-nextToken"></a>
An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.
Type: String
Required: No

## Response Syntax
<a name="API_ListDeploymentInstances_ResponseSyntax"></a>

```
{
   "instancesList": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeploymentInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instancesList](#API_ListDeploymentInstances_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-response-instancesList"></a>
A list of instance IDs.
Type: Array of strings

 ** [nextToken](#API_ListDeploymentInstances_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentInstances-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment instances call to return the next set of deployment instances in the list.
Type: String

## Errors
<a name="API_ListDeploymentInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** DeploymentNotStartedException **
The specified deployment has not started.
HTTP Status Code: 400

 ** InvalidComputePlatformException **
The computePlatform is invalid. The computePlatform should be `Lambda`, `Server`, or `ECS`.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentInstanceTypeException **
An instance type was specified for an in-place deployment. Instance types are supported for blue/green deployments only.
HTTP Status Code: 400

 ** InvalidInstanceStatusException **
The specified instance status does not exist.
HTTP Status Code: 400

 ** InvalidInstanceTypeException **
An invalid instance type was specified for instances in a blue/green deployment. Valid values include "Blue" for an original environment and "Green" for a replacement environment.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTargetFilterNameException **
 The target filter name is invalid.
HTTP Status Code: 400

## Examples
<a name="API_ListDeploymentInstances_Examples"></a>

### Example
<a name="API_ListDeploymentInstances_Example_1"></a>

This example illustrates one usage of ListDeploymentInstances.

#### Sample Request
<a name="API_ListDeploymentInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.ListDeploymentInstances
X-Amz-Date: 20160707T021610Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
	"deploymentId": "d-74D25NS7C"
}
```

#### Sample Response
<a name="API_ListDeploymentInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 57a7b3d6-88e3-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 32

{
    "instancesList": [
        "i-b2f7jf0d00EXAMPLE"
    ]
}
```

## See Also
<a name="API_ListDeploymentInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListDeploymentInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListDeploymentInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
