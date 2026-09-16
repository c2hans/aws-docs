---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html
---

# GetAccessPointScope
<a name="API_control_GetAccessPointScope"></a>

 Returns the access point scope for a directory bucket.

To use this operation, you must have the permission to perform the `s3express:GetAccessPointScope` action.

For information about REST API errors, see [REST error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses).

## Request Syntax
<a name="API_control_GetAccessPointScope_RequestSyntax"></a>

```
GET /v20180820/accesspoint/{{name}}/scope HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPointScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointScope-request-uri-uri-Name"></a>
The name of the access point with the scope you want to retrieve.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointScope-request-header-AccountId"></a>
 The AWS account ID that owns the access point with the scope that you want to retrieve.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPointScope_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPointScope_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointScopeResult>
   <Scope>
      <Permissions>
         <Permission>string</Permission>
      </Permissions>
      <Prefixes>
         <Prefix>string</Prefix>
      </Prefixes>
   </Scope>
</GetAccessPointScopeResult>
```

## Response Elements
<a name="API_control_GetAccessPointScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointScopeResult](#API_control_GetAccessPointScope_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointScope-response-GetAccessPointScopeResult"></a>
Root level tag for the GetAccessPointScopeResult parameters.
Required: Yes

 ** [Scope](#API_control_GetAccessPointScope_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointScope-response-Scope"></a>
The contents of the access point scope.
Type: [Scope](API_control_Scope.md) data type

## See Also
<a name="API_control_GetAccessPointScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointScope)
