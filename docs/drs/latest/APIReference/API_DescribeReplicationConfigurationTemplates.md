---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeReplicationConfigurationTemplates.html
---

# DescribeReplicationConfigurationTemplates
<a name="API_DescribeReplicationConfigurationTemplates"></a>

Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.

## Request Syntax
<a name="API_DescribeReplicationConfigurationTemplates_RequestSyntax"></a>

```
POST /DescribeReplicationConfigurationTemplates HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "replicationConfigurationTemplateIDs": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeReplicationConfigurationTemplates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeReplicationConfigurationTemplates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeReplicationConfigurationTemplates-request-maxResults"></a>
Maximum number of Replication Configuration Templates to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeReplicationConfigurationTemplates-request-nextToken"></a>
The token of the next Replication Configuration Template to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [replicationConfigurationTemplateIDs](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeReplicationConfigurationTemplates-request-replicationConfigurationTemplateIDs"></a>
The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: No

## Response Syntax
<a name="API_DescribeReplicationConfigurationTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "associateDefaultSecurityGroup": boolean,
         "autoReplicateNewDisks": boolean,
         "bandwidthThrottling": number,
         "createPublicIP": boolean,
         "dataPlaneRouting": "string",
         "defaultLargeStagingDiskType": "string",
         "ebsEncryption": "string",
         "ebsEncryptionKeyArn": "string",
         "internetProtocol": "string",
         "pitPolicy": [
            {
               "enabled": boolean,
               "interval": number,
               "retentionDuration": number,
               "ruleID": number,
               "units": "string"
            }
         ],
         "replicationConfigurationTemplateID": "string",
         "replicationServerInstanceType": "string",
         "replicationServersSecurityGroupsIDs": [ "string" ],
         "stagingAreaSubnetId": "string",
         "stagingAreaTags": {
            "string" : "string"
         },
         "tags": {
            "string" : "string"
         },
         "useDedicatedReplicationServer": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeReplicationConfigurationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeReplicationConfigurationTemplates_ResponseSyntax) **   <a name="drs-DescribeReplicationConfigurationTemplates-response-items"></a>
An array of Replication Configuration Templates.
Type: Array of [ReplicationConfigurationTemplate](API_ReplicationConfigurationTemplate.md) objects

 ** [nextToken](#API_DescribeReplicationConfigurationTemplates_ResponseSyntax) **   <a name="drs-DescribeReplicationConfigurationTemplates-response-nextToken"></a>
The token of the next Replication Configuration Template to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeReplicationConfigurationTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReplicationConfigurationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeReplicationConfigurationTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
