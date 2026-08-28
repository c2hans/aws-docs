---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageDescriptor.html
---

# GetSolNetworkPackageDescriptor
<a name="API_GetSolNetworkPackageDescriptor"></a>

Gets the content of the network service descriptor.

A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the AWS infrastructure you want to deploy the network functions on.

## Request Syntax
<a name="API_GetSolNetworkPackageDescriptor_RequestSyntax"></a>

```
GET /sol/nsd/v1/ns_descriptors/{{nsdInfoId}}/nsd HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolNetworkPackageDescriptor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsdInfoId](#API_GetSolNetworkPackageDescriptor_RequestSyntax) **   <a name="TNB-GetSolNetworkPackageDescriptor-request-uri-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolNetworkPackageDescriptor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolNetworkPackageDescriptor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}

{{nsd}}
```

## Response Elements
<a name="API_GetSolNetworkPackageDescriptor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_GetSolNetworkPackageDescriptor_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackageDescriptor-response-contentType"></a>
Indicates the media type of the resource.
Valid Values: `text/plain`

The response returns the following as the HTTP body.

 ** [nsd](#API_GetSolNetworkPackageDescriptor_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackageDescriptor-response-nsd"></a>
Contents of the network service descriptor in the network package.

## Errors
<a name="API_GetSolNetworkPackageDescriptor_Errors"></a>

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
<a name="API_GetSolNetworkPackageDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolNetworkPackageDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkPackageDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
