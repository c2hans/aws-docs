---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateHost.html
---

# CreateHost
<a name="API_CreateHost"></a>

Creates a resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.

**Note**
A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.

## Request Syntax
<a name="API_CreateHost_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "ProviderEndpoint": "{{string}}",
   "ProviderType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcConfiguration": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ],
      "TlsCertificate": "{{string}}",
      "VpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_CreateHost_RequestSyntax) **   <a name="codeconnections-CreateHost-request-Name"></a>
The name of the host to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: Yes

 ** [ProviderEndpoint](#API_CreateHost_RequestSyntax) **   <a name="codeconnections-CreateHost-request-ProviderEndpoint"></a>
The endpoint of the infrastructure to be represented by the host after it is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** [ProviderType](#API_CreateHost_RequestSyntax) **   <a name="codeconnections-CreateHost-request-ProviderType"></a>
The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: Yes

 ** [Tags](#API_CreateHost_RequestSyntax) **   <a name="codeconnections-CreateHost-request-Tags"></a>
Tags for the host to be created.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [VpcConfiguration](#API_CreateHost_RequestSyntax) **   <a name="codeconnections-CreateHost-request-VpcConfiguration"></a>
The VPC configuration to be provisioned for the host. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateHost_ResponseSyntax"></a>

```
{
   "HostArn": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HostArn](#API_CreateHost_ResponseSyntax) **   <a name="codeconnections-CreateHost-response-HostArn"></a>
The Amazon Resource Name (ARN) of the host to be created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`

 ** [Tags](#API_CreateHost_ResponseSyntax) **   <a name="codeconnections-CreateHost-response-Tags"></a>
Tags for the created host.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_CreateHost_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
Exceeded the maximum limit for connections.
HTTP Status Code: 400

## See Also
<a name="API_CreateHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/CreateHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/CreateHost)
