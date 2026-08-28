---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html
---

# CreateDeployment
<a name="API_CreateDeployment"></a>

Deploys an application revision through the specified deployment group.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "autoRollbackConfiguration": {
      "enabled": {{boolean}},
      "events": [ "{{string}}" ]
   },
   "deploymentConfigName": "{{string}}",
   "deploymentGroupName": "{{string}}",
   "description": "{{string}}",
   "fileExistsBehavior": "{{string}}",
   "ignoreApplicationStopFailures": {{boolean}},
   "overrideAlarmConfiguration": {
      "alarms": [
         {
            "name": "{{string}}"
         }
      ],
      "enabled": {{boolean}},
      "ignorePollAlarmFailure": {{boolean}}
   },
   "revision": {
      "appSpecContent": {
         "content": "{{string}}",
         "sha256": "{{string}}"
      },
      "gitHubLocation": {
         "commitId": "{{string}}",
         "repository": "{{string}}"
      },
      "revisionType": "{{string}}",
      "s3Location": {
         "bucket": "{{string}}",
         "bundleType": "{{string}}",
         "eTag": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      },
      "string": {
         "content": "{{string}}",
         "sha256": "{{string}}"
      }
   },
   "targetInstances": {
      "autoScalingGroups": [ "{{string}}" ],
      "ec2TagSet": {
         "ec2TagSetList": [
            [
               {
                  "Key": "{{string}}",
                  "Type": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         ]
      },
      "tagFilters": [
         {
            "Key": "{{string}}",
            "Type": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "updateOutdatedInstancesOnly": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [autoRollbackConfiguration](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-autoRollbackConfiguration"></a>
Configuration information for an automatic rollback that is added when a deployment is created.
Type: [AutoRollbackConfiguration](API_AutoRollbackConfiguration.md) object
Required: No

 ** [deploymentConfigName](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-deploymentConfigName"></a>
The name of a deployment configuration associated with the user or AWS account.
If not specified, the value configured in the deployment group is used as the default. If the deployment group does not have a deployment configuration associated with it, `CodeDeployDefault`.`OneAtATime` is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [deploymentGroupName](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-deploymentGroupName"></a>
The name of the deployment group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [description](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-description"></a>
A comment about the deployment.
Type: String
Required: No

 ** [fileExistsBehavior](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-fileExistsBehavior"></a>
Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.
The `fileExistsBehavior` parameter takes any of the following values:
+ DISALLOW: The deployment fails. This is also the default behavior if no option is specified.
+ OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.
+ RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.
Type: String
Valid Values: `DISALLOW | OVERWRITE | RETAIN`
Required: No

 ** [ignoreApplicationStopFailures](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-ignoreApplicationStopFailures"></a>
 If true, then if an `ApplicationStop`, `BeforeBlockTraffic`, or `AfterBlockTraffic` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if `ApplicationStop` fails, the deployment continues with `DownloadBundle`. If `BeforeBlockTraffic` fails, the deployment continues with `BlockTraffic`. If `AfterBlockTraffic` fails, the deployment continues with `ApplicationStop`.
 If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.
 During a deployment, the AWS CodeDeploy agent runs the scripts specified for `ApplicationStop`, `BeforeBlockTraffic`, and `AfterBlockTraffic` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.
 If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use `ignoreApplicationStopFailures` to specify that the `ApplicationStop`, `BeforeBlockTraffic`, and `AfterBlockTraffic` failures should be ignored.
Type: Boolean
Required: No

 ** [overrideAlarmConfiguration](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-overrideAlarmConfiguration"></a>
Allows you to specify information about alarms associated with a deployment. The alarm configuration that you specify here will override the alarm configuration at the deployment group level. Consider overriding the alarm configuration if you have set up alarms at the deployment group level that are causing deployment failures. In this case, you would call `CreateDeployment` to create a new deployment that uses a previous application revision that is known to work, and set its alarm configuration to turn off alarm polling. Turning off alarm polling ensures that the new deployment proceeds without being blocked by the alarm that was generated by the previous, failed, deployment.
If you specify an `overrideAlarmConfiguration`, you need the `UpdateDeploymentGroup` IAM permission when calling `CreateDeployment`.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [revision](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-revision"></a>
 The type and location of the revision to deploy.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: No

 ** [targetInstances](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-targetInstances"></a>
 Information about the instances that belong to the replacement environment in a blue/green deployment.
Type: [TargetInstances](API_TargetInstances.md) object
Required: No

 ** [updateOutdatedInstancesOnly](#API_CreateDeployment_RequestSyntax) **   <a name="CodeDeploy-CreateDeployment-request-updateOutdatedInstancesOnly"></a>
 Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
{
   "deploymentId": "string"
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentId](#API_CreateDeployment_ResponseSyntax) **   <a name="CodeDeploy-CreateDeployment-response-deploymentId"></a>
 The unique ID of a deployment.
Type: String

## Errors
<a name="API_CreateDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlarmsLimitExceededException **
The maximum number of alarms for a deployment group (10) was exceeded.
HTTP Status Code: 400

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** DeploymentConfigDoesNotExistException **
The deployment configuration does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentGroupNameRequiredException **
The deployment group name was not specified.
HTTP Status Code: 400

 ** DeploymentLimitExceededException **
The number of allowed deployments was exceeded.
HTTP Status Code: 400

 ** DescriptionTooLongException **
The description is too long.
HTTP Status Code: 400

 ** InvalidAlarmConfigException **
The format of the alarm configuration is invalid. Possible causes include:
+ The alarm list is null.
+ The alarm object is null.
+ The alarm name is empty or null or exceeds the limit of 255 characters.
+ Two alarms with the same name have been specified.
+ The alarm configuration is enabled, but the alarm list is empty.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidAutoRollbackConfigException **
The automatic rollback configuration was specified in an invalid format. For example, automatic rollback is enabled, but an invalid triggering event type or no event types were listed.
HTTP Status Code: 400

 ** InvalidAutoScalingGroupException **
The Auto Scaling group was specified in an invalid format or does not exist.
HTTP Status Code: 400

 ** InvalidDeploymentConfigNameException **
The deployment configuration name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentGroupNameException **
The deployment group name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidFileExistsBehaviorException **
An invalid fileExistsBehavior option was specified to determine how AWS CodeDeploy handles files or directories that already exist in a deployment target location, but weren't part of the previous successful deployment. Valid values include "DISALLOW," "OVERWRITE," and "RETAIN."
HTTP Status Code: 400

 ** InvalidGitHubAccountTokenException **
The GitHub token is not valid.
HTTP Status Code: 400

 ** InvalidIgnoreApplicationStopFailuresValueException **
The IgnoreApplicationStopFailures value is invalid. For AWS Lambda deployments, `false` is expected. For EC2/On-premises deployments, `true` or `false` is expected.
HTTP Status Code: 400

 ** InvalidLoadBalancerInfoException **
An invalid load balancer name, or no load balancer name, was specified.
HTTP Status Code: 400

 ** InvalidRevisionException **
The revision was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidRoleException **
The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.
HTTP Status Code: 400

 ** InvalidTargetInstancesException **
The target instance configuration is invalid. Possible causes include:
+ Configuration data for target instances was entered for an in-place deployment.
+ The limit of 10 tags for a tag type was exceeded.
+ The combined length of the tag names exceeded the limit.
+ A specified tag is not currently applied to any instances.
HTTP Status Code: 400

 ** InvalidTrafficRoutingConfigurationException **
 The configuration that specifies how traffic is routed during a deployment is invalid.
HTTP Status Code: 400

 ** InvalidUpdateOutdatedInstancesOnlyValueException **
The UpdateOutdatedInstancesOnly value is invalid. For AWS Lambda deployments, `false` is expected. For EC2/On-premises deployments, `true` or `false` is expected.
HTTP Status Code: 400

 ** RevisionDoesNotExistException **
The named revision does not exist with the user or AWS account.
HTTP Status Code: 400

 ** RevisionRequiredException **
The revision ID was not specified.
HTTP Status Code: 400

 ** ThrottlingException **
An API function was called too frequently.
HTTP Status Code: 400

## Examples
<a name="API_CreateDeployment_Examples"></a>

### Example
<a name="API_CreateDeployment_Example_1"></a>

This example illustrates one usage of CreateDeployment.

#### Sample Request
<a name="API_CreateDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 305
X-Amz-Target: CodeDeploy_20141006.CreateDeployment
X-Amz-Date: 20160707T235543Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-ap-southeast-2",
    "autoRollbackConfiguration": {
        "enabled": true,
        "events": [
            "DEPLOYMENT_FAILURE"
        ]
    },
    "deploymentGroupName": "dep-group-ghi-789",
    "description": "Deployment for Project 1234",
    "deploymentConfigName": "CodeDeployDefault.OneAtATime",
    "ignoreApplicationStopFailures": true,
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bundleType": "zip",
            "bucket": "project-1234",
            "key": "East-App.zip"
        },
        "updateOutdatedInstancesOnly": true
    }
}
```

#### Sample Response
<a name="API_CreateDeployment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b8d39558-88cf-11f5-96e5-8bf4ee0ce84e
Content-Type: application/x-amz-json-1.1
Content-Length: 30

{
    "deploymentId": "d-IIMHK0NHC"
}
```

## See Also
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/CreateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/CreateDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
