---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html
---

# UpdateSolFunctionPackage
<a name="API_UpdateSolFunctionPackage"></a>

Updates the operational state of function package.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Request Syntax
<a name="API_UpdateSolFunctionPackage_RequestSyntax"></a>

```
PATCH /sol/vnfpkgm/v1/vnf_packages/{{vnfPkgId}} HTTP/1.1
Content-type: application/json

{
   "operationalState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSolFunctionPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [vnfPkgId](#API_UpdateSolFunctionPackage_RequestSyntax) **   <a name="TNB-UpdateSolFunctionPackage-request-uri-vnfPkgId"></a>
ID of the function package.
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_UpdateSolFunctionPackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [operationalState](#API_UpdateSolFunctionPackage_RequestSyntax) **   <a name="TNB-UpdateSolFunctionPackage-request-operationalState"></a>
Operational state of the function package.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Syntax
<a name="API_UpdateSolFunctionPackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationalState": "string"
}
```

## Response Elements
<a name="API_UpdateSolFunctionPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationalState](#API_UpdateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-UpdateSolFunctionPackage-response-operationalState"></a>
Operational state of the function package.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateSolFunctionPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSolFunctionPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/UpdateSolFunctionPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/UpdateSolFunctionPackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
