---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetResourcePermission.html
---

# GetResourcePermission
<a name="API_GetResourcePermission"></a>

Gets permissions associated with the target database.

## Request Syntax
<a name="API_GetResourcePermission_RequestSyntax"></a>

```
POST /get-resource-permission HTTP/1.1
Content-type: application/json

{
   "ActionType": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetResourcePermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourcePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionType](#API_GetResourcePermission_RequestSyntax) **   <a name="ssmsap-GetResourcePermission-request-ActionType"></a>

Type: String
Valid Values: `RESTORE`
Required: No

 ** [ResourceArn](#API_GetResourcePermission_RequestSyntax) **   <a name="ssmsap-GetResourcePermission-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: Yes

## Response Syntax
<a name="API_GetResourcePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string"
}
```

## Response Elements
<a name="API_GetResourcePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetResourcePermission_ResponseSyntax) **   <a name="ssmsap-GetResourcePermission-response-Policy"></a>

Type: String

## Errors
<a name="API_GetResourcePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetResourcePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetResourcePermission)
