---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeleteDomain.html
---

# DeleteDomain
<a name="API_DeleteDomain"></a>

Deletes a Domain and all associated resources.

## Request Syntax
<a name="API_DeleteDomain_RequestSyntax"></a>

```
DELETE /domain/{{domainId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_DeleteDomain_RequestSyntax) **   <a name="connecthealth-DeleteDomain-request-uri-domainId"></a>
The id of the Domain to delete
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "domainId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteDomain_ResponseSyntax) **   <a name="connecthealth-DeleteDomain-response-arn"></a>
The ARN of the Domain that was requested for deletion
Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+`

 ** [domainId](#API_DeleteDomain_ResponseSyntax) **   <a name="connecthealth-DeleteDomain-response-domainId"></a>
The id of the Domain requested for deletion
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`

 ** [status](#API_DeleteDomain_ResponseSyntax) **   <a name="connecthealth-DeleteDomain-response-status"></a>
Current status of Domain
Type: String
Valid Values: `ACTIVE | DELETING | DELETED`

## Errors
<a name="API_DeleteDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

## See Also
<a name="API_DeleteDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/DeleteDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/DeleteDomain)
