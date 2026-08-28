---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateAppVersionAppComponent.html
---

# UpdateAppVersionAppComponent
<a name="API_UpdateAppVersionAppComponent"></a>

Updates an existing AppComponent in the AWS Resilience Hub application.

**Note**
This API updates the AWS Resilience Hub application draft version. To use this AppComponent for running assessments, you must publish the AWS Resilience Hub application using the `PublishAppVersion` API.

## Request Syntax
<a name="API_UpdateAppVersionAppComponent_RequestSyntax"></a>

```
POST /update-app-version-app-component HTTP/1.1
Content-type: application/json

{
   "additionalInfo": {
      "{{string}}" : [ "{{string}}" ]
   },
   "appArn": "{{string}}",
   "id": "{{string}}",
   "name": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAppVersionAppComponent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAppVersionAppComponent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalInfo](#API_UpdateAppVersionAppComponent_RequestSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-request-additionalInfo"></a>
Currently, there is no supported additional information for AppComponents.
Type: String to array of strings map
Key Pattern: `\S{1,128}`
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [appArn](#API_UpdateAppVersionAppComponent_RequestSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [id](#API_UpdateAppVersionAppComponent_RequestSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-request-id"></a>
Identifier of the AppComponent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [name](#API_UpdateAppVersionAppComponent_RequestSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-request-name"></a>
Name of the AppComponent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [type](#API_UpdateAppVersionAppComponent_RequestSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-request-type"></a>
Type of AppComponent. For more information about the types of AppComponent, see [Grouping resources in an AppComponent](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateAppVersionAppComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appComponent": {
      "additionalInfo": {
         "string" : [ "string" ]
      },
      "id": "string",
      "name": "string",
      "type": "string"
   },
   "appVersion": "string"
}
```

## Response Elements
<a name="API_UpdateAppVersionAppComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_UpdateAppVersionAppComponent_ResponseSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appComponent](#API_UpdateAppVersionAppComponent_ResponseSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-response-appComponent"></a>
List of AppComponents that belong to this resource.
Type: [AppComponent](API_AppComponent.md) object

 ** [appVersion](#API_UpdateAppVersionAppComponent_ResponseSyntax) **   <a name="resiliencehub-UpdateAppVersionAppComponent-response-appVersion"></a>
 AWS Resilience Hub application version.
Type: String
Pattern: `\S{1,50}`

## Errors
<a name="API_UpdateAppVersionAppComponent_Errors"></a>

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
<a name="API_UpdateAppVersionAppComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/UpdateAppVersionAppComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
