---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/installation-btp.html
---

# Installing AWS SDK for SAP ABAP - BTP edition
<a name="installation-btp"></a>

The BTP edition is in developer preview, and can be installed by joining the preview. To install the SDK, fill the participation form at [AWS SDK for SAP ABAP - BTP edition developer preview](https://pages.awscloud.com/Preview-AWS-SDK-for-SAP-ABAP-BTP-edition-2024-interest.html).

 Before installing SDK for SAP ABAP - BTP edition, ensure that you are meeting the required prerequisites. For more information, see [SAP Landscape Portal](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#landscape-portal) and [SAP Credential Store](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#credential-store).

**Topics**
+ [Install SDK for SAP ABAP - BTP edition](#install-btp)
+ [Modules](#modules-btp)
+ [Patching SDK for SAP ABAP - BTP edition](#patching-btp)

## Install SDK for SAP ABAP - BTP edition
<a name="install-btp"></a>

1. Go to your SAP Landscape Portal instance, and launch the **Deploy Product** fiori application.

1. In **Products**, select **`/AWS1/SDK_OMNI`** under **Partner Products**.

   *Contact Support if you do not see `/AWS1/SDK_OMNI` after being accepted in the developer preview.*

1. In **Target Version**, choose the version of SDK for SAP ABAP - BTP edition you want to install on your system.

1. In **Available Systems**, check the checkboxes for all the SIDs on which you want to install the SDK.

1. Select **Deploy**, enter the scheduling details, and select **Schedule**. You can monitor the progress in **Product Version Deployment Status**.

   The installation may take 30-45 minutes, and includes system downtime. For more details, see [Deploy Product](https://help.sap.com/docs/btp/sap-business-technology-platform/update-product-version).

## Modules
<a name="modules-btp"></a>

The following modules are included in the developer preview of AWS SDK for SAP ABAP - BTP edition.
+ [Amazon API Gateway [`agw`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/agw/index.html)
+ [Amazon Athena [`ath`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/ath/index.html)
+ [Amazon Bedrock Runtime [`bdr`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/bdr/index.html)
+ [Amazon Comprehend [`cpd`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/cpd/index.html)
+ [Amazon EventBridge [`evb`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/evb/index.html)
+ [Amazon Forecast [`fcs`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/fcs/index.html)
+ [Amazon Kinesis [`kns`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/kns/index.html)
+ [Amazon Data Firehose [`frh`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/frh/index.html)
+ [Amazon SageMaker AI [`sgm`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/sgm/index.html)
+ [Amazon Simple Notification Service [`sns`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/sns/index.html)
+ [Amazon Simple Queue Service [`sqs`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/sqs/index.html)
+ [Amazon Simple Storage Service [`s3`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/s3/index.html)
+ [AWS Systems Manager [`ssm`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/ssm/index.html)
+ [Amazon Textract [`tex`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/tex/index.html)
+ [Amazon Transcribe [`tnb`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/tnb/index.html)
+ [Amazon Translate [`xl8`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/xl8/index.html)
+ [AWS CloudTrail [`trl`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/trl/index.html)
+ [AWS IoT [`iot`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/iot/index.html)
+ [AWS KMS [`kms`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/kms/index.html)
+ [AWS Lambda [`lmd`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/lmd/index.html)
+ [AWS Secrets Manager [`smr`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/smr/index.html)
+ [AWS Security Token Service [`sts`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/sts/index.html)
+ [AWS Transfer Family [`trn`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/trn/index.html)
+ [IAM Roles Anywhere [`rla`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/rla/index.html)
+ [Amazon Redshift Data API [`rsd`]](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/rsd/index.html)

## Patching SDK for SAP ABAP - BTP edition
<a name="patching-btp"></a>

The patching process for SDK for SAP ABAP - BTP edition is similar to the installation process. If you install the SDK on a system that has an already installed older version, then the SDK is patched to your choice of new version.
