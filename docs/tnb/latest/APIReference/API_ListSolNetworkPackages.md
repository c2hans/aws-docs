---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackages.html
---

# ListSolNetworkPackages
<a name="API_ListSolNetworkPackages"></a>

Lists network packages.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Request Syntax
<a name="API_ListSolNetworkPackages_RequestSyntax"></a>

```
GET /sol/nsd/v1/ns_descriptors?max_results={{maxResults}}&nextpage_opaque_marker={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSolNetworkPackages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSolNetworkPackages_RequestSyntax) **   <a name="TNB-ListSolNetworkPackages-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSolNetworkPackages_RequestSyntax) **   <a name="TNB-ListSolNetworkPackages-request-uri-nextToken"></a>
The token for the next page of results.

## Request Body
<a name="API_ListSolNetworkPackages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSolNetworkPackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "networkPackages": [
      {
         "arn": "string",
         "id": "string",
         "metadata": {
            "createdAt": "string",
            "lastModified": "string"
         },
         "nsdDesigner": "string",
         "nsdId": "string",
         "nsdInvariantId": "string",
         "nsdName": "string",
         "nsdOnboardingState": "string",
         "nsdOperationalState": "string",
         "nsdUsageState": "string",
         "nsdVersion": "string",
         "vnfPkgIds": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSolNetworkPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkPackages](#API_ListSolNetworkPackages_ResponseSyntax) **   <a name="TNB-ListSolNetworkPackages-response-networkPackages"></a>
Network packages. A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.
Type: Array of [ListSolNetworkPackageInfo](API_ListSolNetworkPackageInfo.md) objects

 ** [nextToken](#API_ListSolNetworkPackages_ResponseSyntax) **   <a name="TNB-ListSolNetworkPackages-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListSolNetworkPackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListSolNetworkPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ListSolNetworkPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkPackages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
