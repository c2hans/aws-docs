---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateAppVersionResource.html
---

# CreateAppVersionResource
<a name="API_CreateAppVersionResource"></a>

Adds a resource to the AWS Resilience Hub application and assigns it to the specified AppComponents. If you specify a new AppComponent, AWS Resilience Hub will automatically create the AppComponent.

**Note**
This action has no effect outside AWS Resilience Hub.
This API updates the AWS Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the AWS Resilience Hub application using the `PublishAppVersion` API.
To update application version with new `physicalResourceID`, you must call `ResolveAppVersionResources` API.
 AWS Resilience Hub blocks manual grouping and automatically groups certain resources based on their dependencies and configurations to prevent configuration errors and ensure accurate resilience assessment results. For more information, see [Managing Application Components](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.html).

## Request Syntax
<a name="API_CreateAppVersionResource_RequestSyntax"></a>

```
POST /create-app-version-resource HTTP/1.1
Content-type: application/json

{
   "additionalInfo": {
      "{{string}}" : [ "{{string}}" ]
   },
   "appArn": "{{string}}",
   "appComponents": [ "{{string}}" ],
   "awsAccountId": "{{string}}",
   "awsRegion": "{{string}}",
   "clientToken": "{{string}}",
   "logicalResourceId": {
      "eksSourceName": "{{string}}",
      "identifier": "{{string}}",
      "logicalStackName": "{{string}}",
      "resourceGroupName": "{{string}}",
      "terraformSourceName": "{{string}}"
   },
   "physicalResourceId": "{{string}}",
   "resourceName": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAppVersionResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAppVersionResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalInfo](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-additionalInfo"></a>
Currently, there is no supported additional information for resources.
Type: String to array of strings map
Key Pattern: `\S{1,128}`
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [appArn](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [appComponents](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-appComponents"></a>
List of AppComponents that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [awsAccountId](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-awsAccountId"></a>
 AWS account that owns the physical resource.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [awsRegion](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-awsRegion"></a>
 AWS region that owns the physical resource.
Type: String
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** [clientToken](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [logicalResourceId](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-logicalResourceId"></a>
Logical identifier of the resource.
Type: [LogicalResourceId](API_LogicalResourceId.md) object
Required: Yes

 ** [physicalResourceId](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-physicalResourceId"></a>
Physical identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [resourceName](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-resourceName"></a>
Name of the resource.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** [resourceType](#API_CreateAppVersionResource_RequestSyntax) **   <a name="resiliencehub-CreateAppVersionResource-request-resourceType"></a>
Type of resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_CreateAppVersionResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appVersion": "string",
   "physicalResource": {
      "additionalInfo": {
         "string" : [ "string" ]
      },
      "appComponents": [
         {
            "additionalInfo": {
               "string" : [ "string" ]
            },
            "id": "string",
            "name": "string",
            "type": "string"
         }
      ],
      "excluded": boolean,
      "logicalResourceId": {
         "eksSourceName": "string",
         "identifier": "string",
         "logicalStackName": "string",
         "resourceGroupName": "string",
         "terraformSourceName": "string"
      },
      "parentResourceName": "string",
      "physicalResourceId": {
         "awsAccountId": "string",
         "awsRegion": "string",
         "identifier": "string",
         "type": "string"
      },
      "resourceName": "string",
      "resourceType": "string",
      "sourceType": "string"
   }
}
```

## Response Elements
<a name="API_CreateAppVersionResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_CreateAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-CreateAppVersionResource-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_CreateAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-CreateAppVersionResource-response-appVersion"></a>
 AWS Resilience Hub application version.
Type: String
Pattern: `\S{1,50}`

 ** [physicalResource](#API_CreateAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-CreateAppVersionResource-response-physicalResource"></a>
Defines a physical resource. A physical resource is a resource that exists in your account. It can be identified using an Amazon Resource Name (ARN) or a Resilience Hub-native identifier.
Type: [PhysicalResource](API_PhysicalResource.md) object

## Errors
<a name="API_CreateAppVersionResource_Errors"></a>

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
<a name="API_CreateAppVersionResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/CreateAppVersionResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/CreateAppVersionResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
