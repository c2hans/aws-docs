---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/required-endpoints.html
---

# Required service endpoints
<a name="required-endpoints"></a>

To set up connections with the AWS services required for the AWS IoT SiteWise Edge gateway, configure endpoints for the following AWS services:
+ [AWS Identity and Access Management (IAM)](#endpoints-iam)
+ [AWS IoT Core](#endpoints-iot-core)
+ [AWS IoT Greengrass V2](#endpoints-greengrass)
+ [AWS IoT SiteWise](#endpoints-sitewise)
+ [AWS Key Management Service (AWS KMS)](#endpoints-kms)
+ [AWS Secrets Manager](#endpoints-secrets-manager)
+ [AWS Security Token Service (AWS STS)](#endpoints-sts)
+ [Amazon Simple Storage Service (Amazon S3)](#endpoints-s3)
+ [AWS Systems Manager](#endpoints-ssm)

Unless noted as *optional*, the endpoints in this section are required by the AWS IoT SiteWise Edge gateway or to adhere to AWS recommendations and security best practices. Set up and test these endpoints before creating the gateway.

|
|
| Note: Values that need to be customized for your deployment configuration are in angle brackets (`<>`). For a complete list of AWS Regions, see [AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions) in *AWS General Reference*. |
| --- |

## IAM endpoint
<a name="endpoints-iam"></a>

The following is the required service endpoint for AWS Identity and Access Management (IAM). For more information, see [IAM endpoints](https://docs.aws.amazon.com/general/latest/gr/iam-service.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| iam.amazonaws.com | 443 | TCP | Outbound | Edge device to IAM |

## AWS IoT Core endpoints
<a name="endpoints-iot-core"></a>

The following are the service endpoints for AWS IoT Core. For more information, see [AWS IoT Core endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html). In this table, `prefix` is your account-specific prefix for [AWS IoT Device Management - jobs data endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-jobs-data-plane-endpoints) (AWS IoT Core documentation).

|
|
| Destination endpoint | Port | Protocol | Direction | AWS CLI commands | Description |
| --- |--- |--- |--- |--- |--- |
| `<prefix-ats>`.iot.`<region>`.amazonaws.com | 443 | TCP | Outbound | `aws iot describe-endpoint --endpoint-type iot:Data-ATS` | Edge device to the account-specific AWS IoT data plane |
| `<prefix>`.credentials.iot.`<region>`.amazonaws.com | 443 | TCP | Outbound | `aws iot describe-endpoint --endpoint-type iot:CredentialProvider` | Edge device to authenticate AWS IoT Core calls by using a built-in [X.509 client certificate](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) |
| `<prefix>`.jobs.iot.`<region>`.amazonaws.com | 443 | TCP | Outbound | `aws iot describe-endpoint --endpoint-type iot:Jobs` | Edge device to the AWS IoT Core control plane |

## AWS IoT Greengrass V2 endpoints
<a name="endpoints-greengrass"></a>

The following are the service endpoints for AWS IoT Greengrass V2. For more information, see [AWS IoT Greengrass V2 endpoints](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| greengrass.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT Greengrass V2 control plane |
| greengrass-ats.iot.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT Greengrass data plane |

## AWS IoT SiteWise endpoints
<a name="endpoints-sitewise"></a>

The following are the service endpoints for AWS IoT SiteWise. For more information, see [AWS IoT SiteWise endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-sitewise.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| data.iotsitewise.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT SiteWise data plane |
| iotsitewise.`<region>`.amazonaws.com | 443 | TCP | Outbound | (Optional) Edge device to the AWS IoT SiteWise service plane |
| api.iotsitewise.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT SiteWise control plane |
| model.iotsitewise.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT SiteWise model control plane |
| edge.iotsitewise.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to the AWS IoT SiteWise edge API operations |

## AWS KMS endpoint
<a name="endpoints-kms"></a>

The following is the service endpoint for AWS Key Management Service (AWS KMS). For more information, see [AWS KMS endpoints](https://docs.aws.amazon.com/general/latest/gr/kms.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| kms.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to AWS KMS |

## Secrets Manager endpoint
<a name="endpoints-secrets-manager"></a>

The following is the service endpoint for AWS Secrets Manager. For more information, see [Secrets Manager endpoints](https://docs.aws.amazon.com/general/latest/gr/asm.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| secretsmanager.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to Secrets Manager |

## AWS STS endpoint
<a name="endpoints-sts"></a>

The following is the service endpoint for AWS Security Token Service (AWS STS). For more information, see [AWS STS endpoints](https://docs.aws.amazon.com/general/latest/gr/sts.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| sts.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to AWS STS |

## Amazon S3 endpoints
<a name="endpoints-s3"></a>

The following are the service endpoints for Amazon Simple Storage Service (Amazon S3). For more information, see [Amazon S3 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| s3.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to all S3 buckets in the AWS Region |
| \*.s3.amazonaws.com | 443 | TCP | Outbound | Edge device to any S3 bucket for downloading all AWS IoT Greengrass V2 [components](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html), including AWS provided components |
| \*.s3.`<region>`.amazonaws.com | 443 | TCP | Outbound | (Optional) Edge device to any S3 bucket in the AWS Region for downloading all AWS IoT Greengrass V2 [components](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html), including AWS provided components |

## Systems Manager endpoints
<a name="endpoints-ssm"></a>

The following are the service endpoints for AWS Systems Manager. For more information, see [AWS Systems Manager endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html).

|
|
| Destination endpoint | Port | Protocol | Direction | Description |
| --- |--- |--- |--- |--- |
| ssm.`<region>`.amazonaws.com | 443 | TCP | Outbound | Edge device to Systems Manager |
| ssmmessages.`<region>`.amazonaws.com | 443 | TCP | Outbound | (Optional) Edge device to Session Manager |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
