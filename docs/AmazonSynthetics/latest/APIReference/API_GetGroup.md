---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetGroup.html
---

# GetGroup
<a name="API_GetGroup"></a>

Returns information about one group. Groups are a global resource, so you can use this operation from any Region.

## Request Syntax
<a name="API_GetGroup_RequestSyntax"></a>

```
GET /group/{{groupIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupIdentifier](#API_GetGroup_RequestSyntax) **   <a name="synthetics-GetGroup-request-uri-GroupIdentifier"></a>
Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the `GroupIdentifier`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_GetGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": {
      "Arn": "string",
      "CreatedTime": number,
      "Id": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_GetGroup_ResponseSyntax) **   <a name="synthetics-GetGroup-response-Group"></a>
A structure that contains information about the group.
Type: [Group](API_Group.md) object

## Errors
<a name="API_GetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_GetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/GetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/GetGroup)
