---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutComplianceItems.html
---

# PutComplianceItems
<a name="API_PutComplianceItems"></a>

Registers a compliance type and other compliance details on a designated resource. This operation lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.

ComplianceType can be one of the following:
+ ExecutionId: The execution ID when the patch, association, or custom compliance item was applied.
+ ExecutionType: Specify patch, association, or Custom:`string`.
+ ExecutionTime. The time the patch, association, or custom compliance item was applied to the managed node.
**Important**
For State Manager associations, this represents the time when compliance status was captured by the Systems Manager service during its internal compliance aggregation workflow, not necessarily when the association was executed on the managed node. State Manager updates compliance information for all associations on an instance whenever any association executes, which may result in multiple associations showing the same execution time.
+ Id: The patch, association, or custom compliance ID.
+ Title: A title.
+ Status: The status of the compliance item. For example, `approved` for patches, or `Failed` for associations.
+ Severity: A patch severity. For example, `Critical`.
+ DocumentName: An SSM document name. For example, `AWS-RunPatchBaseline`.
+ DocumentVersion: An SSM document version number. For example, 4.
+ Classification: A patch classification. For example, `security updates`.
+ PatchBaselineId: A patch baseline ID.
+ PatchSeverity: A patch severity. For example, `Critical`.
+ PatchState: A patch state. For example, `InstancesWithFailedPatches`.
+ PatchGroup: The name of a patch group.
+ InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

## Request Syntax
<a name="API_PutComplianceItems_RequestSyntax"></a>

```
{
   "ComplianceType": "{{string}}",
   "ExecutionSummary": {
      "ExecutionId": "{{string}}",
      "ExecutionTime": {{number}},
      "ExecutionType": "{{string}}"
   },
   "ItemContentHash": "{{string}}",
   "Items": [
      {
         "Details": {
            "{{string}}" : "{{string}}"
         },
         "Id": "{{string}}",
         "Severity": "{{string}}",
         "Status": "{{string}}",
         "Title": "{{string}}"
      }
   ],
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}",
   "UploadType": "{{string}}"
}
```

## Request Parameters
<a name="API_PutComplianceItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComplianceType](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-ComplianceType"></a>
Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:`string`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([A-Za-z0-9_\-]\w+|Custom:[a-zA-Z0-9_\-]\w+)$`
Required: Yes

 ** [ExecutionSummary](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-ExecutionSummary"></a>
A summary of the call execution that includes an execution ID, the type of execution (for example, `Command`), and the date/time of the execution using a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`
Type: [ComplianceExecutionSummary](API_ComplianceExecutionSummary.md) object
Required: Yes

 ** [ItemContentHash](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-ItemContentHash"></a>
MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Items](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-Items"></a>
Information about the compliance as defined by the resource type. For example, for a patch compliance type, `Items` includes information about the PatchSeverity, Classification, and so on.
Type: Array of [ComplianceItemEntry](API_ComplianceItemEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Required: Yes

 ** [ResourceId](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-ResourceId"></a>
Specify an ID for this resource. For a managed node, this is the node ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceType](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-ResourceType"></a>
Specify the type of resource. `ManagedInstance` is currently the only supported resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** [UploadType](#API_PutComplianceItems_RequestSyntax) **   <a name="systemsmanager-PutComplianceItems-request-UploadType"></a>
The mode for uploading compliance items. You can specify `COMPLETE` or `PARTIAL`. In `COMPLETE` mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.
In `PARTIAL` mode, the system overwrites compliance information for a specific association. The association must be configured with `SyncCompliance` set to `MANUAL`. By default, all requests use `COMPLETE` mode.
This attribute is only valid for association compliance.
Type: String
Valid Values: `COMPLETE | PARTIAL`
Required: No

## Response Elements
<a name="API_PutComplianceItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutComplianceItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ComplianceTypeCountLimitExceededException **
You specified too many custom compliance types. You can specify a maximum of 10 different types.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidItemContentException **
One or more content items isn't valid.
HTTP Status Code: 400

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

 ** InvalidResourceType **
The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.
HTTP Status Code: 400

 ** ItemSizeLimitExceededException **
The inventory item size has exceeded the size limit.
HTTP Status Code: 400

 ** TotalSizeLimitExceededException **
The size of inventory data has exceeded the total size limit for the resource.
HTTP Status Code: 400

## Examples
<a name="API_PutComplianceItems_Examples"></a>

### Example
<a name="API_PutComplianceItems_Example_1"></a>

This example illustrates one usage of PutComplianceItems.

#### Sample Request
<a name="API_PutComplianceItems_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.PutComplianceItems
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.27 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/ssm.put-compliance-items
X-Amz-Date: 20240811T170036Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240811/us-west-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 260

{
  "ResourceId": "i-02573cafcfEXAMPLE",
  "ResourceType": "ManagedInstance",
  "ComplianceType": "Custom:AVCheck",
  "ExecutionSummary": {
    "ExecutionTime": 1628697600
  },
  "Items": [
    {
      "Id": "Version2.0",
      "Title": "ScanHost",
      "Severity": "CRITICAL",
      "Status": "COMPLIANT"
    }
  ]
}
```

#### Sample Response
<a name="API_PutComplianceItems_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_PutComplianceItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/PutComplianceItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PutComplianceItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
