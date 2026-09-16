---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DescribeIntegrations.html
---

# DescribeIntegrations
<a name="API_DescribeIntegrations"></a>

The API is used to retrieve a list of integrations.

## Request Syntax
<a name="API_DescribeIntegrations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "IntegrationIdentifier": "{{string}}",
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeIntegrations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeIntegrations_RequestSyntax) **   <a name="Glue-DescribeIntegrations-request-Filters"></a>
A list of key and values, to filter down the results. Supported keys are "Status", "IntegrationName", and "SourceArn". IntegrationName is limited to only one value.
Type: Array of [IntegrationFilter](API_IntegrationFilter.md) objects
Required: No

 ** [IntegrationIdentifier](#API_DescribeIntegrations_RequestSyntax) **   <a name="Glue-DescribeIntegrations-request-IntegrationIdentifier"></a>
The Amazon Resource Name (ARN) for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Marker](#API_DescribeIntegrations_RequestSyntax) **   <a name="Glue-DescribeIntegrations-request-Marker"></a>
A value that indicates the starting point for the next set of response records in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [MaxRecords](#API_DescribeIntegrations_RequestSyntax) **   <a name="Glue-DescribeIntegrations-request-MaxRecords"></a>
The total number of items to return in the output.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeIntegrations_ResponseSyntax"></a>

```
{
   "Integrations": [
      {
         "AdditionalEncryptionContext": {
            "string" : "string"
         },
         "CreateTime": number,
         "DataFilter": "string",
         "Description": "string",
         "Errors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "IntegrationArn": "string",
         "IntegrationConfig": {
            "ContinuousSync": boolean,
            "RefreshInterval": "string",
            "SourceProperties": {
               "string" : "string"
            }
         },
         "IntegrationName": "string",
         "KmsKeyId": "string",
         "SourceArn": "string",
         "Status": "string",
         "Tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "TargetArn": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Integrations](#API_DescribeIntegrations_ResponseSyntax) **   <a name="Glue-DescribeIntegrations-response-Integrations"></a>
A list of zero-ETL integrations.
Type: Array of [Integration](API_Integration.md) objects

 ** [Marker](#API_DescribeIntegrations_ResponseSyntax) **   <a name="Glue-DescribeIntegrations-response-Marker"></a>
A value that indicates the starting point for the next set of response records in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_DescribeIntegrations_Errors"></a>

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

 ** IntegrationNotFoundFault **
The specified integration could not be found.
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

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DescribeIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DescribeIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DescribeIntegrations)
