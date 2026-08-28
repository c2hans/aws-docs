---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAssociationsOnce.html
---

# StartAssociationsOnce
<a name="API_StartAssociationsOnce"></a>

Runs an association immediately and only one time. This operation can be helpful when troubleshooting associations.

## Request Syntax
<a name="API_StartAssociationsOnce_RequestSyntax"></a>

```
{
   "AssociationIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StartAssociationsOnce_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationIds](#API_StartAssociationsOnce_RequestSyntax) **   <a name="systemsmanager-StartAssociationsOnce-request-AssociationIds"></a>
The association IDs that you want to run immediately and only one time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

## Response Elements
<a name="API_StartAssociationsOnce_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartAssociationsOnce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InvalidAssociation **
The association isn't valid or doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_StartAssociationsOnce_Examples"></a>

### Example
<a name="API_StartAssociationsOnce_Example_1"></a>

This example illustrates one usage of StartAssociationsOnce.

#### Sample Request
<a name="API_StartAssociationsOnce_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.StartAssociationsOnce
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T163434Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 60

{
    "AssociationIds": [
        "4332cf28-050d-4fa1-a4df-11b39EXAMPLE"
    ]
}
```

#### Sample Response
<a name="API_StartAssociationsOnce_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_StartAssociationsOnce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StartAssociationsOnce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StartAssociationsOnce)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
