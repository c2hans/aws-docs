---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateWorkgroup.html
---

# CreateWorkgroup
<a name="API_CreateWorkgroup"></a>

Creates an workgroup in Amazon Redshift Serverless.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked:
+ Creating a public access workgroup
+ Modifying a private workgroup to public
+ Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Syntax
<a name="API_CreateWorkgroup_RequestSyntax"></a>

```
{
   "baseCapacity": {{number}},
   "configParameters": [
      {
         "parameterKey": "{{string}}",
         "parameterValue": "{{string}}"
      }
   ],
   "enhancedVpcRouting": {{boolean}},
   "extraComputeForAutomaticOptimization": {{boolean}},
   "ipAddressType": "{{string}}",
   "maxCapacity": {{number}},
   "namespaceName": "{{string}}",
   "port": {{number}},
   "pricePerformanceTarget": {
      "level": {{number}},
      "status": "{{string}}"
   },
   "publiclyAccessible": {{boolean}},
   "securityGroupIds": [ "{{string}}" ],
   "subnetIds": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "trackName": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateWorkgroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [baseCapacity](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-baseCapacity"></a>
The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
Type: Integer
Required: No

 ** [configParameters](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-configParameters"></a>
An array of parameters to set for advanced control over a database. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and either `wlm_json_configuration` or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as `max_scan_row_count`, `max_query_execution_time`) or use `wlm_json_configuration` to define query queues with rules, but not both. If you're using `wlm_json_configuration`, the maximum size of `parameterValue` is 8000 characters. For more information about query monitoring rules and available metrics, see [ Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
Type: Array of [ConfigParameter](API_ConfigParameter.md) objects
Required: No

 ** [enhancedVpcRouting](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-enhancedVpcRouting"></a>
The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC instead of over the internet.
Type: Boolean
Required: No

 ** [extraComputeForAutomaticOptimization](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-extraComputeForAutomaticOptimization"></a>
If `true`, allocates additional compute resources for running automatic optimization operations.
Default: false
Type: Boolean
Required: No

 ** [ipAddressType](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-ipAddressType"></a>
The IP address type that the workgroup supports. Possible values are `ipv4` and `dualstack`.
Type: String
Pattern: `(ipv4|dualstack)`
Required: No

 ** [maxCapacity](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-maxCapacity"></a>
The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
Type: Integer
Required: No

 ** [namespaceName](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-namespaceName"></a>
The name of the namespace to associate with the workgroup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [port](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-port"></a>
The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
Type: Integer
Required: No

 ** [pricePerformanceTarget](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-pricePerformanceTarget"></a>
An object that represents the price performance target settings for the workgroup.
Type: [PerformanceTarget](API_PerformanceTarget.md) object
Required: No

 ** [publiclyAccessible](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-publiclyAccessible"></a>
A value that specifies whether the workgroup can be accessed from a public network.
Type: Boolean
Required: No

 ** [securityGroupIds](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-securityGroupIds"></a>
An array of security group IDs to associate with the workgroup.
Type: Array of strings
Required: No

 ** [subnetIds](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-subnetIds"></a>
An array of VPC subnet IDs to associate with the workgroup.
Type: Array of strings
Required: No

 ** [tags](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-tags"></a>
A array of tag instances.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [trackName](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-trackName"></a>
An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the `current` track.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_]+`
Required: No

 ** [workgroupName](#API_CreateWorkgroup_RequestSyntax) **   <a name="redshiftserverless-CreateWorkgroup-request-workgroupName"></a>
The name of the created workgroup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_CreateWorkgroup_ResponseSyntax"></a>

```
{
   "workgroup": {
      "baseCapacity": number,
      "configParameters": [
         {
            "parameterKey": "string",
            "parameterValue": "string"
         }
      ],
      "creationDate": "string",
      "crossAccountVpcs": [ "string" ],
      "customDomainCertificateArn": "string",
      "customDomainCertificateExpiryTime": "string",
      "customDomainName": "string",
      "endpoint": {
         "address": "string",
         "port": number,
         "vpcEndpoints": [
            {
               "networkInterfaces": [
                  {
                     "availabilityZone": "string",
                     "ipv6Address": "string",
                     "networkInterfaceId": "string",
                     "privateIpAddress": "string",
                     "subnetId": "string"
                  }
               ],
               "vpcEndpointId": "string",
               "vpcId": "string"
            }
         ]
      },
      "enhancedVpcRouting": boolean,
      "extraComputeForAutomaticOptimization": boolean,
      "ipAddressType": "string",
      "maxCapacity": number,
      "namespaceName": "string",
      "patchVersion": "string",
      "pendingTrackName": "string",
      "port": number,
      "pricePerformanceTarget": {
         "level": number,
         "status": "string"
      },
      "publiclyAccessible": boolean,
      "securityGroupIds": [ "string" ],
      "status": "string",
      "subnetIds": [ "string" ],
      "trackName": "string",
      "workgroupArn": "string",
      "workgroupId": "string",
      "workgroupName": "string",
      "workgroupVersion": "string"
   }
}
```

## Response Elements
<a name="API_CreateWorkgroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workgroup](#API_CreateWorkgroup_ResponseSyntax) **   <a name="redshiftserverless-CreateWorkgroup-response-workgroup"></a>
The created workgroup object.
Type: [Workgroup](API_Workgroup.md) object

## Errors
<a name="API_CreateWorkgroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InsufficientCapacityException **
There is an insufficient capacity to perform the action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** Ipv6CidrBlockNotFoundException **
There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** TooManyTagsException **
The request exceeded the number of tags allowed for a resource.
 ** resourceName **
The name of the resource that exceeded the number of tags allowed for a resource.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_CreateWorkgroup_Examples"></a>

### Example
<a name="API_CreateWorkgroup_Example_1"></a>

This example illustrates one usage of CreateWorkgroup.

#### Sample Request
<a name="API_CreateWorkgroup_Example_1_Request"></a>

```
aws redshift-serverless create-workgroup
--workgroup-name test-workgroup
--namespace-name test-namespace
--track-name current
--region us-east-1
```

#### Sample Response
<a name="API_CreateWorkgroup_Example_1_Response"></a>

```
{
    "workgroup": {
        "workgroupId": "875083e4-50b5-4ad7-bd8b-b01beb74d912",
        "workgroupArn": "arn:aws:redshift-serverless:us-east-1:012345678901:workgroup/875083e4-50b5-4ad7-bd8b-b01beb74d912",
        "workgroupName": "test-workgroup",
        "namespaceName": "test-namespace",
        "baseCapacity": 32,
        "enhancedVpcRouting": false,
        ...
        "securityGroupIds": [
            "sg-0f0e3edaf8473b3d2"
        ],
        "subnetIds": [
            "subnet-05a4615a242adf950",
            "subnet-0d364615acc244f2a",
            "subnet-037672f31c13d78a0",
            "subnet-062539bdf89dfa749",
            "subnet-01534423c994e5e30",
            "subnet-042b4ad9afe0826c6"
        ],
        "status": "CREATING",
        "endpoint": {
            "address": "test-workgroup-1.012345678901.us-east-1-dsk.redshift-serverless-dev.amazonaws.com",
            "port": 5439
        },
        "publiclyAccessible": false,
        "creationDate": "2024-12-13T14:19:50.636000+00:00",
        "pricePerformanceTarget": {
            "status": "DISABLED"
        },
        "ipAddressType": "ipv4",
        "trackName": "current"
    }
}
```

## See Also
<a name="API_CreateWorkgroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateWorkgroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateWorkgroup)
