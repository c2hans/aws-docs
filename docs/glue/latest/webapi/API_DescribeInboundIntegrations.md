---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DescribeInboundIntegrations.html
---

# DescribeInboundIntegrations
<a name="API_DescribeInboundIntegrations"></a>

Returns a list of inbound integrations for the specified integration.

## Request Syntax
<a name="API_DescribeInboundIntegrations_RequestSyntax"></a>

```
{
   "IntegrationArn": "{{string}}",
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "TargetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInboundIntegrations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IntegrationArn](#API_DescribeInboundIntegrations_RequestSyntax) **   <a name="Glue-DescribeInboundIntegrations-request-IntegrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Marker](#API_DescribeInboundIntegrations_RequestSyntax) **   <a name="Glue-DescribeInboundIntegrations-request-Marker"></a>
A token to specify where to start paginating. This is the marker from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [MaxRecords](#API_DescribeInboundIntegrations_RequestSyntax) **   <a name="Glue-DescribeInboundIntegrations-request-MaxRecords"></a>
The total number of items to return in the output.
Type: Integer
Required: No

 ** [TargetArn](#API_DescribeInboundIntegrations_RequestSyntax) **   <a name="Glue-DescribeInboundIntegrations-request-TargetArn"></a>
The Amazon Resource Name (ARN) of the target resource in the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_DescribeInboundIntegrations_ResponseSyntax"></a>

```
{
   "InboundIntegrations": [
      {
         "CreateTime": number,
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
         "SourceArn": "string",
         "Status": "string",
         "TargetArn": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeInboundIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InboundIntegrations](#API_DescribeInboundIntegrations_ResponseSyntax) **   <a name="Glue-DescribeInboundIntegrations-response-InboundIntegrations"></a>
A list of inbound integrations.
Type: Array of [InboundIntegration](API_InboundIntegration.md) objects

 ** [Marker](#API_DescribeInboundIntegrations_ResponseSyntax) **   <a name="Glue-DescribeInboundIntegrations-response-Marker"></a>
A value that indicates the starting point for the next set of response records in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_DescribeInboundIntegrations_Errors"></a>

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

 ** OperationNotSupportedException **
The operation is not available in the region.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** TargetResourceNotFound **
The target resource could not be found.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInboundIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DescribeInboundIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DescribeInboundIntegrations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
