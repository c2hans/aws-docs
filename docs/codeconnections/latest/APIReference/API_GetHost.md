---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetHost.html
---

# GetHost
<a name="API_GetHost"></a>

Returns the host ARN and details such as status, provider type, endpoint, and, if applicable, the VPC configuration.

## Request Syntax
<a name="API_GetHost_RequestSyntax"></a>

```
{
   "HostArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HostArn](#API_GetHost_RequestSyntax) **   <a name="codeconnections-GetHost-request-HostArn"></a>
The Amazon Resource Name (ARN) of the requested host.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: Yes

## Response Syntax
<a name="API_GetHost_ResponseSyntax"></a>

```
{
   "Name": "string",
   "ProviderEndpoint": "string",
   "ProviderType": "string",
   "Status": "string",
   "VpcConfiguration": {
      "SecurityGroupIds": [ "string" ],
      "SubnetIds": [ "string" ],
      "TlsCertificate": "string",
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_GetHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_GetHost_ResponseSyntax) **   <a name="codeconnections-GetHost-response-Name"></a>
The name of the requested host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`

 ** [ProviderEndpoint](#API_GetHost_ResponseSyntax) **   <a name="codeconnections-GetHost-response-ProviderEndpoint"></a>
The endpoint of the infrastructure represented by the requested host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`

 ** [ProviderType](#API_GetHost_ResponseSyntax) **   <a name="codeconnections-GetHost-response-ProviderType"></a>
The provider type of the requested host, such as GitHub Enterprise Server.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`

 ** [Status](#API_GetHost_ResponseSyntax) **   <a name="codeconnections-GetHost-response-Status"></a>
The status of the requested host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`

 ** [VpcConfiguration](#API_GetHost_ResponseSyntax) **   <a name="codeconnections-GetHost-response-VpcConfiguration"></a>
The VPC configuration of the requested host.
Type: [VpcConfiguration](API_VpcConfiguration.md) object

## Errors
<a name="API_GetHost_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ResourceUnavailableException **
Resource not found. Verify the ARN for the host resource and try again.
HTTP Status Code: 400

## See Also
<a name="API_GetHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetHost)
