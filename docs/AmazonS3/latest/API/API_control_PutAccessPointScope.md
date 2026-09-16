---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html
---

# PutAccessPointScope
<a name="API_control_PutAccessPointScope"></a>

Creates or replaces the access point scope for a directory bucket. You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.

**Note**
You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.

To use this operation, you must have the permission to perform the `s3express:PutAccessPointScope` action.

For information about REST API errors, see [REST error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses).

## Request Syntax
<a name="API_control_PutAccessPointScope_RequestSyntax"></a>

```
PUT /v20180820/accesspoint/{{name}}/scope HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointScopeRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Scope>
      <Permissions>
         <Permission>{{string}}</Permission>
      </Permissions>
      <Prefixes>
         <Prefix>{{string}}</Prefix>
      </Prefixes>
   </Scope>
</PutAccessPointScopeRequest>
```

## URI Request Parameters
<a name="API_control_PutAccessPointScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointScope-request-uri-uri-Name"></a>
The name of the access point with the scope that you want to create or replace.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_PutAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointScope-request-header-AccountId"></a>
 The AWS account ID that owns the access point with scope that you want to create or replace.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutAccessPointScope_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutAccessPointScopeRequest](#API_control_PutAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointScope-request-PutAccessPointScopeRequest"></a>
Root level tag for the PutAccessPointScopeRequest parameters.
Required: Yes

 ** [Scope](#API_control_PutAccessPointScope_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointScope-request-Scope"></a>
Object prefixes, API operations, or a combination of both.
Type: [Scope](API_control_Scope.md) data type
Required: Yes

## Response Syntax
<a name="API_control_PutAccessPointScope_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutAccessPointScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_PutAccessPointScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointScope)
