---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Creates a connection that can then be given to other AWS services like CodePipeline so that it can access third-party code repositories. The connection is in pending status until the third-party connection handshake is completed from the console.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
{
   "ConnectionName": "{{string}}",
   "HostArn": "{{string}}",
   "ProviderType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionName](#API_CreateConnection_RequestSyntax) **   <a name="codeconnections-CreateConnection-request-ConnectionName"></a>
The name of the connection to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\s\S]*`
Required: Yes

 ** [HostArn](#API_CreateConnection_RequestSyntax) **   <a name="codeconnections-CreateConnection-request-HostArn"></a>
The Amazon Resource Name (ARN) of the host associated with the connection to be created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: No

 ** [ProviderType](#API_CreateConnection_RequestSyntax) **   <a name="codeconnections-CreateConnection-request-ProviderType"></a>
The name of the external provider where your third-party code repository is configured.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: No

 ** [Tags](#API_CreateConnection_RequestSyntax) **   <a name="codeconnections-CreateConnection-request-Tags"></a>
The key-value pair to use when tagging the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
{
   "ConnectionArn": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionArn](#API_CreateConnection_ResponseSyntax) **   <a name="codeconnections-CreateConnection-response-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection to be created. The ARN is used as the connection reference when the connection is shared between AWS services.
The ARN is never reused if the connection is deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`

 ** [Tags](#API_CreateConnection_ResponseSyntax) **   <a name="codeconnections-CreateConnection-response-Tags"></a>
Specifies the tags applied to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
Exceeded the maximum limit for connections.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ResourceUnavailableException **
Resource not found. Verify the ARN for the host resource and try again.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/CreateConnection)
