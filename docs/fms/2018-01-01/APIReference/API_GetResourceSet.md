---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetResourceSet.html
---

# GetResourceSet
<a name="API_GetResourceSet"></a>

Gets information about a specific resource set.

## Request Syntax
<a name="API_GetResourceSet_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetResourceSet_RequestSyntax) **   <a name="fms-GetResourceSet-request-Identifier"></a>
A unique identifier for the resource set, used in a request to refer to the resource set.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^[a-z0-9A-Z]{22}$`
Required: Yes

## Response Syntax
<a name="API_GetResourceSet_ResponseSyntax"></a>

```
{
   "ResourceSet": {
      "Description": "string",
      "Id": "string",
      "LastUpdateTime": number,
      "Name": "string",
      "ResourceSetStatus": "string",
      "ResourceTypeList": [ "string" ],
      "UpdateToken": "string"
   },
   "ResourceSetArn": "string"
}
```

## Response Elements
<a name="API_GetResourceSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceSet](#API_GetResourceSet_ResponseSyntax) **   <a name="fms-GetResourceSet-response-ResourceSet"></a>
Information about the specified resource set.
Type: [ResourceSet](API_ResourceSet.md) object

 ** [ResourceSetArn](#API_GetResourceSet_ResponseSyntax) **   <a name="fms-GetResourceSet-response-ResourceSetArn"></a>
The Amazon Resource Name (ARN) of the resource set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_GetResourceSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetResourceSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetResourceSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetResourceSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
