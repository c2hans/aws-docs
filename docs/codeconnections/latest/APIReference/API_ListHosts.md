---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListHosts.html
---

# ListHosts
<a name="API_ListHosts"></a>

Lists the hosts associated with your account.

## Request Syntax
<a name="API_ListHosts_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListHosts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListHosts_RequestSyntax) **   <a name="codeconnections-ListHosts-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListHosts_RequestSyntax) **   <a name="codeconnections-ListHosts-request-NextToken"></a>
The token that was returned from the previous `ListHosts` call, which can be used to return the next set of hosts in the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

## Response Syntax
<a name="API_ListHosts_ResponseSyntax"></a>

```
{
   "Hosts": [
      {
         "HostArn": "string",
         "Name": "string",
         "ProviderEndpoint": "string",
         "ProviderType": "string",
         "Status": "string",
         "StatusMessage": "string",
         "VpcConfiguration": {
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "TlsCertificate": "string",
            "VpcId": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHosts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Hosts](#API_ListHosts_ResponseSyntax) **   <a name="codeconnections-ListHosts-response-Hosts"></a>
A list of hosts and the details for each host, such as status, endpoint, and provider type.
Type: Array of [Host](API_Host.md) objects

 ** [NextToken](#API_ListHosts_ResponseSyntax) **   <a name="codeconnections-ListHosts-response-NextToken"></a>
A token that can be used in the next `ListHosts` call. To view all items in the list, continue to call this operation with each subsequent token until no more `nextToken` values are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`

## Errors
<a name="API_ListHosts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/ListHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ListHosts)
