---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetProviderService.html
---

# GetProviderService
<a name="API_GetProviderService"></a>

Returns the `ProviderService` of a given name.

## Request Syntax
<a name="API_GetProviderService_RequestSyntax"></a>

```
GET /providerservices/{{providerName}}/{{providerServiceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProviderService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [providerName](#API_GetProviderService_RequestSyntax) **   <a name="API-GetProviderService-request-uri-providerName"></a>
The name of the provider. This name is typically the company name.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** [providerServiceName](#API_GetProviderService_RequestSyntax) **   <a name="API-GetProviderService-request-uri-providerServiceName"></a>
The ARN (Amazon Resource Name) of the product that the provider service provides.
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})`
Required: Yes

## Request Body
<a name="API_GetProviderService_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProviderService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "anonymizedOutput": boolean,
   "providerComponentSchema": {
      "providerSchemaAttributes": [
         {
            "fieldName": "string",
            "hashing": boolean,
            "subType": "string",
            "type": "string"
         }
      ],
      "schemas": [
         [ "string" ]
      ]
   },
   "providerConfigurationDefinition": JSON value,
   "providerEndpointConfiguration": { ... },
   "providerEntityOutputDefinition": JSON value,
   "providerIdNameSpaceConfiguration": {
      "description": "string",
      "providerSourceConfigurationDefinition": JSON value,
      "providerTargetConfigurationDefinition": JSON value
   },
   "providerIntermediateDataAccessConfiguration": {
      "awsAccountIds": [ "string" ],
      "requiredBucketActions": [ "string" ]
   },
   "providerJobConfiguration": JSON value,
   "providerName": "string",
   "providerServiceArn": "string",
   "providerServiceDisplayName": "string",
   "providerServiceName": "string",
   "providerServiceType": "string"
}
```

## Response Elements
<a name="API_GetProviderService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anonymizedOutput](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-anonymizedOutput"></a>
Specifies whether output data from the provider is anonymized. A value of `TRUE` means the output will be anonymized and you can't relate the data that comes back from the provider to the identifying input. A value of `FALSE` means the output won't be anonymized and you can relate the data that comes back from the provider to your source data.
Type: Boolean

 ** [providerComponentSchema](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerComponentSchema"></a>
Input schema for the provider service.
Type: [ProviderComponentSchema](API_ProviderComponentSchema.md) object

 ** [providerConfigurationDefinition](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerConfigurationDefinition"></a>
The definition of the provider configuration.
Type: JSON value

 ** [providerEndpointConfiguration](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerEndpointConfiguration"></a>
The required configuration fields to use with the provider service.
Type: [ProviderEndpointConfiguration](API_ProviderEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [providerEntityOutputDefinition](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerEntityOutputDefinition"></a>
The definition of the provider entity output.
Type: JSON value

 ** [providerIdNameSpaceConfiguration](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerIdNameSpaceConfiguration"></a>
The provider configuration required for different ID namespace types.
Type: [ProviderIdNameSpaceConfiguration](API_ProviderIdNameSpaceConfiguration.md) object

 ** [providerIntermediateDataAccessConfiguration](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerIntermediateDataAccessConfiguration"></a>
The AWS accounts and the S3 permissions that are required by some providers to create an S3 bucket for intermediate data storage.
Type: [ProviderIntermediateDataAccessConfiguration](API_ProviderIntermediateDataAccessConfiguration.md) object

 ** [providerJobConfiguration](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerJobConfiguration"></a>
Provider service job configurations.
Type: JSON value

 ** [providerName](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerName"></a>
The name of the provider. This name is typically the company name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

 ** [providerServiceArn](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerServiceArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the provider service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})`

 ** [providerServiceDisplayName](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerServiceDisplayName"></a>
The display name of the provider service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [providerServiceName](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerServiceName"></a>
The name of the product that the provider service provides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

 ** [providerServiceType](#API_GetProviderService_ResponseSyntax) **   <a name="API-GetProviderService-response-providerServiceType"></a>
The type of provider service.
Type: String
Valid Values: `ASSIGNMENT | ID_MAPPING`

## Errors
<a name="API_GetProviderService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_GetProviderService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetProviderService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetProviderService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
