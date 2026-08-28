---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateWorkspaceInstance.html
---

# CreateWorkspaceInstance
<a name="API_CreateWorkspaceInstance"></a>

Launches a new WorkSpace Instance with specified configuration parameters, enabling programmatic workspace deployment.

## Request Syntax
<a name="API_CreateWorkspaceInstance_RequestSyntax"></a>

```
{
   "BillingConfiguration": {
      "BillingMode": "{{string}}"
   },
   "ClientToken": "{{string}}",
   "ManagedInstance": {
      "BlockDeviceMappings": [
         {
            "DeviceName": "{{string}}",
            "Ebs": {
               "Encrypted": {{boolean}},
               "Iops": {{number}},
               "KmsKeyId": "{{string}}",
               "Throughput": {{number}},
               "VolumeSize": {{number}},
               "VolumeType": "{{string}}"
            },
            "NoDevice": "{{string}}",
            "VirtualName": "{{string}}"
         }
      ],
      "CapacityReservationSpecification": {
         "CapacityReservationPreference": "{{string}}",
         "CapacityReservationTarget": {
            "CapacityReservationId": "{{string}}",
            "CapacityReservationResourceGroupArn": "{{string}}"
         }
      },
      "CpuOptions": {
         "AmdSevSnp": "{{string}}",
         "CoreCount": {{number}},
         "ThreadsPerCore": {{number}}
      },
      "CreditSpecification": {
         "CpuCredits": "{{string}}"
      },
      "DisableApiStop": {{boolean}},
      "EbsOptimized": {{boolean}},
      "EnablePrimaryIpv6": {{boolean}},
      "EnclaveOptions": {
         "Enabled": {{boolean}}
      },
      "HibernationOptions": {
         "Configured": {{boolean}}
      },
      "IamInstanceProfile": {
         "Arn": "{{string}}",
         "Name": "{{string}}"
      },
      "ImageId": "{{string}}",
      "InstanceMarketOptions": {
         "MarketType": "{{string}}",
         "SpotOptions": {
            "BlockDurationMinutes": {{number}},
            "InstanceInterruptionBehavior": "{{string}}",
            "MaxPrice": "{{string}}",
            "SpotInstanceType": "{{string}}",
            "ValidUntilUtc": {{number}}
         }
      },
      "InstanceType": "{{string}}",
      "Ipv6AddressCount": {{number}},
      "Ipv6Addresses": [
         {
            "Ipv6Address": "{{string}}",
            "IsPrimaryIpv6": {{boolean}}
         }
      ],
      "KernelId": "{{string}}",
      "KeyName": "{{string}}",
      "LicenseSpecifications": [
         {
            "LicenseConfigurationArn": "{{string}}"
         }
      ],
      "MaintenanceOptions": {
         "AutoRecovery": "{{string}}"
      },
      "MetadataOptions": {
         "HttpEndpoint": "{{string}}",
         "HttpProtocolIpv6": "{{string}}",
         "HttpPutResponseHopLimit": {{number}},
         "HttpTokens": "{{string}}",
         "InstanceMetadataTags": "{{string}}"
      },
      "Monitoring": {
         "Enabled": {{boolean}}
      },
      "NetworkInterfaces": [
         {
            "AssociateCarrierIpAddress": {{boolean}},
            "AssociatePublicIpAddress": {{boolean}},
            "ConnectionTrackingSpecification": {
               "TcpEstablishedTimeout": {{number}},
               "UdpStreamTimeout": {{number}},
               "UdpTimeout": {{number}}
            },
            "Description": "{{string}}",
            "DeviceIndex": {{number}},
            "EnaSrdSpecification": {
               "EnaSrdEnabled": {{boolean}},
               "EnaSrdUdpSpecification": {
                  "EnaSrdUdpEnabled": {{boolean}}
               }
            },
            "Groups": [ "{{string}}" ],
            "InterfaceType": "{{string}}",
            "Ipv4PrefixCount": {{number}},
            "Ipv4Prefixes": [
               {
                  "Ipv4Prefix": "{{string}}"
               }
            ],
            "Ipv6AddressCount": {{number}},
            "Ipv6Addresses": [
               {
                  "Ipv6Address": "{{string}}",
                  "IsPrimaryIpv6": {{boolean}}
               }
            ],
            "Ipv6PrefixCount": {{number}},
            "Ipv6Prefixes": [
               {
                  "Ipv6Prefix": "{{string}}"
               }
            ],
            "NetworkCardIndex": {{number}},
            "NetworkInterfaceId": "{{string}}",
            "PrimaryIpv6": {{boolean}},
            "PrivateIpAddress": "{{string}}",
            "PrivateIpAddresses": [
               {
                  "Primary": {{boolean}},
                  "PrivateIpAddress": "{{string}}"
               }
            ],
            "SecondaryPrivateIpAddressCount": {{number}},
            "SubnetId": "{{string}}"
         }
      ],
      "NetworkPerformanceOptions": {
         "BandwidthWeighting": "{{string}}"
      },
      "Placement": {
         "Affinity": "{{string}}",
         "AvailabilityZone": "{{string}}",
         "GroupId": "{{string}}",
         "GroupName": "{{string}}",
         "HostId": "{{string}}",
         "HostResourceGroupArn": "{{string}}",
         "PartitionNumber": {{number}},
         "Tenancy": "{{string}}"
      },
      "PrivateDnsNameOptions": {
         "EnableResourceNameDnsAAAARecord": {{boolean}},
         "EnableResourceNameDnsARecord": {{boolean}},
         "HostnameType": "{{string}}"
      },
      "PrivateIpAddress": "{{string}}",
      "RamdiskId": "{{string}}",
      "SecurityGroupIds": [ "{{string}}" ],
      "SecurityGroups": [ "{{string}}" ],
      "SubnetId": "{{string}}",
      "TagSpecifications": [
         {
            "ResourceType": "{{string}}",
            "Tags": [
               {
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "UserData": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateWorkspaceInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingConfiguration](#API_CreateWorkspaceInstance_RequestSyntax) **   <a name="workspacesinstances-CreateWorkspaceInstance-request-BillingConfiguration"></a>
Optional billing configuration for the WorkSpace Instance. Allows customers to specify their preferred billing mode when creating a new instance. Defaults to hourly billing if not specified.
Type: [BillingConfiguration](API_BillingConfiguration.md) object
Required: No

 ** [ClientToken](#API_CreateWorkspaceInstance_RequestSyntax) **   <a name="workspacesinstances-CreateWorkspaceInstance-request-ClientToken"></a>
Unique token to ensure idempotent instance creation, preventing duplicate workspace launches.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [ManagedInstance](#API_CreateWorkspaceInstance_RequestSyntax) **   <a name="workspacesinstances-CreateWorkspaceInstance-request-ManagedInstance"></a>
Comprehensive configuration settings for the WorkSpaces Instance, including network, compute, and storage parameters.
Type: [ManagedInstanceRequest](API_ManagedInstanceRequest.md) object
Required: Yes

 ** [Tags](#API_CreateWorkspaceInstance_RequestSyntax) **   <a name="workspacesinstances-CreateWorkspaceInstance-request-Tags"></a>
Optional metadata tags for categorizing and managing WorkSpaces Instances.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateWorkspaceInstance_ResponseSyntax"></a>

```
{
   "WorkspaceInstanceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspaceInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkspaceInstanceId](#API_CreateWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-CreateWorkspaceInstance-response-WorkspaceInstanceId"></a>
Unique identifier assigned to the newly created WorkSpaces Instance.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 70.
Pattern: `wsinst-[0-9a-zA-Z]{8,63}`

## Errors
<a name="API_CreateWorkspaceInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 400

 ** ConflictException **
Signals a conflict with the current state of the resource.
 ** Message **
Description of the conflict encountered.
 ** ResourceId **
Identifier of the conflicting resource.
 ** ResourceType **
Type of the conflicting resource.
HTTP Status Code: 400

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Indicates that a service quota has been exceeded.
 ** Message **
Description of the quota limitation.
 ** QuotaCode **
Specific code for the exceeded quota.
 ** ResourceId **
Identifier of the resource related to the quota.
 ** ResourceType **
Type of resource related to the quota.
 ** ServiceCode **
Code identifying the service with the quota limitation.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 400

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateWorkspaceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/CreateWorkspaceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/CreateWorkspaceInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
