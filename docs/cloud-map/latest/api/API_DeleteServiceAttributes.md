---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteServiceAttributes.html
---

# DeleteServiceAttributes
<a name="API_DeleteServiceAttributes"></a>

Deletes specific attributes associated with a service.

## Request Syntax
<a name="API_DeleteServiceAttributes_RequestSyntax"></a>

```
{
   "Attributes": [ "{{string}}" ],
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteServiceAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_DeleteServiceAttributes_RequestSyntax) **   <a name="cloudmap-DeleteServiceAttributes-request-Attributes"></a>
A list of keys corresponding to each attribute that you want to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Maximum length of 255.
Required: Yes

 ** [ServiceId](#API_DeleteServiceAttributes_RequestSyntax) **   <a name="cloudmap-DeleteServiceAttributes-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service from which the attributes will be deleted. For services created in a namespace shared with your AWS account, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_DeleteServiceAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteServiceAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_DeleteServiceAttributes_Examples"></a>

### DeleteServiceAttributes Example
<a name="API_DeleteServiceAttributes_Example_1"></a>

This example API request deletes the attribute `Port` associated with the service `srv-e4anhexample0004`.

#### Sample Request
<a name="API_DeleteServiceAttributes_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0004",
    "Attributes" : ["Port"]
}
```

#### Sample Response
<a name="API_DeleteServiceAttributes_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

### DeleteServiceAttributes Example using ARN
<a name="API_DeleteServiceAttributes_Example_2"></a>

This example API request deletes the attribute `Port` associated with a service in a shared namespace using its ARN.

#### Sample Request
<a name="API_DeleteServiceAttributes_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
    "Attributes" : ["Port"]
}
```

#### Sample Response
<a name="API_DeleteServiceAttributes_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

## See Also
<a name="API_DeleteServiceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DeleteServiceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DeleteServiceAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
