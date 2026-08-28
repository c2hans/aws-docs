---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribeWebApp.html
---

# DescribeWebApp
<a name="API_DescribeWebApp"></a>

Describes the web app that's identified by `WebAppId`. The response includes endpoint configuration details such as whether the web app is publicly accessible or VPC hosted.

For more information about using VPC endpoints with AWS Transfer Family, see [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html).

## Request Syntax
<a name="API_DescribeWebApp_RequestSyntax"></a>

```
{
   "WebAppId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWebApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WebAppId](#API_DescribeWebApp_RequestSyntax) **   <a name="TransferFamily-DescribeWebApp-request-WebAppId"></a>
Provide the unique identifier for the web app.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

## Response Syntax
<a name="API_DescribeWebApp_ResponseSyntax"></a>

```
{
   "WebApp": {
      "AccessEndpoint": "string",
      "Arn": "string",
      "DescribedEndpointDetails": { ... },
      "DescribedIdentityProviderDetails": { ... },
      "EndpointType": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "WebAppEndpoint": "string",
      "WebAppEndpointPolicy": "string",
      "WebAppId": "string",
      "WebAppUnits": { ... }
   }
}
```

## Response Elements
<a name="API_DescribeWebApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WebApp](#API_DescribeWebApp_ResponseSyntax) **   <a name="TransferFamily-DescribeWebApp-response-WebApp"></a>
Returns a structure that contains the details of the web app.
Type: [DescribedWebApp](API_DescribedWebApp.md) object

## Errors
<a name="API_DescribeWebApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/DescribeWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribeWebApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
