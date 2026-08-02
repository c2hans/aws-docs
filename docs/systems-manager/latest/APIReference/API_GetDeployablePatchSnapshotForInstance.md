---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDeployablePatchSnapshotForInstance.html
---

# GetDeployablePatchSnapshotForInstance
<a name="API_GetDeployablePatchSnapshotForInstance"></a>

Retrieves the current snapshot for the patch baseline the managed node uses. This API is primarily used by the `AWS-RunPatchBaseline` Systems Manager document (SSM document).

**Note**
If you run the command locally, such as with the AWS Command Line Interface (AWS CLI), the system attempts to use your local AWS credentials and the operation fails. To avoid this, you can run the command in the AWS Systems Manager console. Use Run Command, a tool in AWS Systems Manager, with an SSM document that enables you to target a managed node with a script or command. For example, run the command using the `AWS-RunShellScript` document or the `AWS-RunPowerShellScript` document.

## Request Syntax
<a name="API_GetDeployablePatchSnapshotForInstance_RequestSyntax"></a>

```
{
   "BaselineOverride": {
      "ApprovalRules": {
         "PatchRules": [
            {
               "ApproveAfterDays": {{number}},
               "ApproveUntilDate": "{{string}}",
               "ComplianceLevel": "{{string}}",
               "EnableNonSecurity": {{boolean}},
               "PatchFilterGroup": {
                  "PatchFilters": [
                     {
                        "Key": "{{string}}",
                        "Values": [ "{{string}}" ]
                     }
                  ]
               }
            }
         ]
      },
      "ApprovedPatches": [ "{{string}}" ],
      "ApprovedPatchesComplianceLevel": "{{string}}",
      "ApprovedPatchesEnableNonSecurity": {{boolean}},
      "AvailableSecurityUpdatesComplianceStatus": "{{string}}",
      "GlobalFilters": {
         "PatchFilters": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ]
      },
      "OperatingSystem": "{{string}}",
      "RejectedPatches": [ "{{string}}" ],
      "RejectedPatchesAction": "{{string}}",
      "Sources": [
         {
            "Configuration": "{{string}}",
            "Name": "{{string}}",
            "Products": [ "{{string}}" ]
         }
      ]
   },
   "InstanceId": "{{string}}",
   "SnapshotId": "{{string}}",
   "UseS3DualStackEndpoint": {{boolean}}
}
```

## Request Parameters
<a name="API_GetDeployablePatchSnapshotForInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineOverride](#API_GetDeployablePatchSnapshotForInstance_RequestSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-request-BaselineOverride"></a>
Defines the basic information about a patch baseline override.
Type: [BaselineOverride](API_BaselineOverride.md) object
Required: No

 ** [InstanceId](#API_GetDeployablePatchSnapshotForInstance_RequestSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-request-InstanceId"></a>
The ID of the managed node for which the appropriate patch snapshot should be retrieved.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [SnapshotId](#API_GetDeployablePatchSnapshotForInstance_RequestSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-request-SnapshotId"></a>
The snapshot ID provided by the user when running `AWS-RunPatchBaseline`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** [UseS3DualStackEndpoint](#API_GetDeployablePatchSnapshotForInstance_RequestSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-request-UseS3DualStackEndpoint"></a>
Specifies whether to use S3 dualstack endpoints for the patch snapshot download URL. Set to `true` to receive a presigned URL that supports both IPv4 and IPv6 connectivity. Set to `false` to use standard IPv4-only endpoints. Default is `false`. This parameter is required for managed nodes in IPv6-only environments.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetDeployablePatchSnapshotForInstance_ResponseSyntax"></a>

```
{
   "InstanceId": "string",
   "Product": "string",
   "SnapshotDownloadUrl": "string",
   "SnapshotId": "string"
}
```

## Response Elements
<a name="API_GetDeployablePatchSnapshotForInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceId](#API_GetDeployablePatchSnapshotForInstance_ResponseSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-response-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`

 ** [Product](#API_GetDeployablePatchSnapshotForInstance_ResponseSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-response-Product"></a>
Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the managed node for the specified patch snapshot.
Type: String

 ** [SnapshotDownloadUrl](#API_GetDeployablePatchSnapshotForInstance_ResponseSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-response-SnapshotDownloadUrl"></a>
A pre-signed Amazon Simple Storage Service (Amazon S3) URL that can be used to download the patch snapshot.
Type: String

 ** [SnapshotId](#API_GetDeployablePatchSnapshotForInstance_ResponseSyntax) **   <a name="systemsmanager-GetDeployablePatchSnapshotForInstance-response-SnapshotId"></a>
The user-defined snapshot ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetDeployablePatchSnapshotForInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** UnsupportedFeatureRequiredException **
Patching for applications released by Microsoft is only available on EC2 instances and advanced instances. To patch applications released by Microsoft on on-premises servers and VMs, you must enable advanced instances. For more information, see [Turning on the advanced-instances tier](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances-advanced.html) in the * AWS Systems Manager User Guide*.
HTTP Status Code: 400

 ** UnsupportedOperatingSystem **
The operating systems you specified isn't supported, or the operation isn't supported for the operating system.
HTTP Status Code: 400

## Examples
<a name="API_GetDeployablePatchSnapshotForInstance_Examples"></a>

### Example
<a name="API_GetDeployablePatchSnapshotForInstance_Example_1"></a>

This example illustrates one usage of GetDeployablePatchSnapshotForInstance.

#### Sample Request
<a name="API_GetDeployablePatchSnapshotForInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 91
X-Amz-Target: AmazonSSM.GetDeployablePatchSnapshotForInstance
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.12 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/ssm.get-deployable-patch-snapshot-for-instance
X-Amz-Date: 20240618T204500Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240618/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "InstanceId": "i-02573cafcfEXAMPLE",
    "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE"
}
```

#### Sample Response
<a name="API_GetDeployablePatchSnapshotForInstance_Example_1_Response"></a>

```
{
    "InstanceId": "i-02573cafcfEXAMPLE",
    "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE",
    "Product": "AmazonLinux2018.03",
    "SnapshotDownloadUrl": "https://amzn-s3-demo-bucket.s3.us-east-2.amazonaws.com/b7d801675252464bEXAMPLE--truncated--"
}
```

## See Also
<a name="API_GetDeployablePatchSnapshotForInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)
