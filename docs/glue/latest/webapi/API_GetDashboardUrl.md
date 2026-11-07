---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDashboardUrl.html
---

# GetDashboardUrl
<a name="API_GetDashboardUrl"></a>

Retrieves the URL for the Spark monitoring dashboard for a Glue resource.

## Request Syntax
<a name="API_GetDashboardUrl_RequestSyntax"></a>

```
{
   "RequestOrigin": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDashboardUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RequestOrigin](#API_GetDashboardUrl_RequestSyntax) **   <a name="Glue-GetDashboardUrl-request-RequestOrigin"></a>
The origin of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [ResourceId](#API_GetDashboardUrl_RequestSyntax) **   <a name="Glue-GetDashboardUrl-request-ResourceId"></a>
The unique identifier of the resource for which to retrieve the dashboard URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [ResourceType](#API_GetDashboardUrl_RequestSyntax) **   <a name="Glue-GetDashboardUrl-request-ResourceType"></a>
The type of the resource. Valid values are `SESSION` and `JOB`.
Type: String
Valid Values: `JOB | SESSION`
Required: Yes

## Response Syntax
<a name="API_GetDashboardUrl_ResponseSyntax"></a>

```
{
   "Url": "string"
}
```

## Response Elements
<a name="API_GetDashboardUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Url](#API_GetDashboardUrl_ResponseSyntax) **   <a name="Glue-GetDashboardUrl-response-Url"></a>
The URL for the Spark monitoring dashboard.
Type: String
Length Constraints: Maximum length of 40000.

## Errors
<a name="API_GetDashboardUrl_Errors"></a>

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

## Examples
<a name="API_GetDashboardUrl_Examples"></a>

### Get Spark UI dashboard URL for a session
<a name="API_GetDashboardUrl_Example_1"></a>

This example illustrates one usage of GetDashboardUrl.

```
aws glue get-dashboard-url --resource-id ses-1234567890abcdef0 --resource-type SESSION
```

## See Also
<a name="API_GetDashboardUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDashboardUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDashboardUrl)
