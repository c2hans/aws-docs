---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds tags to a resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
PUT /tags/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="licensemanagerusersubscriptions-TagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to tag.
Pattern: `arn:([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,63}):([a-z0-9-\.]{1,510})/([a-z0-9-\.]{1,510})`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="licensemanagerusersubscriptions-TagResource-request-Tags"></a>
The tags to apply to the specified resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/TagResource)
