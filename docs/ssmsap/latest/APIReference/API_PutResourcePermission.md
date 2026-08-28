---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_PutResourcePermission.html
---

# PutResourcePermission
<a name="API_PutResourcePermission"></a>

Adds permissions to the target database.

## Request Syntax
<a name="API_PutResourcePermission_RequestSyntax"></a>

```
POST /put-resource-permission HTTP/1.1
Content-type: application/json

{
   "ActionType": "{{string}}",
   "ResourceArn": "{{string}}",
   "SourceResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionType](#API_PutResourcePermission_RequestSyntax) **   <a name="ssmsap-PutResourcePermission-request-ActionType"></a>

Type: String
Valid Values: `RESTORE`
Required: Yes

 ** [ResourceArn](#API_PutResourcePermission_RequestSyntax) **   <a name="ssmsap-PutResourcePermission-request-ResourceArn"></a>

Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: Yes

 ** [SourceResourceArn](#API_PutResourcePermission_RequestSyntax) **   <a name="ssmsap-PutResourcePermission-request-SourceResourceArn"></a>

Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: Yes

## Response Syntax
<a name="API_PutResourcePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string"
}
```

## Response Elements
<a name="API_PutResourcePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutResourcePermission_ResponseSyntax) **   <a name="ssmsap-PutResourcePermission-response-Policy"></a>

Type: String

## Errors
<a name="API_PutResourcePermission_Errors"></a>

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
<a name="API_PutResourcePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/PutResourcePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/PutResourcePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
