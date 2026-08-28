---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateApp.html
---

# CreateApp
<a name="API_CreateApp"></a>

Creates an AWS Resilience Hub application. An AWS Resilience Hub application is a collection of AWS resources structured to prevent and recover AWS application disruptions. To describe a AWS Resilience Hub application, you provide an application name, resources from one or more AWS CloudFormation stacks, AWS Resource Groups, Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub).

After you create an AWS Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).

## Request Syntax
<a name="API_CreateApp_RequestSyntax"></a>

```
POST /create-app HTTP/1.1
Content-type: application/json

{
   "assessmentSchedule": "{{string}}",
   "awsApplicationArn": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "eventSubscriptions": [
      {
         "eventType": "{{string}}",
         "name": "{{string}}",
         "snsTopicArn": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "permissionModel": {
      "crossAccountRoleArns": [ "{{string}}" ],
      "invokerRoleName": "{{string}}",
      "type": "{{string}}"
   },
   "policyArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApp_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentSchedule](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-assessmentSchedule"></a>
 Assessment execution schedule with 'Daily' or 'Disabled' values.
Type: String
Valid Values: `Disabled | Daily`
Required: No

 ** [awsApplicationArn](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-awsApplicationArn"></a>
Amazon Resource Name (ARN) of AWS Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [clientToken](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [description](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-description"></a>
The optional description for an app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [eventSubscriptions](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-eventSubscriptions"></a>
The list of events you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports only **Drift detected** and **Scheduled assessment failure** events notification.
Type: Array of [EventSubscription](API_EventSubscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [name](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-name"></a>
Name of the application.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [permissionModel](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-permissionModel"></a>
Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
Type: [PermissionModel](API_PermissionModel.md) object
Required: No

 ** [policyArn](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-policyArn"></a>
Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:resiliency-policy/`policy-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [tags](#API_CreateApp_RequestSyntax) **   <a name="resiliencehub-CreateApp-request-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## Response Syntax
<a name="API_CreateApp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "app": {
      "appArn": "string",
      "assessmentSchedule": "string",
      "awsApplicationArn": "string",
      "complianceStatus": "string",
      "creationTime": number,
      "description": "string",
      "driftStatus": "string",
      "eventSubscriptions": [
         {
            "eventType": "string",
            "name": "string",
            "snsTopicArn": "string"
         }
      ],
      "lastAppComplianceEvaluationTime": number,
      "lastDriftEvaluationTime": number,
      "lastResiliencyScoreEvaluationTime": number,
      "name": "string",
      "permissionModel": {
         "crossAccountRoleArns": [ "string" ],
         "invokerRoleName": "string",
         "type": "string"
      },
      "policyArn": "string",
      "resiliencyScore": number,
      "rpoInSecs": number,
      "rtoInSecs": number,
      "status": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [app](#API_CreateApp_ResponseSyntax) **   <a name="resiliencehub-CreateApp-response-app"></a>
The created application returned as an object with details including compliance status, creation time, description, resiliency score, and more.
Type: [App](API_App.md) object

## Errors
<a name="API_CreateApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 409

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/CreateApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/CreateApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
