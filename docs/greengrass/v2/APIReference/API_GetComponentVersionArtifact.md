---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponentVersionArtifact.html
---

# GetComponentVersionArtifact
<a name="API_GetComponentVersionArtifact"></a>

Gets the pre-signed URL to download a public or a Lambda component artifact. Core devices call this operation to identify the URL that they can use to download an artifact to install.

## Request Syntax
<a name="API_GetComponentVersionArtifact_RequestSyntax"></a>

```
GET /greengrass/v2/components/{{arn}}/artifacts/{{artifactName+}}?s3EndpointType={{s3EndpointType}} HTTP/1.1
x-amz-iot-endpoint-type: {{iotEndpointType}}
```

## URI Request Parameters
<a name="API_GetComponentVersionArtifact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetComponentVersionArtifact_RequestSyntax) **   <a name="greengrassv2-GetComponentVersionArtifact-request-uri-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version. Specify the ARN of a public or a Lambda component version.
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`
Required: Yes

 ** [artifactName](#API_GetComponentVersionArtifact_RequestSyntax) **   <a name="greengrassv2-GetComponentVersionArtifact-request-uri-artifactName"></a>
The name of the artifact.
You can use the [GetComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html) operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI `greengrass:SomeArtifact.zip`, the artifact name is `SomeArtifact.zip`.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [iotEndpointType](#API_GetComponentVersionArtifact_RequestSyntax) **   <a name="greengrassv2-GetComponentVersionArtifact-request-iotEndpointType"></a>
Determines if the Amazon S3 URL returned is a FIPS pre-signed URL endpoint. Specify `fips` if you want the returned Amazon S3 pre-signed URL to point to an Amazon S3 FIPS endpoint. If you don't specify a value, the default is `standard`.
Valid Values: `fips | standard`

 ** [s3EndpointType](#API_GetComponentVersionArtifact_RequestSyntax) **   <a name="greengrassv2-GetComponentVersionArtifact-request-uri-s3EndpointType"></a>
Specifies the endpoint to use when getting Amazon S3 pre-signed URLs.
All AWS Regions except US East (N. Virginia) use `REGIONAL` in all cases. In the US East (N. Virginia) Region the default is `GLOBAL`, but you can change it to `REGIONAL` with this parameter.
Valid Values: `REGIONAL | GLOBAL`

## Request Body
<a name="API_GetComponentVersionArtifact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetComponentVersionArtifact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "preSignedUrl": "string"
}
```

## Response Elements
<a name="API_GetComponentVersionArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [preSignedUrl](#API_GetComponentVersionArtifact_ResponseSyntax) **   <a name="greengrassv2-GetComponentVersionArtifact-response-preSignedUrl"></a>
The URL of the artifact.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetComponentVersionArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** resourceId **
The ID of the resource that isn't found.
 ** resourceType **
The type of the resource that isn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetComponentVersionArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetComponentVersionArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/GetComponentVersionArtifact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
