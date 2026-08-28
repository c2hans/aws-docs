---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeJob.html
---

# DescribeJob
<a name="API_DescribeJob"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns information about a specific job including shipping information, job status, and other important metadata.

## Request Syntax
<a name="API_DescribeJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeJob_RequestSyntax) **   <a name="Snowball-DescribeJob-request-JobId"></a>
The automatically generated ID for a job, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeJob_ResponseSyntax"></a>

```
{
   "JobMetadata": {
      "AddressId": "string",
      "ClusterId": "string",
      "CreationDate": number,
      "DataTransferProgress": {
         "BytesTransferred": number,
         "ObjectsTransferred": number,
         "TotalBytes": number,
         "TotalObjects": number
      },
      "Description": "string",
      "DeviceConfiguration": {
         "SnowconeDeviceConfiguration": {
            "WirelessConnection": {
               "IsWifiEnabled": boolean
            }
         }
      },
      "ForwardingAddressId": "string",
      "ImpactLevel": "string",
      "JobId": "string",
      "JobLogInfo": {
         "JobCompletionReportURI": "string",
         "JobFailureLogURI": "string",
         "JobSuccessLogURI": "string"
      },
      "JobState": "string",
      "JobType": "string",
      "KmsKeyARN": "string",
      "LongTermPricingId": "string",
      "Notification": {
         "DevicePickupSnsTopicARN": "string",
         "JobStatesToNotify": [ "string" ],
         "NotifyAll": boolean,
         "SnsTopicARN": "string"
      },
      "OnDeviceServiceConfiguration": {
         "EKSOnDeviceService": {
            "EKSAnywhereVersion": "string",
            "KubernetesVersion": "string"
         },
         "NFSOnDeviceService": {
            "StorageLimit": number,
            "StorageUnit": "string"
         },
         "S3OnDeviceService": {
            "FaultTolerance": number,
            "ServiceSize": number,
            "StorageLimit": number,
            "StorageUnit": "string"
         },
         "TGWOnDeviceService": {
            "StorageLimit": number,
            "StorageUnit": "string"
         }
      },
      "PickupDetails": {
         "DevicePickupId": "string",
         "Email": "string",
         "IdentificationExpirationDate": number,
         "IdentificationIssuingOrg": "string",
         "IdentificationNumber": "string",
         "Name": "string",
         "PhoneNumber": "string"
      },
      "RemoteManagement": "string",
      "Resources": {
         "Ec2AmiResources": [
            {
               "AmiId": "string",
               "SnowballAmiId": "string"
            }
         ],
         "LambdaResources": [
            {
               "EventTriggers": [
                  {
                     "EventResourceARN": "string"
                  }
               ],
               "LambdaArn": "string"
            }
         ],
         "S3Resources": [
            {
               "BucketArn": "string",
               "KeyRange": {
                  "BeginMarker": "string",
                  "EndMarker": "string"
               },
               "TargetOnDeviceServices": [
                  {
                     "ServiceName": "string",
                     "TransferOption": "string"
                  }
               ]
            }
         ]
      },
      "RoleARN": "string",
      "ShippingDetails": {
         "InboundShipment": {
            "Status": "string",
            "TrackingNumber": "string"
         },
         "OutboundShipment": {
            "Status": "string",
            "TrackingNumber": "string"
         },
         "ShippingOption": "string"
      },
      "SnowballCapacityPreference": "string",
      "SnowballId": "string",
      "SnowballType": "string",
      "TaxDocuments": {
         "IND": {
            "GSTIN": "string"
         }
      }
   },
   "SubJobMetadata": [
      {
         "AddressId": "string",
         "ClusterId": "string",
         "CreationDate": number,
         "DataTransferProgress": {
            "BytesTransferred": number,
            "ObjectsTransferred": number,
            "TotalBytes": number,
            "TotalObjects": number
         },
         "Description": "string",
         "DeviceConfiguration": {
            "SnowconeDeviceConfiguration": {
               "WirelessConnection": {
                  "IsWifiEnabled": boolean
               }
            }
         },
         "ForwardingAddressId": "string",
         "ImpactLevel": "string",
         "JobId": "string",
         "JobLogInfo": {
            "JobCompletionReportURI": "string",
            "JobFailureLogURI": "string",
            "JobSuccessLogURI": "string"
         },
         "JobState": "string",
         "JobType": "string",
         "KmsKeyARN": "string",
         "LongTermPricingId": "string",
         "Notification": {
            "DevicePickupSnsTopicARN": "string",
            "JobStatesToNotify": [ "string" ],
            "NotifyAll": boolean,
            "SnsTopicARN": "string"
         },
         "OnDeviceServiceConfiguration": {
            "EKSOnDeviceService": {
               "EKSAnywhereVersion": "string",
               "KubernetesVersion": "string"
            },
            "NFSOnDeviceService": {
               "StorageLimit": number,
               "StorageUnit": "string"
            },
            "S3OnDeviceService": {
               "FaultTolerance": number,
               "ServiceSize": number,
               "StorageLimit": number,
               "StorageUnit": "string"
            },
            "TGWOnDeviceService": {
               "StorageLimit": number,
               "StorageUnit": "string"
            }
         },
         "PickupDetails": {
            "DevicePickupId": "string",
            "Email": "string",
            "IdentificationExpirationDate": number,
            "IdentificationIssuingOrg": "string",
            "IdentificationNumber": "string",
            "Name": "string",
            "PhoneNumber": "string"
         },
         "RemoteManagement": "string",
         "Resources": {
            "Ec2AmiResources": [
               {
                  "AmiId": "string",
                  "SnowballAmiId": "string"
               }
            ],
            "LambdaResources": [
               {
                  "EventTriggers": [
                     {
                        "EventResourceARN": "string"
                     }
                  ],
                  "LambdaArn": "string"
               }
            ],
            "S3Resources": [
               {
                  "BucketArn": "string",
                  "KeyRange": {
                     "BeginMarker": "string",
                     "EndMarker": "string"
                  },
                  "TargetOnDeviceServices": [
                     {
                        "ServiceName": "string",
                        "TransferOption": "string"
                     }
                  ]
               }
            ]
         },
         "RoleARN": "string",
         "ShippingDetails": {
            "InboundShipment": {
               "Status": "string",
               "TrackingNumber": "string"
            },
            "OutboundShipment": {
               "Status": "string",
               "TrackingNumber": "string"
            },
            "ShippingOption": "string"
         },
         "SnowballCapacityPreference": "string",
         "SnowballId": "string",
         "SnowballType": "string",
         "TaxDocuments": {
            "IND": {
               "GSTIN": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobMetadata](#API_DescribeJob_ResponseSyntax) **   <a name="Snowball-DescribeJob-response-JobMetadata"></a>
Information about a specific job, including shipping information, job status, and other important metadata.
Type: [JobMetadata](API_JobMetadata.md) object

 ** [SubJobMetadata](#API_DescribeJob_ResponseSyntax) **   <a name="Snowball-DescribeJob-response-SubJobMetadata"></a>
Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.
Type: Array of [JobMetadata](API_JobMetadata.md) objects

## Errors
<a name="API_DescribeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/DescribeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DescribeJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
