---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetIntegrationResourceProperty.html
---

# GetIntegrationResourceProperty
<a name="API_GetIntegrationResourceProperty"></a>

This API is used for fetching the `ResourceProperty` of the AWS Glue connection (for the source) or AWS Glue database ARN (for the target)

## Request Syntax
<a name="API_GetIntegrationResourceProperty_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIntegrationResourceProperty_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_GetIntegrationResourceProperty_RequestSyntax) **   <a name="Glue-GetIntegrationResourceProperty-request-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## Response Syntax
<a name="API_GetIntegrationResourceProperty_ResponseSyntax"></a>

```
{
   "ResourceArn": "string",
   "ResourcePropertyArn": "string",
   "SourceProcessingProperties": {
      "RoleArn": "string"
   },
   "TargetProcessingProperties": {
      "ConnectionName": "string",
      "EventBusArn": "string",
      "KmsArn": "string",
      "RoleArn": "string"
   }
}
```

## Response Elements
<a name="API_GetIntegrationResourceProperty_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceArn](#API_GetIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-GetIntegrationResourceProperty-response-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [ResourcePropertyArn](#API_GetIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-GetIntegrationResourceProperty-response-ResourcePropertyArn"></a>
The resource ARN created through this create API. The format is something like arn:aws:glue:<region>:<account\_id>:integrationresourceproperty/\*
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SourceProcessingProperties](#API_GetIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-GetIntegrationResourceProperty-response-SourceProcessingProperties"></a>
The resource properties associated with the integration source.
Type: [SourceProcessingProperties](API_SourceProcessingProperties.md) object

 ** [TargetProcessingProperties](#API_GetIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-GetIntegrationResourceProperty-response-TargetProcessingProperties"></a>
The resource properties associated with the integration target.
Type: [TargetProcessingProperties](API_TargetProcessingProperties.md) object

## Errors
<a name="API_GetIntegrationResourceProperty_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetIntegrationResourceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetIntegrationResourceProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetIntegrationResourceProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
