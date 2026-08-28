---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListWebApps.html
---

# ListWebApps
<a name="API_ListWebApps"></a>

Lists all web apps associated with your AWS account for your current region. The response includes the endpoint type for each web app, showing whether it is publicly accessible or VPC hosted.

For more information about using VPC endpoints with AWS Transfer Family, see [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html).

## Request Syntax
<a name="API_ListWebApps_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWebApps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListWebApps_RequestSyntax) **   <a name="TransferFamily-ListWebApps-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListWebApps_RequestSyntax) **   <a name="TransferFamily-ListWebApps-request-NextToken"></a>
Returns the `NextToken` parameter in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional web apps.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

## Response Syntax
<a name="API_ListWebApps_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WebApps": [
      {
         "AccessEndpoint": "string",
         "Arn": "string",
         "EndpointType": "string",
         "WebAppEndpoint": "string",
         "WebAppId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWebApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWebApps_ResponseSyntax) **   <a name="TransferFamily-ListWebApps-response-NextToken"></a>
Provide this value for the `NextToken` parameter in a subsequent command to continue listing additional web apps.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [WebApps](#API_ListWebApps_ResponseSyntax) **   <a name="TransferFamily-ListWebApps-response-WebApps"></a>
Returns, for each listed web app, a structure that contains details for the web app.
Type: Array of [ListedWebApp](API_ListedWebApp.md) objects

## Errors
<a name="API_ListWebApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` parameter that was passed is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_ListWebApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/ListWebApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListWebApps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
