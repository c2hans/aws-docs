---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_ListHypervisors.html
---

# ListHypervisors
<a name="API_BGW_ListHypervisors"></a>

Lists your hypervisors.

## Request Syntax
<a name="API_BGW_ListHypervisors_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_BGW_ListHypervisors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_BGW_ListHypervisors_RequestSyntax) **   <a name="Backup-BGW_ListHypervisors-request-MaxResults"></a>
The maximum number of hypervisors to list.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_BGW_ListHypervisors_RequestSyntax) **   <a name="Backup-BGW_ListHypervisors-request-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `maxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_BGW_ListHypervisors_ResponseSyntax"></a>

```
{
   "Hypervisors": [
      {
         "Host": "string",
         "HypervisorArn": "string",
         "KmsKeyArn": "string",
         "Name": "string",
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_BGW_ListHypervisors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Hypervisors](#API_BGW_ListHypervisors_ResponseSyntax) **   <a name="Backup-BGW_ListHypervisors-response-Hypervisors"></a>
A list of your `Hypervisor` objects, ordered by their Amazon Resource Names (ARNs).
Type: Array of [Hypervisor](API_BGW_Hypervisor.md) objects

 ** [NextToken](#API_BGW_ListHypervisors_ResponseSyntax) **   <a name="Backup-BGW_ListHypervisors-response-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `maxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.+`

## Errors
<a name="API_BGW_ListHypervisors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The operation did not succeed because an internal error occurred. Try again later.
 ** ErrorCode **
A description of which internal error occured.
HTTP Status Code: 500

 ** ThrottlingException **
TPS has been limited to protect against intentional or unintentional high request volumes.
 ** ErrorCode **
Error: TPS has been limited to protect against intentional or unintentional high request volumes.
HTTP Status Code: 400

 ** ValidationException **
The operation did not succeed because a validation error occurred.
 ** ErrorCode **
A description of what caused the validation error.
HTTP Status Code: 400

## See Also
<a name="API_BGW_ListHypervisors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/ListHypervisors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/ListHypervisors)
