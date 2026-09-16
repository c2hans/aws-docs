---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListConnections.html
---

# ListConnections
<a name="API_ListConnections"></a>

Lists the connections associated with your account.

## Request Syntax
<a name="API_ListConnections_RequestSyntax"></a>

```
{
   "HostArnFilter": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProviderTypeFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HostArnFilter](#API_ListConnections_RequestSyntax) **   <a name="codeconnections-ListConnections-request-HostArnFilter"></a>
Filters the list of connections to those associated with a specified host.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: No

 ** [MaxResults](#API_ListConnections_RequestSyntax) **   <a name="codeconnections-ListConnections-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListConnections_RequestSyntax) **   <a name="codeconnections-ListConnections-request-NextToken"></a>
The token that was returned from the previous `ListConnections` call, which can be used to return the next set of connections in the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

 ** [ProviderTypeFilter](#API_ListConnections_RequestSyntax) **   <a name="codeconnections-ListConnections-request-ProviderTypeFilter"></a>
Filters the list of connections to those associated with a specified provider, such as Bitbucket.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: No

## Response Syntax
<a name="API_ListConnections_ResponseSyntax"></a>

```
{
   "Connections": [
      {
         "ConnectionArn": "string",
         "ConnectionName": "string",
         "ConnectionStatus": "string",
         "HostArn": "string",
         "OwnerAccountId": "string",
         "ProviderType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connections](#API_ListConnections_ResponseSyntax) **   <a name="codeconnections-ListConnections-response-Connections"></a>
A list of connections and the details for each connection, such as status, owner, and provider type.
Type: Array of [Connection](API_Connection.md) objects

 ** [NextToken](#API_ListConnections_ResponseSyntax) **   <a name="codeconnections-ListConnections-response-NextToken"></a>
A token that can be used in the next `ListConnections` call. To view all items in the list, continue to call this operation with each subsequent token until no more `nextToken` values are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`

## Errors
<a name="API_ListConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/ListConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ListConnections)
