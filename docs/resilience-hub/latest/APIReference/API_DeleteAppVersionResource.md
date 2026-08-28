---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteAppVersionResource.html
---

# DeleteAppVersionResource
<a name="API_DeleteAppVersionResource"></a>

Deletes a resource from the AWS Resilience Hub application.

**Note**
You can only delete a manually added resource. To exclude non-manually added resources, use the `UpdateAppVersionResource` API.
This action has no effect outside AWS Resilience Hub.
This API updates the AWS Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the AWS Resilience Hub application using the `PublishAppVersion` API.

## Request Syntax
<a name="API_DeleteAppVersionResource_RequestSyntax"></a>

```
POST /delete-app-version-resource HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
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
   "resourceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteAppVersionResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAppVersionResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [awsAccountId](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-awsAccountId"></a>
 AWS account that owns the physical resource.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [awsRegion](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-awsRegion"></a>
 AWS region that owns the physical resource.
Type: String
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** [clientToken](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [logicalResourceId](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-logicalResourceId"></a>
Logical identifier of the resource.
Type: [LogicalResourceId](API_LogicalResourceId.md) object
Required: No

 ** [physicalResourceId](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-physicalResourceId"></a>
Physical identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [resourceName](#API_DeleteAppVersionResource_RequestSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-request-resourceName"></a>
Name of the resource.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

## Response Syntax
<a name="API_DeleteAppVersionResource_ResponseSyntax"></a>

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
<a name="API_DeleteAppVersionResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_DeleteAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_DeleteAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-response-appVersion"></a>
 AWS Resilience Hub application version.
Type: String
Pattern: `\S{1,50}`

 ** [physicalResource](#API_DeleteAppVersionResource_ResponseSyntax) **   <a name="resiliencehub-DeleteAppVersionResource-response-physicalResource"></a>
Defines a physical resource. A physical resource is a resource that exists in your account. It can be identified using an Amazon Resource Name (ARN) or a Resilience Hub-native identifier.
Type: [PhysicalResource](API_PhysicalResource.md) object

## Errors
<a name="API_DeleteAppVersionResource_Errors"></a>

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

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAppVersionResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/DeleteAppVersionResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DeleteAppVersionResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
