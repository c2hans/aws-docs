---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListServiceVersions.html
---

# ListServiceVersions
<a name="API_ListServiceVersions"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Lists all supported versions for Snow on-device services. Returns an array of `ServiceVersion` object containing the supported versions for a particular service.

## Request Syntax
<a name="API_ListServiceVersions_RequestSyntax"></a>

```
{
   "DependentServices": [
      {
         "ServiceName": "{{string}}",
         "ServiceVersion": {
            "Version": "{{string}}"
         }
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServiceVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DependentServices](#API_ListServiceVersions_RequestSyntax) **   <a name="Snowball-ListServiceVersions-request-DependentServices"></a>
A list of names and versions of dependant services of the requested service.
Type: Array of [DependentService](API_DependentService.md) objects
Required: No

 ** [MaxResults](#API_ListServiceVersions_RequestSyntax) **   <a name="Snowball-ListServiceVersions-request-MaxResults"></a>
The maximum number of `ListServiceVersions` objects to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListServiceVersions_RequestSyntax) **   <a name="Snowball-ListServiceVersions-request-NextToken"></a>
Because HTTP requests are stateless, this is the starting point for the next list of returned `ListServiceVersionsRequest` versions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [ServiceName](#API_ListServiceVersions_RequestSyntax) **   <a name="Snowball-ListServiceVersions-request-ServiceName"></a>
The name of the service for which you're requesting supported versions.
Type: String
Valid Values: `KUBERNETES | EKS_ANYWHERE`
Required: Yes

## Response Syntax
<a name="API_ListServiceVersions_ResponseSyntax"></a>

```
{
   "DependentServices": [
      {
         "ServiceName": "string",
         "ServiceVersion": {
            "Version": "string"
         }
      }
   ],
   "NextToken": "string",
   "ServiceName": "string",
   "ServiceVersions": [
      {
         "Version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DependentServices](#API_ListServiceVersions_ResponseSyntax) **   <a name="Snowball-ListServiceVersions-response-DependentServices"></a>
A list of names and versions of dependant services of the service for which the system provided supported versions.
Type: Array of [DependentService](API_DependentService.md) objects

 ** [NextToken](#API_ListServiceVersions_ResponseSyntax) **   <a name="Snowball-ListServiceVersions-response-NextToken"></a>
Because HTTP requests are stateless, this is the starting point of the next list of returned `ListServiceVersionsResult` results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

 ** [ServiceName](#API_ListServiceVersions_ResponseSyntax) **   <a name="Snowball-ListServiceVersions-response-ServiceName"></a>
The name of the service for which the system provided supported versions.
Type: String
Valid Values: `KUBERNETES | EKS_ANYWHERE`

 ** [ServiceVersions](#API_ListServiceVersions_ResponseSyntax) **   <a name="Snowball-ListServiceVersions-response-ServiceVersions"></a>
A list of supported versions.
Type: Array of [ServiceVersion](API_ServiceVersion.md) objects

## Errors
<a name="API_ListServiceVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListServiceVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListServiceVersions)
