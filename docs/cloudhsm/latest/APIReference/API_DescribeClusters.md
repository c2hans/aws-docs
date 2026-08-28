---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html
---

# DescribeClusters
<a name="API_DescribeClusters"></a>

Gets information about AWS CloudHSM clusters.

This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a `NextToken` value. Use this value in a subsequent `DescribeClusters` request to get more clusters. When you receive a response with no `NextToken` (or an empty or null value), that means there are no more clusters to get.

 **Cross-account use:** No. You cannot perform this operation on AWS CloudHSM clusters in a different AWS account.

## Request Syntax
<a name="API_DescribeClusters_RequestSyntax"></a>

```
{
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeClusters_RequestSyntax) **   <a name="CloudHSMV2-DescribeClusters-request-Filters"></a>
One or more filters to limit the items returned in the response.
Use the `clusterIds` filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).
Use the `vpcIds` filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).
Use the `states` filter to return only clusters that match the specified state.
Type: String to array of strings map
Map Entries: Maximum number of 30 items.
Key Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [MaxResults](#API_DescribeClusters_RequestSyntax) **   <a name="CloudHSMV2-DescribeClusters-request-MaxResults"></a>
The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeClusters_RequestSyntax) **   <a name="CloudHSMV2-DescribeClusters-request-NextToken"></a>
The `NextToken` value that you received in the previous response. Use this value to get more clusters.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_DescribeClusters_ResponseSyntax"></a>

```
{
   "Clusters": [
      {
         "BackupPolicy": "string",
         "BackupRetentionPolicy": {
            "Type": "string",
            "Value": "string"
         },
         "Certificates": {
            "AwsHardwareCertificate": "string",
            "ClusterCertificate": "string",
            "ClusterCsr": "string",
            "HsmCertificate": "string",
            "ManufacturerHardwareCertificate": "string"
         },
         "ClusterId": "string",
         "CreateTimestamp": number,
         "Hsms": [
            {
               "AvailabilityZone": "string",
               "ClusterId": "string",
               "EniId": "string",
               "EniIp": "string",
               "EniIpV6": "string",
               "HsmId": "string",
               "HsmType": "string",
               "State": "string",
               "StateMessage": "string",
               "SubnetId": "string"
            }
         ],
         "HsmType": "string",
         "HsmTypeRollbackExpiration": number,
         "Mode": "string",
         "NetworkType": "string",
         "PreCoPassword": "string",
         "SecurityGroup": "string",
         "SourceBackupId": "string",
         "State": "string",
         "StateMessage": "string",
         "SubnetMapping": {
            "string" : "string"
         },
         "TagList": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "VpcId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Clusters](#API_DescribeClusters_ResponseSyntax) **   <a name="CloudHSMV2-DescribeClusters-response-Clusters"></a>
A list of clusters.
Type: Array of [Cluster](API_Cluster.md) objects

 ** [NextToken](#API_DescribeClusters_ResponseSyntax) **   <a name="CloudHSMV2-DescribeClusters-response-NextToken"></a>
An opaque string that indicates that the response contains only a subset of clusters. Use this value in a subsequent `DescribeClusters` request to get more clusters.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_DescribeClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmAccessDeniedException **
The request was rejected because the requester does not have permission to perform the requested operation.
HTTP Status Code: 400

 ** CloudHsmInternalFailureException **
The request was rejected because of an AWS CloudHSM internal failure. The request can be retried.
HTTP Status Code: 500

 ** CloudHsmInvalidRequestException **
The request was rejected because it is not a valid request.
HTTP Status Code: 400

 ** CloudHsmServiceException **
The request was rejected because an error occurred.
HTTP Status Code: 400

 ** CloudHsmTagException **
The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DescribeClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DescribeClusters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
