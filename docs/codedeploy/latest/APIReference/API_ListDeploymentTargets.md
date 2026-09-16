---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentTargets.html
---

# ListDeploymentTargets
<a name="API_ListDeploymentTargets"></a>

 Returns an array of target IDs that are associated a deployment.

## Request Syntax
<a name="API_ListDeploymentTargets_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "nextToken": "{{string}}",
   "targetFilters": {
      "{{string}}" : [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_ListDeploymentTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_ListDeploymentTargets_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentTargets-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [nextToken](#API_ListDeploymentTargets_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentTargets-request-nextToken"></a>
 A token identifier returned from the previous `ListDeploymentTargets` call. It can be used to return the next set of deployment targets in the list.
Type: String
Required: No

 ** [targetFilters](#API_ListDeploymentTargets_RequestSyntax) **   <a name="CodeDeploy-ListDeploymentTargets-request-targetFilters"></a>
 A key used to filter the returned targets. The two valid values are:
+  `TargetStatus` - A `TargetStatus` filter string can be `Failed`, `InProgress`, `Pending`, `Ready`, `Skipped`, `Succeeded`, or `Unknown`.
+  `ServerInstanceLabel` - A `ServerInstanceLabel` filter string can be `Blue` or `Green`.
Type: String to array of strings map
Valid Keys: `TargetStatus | ServerInstanceLabel`
Required: No

## Response Syntax
<a name="API_ListDeploymentTargets_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "targetIds": [ "string" ]
}
```

## Response Elements
<a name="API_ListDeploymentTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDeploymentTargets_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentTargets-response-nextToken"></a>
 If a large amount of information is returned, a token identifier is also returned. It can be used in a subsequent `ListDeploymentTargets` call to return the next set of deployment targets in the list.
Type: String

 ** [targetIds](#API_ListDeploymentTargets_ResponseSyntax) **   <a name="CodeDeploy-ListDeploymentTargets-response-targetIds"></a>
 The unique IDs of deployment targets.
Type: Array of strings

## Errors
<a name="API_ListDeploymentTargets_Errors"></a>

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

## See Also
<a name="API_ListDeploymentTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListDeploymentTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListDeploymentTargets)
