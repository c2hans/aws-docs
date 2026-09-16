---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ImportResourcesToDraftAppVersion.html
---

# ImportResourcesToDraftAppVersion
<a name="API_ImportResourcesToDraftAppVersion"></a>

Imports resources to AWS Resilience Hub application draft version from different input sources. For more information about the input sources supported by AWS Resilience Hub, see [Discover the structure and describe your Resilience Hub application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html).

## Request Syntax
<a name="API_ImportResourcesToDraftAppVersion_RequestSyntax"></a>

```
POST /import-resources-to-draft-app-version HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "eksSources": [
      {
         "eksClusterArn": "{{string}}",
         "namespaces": [ "{{string}}" ]
      }
   ],
   "importStrategy": "{{string}}",
   "sourceArns": [ "{{string}}" ],
   "terraformSources": [
      {
         "s3StateFileUrl": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_ImportResourcesToDraftAppVersion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportResourcesToDraftAppVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_ImportResourcesToDraftAppVersion_RequestSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [eksSources](#API_ImportResourcesToDraftAppVersion_RequestSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-request-eksSources"></a>
The input sources of the Amazon Elastic Kubernetes Service resources you need to import.
Type: Array of [EksSource](API_EksSource.md) objects
Required: No

 ** [importStrategy](#API_ImportResourcesToDraftAppVersion_RequestSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-request-importStrategy"></a>
The import strategy you would like to set to import resources into AWS Resilience Hub application.
Type: String
Valid Values: `AddOnly | ReplaceAll`
Required: No

 ** [sourceArns](#API_ImportResourcesToDraftAppVersion_RequestSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-request-sourceArns"></a>
The Amazon Resource Names (ARNs) for the resources.
Type: Array of strings
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [terraformSources](#API_ImportResourcesToDraftAppVersion_RequestSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-request-terraformSources"></a>
 A list of terraform file s3 URLs you need to import.
Type: Array of [TerraformSource](API_TerraformSource.md) objects
Required: No

## Response Syntax
<a name="API_ImportResourcesToDraftAppVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appVersion": "string",
   "eksSources": [
      {
         "eksClusterArn": "string",
         "namespaces": [ "string" ]
      }
   ],
   "sourceArns": [ "string" ],
   "status": "string",
   "terraformSources": [
      {
         "s3StateFileUrl": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ImportResourcesToDraftAppVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-appVersion"></a>
The version of the application.
Type: String
Pattern: `\S{1,50}`

 ** [eksSources](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-eksSources"></a>
The input sources of the Amazon Elastic Kubernetes Service resources you have imported.
Type: Array of [EksSource](API_EksSource.md) objects

 ** [sourceArns](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-sourceArns"></a>
The Amazon Resource Names (ARNs) for the resources you have imported.
Type: Array of strings
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [status](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-status"></a>
Status of the action.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`

 ** [terraformSources](#API_ImportResourcesToDraftAppVersion_ResponseSyntax) **   <a name="resiliencehub-ImportResourcesToDraftAppVersion-response-terraformSources"></a>
 A list of terraform file s3 URLs you have imported.
Type: Array of [TerraformSource](API_TerraformSource.md) objects

## Errors
<a name="API_ImportResourcesToDraftAppVersion_Errors"></a>

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
<a name="API_ImportResourcesToDraftAppVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)
