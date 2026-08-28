---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindings.html
---

# GetFindings
<a name="API_GetFindings"></a>

Describes Amazon GuardDuty findings specified by finding IDs.

## Request Syntax
<a name="API_GetFindings_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/findings/get HTTP/1.1
Content-type: application/json

{
   "findingIds": [ "{{string}}" ],
   "sortCriteria": {
      "attributeName": "{{string}}",
      "orderBy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetFindings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetFindings_RequestSyntax) **   <a name="guardduty-GetFindings-request-uri-DetectorId"></a>
The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingIds](#API_GetFindings_RequestSyntax) **   <a name="guardduty-GetFindings-request-findingIds"></a>
The IDs of the findings that you want to retrieve.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [sortCriteria](#API_GetFindings_RequestSyntax) **   <a name="guardduty-GetFindings-request-sortCriteria"></a>
Represents the criteria used for sorting findings.
Type: [SortCriteria](API_SortCriteria.md) object
Required: No

## Response Syntax
<a name="API_GetFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "accountId": "string",
         "arn": "string",
         "associatedAttackSequenceArn": "string",
         "confidence": number,
         "createdAt": "string",
         "description": "string",
         "id": "string",
         "partition": "string",
         "region": "string",
         "resource": {
            "accessKeyDetails": {
               "accessKeyId": "string",
               "principalId": "string",
               "userName": "string",
               "userType": "string"
            },
            "bedrockGuardrailDetails": {
               "contentPolicyFilters": [
                  {
                     "action": "string",
                     "confidence": "string",
                     "type": "string"
                  }
               ],
               "guardrailAction": "string",
               "guardrailArn": "string",
               "guardrails": [
                  {
                     "arn": "string",
                     "version": "string"
                  }
               ],
               "guardrailSource": "string",
               "guardrailVersion": "string"
            },
            "containerDetails": {
               "containerRuntime": "string",
               "id": "string",
               "image": "string",
               "imagePrefix": "string",
               "name": "string",
               "securityContext": {
                  "allowPrivilegeEscalation": boolean,
                  "privileged": boolean
               },
               "volumeMounts": [
                  {
                     "mountPath": "string",
                     "name": "string"
                  }
               ]
            },
            "ebsSnapshotDetails": {
               "snapshotArn": "string"
            },
            "ebsVolumeDetails": {
               "scannedVolumeDetails": [
                  {
                     "deviceName": "string",
                     "encryptionType": "string",
                     "kmsKeyArn": "string",
                     "snapshotArn": "string",
                     "volumeArn": "string",
                     "volumeSizeInGB": number,
                     "volumeType": "string"
                  }
               ],
               "skippedVolumeDetails": [
                  {
                     "deviceName": "string",
                     "encryptionType": "string",
                     "kmsKeyArn": "string",
                     "snapshotArn": "string",
                     "volumeArn": "string",
                     "volumeSizeInGB": number,
                     "volumeType": "string"
                  }
               ]
            },
            "ec2ImageDetails": {
               "imageArn": "string"
            },
            "ecsClusterDetails": {
               "activeServicesCount": number,
               "arn": "string",
               "name": "string",
               "registeredContainerInstancesCount": number,
               "runningTasksCount": number,
               "status": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "taskDetails": {
                  "arn": "string",
                  "containers": [
                     {
                        "containerRuntime": "string",
                        "id": "string",
                        "image": "string",
                        "imagePrefix": "string",
                        "name": "string",
                        "securityContext": {
                           "allowPrivilegeEscalation": boolean,
                           "privileged": boolean
                        },
                        "volumeMounts": [
                           {
                              "mountPath": "string",
                              "name": "string"
                           }
                        ]
                     }
                  ],
                  "definitionArn": "string",
                  "group": "string",
                  "launchType": "string",
                  "startedAt": number,
                  "startedBy": "string",
                  "tags": [
                     {
                        "key": "string",
                        "value": "string"
                     }
                  ],
                  "createdAt": number,
                  "version": "string",
                  "volumes": [
                     {
                        "hostPath": {
                           "path": "string"
                        },
                        "name": "string"
                     }
                  ]
               }
            },
            "eksClusterDetails": {
               "arn": "string",
               "createdAt": number,
               "name": "string",
               "status": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "vpcId": "string"
            },
            "instanceDetails": {
               "availabilityZone": "string",
               "iamInstanceProfile": {
                  "arn": "string",
                  "id": "string"
               },
               "imageDescription": "string",
               "imageId": "string",
               "instanceId": "string",
               "instanceState": "string",
               "instanceType": "string",
               "launchTime": "string",
               "networkInterfaces": [
                  {
                     "ipv6Addresses": [ "string" ],
                     "networkInterfaceId": "string",
                     "privateDnsName": "string",
                     "privateIpAddress": "string",
                     "privateIpAddresses": [
                        {
                           "privateDnsName": "string",
                           "privateIpAddress": "string"
                        }
                     ],
                     "publicDnsName": "string",
                     "publicIp": "string",
                     "securityGroups": [
                        {
                           "groupId": "string",
                           "groupName": "string"
                        }
                     ],
                     "subnetId": "string",
                     "vpcId": "string"
                  }
               ],
               "outpostArn": "string",
               "platform": "string",
               "productCodes": [
                  {
                     "productCodeId": "string",
                     "productCodeType": "string"
                  }
               ],
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ]
            },
            "kubernetesDetails": {
               "kubernetesUserDetails": {
                  "groups": [ "string" ],
                  "impersonatedUser": {
                     "groups": [ "string" ],
                     "username": "string"
                  },
                  "sessionName": [ "string" ],
                  "uid": "string",
                  "username": "string"
               },
               "kubernetesWorkloadDetails": {
                  "containers": [
                     {
                        "containerRuntime": "string",
                        "id": "string",
                        "image": "string",
                        "imagePrefix": "string",
                        "name": "string",
                        "securityContext": {
                           "allowPrivilegeEscalation": boolean,
                           "privileged": boolean
                        },
                        "volumeMounts": [
                           {
                              "mountPath": "string",
                              "name": "string"
                           }
                        ]
                     }
                  ],
                  "hostIPC": boolean,
                  "hostNetwork": boolean,
                  "hostPID": boolean,
                  "name": "string",
                  "namespace": "string",
                  "serviceAccountName": "string",
                  "type": "string",
                  "uid": "string",
                  "volumes": [
                     {
                        "hostPath": {
                           "path": "string"
                        },
                        "name": "string"
                     }
                  ]
               }
            },
            "lambdaDetails": {
               "description": "string",
               "functionArn": "string",
               "functionName": "string",
               "functionVersion": "string",
               "lastModifiedAt": number,
               "revisionId": "string",
               "role": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "vpcConfig": {
                  "securityGroups": [
                     {
                        "groupId": "string",
                        "groupName": "string"
                     }
                  ],
                  "subnetIds": [ "string" ],
                  "vpcId": "string"
               }
            },
            "modelDetails": [
               {
                  "modelId": "string"
               }
            ],
            "rdsDbInstanceDetails": {
               "dbClusterIdentifier": "string",
               "dbInstanceArn": "string",
               "dbInstanceIdentifier": "string",
               "dbiResourceId": "string",
               "engine": "string",
               "engineVersion": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ]
            },
            "rdsDbUserDetails": {
               "application": "string",
               "authMethod": "string",
               "database": "string",
               "ssl": "string",
               "user": "string"
            },
            "rdsLimitlessDbDetails": {
               "dbClusterIdentifier": "string",
               "dbShardGroupArn": "string",
               "dbShardGroupIdentifier": "string",
               "dbShardGroupResourceId": "string",
               "engine": "string",
               "engineVersion": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ]
            },
            "recoveryPointDetails": {
               "backupVaultName": "string",
               "continuousScanDetails": {
                  "endTime": number,
                  "startTime": number
               },
               "recoveryPointArn": "string"
            },
            "resourceType": "string",
            "s3BucketDetails": [
               {
                  "arn": "string",
                  "createdAt": number,
                  "defaultServerSideEncryption": {
                     "encryptionType": "string",
                     "kmsMasterKeyArn": "string"
                  },
                  "name": "string",
                  "owner": {
                     "id": "string"
                  },
                  "publicAccess": {
                     "effectivePermission": "string",
                     "permissionConfiguration": {
                        "accountLevelPermissions": {
                           "blockPublicAccess": {
                              "blockPublicAcls": boolean,
                              "blockPublicPolicy": boolean,
                              "ignorePublicAcls": boolean,
                              "restrictPublicBuckets": boolean
                           }
                        },
                        "bucketLevelPermissions": {
                           "accessControlList": {
                              "allowsPublicReadAccess": boolean,
                              "allowsPublicWriteAccess": boolean
                           },
                           "blockPublicAccess": {
                              "blockPublicAcls": boolean,
                              "blockPublicPolicy": boolean,
                              "ignorePublicAcls": boolean,
                              "restrictPublicBuckets": boolean
                           },
                           "bucketPolicy": {
                              "allowsPublicReadAccess": boolean,
                              "allowsPublicWriteAccess": boolean
                           }
                        }
                     }
                  },
                  "s3ObjectDetails": [
                     {
                        "eTag": "string",
                        "hash": "string",
                        "key": "string",
                        "objectArn": "string",
                        "versionId": "string"
                     }
                  ],
                  "tags": [
                     {
                        "key": "string",
                        "value": "string"
                     }
                  ],
                  "type": "string"
               }
            ]
         },
         "schemaVersion": "string",
         "service": {
            "action": {
               "actionType": "string",
               "awsApiCallAction": {
                  "affectedResources": {
                     "string" : "string"
                  },
                  "api": "string",
                  "callerType": "string",
                  "domainDetails": {
                     "domain": "string"
                  },
                  "errorCode": "string",
                  "remoteAccountDetails": {
                     "accountId": "string",
                     "affiliated": boolean
                  },
                  "remoteIpDetails": {
                     "city": {
                        "cityName": "string"
                     },
                     "country": {
                        "countryCode": "string",
                        "countryName": "string"
                     },
                     "geoLocation": {
                        "lat": number,
                        "lon": number
                     },
                     "ipAddressV4": "string",
                     "ipAddressV6": "string",
                     "organization": {
                        "asn": "string",
                        "asnOrg": "string",
                        "isp": "string",
                        "org": "string"
                     }
                  },
                  "serviceName": "string",
                  "userAgent": "string"
               },
               "dnsRequestAction": {
                  "blocked": boolean,
                  "domain": "string",
                  "domainWithSuffix": "string",
                  "protocol": "string",
                  "vpcOwnerAccountId": "string"
               },
               "kubernetesApiCallAction": {
                  "namespace": "string",
                  "parameters": "string",
                  "remoteIpDetails": {
                     "city": {
                        "cityName": "string"
                     },
                     "country": {
                        "countryCode": "string",
                        "countryName": "string"
                     },
                     "geoLocation": {
                        "lat": number,
                        "lon": number
                     },
                     "ipAddressV4": "string",
                     "ipAddressV6": "string",
                     "organization": {
                        "asn": "string",
                        "asnOrg": "string",
                        "isp": "string",
                        "org": "string"
                     }
                  },
                  "requestUri": "string",
                  "resource": "string",
                  "resourceName": "string",
                  "sourceIPs": [ "string" ],
                  "statusCode": number,
                  "subresource": "string",
                  "userAgent": "string",
                  "verb": "string"
               },
               "kubernetesPermissionCheckedDetails": {
                  "allowed": boolean,
                  "namespace": "string",
                  "resource": "string",
                  "verb": "string"
               },
               "kubernetesRoleBindingDetails": {
                  "kind": "string",
                  "name": "string",
                  "roleRefKind": "string",
                  "roleRefName": "string",
                  "uid": "string"
               },
               "kubernetesRoleDetails": {
                  "kind": "string",
                  "name": "string",
                  "uid": "string"
               },
               "networkConnectionAction": {
                  "blocked": boolean,
                  "connectionDirection": "string",
                  "localIpDetails": {
                     "ipAddressV4": "string",
                     "ipAddressV6": "string"
                  },
                  "localNetworkInterface": "string",
                  "localPortDetails": {
                     "port": number,
                     "portName": "string"
                  },
                  "protocol": "string",
                  "remoteIpDetails": {
                     "city": {
                        "cityName": "string"
                     },
                     "country": {
                        "countryCode": "string",
                        "countryName": "string"
                     },
                     "geoLocation": {
                        "lat": number,
                        "lon": number
                     },
                     "ipAddressV4": "string",
                     "ipAddressV6": "string",
                     "organization": {
                        "asn": "string",
                        "asnOrg": "string",
                        "isp": "string",
                        "org": "string"
                     }
                  },
                  "remotePortDetails": {
                     "port": number,
                     "portName": "string"
                  }
               },
               "portProbeAction": {
                  "blocked": boolean,
                  "portProbeDetails": [
                     {
                        "localIpDetails": {
                           "ipAddressV4": "string",
                           "ipAddressV6": "string"
                        },
                        "localPortDetails": {
                           "port": number,
                           "portName": "string"
                        },
                        "remoteIpDetails": {
                           "city": {
                              "cityName": "string"
                           },
                           "country": {
                              "countryCode": "string",
                              "countryName": "string"
                           },
                           "geoLocation": {
                              "lat": number,
                              "lon": number
                           },
                           "ipAddressV4": "string",
                           "ipAddressV6": "string",
                           "organization": {
                              "asn": "string",
                              "asnOrg": "string",
                              "isp": "string",
                              "org": "string"
                           }
                        }
                     }
                  ]
               },
               "rdsLoginAttemptAction": {
                  "LoginAttributes": [
                     {
                        "application": "string",
                        "failedLoginAttempts": number,
                        "successfulLoginAttempts": number,
                        "user": "string"
                     }
                  ],
                  "remoteIpDetails": {
                     "city": {
                        "cityName": "string"
                     },
                     "country": {
                        "countryCode": "string",
                        "countryName": "string"
                     },
                     "geoLocation": {
                        "lat": number,
                        "lon": number
                     },
                     "ipAddressV4": "string",
                     "ipAddressV6": "string",
                     "organization": {
                        "asn": "string",
                        "asnOrg": "string",
                        "isp": "string",
                        "org": "string"
                     }
                  }
               }
            },
            "additionalInfo": {
               "type": "string",
               "value": "string"
            },
            "archived": boolean,
            "count": number,
            "detection": {
               "anomaly": {
                  "profiles": {
                     "string" : {
                        "string" : [
                           {
                              "observations": {
                                 "number": [ number ],
                                 "text": [ "string" ]
                              },
                              "profileSubtype": "string",
                              "profileType": "string"
                           }
                        ]
                     }
                  },
                  "unusual": {
                     "behavior": {
                        "string" : {
                           "string" : {
                              "observations": {
                                 "number": [ number ],
                                 "text": [ "string" ]
                              },
                              "profileSubtype": "string",
                              "profileType": "string"
                           }
                        }
                     }
                  }
               },
               "sequence": {
                  "actors": [
                     {
                        "id": "string",
                        "process": {
                           "name": "string",
                           "path": "string",
                           "sha256": "string"
                        },
                        "session": {
                           "createdTime": number,
                           "issuer": "string",
                           "mfaStatus": "string",
                           "uid": "string"
                        },
                        "user": {
                           "account": {
                              "account": "string",
                              "uid": "string"
                           },
                           "credentialUid": "string",
                           "name": "string",
                           "type": "string",
                           "uid": "string"
                        }
                     }
                  ],
                  "additionalSequenceTypes": [ "string" ],
                  "description": "string",
                  "endpoints": [
                     {
                        "autonomousSystem": {
                           "name": "string",
                           "number": number
                        },
                        "connection": {
                           "direction": "string"
                        },
                        "domain": "string",
                        "id": "string",
                        "ip": "string",
                        "location": {
                           "city": "string",
                           "country": "string",
                           "lat": number,
                           "lon": number
                        },
                        "port": number
                     }
                  ],
                  "resources": [
                     {
                        "accountId": "string",
                        "cloudPartition": "string",
                        "data": {
                           "accessKey": {
                              "principalId": "string",
                              "userName": "string",
                              "userType": "string"
                           },
                           "autoscalingAutoScalingGroup": {
                              "ec2InstanceUids": [ "string" ]
                           },
                           "cloudformationStack": {
                              "ec2InstanceUids": [ "string" ]
                           },
                           "container": {
                              "image": "string",
                              "imageUid": "string"
                           },
                           "ec2Image": {
                              "ec2InstanceUids": [ "string" ]
                           },
                           "ec2Instance": {
                              "availabilityZone": "string",
                              "ec2NetworkInterfaceUids": [ "string" ],
                              "IamInstanceProfile": {
                                 "arn": "string",
                                 "id": "string"
                              },
                              "imageDescription": "string",
                              "instanceState": "string",
                              "instanceType": "string",
                              "outpostArn": "string",
                              "platform": "string",
                              "productCodes": [
                                 {
                                    "productCodeId": "string",
                                    "productCodeType": "string"
                                 }
                              ]
                           },
                           "ec2LaunchTemplate": {
                              "ec2InstanceUids": [ "string" ],
                              "version": "string"
                           },
                           "ec2NetworkInterface": {
                              "ipv6Addresses": [ "string" ],
                              "privateIpAddresses": [
                                 {
                                    "privateDnsName": "string",
                                    "privateIpAddress": "string"
                                 }
                              ],
                              "publicIp": "string",
                              "securityGroups": [
                                 {
                                    "groupId": "string",
                                    "groupName": "string"
                                 }
                              ],
                              "subNetId": "string",
                              "vpcId": "string"
                           },
                           "ec2Vpc": {
                              "ec2InstanceUids": [ "string" ]
                           },
                           "ecsCluster": {
                              "ec2InstanceUids": [ "string" ],
                              "status": "string"
                           },
                           "ecsTask": {
                              "containerUids": [ "string" ],
                              "createdAt": number,
                              "launchType": "string",
                              "taskDefinitionArn": "string"
                           },
                           "eksCluster": {
                              "arn": "string",
                              "createdAt": number,
                              "ec2InstanceUids": [ "string" ],
                              "status": "string",
                              "vpcId": "string"
                           },
                           "iamInstanceProfile": {
                              "ec2InstanceUids": [ "string" ]
                           },
                           "kubernetesWorkload": {
                              "containerUids": [ "string" ],
                              "type": "string",
                              "namespace": "string"
                           },
                           "s3Bucket": {
                              "accountPublicAccess": {
                                 "publicAclAccess": "string",
                                 "publicAclIgnoreBehavior": "string",
                                 "publicBucketRestrictBehavior": "string",
                                 "publicPolicyAccess": "string"
                              },
                              "bucketPublicAccess": {
                                 "publicAclAccess": "string",
                                 "publicAclIgnoreBehavior": "string",
                                 "publicBucketRestrictBehavior": "string",
                                 "publicPolicyAccess": "string"
                              },
                              "createdAt": number,
                              "effectivePermission": "string",
                              "encryptionKeyArn": "string",
                              "encryptionType": "string",
                              "ownerId": "string",
                              "publicReadAccess": "string",
                              "publicWriteAccess": "string",
                              "s3ObjectUids": [ "string" ]
                           },
                           "s3Object": {
                              "eTag": "string",
                              "key": "string",
                              "versionId": "string"
                           }
                        },
                        "name": "string",
                        "region": "string",
                        "resourceType": "string",
                        "service": "string",
                        "tags": [
                           {
                              "key": "string",
                              "value": "string"
                           }
                        ],
                        "uid": "string"
                     }
                  ],
                  "sequenceIndicators": [
                     {
                        "key": "string",
                        "title": "string",
                        "values": [ "string" ]
                     }
                  ],
                  "signals": [
                     {
                        "actorIds": [ "string" ],
                        "count": number,
                        "createdAt": number,
                        "description": "string",
                        "endpointIds": [ "string" ],
                        "firstSeenAt": number,
                        "lastSeenAt": number,
                        "name": "string",
                        "resourceUids": [ "string" ],
                        "severity": number,
                        "signalIndicators": [
                           {
                              "key": "string",
                              "title": "string",
                              "values": [ "string" ]
                           }
                        ],
                        "type": "string",
                        "uid": "string",
                        "updatedAt": number
                     }
                  ],
                  "uid": "string"
               }
            },
            "detectorId": "string",
            "ebsVolumeScanDetails": {
               "scanCompletedAt": number,
               "scanDetections": {
                  "highestSeverityThreatDetails": {
                     "count": number,
                     "severity": "string",
                     "threatName": "string"
                  },
                  "scannedItemCount": {
                     "files": number,
                     "totalGb": number,
                     "volumes": number
                  },
                  "threatDetectedByName": {
                     "itemCount": number,
                     "shortened": boolean,
                     "threatNames": [
                        {
                           "filePaths": [
                              {
                                 "fileName": "string",
                                 "filePath": "string",
                                 "hash": "string",
                                 "volumeArn": "string"
                              }
                           ],
                           "itemCount": number,
                           "name": "string",
                           "severity": "string"
                        }
                     ],
                     "uniqueThreatNameCount": number
                  },
                  "threatsDetectedItemCount": {
                     "files": number
                  }
               },
               "scanId": "string",
               "scanStartedAt": number,
               "scanType": "string",
               "sources": [ "string" ],
               "triggerFindingId": "string"
            },
            "eventFirstSeen": "string",
            "eventLastSeen": "string",
            "evidence": {
               "threatIntelligenceDetails": [
                  {
                     "threatFileSha256": "string",
                     "threatListName": "string",
                     "threatNames": [ "string" ]
                  }
               ]
            },
            "featureName": "string",
            "malwareScanDetails": {
               "scanCategory": "string",
               "scanConfiguration": {
                  "incrementalScanDetails": {
                     "baselineResourceArn": "string"
                  },
                  "triggerType": "string"
               },
               "scanId": "string",
               "scanType": "string",
               "threats": [
                  {
                     "count": number,
                     "hash": "string",
                     "itemDetails": [
                        {
                           "additionalInfo": {
                              "deviceName": "string",
                              "versionId": "string"
                           },
                           "hash": "string",
                           "itemPath": "string",
                           "resourceArn": "string"
                        }
                     ],
                     "itemPaths": [
                        {
                           "hash": "string",
                           "nestedItemPath": "string"
                        }
                     ],
                     "name": "string",
                     "source": "string"
                  }
               ],
               "uniqueThreatCount": number
            },
            "resourceRole": "string",
            "runtimeDetails": {
               "context": {
                  "addressFamily": "string",
                  "commandLineExample": "string",
                  "fileOperation": "string",
                  "filePath": "string",
                  "fileSystemType": "string",
                  "flags": [ "string" ],
                  "ianaProtocolNumber": number,
                  "ldPreloadValue": "string",
                  "libraryPath": "string",
                  "memoryRegions": [ "string" ],
                  "modifiedAt": number,
                  "modifyingProcess": {
                     "euid": number,
                     "executablePath": "string",
                     "executableSha256": "string",
                     "lineage": [
                        {
                           "euid": number,
                           "executablePath": "string",
                           "name": "string",
                           "namespacePid": number,
                           "parentUuid": "string",
                           "pid": number,
                           "startTime": number,
                           "userId": number,
                           "uuid": "string"
                        }
                     ],
                     "name": "string",
                     "namespacePid": number,
                     "parentUuid": "string",
                     "pid": number,
                     "pwd": "string",
                     "startTime": number,
                     "user": "string",
                     "userId": number,
                     "uuid": "string"
                  },
                  "moduleFilePath": "string",
                  "moduleName": "string",
                  "moduleSha256": "string",
                  "mountSource": "string",
                  "mountTarget": "string",
                  "relatedFilePaths": [ "string" ],
                  "releaseAgentPath": "string",
                  "runcBinaryPath": "string",
                  "scriptPath": "string",
                  "serviceName": "string",
                  "shellHistoryFilePath": "string",
                  "socketPath": "string",
                  "targetProcess": {
                     "euid": number,
                     "executablePath": "string",
                     "executableSha256": "string",
                     "lineage": [
                        {
                           "euid": number,
                           "executablePath": "string",
                           "name": "string",
                           "namespacePid": number,
                           "parentUuid": "string",
                           "pid": number,
                           "startTime": number,
                           "userId": number,
                           "uuid": "string"
                        }
                     ],
                     "name": "string",
                     "namespacePid": number,
                     "parentUuid": "string",
                     "pid": number,
                     "pwd": "string",
                     "startTime": number,
                     "user": "string",
                     "userId": number,
                     "uuid": "string"
                  },
                  "threatFilePath": "string",
                  "toolCategory": "string",
                  "toolName": "string"
               },
               "process": {
                  "euid": number,
                  "executablePath": "string",
                  "executableSha256": "string",
                  "lineage": [
                     {
                        "euid": number,
                        "executablePath": "string",
                        "name": "string",
                        "namespacePid": number,
                        "parentUuid": "string",
                        "pid": number,
                        "startTime": number,
                        "userId": number,
                        "uuid": "string"
                     }
                  ],
                  "name": "string",
                  "namespacePid": number,
                  "parentUuid": "string",
                  "pid": number,
                  "pwd": "string",
                  "startTime": number,
                  "user": "string",
                  "userId": number,
                  "uuid": "string"
               }
            },
            "serviceName": "string",
            "userFeedback": "string"
         },
         "severity": number,
         "title": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_GetFindings_ResponseSyntax) **   <a name="guardduty-GetFindings-response-findings"></a>
A list of findings.
Type: Array of [Finding](API_Finding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_GetFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_GetFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
