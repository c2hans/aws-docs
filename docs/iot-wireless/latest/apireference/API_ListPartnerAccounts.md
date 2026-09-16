---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListPartnerAccounts.html
---

# ListPartnerAccounts
<a name="API_ListPartnerAccounts"></a>

Lists the partner accounts associated with your AWS account.

## Request Syntax
<a name="API_ListPartnerAccounts_RequestSyntax"></a>

```
GET /partner-accounts?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPartnerAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListPartnerAccounts_RequestSyntax) **   <a name="iotwireless-ListPartnerAccounts-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListPartnerAccounts_RequestSyntax) **   <a name="iotwireless-ListPartnerAccounts-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

## Request Body
<a name="API_ListPartnerAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPartnerAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Sidewalk": [
      {
         "AmazonId": "string",
         "Arn": "string",
         "Fingerprint": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPartnerAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPartnerAccounts_ResponseSyntax) **   <a name="iotwireless-ListPartnerAccounts-response-NextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Sidewalk](#API_ListPartnerAccounts_ResponseSyntax) **   <a name="iotwireless-ListPartnerAccounts-response-Sidewalk"></a>
The Sidewalk account credentials.
Type: Array of [SidewalkAccountInfoWithFingerprint](API_SidewalkAccountInfoWithFingerprint.md) objects

## Errors
<a name="API_ListPartnerAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListPartnerAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListPartnerAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListPartnerAccounts)
