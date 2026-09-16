---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeReplicationConfigurationTemplates.html
---

# DescribeReplicationConfigurationTemplates
<a name="API_DescribeReplicationConfigurationTemplates"></a>

Lists all ReplicationConfigurationTemplates, filtered by replication configuration template IDs.

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

 ** [maxResults](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeReplicationConfigurationTemplates-request-maxResults"></a>
Request to describe Replication Configuration template by max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeReplicationConfigurationTemplates-request-nextToken"></a>
Request to describe Replication Configuration template by next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [replicationConfigurationTemplateIDs](#API_DescribeReplicationConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeReplicationConfigurationTemplates-request-replicationConfigurationTemplateIDs"></a>
Request to describe Replication Configuration template by template IDs.
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
         "bandwidthThrottling": number,
         "createPublicIP": boolean,
         "dataPlaneRouting": "string",
         "defaultLargeStagingDiskType": "string",
         "ebsEncryption": "string",
         "ebsEncryptionKeyArn": "string",
         "internetProtocol": "string",
         "replicationConfigurationTemplateID": "string",
         "replicationServerInstanceType": "string",
         "replicationServersSecurityGroupsIDs": [ "string" ],
         "stagingAreaSubnetId": "string",
         "stagingAreaTags": {
            "string" : "string"
         },
         "storageConfiguration": {
            "fsxOntapConfiguration": {
               "credentialsSecretArn": "string",
               "storageVirtualMachineId": "string"
            },
            "storageType": "string"
         },
         "storeSnapshotOnLocalZone": boolean,
         "tags": {
            "string" : "string"
         },
         "useDedicatedReplicationServer": boolean,
         "useFipsEndpoint": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeReplicationConfigurationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeReplicationConfigurationTemplates_ResponseSyntax) **   <a name="mgn-DescribeReplicationConfigurationTemplates-response-items"></a>
Request to describe Replication Configuration template by items.
Type: Array of [ReplicationConfigurationTemplate](API_ReplicationConfigurationTemplate.md) objects

 ** [nextToken](#API_DescribeReplicationConfigurationTemplates_ResponseSyntax) **   <a name="mgn-DescribeReplicationConfigurationTemplates-response-nextToken"></a>
Request to describe Replication Configuration template by next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeReplicationConfigurationTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReplicationConfigurationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeReplicationConfigurationTemplates)
