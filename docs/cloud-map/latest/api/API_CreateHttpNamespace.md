---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateHttpNamespace.html
---

# CreateHttpNamespace
<a name="API_CreateHttpNamespace"></a>

Creates an HTTP namespace. Service instances registered using an HTTP namespace can be discovered using a `DiscoverInstances` request but can't be discovered using DNS.

For the current quota on the number of namespaces that you can create using the same AWS account, see [AWS Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the * AWS Cloud Map Developer Guide*.

## Request Syntax
<a name="API_CreateHttpNamespace_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateHttpNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_CreateHttpNamespace_RequestSyntax) **   <a name="cloudmap-CreateHttpNamespace-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed `CreateHttpNamespace` requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/time stamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [Description](#API_CreateHttpNamespace_RequestSyntax) **   <a name="cloudmap-CreateHttpNamespace-request-Description"></a>
A description for the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Name](#API_CreateHttpNamespace_RequestSyntax) **   <a name="cloudmap-CreateHttpNamespace-request-Name"></a>
The name that you want to assign to this namespace.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(?!arn:)[!-~]{1,1024}$`
Required: Yes

 ** [Tags](#API_CreateHttpNamespace_RequestSyntax) **   <a name="cloudmap-CreateHttpNamespace-request-Tags"></a>
The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateHttpNamespace_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_CreateHttpNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_CreateHttpNamespace_ResponseSyntax) **   <a name="cloudmap-CreateHttpNamespace-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_CreateHttpNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceAlreadyExists **
The namespace that you're trying to create already exists.
 ** CreatorRequestId **
The `CreatorRequestId` that was used to create the namespace.
 ** NamespaceId **
The ID of the existing namespace.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
The resource can't be created because you've reached the quota on the number of resources.
HTTP Status Code: 400

 ** TooManyTagsException **
The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.
 ** ResourceName **
The name of the resource.
HTTP Status Code: 400

## Examples
<a name="API_CreateHttpNamespace_Examples"></a>

### CreateHttpNamespace Example
<a name="API_CreateHttpNamespace_Example_1"></a>

This example creates an HTTP namespace called `example-http.com`.

#### Sample Request
<a name="API_CreateHttpNamespace_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211703Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.CreateHttpNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0001",
    "Name": "example-http.com",
    "Description": "Example.com AWS Cloud Map HTTP Namespace"
}
```

#### Sample Response
<a name="API_CreateHttpNamespace_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"httpvoqozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_CreateHttpNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/CreateHttpNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/CreateHttpNamespace)
