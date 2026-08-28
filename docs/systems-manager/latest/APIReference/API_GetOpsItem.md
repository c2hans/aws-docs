---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsItem.html
---

# GetOpsItem
<a name="API_GetOpsItem"></a>

Get information about an OpsItem by using the ID. You must have permission in AWS Identity and Access Management (IAM) to view information about an OpsItem. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the * AWS Systems Manager User Guide*.

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_GetOpsItem_RequestSyntax"></a>

```
{
   "OpsItemArn": "{{string}}",
   "OpsItemId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOpsItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OpsItemArn](#API_GetOpsItem_RequestSyntax) **   <a name="systemsmanager-GetOpsItem-request-OpsItemArn"></a>
The OpsItem Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[0-9]{12}:opsitem.*`
Required: No

 ** [OpsItemId](#API_GetOpsItem_RequestSyntax) **   <a name="systemsmanager-GetOpsItem-request-OpsItemId"></a>
The ID of the OpsItem that you want to get.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetOpsItem_ResponseSyntax"></a>

```
{
   "OpsItem": {
      "ActualEndTime": number,
      "ActualStartTime": number,
      "Category": "string",
      "CreatedBy": "string",
      "CreatedTime": number,
      "Description": "string",
      "LastModifiedBy": "string",
      "LastModifiedTime": number,
      "Notifications": [
         {
            "Arn": "string"
         }
      ],
      "OperationalData": {
         "string" : {
            "Type": "string",
            "Value": "string"
         }
      },
      "OpsItemArn": "string",
      "OpsItemId": "string",
      "OpsItemType": "string",
      "PlannedEndTime": number,
      "PlannedStartTime": number,
      "Priority": number,
      "RelatedOpsItems": [
         {
            "OpsItemId": "string"
         }
      ],
      "Severity": "string",
      "Source": "string",
      "Status": "string",
      "Title": "string",
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_GetOpsItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OpsItem](#API_GetOpsItem_ResponseSyntax) **   <a name="systemsmanager-GetOpsItem-response-OpsItem"></a>
The OpsItem.
Type: [OpsItem](API_OpsItem.md) object

## Errors
<a name="API_GetOpsItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemAccessDeniedException **
You don't have permission to view OpsItems in the specified account. Verify that your account is configured either as a Systems Manager delegated administrator or that you are logged into the AWS Organizations management account.
HTTP Status Code: 400

 ** OpsItemNotFoundException **
The specified OpsItem ID doesn't exist. Verify the ID and try again.
HTTP Status Code: 400

## Examples
<a name="API_GetOpsItem_Examples"></a>

### Example
<a name="API_GetOpsItem_Example_1"></a>

This example illustrates one usage of GetOpsItem.

#### Sample Request
<a name="API_GetOpsItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetOpsItem
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T153712Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 32

{
    "OpsItemId": "oi-f99f2EXAMPLE"
}
```

#### Sample Response
<a name="API_GetOpsItem_Example_1_Response"></a>

```
{
    "OpsItem": {
        "Category": "Availability",
        "CreatedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
        "CreatedTime": 1582701517.193,
        "Description": "CloudWatch Event Rule SSMOpsItems-SSM-maintenance-window-execution-failed was triggered. Your SSM Maintenance Window execution has failed. See below for more details.",
        "LastModifiedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
        "LastModifiedTime": 1582701517.193,
        "Notifications": [],
        "OperationalData": {
            "/aws/dedup": {
                "Type": "SearchableString",
                "Value": "{\"dedupString\":\"SSMOpsItems-SSM-maintenance-window-execution-failed\"}"
            },
            "/aws/resources": {
                "Type": "SearchableString",
                "Value": "[{\"arn\":\"arn:aws:ssm:us-east-2:111122223333:maintenancewindow/mw-0e357ebdc6EXAMPLE\"}]"
            },
            "window-execution-id": {
                "Type": "String",
                "Value": "e79e904b-0e42-43b8-a83d-b2aedEXAMPLE"
            },
            "window-id": {
                "Type": "String",
                "Value": "mw-0e357ebdc6EXAMPLE"
            }
        },
        "OpsItemId": "oi-f99f2EXAMPLE",
        "RelatedOpsItems": [],
        "Severity": "3",
        "Source": "SSM",
        "Status": "Open",
        "Title": "SSM Maintenance Window execution failed"
    }
}
```

## See Also
<a name="API_GetOpsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetOpsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetOpsItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
