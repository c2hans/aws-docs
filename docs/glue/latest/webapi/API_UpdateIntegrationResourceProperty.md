---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateIntegrationResourceProperty.html
---

# UpdateIntegrationResourceProperty
<a name="API_UpdateIntegrationResourceProperty"></a>

This API can be used for updating the `ResourceProperty` of the AWS Glue connection (for the source) or AWS Glue database ARN (for the target). These properties can include the role to access the connection or database. Since the same resource can be used across multiple integrations, updating resource properties will impact all the integrations using it.

## Request Syntax
<a name="API_UpdateIntegrationResourceProperty_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "SourceProcessingProperties": {
      "RoleArn": "{{string}}"
   },
   "TargetProcessingProperties": {
      "ConnectionName": "{{string}}",
      "EventBusArn": "{{string}}",
      "KmsArn": "{{string}}",
      "RoleArn": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateIntegrationResourceProperty_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UpdateIntegrationResourceProperty_RequestSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-request-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [SourceProcessingProperties](#API_UpdateIntegrationResourceProperty_RequestSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-request-SourceProcessingProperties"></a>
The resource properties associated with the integration source.
Type: [SourceProcessingProperties](API_SourceProcessingProperties.md) object
Required: No

 ** [TargetProcessingProperties](#API_UpdateIntegrationResourceProperty_RequestSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-request-TargetProcessingProperties"></a>
The resource properties associated with the integration target.
Type: [TargetProcessingProperties](API_TargetProcessingProperties.md) object
Required: No

## Response Syntax
<a name="API_UpdateIntegrationResourceProperty_ResponseSyntax"></a>

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
<a name="API_UpdateIntegrationResourceProperty_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceArn](#API_UpdateIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-response-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [ResourcePropertyArn](#API_UpdateIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-response-ResourcePropertyArn"></a>
The resource ARN created through this create API. The format is something like arn:aws:glue:<region>:<account\_id>:integrationresourceproperty/\*
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SourceProcessingProperties](#API_UpdateIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-response-SourceProcessingProperties"></a>
The resource properties associated with the integration source.
Type: [SourceProcessingProperties](API_SourceProcessingProperties.md) object

 ** [TargetProcessingProperties](#API_UpdateIntegrationResourceProperty_ResponseSyntax) **   <a name="Glue-UpdateIntegrationResourceProperty-response-TargetProcessingProperties"></a>
The resource properties associated with the integration target.
Type: [TargetProcessingProperties](API_TargetProcessingProperties.md) object

## Errors
<a name="API_UpdateIntegrationResourceProperty_Errors"></a>

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
<a name="API_UpdateIntegrationResourceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateIntegrationResourceProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateIntegrationResourceProperty)
