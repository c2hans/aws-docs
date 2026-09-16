---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindings.html
---

# GetFindings
<a name="API_GetFindings"></a>

Returns a list of findings that match the specified criteria.

If cross-Region aggregation is enabled, then when you call `GetFindings` from the home Region, the results include all of the matching findings from both the home Region and linked Regions.

## Request Syntax
<a name="API_GetFindings_RequestSyntax"></a>

```
POST /findings HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "AwsAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "AwsAccountName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "CompanyName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceAssociatedStandardsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlParametersName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlParametersValue": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Confidence": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "CreatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "Criticality": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "Description": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsConfidence": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "FindingProviderFieldsCriticality": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "FindingProviderFieldsRelatedFindingsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsRelatedFindingsProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsSeverityLabel": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsSeverityOriginal": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsTypes": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FirstObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "GeneratorId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Id": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Keyword": [
         {
            "Value": "{{string}}"
         }
      ],
      "LastObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "MalwareName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwarePath": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwareState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwareType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkDestinationDomain": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkDestinationIpV4": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkDestinationIpV6": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkDestinationPort": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "NetworkDirection": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkProtocol": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourceDomain": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourceIpV4": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkSourceIpV6": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkSourceMac": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourcePort": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "NoteText": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NoteUpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "NoteUpdatedBy": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ProcessName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessParentPid": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "ProcessPath": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessPid": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "ProcessTerminatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductFields": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RecommendationText": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RecordState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Region": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIamInstanceProfileArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceImageId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIpV4Addresses": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIpV6Addresses": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceKeyName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceSubnetId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceVpcId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyCreatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyPrincipalName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyUserName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamUserUserName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsS3BucketOwnerId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsS3BucketOwnerName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerImageId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerImageName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceContainerName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceDetailsOther": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerOrgId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourcePartition": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceProvider": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceRegion": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceTags": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Sample": [
         {
            "Value": {{boolean}}
         }
      ],
      "SeverityLabel": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SeverityNormalized": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "SeverityProduct": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "SourceUrl": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorCategory": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorLastObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorSource": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorSourceUrl": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorValue": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Title": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Type": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "UpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "UserDefinedFields": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VerificationState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VulnerabilitiesExploitAvailable": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VulnerabilitiesFixAvailable": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "WorkflowState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "WorkflowStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortCriteria": [
      {
         "Field": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetFindings_RequestSyntax) **   <a name="securityhub-GetFindings-request-Filters"></a>
The finding attributes used to define a condition to filter the returned findings.
You can filter by up to 10 finding attributes. For each attribute, you can provide up to 20 filter values.
Note that in the available filter fields, `WorkflowState` is deprecated. To search for a finding based on its workflow status, use `WorkflowStatus`.
Type: [AwsSecurityFindingFilters](API_AwsSecurityFindingFilters.md) object
Required: No

 ** [MaxResults](#API_GetFindings_RequestSyntax) **   <a name="securityhub-GetFindings-request-MaxResults"></a>
The maximum number of findings to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetFindings_RequestSyntax) **   <a name="securityhub-GetFindings-request-NextToken"></a>
The token that is required for pagination. On your first call to the `GetFindings` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.
Type: String
Required: No

 ** [SortCriteria](#API_GetFindings_RequestSyntax) **   <a name="securityhub-GetFindings-request-SortCriteria"></a>
The finding attributes used to sort the list of returned findings.
Type: Array of [SortCriterion](API_SortCriterion.md) objects
Required: No

## Response Syntax
<a name="API_GetFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Findings": [
      {
         "Action": {
            "ActionType": "string",
            "AwsApiCallAction": {
               "AffectedResources": {
                  "string" : "string"
               },
               "Api": "string",
               "CallerType": "string",
               "DomainDetails": {
                  "Domain": "string"
               },
               "FirstSeen": "string",
               "LastSeen": "string",
               "RemoteIpDetails": {
                  "City": {
                     "CityName": "string"
                  },
                  "Country": {
                     "CountryCode": "string",
                     "CountryName": "string"
                  },
                  "GeoLocation": {
                     "Lat": number,
                     "Lon": number
                  },
                  "IpAddressV4": "string",
                  "Organization": {
                     "Asn": number,
                     "AsnOrg": "string",
                     "Isp": "string",
                     "Org": "string"
                  }
               },
               "ServiceName": "string"
            },
            "DnsRequestAction": {
               "Blocked": boolean,
               "Domain": "string",
               "Protocol": "string"
            },
            "NetworkConnectionAction": {
               "Blocked": boolean,
               "ConnectionDirection": "string",
               "LocalPortDetails": {
                  "Port": number,
                  "PortName": "string"
               },
               "Protocol": "string",
               "RemoteIpDetails": {
                  "City": {
                     "CityName": "string"
                  },
                  "Country": {
                     "CountryCode": "string",
                     "CountryName": "string"
                  },
                  "GeoLocation": {
                     "Lat": number,
                     "Lon": number
                  },
                  "IpAddressV4": "string",
                  "Organization": {
                     "Asn": number,
                     "AsnOrg": "string",
                     "Isp": "string",
                     "Org": "string"
                  }
               },
               "RemotePortDetails": {
                  "Port": number,
                  "PortName": "string"
               }
            },
            "PortProbeAction": {
               "Blocked": boolean,
               "PortProbeDetails": [
                  {
                     "LocalIpDetails": {
                        "IpAddressV4": "string"
                     },
                     "LocalPortDetails": {
                        "Port": number,
                        "PortName": "string"
                     },
                     "RemoteIpDetails": {
                        "City": {
                           "CityName": "string"
                        },
                        "Country": {
                           "CountryCode": "string",
                           "CountryName": "string"
                        },
                        "GeoLocation": {
                           "Lat": number,
                           "Lon": number
                        },
                        "IpAddressV4": "string",
                        "Organization": {
                           "Asn": number,
                           "AsnOrg": "string",
                           "Isp": "string",
                           "Org": "string"
                        }
                     }
                  }
               ]
            }
         },
         "AwsAccountId": "string",
         "AwsAccountName": "string",
         "CompanyName": "string",
         "Compliance": {
            "AssociatedStandards": [
               {
                  "StandardsId": "string"
               }
            ],
            "RelatedRequirements": [ "string" ],
            "SecurityControlId": "string",
            "SecurityControlParameters": [
               {
                  "Name": "string",
                  "Value": [ "string" ]
               }
            ],
            "Status": "string",
            "StatusReasons": [
               {
                  "Description": "string",
                  "ReasonCode": "string"
               }
            ]
         },
         "Confidence": number,
         "CreatedAt": "string",
         "Criticality": number,
         "Description": "string",
         "Detection": {
            "Sequence": {
               "Actors": [
                  {
                     "Id": "string",
                     "Session": {
                        "CreatedTime": number,
                        "Issuer": "string",
                        "MfaStatus": "string",
                        "Uid": "string"
                     },
                     "User": {
                        "Account": {
                           "Name": "string",
                           "Uid": "string"
                        },
                        "CredentialUid": "string",
                        "Name": "string",
                        "Type": "string",
                        "Uid": "string"
                     }
                  }
               ],
               "Endpoints": [
                  {
                     "AutonomousSystem": {
                        "Name": "string",
                        "Number": number
                     },
                     "Connection": {
                        "Direction": "string"
                     },
                     "Domain": "string",
                     "Id": "string",
                     "Ip": "string",
                     "Location": {
                        "City": "string",
                        "Country": "string",
                        "Lat": number,
                        "Lon": number
                     },
                     "Port": number
                  }
               ],
               "SequenceIndicators": [
                  {
                     "Key": "string",
                     "Title": "string",
                     "Type": "string",
                     "Values": [ "string" ]
                  }
               ],
               "Signals": [
                  {
                     "ActorIds": [ "string" ],
                     "Count": number,
                     "CreatedAt": number,
                     "EndpointIds": [ "string" ],
                     "FirstSeenAt": number,
                     "Id": "string",
                     "LastSeenAt": number,
                     "Name": "string",
                     "ProductArn": "string",
                     "ResourceIds": [ "string" ],
                     "Severity": number,
                     "SignalIndicators": [
                        {
                           "Key": "string",
                           "Title": "string",
                           "Type": "string",
                           "Values": [ "string" ]
                        }
                     ],
                     "Title": "string",
                     "Type": "string",
                     "UpdatedAt": number
                  }
               ],
               "Uid": "string"
            }
         },
         "FindingProviderFields": {
            "Confidence": number,
            "Criticality": number,
            "RelatedFindings": [
               {
                  "Id": "string",
                  "ProductArn": "string"
               }
            ],
            "Severity": {
               "Label": "string",
               "Original": "string"
            },
            "Types": [ "string" ]
         },
         "FirstObservedAt": "string",
         "GeneratorDetails": {
            "Description": "string",
            "Labels": [ "string" ],
            "Name": "string"
         },
         "GeneratorId": "string",
         "Id": "string",
         "LastObservedAt": "string",
         "Malware": [
            {
               "Name": "string",
               "Path": "string",
               "State": "string",
               "Type": "string"
            }
         ],
         "Network": {
            "DestinationDomain": "string",
            "DestinationIpV4": "string",
            "DestinationIpV6": "string",
            "DestinationPort": number,
            "Direction": "string",
            "OpenPortRange": {
               "Begin": number,
               "End": number
            },
            "Protocol": "string",
            "SourceDomain": "string",
            "SourceIpV4": "string",
            "SourceIpV6": "string",
            "SourceMac": "string",
            "SourcePort": number
         },
         "NetworkPath": [
            {
               "ComponentId": "string",
               "ComponentType": "string",
               "Egress": {
                  "Destination": {
                     "Address": [ "string" ],
                     "PortRanges": [
                        {
                           "Begin": number,
                           "End": number
                        }
                     ]
                  },
                  "Protocol": "string",
                  "Source": {
                     "Address": [ "string" ],
                     "PortRanges": [
                        {
                           "Begin": number,
                           "End": number
                        }
                     ]
                  }
               },
               "Ingress": {
                  "Destination": {
                     "Address": [ "string" ],
                     "PortRanges": [
                        {
                           "Begin": number,
                           "End": number
                        }
                     ]
                  },
                  "Protocol": "string",
                  "Source": {
                     "Address": [ "string" ],
                     "PortRanges": [
                        {
                           "Begin": number,
                           "End": number
                        }
                     ]
                  }
               }
            }
         ],
         "Note": {
            "Text": "string",
            "UpdatedAt": "string",
            "UpdatedBy": "string"
         },
         "PatchSummary": {
            "FailedCount": number,
            "Id": "string",
            "InstalledCount": number,
            "InstalledOtherCount": number,
            "InstalledPendingReboot": number,
            "InstalledRejectedCount": number,
            "MissingCount": number,
            "Operation": "string",
            "OperationEndTime": "string",
            "OperationStartTime": "string",
            "RebootOption": "string"
         },
         "Process": {
            "LaunchedAt": "string",
            "Name": "string",
            "ParentPid": number,
            "Path": "string",
            "Pid": number,
            "TerminatedAt": "string"
         },
         "ProcessedAt": "string",
         "ProductArn": "string",
         "ProductFields": {
            "string" : "string"
         },
         "ProductName": "string",
         "RecordState": "string",
         "Region": "string",
         "RelatedFindings": [
            {
               "Id": "string",
               "ProductArn": "string"
            }
         ],
         "Remediation": {
            "Recommendation": {
               "Text": "string",
               "Url": "string"
            }
         },
         "Resources": [
            {
               "ApplicationArn": "string",
               "ApplicationName": "string",
               "DataClassification": {
                  "DetailedResultsLocation": "string",
                  "Result": {
                     "AdditionalOccurrences": boolean,
                     "CustomDataIdentifiers": {
                        "Detections": [
                           {
                              "Arn": "string",
                              "Count": number,
                              "Name": "string",
                              "Occurrences": {
                                 "Cells": [
                                    {
                                       "CellReference": "string",
                                       "Column": number,
                                       "ColumnName": "string",
                                       "Row": number
                                    }
                                 ],
                                 "LineRanges": [
                                    {
                                       "End": number,
                                       "Start": number,
                                       "StartColumn": number
                                    }
                                 ],
                                 "OffsetRanges": [
                                    {
                                       "End": number,
                                       "Start": number,
                                       "StartColumn": number
                                    }
                                 ],
                                 "Pages": [
                                    {
                                       "LineRange": {
                                          "End": number,
                                          "Start": number,
                                          "StartColumn": number
                                       },
                                       "OffsetRange": {
                                          "End": number,
                                          "Start": number,
                                          "StartColumn": number
                                       },
                                       "PageNumber": number
                                    }
                                 ],
                                 "Records": [
                                    {
                                       "JsonPath": "string",
                                       "RecordIndex": number
                                    }
                                 ]
                              }
                           }
                        ],
                        "TotalCount": number
                     },
                     "MimeType": "string",
                     "SensitiveData": [
                        {
                           "Category": "string",
                           "Detections": [
                              {
                                 "Count": number,
                                 "Occurrences": {
                                    "Cells": [
                                       {
                                          "CellReference": "string",
                                          "Column": number,
                                          "ColumnName": "string",
                                          "Row": number
                                       }
                                    ],
                                    "LineRanges": [
                                       {
                                          "End": number,
                                          "Start": number,
                                          "StartColumn": number
                                       }
                                    ],
                                    "OffsetRanges": [
                                       {
                                          "End": number,
                                          "Start": number,
                                          "StartColumn": number
                                       }
                                    ],
                                    "Pages": [
                                       {
                                          "LineRange": {
                                             "End": number,
                                             "Start": number,
                                             "StartColumn": number
                                          },
                                          "OffsetRange": {
                                             "End": number,
                                             "Start": number,
                                             "StartColumn": number
                                          },
                                          "PageNumber": number
                                       }
                                    ],
                                    "Records": [
                                       {
                                          "JsonPath": "string",
                                          "RecordIndex": number
                                       }
                                    ]
                                 },
                                 "Type": "string"
                              }
                           ],
                           "TotalCount": number
                        }
                     ],
                     "SizeClassified": number,
                     "Status": {
                        "Code": "string",
                        "Reason": "string"
                     }
                  }
               },
               "Details": {
                  "AwsAmazonMqBroker": {
                     "AuthenticationStrategy": "string",
                     "AutoMinorVersionUpgrade": boolean,
                     "BrokerArn": "string",
                     "BrokerId": "string",
                     "BrokerName": "string",
                     "DeploymentMode": "string",
                     "EncryptionOptions": {
                        "KmsKeyId": "string",
                        "UseAwsOwnedKey": boolean
                     },
                     "EngineType": "string",
                     "EngineVersion": "string",
                     "HostInstanceType": "string",
                     "LdapServerMetadata": {
                        "Hosts": [ "string" ],
                        "RoleBase": "string",
                        "RoleName": "string",
                        "RoleSearchMatching": "string",
                        "RoleSearchSubtree": boolean,
                        "ServiceAccountUsername": "string",
                        "UserBase": "string",
                        "UserRoleName": "string",
                        "UserSearchMatching": "string",
                        "UserSearchSubtree": boolean
                     },
                     "Logs": {
                        "Audit": boolean,
                        "AuditLogGroup": "string",
                        "General": boolean,
                        "GeneralLogGroup": "string",
                        "Pending": {
                           "Audit": boolean,
                           "General": boolean
                        }
                     },
                     "MaintenanceWindowStartTime": {
                        "DayOfWeek": "string",
                        "TimeOfDay": "string",
                        "TimeZone": "string"
                     },
                     "PubliclyAccessible": boolean,
                     "SecurityGroups": [ "string" ],
                     "StorageType": "string",
                     "SubnetIds": [ "string" ],
                     "Users": [
                        {
                           "PendingChange": "string",
                           "Username": "string"
                        }
                     ]
                  },
                  "AwsApiGatewayRestApi": {
                     "ApiKeySource": "string",
                     "BinaryMediaTypes": [ "string" ],
                     "CreatedDate": "string",
                     "Description": "string",
                     "EndpointConfiguration": {
                        "Types": [ "string" ]
                     },
                     "Id": "string",
                     "MinimumCompressionSize": number,
                     "Name": "string",
                     "Version": "string"
                  },
                  "AwsApiGatewayStage": {
                     "AccessLogSettings": {
                        "DestinationArn": "string",
                        "Format": "string"
                     },
                     "CacheClusterEnabled": boolean,
                     "CacheClusterSize": "string",
                     "CacheClusterStatus": "string",
                     "CanarySettings": {
                        "DeploymentId": "string",
                        "PercentTraffic": number,
                        "StageVariableOverrides": {
                           "string" : "string"
                        },
                        "UseStageCache": boolean
                     },
                     "ClientCertificateId": "string",
                     "CreatedDate": "string",
                     "DeploymentId": "string",
                     "Description": "string",
                     "DocumentationVersion": "string",
                     "LastUpdatedDate": "string",
                     "MethodSettings": [
                        {
                           "CacheDataEncrypted": boolean,
                           "CacheTtlInSeconds": number,
                           "CachingEnabled": boolean,
                           "DataTraceEnabled": boolean,
                           "HttpMethod": "string",
                           "LoggingLevel": "string",
                           "MetricsEnabled": boolean,
                           "RequireAuthorizationForCacheControl": boolean,
                           "ResourcePath": "string",
                           "ThrottlingBurstLimit": number,
                           "ThrottlingRateLimit": number,
                           "UnauthorizedCacheControlHeaderStrategy": "string"
                        }
                     ],
                     "StageName": "string",
                     "TracingEnabled": boolean,
                     "Variables": {
                        "string" : "string"
                     },
                     "WebAclArn": "string"
                  },
                  "AwsApiGatewayV2Api": {
                     "ApiEndpoint": "string",
                     "ApiId": "string",
                     "ApiKeySelectionExpression": "string",
                     "CorsConfiguration": {
                        "AllowCredentials": boolean,
                        "AllowHeaders": [ "string" ],
                        "AllowMethods": [ "string" ],
                        "AllowOrigins": [ "string" ],
                        "ExposeHeaders": [ "string" ],
                        "MaxAge": number
                     },
                     "CreatedDate": "string",
                     "Description": "string",
                     "Name": "string",
                     "ProtocolType": "string",
                     "RouteSelectionExpression": "string",
                     "Version": "string"
                  },
                  "AwsApiGatewayV2Stage": {
                     "AccessLogSettings": {
                        "DestinationArn": "string",
                        "Format": "string"
                     },
                     "ApiGatewayManaged": boolean,
                     "AutoDeploy": boolean,
                     "ClientCertificateId": "string",
                     "CreatedDate": "string",
                     "DefaultRouteSettings": {
                        "DataTraceEnabled": boolean,
                        "DetailedMetricsEnabled": boolean,
                        "LoggingLevel": "string",
                        "ThrottlingBurstLimit": number,
                        "ThrottlingRateLimit": number
                     },
                     "DeploymentId": "string",
                     "Description": "string",
                     "LastDeploymentStatusMessage": "string",
                     "LastUpdatedDate": "string",
                     "RouteSettings": {
                        "DataTraceEnabled": boolean,
                        "DetailedMetricsEnabled": boolean,
                        "LoggingLevel": "string",
                        "ThrottlingBurstLimit": number,
                        "ThrottlingRateLimit": number
                     },
                     "StageName": "string",
                     "StageVariables": {
                        "string" : "string"
                     }
                  },
                  "AwsAppSyncGraphQlApi": {
                     "AdditionalAuthenticationProviders": [
                        {
                           "AuthenticationType": "string",
                           "LambdaAuthorizerConfig": {
                              "AuthorizerResultTtlInSeconds": number,
                              "AuthorizerUri": "string",
                              "IdentityValidationExpression": "string"
                           },
                           "OpenIdConnectConfig": {
                              "AuthTtL": number,
                              "ClientId": "string",
                              "IatTtL": number,
                              "Issuer": "string"
                           },
                           "UserPoolConfig": {
                              "AppIdClientRegex": "string",
                              "AwsRegion": "string",
                              "DefaultAction": "string",
                              "UserPoolId": "string"
                           }
                        }
                     ],
                     "ApiId": "string",
                     "Arn": "string",
                     "AuthenticationType": "string",
                     "Id": "string",
                     "LambdaAuthorizerConfig": {
                        "AuthorizerResultTtlInSeconds": number,
                        "AuthorizerUri": "string",
                        "IdentityValidationExpression": "string"
                     },
                     "LogConfig": {
                        "CloudWatchLogsRoleArn": "string",
                        "ExcludeVerboseContent": boolean,
                        "FieldLogLevel": "string"
                     },
                     "Name": "string",
                     "OpenIdConnectConfig": {
                        "AuthTtL": number,
                        "ClientId": "string",
                        "IatTtL": number,
                        "Issuer": "string"
                     },
                     "UserPoolConfig": {
                        "AppIdClientRegex": "string",
                        "AwsRegion": "string",
                        "DefaultAction": "string",
                        "UserPoolId": "string"
                     },
                     "WafWebAclArn": "string",
                     "XrayEnabled": boolean
                  },
                  "AwsAthenaWorkGroup": {
                     "Configuration": {
                        "ResultConfiguration": {
                           "EncryptionConfiguration": {
                              "EncryptionOption": "string",
                              "KmsKey": "string"
                           }
                        }
                     },
                     "Description": "string",
                     "Name": "string",
                     "State": "string"
                  },
                  "AwsAutoScalingAutoScalingGroup": {
                     "AvailabilityZones": [
                        {
                           "Value": "string"
                        }
                     ],
                     "CapacityRebalance": boolean,
                     "CreatedTime": "string",
                     "HealthCheckGracePeriod": number,
                     "HealthCheckType": "string",
                     "LaunchConfigurationName": "string",
                     "LaunchTemplate": {
                        "LaunchTemplateId": "string",
                        "LaunchTemplateName": "string",
                        "Version": "string"
                     },
                     "LoadBalancerNames": [ "string" ],
                     "MixedInstancesPolicy": {
                        "InstancesDistribution": {
                           "OnDemandAllocationStrategy": "string",
                           "OnDemandBaseCapacity": number,
                           "OnDemandPercentageAboveBaseCapacity": number,
                           "SpotAllocationStrategy": "string",
                           "SpotInstancePools": number,
                           "SpotMaxPrice": "string"
                        },
                        "LaunchTemplate": {
                           "LaunchTemplateSpecification": {
                              "LaunchTemplateId": "string",
                              "LaunchTemplateName": "string",
                              "Version": "string"
                           },
                           "Overrides": [
                              {
                                 "InstanceType": "string",
                                 "WeightedCapacity": "string"
                              }
                           ]
                        }
                     }
                  },
                  "AwsAutoScalingLaunchConfiguration": {
                     "AssociatePublicIpAddress": boolean,
                     "BlockDeviceMappings": [
                        {
                           "DeviceName": "string",
                           "Ebs": {
                              "DeleteOnTermination": boolean,
                              "Encrypted": boolean,
                              "Iops": number,
                              "SnapshotId": "string",
                              "VolumeSize": number,
                              "VolumeType": "string"
                           },
                           "NoDevice": boolean,
                           "VirtualName": "string"
                        }
                     ],
                     "ClassicLinkVpcId": "string",
                     "ClassicLinkVpcSecurityGroups": [ "string" ],
                     "CreatedTime": "string",
                     "EbsOptimized": boolean,
                     "IamInstanceProfile": "string",
                     "ImageId": "string",
                     "InstanceMonitoring": {
                        "Enabled": boolean
                     },
                     "InstanceType": "string",
                     "KernelId": "string",
                     "KeyName": "string",
                     "LaunchConfigurationName": "string",
                     "MetadataOptions": {
                        "HttpEndpoint": "string",
                        "HttpPutResponseHopLimit": number,
                        "HttpTokens": "string"
                     },
                     "PlacementTenancy": "string",
                     "RamdiskId": "string",
                     "SecurityGroups": [ "string" ],
                     "SpotPrice": "string",
                     "UserData": "string"
                  },
                  "AwsBackupBackupPlan": {
                     "BackupPlan": {
                        "AdvancedBackupSettings": [
                           {
                              "BackupOptions": {
                                 "string" : "string"
                              },
                              "ResourceType": "string"
                           }
                        ],
                        "BackupPlanName": "string",
                        "BackupPlanRule": [
                           {
                              "CompletionWindowMinutes": number,
                              "CopyActions": [
                                 {
                                    "DestinationBackupVaultArn": "string",
                                    "Lifecycle": {
                                       "DeleteAfterDays": number,
                                       "MoveToColdStorageAfterDays": number
                                    }
                                 }
                              ],
                              "EnableContinuousBackup": boolean,
                              "Lifecycle": {
                                 "DeleteAfterDays": number,
                                 "MoveToColdStorageAfterDays": number
                              },
                              "RuleId": "string",
                              "RuleName": "string",
                              "ScheduleExpression": "string",
                              "StartWindowMinutes": number,
                              "TargetBackupVault": "string"
                           }
                        ]
                     },
                     "BackupPlanArn": "string",
                     "BackupPlanId": "string",
                     "VersionId": "string"
                  },
                  "AwsBackupBackupVault": {
                     "AccessPolicy": "string",
                     "BackupVaultArn": "string",
                     "BackupVaultName": "string",
                     "EncryptionKeyArn": "string",
                     "Notifications": {
                        "BackupVaultEvents": [ "string" ],
                        "SnsTopicArn": "string"
                     }
                  },
                  "AwsBackupRecoveryPoint": {
                     "BackupSizeInBytes": number,
                     "BackupVaultArn": "string",
                     "BackupVaultName": "string",
                     "CalculatedLifecycle": {
                        "DeleteAt": "string",
                        "MoveToColdStorageAt": "string"
                     },
                     "CompletionDate": "string",
                     "CreatedBy": {
                        "BackupPlanArn": "string",
                        "BackupPlanId": "string",
                        "BackupPlanVersion": "string",
                        "BackupRuleId": "string"
                     },
                     "CreationDate": "string",
                     "EncryptionKeyArn": "string",
                     "IamRoleArn": "string",
                     "IsEncrypted": boolean,
                     "LastRestoreTime": "string",
                     "Lifecycle": {
                        "DeleteAfterDays": number,
                        "MoveToColdStorageAfterDays": number
                     },
                     "RecoveryPointArn": "string",
                     "ResourceArn": "string",
                     "ResourceType": "string",
                     "SourceBackupVaultArn": "string",
                     "Status": "string",
                     "StatusMessage": "string",
                     "StorageClass": "string"
                  },
                  "AwsCertificateManagerCertificate": {
                     "CertificateAuthorityArn": "string",
                     "CreatedAt": "string",
                     "DomainName": "string",
                     "DomainValidationOptions": [
                        {
                           "DomainName": "string",
                           "ResourceRecord": {
                              "Name": "string",
                              "Type": "string",
                              "Value": "string"
                           },
                           "ValidationDomain": "string",
                           "ValidationEmails": [ "string" ],
                           "ValidationMethod": "string",
                           "ValidationStatus": "string"
                        }
                     ],
                     "ExtendedKeyUsages": [
                        {
                           "Name": "string",
                           "OId": "string"
                        }
                     ],
                     "FailureReason": "string",
                     "ImportedAt": "string",
                     "InUseBy": [ "string" ],
                     "IssuedAt": "string",
                     "Issuer": "string",
                     "KeyAlgorithm": "string",
                     "KeyUsages": [
                        {
                           "Name": "string"
                        }
                     ],
                     "NotAfter": "string",
                     "NotBefore": "string",
                     "Options": {
                        "CertificateTransparencyLoggingPreference": "string"
                     },
                     "RenewalEligibility": "string",
                     "RenewalSummary": {
                        "DomainValidationOptions": [
                           {
                              "DomainName": "string",
                              "ResourceRecord": {
                                 "Name": "string",
                                 "Type": "string",
                                 "Value": "string"
                              },
                              "ValidationDomain": "string",
                              "ValidationEmails": [ "string" ],
                              "ValidationMethod": "string",
                              "ValidationStatus": "string"
                           }
                        ],
                        "RenewalStatus": "string",
                        "RenewalStatusReason": "string",
                        "UpdatedAt": "string"
                     },
                     "Serial": "string",
                     "SignatureAlgorithm": "string",
                     "Status": "string",
                     "Subject": "string",
                     "SubjectAlternativeNames": [ "string" ],
                     "Type": "string"
                  },
                  "AwsCloudFormationStack": {
                     "Capabilities": [ "string" ],
                     "CreationTime": "string",
                     "Description": "string",
                     "DisableRollback": boolean,
                     "DriftInformation": {
                        "StackDriftStatus": "string"
                     },
                     "EnableTerminationProtection": boolean,
                     "LastUpdatedTime": "string",
                     "NotificationArns": [ "string" ],
                     "Outputs": [
                        {
                           "Description": "string",
                           "OutputKey": "string",
                           "OutputValue": "string"
                        }
                     ],
                     "RoleArn": "string",
                     "StackId": "string",
                     "StackName": "string",
                     "StackStatus": "string",
                     "StackStatusReason": "string",
                     "TimeoutInMinutes": number
                  },
                  "AwsCloudFrontDistribution": {
                     "CacheBehaviors": {
                        "Items": [
                           {
                              "ViewerProtocolPolicy": "string"
                           }
                        ]
                     },
                     "DefaultCacheBehavior": {
                        "ViewerProtocolPolicy": "string"
                     },
                     "DefaultRootObject": "string",
                     "DomainName": "string",
                     "ETag": "string",
                     "LastModifiedTime": "string",
                     "Logging": {
                        "Bucket": "string",
                        "Enabled": boolean,
                        "IncludeCookies": boolean,
                        "Prefix": "string"
                     },
                     "OriginGroups": {
                        "Items": [
                           {
                              "FailoverCriteria": {
                                 "StatusCodes": {
                                    "Items": [ number ],
                                    "Quantity": number
                                 }
                              }
                           }
                        ]
                     },
                     "Origins": {
                        "Items": [
                           {
                              "CustomOriginConfig": {
                                 "HttpPort": number,
                                 "HttpsPort": number,
                                 "OriginKeepaliveTimeout": number,
                                 "OriginProtocolPolicy": "string",
                                 "OriginReadTimeout": number,
                                 "OriginSslProtocols": {
                                    "Items": [ "string" ],
                                    "Quantity": number
                                 }
                              },
                              "DomainName": "string",
                              "Id": "string",
                              "OriginPath": "string",
                              "S3OriginConfig": {
                                 "OriginAccessIdentity": "string"
                              }
                           }
                        ]
                     },
                     "Status": "string",
                     "ViewerCertificate": {
                        "AcmCertificateArn": "string",
                        "Certificate": "string",
                        "CertificateSource": "string",
                        "CloudFrontDefaultCertificate": boolean,
                        "IamCertificateId": "string",
                        "MinimumProtocolVersion": "string",
                        "SslSupportMethod": "string"
                     },
                     "WebAclId": "string"
                  },
                  "AwsCloudTrailTrail": {
                     "CloudWatchLogsLogGroupArn": "string",
                     "CloudWatchLogsRoleArn": "string",
                     "HasCustomEventSelectors": boolean,
                     "HomeRegion": "string",
                     "IncludeGlobalServiceEvents": boolean,
                     "IsMultiRegionTrail": boolean,
                     "IsOrganizationTrail": boolean,
                     "KmsKeyId": "string",
                     "LogFileValidationEnabled": boolean,
                     "Name": "string",
                     "S3BucketName": "string",
                     "S3KeyPrefix": "string",
                     "SnsTopicArn": "string",
                     "SnsTopicName": "string",
                     "TrailArn": "string"
                  },
                  "AwsCloudWatchAlarm": {
                     "ActionsEnabled": boolean,
                     "AlarmActions": [ "string" ],
                     "AlarmArn": "string",
                     "AlarmConfigurationUpdatedTimestamp": "string",
                     "AlarmDescription": "string",
                     "AlarmName": "string",
                     "ComparisonOperator": "string",
                     "DatapointsToAlarm": number,
                     "Dimensions": [
                        {
                           "Name": "string",
                           "Value": "string"
                        }
                     ],
                     "EvaluateLowSampleCountPercentile": "string",
                     "EvaluationPeriods": number,
                     "ExtendedStatistic": "string",
                     "InsufficientDataActions": [ "string" ],
                     "MetricName": "string",
                     "Namespace": "string",
                     "OkActions": [ "string" ],
                     "Period": number,
                     "Statistic": "string",
                     "Threshold": number,
                     "ThresholdMetricId": "string",
                     "TreatMissingData": "string",
                     "Unit": "string"
                  },
                  "AwsCodeBuildProject": {
                     "Artifacts": [
                        {
                           "ArtifactIdentifier": "string",
                           "EncryptionDisabled": boolean,
                           "Location": "string",
                           "Name": "string",
                           "NamespaceType": "string",
                           "OverrideArtifactName": boolean,
                           "Packaging": "string",
                           "Path": "string",
                           "Type": "string"
                        }
                     ],
                     "EncryptionKey": "string",
                     "Environment": {
                        "Certificate": "string",
                        "EnvironmentVariables": [
                           {
                              "Name": "string",
                              "Type": "string",
                              "Value": "string"
                           }
                        ],
                        "ImagePullCredentialsType": "string",
                        "PrivilegedMode": boolean,
                        "RegistryCredential": {
                           "Credential": "string",
                           "CredentialProvider": "string"
                        },
                        "Type": "string"
                     },
                     "LogsConfig": {
                        "CloudWatchLogs": {
                           "GroupName": "string",
                           "Status": "string",
                           "StreamName": "string"
                        },
                        "S3Logs": {
                           "EncryptionDisabled": boolean,
                           "Location": "string",
                           "Status": "string"
                        }
                     },
                     "Name": "string",
                     "SecondaryArtifacts": [
                        {
                           "ArtifactIdentifier": "string",
                           "EncryptionDisabled": boolean,
                           "Location": "string",
                           "Name": "string",
                           "NamespaceType": "string",
                           "OverrideArtifactName": boolean,
                           "Packaging": "string",
                           "Path": "string",
                           "Type": "string"
                        }
                     ],
                     "ServiceRole": "string",
                     "Source": {
                        "GitCloneDepth": number,
                        "InsecureSsl": boolean,
                        "Location": "string",
                        "Type": "string"
                     },
                     "VpcConfig": {
                        "SecurityGroupIds": [ "string" ],
                        "Subnets": [ "string" ],
                        "VpcId": "string"
                     }
                  },
                  "AwsDmsEndpoint": {
                     "CertificateArn": "string",
                     "DatabaseName": "string",
                     "EndpointArn": "string",
                     "EndpointIdentifier": "string",
                     "EndpointType": "string",
                     "EngineName": "string",
                     "ExternalId": "string",
                     "ExtraConnectionAttributes": "string",
                     "KmsKeyId": "string",
                     "Port": number,
                     "ServerName": "string",
                     "SslMode": "string",
                     "Username": "string"
                  },
                  "AwsDmsReplicationInstance": {
                     "AllocatedStorage": number,
                     "AutoMinorVersionUpgrade": boolean,
                     "AvailabilityZone": "string",
                     "EngineVersion": "string",
                     "KmsKeyId": "string",
                     "MultiAZ": boolean,
                     "PreferredMaintenanceWindow": "string",
                     "PubliclyAccessible": boolean,
                     "ReplicationInstanceClass": "string",
                     "ReplicationInstanceIdentifier": "string",
                     "ReplicationSubnetGroup": {
                        "ReplicationSubnetGroupIdentifier": "string"
                     },
                     "VpcSecurityGroups": [
                        {
                           "VpcSecurityGroupId": "string"
                        }
                     ]
                  },
                  "AwsDmsReplicationTask": {
                     "CdcStartPosition": "string",
                     "CdcStartTime": "string",
                     "CdcStopPosition": "string",
                     "Id": "string",
                     "MigrationType": "string",
                     "ReplicationInstanceArn": "string",
                     "ReplicationTaskIdentifier": "string",
                     "ReplicationTaskSettings": "string",
                     "ResourceIdentifier": "string",
                     "SourceEndpointArn": "string",
                     "TableMappings": "string",
                     "TargetEndpointArn": "string",
                     "TaskData": "string"
                  },
                  "AwsDynamoDbTable": {
                     "AttributeDefinitions": [
                        {
                           "AttributeName": "string",
                           "AttributeType": "string"
                        }
                     ],
                     "BillingModeSummary": {
                        "BillingMode": "string",
                        "LastUpdateToPayPerRequestDateTime": "string"
                     },
                     "CreationDateTime": "string",
                     "DeletionProtectionEnabled": boolean,
                     "GlobalSecondaryIndexes": [
                        {
                           "Backfilling": boolean,
                           "IndexArn": "string",
                           "IndexName": "string",
                           "IndexSizeBytes": number,
                           "IndexStatus": "string",
                           "ItemCount": number,
                           "KeySchema": [
                              {
                                 "AttributeName": "string",
                                 "KeyType": "string"
                              }
                           ],
                           "Projection": {
                              "NonKeyAttributes": [ "string" ],
                              "ProjectionType": "string"
                           },
                           "ProvisionedThroughput": {
                              "LastDecreaseDateTime": "string",
                              "LastIncreaseDateTime": "string",
                              "NumberOfDecreasesToday": number,
                              "ReadCapacityUnits": number,
                              "WriteCapacityUnits": number
                           }
                        }
                     ],
                     "GlobalTableVersion": "string",
                     "ItemCount": number,
                     "KeySchema": [
                        {
                           "AttributeName": "string",
                           "KeyType": "string"
                        }
                     ],
                     "LatestStreamArn": "string",
                     "LatestStreamLabel": "string",
                     "LocalSecondaryIndexes": [
                        {
                           "IndexArn": "string",
                           "IndexName": "string",
                           "KeySchema": [
                              {
                                 "AttributeName": "string",
                                 "KeyType": "string"
                              }
                           ],
                           "Projection": {
                              "NonKeyAttributes": [ "string" ],
                              "ProjectionType": "string"
                           }
                        }
                     ],
                     "ProvisionedThroughput": {
                        "LastDecreaseDateTime": "string",
                        "LastIncreaseDateTime": "string",
                        "NumberOfDecreasesToday": number,
                        "ReadCapacityUnits": number,
                        "WriteCapacityUnits": number
                     },
                     "Replicas": [
                        {
                           "GlobalSecondaryIndexes": [
                              {
                                 "IndexName": "string",
                                 "ProvisionedThroughputOverride": {
                                    "ReadCapacityUnits": number
                                 }
                              }
                           ],
                           "KmsMasterKeyId": "string",
                           "ProvisionedThroughputOverride": {
                              "ReadCapacityUnits": number
                           },
                           "RegionName": "string",
                           "ReplicaStatus": "string",
                           "ReplicaStatusDescription": "string"
                        }
                     ],
                     "RestoreSummary": {
                        "RestoreDateTime": "string",
                        "RestoreInProgress": boolean,
                        "SourceBackupArn": "string",
                        "SourceTableArn": "string"
                     },
                     "SseDescription": {
                        "InaccessibleEncryptionDateTime": "string",
                        "KmsMasterKeyArn": "string",
                        "SseType": "string",
                        "Status": "string"
                     },
                     "StreamSpecification": {
                        "StreamEnabled": boolean,
                        "StreamViewType": "string"
                     },
                     "TableId": "string",
                     "TableName": "string",
                     "TableSizeBytes": number,
                     "TableStatus": "string"
                  },
                  "AwsEc2ClientVpnEndpoint": {
                     "AuthenticationOptions": [
                        {
                           "ActiveDirectory": {
                              "DirectoryId": "string"
                           },
                           "FederatedAuthentication": {
                              "SamlProviderArn": "string",
                              "SelfServiceSamlProviderArn": "string"
                           },
                           "MutualAuthentication": {
                              "ClientRootCertificateChain": "string"
                           },
                           "Type": "string"
                        }
                     ],
                     "ClientCidrBlock": "string",
                     "ClientConnectOptions": {
                        "Enabled": boolean,
                        "LambdaFunctionArn": "string",
                        "Status": {
                           "Code": "string",
                           "Message": "string"
                        }
                     },
                     "ClientLoginBannerOptions": {
                        "BannerText": "string",
                        "Enabled": boolean
                     },
                     "ClientVpnEndpointId": "string",
                     "ConnectionLogOptions": {
                        "CloudwatchLogGroup": "string",
                        "CloudwatchLogStream": "string",
                        "Enabled": boolean
                     },
                     "Description": "string",
                     "DnsServer": [ "string" ],
                     "SecurityGroupIdSet": [ "string" ],
                     "SelfServicePortalUrl": "string",
                     "ServerCertificateArn": "string",
                     "SessionTimeoutHours": number,
                     "SplitTunnel": boolean,
                     "TransportProtocol": "string",
                     "VpcId": "string",
                     "VpnPort": number
                  },
                  "AwsEc2Eip": {
                     "AllocationId": "string",
                     "AssociationId": "string",
                     "Domain": "string",
                     "InstanceId": "string",
                     "NetworkBorderGroup": "string",
                     "NetworkInterfaceId": "string",
                     "NetworkInterfaceOwnerId": "string",
                     "PrivateIpAddress": "string",
                     "PublicIp": "string",
                     "PublicIpv4Pool": "string"
                  },
                  "AwsEc2Instance": {
                     "IamInstanceProfileArn": "string",
                     "ImageId": "string",
                     "IpV4Addresses": [ "string" ],
                     "IpV6Addresses": [ "string" ],
                     "KeyName": "string",
                     "LaunchedAt": "string",
                     "MetadataOptions": {
                        "HttpEndpoint": "string",
                        "HttpProtocolIpv6": "string",
                        "HttpPutResponseHopLimit": number,
                        "HttpTokens": "string",
                        "InstanceMetadataTags": "string"
                     },
                     "Monitoring": {
                        "State": "string"
                     },
                     "NetworkInterfaces": [
                        {
                           "NetworkInterfaceId": "string"
                        }
                     ],
                     "SubnetId": "string",
                     "Type": "string",
                     "VirtualizationType": "string",
                     "VpcId": "string"
                  },
                  "AwsEc2LaunchTemplate": {
                     "DefaultVersionNumber": number,
                     "Id": "string",
                     "LatestVersionNumber": number,
                     "LaunchTemplateData": {
                        "BlockDeviceMappingSet": [
                           {
                              "DeviceName": "string",
                              "Ebs": {
                                 "DeleteOnTermination": boolean,
                                 "Encrypted": boolean,
                                 "Iops": number,
                                 "KmsKeyId": "string",
                                 "SnapshotId": "string",
                                 "Throughput": number,
                                 "VolumeSize": number,
                                 "VolumeType": "string"
                              },
                              "NoDevice": "string",
                              "VirtualName": "string"
                           }
                        ],
                        "CapacityReservationSpecification": {
                           "CapacityReservationPreference": "string",
                           "CapacityReservationTarget": {
                              "CapacityReservationId": "string",
                              "CapacityReservationResourceGroupArn": "string"
                           }
                        },
                        "CpuOptions": {
                           "CoreCount": number,
                           "ThreadsPerCore": number
                        },
                        "CreditSpecification": {
                           "CpuCredits": "string"
                        },
                        "DisableApiStop": boolean,
                        "DisableApiTermination": boolean,
                        "EbsOptimized": boolean,
                        "ElasticGpuSpecificationSet": [
                           {
                              "Type": "string"
                           }
                        ],
                        "ElasticInferenceAcceleratorSet": [
                           {
                              "Count": number,
                              "Type": "string"
                           }
                        ],
                        "EnclaveOptions": {
                           "Enabled": boolean
                        },
                        "HibernationOptions": {
                           "Configured": boolean
                        },
                        "IamInstanceProfile": {
                           "Arn": "string",
                           "Name": "string"
                        },
                        "ImageId": "string",
                        "InstanceInitiatedShutdownBehavior": "string",
                        "InstanceMarketOptions": {
                           "MarketType": "string",
                           "SpotOptions": {
                              "BlockDurationMinutes": number,
                              "InstanceInterruptionBehavior": "string",
                              "MaxPrice": "string",
                              "SpotInstanceType": "string",
                              "ValidUntil": "string"
                           }
                        },
                        "InstanceRequirements": {
                           "AcceleratorCount": {
                              "Max": number,
                              "Min": number
                           },
                           "AcceleratorManufacturers": [ "string" ],
                           "AcceleratorNames": [ "string" ],
                           "AcceleratorTotalMemoryMiB": {
                              "Max": number,
                              "Min": number
                           },
                           "AcceleratorTypes": [ "string" ],
                           "BareMetal": "string",
                           "BaselineEbsBandwidthMbps": {
                              "Max": number,
                              "Min": number
                           },
                           "BurstablePerformance": "string",
                           "CpuManufacturers": [ "string" ],
                           "ExcludedInstanceTypes": [ "string" ],
                           "InstanceGenerations": [ "string" ],
                           "LocalStorage": "string",
                           "LocalStorageTypes": [ "string" ],
                           "MemoryGiBPerVCpu": {
                              "Max": number,
                              "Min": number
                           },
                           "MemoryMiB": {
                              "Max": number,
                              "Min": number
                           },
                           "NetworkInterfaceCount": {
                              "Max": number,
                              "Min": number
                           },
                           "OnDemandMaxPricePercentageOverLowestPrice": number,
                           "RequireHibernateSupport": boolean,
                           "SpotMaxPricePercentageOverLowestPrice": number,
                           "TotalLocalStorageGB": {
                              "Max": number,
                              "Min": number
                           },
                           "VCpuCount": {
                              "Max": number,
                              "Min": number
                           }
                        },
                        "InstanceType": "string",
                        "KernelId": "string",
                        "KeyName": "string",
                        "LicenseSet": [
                           {
                              "LicenseConfigurationArn": "string"
                           }
                        ],
                        "MaintenanceOptions": {
                           "AutoRecovery": "string"
                        },
                        "MetadataOptions": {
                           "HttpEndpoint": "string",
                           "HttpProtocolIpv6": "string",
                           "HttpPutResponseHopLimit": number,
                           "HttpTokens": "string",
                           "InstanceMetadataTags": "string"
                        },
                        "Monitoring": {
                           "Enabled": boolean
                        },
                        "NetworkInterfaceSet": [
                           {
                              "AssociateCarrierIpAddress": boolean,
                              "AssociatePublicIpAddress": boolean,
                              "DeleteOnTermination": boolean,
                              "Description": "string",
                              "DeviceIndex": number,
                              "Groups": [ "string" ],
                              "InterfaceType": "string",
                              "Ipv4PrefixCount": number,
                              "Ipv4Prefixes": [
                                 {
                                    "Ipv4Prefix": "string"
                                 }
                              ],
                              "Ipv6AddressCount": number,
                              "Ipv6Addresses": [
                                 {
                                    "Ipv6Address": "string"
                                 }
                              ],
                              "Ipv6PrefixCount": number,
                              "Ipv6Prefixes": [
                                 {
                                    "Ipv6Prefix": "string"
                                 }
                              ],
                              "NetworkCardIndex": number,
                              "NetworkInterfaceId": "string",
                              "PrivateIpAddress": "string",
                              "PrivateIpAddresses": [
                                 {
                                    "Primary": boolean,
                                    "PrivateIpAddress": "string"
                                 }
                              ],
                              "SecondaryPrivateIpAddressCount": number,
                              "SubnetId": "string"
                           }
                        ],
                        "Placement": {
                           "Affinity": "string",
                           "AvailabilityZone": "string",
                           "GroupName": "string",
                           "HostId": "string",
                           "HostResourceGroupArn": "string",
                           "PartitionNumber": number,
                           "SpreadDomain": "string",
                           "Tenancy": "string"
                        },
                        "PrivateDnsNameOptions": {
                           "EnableResourceNameDnsAAAARecord": boolean,
                           "EnableResourceNameDnsARecord": boolean,
                           "HostnameType": "string"
                        },
                        "RamDiskId": "string",
                        "SecurityGroupIdSet": [ "string" ],
                        "SecurityGroupSet": [ "string" ],
                        "UserData": "string"
                     },
                     "LaunchTemplateName": "string"
                  },
                  "AwsEc2NetworkAcl": {
                     "Associations": [
                        {
                           "NetworkAclAssociationId": "string",
                           "NetworkAclId": "string",
                           "SubnetId": "string"
                        }
                     ],
                     "Entries": [
                        {
                           "CidrBlock": "string",
                           "Egress": boolean,
                           "IcmpTypeCode": {
                              "Code": number,
                              "Type": number
                           },
                           "Ipv6CidrBlock": "string",
                           "PortRange": {
                              "From": number,
                              "To": number
                           },
                           "Protocol": "string",
                           "RuleAction": "string",
                           "RuleNumber": number
                        }
                     ],
                     "IsDefault": boolean,
                     "NetworkAclId": "string",
                     "OwnerId": "string",
                     "VpcId": "string"
                  },
                  "AwsEc2NetworkInterface": {
                     "Attachment": {
                        "AttachmentId": "string",
                        "AttachTime": "string",
                        "DeleteOnTermination": boolean,
                        "DeviceIndex": number,
                        "InstanceId": "string",
                        "InstanceOwnerId": "string",
                        "Status": "string"
                     },
                     "IpV6Addresses": [
                        {
                           "IpV6Address": "string"
                        }
                     ],
                     "NetworkInterfaceId": "string",
                     "PrivateIpAddresses": [
                        {
                           "PrivateDnsName": "string",
                           "PrivateIpAddress": "string"
                        }
                     ],
                     "PublicDnsName": "string",
                     "PublicIp": "string",
                     "SecurityGroups": [
                        {
                           "GroupId": "string",
                           "GroupName": "string"
                        }
                     ],
                     "SourceDestCheck": boolean
                  },
                  "AwsEc2RouteTable": {
                     "AssociationSet": [
                        {
                           "AssociationState": {
                              "State": "string",
                              "StatusMessage": "string"
                           },
                           "GatewayId": "string",
                           "Main": boolean,
                           "RouteTableAssociationId": "string",
                           "RouteTableId": "string",
                           "SubnetId": "string"
                        }
                     ],
                     "OwnerId": "string",
                     "PropagatingVgwSet": [
                        {
                           "GatewayId": "string"
                        }
                     ],
                     "RouteSet": [
                        {
                           "CarrierGatewayId": "string",
                           "CoreNetworkArn": "string",
                           "DestinationCidrBlock": "string",
                           "DestinationIpv6CidrBlock": "string",
                           "DestinationPrefixListId": "string",
                           "EgressOnlyInternetGatewayId": "string",
                           "GatewayId": "string",
                           "InstanceId": "string",
                           "InstanceOwnerId": "string",
                           "LocalGatewayId": "string",
                           "NatGatewayId": "string",
                           "NetworkInterfaceId": "string",
                           "Origin": "string",
                           "State": "string",
                           "TransitGatewayId": "string",
                           "VpcPeeringConnectionId": "string"
                        }
                     ],
                     "RouteTableId": "string",
                     "VpcId": "string"
                  },
                  "AwsEc2SecurityGroup": {
                     "GroupId": "string",
                     "GroupName": "string",
                     "IpPermissions": [
                        {
                           "FromPort": number,
                           "IpProtocol": "string",
                           "IpRanges": [
                              {
                                 "CidrIp": "string"
                              }
                           ],
                           "Ipv6Ranges": [
                              {
                                 "CidrIpv6": "string"
                              }
                           ],
                           "PrefixListIds": [
                              {
                                 "PrefixListId": "string"
                              }
                           ],
                           "ToPort": number,
                           "UserIdGroupPairs": [
                              {
                                 "GroupId": "string",
                                 "GroupName": "string",
                                 "PeeringStatus": "string",
                                 "UserId": "string",
                                 "VpcId": "string",
                                 "VpcPeeringConnectionId": "string"
                              }
                           ]
                        }
                     ],
                     "IpPermissionsEgress": [
                        {
                           "FromPort": number,
                           "IpProtocol": "string",
                           "IpRanges": [
                              {
                                 "CidrIp": "string"
                              }
                           ],
                           "Ipv6Ranges": [
                              {
                                 "CidrIpv6": "string"
                              }
                           ],
                           "PrefixListIds": [
                              {
                                 "PrefixListId": "string"
                              }
                           ],
                           "ToPort": number,
                           "UserIdGroupPairs": [
                              {
                                 "GroupId": "string",
                                 "GroupName": "string",
                                 "PeeringStatus": "string",
                                 "UserId": "string",
                                 "VpcId": "string",
                                 "VpcPeeringConnectionId": "string"
                              }
                           ]
                        }
                     ],
                     "OwnerId": "string",
                     "VpcId": "string"
                  },
                  "AwsEc2Subnet": {
                     "AssignIpv6AddressOnCreation": boolean,
                     "AvailabilityZone": "string",
                     "AvailabilityZoneId": "string",
                     "AvailableIpAddressCount": number,
                     "CidrBlock": "string",
                     "DefaultForAz": boolean,
                     "Ipv6CidrBlockAssociationSet": [
                        {
                           "AssociationId": "string",
                           "CidrBlockState": "string",
                           "Ipv6CidrBlock": "string"
                        }
                     ],
                     "MapPublicIpOnLaunch": boolean,
                     "OwnerId": "string",
                     "State": "string",
                     "SubnetArn": "string",
                     "SubnetId": "string",
                     "VpcId": "string"
                  },
                  "AwsEc2TransitGateway": {
                     "AmazonSideAsn": number,
                     "AssociationDefaultRouteTableId": "string",
                     "AutoAcceptSharedAttachments": "string",
                     "DefaultRouteTableAssociation": "string",
                     "DefaultRouteTablePropagation": "string",
                     "Description": "string",
                     "DnsSupport": "string",
                     "Id": "string",
                     "MulticastSupport": "string",
                     "PropagationDefaultRouteTableId": "string",
                     "TransitGatewayCidrBlocks": [ "string" ],
                     "VpnEcmpSupport": "string"
                  },
                  "AwsEc2Volume": {
                     "Attachments": [
                        {
                           "AttachTime": "string",
                           "DeleteOnTermination": boolean,
                           "InstanceId": "string",
                           "Status": "string"
                        }
                     ],
                     "CreateTime": "string",
                     "DeviceName": "string",
                     "Encrypted": boolean,
                     "KmsKeyId": "string",
                     "Size": number,
                     "SnapshotId": "string",
                     "Status": "string",
                     "VolumeId": "string",
                     "VolumeScanStatus": "string",
                     "VolumeType": "string"
                  },
                  "AwsEc2Vpc": {
                     "CidrBlockAssociationSet": [
                        {
                           "AssociationId": "string",
                           "CidrBlock": "string",
                           "CidrBlockState": "string"
                        }
                     ],
                     "DhcpOptionsId": "string",
                     "Ipv6CidrBlockAssociationSet": [
                        {
                           "AssociationId": "string",
                           "CidrBlockState": "string",
                           "Ipv6CidrBlock": "string"
                        }
                     ],
                     "State": "string"
                  },
                  "AwsEc2VpcEndpointService": {
                     "AcceptanceRequired": boolean,
                     "AvailabilityZones": [ "string" ],
                     "BaseEndpointDnsNames": [ "string" ],
                     "GatewayLoadBalancerArns": [ "string" ],
                     "ManagesVpcEndpoints": boolean,
                     "NetworkLoadBalancerArns": [ "string" ],
                     "PrivateDnsName": "string",
                     "ServiceId": "string",
                     "ServiceName": "string",
                     "ServiceState": "string",
                     "ServiceType": [
                        {
                           "ServiceType": "string"
                        }
                     ]
                  },
                  "AwsEc2VpcPeeringConnection": {
                     "AccepterVpcInfo": {
                        "CidrBlock": "string",
                        "CidrBlockSet": [
                           {
                              "CidrBlock": "string"
                           }
                        ],
                        "Ipv6CidrBlockSet": [
                           {
                              "Ipv6CidrBlock": "string"
                           }
                        ],
                        "OwnerId": "string",
                        "PeeringOptions": {
                           "AllowDnsResolutionFromRemoteVpc": boolean,
                           "AllowEgressFromLocalClassicLinkToRemoteVpc": boolean,
                           "AllowEgressFromLocalVpcToRemoteClassicLink": boolean
                        },
                        "Region": "string",
                        "VpcId": "string"
                     },
                     "ExpirationTime": "string",
                     "RequesterVpcInfo": {
                        "CidrBlock": "string",
                        "CidrBlockSet": [
                           {
                              "CidrBlock": "string"
                           }
                        ],
                        "Ipv6CidrBlockSet": [
                           {
                              "Ipv6CidrBlock": "string"
                           }
                        ],
                        "OwnerId": "string",
                        "PeeringOptions": {
                           "AllowDnsResolutionFromRemoteVpc": boolean,
                           "AllowEgressFromLocalClassicLinkToRemoteVpc": boolean,
                           "AllowEgressFromLocalVpcToRemoteClassicLink": boolean
                        },
                        "Region": "string",
                        "VpcId": "string"
                     },
                     "Status": {
                        "Code": "string",
                        "Message": "string"
                     },
                     "VpcPeeringConnectionId": "string"
                  },
                  "AwsEc2VpnConnection": {
                     "Category": "string",
                     "CustomerGatewayConfiguration": "string",
                     "CustomerGatewayId": "string",
                     "Options": {
                        "StaticRoutesOnly": boolean,
                        "TunnelOptions": [
                           {
                              "DpdTimeoutSeconds": number,
                              "IkeVersions": [ "string" ],
                              "OutsideIpAddress": "string",
                              "Phase1DhGroupNumbers": [ number ],
                              "Phase1EncryptionAlgorithms": [ "string" ],
                              "Phase1IntegrityAlgorithms": [ "string" ],
                              "Phase1LifetimeSeconds": number,
                              "Phase2DhGroupNumbers": [ number ],
                              "Phase2EncryptionAlgorithms": [ "string" ],
                              "Phase2IntegrityAlgorithms": [ "string" ],
                              "Phase2LifetimeSeconds": number,
                              "PreSharedKey": "string",
                              "RekeyFuzzPercentage": number,
                              "RekeyMarginTimeSeconds": number,
                              "ReplayWindowSize": number,
                              "TunnelInsideCidr": "string"
                           }
                        ]
                     },
                     "Routes": [
                        {
                           "DestinationCidrBlock": "string",
                           "State": "string"
                        }
                     ],
                     "State": "string",
                     "TransitGatewayId": "string",
                     "Type": "string",
                     "VgwTelemetry": [
                        {
                           "AcceptedRouteCount": number,
                           "CertificateArn": "string",
                           "LastStatusChange": "string",
                           "OutsideIpAddress": "string",
                           "Status": "string",
                           "StatusMessage": "string"
                        }
                     ],
                     "VpnConnectionId": "string",
                     "VpnGatewayId": "string"
                  },
                  "AwsEcrContainerImage": {
                     "Architecture": "string",
                     "ImageDigest": "string",
                     "ImagePublishedAt": "string",
                     "ImageTags": [ "string" ],
                     "RegistryId": "string",
                     "RepositoryName": "string"
                  },
                  "AwsEcrRepository": {
                     "Arn": "string",
                     "ImageScanningConfiguration": {
                        "ScanOnPush": boolean
                     },
                     "ImageTagMutability": "string",
                     "LifecyclePolicy": {
                        "LifecyclePolicyText": "string",
                        "RegistryId": "string"
                     },
                     "RepositoryName": "string",
                     "RepositoryPolicyText": "string"
                  },
                  "AwsEcsCluster": {
                     "ActiveServicesCount": number,
                     "CapacityProviders": [ "string" ],
                     "ClusterArn": "string",
                     "ClusterName": "string",
                     "ClusterSettings": [
                        {
                           "Name": "string",
                           "Value": "string"
                        }
                     ],
                     "Configuration": {
                        "ExecuteCommandConfiguration": {
                           "KmsKeyId": "string",
                           "LogConfiguration": {
                              "CloudWatchEncryptionEnabled": boolean,
                              "CloudWatchLogGroupName": "string",
                              "S3BucketName": "string",
                              "S3EncryptionEnabled": boolean,
                              "S3KeyPrefix": "string"
                           },
                           "Logging": "string"
                        }
                     },
                     "DefaultCapacityProviderStrategy": [
                        {
                           "Base": number,
                           "CapacityProvider": "string",
                           "Weight": number
                        }
                     ],
                     "RegisteredContainerInstancesCount": number,
                     "RunningTasksCount": number,
                     "Status": "string"
                  },
                  "AwsEcsContainer": {
                     "Image": "string",
                     "MountPoints": [
                        {
                           "ContainerPath": "string",
                           "SourceVolume": "string"
                        }
                     ],
                     "Name": "string",
                     "Privileged": boolean
                  },
                  "AwsEcsService": {
                     "CapacityProviderStrategy": [
                        {
                           "Base": number,
                           "CapacityProvider": "string",
                           "Weight": number
                        }
                     ],
                     "Cluster": "string",
                     "DeploymentConfiguration": {
                        "DeploymentCircuitBreaker": {
                           "Enable": boolean,
                           "Rollback": boolean
                        },
                        "MaximumPercent": number,
                        "MinimumHealthyPercent": number
                     },
                     "DeploymentController": {
                        "Type": "string"
                     },
                     "DesiredCount": number,
                     "EnableEcsManagedTags": boolean,
                     "EnableExecuteCommand": boolean,
                     "HealthCheckGracePeriodSeconds": number,
                     "LaunchType": "string",
                     "LoadBalancers": [
                        {
                           "ContainerName": "string",
                           "ContainerPort": number,
                           "LoadBalancerName": "string",
                           "TargetGroupArn": "string"
                        }
                     ],
                     "Name": "string",
                     "NetworkConfiguration": {
                        "AwsVpcConfiguration": {
                           "AssignPublicIp": "string",
                           "SecurityGroups": [ "string" ],
                           "Subnets": [ "string" ]
                        }
                     },
                     "PlacementConstraints": [
                        {
                           "Expression": "string",
                           "Type": "string"
                        }
                     ],
                     "PlacementStrategies": [
                        {
                           "Field": "string",
                           "Type": "string"
                        }
                     ],
                     "PlatformVersion": "string",
                     "PropagateTags": "string",
                     "Role": "string",
                     "SchedulingStrategy": "string",
                     "ServiceArn": "string",
                     "ServiceName": "string",
                     "ServiceRegistries": [
                        {
                           "ContainerName": "string",
                           "ContainerPort": number,
                           "Port": number,
                           "RegistryArn": "string"
                        }
                     ],
                     "TaskDefinition": "string"
                  },
                  "AwsEcsTask": {
                     "ClusterArn": "string",
                     "Containers": [
                        {
                           "Image": "string",
                           "MountPoints": [
                              {
                                 "ContainerPath": "string",
                                 "SourceVolume": "string"
                              }
                           ],
                           "Name": "string",
                           "Privileged": boolean
                        }
                     ],
                     "CreatedAt": "string",
                     "Group": "string",
                     "StartedAt": "string",
                     "StartedBy": "string",
                     "TaskDefinitionArn": "string",
                     "Version": "string",
                     "Volumes": [
                        {
                           "Host": {
                              "SourcePath": "string"
                           },
                           "Name": "string"
                        }
                     ]
                  },
                  "AwsEcsTaskDefinition": {
                     "ContainerDefinitions": [
                        {
                           "Command": [ "string" ],
                           "Cpu": number,
                           "DependsOn": [
                              {
                                 "Condition": "string",
                                 "ContainerName": "string"
                              }
                           ],
                           "DisableNetworking": boolean,
                           "DnsSearchDomains": [ "string" ],
                           "DnsServers": [ "string" ],
                           "DockerLabels": {
                              "string" : "string"
                           },
                           "DockerSecurityOptions": [ "string" ],
                           "EntryPoint": [ "string" ],
                           "Environment": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "EnvironmentFiles": [
                              {
                                 "Type": "string",
                                 "Value": "string"
                              }
                           ],
                           "Essential": boolean,
                           "ExtraHosts": [
                              {
                                 "Hostname": "string",
                                 "IpAddress": "string"
                              }
                           ],
                           "FirelensConfiguration": {
                              "Options": {
                                 "string" : "string"
                              },
                              "Type": "string"
                           },
                           "HealthCheck": {
                              "Command": [ "string" ],
                              "Interval": number,
                              "Retries": number,
                              "StartPeriod": number,
                              "Timeout": number
                           },
                           "Hostname": "string",
                           "Image": "string",
                           "Interactive": boolean,
                           "Links": [ "string" ],
                           "LinuxParameters": {
                              "Capabilities": {
                                 "Add": [ "string" ],
                                 "Drop": [ "string" ]
                              },
                              "Devices": [
                                 {
                                    "ContainerPath": "string",
                                    "HostPath": "string",
                                    "Permissions": [ "string" ]
                                 }
                              ],
                              "InitProcessEnabled": boolean,
                              "MaxSwap": number,
                              "SharedMemorySize": number,
                              "Swappiness": number,
                              "Tmpfs": [
                                 {
                                    "ContainerPath": "string",
                                    "MountOptions": [ "string" ],
                                    "Size": number
                                 }
                              ]
                           },
                           "LogConfiguration": {
                              "LogDriver": "string",
                              "Options": {
                                 "string" : "string"
                              },
                              "SecretOptions": [
                                 {
                                    "Name": "string",
                                    "ValueFrom": "string"
                                 }
                              ]
                           },
                           "Memory": number,
                           "MemoryReservation": number,
                           "MountPoints": [
                              {
                                 "ContainerPath": "string",
                                 "ReadOnly": boolean,
                                 "SourceVolume": "string"
                              }
                           ],
                           "Name": "string",
                           "PortMappings": [
                              {
                                 "ContainerPort": number,
                                 "HostPort": number,
                                 "Protocol": "string"
                              }
                           ],
                           "Privileged": boolean,
                           "PseudoTerminal": boolean,
                           "ReadonlyRootFilesystem": boolean,
                           "RepositoryCredentials": {
                              "CredentialsParameter": "string"
                           },
                           "ResourceRequirements": [
                              {
                                 "Type": "string",
                                 "Value": "string"
                              }
                           ],
                           "Secrets": [
                              {
                                 "Name": "string",
                                 "ValueFrom": "string"
                              }
                           ],
                           "StartTimeout": number,
                           "StopTimeout": number,
                           "SystemControls": [
                              {
                                 "Namespace": "string",
                                 "Value": "string"
                              }
                           ],
                           "Ulimits": [
                              {
                                 "HardLimit": number,
                                 "Name": "string",
                                 "SoftLimit": number
                              }
                           ],
                           "User": "string",
                           "VolumesFrom": [
                              {
                                 "ReadOnly": boolean,
                                 "SourceContainer": "string"
                              }
                           ],
                           "WorkingDirectory": "string"
                        }
                     ],
                     "Cpu": "string",
                     "ExecutionRoleArn": "string",
                     "Family": "string",
                     "InferenceAccelerators": [
                        {
                           "DeviceName": "string",
                           "DeviceType": "string"
                        }
                     ],
                     "IpcMode": "string",
                     "Memory": "string",
                     "NetworkMode": "string",
                     "PidMode": "string",
                     "PlacementConstraints": [
                        {
                           "Expression": "string",
                           "Type": "string"
                        }
                     ],
                     "ProxyConfiguration": {
                        "ContainerName": "string",
                        "ProxyConfigurationProperties": [
                           {
                              "Name": "string",
                              "Value": "string"
                           }
                        ],
                        "Type": "string"
                     },
                     "RequiresCompatibilities": [ "string" ],
                     "Status": "string",
                     "TaskRoleArn": "string",
                     "Volumes": [
                        {
                           "DockerVolumeConfiguration": {
                              "Autoprovision": boolean,
                              "Driver": "string",
                              "DriverOpts": {
                                 "string" : "string"
                              },
                              "Labels": {
                                 "string" : "string"
                              },
                              "Scope": "string"
                           },
                           "EfsVolumeConfiguration": {
                              "AuthorizationConfig": {
                                 "AccessPointId": "string",
                                 "Iam": "string"
                              },
                              "FilesystemId": "string",
                              "RootDirectory": "string",
                              "TransitEncryption": "string",
                              "TransitEncryptionPort": number
                           },
                           "Host": {
                              "SourcePath": "string"
                           },
                           "Name": "string"
                        }
                     ]
                  },
                  "AwsEfsAccessPoint": {
                     "AccessPointId": "string",
                     "Arn": "string",
                     "ClientToken": "string",
                     "FileSystemId": "string",
                     "PosixUser": {
                        "Gid": "string",
                        "SecondaryGids": [ "string" ],
                        "Uid": "string"
                     },
                     "RootDirectory": {
                        "CreationInfo": {
                           "OwnerGid": "string",
                           "OwnerUid": "string",
                           "Permissions": "string"
                        },
                        "Path": "string"
                     }
                  },
                  "AwsEksCluster": {
                     "Arn": "string",
                     "CertificateAuthorityData": "string",
                     "ClusterStatus": "string",
                     "Endpoint": "string",
                     "Logging": {
                        "ClusterLogging": [
                           {
                              "Enabled": boolean,
                              "Types": [ "string" ]
                           }
                        ]
                     },
                     "Name": "string",
                     "ResourcesVpcConfig": {
                        "EndpointPublicAccess": boolean,
                        "SecurityGroupIds": [ "string" ],
                        "SubnetIds": [ "string" ]
                     },
                     "RoleArn": "string",
                     "Version": "string"
                  },
                  "AwsElasticBeanstalkEnvironment": {
                     "ApplicationName": "string",
                     "Cname": "string",
                     "DateCreated": "string",
                     "DateUpdated": "string",
                     "Description": "string",
                     "EndpointUrl": "string",
                     "EnvironmentArn": "string",
                     "EnvironmentId": "string",
                     "EnvironmentLinks": [
                        {
                           "EnvironmentName": "string",
                           "LinkName": "string"
                        }
                     ],
                     "EnvironmentName": "string",
                     "OptionSettings": [
                        {
                           "Namespace": "string",
                           "OptionName": "string",
                           "ResourceName": "string",
                           "Value": "string"
                        }
                     ],
                     "PlatformArn": "string",
                     "SolutionStackName": "string",
                     "Status": "string",
                     "Tier": {
                        "Name": "string",
                        "Type": "string",
                        "Version": "string"
                     },
                     "VersionLabel": "string"
                  },
                  "AwsElasticsearchDomain": {
                     "AccessPolicies": "string",
                     "DomainEndpointOptions": {
                        "EnforceHTTPS": boolean,
                        "TLSSecurityPolicy": "string"
                     },
                     "DomainId": "string",
                     "DomainName": "string",
                     "ElasticsearchClusterConfig": {
                        "DedicatedMasterCount": number,
                        "DedicatedMasterEnabled": boolean,
                        "DedicatedMasterType": "string",
                        "InstanceCount": number,
                        "InstanceType": "string",
                        "ZoneAwarenessConfig": {
                           "AvailabilityZoneCount": number
                        },
                        "ZoneAwarenessEnabled": boolean
                     },
                     "ElasticsearchVersion": "string",
                     "EncryptionAtRestOptions": {
                        "Enabled": boolean,
                        "KmsKeyId": "string"
                     },
                     "Endpoint": "string",
                     "Endpoints": {
                        "string" : "string"
                     },
                     "LogPublishingOptions": {
                        "AuditLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        },
                        "IndexSlowLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        },
                        "SearchSlowLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        }
                     },
                     "NodeToNodeEncryptionOptions": {
                        "Enabled": boolean
                     },
                     "ServiceSoftwareOptions": {
                        "AutomatedUpdateDate": "string",
                        "Cancellable": boolean,
                        "CurrentVersion": "string",
                        "Description": "string",
                        "NewVersion": "string",
                        "UpdateAvailable": boolean,
                        "UpdateStatus": "string"
                     },
                     "VPCOptions": {
                        "AvailabilityZones": [ "string" ],
                        "SecurityGroupIds": [ "string" ],
                        "SubnetIds": [ "string" ],
                        "VPCId": "string"
                     }
                  },
                  "AwsElbLoadBalancer": {
                     "AvailabilityZones": [ "string" ],
                     "BackendServerDescriptions": [
                        {
                           "InstancePort": number,
                           "PolicyNames": [ "string" ]
                        }
                     ],
                     "CanonicalHostedZoneName": "string",
                     "CanonicalHostedZoneNameID": "string",
                     "CreatedTime": "string",
                     "DnsName": "string",
                     "HealthCheck": {
                        "HealthyThreshold": number,
                        "Interval": number,
                        "Target": "string",
                        "Timeout": number,
                        "UnhealthyThreshold": number
                     },
                     "Instances": [
                        {
                           "InstanceId": "string"
                        }
                     ],
                     "ListenerDescriptions": [
                        {
                           "Listener": {
                              "InstancePort": number,
                              "InstanceProtocol": "string",
                              "LoadBalancerPort": number,
                              "Protocol": "string",
                              "SslCertificateId": "string"
                           },
                           "PolicyNames": [ "string" ]
                        }
                     ],
                     "LoadBalancerAttributes": {
                        "AccessLog": {
                           "EmitInterval": number,
                           "Enabled": boolean,
                           "S3BucketName": "string",
                           "S3BucketPrefix": "string"
                        },
                        "AdditionalAttributes": [
                           {
                              "Key": "string",
                              "Value": "string"
                           }
                        ],
                        "ConnectionDraining": {
                           "Enabled": boolean,
                           "Timeout": number
                        },
                        "ConnectionSettings": {
                           "IdleTimeout": number
                        },
                        "CrossZoneLoadBalancing": {
                           "Enabled": boolean
                        }
                     },
                     "LoadBalancerName": "string",
                     "Policies": {
                        "AppCookieStickinessPolicies": [
                           {
                              "CookieName": "string",
                              "PolicyName": "string"
                           }
                        ],
                        "LbCookieStickinessPolicies": [
                           {
                              "CookieExpirationPeriod": number,
                              "PolicyName": "string"
                           }
                        ],
                        "OtherPolicies": [ "string" ]
                     },
                     "Scheme": "string",
                     "SecurityGroups": [ "string" ],
                     "SourceSecurityGroup": {
                        "GroupName": "string",
                        "OwnerAlias": "string"
                     },
                     "Subnets": [ "string" ],
                     "VpcId": "string"
                  },
                  "AwsElbv2LoadBalancer": {
                     "AvailabilityZones": [
                        {
                           "SubnetId": "string",
                           "ZoneName": "string"
                        }
                     ],
                     "CanonicalHostedZoneId": "string",
                     "CreatedTime": "string",
                     "DNSName": "string",
                     "IpAddressType": "string",
                     "LoadBalancerAttributes": [
                        {
                           "Key": "string",
                           "Value": "string"
                        }
                     ],
                     "Scheme": "string",
                     "SecurityGroups": [ "string" ],
                     "State": {
                        "Code": "string",
                        "Reason": "string"
                     },
                     "Type": "string",
                     "VpcId": "string"
                  },
                  "AwsEventSchemasRegistry": {
                     "Description": "string",
                     "RegistryArn": "string",
                     "RegistryName": "string"
                  },
                  "AwsEventsEndpoint": {
                     "Arn": "string",
                     "Description": "string",
                     "EndpointId": "string",
                     "EndpointUrl": "string",
                     "EventBuses": [
                        {
                           "EventBusArn": "string"
                        }
                     ],
                     "Name": "string",
                     "ReplicationConfig": {
                        "State": "string"
                     },
                     "RoleArn": "string",
                     "RoutingConfig": {
                        "FailoverConfig": {
                           "Primary": {
                              "HealthCheck": "string"
                           },
                           "Secondary": {
                              "Route": "string"
                           }
                        }
                     },
                     "State": "string",
                     "StateReason": "string"
                  },
                  "AwsEventsEventbus": {
                     "Arn": "string",
                     "Name": "string",
                     "Policy": "string"
                  },
                  "AwsGuardDutyDetector": {
                     "DataSources": {
                        "CloudTrail": {
                           "Status": "string"
                        },
                        "DnsLogs": {
                           "Status": "string"
                        },
                        "FlowLogs": {
                           "Status": "string"
                        },
                        "Kubernetes": {
                           "AuditLogs": {
                              "Status": "string"
                           }
                        },
                        "MalwareProtection": {
                           "ScanEc2InstanceWithFindings": {
                              "EbsVolumes": {
                                 "Reason": "string",
                                 "Status": "string"
                              }
                           },
                           "ServiceRole": "string"
                        },
                        "S3Logs": {
                           "Status": "string"
                        }
                     },
                     "Features": [
                        {
                           "Name": "string",
                           "Status": "string"
                        }
                     ],
                     "FindingPublishingFrequency": "string",
                     "ServiceRole": "string",
                     "Status": "string"
                  },
                  "AwsIamAccessKey": {
                     "AccessKeyId": "string",
                     "AccountId": "string",
                     "CreatedAt": "string",
                     "PrincipalId": "string",
                     "PrincipalName": "string",
                     "PrincipalType": "string",
                     "SessionContext": {
                        "Attributes": {
                           "CreationDate": "string",
                           "MfaAuthenticated": boolean
                        },
                        "SessionIssuer": {
                           "AccountId": "string",
                           "Arn": "string",
                           "PrincipalId": "string",
                           "Type": "string",
                           "UserName": "string"
                        }
                     },
                     "Status": "string",
                     "UserName": "string"
                  },
                  "AwsIamGroup": {
                     "AttachedManagedPolicies": [
                        {
                           "PolicyArn": "string",
                           "PolicyName": "string"
                        }
                     ],
                     "CreateDate": "string",
                     "GroupId": "string",
                     "GroupName": "string",
                     "GroupPolicyList": [
                        {
                           "PolicyName": "string"
                        }
                     ],
                     "Path": "string"
                  },
                  "AwsIamPolicy": {
                     "AttachmentCount": number,
                     "CreateDate": "string",
                     "DefaultVersionId": "string",
                     "Description": "string",
                     "IsAttachable": boolean,
                     "Path": "string",
                     "PermissionsBoundaryUsageCount": number,
                     "PolicyId": "string",
                     "PolicyName": "string",
                     "PolicyVersionList": [
                        {
                           "CreateDate": "string",
                           "IsDefaultVersion": boolean,
                           "VersionId": "string"
                        }
                     ],
                     "UpdateDate": "string"
                  },
                  "AwsIamRole": {
                     "AssumeRolePolicyDocument": "string",
                     "AttachedManagedPolicies": [
                        {
                           "PolicyArn": "string",
                           "PolicyName": "string"
                        }
                     ],
                     "CreateDate": "string",
                     "InstanceProfileList": [
                        {
                           "Arn": "string",
                           "CreateDate": "string",
                           "InstanceProfileId": "string",
                           "InstanceProfileName": "string",
                           "Path": "string",
                           "Roles": [
                              {
                                 "Arn": "string",
                                 "AssumeRolePolicyDocument": "string",
                                 "CreateDate": "string",
                                 "Path": "string",
                                 "RoleId": "string",
                                 "RoleName": "string"
                              }
                           ]
                        }
                     ],
                     "MaxSessionDuration": number,
                     "Path": "string",
                     "PermissionsBoundary": {
                        "PermissionsBoundaryArn": "string",
                        "PermissionsBoundaryType": "string"
                     },
                     "RoleId": "string",
                     "RoleName": "string",
                     "RolePolicyList": [
                        {
                           "PolicyName": "string"
                        }
                     ]
                  },
                  "AwsIamUser": {
                     "AttachedManagedPolicies": [
                        {
                           "PolicyArn": "string",
                           "PolicyName": "string"
                        }
                     ],
                     "CreateDate": "string",
                     "GroupList": [ "string" ],
                     "Path": "string",
                     "PermissionsBoundary": {
                        "PermissionsBoundaryArn": "string",
                        "PermissionsBoundaryType": "string"
                     },
                     "UserId": "string",
                     "UserName": "string",
                     "UserPolicyList": [
                        {
                           "PolicyName": "string"
                        }
                     ]
                  },
                  "AwsKinesisStream": {
                     "Arn": "string",
                     "Name": "string",
                     "RetentionPeriodHours": number,
                     "ShardCount": number,
                     "StreamEncryption": {
                        "EncryptionType": "string",
                        "KeyId": "string"
                     }
                  },
                  "AwsKmsKey": {
                     "AWSAccountId": "string",
                     "CreationDate": number,
                     "Description": "string",
                     "KeyId": "string",
                     "KeyManager": "string",
                     "KeyRotationStatus": boolean,
                     "KeyState": "string",
                     "Origin": "string"
                  },
                  "AwsLambdaFunction": {
                     "Architectures": [ "string" ],
                     "Code": {
                        "S3Bucket": "string",
                        "S3Key": "string",
                        "S3ObjectVersion": "string",
                        "ZipFile": "string"
                     },
                     "CodeSha256": "string",
                     "DeadLetterConfig": {
                        "TargetArn": "string"
                     },
                     "Environment": {
                        "Error": {
                           "ErrorCode": "string",
                           "Message": "string"
                        },
                        "Variables": {
                           "string" : "string"
                        }
                     },
                     "FunctionName": "string",
                     "Handler": "string",
                     "KmsKeyArn": "string",
                     "LastModified": "string",
                     "Layers": [
                        {
                           "Arn": "string",
                           "CodeSize": number
                        }
                     ],
                     "MasterArn": "string",
                     "MemorySize": number,
                     "PackageType": "string",
                     "RevisionId": "string",
                     "Role": "string",
                     "Runtime": "string",
                     "Timeout": number,
                     "TracingConfig": {
                        "Mode": "string"
                     },
                     "Version": "string",
                     "VpcConfig": {
                        "SecurityGroupIds": [ "string" ],
                        "SubnetIds": [ "string" ],
                        "VpcId": "string"
                     }
                  },
                  "AwsLambdaLayerVersion": {
                     "CompatibleRuntimes": [ "string" ],
                     "CreatedDate": "string",
                     "Version": number
                  },
                  "AwsMskCluster": {
                     "ClusterInfo": {
                        "ClientAuthentication": {
                           "Sasl": {
                              "Iam": {
                                 "Enabled": boolean
                              },
                              "Scram": {
                                 "Enabled": boolean
                              }
                           },
                           "Tls": {
                              "CertificateAuthorityArnList": [ "string" ],
                              "Enabled": boolean
                           },
                           "Unauthenticated": {
                              "Enabled": boolean
                           }
                        },
                        "ClusterName": "string",
                        "CurrentVersion": "string",
                        "EncryptionInfo": {
                           "EncryptionAtRest": {
                              "DataVolumeKMSKeyId": "string"
                           },
                           "EncryptionInTransit": {
                              "ClientBroker": "string",
                              "InCluster": boolean
                           }
                        },
                        "EnhancedMonitoring": "string",
                        "NumberOfBrokerNodes": number
                     }
                  },
                  "AwsNetworkFirewallFirewall": {
                     "DeleteProtection": boolean,
                     "Description": "string",
                     "FirewallArn": "string",
                     "FirewallId": "string",
                     "FirewallName": "string",
                     "FirewallPolicyArn": "string",
                     "FirewallPolicyChangeProtection": boolean,
                     "SubnetChangeProtection": boolean,
                     "SubnetMappings": [
                        {
                           "SubnetId": "string"
                        }
                     ],
                     "VpcId": "string"
                  },
                  "AwsNetworkFirewallFirewallPolicy": {
                     "Description": "string",
                     "FirewallPolicy": {
                        "StatefulRuleGroupReferences": [
                           {
                              "ResourceArn": "string"
                           }
                        ],
                        "StatelessCustomActions": [
                           {
                              "ActionDefinition": {
                                 "PublishMetricAction": {
                                    "Dimensions": [
                                       {
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "ActionName": "string"
                           }
                        ],
                        "StatelessDefaultActions": [ "string" ],
                        "StatelessFragmentDefaultActions": [ "string" ],
                        "StatelessRuleGroupReferences": [
                           {
                              "Priority": number,
                              "ResourceArn": "string"
                           }
                        ]
                     },
                     "FirewallPolicyArn": "string",
                     "FirewallPolicyId": "string",
                     "FirewallPolicyName": "string"
                  },
                  "AwsNetworkFirewallRuleGroup": {
                     "Capacity": number,
                     "Description": "string",
                     "RuleGroup": {
                        "RulesSource": {
                           "RulesSourceList": {
                              "GeneratedRulesType": "string",
                              "Targets": [ "string" ],
                              "TargetTypes": [ "string" ]
                           },
                           "RulesString": "string",
                           "StatefulRules": [
                              {
                                 "Action": "string",
                                 "Header": {
                                    "Destination": "string",
                                    "DestinationPort": "string",
                                    "Direction": "string",
                                    "Protocol": "string",
                                    "Source": "string",
                                    "SourcePort": "string"
                                 },
                                 "RuleOptions": [
                                    {
                                       "Keyword": "string",
                                       "Settings": [ "string" ]
                                    }
                                 ]
                              }
                           ],
                           "StatelessRulesAndCustomActions": {
                              "CustomActions": [
                                 {
                                    "ActionDefinition": {
                                       "PublishMetricAction": {
                                          "Dimensions": [
                                             {
                                                "Value": "string"
                                             }
                                          ]
                                       }
                                    },
                                    "ActionName": "string"
                                 }
                              ],
                              "StatelessRules": [
                                 {
                                    "Priority": number,
                                    "RuleDefinition": {
                                       "Actions": [ "string" ],
                                       "MatchAttributes": {
                                          "DestinationPorts": [
                                             {
                                                "FromPort": number,
                                                "ToPort": number
                                             }
                                          ],
                                          "Destinations": [
                                             {
                                                "AddressDefinition": "string"
                                             }
                                          ],
                                          "Protocols": [ number ],
                                          "SourcePorts": [
                                             {
                                                "FromPort": number,
                                                "ToPort": number
                                             }
                                          ],
                                          "Sources": [
                                             {
                                                "AddressDefinition": "string"
                                             }
                                          ],
                                          "TcpFlags": [
                                             {
                                                "Flags": [ "string" ],
                                                "Masks": [ "string" ]
                                             }
                                          ]
                                       }
                                    }
                                 }
                              ]
                           }
                        },
                        "RuleVariables": {
                           "IpSets": {
                              "Definition": [ "string" ]
                           },
                           "PortSets": {
                              "Definition": [ "string" ]
                           }
                        }
                     },
                     "RuleGroupArn": "string",
                     "RuleGroupId": "string",
                     "RuleGroupName": "string",
                     "Type": "string"
                  },
                  "AwsOpenSearchServiceDomain": {
                     "AccessPolicies": "string",
                     "AdvancedSecurityOptions": {
                        "Enabled": boolean,
                        "InternalUserDatabaseEnabled": boolean,
                        "MasterUserOptions": {
                           "MasterUserArn": "string",
                           "MasterUserName": "string",
                           "MasterUserPassword": "string"
                        }
                     },
                     "Arn": "string",
                     "ClusterConfig": {
                        "DedicatedMasterCount": number,
                        "DedicatedMasterEnabled": boolean,
                        "DedicatedMasterType": "string",
                        "InstanceCount": number,
                        "InstanceType": "string",
                        "WarmCount": number,
                        "WarmEnabled": boolean,
                        "WarmType": "string",
                        "ZoneAwarenessConfig": {
                           "AvailabilityZoneCount": number
                        },
                        "ZoneAwarenessEnabled": boolean
                     },
                     "DomainEndpoint": "string",
                     "DomainEndpointOptions": {
                        "CustomEndpoint": "string",
                        "CustomEndpointCertificateArn": "string",
                        "CustomEndpointEnabled": boolean,
                        "EnforceHTTPS": boolean,
                        "TLSSecurityPolicy": "string"
                     },
                     "DomainEndpoints": {
                        "string" : "string"
                     },
                     "DomainName": "string",
                     "EncryptionAtRestOptions": {
                        "Enabled": boolean,
                        "KmsKeyId": "string"
                     },
                     "EngineVersion": "string",
                     "Id": "string",
                     "LogPublishingOptions": {
                        "AuditLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        },
                        "IndexSlowLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        },
                        "SearchSlowLogs": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "Enabled": boolean
                        }
                     },
                     "NodeToNodeEncryptionOptions": {
                        "Enabled": boolean
                     },
                     "ServiceSoftwareOptions": {
                        "AutomatedUpdateDate": "string",
                        "Cancellable": boolean,
                        "CurrentVersion": "string",
                        "Description": "string",
                        "NewVersion": "string",
                        "OptionalDeployment": boolean,
                        "UpdateAvailable": boolean,
                        "UpdateStatus": "string"
                     },
                     "VpcOptions": {
                        "SecurityGroupIds": [ "string" ],
                        "SubnetIds": [ "string" ]
                     }
                  },
                  "AwsRdsDbCluster": {
                     "ActivityStreamStatus": "string",
                     "AllocatedStorage": number,
                     "AssociatedRoles": [
                        {
                           "RoleArn": "string",
                           "Status": "string"
                        }
                     ],
                     "AutoMinorVersionUpgrade": boolean,
                     "AvailabilityZones": [ "string" ],
                     "BackupRetentionPeriod": number,
                     "ClusterCreateTime": "string",
                     "CopyTagsToSnapshot": boolean,
                     "CrossAccountClone": boolean,
                     "CustomEndpoints": [ "string" ],
                     "DatabaseName": "string",
                     "DbClusterIdentifier": "string",
                     "DbClusterMembers": [
                        {
                           "DbClusterParameterGroupStatus": "string",
                           "DbInstanceIdentifier": "string",
                           "IsClusterWriter": boolean,
                           "PromotionTier": number
                        }
                     ],
                     "DbClusterOptionGroupMemberships": [
                        {
                           "DbClusterOptionGroupName": "string",
                           "Status": "string"
                        }
                     ],
                     "DbClusterParameterGroup": "string",
                     "DbClusterResourceId": "string",
                     "DbSubnetGroup": "string",
                     "DeletionProtection": boolean,
                     "DomainMemberships": [
                        {
                           "Domain": "string",
                           "Fqdn": "string",
                           "IamRoleName": "string",
                           "Status": "string"
                        }
                     ],
                     "EnabledCloudWatchLogsExports": [ "string" ],
                     "Endpoint": "string",
                     "Engine": "string",
                     "EngineMode": "string",
                     "EngineVersion": "string",
                     "HostedZoneId": "string",
                     "HttpEndpointEnabled": boolean,
                     "IamDatabaseAuthenticationEnabled": boolean,
                     "KmsKeyId": "string",
                     "MasterUsername": "string",
                     "MultiAz": boolean,
                     "Port": number,
                     "PreferredBackupWindow": "string",
                     "PreferredMaintenanceWindow": "string",
                     "ReaderEndpoint": "string",
                     "ReadReplicaIdentifiers": [ "string" ],
                     "Status": "string",
                     "StorageEncrypted": boolean,
                     "VpcSecurityGroups": [
                        {
                           "Status": "string",
                           "VpcSecurityGroupId": "string"
                        }
                     ]
                  },
                  "AwsRdsDbClusterSnapshot": {
                     "AllocatedStorage": number,
                     "AvailabilityZones": [ "string" ],
                     "ClusterCreateTime": "string",
                     "DbClusterIdentifier": "string",
                     "DbClusterSnapshotAttributes": [
                        {
                           "AttributeName": "string",
                           "AttributeValues": [ "string" ]
                        }
                     ],
                     "DbClusterSnapshotIdentifier": "string",
                     "Engine": "string",
                     "EngineVersion": "string",
                     "IamDatabaseAuthenticationEnabled": boolean,
                     "KmsKeyId": "string",
                     "LicenseModel": "string",
                     "MasterUsername": "string",
                     "PercentProgress": number,
                     "Port": number,
                     "SnapshotCreateTime": "string",
                     "SnapshotType": "string",
                     "Status": "string",
                     "StorageEncrypted": boolean,
                     "VpcId": "string"
                  },
                  "AwsRdsDbInstance": {
                     "AllocatedStorage": number,
                     "AssociatedRoles": [
                        {
                           "FeatureName": "string",
                           "RoleArn": "string",
                           "Status": "string"
                        }
                     ],
                     "AutoMinorVersionUpgrade": boolean,
                     "AvailabilityZone": "string",
                     "BackupRetentionPeriod": number,
                     "CACertificateIdentifier": "string",
                     "CharacterSetName": "string",
                     "CopyTagsToSnapshot": boolean,
                     "DBClusterIdentifier": "string",
                     "DBInstanceClass": "string",
                     "DBInstanceIdentifier": "string",
                     "DbInstancePort": number,
                     "DbInstanceStatus": "string",
                     "DbiResourceId": "string",
                     "DBName": "string",
                     "DbParameterGroups": [
                        {
                           "DbParameterGroupName": "string",
                           "ParameterApplyStatus": "string"
                        }
                     ],
                     "DbSecurityGroups": [ "string" ],
                     "DbSubnetGroup": {
                        "DbSubnetGroupArn": "string",
                        "DbSubnetGroupDescription": "string",
                        "DbSubnetGroupName": "string",
                        "SubnetGroupStatus": "string",
                        "Subnets": [
                           {
                              "SubnetAvailabilityZone": {
                                 "Name": "string"
                              },
                              "SubnetIdentifier": "string",
                              "SubnetStatus": "string"
                           }
                        ],
                        "VpcId": "string"
                     },
                     "DeletionProtection": boolean,
                     "DomainMemberships": [
                        {
                           "Domain": "string",
                           "Fqdn": "string",
                           "IamRoleName": "string",
                           "Status": "string"
                        }
                     ],
                     "EnabledCloudWatchLogsExports": [ "string" ],
                     "Endpoint": {
                        "Address": "string",
                        "HostedZoneId": "string",
                        "Port": number
                     },
                     "Engine": "string",
                     "EngineVersion": "string",
                     "EnhancedMonitoringResourceArn": "string",
                     "IAMDatabaseAuthenticationEnabled": boolean,
                     "InstanceCreateTime": "string",
                     "Iops": number,
                     "KmsKeyId": "string",
                     "LatestRestorableTime": "string",
                     "LicenseModel": "string",
                     "ListenerEndpoint": {
                        "Address": "string",
                        "HostedZoneId": "string",
                        "Port": number
                     },
                     "MasterUsername": "string",
                     "MaxAllocatedStorage": number,
                     "MonitoringInterval": number,
                     "MonitoringRoleArn": "string",
                     "MultiAz": boolean,
                     "OptionGroupMemberships": [
                        {
                           "OptionGroupName": "string",
                           "Status": "string"
                        }
                     ],
                     "PendingModifiedValues": {
                        "AllocatedStorage": number,
                        "BackupRetentionPeriod": number,
                        "CaCertificateIdentifier": "string",
                        "DbInstanceClass": "string",
                        "DbInstanceIdentifier": "string",
                        "DbSubnetGroupName": "string",
                        "EngineVersion": "string",
                        "Iops": number,
                        "LicenseModel": "string",
                        "MasterUserPassword": "string",
                        "MultiAZ": boolean,
                        "PendingCloudWatchLogsExports": {
                           "LogTypesToDisable": [ "string" ],
                           "LogTypesToEnable": [ "string" ]
                        },
                        "Port": number,
                        "ProcessorFeatures": [
                           {
                              "Name": "string",
                              "Value": "string"
                           }
                        ],
                        "StorageType": "string"
                     },
                     "PerformanceInsightsEnabled": boolean,
                     "PerformanceInsightsKmsKeyId": "string",
                     "PerformanceInsightsRetentionPeriod": number,
                     "PreferredBackupWindow": "string",
                     "PreferredMaintenanceWindow": "string",
                     "ProcessorFeatures": [
                        {
                           "Name": "string",
                           "Value": "string"
                        }
                     ],
                     "PromotionTier": number,
                     "PubliclyAccessible": boolean,
                     "ReadReplicaDBClusterIdentifiers": [ "string" ],
                     "ReadReplicaDBInstanceIdentifiers": [ "string" ],
                     "ReadReplicaSourceDBInstanceIdentifier": "string",
                     "SecondaryAvailabilityZone": "string",
                     "StatusInfos": [
                        {
                           "Message": "string",
                           "Normal": boolean,
                           "Status": "string",
                           "StatusType": "string"
                        }
                     ],
                     "StorageEncrypted": boolean,
                     "StorageType": "string",
                     "TdeCredentialArn": "string",
                     "Timezone": "string",
                     "VpcSecurityGroups": [
                        {
                           "Status": "string",
                           "VpcSecurityGroupId": "string"
                        }
                     ]
                  },
                  "AwsRdsDbSecurityGroup": {
                     "DbSecurityGroupArn": "string",
                     "DbSecurityGroupDescription": "string",
                     "DbSecurityGroupName": "string",
                     "Ec2SecurityGroups": [
                        {
                           "Ec2SecurityGroupId": "string",
                           "Ec2SecurityGroupName": "string",
                           "Ec2SecurityGroupOwnerId": "string",
                           "Status": "string"
                        }
                     ],
                     "IpRanges": [
                        {
                           "CidrIp": "string",
                           "Status": "string"
                        }
                     ],
                     "OwnerId": "string",
                     "VpcId": "string"
                  },
                  "AwsRdsDbSnapshot": {
                     "AllocatedStorage": number,
                     "AvailabilityZone": "string",
                     "DbInstanceIdentifier": "string",
                     "DbiResourceId": "string",
                     "DbSnapshotIdentifier": "string",
                     "Encrypted": boolean,
                     "Engine": "string",
                     "EngineVersion": "string",
                     "IamDatabaseAuthenticationEnabled": boolean,
                     "InstanceCreateTime": "string",
                     "Iops": number,
                     "KmsKeyId": "string",
                     "LicenseModel": "string",
                     "MasterUsername": "string",
                     "OptionGroupName": "string",
                     "PercentProgress": number,
                     "Port": number,
                     "ProcessorFeatures": [
                        {
                           "Name": "string",
                           "Value": "string"
                        }
                     ],
                     "SnapshotCreateTime": "string",
                     "SnapshotType": "string",
                     "SourceDbSnapshotIdentifier": "string",
                     "SourceRegion": "string",
                     "Status": "string",
                     "StorageType": "string",
                     "TdeCredentialArn": "string",
                     "Timezone": "string",
                     "VpcId": "string"
                  },
                  "AwsRdsEventSubscription": {
                     "CustomerAwsId": "string",
                     "CustSubscriptionId": "string",
                     "Enabled": boolean,
                     "EventCategoriesList": [ "string" ],
                     "EventSubscriptionArn": "string",
                     "SnsTopicArn": "string",
                     "SourceIdsList": [ "string" ],
                     "SourceType": "string",
                     "Status": "string",
                     "SubscriptionCreationTime": "string"
                  },
                  "AwsRedshiftCluster": {
                     "AllowVersionUpgrade": boolean,
                     "AutomatedSnapshotRetentionPeriod": number,
                     "AvailabilityZone": "string",
                     "ClusterAvailabilityStatus": "string",
                     "ClusterCreateTime": "string",
                     "ClusterIdentifier": "string",
                     "ClusterNodes": [
                        {
                           "NodeRole": "string",
                           "PrivateIpAddress": "string",
                           "PublicIpAddress": "string"
                        }
                     ],
                     "ClusterParameterGroups": [
                        {
                           "ClusterParameterStatusList": [
                              {
                                 "ParameterApplyErrorDescription": "string",
                                 "ParameterApplyStatus": "string",
                                 "ParameterName": "string"
                              }
                           ],
                           "ParameterApplyStatus": "string",
                           "ParameterGroupName": "string"
                        }
                     ],
                     "ClusterPublicKey": "string",
                     "ClusterRevisionNumber": "string",
                     "ClusterSecurityGroups": [
                        {
                           "ClusterSecurityGroupName": "string",
                           "Status": "string"
                        }
                     ],
                     "ClusterSnapshotCopyStatus": {
                        "DestinationRegion": "string",
                        "ManualSnapshotRetentionPeriod": number,
                        "RetentionPeriod": number,
                        "SnapshotCopyGrantName": "string"
                     },
                     "ClusterStatus": "string",
                     "ClusterSubnetGroupName": "string",
                     "ClusterVersion": "string",
                     "DBName": "string",
                     "DeferredMaintenanceWindows": [
                        {
                           "DeferMaintenanceEndTime": "string",
                           "DeferMaintenanceIdentifier": "string",
                           "DeferMaintenanceStartTime": "string"
                        }
                     ],
                     "ElasticIpStatus": {
                        "ElasticIp": "string",
                        "Status": "string"
                     },
                     "ElasticResizeNumberOfNodeOptions": "string",
                     "Encrypted": boolean,
                     "Endpoint": {
                        "Address": "string",
                        "Port": number
                     },
                     "EnhancedVpcRouting": boolean,
                     "ExpectedNextSnapshotScheduleTime": "string",
                     "ExpectedNextSnapshotScheduleTimeStatus": "string",
                     "HsmStatus": {
                        "HsmClientCertificateIdentifier": "string",
                        "HsmConfigurationIdentifier": "string",
                        "Status": "string"
                     },
                     "IamRoles": [
                        {
                           "ApplyStatus": "string",
                           "IamRoleArn": "string"
                        }
                     ],
                     "KmsKeyId": "string",
                     "LoggingStatus": {
                        "BucketName": "string",
                        "LastFailureMessage": "string",
                        "LastFailureTime": "string",
                        "LastSuccessfulDeliveryTime": "string",
                        "LoggingEnabled": boolean,
                        "S3KeyPrefix": "string"
                     },
                     "MaintenanceTrackName": "string",
                     "ManualSnapshotRetentionPeriod": number,
                     "MasterUsername": "string",
                     "NextMaintenanceWindowStartTime": "string",
                     "NodeType": "string",
                     "NumberOfNodes": number,
                     "PendingActions": [ "string" ],
                     "PendingModifiedValues": {
                        "AutomatedSnapshotRetentionPeriod": number,
                        "ClusterIdentifier": "string",
                        "ClusterType": "string",
                        "ClusterVersion": "string",
                        "EncryptionType": "string",
                        "EnhancedVpcRouting": boolean,
                        "MaintenanceTrackName": "string",
                        "MasterUserPassword": "string",
                        "NodeType": "string",
                        "NumberOfNodes": number,
                        "PubliclyAccessible": boolean
                     },
                     "PreferredMaintenanceWindow": "string",
                     "PubliclyAccessible": boolean,
                     "ResizeInfo": {
                        "AllowCancelResize": boolean,
                        "ResizeType": "string"
                     },
                     "RestoreStatus": {
                        "CurrentRestoreRateInMegaBytesPerSecond": number,
                        "ElapsedTimeInSeconds": number,
                        "EstimatedTimeToCompletionInSeconds": number,
                        "ProgressInMegaBytes": number,
                        "SnapshotSizeInMegaBytes": number,
                        "Status": "string"
                     },
                     "SnapshotScheduleIdentifier": "string",
                     "SnapshotScheduleState": "string",
                     "VpcId": "string",
                     "VpcSecurityGroups": [
                        {
                           "Status": "string",
                           "VpcSecurityGroupId": "string"
                        }
                     ]
                  },
                  "AwsRoute53HostedZone": {
                     "HostedZone": {
                        "Config": {
                           "Comment": "string"
                        },
                        "Id": "string",
                        "Name": "string"
                     },
                     "NameServers": [ "string" ],
                     "QueryLoggingConfig": {
                        "CloudWatchLogsLogGroupArn": {
                           "CloudWatchLogsLogGroupArn": "string",
                           "HostedZoneId": "string",
                           "Id": "string"
                        }
                     },
                     "Vpcs": [
                        {
                           "Id": "string",
                           "Region": "string"
                        }
                     ]
                  },
                  "AwsS3AccessPoint": {
                     "AccessPointArn": "string",
                     "Alias": "string",
                     "Bucket": "string",
                     "BucketAccountId": "string",
                     "Name": "string",
                     "NetworkOrigin": "string",
                     "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": boolean,
                        "BlockPublicPolicy": boolean,
                        "IgnorePublicAcls": boolean,
                        "RestrictPublicBuckets": boolean
                     },
                     "VpcConfiguration": {
                        "VpcId": "string"
                     }
                  },
                  "AwsS3AccountPublicAccessBlock": {
                     "BlockPublicAcls": boolean,
                     "BlockPublicPolicy": boolean,
                     "IgnorePublicAcls": boolean,
                     "RestrictPublicBuckets": boolean
                  },
                  "AwsS3Bucket": {
                     "AccessControlList": "string",
                     "BucketLifecycleConfiguration": {
                        "Rules": [
                           {
                              "AbortIncompleteMultipartUpload": {
                                 "DaysAfterInitiation": number
                              },
                              "ExpirationDate": "string",
                              "ExpirationInDays": number,
                              "ExpiredObjectDeleteMarker": boolean,
                              "Filter": {
                                 "Predicate": {
                                    "Operands": [
                                       {
                                          "Prefix": "string",
                                          "Tag": {
                                             "Key": "string",
                                             "Value": "string"
                                          },
                                          "Type": "string"
                                       }
                                    ],
                                    "Prefix": "string",
                                    "Tag": {
                                       "Key": "string",
                                       "Value": "string"
                                    },
                                    "Type": "string"
                                 }
                              },
                              "ID": "string",
                              "NoncurrentVersionExpirationInDays": number,
                              "NoncurrentVersionTransitions": [
                                 {
                                    "Days": number,
                                    "StorageClass": "string"
                                 }
                              ],
                              "Prefix": "string",
                              "Status": "string",
                              "Transitions": [
                                 {
                                    "Date": "string",
                                    "Days": number,
                                    "StorageClass": "string"
                                 }
                              ]
                           }
                        ]
                     },
                     "BucketLoggingConfiguration": {
                        "DestinationBucketName": "string",
                        "LogFilePrefix": "string"
                     },
                     "BucketNotificationConfiguration": {
                        "Configurations": [
                           {
                              "Destination": "string",
                              "Events": [ "string" ],
                              "Filter": {
                                 "S3KeyFilter": {
                                    "FilterRules": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Type": "string"
                           }
                        ]
                     },
                     "BucketVersioningConfiguration": {
                        "IsMfaDeleteEnabled": boolean,
                        "Status": "string"
                     },
                     "BucketWebsiteConfiguration": {
                        "ErrorDocument": "string",
                        "IndexDocumentSuffix": "string",
                        "RedirectAllRequestsTo": {
                           "Hostname": "string",
                           "Protocol": "string"
                        },
                        "RoutingRules": [
                           {
                              "Condition": {
                                 "HttpErrorCodeReturnedEquals": "string",
                                 "KeyPrefixEquals": "string"
                              },
                              "Redirect": {
                                 "Hostname": "string",
                                 "HttpRedirectCode": "string",
                                 "Protocol": "string",
                                 "ReplaceKeyPrefixWith": "string",
                                 "ReplaceKeyWith": "string"
                              }
                           }
                        ]
                     },
                     "CreatedAt": "string",
                     "Name": "string",
                     "ObjectLockConfiguration": {
                        "ObjectLockEnabled": "string",
                        "Rule": {
                           "DefaultRetention": {
                              "Days": number,
                              "Mode": "string",
                              "Years": number
                           }
                        }
                     },
                     "OwnerAccountId": "string",
                     "OwnerId": "string",
                     "OwnerName": "string",
                     "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": boolean,
                        "BlockPublicPolicy": boolean,
                        "IgnorePublicAcls": boolean,
                        "RestrictPublicBuckets": boolean
                     },
                     "ServerSideEncryptionConfiguration": {
                        "Rules": [
                           {
                              "ApplyServerSideEncryptionByDefault": {
                                 "KMSMasterKeyID": "string",
                                 "SSEAlgorithm": "string"
                              }
                           }
                        ]
                     }
                  },
                  "AwsS3Object": {
                     "ContentType": "string",
                     "ETag": "string",
                     "LastModified": "string",
                     "ServerSideEncryption": "string",
                     "SSEKMSKeyId": "string",
                     "VersionId": "string"
                  },
                  "AwsSageMakerNotebookInstance": {
                     "AcceleratorTypes": [ "string" ],
                     "AdditionalCodeRepositories": [ "string" ],
                     "DefaultCodeRepository": "string",
                     "DirectInternetAccess": "string",
                     "FailureReason": "string",
                     "InstanceMetadataServiceConfiguration": {
                        "MinimumInstanceMetadataServiceVersion": "string"
                     },
                     "InstanceType": "string",
                     "KmsKeyId": "string",
                     "NetworkInterfaceId": "string",
                     "NotebookInstanceArn": "string",
                     "NotebookInstanceLifecycleConfigName": "string",
                     "NotebookInstanceName": "string",
                     "NotebookInstanceStatus": "string",
                     "PlatformIdentifier": "string",
                     "RoleArn": "string",
                     "RootAccess": "string",
                     "SecurityGroups": [ "string" ],
                     "SubnetId": "string",
                     "Url": "string",
                     "VolumeSizeInGB": number
                  },
                  "AwsSecretsManagerSecret": {
                     "Deleted": boolean,
                     "Description": "string",
                     "KmsKeyId": "string",
                     "Name": "string",
                     "RotationEnabled": boolean,
                     "RotationLambdaArn": "string",
                     "RotationOccurredWithinFrequency": boolean,
                     "RotationRules": {
                        "AutomaticallyAfterDays": number
                     }
                  },
                  "AwsSnsTopic": {
                     "ApplicationSuccessFeedbackRoleArn": "string",
                     "FirehoseFailureFeedbackRoleArn": "string",
                     "FirehoseSuccessFeedbackRoleArn": "string",
                     "HttpFailureFeedbackRoleArn": "string",
                     "HttpSuccessFeedbackRoleArn": "string",
                     "KmsMasterKeyId": "string",
                     "Owner": "string",
                     "SqsFailureFeedbackRoleArn": "string",
                     "SqsSuccessFeedbackRoleArn": "string",
                     "Subscription": [
                        {
                           "Endpoint": "string",
                           "Protocol": "string"
                        }
                     ],
                     "TopicName": "string"
                  },
                  "AwsSqsQueue": {
                     "DeadLetterTargetArn": "string",
                     "KmsDataKeyReusePeriodSeconds": number,
                     "KmsMasterKeyId": "string",
                     "QueueName": "string"
                  },
                  "AwsSsmPatchCompliance": {
                     "Patch": {
                        "ComplianceSummary": {
                           "ComplianceType": "string",
                           "CompliantCriticalCount": number,
                           "CompliantHighCount": number,
                           "CompliantInformationalCount": number,
                           "CompliantLowCount": number,
                           "CompliantMediumCount": number,
                           "CompliantUnspecifiedCount": number,
                           "ExecutionType": "string",
                           "NonCompliantCriticalCount": number,
                           "NonCompliantHighCount": number,
                           "NonCompliantInformationalCount": number,
                           "NonCompliantLowCount": number,
                           "NonCompliantMediumCount": number,
                           "NonCompliantUnspecifiedCount": number,
                           "OverallSeverity": "string",
                           "PatchBaselineId": "string",
                           "PatchGroup": "string",
                           "Status": "string"
                        }
                     }
                  },
                  "AwsStepFunctionStateMachine": {
                     "Label": "string",
                     "LoggingConfiguration": {
                        "Destinations": [
                           {
                              "CloudWatchLogsLogGroup": {
                                 "LogGroupArn": "string"
                              }
                           }
                        ],
                        "IncludeExecutionData": boolean,
                        "Level": "string"
                     },
                     "Name": "string",
                     "RoleArn": "string",
                     "StateMachineArn": "string",
                     "Status": "string",
                     "TracingConfiguration": {
                        "Enabled": boolean
                     },
                     "Type": "string"
                  },
                  "AwsWafRateBasedRule": {
                     "MatchPredicates": [
                        {
                           "DataId": "string",
                           "Negated": boolean,
                           "Type": "string"
                        }
                     ],
                     "MetricName": "string",
                     "Name": "string",
                     "RateKey": "string",
                     "RateLimit": number,
                     "RuleId": "string"
                  },
                  "AwsWafRegionalRateBasedRule": {
                     "MatchPredicates": [
                        {
                           "DataId": "string",
                           "Negated": boolean,
                           "Type": "string"
                        }
                     ],
                     "MetricName": "string",
                     "Name": "string",
                     "RateKey": "string",
                     "RateLimit": number,
                     "RuleId": "string"
                  },
                  "AwsWafRegionalRule": {
                     "MetricName": "string",
                     "Name": "string",
                     "PredicateList": [
                        {
                           "DataId": "string",
                           "Negated": boolean,
                           "Type": "string"
                        }
                     ],
                     "RuleId": "string"
                  },
                  "AwsWafRegionalRuleGroup": {
                     "MetricName": "string",
                     "Name": "string",
                     "RuleGroupId": "string",
                     "Rules": [
                        {
                           "Action": {
                              "Type": "string"
                           },
                           "Priority": number,
                           "RuleId": "string",
                           "Type": "string"
                        }
                     ]
                  },
                  "AwsWafRegionalWebAcl": {
                     "DefaultAction": "string",
                     "MetricName": "string",
                     "Name": "string",
                     "RulesList": [
                        {
                           "Action": {
                              "Type": "string"
                           },
                           "OverrideAction": {
                              "Type": "string"
                           },
                           "Priority": number,
                           "RuleId": "string",
                           "Type": "string"
                        }
                     ],
                     "WebAclId": "string"
                  },
                  "AwsWafRule": {
                     "MetricName": "string",
                     "Name": "string",
                     "PredicateList": [
                        {
                           "DataId": "string",
                           "Negated": boolean,
                           "Type": "string"
                        }
                     ],
                     "RuleId": "string"
                  },
                  "AwsWafRuleGroup": {
                     "MetricName": "string",
                     "Name": "string",
                     "RuleGroupId": "string",
                     "Rules": [
                        {
                           "Action": {
                              "Type": "string"
                           },
                           "Priority": number,
                           "RuleId": "string",
                           "Type": "string"
                        }
                     ]
                  },
                  "AwsWafv2RuleGroup": {
                     "Arn": "string",
                     "Capacity": number,
                     "Description": "string",
                     "Id": "string",
                     "Name": "string",
                     "Rules": [
                        {
                           "Action": {
                              "Allow": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Block": {
                                 "CustomResponse": {
                                    "CustomResponseBodyKey": "string",
                                    "ResponseCode": number,
                                    "ResponseHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Captcha": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Count": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              }
                           },
                           "Name": "string",
                           "OverrideAction": "string",
                           "Priority": number,
                           "VisibilityConfig": {
                              "CloudWatchMetricsEnabled": boolean,
                              "MetricName": "string",
                              "SampledRequestsEnabled": boolean
                           }
                        }
                     ],
                     "Scope": "string",
                     "VisibilityConfig": {
                        "CloudWatchMetricsEnabled": boolean,
                        "MetricName": "string",
                        "SampledRequestsEnabled": boolean
                     }
                  },
                  "AwsWafv2WebAcl": {
                     "Arn": "string",
                     "Capacity": number,
                     "CaptchaConfig": {
                        "ImmunityTimeProperty": {
                           "ImmunityTime": number
                        }
                     },
                     "DefaultAction": {
                        "Allow": {
                           "CustomRequestHandling": {
                              "InsertHeaders": [
                                 {
                                    "Name": "string",
                                    "Value": "string"
                                 }
                              ]
                           }
                        },
                        "Block": {
                           "CustomResponse": {
                              "CustomResponseBodyKey": "string",
                              "ResponseCode": number,
                              "ResponseHeaders": [
                                 {
                                    "Name": "string",
                                    "Value": "string"
                                 }
                              ]
                           }
                        }
                     },
                     "Description": "string",
                     "Id": "string",
                     "ManagedbyFirewallManager": boolean,
                     "Name": "string",
                     "Rules": [
                        {
                           "Action": {
                              "Allow": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Block": {
                                 "CustomResponse": {
                                    "CustomResponseBodyKey": "string",
                                    "ResponseCode": number,
                                    "ResponseHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Captcha": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              },
                              "Count": {
                                 "CustomRequestHandling": {
                                    "InsertHeaders": [
                                       {
                                          "Name": "string",
                                          "Value": "string"
                                       }
                                    ]
                                 }
                              }
                           },
                           "Name": "string",
                           "OverrideAction": "string",
                           "Priority": number,
                           "VisibilityConfig": {
                              "CloudWatchMetricsEnabled": boolean,
                              "MetricName": "string",
                              "SampledRequestsEnabled": boolean
                           }
                        }
                     ],
                     "VisibilityConfig": {
                        "CloudWatchMetricsEnabled": boolean,
                        "MetricName": "string",
                        "SampledRequestsEnabled": boolean
                     }
                  },
                  "AwsWafWebAcl": {
                     "DefaultAction": "string",
                     "Name": "string",
                     "Rules": [
                        {
                           "Action": {
                              "Type": "string"
                           },
                           "ExcludedRules": [
                              {
                                 "RuleId": "string"
                              }
                           ],
                           "OverrideAction": {
                              "Type": "string"
                           },
                           "Priority": number,
                           "RuleId": "string",
                           "Type": "string"
                        }
                     ],
                     "WebAclId": "string"
                  },
                  "AwsXrayEncryptionConfig": {
                     "KeyId": "string",
                     "Status": "string",
                     "Type": "string"
                  },
                  "AzureResource": JSON value,
                  "CodeRepository": {
                     "CodeSecurityIntegrationArn": "string",
                     "ProjectName": "string",
                     "ProviderType": "string"
                  },
                  "Container": {
                     "ContainerRuntime": "string",
                     "ImageId": "string",
                     "ImageName": "string",
                     "LaunchedAt": "string",
                     "Name": "string",
                     "Privileged": boolean,
                     "VolumeMounts": [
                        {
                           "MountPath": "string",
                           "Name": "string"
                        }
                     ]
                  },
                  "Other": {
                     "string" : "string"
                  }
               },
               "Id": "string",
               "Owner": {
                  "Account": {
                     "Id": "string"
                  },
                  "Org": {
                     "Id": "string"
                  }
               },
               "Partition": "string",
               "Provider": "string",
               "Region": "string",
               "ResourceRole": "string",
               "Tags": {
                  "string" : "string"
               },
               "Type": "string"
            }
         ],
         "Sample": boolean,
         "SchemaVersion": "string",
         "Severity": {
            "Label": "string",
            "Normalized": number,
            "Original": "string",
            "Product": number
         },
         "SourceUrl": "string",
         "ThreatIntelIndicators": [
            {
               "Category": "string",
               "LastObservedAt": "string",
               "Source": "string",
               "SourceUrl": "string",
               "Type": "string",
               "Value": "string"
            }
         ],
         "Threats": [
            {
               "FilePaths": [
                  {
                     "FileName": "string",
                     "FilePath": "string",
                     "Hash": "string",
                     "ResourceId": "string"
                  }
               ],
               "ItemCount": number,
               "Name": "string",
               "Severity": "string"
            }
         ],
         "Title": "string",
         "Types": [ "string" ],
         "UpdatedAt": "string",
         "UserDefinedFields": {
            "string" : "string"
         },
         "VerificationState": "string",
         "Vulnerabilities": [
            {
               "CodeVulnerabilities": [
                  {
                     "Cwes": [ "string" ],
                     "FilePath": {
                        "EndLine": number,
                        "FileName": "string",
                        "FilePath": "string",
                        "StartLine": number
                     },
                     "SourceArn": "string"
                  }
               ],
               "Cvss": [
                  {
                     "Adjustments": [
                        {
                           "Metric": "string",
                           "Reason": "string"
                        }
                     ],
                     "BaseScore": number,
                     "BaseVector": "string",
                     "Source": "string",
                     "Version": "string"
                  }
               ],
               "EpssScore": number,
               "ExploitAvailable": "string",
               "FixAvailable": "string",
               "Id": "string",
               "LastKnownExploitAt": "string",
               "ReferenceUrls": [ "string" ],
               "RelatedVulnerabilities": [ "string" ],
               "Vendor": {
                  "Name": "string",
                  "Url": "string",
                  "VendorCreatedAt": "string",
                  "VendorSeverity": "string",
                  "VendorUpdatedAt": "string"
               },
               "VulnerablePackages": [
                  {
                     "Architecture": "string",
                     "Epoch": "string",
                     "FilePath": "string",
                     "FixedInVersion": "string",
                     "Name": "string",
                     "PackageManager": "string",
                     "Release": "string",
                     "Remediation": "string",
                     "SourceLayerArn": "string",
                     "SourceLayerHash": "string",
                     "Version": "string"
                  }
               ]
            }
         ],
         "Workflow": {
            "Status": "string"
         },
         "WorkflowState": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Findings](#API_GetFindings_ResponseSyntax) **   <a name="securityhub-GetFindings-response-Findings"></a>
The findings that matched the filters specified in the request.
Type: Array of [AwsSecurityFinding](API_AwsSecurityFinding.md) objects

 ** [NextToken](#API_GetFindings_ResponseSyntax) **   <a name="securityhub-GetFindings-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

## Errors
<a name="API_GetFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindings)
