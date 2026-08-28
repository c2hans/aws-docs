---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteService.html
---

# DeleteService
<a name="API_DeleteService"></a>

Deletes a specified service and all associated service attributes. If the service still contains one or more registered instances, the request fails.

## Request Syntax
<a name="API_DeleteService_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_DeleteService_RequestSyntax) **   <a name="cloudmap-DeleteService-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to delete. If the namespace associated with the service is shared with your AWS account, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_DeleteService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ResourceInUse **
The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_DeleteService_Examples"></a>

### DeleteService Example
<a name="API_DeleteService_Example_1"></a>

This example deletes the specified service.

#### Sample Request
<a name="API_DeleteService_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211708Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeleteService_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

### DeleteService Example using ARN
<a name="API_DeleteService_Example_2"></a>

This example deletes a service in a shared namespace using its ARN.

#### Sample Request
<a name="API_DeleteService_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211708Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeleteService_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

## See Also
<a name="API_DeleteService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DeleteService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DeleteService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
